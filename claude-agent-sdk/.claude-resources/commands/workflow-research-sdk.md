# Research Claude Agent SDK

You are the CLI research orchestrator (SDK version). You follow the exact same workflow as the CLI /workflow-research-cli command.

---

## STEP 1: SPAWN THE REDDIT RESEARCH AGENT

Use the Task tool to spawn the reddit-game-research-agent subagent with this prompt:

> You are the Reddit Research Agent. Your iteration number is {iteration}.
> Research the following: Find all {game} games released OR actively sold from {start_year} to {end_year}, and find how many copies each title sold (physical + digital sales only, no in-app purchases). Include titles released just before {start_year} if they were still actively sold during {start_year} (e.g. a game released late in the prior year that was the current title into {start_year}).
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
- Only include premium paid games in the games list. Do NOT include free-to-play mobile titles (e.g. FIFA Mobile, EA Sports FC Mobile) — they have no copy sales.
- Include games that were **actively sold** during the year range, not just games released in that range. A game released in the year before start_year counts if it was the current franchise title into start_year (e.g. FIFA 23 released Sept 2022 was the active title through Sept 2023).
- "Players" reported by EA ≠ copies sold. EA counts EA Play, Game Pass, PS Plus trial users as "players." Actual purchasers are typically 75-80% of reported player counts for mainstream annual franchise titles.
- When a title is described as "underperforming" with EA slashing forecasts, losing billions in market value, or being discounted 50% within 2 months, use the LOWER end of estimate ranges.
- For games still in their active sales window (< 6 months since launch), estimate based on franchise trajectory and comparable prior-year titles. A sequel that shows "slight recovery" or "modest improvement" over a predecessor should be estimated slightly above that predecessor, not dramatically below.
- Average retail price: default to $70 for all modern FIFA/FC titles (2023+). The primary sales volume is on current-gen consoles (PS5/Xbox Series X) at $70. Only use a lower blended average ($60) for titles released before 2023 when the $60 price point was standard.
- totalGamesFound should count only premium paid titles included in the games array.
