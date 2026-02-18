#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR"

if [ -z "$1" ]; then
  echo "Usage: $0 <iterations>"
  echo "Example: $0 100"
  exit 1
fi

echo "========================================"
echo "FIFA Research Self-Evolving Loop"
echo "Max iterations: $1"
echo "========================================"
echo ""

for ((i=1; i<=$1; i++)); do
  echo "========== Iteration $i =========="
  echo "$(date)"
  echo "--------------------------------"

  result=$(claude -p "$(cat "$PROJECT_ROOT/prompt.md")" --output-format text 2>&1) || true

  echo "$result"

  if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
    echo ""
    echo "========================================"
    echo "CONVERGED after $i iterations!"
    echo "Both agents achieved 90%+ similarity."
    echo "========================================"
    exit 0
  fi

  echo ""
  echo "--- End of iteration $i ---"
  echo ""
done

echo "Reached max iterations ($1) without convergence."
exit 1
