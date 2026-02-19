# FIFA / EA Sports FC Games Research Report (2023-2025) - Iteration 3

## Overview

This report covers all FIFA-branded and EA Sports FC games released between 2023 and 2025. In 2023, EA dropped the FIFA naming license and rebranded to "EA Sports FC." The franchise continued its annual release cycle under the new name. Revenue calculations below cover **copy sales only** (physical + digital purchases). Microtransactions, DLC, loot boxes, and in-app purchases are excluded.

---

## A. Revenue Table

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | 10,500,000 | $735,000,000 | medium |
| 2 | EA Sports FC 25 | 2024 | 6,000,000 | $420,000,000 | low |
| 3 | EA Sports FC 26 | 2025 | 6,500,000 | $455,000,000 | low |
| **TOTAL** | | | **23,000,000** | **$1.61 B** | |

### Revenue Calculation Notes

- **EA Sports FC 24 (2023):** EA reported 11.3 million players in the first week (including EA Play trials). Based on Reddit discussions comparing this to FIFA 23 patterns, actual paid copy sales are estimated at ~10.5 million lifetime. Average retail price at launch: $69.99 (next-gen) / $59.99 (last-gen/PC). Blended average ~$70 used for calculation.
- **EA Sports FC 25 (2024):** Significantly underperformed. EA slashed its fiscal year forecast in January 2025, and the company lost $6 billion in market value partly due to FC 25 weakness. Reddit consensus and earnings data suggest a major decline. EA also launched a free-to-play "Showcase" version in April 2025 to try to boost engagement. Estimated ~6 million copies at ~$70 average.
- **EA Sports FC 26 (2025):** Released late 2025. Was beaten by Ghost of Yotei in UK physical launch sales. No official sales figures yet. Conservative estimate of ~6.5 million copies based on franchise trajectory and slight recovery from FC 25 backlash. Average price ~$70.

### Notes on Excluded Titles
- **EA Sports FC Mobile** (2023-2025): Free-to-play mobile game. No copy sales. Revenue comes entirely from in-app purchases, which are excluded per the research criteria.

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
      "estimatedRevenue": 735000000,
      "revenueSource": "Reddit discussions of EA's 11.3M first-week player announcement (r/pcgaming), VGC article threads, PS Plus giveaway timing analysis, EA earnings discussions on r/Games",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 6000000,
      "estimatedRevenue": 420000000,
      "revenueSource": "Reddit posts about EA losing $6B market value (r/Games), Jason Schreier report on EA slashing forecast (r/pcgaming), EA Q3 earnings decline discussions, community feedback on FC 25 minimal improvements",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch 2",
      "publisher": "Electronic Arts",
      "copiesSold": 6500000,
      "estimatedRevenue": 455000000,
      "revenueSource": "Reddit discussions of UK physical sales performance vs Ghost of Yotei (r/gaming), franchise trajectory analysis from best-selling franchises thread, EA FC 26 reveal trailer reception on r/EASportsFC",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1610000000,
  "totalGamesFound": 3,
  "searchQueries": [
    "FIFA EA Sports FC games released 2023 2024 2025",
    "EA Sports FC 24 FC 25 copies sold sales million",
    "FIFA EA FC sales numbers copies sold millions",
    "EA Sports FC 25 underperformance sales decline numbers",
    "EA Sports FC 24 sales figures copies sold million players",
    "FIFA EA FC 24 25 revenue earnings quarterly report billion",
    "EA FC 24 14.5 million 11 million copies sold players",
    "FIFA Mobile EA Sports FC Mobile 2023 2024 2025",
    "EA Sports FC 24 total sales lifetime copies sold VGChartz NPD",
    "EA Sports FC 25 sales drop percent decline units",
    "Best Selling Video Game Franchises Ever"
  ],
  "redditPostsAnalyzed": 25
}
```

---

## Key Findings

1. **The FIFA-to-EA Sports FC rebrand (2023)** did not significantly hurt initial sales of FC 24, which performed comparably to FIFA 23 in its first week (11.3M players vs 10.3M for FIFA 23).

2. **FC 25 was a major underperformer.** EA slashed its fiscal year forecast and lost $6 billion in market value. Reddit community consensus attributed this to minimal gameplay improvements, buggy anti-cheat, and general franchise fatigue.

3. **FC 26 launched in late 2025** but was beaten in UK physical sales by Ghost of Yotei, suggesting continued softness in the franchise.

4. **EA Sports FC Mobile** is free-to-play and generates revenue through microtransactions only (excluded from this analysis). The service appeared to be winding down by mid-2025.

5. **Copy sales revenue for the franchise from 2023-2025 is estimated at approximately $1.61 billion**, with the significant caveat that the majority of EA's football game revenue actually comes from Ultimate Team microtransactions (not counted here).

---

## Sources

All data sourced from Reddit via MCP tools. Key subreddits: r/EASportsFC, r/gaming, r/Games, r/pcgaming, r/FUTMobile, r/PS5. Key external sources discussed on Reddit: VideoGamesChronicle (VGC), Hollywood Reporter, Jason Schreier (Bloomberg/Bluesky), Engadget, PushSquare.
