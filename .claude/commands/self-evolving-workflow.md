# Self-Evolving Workflow

You are the top-level orchestrator for a self-evolving system. Your goal is to **evolve the Claude Agent SDK (FastAPI app)** until it produces the same output as the Claude Code CLI agent.

**Key principle:** The CLI output is the **ground truth** (100% correct). You NEVER modify CLI agent files. The self-evolving process ONLY modifies the SDK code (`claude-agent-sdk/agent.py`, `claude-agent-sdk/main.py`) to improve its output until it matches the CLI output at 90%+ similarity.

**No fallbacks:** If the SDK FastAPI app fails, you must **fix the code** — never mock it with a subagent.

---

## PHASE 1: INITIALIZE

1. Read `research/research-workflow-state.yaml` to get the current iteration number
2. Increment the iteration: `iteration = previous_iteration + 1`
3. Create iteration directories: `mkdir -p research/research-{iteration}/claude-code-cli research/research-{iteration}/claude-agent-sdk`
4. Update `research/research-workflow-state.yaml`:
   ```yaml
   iteration: {iteration}
   phase: GENERATE_CLI
   status: IN_PROGRESS
   lastScore: {previous score or 0}
   lastUpdated: {current ISO timestamp}
   ```

---

## PHASE 2: GENERATE CLI RESEARCH (Ground Truth)

Execute the `/research-claude-code-cli` logic:

1. Read `problem-statement/problem-statement.md` for the research problem
2. Read `.claude/agents/claude-code-cli-games-revenue-researcher.md` for agent instructions
3. Spawn a subagent (subagent_type: "general-purpose") to do the CLI research:
   - Tell it: "You are the CLI Research Agent. Your iteration number is {iteration}."
   - Include full contents of `problem-statement/problem-statement.md` and code-cli-researcher.md
   - Tell it to use Reddit MCP tools ONLY
   - Tell it to write TWO files:
     1. `research/research-{iteration}/claude-code-cli/reddit-data-{iteration}.md`
     2. `research/research-{iteration}/claude-code-cli/research-{iteration}.md`
4. Wait for completion and verify both files exist
5. Commit CLI research:
   ```
   git add research/research-{iteration}/claude-code-cli/
   git commit -m "cli-research({iteration}): ground truth research complete"
   ```

---

## PHASE 3: GENERATE SDK RESEARCH

**The SDK FastAPI app MUST work. If it fails, fix the code.**

1. Hit the SDK FastAPI endpoint:
   ```
   curl -s -w "\n%{http_code}" http://localhost:8000/research-claude-agent-sdk -X POST -H "Content-Type: application/json" -d '{"iteration": {iteration}}'
   ```
2. **If the SDK app responds successfully (HTTP 200):**
   - Verify output was written to:
     - `research/research-{iteration}/claude-agent-sdk/research-{iteration}.md`
     - `research/research-{iteration}/claude-agent-sdk/reddit-data-{iteration}.md`
   - If files exist, proceed to Phase 4

3. **If the SDK app FAILS (connection refused, HTTP 500, timeout, or missing output files):**
   - **DO NOT mock or use a fallback subagent**
   - Capture the error message/response
   - Read the current SDK code:
     - `claude-agent-sdk/main.py`
     - `claude-agent-sdk/agent.py`
   - Analyze the error and **fix the code** by editing `main.py` and/or `agent.py`
   - Commit the fix:
     ```
     git add claude-agent-sdk/
     git commit -m "sdk-fix({iteration}): fixed SDK error - {brief description}"
     ```
   - **Retry the curl request** (up to 3 attempts)
   - If still failing after 3 fix attempts, log the error in state and output `CONTINUING_RESEARCH`

4. Commit SDK research output:
   ```
   git add research/research-{iteration}/claude-agent-sdk/
   git commit -m "sdk-research({iteration}): SDK agent research complete"
   ```

---

## PHASE 4: COMPARE

Execute the `/compare-research` logic:

1. Read `.claude/agents/research-compare.md` for comparison instructions
2. Spawn a comparator subagent (subagent_type: "general-purpose"):
   - Tell it: "You are the Research Comparator. Compare iteration {iteration} outputs. The CLI output is the ground truth — measure how close the SDK output is to it."
   - Include full research-compare.md instructions
   - Tell it to read both research files and write comparison to `research/research-{iteration}/comparison-{iteration}.md`
3. Wait for completion
4. Read the comparison report and parse the similarity score from the JSON block
5. Commit comparison:
   ```
   git add research/research-{iteration}/comparison-{iteration}.md
   git commit -m "comparison({iteration}): similarity={score}%"
   ```

---

## PHASE 5: EVALUATE & EVOLVE SDK

1. **If similarity >= 90:**
   - Set `status: CONVERGED`, `converged: true`
   - Skip to Phase 6

2. **If similarity < 90:**
   - Set `status: CONTINUING`, `converged: false`
   - **Evolve the SDK code** (NOT the CLI agent — CLI is ground truth):
     a. Read the comparison report for discrepancies (missing items, value differences)
     b. Read the current SDK code:
        - `claude-agent-sdk/agent.py`
        - `claude-agent-sdk/main.py`
     c. Read `.claude/agents/claude-code-cli-games-revenue-researcher.md` to understand how the CLI agent works
     d. **Modify the SDK code** to address the discrepancies:
        - If the SDK is missing items → improve the search queries or prompt in `agent.py`
        - If values are off → adjust the system prompt guidance in `agent.py`
        - If the SDK agent structure differs from CLI → align `agent.py` to use similar logic/prompts as code-cli-researcher.md
     e. Write/update `research/sdk-evolution-log.md` documenting what was changed and why:
        ```
        ### Iteration {n} Evolution (Score: {score}%)
        - Discrepancies found: {summary}
        - Changes made to agent.py: {description}
        - Changes made to main.py: {description if any}
        ```
     f. Commit SDK evolution:
        ```
        git add claude-agent-sdk/ research/sdk-evolution-log.md
        git commit -m "evolve({iteration}): SDK evolved - {brief description of changes}"
        ```

---

## PHASE 6: UPDATE STATE & REPORT

1. Append this iteration to `research/research-iterations.yaml`:
   ```yaml
   - iteration: {n}
     score: {similarity}
     status: {CONVERGED|CONTINUING}
     timestamp: {current ISO timestamp}
   ```
2. Update `research/research-status.json`:
   ```json
   {
     "iteration": {n},
     "status": "{CONVERGED|CONTINUING}",
     "similarityScore": {score},
     "converged": {true|false}
   }
   ```
3. Update `research/research-workflow-state.yaml`:
   ```yaml
   iteration: {n}
   phase: COMPLETE
   status: {CONVERGED|CONTINUING}
   lastScore: {score}
   lastUpdated: {ISO timestamp}
   ```
4. Commit state:
   ```
   git add research/research-workflow-state.yaml research/research-iterations.yaml research/research-status.json
   git commit -m "state({iteration}): {CONVERGED|CONTINUING} similarity={score}%"
   ```
5. Output the final status:
   - If converged: Output `<promise>COMPLETE</promise>`
   - If not converged: Output `CONTINUING_RESEARCH`

---

## Critical Rules

- **CLI output is ground truth** — NEVER modify `.claude/agents/claude-code-cli-games-revenue-researcher.md` or CLI output files
- **SDK evolves** — the self-evolving process modifies `claude-agent-sdk/agent.py` and `claude-agent-sdk/main.py`
- **No fallbacks** — if the SDK API fails, fix the code; never mock with a subagent
- The SDK should ideally use the same agent definition (code-cli-researcher.md) and produce output in the same format as the CLI
- Always read state before starting — pick up where the last iteration left off
- If any phase fails, log the error in state and output `CONTINUING_RESEARCH`
- Never modify `problem-statement/problem-statement.md`
- Always write outputs before committing
- The iteration number must always increment from the previous one
- JSON output blocks must be valid parseable JSON
