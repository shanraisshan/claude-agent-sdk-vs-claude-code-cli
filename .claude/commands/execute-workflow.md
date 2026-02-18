# Execute Workflow — Self-Evolving FIFA Research

You are the orchestrator for a self-evolving dual-agent research system. Execute all 7 phases below **in order**, updating state files as you go.

---

## PHASE 1: INITIALIZE

1. Read `research/research-workflow-state.yaml` to get the current iteration number
2. Increment the iteration: `iteration = previous_iteration + 1`
3. Update state to: `phase: GENERATE_CLI, status: IN_PROGRESS`
4. Write updated state back to `research/research-workflow-state.yaml`

---

## PHASE 2: GENERATE CLI RESEARCH

1. Read `.claude/agents/opus-cli-researcher.md` to understand the research agent instructions
2. Use the Task tool to spawn a subagent (subagent_type: "general-purpose") with these instructions:
   - Tell it: "You are the FIFA CLI Research Agent. Your iteration number is {iteration}."
   - Include the full contents of the opus-cli-researcher.md instructions
   - Tell it to use Tavily MCP and Reddit MCP tools to research FIFA/EA FC games
   - Tell it to write output to `claude-code-cli/research-{iteration}-output.md`
   - The output must contain a markdown summary AND a JSON code block with the ResearchOutput schema
3. Wait for the subagent to complete
4. Verify the output file exists at `claude-code-cli/research-{iteration}-output.md`
5. Update state: `phase: GENERATE_SDK`

---

## PHASE 3: GENERATE SDK RESEARCH

1. Check if the SDK app is running by making a request:
   ```
   curl -s http://localhost:3000/api/research -X POST -H "Content-Type: application/json" -d '{"iteration": {iteration}}'
   ```
2. If the SDK app responds, read the response and verify output was written to `claude-agent-sdk/research-{iteration}-output.md`
3. If the SDK app is NOT running (connection refused), create the SDK output manually:
   - Use the Task tool to spawn a subagent (subagent_type: "general-purpose") with research instructions similar to the CLI agent but framed as the SDK agent
   - Tell it to use web search tools to find FIFA/EA FC game data
   - Tell it to write output to `claude-agent-sdk/research-{iteration}-output.md`
4. Update state: `phase: COMPARE`

---

## PHASE 4: COMPARE

1. Read `.claude/agents/opus-comparator.md` for comparison instructions
2. Use the Task tool to spawn a comparator subagent (subagent_type: "general-purpose"):
   - Tell it: "You are the FIFA Research Comparator. Compare iteration {iteration} outputs."
   - Include the full opus-comparator.md instructions
   - Tell it to read both output files and write comparison to `research/comparison-{iteration}.md`
3. Wait for completion
4. Read `research/comparison-{iteration}.md` and parse the similarity score from the JSON block
5. Update state: `phase: EVALUATE`

---

## PHASE 5: EVALUATE

1. Check the similarity score from the comparison report
2. If similarity >= 90:
   - Set `status: CONVERGED`
   - Set `converged: true`
3. If similarity < 90:
   - Set `status: CONTINUING`
   - Set `converged: false`
4. Update `research/research-workflow-state.yaml` with the score and status
5. Append this iteration to `research/research-iterations.yaml`:
   ```yaml
   - iteration: {n}
     score: {similarity}
     status: {CONVERGED|CONTINUING}
     timestamp: {current ISO timestamp}
   ```
6. Update state: `phase: UPDATE_AGENTS`

---

## PHASE 6: UPDATE AGENTS (skip if converged)

If NOT converged:
1. Read the comparison report for discrepancies (missing games, revenue differences)
2. Append findings to `.claude/agents/opus-cli-researcher.md` under the "Findings Log" section:
   ```
   ### Iteration {n} Findings (Score: {score}%)
   - Missing games: {list}
   - Revenue discrepancies: {list with expected corrections}
   - Action: Search for these specific games/revenue figures next iteration
   ```
3. Write/update `research/sdk-evolution-hints.md` with the same discrepancy data so the SDK agent can use it next iteration
4. Update state: `phase: COMMIT`

If converged, skip to COMMIT.

---

## PHASE 7: COMMIT

1. Stage all changed files:
   ```
   git add claude-code-cli/ claude-agent-sdk/ research/ .claude/agents/ shared/
   ```
2. Commit with message:
   ```
   research({iteration}): {CONVERGED|CONTINUING} similarity={score}%
   ```
3. Update state: `phase: REPORT`

---

## PHASE 8: REPORT

1. Update `research/research-status.json`:
   ```json
   {
     "iteration": {n},
     "status": "{CONVERGED|CONTINUING}",
     "similarityScore": {score},
     "converged": {true|false}
   }
   ```
2. Update `research/research-workflow-state.yaml`:
   ```yaml
   iteration: {n}
   phase: COMPLETE
   status: {CONVERGED|CONTINUING}
   lastScore: {score}
   lastUpdated: {ISO timestamp}
   ```
3. Output the final status:
   - If converged: Output `<promise>COMPLETE</promise>`
   - If not converged: Output `CONTINUING_RESEARCH`

---

## Critical Rules

- Always read state before starting — pick up where the last iteration left off
- If any phase fails, log the error in the state file and output `CONTINUING_RESEARCH`
- Never modify the core research goal
- Always write outputs before committing
- The iteration number must always increment from the previous one
- JSON output blocks in research files must be valid parseable JSON
