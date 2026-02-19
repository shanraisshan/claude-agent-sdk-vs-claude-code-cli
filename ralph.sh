#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR"
LOG_FILE="$PROJECT_ROOT/research/loop.log"
STATE_FILE="$PROJECT_ROOT/research/self-evolving-state.yaml"
COOLDOWN_SECONDS=30
ITERATION_TIMEOUT=1800  # 30 minutes per iteration

if [ -z "$1" ]; then
  echo "Usage: $0 <iterations>"
  echo "Example: $0 100"
  exit 1
fi

# Ensure research directory and log file exist
mkdir -p "$PROJECT_ROOT/research"
touch "$LOG_FILE"

log() {
  local msg="[$(date '+%Y-%m-%d %H:%M:%S')] $1"
  echo "$msg"
  echo "$msg" >> "$LOG_FILE"
}

log "========================================"
log "Self-Evolving Research Loop"
log "Max iterations: $1"
log "Cooldown: ${COOLDOWN_SECONDS}s | Timeout: ${ITERATION_TIMEOUT}s"
log "Log file: $LOG_FILE"
log "========================================"

for ((i=1; i<=$1; i++)); do
  log ""
  log "========== Loop $i of $1 =========="

  # --- State file validation ---
  if [ -f "$STATE_FILE" ]; then
    current_phase=$(grep '^phase:' "$STATE_FILE" | awk '{print $2}')
    current_status=$(grep '^status:' "$STATE_FILE" | awk '{print $2}')
    current_iteration=$(grep '^iteration:' "$STATE_FILE" | awk '{print $2}')
    last_score=$(grep '^lastScore:' "$STATE_FILE" | awk '{print $2}')

    log "State: iteration=$current_iteration phase=$current_phase status=$current_status score=$last_score"

    # If previous iteration left state dirty, log a warning
    if [[ "$current_phase" != "COMPLETE" && "$current_phase" != "IDLE" && "$current_status" == "IN_PROGRESS" ]]; then
      log "WARNING: Previous iteration left dirty state (phase=$current_phase, status=$current_status)"
      log "WARNING: Resetting state to allow next iteration to proceed"
      # Reset phase to COMPLETE so the next iteration can increment properly
      sed -i '' "s/^phase:.*/phase: COMPLETE/" "$STATE_FILE"
      sed -i '' "s/^status:.*/status: DIRTY_RECOVERY/" "$STATE_FILE"
    fi
  else
    log "No state file found — starting fresh"
  fi

  # --- Disk space check ---
  available_mb=$(df -m "$PROJECT_ROOT" | awk 'NR==2 {print $4}')
  if [ "$available_mb" -lt 500 ]; then
    log "ERROR: Low disk space (${available_mb}MB available). Stopping loop."
    exit 1
  fi

  # --- Run iteration with timeout ---
  log "Starting Claude session (timeout: ${ITERATION_TIMEOUT}s)..."

  # Use perl for timeout since macOS doesn't have GNU timeout
  result=$(perl -e '
    alarm $ARGV[0];
    $SIG{ALRM} = sub { kill("TERM", $pid); die "TIMEOUT" };
    $pid = open(KID, "-|", @ARGV[1..$#ARGV]) or die "Cannot fork: $!";
    local $/;
    $out = <KID>;
    close KID;
    print $out;
  ' "$ITERATION_TIMEOUT" claude --dangerously-skip-permissions -p "$(cat "$PROJECT_ROOT/prompt.md")" --output-format text 2>&1) || true

  exit_code=$?

  # Log result summary (first and last 20 lines to keep log manageable)
  result_lines=$(echo "$result" | wc -l | tr -d ' ')
  if [ "$result_lines" -gt 40 ]; then
    log "Output (${result_lines} lines, showing first/last 20):"
    echo "$result" | head -20 >> "$LOG_FILE"
    echo "... [$(($result_lines - 40)) lines omitted] ..." >> "$LOG_FILE"
    echo "$result" | tail -20 >> "$LOG_FILE"
  else
    echo "$result" >> "$LOG_FILE"
  fi

  # Check for timeout
  if [[ "$result" == *"TIMEOUT"* && -z "$(echo "$result" | grep -v TIMEOUT)" ]]; then
    log "ERROR: Iteration timed out after ${ITERATION_TIMEOUT}s"
    log "--- End of loop $i (TIMEOUT) ---"
    log "Cooling down for ${COOLDOWN_SECONDS}s..."
    sleep "$COOLDOWN_SECONDS"
    continue
  fi

  # --- Check for convergence ---
  if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
    log ""
    log "========================================"
    log "CONVERGED after loop $i!"
    log "Both agents achieved 90%+ similarity."
    log "========================================"
    exit 0
  fi

  # --- Check for continuing ---
  if [[ "$result" == *"CONTINUING_RESEARCH"* ]]; then
    new_score=$(grep '^lastScore:' "$STATE_FILE" 2>/dev/null | awk '{print $2}')
    log "Result: CONTINUING (score: ${new_score:-unknown}%)"
  else
    log "Result: Unknown output (no COMPLETE or CONTINUING marker found)"
  fi

  log "--- End of loop $i ---"

  # --- Cooldown between iterations ---
  if [ "$i" -lt "$1" ]; then
    log "Cooling down for ${COOLDOWN_SECONDS}s..."
    sleep "$COOLDOWN_SECONDS"
  fi
done

log ""
log "Reached max iterations ($1) without convergence."
exit 1
