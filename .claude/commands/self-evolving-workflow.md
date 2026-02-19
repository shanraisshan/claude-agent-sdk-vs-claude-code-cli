# Self-Evolving Workflow

You are a thin orchestrator for a self-evolving system. Your ONLY jobs are: manage state, delegate to sub-commands, call the SDK API, evaluate results, and evolve the SDK code if needed.

**Key principle:** You do NOT contain any research or comparison logic. You delegate those to `/research-claude-code-cli` and `/compare-research`. If something fails, it fails — no fallbacks.

---

## PHASE 1: INITIALIZE STATE

1. Read `research/self-evolving-state.yaml` to get the current iteration
2. Increment: `iteration = previous_iteration + 1`
3. Update `research/self-evolving-state.yaml`:
   ```yaml
   iteration: {iteration}
   phase: GENERATE_CLI
   status: IN_PROGRESS
   lastScore: {previous score or 0}
   lastUpdated: {current ISO timestamp}
   ```

---

## PHASE 2: DELEGATE CLI RESEARCH

Spawn a subagent (subagent_type: "general-purpose") with this prompt:

> Read the file `.claude/commands/research-claude-code-cli.md` in full, then follow its instructions exactly and completely. The current iteration number is already set in `research/self-evolving-state.yaml` — use that. Do not modify the state file.

Wait for the subagent to complete. Its output should contain `CLI_RESEARCH_COMPLETE`.
If it does not, this phase has failed — stop and output `CONTINUING_RESEARCH`.

---

## PHASE 3: SDK RESEARCH

1. Hit the SDK FastAPI endpoint:
   ```
   curl -s -w "\n%{http_code}" http://localhost:8000/research-claude-agent-sdk -X POST -H "Content-Type: application/json" -d '{"iteration": {iteration}}'
   ```
2. If HTTP 200: verify output files exist at `research/research-{iteration}/claude-agent-sdk/`
3. If the SDK fails (connection refused, HTTP 500, timeout, missing output files):
   - Read `claude-agent-sdk/main.py` and `claude-agent-sdk/agent.py`
   - Analyze the error and fix the code
   - Commit the fix: `git commit -m "sdk-fix({iteration}): {brief description}"`
   - Retry the curl request (up to 3 attempts total)
   - If still failing after 3 attempts, stop and output `CONTINUING_RESEARCH`
4. Commit SDK output: `git add research/research-{iteration}/claude-agent-sdk/ && git commit -m "sdk-research({iteration}): SDK agent research complete"`

---

## PHASE 4: DELEGATE COMPARISON

Spawn a subagent (subagent_type: "general-purpose") with this prompt:

> Read the file `.claude/commands/compare-research.md` in full, then follow its instructions exactly and completely. The current iteration number is already set in `research/self-evolving-state.yaml` — use that.

Wait for the subagent to complete. Parse the similarity score from:
```
COMPARISON_COMPLETE iteration={n} similarity={score}%
```
If the output contains `COMPARE_ERROR`, this phase has failed — stop and output `CONTINUING_RESEARCH`.

---

## PHASE 5: EVALUATE & EVOLVE SDK

1. **If similarity >= 90:** set `converged = true`, skip to Phase 6.

2. **If similarity < 90:** set `converged = false`, then evolve:
   a. Read `research/research-{iteration}/comparison-{iteration}.md` for discrepancies
   b. Read `claude-agent-sdk/agent.py` and `claude-agent-sdk/main.py`
   c. Read `.claude/agents/claude-code-cli-games-revenue-researcher.md` to understand CLI approach
   d. Modify SDK code to address discrepancies (improve prompts, queries, output formatting)
   e. Update `research/sdk-evolution-log.md`:
      ```
      ### Iteration {n} Evolution (Score: {score}%)
      - Discrepancies: {summary}
      - Changes to agent.py: {description}
      - Changes to main.py: {description if any}
      ```
   f. Commit: `git add claude-agent-sdk/ research/sdk-evolution-log.md && git commit -m "evolve({iteration}): {brief description}"`

---

## PHASE 6: UPDATE STATE & REPORT

1. Append to `research/research-iterations.yaml`:
   ```yaml
   - iteration: {n}
     score: {similarity}
     status: {CONVERGED|CONTINUING}
     timestamp: {ISO timestamp}
   ```
2. Update `research/research-status.json`:
   ```json
   {"iteration": {n}, "status": "{CONVERGED|CONTINUING}", "similarityScore": {score}, "converged": {true|false}}
   ```
3. Update `research/self-evolving-state.yaml`:
   ```yaml
   iteration: {n}
   phase: COMPLETE
   status: {CONVERGED|CONTINUING}
   lastScore: {score}
   lastUpdated: {ISO timestamp}
   ```
4. Commit state:
   ```
   git add research/self-evolving-state.yaml research/research-iterations.yaml research/research-status.json
   git commit -m "state({iteration}): {CONVERGED|CONTINUING} similarity={score}%"
   ```
5. Output:
   - If converged: `<promise>COMPLETE</promise>`
   - If not converged: `CONTINUING_RESEARCH`

---

## Critical Rules

- **Delegate, don't duplicate** — CLI research logic lives in `/research-claude-code-cli`, comparison logic lives in `/compare-research`. Never inline their logic here.
- **CLI output is ground truth** — never modify CLI agent files or CLI output
- **SDK evolves** — only `claude-agent-sdk/agent.py` and `claude-agent-sdk/main.py` are modified
- **No fallbacks** — if the SDK API fails, fix the code or stop. Never mock with a subagent.
- Never modify `problem-statement/problem-statement.json`
- The iteration number must always increment from the previous one
