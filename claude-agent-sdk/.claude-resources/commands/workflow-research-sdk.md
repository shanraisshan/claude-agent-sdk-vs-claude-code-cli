# Research Claude Agent SDK

You are the CLI research orchestrator (SDK version). You follow the exact same workflow as the CLI /workflow-research-cli command.

---

## STEP 1: SPAWN THE REDDIT RESEARCH AGENT

Use the Task tool to spawn the reddit-game-research-agent subagent with this prompt:

> You are the Reddit Research Agent. Your iteration number is {iteration}.
> Research the following: Find all {game} games released OR actively sold from {start_year} to {end_year}, and find how many copies each title sold (physical + digital sales only, no in-app purchases). Include titles released just before {start_year} if they were still actively sold during {start_year} (e.g. a game released late in the prior year that was the current title into {start_year}). Also include the latest title released in {end_year} even if it's very recent — search specifically for it.
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
- **Always include the latest franchise title released in end_year**, even if it launched recently and is still accumulating sales. For annual sports franchises, the game released in the end_year MUST appear in the output. If the end_year is 2025, include the 2025 title (e.g. EA Sports FC 26). Search specifically for it.
- "Players" reported by EA ≠ copies sold. EA counts EA Play, Game Pass, PS Plus trial users as "players." Actual purchasers are typically 75-80% of reported player counts for mainstream annual franchise titles. **IMPORTANT**: The 75-80% conversion already represents full lifecycle sales — do NOT add an additional "lifecycle bump" of 10-15% on top. For example, if EA reports 14.5M players, use 14.5M × 0.76 ≈ 11M copies as the FINAL estimate. Do not then multiply by 1.1-1.15.
- **World Cup / major event boost**: When a title coincides with a FIFA World Cup year (e.g. FIFA 23 with Qatar 2022 World Cup), its sales are significantly boosted above the franchise average. Estimate 20-25% above the typical annual franchise baseline (~10.8M average for modern FIFA titles). For FIFA 23, this means ~13-14M copies, not 10-11M.
- **Underperformance rule**: When a title is described as "underperforming" with EA slashing fiscal year forecasts by $500M+, losing $6B+ in market value, or being discounted 50% within 2 months, estimate copies sold at **70-80% of the previous year's title** (NOT just 5% less). A ~5% decline in European GSD data does not capture the global picture — EA's severity (cutting guidance ~$600M, losing $6B market cap) indicates a 20-30% drop in copies vs prior year. **IMPORTANT**: Use the CORRECT prior-year copies as the base. If the prior year was ~11M copies, then 70-73% of 11M = ~8M, not 9.5M. Always calculate from the actual prior-year estimate, not an inflated one.
- For games still in their active sales window (< 6 months since launch), **estimate the full annual lifecycle total, NOT just copies sold to date**. Annual sports franchises sell ~85-90% of their lifetime copies in the first 12 months. Project the full-year trajectory based on the franchise trend and any recovery signals. A sequel showing "slight recovery" or "modest improvement" over a severely underperforming predecessor should be estimated 15-20% above that predecessor's full-year total (e.g., if predecessor sold 8M, estimate 9-10M for the recovery title). Do NOT cap the estimate at 5-month sales only.
- Average retail price: default to $70 for all modern FIFA/FC titles (2023+). The primary sales volume is on current-gen consoles (PS5/Xbox Series X) at $70. Only use a lower blended average ($60) for titles released before 2023 when the $60 price point was standard.
- totalGamesFound should count only premium paid titles included in the games array.
