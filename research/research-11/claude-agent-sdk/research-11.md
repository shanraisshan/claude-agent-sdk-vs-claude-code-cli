# Research Report: FIFA / EA Sports FC Games (2023–2025)
## Iteration 11 — Claude Agent SDK

---

## Methodology

This report synthesizes data from **38 Reddit posts** across r/EASportsFC, r/gaming, r/Games, r/pcgaming, r/PS5, r/XboxSeriesX, r/FUTMobile, and r/truegaming. Over **20 search queries** were executed via the Reddit MCP tool.

**Important caveat:** EA does not publicly disclose per-title unit sales for its FIFA/EA Sports FC franchise. EA reports "active players" (which includes EA Play trial users and non-purchasers) rather than copies sold. All copy sales figures below are **estimates** derived from:
- EA's reported "14.5 million players" for FC 24's first month (adjusted downward for non-purchasers)
- Confirmed year-over-year decline statements from industry data (thegamebusiness.com cited on Reddit)
- Steam peak concurrent player trends as a proxy for overall engagement
- EA financial disclosures (revenue declines, forecast cuts, $6B market cap loss)
- European and UK retail chart positions

**Scope:** Games with the FIFA/EA Sports FC brand **released** between 2023 and 2025. FIFA 23 (released September 2022) is excluded. EA Sports FC Mobile is excluded as it is free-to-play with no copy sales.

**Revenue calculation:** Revenue = estimated copies sold × blended average retail price at launch. Prices reflect a weighted average across PS5/Xbox Series X ($69.99), PS4/Xbox One/PC ($59.99), and Nintendo Switch Legacy ($39.99). FC 26 dropped last-gen support but added Switch 2. A blended average of **~$65 USD** is used for FC 24 and FC 25; **$70 USD** for FC 26 (current-gen only). Only physical + digital copy sales are counted. **Microtransactions, DLC, loot boxes, Ultimate Team card packs, and in-app purchases are excluded.**

---

## A. Revenue Table

| # | Title | Year | Copies Sold (Est.) | Revenue (USD, Est.) | Confidence |
|---|-------|------|--------------------|---------------------|------------|
| 1 | EA Sports FC 24 | 2023 | ~11.0M | ~$715,000,000 | Medium |
| 2 | EA Sports FC 25 | 2024 | ~9.0M | ~$585,000,000 | Medium |
| 3 | EA Sports FC 26 | 2025 | ~8.0M | ~$560,000,000 | Low |
| — | EA Sports FC Mobile | 2023–2025 | N/A (Free-to-Play) | N/A (MTX only) | — |
| **TOTAL** | | | **~28.0M** | **~$1.86B** | |

### Notes on Estimates

**EA Sports FC 24 (~11M copies, Medium confidence):**
- EA reported 14.5M "players" in the first month; adjusting ~25% for EA Play trial users and non-purchasers yields ~10–12M actual copies sold.
- Was #1 in UK physical charts as late as March 2024 (6 months post-launch) — r/PS5 post id: 1bn5h89.
- Confirmed to have sold fewer copies than FIFA 23: "the newer games all sold fewer games than their predecessors" — thegamebusiness.com data cited in r/Games post id: 1k2tg9f.
- Given away on PlayStation Plus by May 2024 (~7 months post-launch), suggesting premium sales had largely peaked.
- Was 55% digital in Europe.
- Discounted 50% within ~6 weeks of launch — r/EASportsFC post id: 17umubg.
- Steam all-time peak: 107,109 concurrent players, down 3.3% from FIFA 23.
- **Midpoint estimate: 11M copies.**

**EA Sports FC 25 (~9M copies, Medium confidence):**
- Sold fewer copies than FC 24 — explicitly confirmed (same thegamebusiness.com source, r/Games post id: 1k2tg9f).
- EA slashed full fiscal year forecast; EA lost $6B in market cap primarily due to FC 25 underperformance — r/Games post id: 1i8x6am, r/pcgaming post id: 1i7m0ck.
- EA Q3 FY2025 revenue fell from $1.94B to $1.88B, partly due to FC 25 — r/Games post id: 1ihva33.
- Was 62% digital in Europe (up from 55% for FC 24).
- Despite underperformance vs. EA targets, was still the **#1 best-selling game in ALL 17 tracked European countries** for H1 2025 — r/Games post id: 1m2vrvv.
- Worst user-rated game in franchise history on Metacritic, Google, and Steam — r/EASportsFC post id: 1n7ixhg.
- Steam peak concurrent was actually +1.3% YoY (108,534 vs 107,109), but Steam alone is not representative of console trends.
- EA notably never released any player count or sales milestone for FC 25 — strongly suggesting disappointing numbers.
- **Midpoint estimate: 9M copies.**

**EA Sports FC 26 (~8M copies, Low confidence):**
- Steam peak concurrent dropped 12% YoY to 95,489 — lowest in 5 years — r/EASportsFC post id: 1qvnm2k.
- First year EA did NOT issue an official sales/player count press release (a franchise first).
- Outsold at European launch by Battlefield 6 (which sold 6.5M globally in first days) — r/gaming post id: 1o9atzm.
- Lost UK physical sales #1 spot to Ghost of Yotei during launch window — r/gaming post id: 1nzc677.
- Standard edition sales fell 62% week-over-week in its second week — r/gaming post id: 1o6tv4e.
- Despite all this, topped European charts for 3+ consecutive weeks at launch.
- Dropped PS4/Xbox One support; first to launch on Nintendo Switch 2.
- Community speculation suggests "console has definitely dropped more than 12%" — r/EASportsFC post id: 1qvnm2k comments.
- **Midpoint estimate: 8M copies (highly speculative; could range 7–9M).**

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
      "copiesSold": 11000000,
      "estimatedRevenue": 715000000,
      "revenueSource": "Reddit: 14.5M players first month adjusted for non-purchasers; #1 UK physical charts Mar 2024 (r/PS5 1bn5h89); sold fewer than FIFA 23 confirmed (r/Games 1k2tg9f); PS Plus May 2024 (r/PS5 1chp0eh); Steam peak 107,109 (r/EASportsFC 1qvnm2k); 55% digital Europe; 50% off 6 weeks post-launch (r/EASportsFC 17umubg)",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 9000000,
      "estimatedRevenue": 585000000,
      "revenueSource": "Reddit: Confirmed sold fewer than FC 24 (r/Games 1k2tg9f); EA lost $6B market cap (r/Games 1i8x6am); EA slashed fiscal forecast (r/pcgaming 1i7m0ck); Q3 FY25 revenue fell to $1.88B (r/Games 1ihva33); #1 in all 17 EU countries H1 2025 (r/Games 1m2vrvv); worst user-rated ever (r/EASportsFC 1n7ixhg); Steam peak 108,534 (r/EASportsFC 1qvnm2k); 62% digital Europe",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch 2",
      "publisher": "Electronic Arts",
      "copiesSold": 8000000,
      "estimatedRevenue": 560000000,
      "revenueSource": "Reddit: Steam peak dropped 12% to 95,489 lowest in 5 years (r/EASportsFC 1qvnm2k); outsold by BF6 EU launch (r/gaming 1o9atzm); lost UK physical #1 to Ghost of Yotei (r/gaming 1nzc677); 62% WoW standard edition decline (r/gaming 1o6tv4e); no official EA sales press release — franchise first; topped EU charts 3+ weeks",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1860000000,
  "totalGamesFound": 3,
  "searchQueries": [
    "FIFA EA Sports FC game releases 2023 2024 2025 complete list",
    "EA Sports FC 24 FC 25 FIFA rebrand all titles",
    "FIFA EA FC timeline every game released franchise",
    "EA Sports FC 24 release date rebrand from FIFA",
    "EA Sports FC 24 copies sold sales figures million units",
    "EA Sports FC 25 sales numbers copies sold units",
    "EA Sports FC 26 sales copies sold launch",
    "FC 25 underperformance sales decline revenue EA earnings report",
    "EA Sports FC 24 million players best selling football game",
    "FIFA mobile EA Sports FC mobile 2023 2024 2025",
    "VGChartz FIFA EA FC sales data units sold football game",
    "EA Sports FC 25 FC 24 NPD UK charts best selling game 2024",
    "FIFA franchise 325 million total sales copies sold all time",
    "EA Sports FC 24 record launch first week fastest selling",
    "EA FC 25 sales down decline percent compared FC 24 fewer copies",
    "EA FC 25 flopped sales underperformed FIFA annual revenue down",
    "EA FC 24 sold 11.3 million 14.5 million active players record",
    "EA FC Mobile shutting down discontinued 2025",
    "EA FC 26 launch week sales September October 2025",
    "FC 26 Engagement numbers Steam"
  ],
  "redditPostsAnalyzed": 38
}
```

---

## C. Key Findings

1. **No exact sales figures exist on Reddit.** EA deliberately obscures unit sales by reporting "active players" instead. All figures in this report are estimates.

2. **Confirmed declining trend:** An authoritative industry source (thegamebusiness.com, cited on r/Games) explicitly states: *"the newer games all sold fewer games than their predecessors"* — confirming FIFA 23 > FC 24 > FC 25 in unit sales.

3. **FC 25 was a major commercial disappointment.** Despite being the #1 game in all 17 European countries for H1 2025, FC 25 underperformed EA's internal targets enough to cause a fiscal year forecast revision and $6B market cap loss. EA never released any player/sales milestone — a first for the franchise.

4. **FC 26 represents the steepest decline.** A 12% drop in Steam engagement, no official press release, and being outsold by Battlefield 6 and Ghost of Yotei at launch all point to the weakest-selling entry in recent franchise history.

5. **The franchise remains dominant despite decline.** Even at reduced sales, EA Sports FC games are among the best-selling titles in Europe. FC 25 was #1 in all 17 tracked European countries for H1 2025. FC 26 topped European charts for 3+ weeks at launch. The franchise's floor is still enormous by industry standards.

6. **Copy sale revenue is a fraction of total franchise income.** Multiple Reddit comments note that Ultimate Team microtransactions generate "billions every year" — far exceeding copy sale revenue. This report deliberately excludes that revenue per the research brief.

7. **EA Sports FC Mobile is free-to-play** and therefore excluded from copy sales calculations. It was active throughout 2023–2025 but showed declining community engagement.

---

## D. Confidence Assessment

| Rating | Meaning |
|--------|---------|
| **High** | Data directly sourced from official EA communications or verified industry reports cited on Reddit |
| **Medium** | Estimates derived from multiple corroborating Reddit data points (player counts, chart positions, financial disclosures) |
| **Low** | Estimates based primarily on engagement proxies (Steam data) and competitive comparisons, with limited direct evidence |

The overall confidence in the **total revenue estimate of ~$1.86B** is **Medium-Low**. The direction of the trend (declining sales year-over-year) is high confidence; the specific unit numbers carry meaningful uncertainty ranges (±15–25%).

---

*Research conducted via Reddit MCP tools. 38 posts analyzed across 20+ search queries. All revenue calculations reflect copy sales (physical + digital) only — no microtransactions, DLC, loot boxes, or in-app purchases included.*
