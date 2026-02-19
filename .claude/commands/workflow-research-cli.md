# Research Claude Code CLI

You are the CLI research orchestrator. You read the problem, spawn the Reddit research agent to gather raw data, then synthesize the data into a final research report.

---

## STEP 1: READ STATE & PROBLEM

1. Read `research/self-evolving-state.yaml` to get the current iteration number. If iteration is 0 or IDLE, use iteration 1.
2. Read `problem-statement/problem-statement.json` to get the research problem (JSON with keys: `game`, `start_year`, `end_year`).
3. Create the output directory: `mkdir -p research/research-{iteration}/claude-code-cli`

---

## STEP 2: SPAWN THE REDDIT RESEARCH AGENT

Use the Task tool to spawn a subagent (subagent_type: `reddit-game-research-agent`) with this prompt:

> You are the Reddit Research Agent. Your iteration number is {iteration}.
> Research the following: Find all {game} games released from {start_year} to {end_year}, and find how many copies each title sold (physical + digital sales only, no in-app purchases).
> Write your output to: research/research-{iteration}/claude-code-cli/reddit-data-{iteration}.md

Wait for the subagent to complete. Verify `research/research-{iteration}/claude-code-cli/reddit-data-{iteration}.md` exists.

---

## STEP 3: SYNTHESIZE RESEARCH REPORT

1. Read `research/research-{iteration}/claude-code-cli/reddit-data-{iteration}.md` (the raw Reddit data)
2. Using the data, build a final research report and write it to `research/research-{iteration}/claude-code-cli/research-{iteration}.md`

The research report must contain:

**A. Revenue Table**

Calculate revenue as: copies sold x average retail price at time of release. Only count copy sales (physical + digital). Do NOT include microtransactions, DLC, loot boxes, or in-app purchases.

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | ... | ... | ... | ... | ... |
| **TOTAL** | | | | **$X.XX B** | |

**B. JSON Data Block**

```json
{
  "games": [
    {
      "name": "string",
      "year": "number",
      "platform": "string",
      "publisher": "string",
      "copiesSold": "number",
      "estimatedRevenue": "number (USD)",
      "revenueSource": "string (Reddit source summary)",
      "confidence": "low | medium | high"
    }
  ],
  "totalRevenue": "number (USD)",
  "totalGamesFound": "number",
  "searchQueries": ["array of search queries used"],
  "redditPostsAnalyzed": "number"
}
```

---

## STEP 4: REPORT

Output: `CLI_RESEARCH_COMPLETE iteration={iteration}`

---

## Rules

- Revenue = copy sales only (physical + digital). No microtransactions, DLC, or in-app purchases.
- Do NOT modify `research/self-evolving-state.yaml` — the workflow-self-evolving-loop manages state
