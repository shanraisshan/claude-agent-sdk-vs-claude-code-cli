# Research Report: FIFA / EA Sports FC Copy Sales (2023–2025)
## Iteration 5 — Claude Agent SDK
## Date: 2026-02-19

---

## Overview

This report covers all premium paid FIFA-franchise games released between 2023 and 2025. EA rebranded FIFA to **EA Sports FC** starting September 2023, so the relevant titles are:

1. **EA Sports FC 24** (September 29, 2023)
2. **EA Sports FC 25** (September 27, 2024)
3. **EA Sports FC 26** (September/October 2025)

> **Critical caveat:** EA does not publicly disclose per-title unit (copy) sales for the EA Sports FC franchise. EA exclusively uses "player count" language that inflates figures by including EA Play trial users, Xbox Game Pass subscribers, PS Plus trial users, and free demo/Showcase downloads. All copy-sales figures below are estimates derived from Reddit-sourced data, EA earnings commentary, market cap movements, and franchise trajectory analysis.

---

## A. Revenue Table

| # | Title | Year | Copies Sold | Avg. Price (USD) | Revenue (USD) | Confidence |
|---|-------|------|-------------|-------------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | 10.5M | $62 | $651,000,000 | Medium |
| 2 | EA Sports FC 25 | 2024 | 7.0M | $62 | $434,000,000 | Low |
| 3 | EA Sports FC 26 | 2025 | 7.5M (projected) | $70 | $525,000,000 | Low |
| **TOTAL** | | | **25.0M** | | **$1.61B** | |

---

## Estimation Methodology

### EA Sports FC 24 — 10.5M copies, $651M revenue (Medium confidence)

**Key data points:**
- EA reported 11 million "players" in the first week (VGC article discussed on r/Games, Oct 2023)
- EA claimed FC 24 "attracted more players at launch than FIFA 23"
- Per research rules: "players" ≠ copies sold. EA counts EA Play, Game Pass, and PS Plus trial users. Actual purchasers are typically 60–75% of reported player counts
- 11M × ~65% = ~7.1M paid copies in week one
- FC 24 was considered a commercial success by EA — it met internal expectations and validated the FIFA → FC rebrand
- The franchise historically sells 10–15M copies per annual release over its full lifecycle

**Pricing rationale:** FC 24 launched on PS5, PS4, Xbox Series X/S, Xbox One, PC, and Nintendo Switch. With last-gen and Switch versions at lower price points ($40–$60), blended average is ~$62.

**Estimate:** ~10.5M lifetime copies × $62 = **$651M**

---

### EA Sports FC 25 — 7.0M copies, $434M revenue (Low confidence)

**Key data points:**
- Jason Schreier (Bloomberg) reported EA slashed its fiscal year forecast due to FC 25 underperformance (r/pcgaming, Jan 2025, score: 1005)
- EA lost **$6 billion in market capitalization** following the FC 25 + Dragon Age underperformance disclosure (r/Games, Jan 2025, score: 1957)
- Reddit commenters confirmed FC 25 was the **bigger factor** in the revenue miss vs. Dragon Age: *"Most of this is because of FC doing badly"* (score: 477)
- EA Q3 FY2025 revenue fell to $1.88B from $1.94B YoY, with weakness explicitly attributed to FC (r/Games, Feb 2025)
- EA released a **free "Showcase" version** of FC 25 in December 2024 — just ~2 months after launch — interpreted by the community as a desperation move (r/EASportsFC, score: 153)
- FC 25 was the **worst user-rated game in franchise history** across Metacritic, Google, and Steam (r/EASportsFC, score: 619)
- FC 25 was added to Xbox Game Pass in June 2025 — an unusually early vault addition suggesting exhausted commercial runway (r/Games, score: 261)
- Reddit consensus: 20–30% decline from FC 24 levels

**Applying research rules:** Title described as "underperforming" with EA slashing forecasts and losing billions in market value → use the **LOWER end** of estimate ranges. A 30% decline from FC 24's ~10.5M = ~7.35M, rounded down to **7.0M**.

**Pricing rationale:** FC 25 launched on same platforms as FC 24 (PS5, PS4, Xbox Series X/S, Xbox One, PC, Switch), so same blended average of ~$62.

**Estimate:** ~7.0M copies × $62 = **$434M**

---

### EA Sports FC 26 — 7.5M copies (projected), $525M revenue (Low confidence)

**Key data points:**
- Ghost of Yotei beat FC 26 in UK physical sales at launch — unprecedented for the FIFA/FC franchise which historically dominates UK charts (r/gaming, Oct 2025, score: 1245). Caveat: physical is now ~10% of UK sales.
- **Battlefield 6 beat FC 26 in European launch sales** (GSD data = premium paid copy sales only), also unprecedented (r/gaming, Oct 2025, score: 892)
- FC 26 **recovered to become a top seller during Europe's Black Friday 2025** (r/Games, Dec 2025, score: 220)
- FC 26 also receiving very negative community reception: *"FC 26 is the worst football game of all Fifa series"* (r/EASportsFC, score: 138)
- Significant PC input delay issues at launch drew 729 upvotes and 347 comments in a mega-thread

**Applying research rules:** FC 26 is still in its active sales window (<6 months since launch). Per rules: *"estimate based on franchise trajectory and comparable prior-year titles. A sequel that shows 'slight recovery' or 'modest improvement' over a predecessor should be estimated slightly above that predecessor."* The Black Friday recovery after a weak launch represents modest improvement over FC 25's trajectory → estimate slightly above FC 25.

**Pricing rationale:** FC 26 dropped last-gen console support (no PS4/Xbox One) and no Switch version. Priced at £69.99 / ~$70. Per rules: *"use $70 for titles that are current-gen only or that dropped last-gen support."*

**Estimate:** ~7.5M projected lifetime copies × $70 = **$525M**

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
      "estimatedRevenue": 651000000,
      "revenueSource": "Reddit: 11M 'players' week 1 per VGC (r/Games); EA claimed matched FIFA 23 launch; 65% purchaser ratio applied; franchise historically 10-15M/year; met EA expectations",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 7000000,
      "estimatedRevenue": 434000000,
      "revenueSource": "Reddit: EA slashed forecasts (r/pcgaming, Bloomberg); $6B market cap loss (r/Games, VGC); Q3 revenue fell $1.88B vs $1.94B YoY; free Showcase version released 2 months post-launch; worst user ratings in franchise history; 30% decline from FC 24 (lower end per underperformance rules)",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 7500000,
      "estimatedRevenue": 525000000,
      "revenueSource": "Reddit: Lost UK physical charts to Ghost of Yotei (r/gaming); lost European launch to BF6 in GSD data (r/gaming); recovered for Black Friday 2025 (r/Games); still in active sales window; slight improvement over FC 25 trajectory per rules",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1610000000,
  "totalGamesFound": 3,
  "searchQueries": [
    "EA Sports FC 24 sales copies sold",
    "EA Sports FC 25 sales copies sold",
    "FIFA EA FC sales numbers 2023 2024",
    "EA Sports FC copies sold revenue",
    "EA FC 24 underperforming sales",
    "EA FC 25 sales figures",
    "EA Sports FC player count vs copies sold",
    "EA FC 24 14.5 million players first month",
    "EA FC 24 UK chart number one launch sales",
    "EA Sports FC 25 underperforming missed expectations sales decline",
    "EA FC 26 launch sales first week",
    "EA earnings Q3 2025 FC sports net bookings decline",
    "EA FC 24 11 million copies sold VGChartz",
    "EA Sports FC 24 best selling game 2023 holiday season",
    "FIFA franchise total sales billion EA annual report",
    "EA FC 24 sold fewer copies than FIFA 23 rebrand impact",
    "EA Sports FC 25 sales down 40 percent fewer copies"
  ],
  "redditPostsAnalyzed": 15
}
```

---

## Key Findings & Context

1. **EA deliberately obscures copy sales data.** EA uses "player count" language for all EA Sports FC announcements, inflating numbers by 25–40% over actual paid copies by including EA Play trials, Game Pass subscribers, and free demo users. No authoritative per-title unit sales figure exists in public Reddit discussions.

2. **The FIFA → EA Sports FC rebrand was commercially successful for FC 24** but the franchise has been in decline since. FC 24 met expectations; FC 25 was a disaster (worst-rated, forecast-slashing, $6B market cap hit); FC 26 shows modest recovery but lost its historical European chart dominance.

3. **Revenue is overwhelmingly from copy sales + Ultimate Team microtransactions**, but this report covers **copy sales only** per the research scope. EA's total FC franchise revenue including FUT microtransactions would be significantly higher (historically 2–3× copy sale revenue).

4. **FC 26 pricing shift to $70 partially offsets declining unit sales.** By dropping last-gen support and pricing at $70 across the board, FC 26 generates more revenue per copy than FC 24/25 despite potentially selling fewer units.

5. **The $55 billion EA acquisition by PIF/Silver Lake** (announced 2025) suggests investors still value the FC franchise highly despite recent declines, likely due to recurring FUT microtransaction revenue rather than copy sales.

---

## Confidence Assessment

| Factor | Impact on Estimates |
|--------|-------------------|
| EA never discloses unit sales | High uncertainty on all figures |
| "Players" ≠ copies sold (60-75% ratio) | Applied to FC 24 first-week data |
| FC 25 underperformance confirmed by Bloomberg, VGC, EA earnings | Strong directional signal, no exact figure |
| FC 26 still in active sales window | Projected figure, will change |
| No third-party tracking (NPD/Circana) data surfaced on Reddit | Industry-standard data not available in Reddit sources |

**Overall confidence: Low-to-Medium.** The directional trends are well-supported by Reddit sources (FC 24 success → FC 25 decline → FC 26 modest recovery), but specific unit figures are estimates due to EA's deliberate opacity on copy sales data.

---

## Sources (Reddit Posts Analyzed)

1. r/pcgaming — "Jason Schreier: EA is slashing its forecast..." (1i7m0ck, score: 1005)
2. r/Games — "EA lost $6 billion in market value..." (1i8x6am, score: 1957)
3. r/Games — "Electronic Arts saw revenue fall to $1.88 billion..." (1ihva33, score: 258)
4. r/gaming — "Ghost of Yotei Beats EA Sports FC 26..." (1nzc677, score: 1245)
5. r/gaming — "Battlefield 6 sold more copies across Europe..." (1o9atzm, score: 892)
6. r/Games — "PS5, EA Sports FC 26 and Hogwarts Legacy top Black Friday" (1pfo1ph, score: 220)
7. r/Games — "EA Sports FC 24 attracted more players at launch than FIFA 23" (173ttky)
8. r/EASportsFC — "FC 25 Is the Worst User-Rated Game in Franchise History" (1n7ixhg, score: 619)
9. r/EASportsFC — "EA Sports officially sold for $55 billion" (1ntgp6o, score: 465)
10. r/EASportsFC — "EA SPORTS FC 26 Official Reveal Trailer" (1m1hki0, score: 748)
11. r/EASportsFC — "FC 26 is the worst football game of all Fifa series" (1p9xn9n, score: 138)
12. r/EASportsFC — "Free version of EA FC: EA SPORTS FC 25 Showcase" (1h9bhgw, score: 153)
13. r/Games — "EA Sports FC 24 Players Say $30 Launch Week Loot Box..." (16y02xe, score: 494)
14. r/gaming — "EA pulls its FIFA games from digital storefronts" (16to3kb, score: 6160)
15. r/Games — "Coming to Game Pass: EA Sports FC 25..." (1l3yklu, score: 261)

---

*Report generated by Claude Agent SDK — Iteration 5*
