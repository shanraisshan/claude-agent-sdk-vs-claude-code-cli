# Research Claude Code CLI

You are the CLI research agent orchestrator. Your ONLY job is to generate research output using the Claude Code CLI agent. The output you produce is the **ground truth** — it is considered 100% correct and will never be modified by the self-evolving process.

---

## STEP 1: READ PROBLEM & STATE

1. Read `problem-statement/problem-statement.json` to load the research problem definition (JSON with keys: `game`, `start_year`, `end_year`)
2. Read `research/self-evolving-state.yaml` to get the current iteration number
3. Determine the iteration: use the current iteration from state (it should already be set by the self-evolving-workflow orchestrator). If state shows iteration 0 or IDLE, use iteration 1.
4. Create the output directory: `mkdir -p research/research-{iteration}/claude-code-cli`

---

## STEP 2: GENERATE CLI RESEARCH

1. Read `problem-statement/problem-statement.json` for the research problem (parse JSON: `game`, `start_year`, `end_year`)
2. Read `.claude/agents/claude-code-cli-games-revenue-researcher.md` for the agent instructions
3. Use the Task tool to spawn a subagent (subagent_type: "general-purpose") with these instructions:
   - Tell it: "You are the CLI Research Agent. Your iteration number is {iteration}."
   - Include the parsed problem: "Calculate the revenue of all the {game} games released from {start_year} to {end_year}."
   - Include the **full contents** of code-cli-researcher.md instructions
   - Tell it to use Reddit MCP tools ONLY (NO Tavily or other web search)
   - Tell it to write TWO files:
     1. `research/research-{iteration}/claude-code-cli/reddit-data-{iteration}.md` — raw Reddit data
     2. `research/research-{iteration}/claude-code-cli/research-{iteration}.md` — synthesized research with JSON block
   - The research output must contain a markdown summary AND a JSON code block with the ResearchOutput schema from the agent instructions
4. Wait for the subagent to complete
5. Verify both output files exist

---

## STEP 3: COMMIT CLI RESEARCH

1. Stage the CLI research files:
   ```
   git add research/research-{iteration}/claude-code-cli/
   ```
2. Commit with message:
   ```
   cli-research({iteration}): CLI agent research complete (ground truth)
   ```

---

## STEP 4: REPORT

Output: `CLI_RESEARCH_COMPLETE iteration={iteration}`

---

## Critical Rules

- Read `problem-statement/problem-statement.json` — the research problem is defined there as JSON (`game`, `start_year`, `end_year`), not hardcoded
- The CLI output is **ground truth** — it is always considered correct
- Do NOT trigger the SDK agent or run comparisons — that is handled by other commands
- Do NOT modify `research/self-evolving-state.yaml` — the self-evolving-workflow manages state
- Always write outputs before committing
- JSON output blocks in research files must be valid parseable JSON
- The agent must produce TWO files: reddit-data and research
