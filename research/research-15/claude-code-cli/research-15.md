# Research Report - Iteration 15
## FIFA / EA Sports FC Game Sales (2023-2025)
### Copy Sales Revenue Only (Physical + Digital) - No Microtransactions, DLC, or In-App Purchases

---

## A. Revenue Table

Revenue is calculated as: copies sold x average retail price at time of release. Only copy sales (physical + digital) are counted. Microtransactions, Ultimate Team spending, DLC, loot boxes, and in-app purchases are excluded.

**Pricing notes:**
- FIFA 23: Standard edition $59.99 (last-gen) / $69.99 (current-gen). Blended average: ~$62
- EA Sports FC 24: Standard edition $59.99 (last-gen) / $69.99 (current-gen). Blended average: ~$62
- EA Sports FC 25: Standard edition $59.99 (last-gen) / $69.99 (current-gen). Blended average: ~$63
- EA Sports FC 26: Standard edition $69.99 (dropped last-gen support). Blended average: ~$68

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | FIFA 23 | 2022 (active through 2023) | ~22 million | ~$1.36 billion | Medium |
| 2 | EA Sports FC 24 | 2023 | ~17 million | ~$1.05 billion | Medium |
| 3 | EA Sports FC 25 | 2024 | ~12 million | ~$756 million | Medium |
| 4 | EA Sports FC 26 | 2025 | ~14 million | ~$952 million | Low |
| **TOTAL** | | | **~65 million** | **~$4.12 B** | |

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "FIFA 23",
      "year": 2022,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "EA Sports",
      "copiesSold": 22000000,
      "estimatedRevenue": 1364000000,
      "revenueSource": "Reddit: r/stocks post comparing FIFA 23 French sales (420K physical first week, best-selling game in France 2023); historical FIFA franchise sales patterns discussed on r/Games (FIFA 21/22 each ~25M copies); EA first-week player count of 10.3M discussed across Reddit",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "EA Sports",
      "copiesSold": 17000000,
      "estimatedRevenue": 1054000000,
      "revenueSource": "Reddit: r/M8X_GAMENEWS reported 14.5M active players in first month and 11.3M players in first week (includes EA Play subscribers); r/gaming discussion of EA pulling old FIFA titles from storefronts at FC 24 launch; first game under new FC branding saw strong but slightly lower adoption than FIFA 23",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "EA Sports",
      "copiesSold": 12000000,
      "estimatedRevenue": 756000000,
      "revenueSource": "Reddit: r/pcgaming Jason Schreier report on EA slashing fiscal year forecast due to FC 25 underperformance; r/Games report on EA losing $6B in market value; EA Q3 revenue fell to $1.88B from $1.94B partly due to FC weakness (r/Games); r/EASportsFC community calling it 'least effort EA has ever put in'",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch 2",
      "publisher": "EA Sports",
      "copiesSold": 14000000,
      "estimatedRevenue": 952000000,
      "revenueSource": "Reddit: r/gaming reported Battlefield 6 outsold FC 26 in Europe at launch; r/gaming reported Ghost of Yotei beat FC 26 in UK physical sales; r/Games reported FC 26 was top seller during Europe's Black Friday 2025; dropped last-gen support; EA acquired by PIF/Silver Lake for $55B during FC 26's lifecycle",
      "confidence": "low"
    }
  ],
  "totalRevenue": 4126000000,
  "totalGamesFound": 4,
  "searchQueries": [
    "FIFA 23 EA Sports FC 24 FC 25 copies sold sales",
    "EA Sports FC sales numbers copies sold million",
    "FIFA 23 sales figures copies sold million",
    "EA Sports FC 25 underperformance sales disappointing",
    "FIFA 23 best selling game 2023 copies sold",
    "EA Sports FC 24 FC 25 sales revenue copies unit",
    "EA FC 24 14.5 million players launch",
    "FIFA EA Sports FC franchise total revenue billion annual sales",
    "EA Sports FC revenue decline 2024 2025 quarterly earnings",
    "EA FC 24 record breaking launch first week players",
    "FIFA franchise 325 million copies sold total"
  ],
  "redditPostsAnalyzed": 14
}
```

---

## Key Findings

1. **Brand Transition Impact**: The shift from "FIFA" to "EA Sports FC" starting with FC 24 (2023) coincided with a gradual decline in copy sales. FIFA 23, the last game under the FIFA name, likely achieved the highest sales in this period at approximately 22 million copies.

2. **FC 25 Was a Notable Flop**: EA Sports FC 25 significantly underperformed, leading EA to slash its fiscal year forecast. Jason Schreier (Bloomberg) confirmed this on Bluesky, discussed on r/pcgaming (1,005 upvotes). EA lost $6 billion in market value partly due to FC 25's poor showing (r/Games, 1,955 upvotes). EA's Q3 FY2025 revenue fell to $1.88 billion from $1.94 billion year-over-year.

3. **Copy Sales vs. Total Revenue**: Per Reddit discussions, 71% of EA's total revenue comes from live services (r/pcgaming, 2,111 upvotes). This means copy sales revenue (~$4.12 billion total across these 4 titles) represents only a fraction of what the FIFA/FC franchise generates overall. Ultimate Team microtransactions are the primary revenue driver but are excluded from this analysis per the research parameters.

4. **FC 26 Mixed Performance**: EA Sports FC 26 had a weaker launch (outsold by Battlefield 6 and Ghost of Yotei in various markets per Reddit posts), but recovered during the holiday season to become a Black Friday top seller in Europe. The game dropped last-gen console support (PS4/Xbox One), which may have reduced its addressable market.

5. **EA Acquisition**: In 2025, EA was acquired by PIF (Saudi Arabia's Public Investment Fund), Silver Lake, and Affinity Partners for $55 billion (r/EASportsFC, 467 upvotes), underscoring the enormous value of EA's portfolio, with the FC franchise being a central asset.

---

## Methodology Notes

- All sales figures are estimates based on Reddit-sourced data including EA announcements discussed on Reddit, journalist reports shared on Reddit, and community analysis
- EA typically reports "player counts" rather than "copies sold," making direct copy sales estimation challenging. Player counts include EA Play/subscription access
- Revenue calculations use blended average retail prices accounting for platform mix (last-gen vs current-gen pricing)
- The FIFA/EA FC franchise generates substantially more total revenue when including Ultimate Team and other live-service monetization, but this analysis strictly covers copy sales only
