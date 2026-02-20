# Research Report: FIFA / EA Sports FC Game Sales (2023–2025)
## Iteration 14 — Claude Agent SDK

**Date**: 2026-02-20
**Scope**: All FIFA/EA Sports FC titles released from 2023 to 2025 (inclusive)
**Revenue Basis**: Physical + digital copy sales only (no microtransactions, DLC, loot boxes, or in-app purchases)

---

## Executive Summary

EA rebranded the FIFA franchise to **EA Sports FC** beginning with FC 24 (September 2023). Three titles were released in the 2023–2025 window: FC 24, FC 25, and FC 26. EA does **not** publicly disclose unit/copy sales figures for its FC titles — instead reporting "players" (which includes EA Play subscribers, free trial users, PS Plus giveaway recipients, and demo users). All copy-sales estimates below are derived from Reddit-sourced financial data, chart performance, discounting patterns, and historical franchise benchmarks. Confidence is **low** across the board due to EA's deliberate opacity on this metric.

The franchise showed a clear downward trajectory: FC 24 performed in line with historical norms, FC 25 was a significant underperformance that cost EA $6 billion in market cap, and FC 26 showed continued weakness at launch.

---

## A. Revenue Table

Revenue = copies sold × $65 blended average retail price. Only physical + digital copy sales counted. **No microtransactions, DLC, loot boxes, FUT packs, or in-app purchases included.**

The $65 blended average accounts for: current-gen pricing ($69.99), last-gen pricing ($59.99), regional/emerging-market pricing, and lifecycle discounts. All three FC titles reached 50% off within 6–8 weeks of launch as a deliberate franchise strategy to grow the FUT player base — this discounting pattern is baked into the blended average.

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | ~10.5 million | ~$682,500,000 | Medium |
| 2 | EA Sports FC 25 | 2024 | ~7.0 million | ~$455,000,000 | Low |
| 3 | EA Sports FC 26 | 2025 | ~6.0 million | ~$390,000,000 | Low |
| **TOTAL** | | | **~23.5 million** | **~$1.53 B** | |

### Copy Sales Estimation Methodology

**EA Sports FC 24 (~10.5M copies)**:
- EA raised stock profit projections in November 2023, indicating FC 24 met or exceeded expectations
- No underperformance signals found in any Reddit discussion
- Historical FIFA franchise annual copy sales range: 6–15 million
- Normal discounting pattern (50% off by ~6 weeks; PS Plus free by May 2024) is consistent with the franchise's long-standing approach of prioritizing Ultimate Team microtransaction revenue over copy price
- Estimated in the mid-range of historical norms

**EA Sports FC 25 (~7.0M copies)**:
- **Confirmed significant underperformance** across multiple high-engagement Reddit threads:
  - EA lost $6 billion in market cap, with FC 25 cited as the primary driver (r/Games, 1,957 upvotes)
  - EA slashed its full fiscal year forecast citing FC 25 weakness (r/pcgaming, 1,011 upvotes)
  - EA Q3 FY25 revenue fell to $1.88B vs. $1.94B year-earlier (r/Games, 261 upvotes)
  - Bloomberg reported bookings "slid on weakness in soccer" (r/Games, 207 upvotes)
- Worst user-rated game in franchise history across Metacritic, Google, and Steam (r/EASportsFC, 623 upvotes)
- Pre-launch beta sentiment was overwhelmingly negative, with many players indicating they would skip FC 25
- Half price within ~7 weeks; added to Xbox Game Pass within ~9 months
- Not in US Circana top 20 by February 2025 (~5 months post-launch)
- Estimated ~33% decline from FC 24, consistent with "significant underperformance" language and $6B market cap loss

**EA Sports FC 26 (~6.0M copies)**:
- **Lifecycle ongoing** — only ~5 months since September 2025 launch as of this report
- Weak launch signals from multiple tracking sources:
  - Beaten by Ghost of Yotei in UK physical launch sales (r/gaming, 1,243 upvotes) — historically unprecedented for FIFA/FC in the UK
  - Beaten by Battlefield 6 in European premium launch sales (GSD data; r/gaming, 893 upvotes)
  - NOT the #1 game in US Circana data for September 2025 (Borderlands 4 was)
  - NOT in Circana's 2025 year-to-date US best-sellers list as of October data
- Required deep discounting: 20–25% off within 2–3 weeks, 50% off by Black Friday
- Topped European Black Friday charts, but only at 50% discount
- Estimate reflects ~5 months of sales; lifetime total may reach 7–8M copies

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 10500000,
      "estimatedRevenue": 682500000,
      "revenueSource": "Reddit: EA raised stock projections Nov 2023 (r/EASportsFC, 328 score); no underperformance signals; 50% off by week 6 (normal pattern); PS Plus free May 2024; EA Q1 FY24 record net bookings +21% YoY (r/pcgaming, 128 score). Estimated from historical FIFA franchise norms (6-15M/year).",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 7000000,
      "estimatedRevenue": 455000000,
      "revenueSource": "Reddit: EA lost $6B market cap due to FC 25 underperformance (r/Games, 1957 score); EA slashed fiscal year forecast (r/pcgaming, 1011 score); Q3 FY25 revenue fell $1.88B vs $1.94B YoY (r/Games, 261 score); Bloomberg: bookings slid on soccer weakness (r/Games, 207 score); worst user-rated in franchise history (r/EASportsFC, 623 score). Estimated ~33% decline from FC 24.",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 6000000,
      "estimatedRevenue": 390000000,
      "revenueSource": "Reddit: Beaten by Ghost of Yotei in UK physical launch (r/gaming, 1243 score); beaten by Battlefield 6 in European premium launch sales (r/gaming, 893 score); NOT #1 in US Circana Sept 2025 (r/Games, 466 score); not in Circana 2025 YTD best-sellers (r/Games, 754 score); 20-25% off within 2-3 weeks; 50% off by Black Friday (r/Games, 224 score). Lifecycle ongoing (~5 months). Estimate may increase to 7-8M lifetime.",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1527500000,
  "totalGamesFound": 3,
  "searchQueries": [
    "EA Sports FC 24 copies sold sales numbers",
    "EA Sports FC 25 copies sold sales numbers",
    "EA Sports FC 26 release announcement 2025",
    "FIFA EA FC sales data 2023 2024 2025",
    "EA Sports FC 24 million players launch",
    "EA FC 25 underperformance sales decline revenue",
    "EA earnings report fiscal year FC football unit sales copies",
    "FC 24 14.5 million players not copies sold",
    "EA Sports FC 24 best selling game 2023 chart sales",
    "FIFA EA FC annual sales copies sold franchise history VGChartz",
    "EA Sports FC 26 launch sales first week September October 2025",
    "EA FC 25 sold fewer copies decline worst selling",
    "EA Sports FC 24 million players million copies",
    "EA FC 25 FC 24 UK charts number one best selling Europe",
    "EA FC revenue decline net bookings football soccer quarterly",
    "FIFA 23 sales copies sold million last FIFA game",
    "EA FC 24 11 million 14 million copies sold players difference",
    "EA Sports FC sales numbers copies sold million 2024 2025",
    "EA FC 25 sold less than FC 24 copies decline percentage"
  ],
  "redditPostsAnalyzed": 26
}
```

---

## C. Key Caveats & Limitations

1. **EA does not disclose unit sales.** EA reports "players" (which includes EA Play/Game Pass subscribers, free trial users, PS Plus recipients, and demo players) and aggregate revenue/net bookings — never per-title copy sales. This was explicitly noted by multiple Reddit commenters and confirmed by EA's refusal to disclose Battlefield 2042 unit sales (r/pcgaming, 4,540 upvotes).

2. **"Players" ≠ copies sold.** As noted in the research rules and corroborated by Reddit user u/vKEVUv: "Wording with 'players' to investors is corny since game is also on EA Play and was 'free' with GeForce Now subscription." EA historically reports 10–30M+ "players" for FIFA/FC titles, but actual paid copy sales are a fraction of that figure.

3. **All copy-sales figures are estimates** derived from: (a) historical franchise benchmarks (6–15M copies/year), (b) comparative chart performance data from Reddit-sourced Circana/GSD reports, (c) EA earnings call data discussed on Reddit, and (d) discounting and subscription inclusion patterns. No Reddit post contained a specific "X million copies sold" figure for any FC title.

4. **FC 26 lifecycle is ongoing.** The 6.0M estimate reflects approximately 5 months of sales (September 2025 – February 2026). Lifetime sales could reach 7–8M copies as deep discounting continues.

5. **Revenue excludes microtransactions.** EA's Ultimate Team mode is the franchise's primary revenue driver — cumulative Ultimate Team revenue across all EA Sports titles exceeded $6 billion by 2020. Copy sales represent a minority of total franchise revenue.

6. **EA acquisition context.** EA was acquired by PIF/Silver Lake/Affinity Partners for $55 billion in 2025. Post-acquisition, EA's financial reporting transparency may change further.

---

## D. Sources (Reddit Posts Analyzed)

| Post ID | Subreddit | Score | Date | Topic |
|---------|-----------|-------|------|-------|
| 1i8x6am | r/Games | 1,957 | 2025-01-24 | EA lost $6B market value (FC 25 + Dragon Age) |
| 1ihva33 | r/Games | 261 | 2025-02-04 | EA Q3 revenue fell to $1.88B |
| 1i7m0ck | r/pcgaming | 1,011 | 2025-01-22 | EA slashed fiscal year forecast |
| 1i7m1w1 | r/Games | 207 | 2025-01-22 | Bloomberg: bookings slid on soccer weakness |
| 1nzc677 | r/gaming | 1,243 | 2025-10-06 | Ghost of Yotei beats FC 26 UK physical |
| 1o9atzm | r/gaming | 893 | 2025-10-17 | BF6 beats FC 26 European launch sales |
| 1ojbn4a | r/pcgaming | 184 | 2025-10-28 | EA Q2 FY26 net bookings down 13% |
| 1m1hki0 | r/EASportsFC | 749 | 2025-07-16 | FC 26 Official Reveal Trailer |
| 1ntgp6o | r/EASportsFC | 465 | 2025-09-29 | EA sold for $55B |
| 1n7ixhg | r/EASportsFC | 623 | 2025-09-04 | FC 25 worst user-rated in franchise history |
| 1pfo1ph | r/Games | 224 | 2025-12-06 | FC 26 tops Black Friday at 50% off |
| 1o5m20l | r/EASportsFC | 248 | 2025-10-13 | FC 26 already 20-25% off |
| 17umubg | r/EASportsFC | 328 | 2023-11-13 | FC 24 already 50% off |
| 1em3old | r/EASportsFC | 516 | 2024-08-07 | FC 25 least effort EA has ever put in |
| 16to3kb | r/gaming | 6,167 | 2023-09-27 | EA pulls FIFA games from storefronts |
| 1l3yklu | r/Games | 263 | 2025-06-05 | FC 25 coming to Game Pass |
| 1chp0eh | r/PS5 | 1,552 | 2024-05-01 | FC 24 free on PS Plus May 2024 |
| 1olq87u | r/EASportsFC | 1,065 | 2025-10-31 | FC 26 input delay (cites EA revenue) |
| 1npg5mw | r/EASportsFC | 730 | 2025-09-24 | FC 26 PC Input Delay megathread |
| hfjo7a | r/pcgaming | 24,461 | 2024-12-16 | Balatro dev vs PEGI (FC 25 MTX) |
| gp282o | r/Games | 545 | 2020-05-23 | Ultimate Team cumulative revenue $6B |
| 1od7v2m | r/Games | 466 | 2025-10-21 | Circana Sept 2025 (Borderlands 4 #1) |
| 15foxrm | r/pcgaming | 128 | 2023-08-01 | EA record Q1 FY24 bookings +21% |
| 1lm4fvs | r/EASportsFC | 1,337 | 2025-06-27 | Satirical "thank you EA" post |
| 1p2409b | r/Games | 754 | 2025-11-20 | Circana: BF6 best-selling game of 2025 |
| 1nk6tjr | r/EASportsFC | 132 | 2025-09-18 | FC 26 launch day |

---

*Research conducted 2026-02-20 using Reddit MCP tools via Claude Agent SDK. All sales figures are estimates — EA does not publicly disclose unit/copy sales data.*
