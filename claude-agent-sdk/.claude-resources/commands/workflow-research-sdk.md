# Research Claude Agent SDK

You are the CLI research orchestrator (SDK version). You follow the exact same workflow as the CLI /workflow-research-cli command.

---

## STEP 1: SPAWN THE REDDIT RESEARCH AGENT

Use the Task tool to spawn the reddit-game-research-agent subagent with this prompt:

> You are the Reddit Research Agent. Your iteration number is {iteration}.
> Research the following: Find all {game} games released from {start_year} to {end_year}, and find how many copies each title sold (physical + digital sales only, no in-app purchases).
> Write your output to: research/research-{iteration}/claude-agent-sdk/reddit-data-{iteration}.md

Wait for the subagent to complete.

---

## STEP 2: SYNTHESIZE RESEARCH REPORT

Read research/research-{iteration}/claude-agent-sdk/reddit-data-{iteration}.md (the raw Reddit data).
Using the data, build a final research report and write it to research/research-{iteration}/claude-agent-sdk/research-{iteration}.md

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

## STEP 3: REPORT

Output: `SDK_RESEARCH_COMPLETE iteration={iteration}`

---

## Rules

- Revenue = copy sales only (physical + digital). No microtransactions, DLC, or in-app purchases.
