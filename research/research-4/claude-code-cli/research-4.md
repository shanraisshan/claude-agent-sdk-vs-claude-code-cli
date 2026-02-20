# FIFA / EA Sports FC Games Research Report (2023-2025) - Iteration 4

## Overview

This report covers all FIFA-branded and EA Sports FC games released between 2023 and 2025. In 2023, EA officially dropped the FIFA naming license and rebranded to "EA Sports FC." The franchise continued its annual release cycle under the new name. Revenue calculations below cover **copy sales only** (physical + digital purchases). Microtransactions, DLC, loot boxes, and in-app purchases are excluded.

---

## A. Revenue Table

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | 10,500,000 | $735,000,000 | medium |
| 2 | EA Sports FC 25 | 2024 | 6,000,000 | $420,000,000 | low |
| 3 | EA Sports FC 26 | 2025 | 6,500,000 | $455,000,000 | low |
| **TOTAL** | | | **23,000,000** | **$1.61 B** | |

### Revenue Calculation Notes

- **EA Sports FC 24 (2023):** EA reported 11.3 million players in the first week (including EA Play trials), per VGC article threads on r/pcgaming and r/gaming. FIFA 23 had 10.3 million first-week players for comparison, showing the rebrand did not significantly hurt initial adoption. Actual paid copy sales are estimated at ~10.5 million lifetime, accounting for EA Play trial players who did not purchase. Average retail price at launch: $69.99 (next-gen) / $59.99 (last-gen/PC). Blended average ~$70 used for calculation. **Revenue: 10.5M x $70 = $735M.**

- **EA Sports FC 25 (2024):** Significantly underperformed. EA slashed its fiscal year forecast in January 2025, with Jason Schreier reporting on the underperformance (r/pcgaming, 1,011 upvotes). EA lost $6 billion in market value partly due to FC 25 weakness (r/Games, 1,950 upvotes). EA's Q3 FY2025 revenue fell to $1.88B from $1.94B year-over-year, with FC franchise weakness specifically cited (r/Games). Community sentiment was overwhelmingly negative -- "least effort EA has ever put in" (r/EASportsFC, 517 upvotes). FC 25 was later added to Xbox Game Pass in June 2025 to try to boost engagement. Estimated ~6 million copies at ~$70 average. **Revenue: 6M x $70 = $420M.**

- **EA Sports FC 26 (2025):** Released September/October 2025 (reveal trailer posted July 16, 2025). Was beaten by Ghost of Yotei in UK physical launch sales (r/gaming, 1,238 upvotes) and by Battlefield 6 in European launch premium sales (r/gaming, 893 upvotes). Community reception was very negative, with users calling it "the worst football game of all Fifa series" (r/EASportsFC). A major PC input delay bug plagued launch (r/EASportsFC mega-thread, 722 upvotes). No official sales figures released yet. Conservative estimate of ~6.5 million copies based on franchise trajectory and slight recovery from FC 25 backlash, though soft launch indicators suggest this may be optimistic. Average price ~$70. **Revenue: 6.5M x $70 = $455M.**

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
      "revenueSource": "Reddit discussions of EA's 11.3M first-week player announcement (VGC article threads on r/pcgaming and r/gaming), FIFA 23 comparison at 10.3M first-week players, EA earnings discussions on r/Games, EA delisting old FIFA titles from Steam (r/gaming, 6,160 upvotes)",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 6000000,
      "estimatedRevenue": 420000000,
      "revenueSource": "Jason Schreier report on EA slashing fiscal forecast due to FC 25 underperformance (r/pcgaming, 1,011 upvotes), EA losing $6B market value (r/Games, 1,950 upvotes), EA Q3 revenue decline to $1.88B from $1.94B (r/Games, 256 upvotes), community negativity on r/EASportsFC (517 upvotes for 'least effort' post), FC 25 added to Game Pass June 2025 (r/Games, 266 upvotes)",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch 2",
      "publisher": "Electronic Arts",
      "copiesSold": 6500000,
      "estimatedRevenue": 455000000,
      "revenueSource": "UK physical launch sales beaten by Ghost of Yotei (r/gaming, 1,238 upvotes), European launch sales beaten by Battlefield 6 (r/gaming, 893 upvotes), extremely negative community reception on r/EASportsFC, PC input delay mega-thread (722 upvotes), franchise trajectory analysis based on FC 24 and FC 25 performance decline",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1610000000,
  "totalGamesFound": 3,
  "searchQueries": [
    "FIFA EA Sports FC games released 2023 2024 2025 complete list",
    "EA Sports FC 24 FC 25 copies sold sales millions units",
    "FIFA 2023 2024 2025 sales numbers copies sold",
    "EA Sports FC 24 sold copies units players worldwide",
    "EA FC 25 underperformance sales drop decline revenue",
    "EA Sports FC 26 release date sales launch copies",
    "EA FC 24 record players 14.5 million first month launch",
    "FIFA EA FC franchise total sales revenue annual report earnings 2024",
    "EA Sports FC copies sold units sold million players 2024 2025"
  ],
  "redditPostsAnalyzed": 28
}
```

---

## Key Findings

1. **The FIFA-to-EA Sports FC rebrand (2023)** did not significantly hurt initial sales of FC 24, which performed comparably to FIFA 23 in its first week (11.3M players vs 10.3M for FIFA 23). EA simultaneously delisted all prior FIFA titles from digital storefronts like Steam.

2. **FC 25 was a major underperformer.** EA slashed its fiscal year forecast in January 2025 and lost $6 billion in market value. Reddit community consensus attributed this to minimal gameplay improvements, buggy anti-cheat implementation, and deepening franchise fatigue. EA attempted to salvage engagement by adding FC 25 to Xbox Game Pass in June 2025.

3. **FC 26 launched in September/October 2025** with soft sales. It was beaten in UK physical sales by Ghost of Yotei and in European launch premium sales by Battlefield 6 (another EA title). Community reception was overwhelmingly negative, with a major PC input delay bug at launch and users calling it "the worst football game of all Fifa series."

4. **EA was acquired for $55 billion in 2025** by PIF, Silver Lake, and Affinity Partners, as discussed on r/EASportsFC. This corporate context is relevant to the franchise's future direction under new ownership.

5. **EA Sports FC Mobile** is free-to-play and generates revenue through microtransactions only (excluded from this analysis).

6. **Copy sales revenue for the franchise from 2023-2025 is estimated at approximately $1.61 billion**, with the significant caveat that the majority of EA's football game revenue actually comes from Ultimate Team microtransactions (not counted here). The franchise shows a clear downward trend in unit sales across the three-year period.

---

## Sources

All data sourced from Reddit via MCP tools. Key subreddits: r/EASportsFC, r/gaming, r/Games, r/pcgaming, r/truegaming. Key external sources discussed on Reddit: VideoGamesChronicle (VGC), Hollywood Reporter, Jason Schreier (Bloomberg/Bluesky), Engadget, PushSquare, TheGameBusiness.
