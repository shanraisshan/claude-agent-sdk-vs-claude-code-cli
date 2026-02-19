# FIFA / EA Sports FC Research Report — Iteration 1

**Research Period:** 2023–2025
**Date:** 2026-02-19
**Source:** Reddit (r/EASportsFC, r/Games, r/gaming, r/pcgaming, r/gamernews, r/truegaming)

---

## Executive Summary

The FIFA franchise transitioned to "EA Sports FC" starting in 2023. Three titles were released in the 2023–2025 window: EA Sports FC 24 (2023), EA Sports FC 25 (2024), and EA Sports FC 26 (2025). The rebrand maintained most of the playerbase but saw a notable sales decline with FC 25, which contributed to EA losing $6 billion in market value. FC 26 showed signs of recovery with strong Black Friday 2025 performance.

EA stopped publishing exact unit sales figures, instead reporting "players" (which includes EA Play trial users and Game Pass subscribers). All copy sales figures below are estimates derived from Reddit discussions of EA earnings reports, Steam data, and industry analysis.

---

## A. Revenue Table

Revenue calculated as: copies sold × average retail price at time of release.
- EA Sports FC 24: Average price ~$60 (standard edition across platforms)
- EA Sports FC 25: Average price ~$60 (standard edition; Ultimate Edition at $100 drove higher launch revenue)
- EA Sports FC 26: Average price ~$60 (standard edition)

**Note:** Revenue includes ONLY physical + digital copy sales. Excludes microtransactions, FIFA/FC Points, DLC, loot boxes, and in-app purchases.

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | ~14,000,000 | ~$840,000,000 | Medium |
| 2 | EA Sports FC 25 | 2024 | ~10,000,000 | ~$600,000,000 | Medium-Low |
| 3 | EA Sports FC 26 | 2025 | ~10,000,000 | ~$600,000,000 | Low |
| **TOTAL** | | | **~34,000,000** | **$2.04 B** | |

### Notes on Estimates

- **FC 24 (~14M):** EA reported 14.5M "players" in the first month. Discounting EA Play/Game Pass trial users (~20-30%), actual copy sales likely ~10-11M in the first month, with lifetime reaching ~14M. This aligns with Reddit estimates of 12-15M.
- **FC 25 (~10M):** Significantly underperformed FC 24. EA slashed fiscal forecasts. Jason Schreier confirmed underperformance. Reddit consensus put lifetime sales ~8-11M. Using midpoint of ~10M.
- **FC 26 (~10M):** Released Sept/Oct 2025, only ~4-5 months of sales data as of Feb 2026. Was #1 game during Europe's Black Friday 2025. Estimated ~10M based on early lifecycle performance and franchise baseline, though this could grow significantly.

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, Nintendo Switch, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 14000000,
      "estimatedRevenue": 840000000,
      "revenueSource": "Reddit estimates from EA earnings discussions (r/Games, r/EASportsFC, r/pcgaming). EA reported 14.5M players in first month; copy sales estimated at ~14M lifetime after discounting EA Play/Game Pass trial users.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, Nintendo Switch, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 10000000,
      "estimatedRevenue": 600000000,
      "revenueSource": "Reddit discussions of EA $6B market cap loss and fiscal forecast cuts (r/Games 1.9K upvotes, r/pcgaming 1K upvotes). Jason Schreier confirmed underperformance. FC 25 launch broke US revenue record but unit sales declined vs FC 24.",
      "confidence": "medium-low"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch 2",
      "publisher": "Electronic Arts",
      "copiesSold": 10000000,
      "estimatedRevenue": 600000000,
      "revenueSource": "Reddit posts show FC 26 was #1 game during Europe Black Friday 2025 (r/Games, 224 upvotes). Active player discussions on r/EASportsFC in Jan-Feb 2026. Early lifecycle estimate based on franchise baseline.",
      "confidence": "low"
    }
  ],
  "totalRevenue": 2040000000,
  "totalGamesFound": 3,
  "searchQueries": [
    "EA Sports FC 24 sales numbers copies sold",
    "EA FC 25 sales decline units sold revenue",
    "FIFA EA FC sales decline 2023 2024 2025",
    "EA Sports FC FIFA rebrand sales comparison copies",
    "EA Sports FC 25 underperformance sales revenue record soccer",
    "EA Sports FC 26 release sales 2025"
  ],
  "redditPostsAnalyzed": 40
}
```

---

## Key Findings

1. **Total estimated copy sales revenue (2023-2025): ~$2.04 billion** from ~34 million copies across three titles.

2. **FC 25 was the weakest entry**, contributing to EA's $6B market cap loss in January 2025. EA slashed its fiscal year forecast. Reddit community consensus was that FC 25 represented "the least effort EA has ever put in."

3. **FC 26 shows recovery signs**, topping European Black Friday 2025 charts and generating active community engagement.

4. **EA was acquired for $55 billion** during the FC 26 lifecycle (announced on r/EASportsFC with 463 upvotes), marking a transformative corporate event for the franchise's future.

5. **Data quality limitation:** EA no longer reports unit sales, only "players" (inflated by EA Play/Game Pass). All figures are community-derived estimates with medium-to-low confidence.
