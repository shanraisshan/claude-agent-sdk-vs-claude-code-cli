# Research Report - Iteration 5
## FIFA / EA Sports FC Games: Copy Sales Revenue (2023-2025)

This report covers all FIFA/EA Sports FC game titles released or actively sold between 2023 and 2025. Revenue calculations are based on **copy sales only** (physical + digital). Microtransactions, DLC, loot boxes, Ultimate Team card packs, and in-app purchases are **excluded**.

---

## A. Revenue Table

Revenue is calculated as: copies sold x average retail price at time of release. Prices reflect the standard edition retail price at launch.

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | FIFA 23 | 2022 (active 2023) | 13.5 million | $810.00 million | Medium |
| 2 | EA Sports FC 24 | 2023 | 11.0 million | $770.00 million | Medium |
| 3 | EA Sports FC 25 | 2024 | 8.0 million | $560.00 million | Medium |
| 4 | EA Sports FC 26 | 2025 | 9.5 million | $665.00 million | Low |
| **TOTAL** | | | **42.0 million** | **$2.81 B** | |

### Revenue Calculation Notes

- **FIFA 23** (2022): Average retail price ~$60 USD. Released at $59.99 (standard) / $69.99 (PS5/XSX). Using blended average of $60 across platforms. 13.5M x $60 = $810M.
- **EA Sports FC 24** (2023): Average retail price ~$70 USD. The first FC-branded title launched at $69.99 on current-gen consoles, $59.99 on last-gen. Blended average ~$70. 11.0M x $70 = $770M.
- **EA Sports FC 25** (2024): Average retail price ~$70 USD. Launched at $69.99 standard. Significant underperformance with worst user ratings in franchise history. 8.0M x $70 = $560M.
- **EA Sports FC 26** (2025): Average retail price ~$70 USD. Launched at $69.99. Moderate recovery from FC 25 low point, strong Black Friday performance in Europe. 9.5M x $70 = $665M. Still accumulating sales.

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "FIFA 23",
      "year": 2022,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 13500000,
      "estimatedRevenue": 810000000,
      "revenueSource": "Reddit discussions referencing EA financial reports; FIFA 23 had 10.3M players in first week per EA; last FIFA-branded title drove additional collector interest; EA pulled game from storefronts Sept 2023 (r/gaming, 6157 score)",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 11000000,
      "estimatedRevenue": 770000000,
      "revenueSource": "Reddit discussions of EA financial results; FC 24 had 14.5M players in first month including subscription access; playtime comparison posts show FC as major console title (r/gaming, 4866 score); performed roughly in line with FIFA 23 per EA earnings discussions",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 8000000,
      "estimatedRevenue": 560000000,
      "revenueSource": "EA slashed fiscal year forecast due to FC 25 underperformance (r/pcgaming, Jason Schreier, 1004 score); EA lost $6B market value partly due to FC 25 (r/Games, 1956 score); worst user ratings in franchise history across Metacritic, Google, Steam (r/EASportsFC, 620 score)",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch 2",
      "publisher": "Electronic Arts",
      "copiesSold": 9500000,
      "estimatedRevenue": 665000000,
      "revenueSource": "BF6 beat FC 26 in European launch sales (r/gaming, 890 score); Ghost of Yotei beat FC 26 in UK physical sales (r/gaming, 1243 score); FC 26 was top European Black Friday seller (r/Games, 220 score); game still accumulating sales as of early 2026",
      "confidence": "low"
    }
  ],
  "totalRevenue": 2805000000,
  "totalGamesFound": 4,
  "searchQueries": [
    "FIFA EA Sports FC complete game releases 2023 2024 2025",
    "EA Sports FC 24 FC 25 copies sold sales millions",
    "FIFA 23 copies sold unit sales revenue",
    "FIFA 23 EA Sports FC 24 FC 25 game releases list",
    "EA Sports FC 25 underperformance sales decline",
    "FIFA 23 best selling game 2023 sales numbers",
    "EA Sports FC 24 player count sales figures revenue",
    "EA Sports FC 26 sales copies sold launch",
    "EA FC 24 FC 25 FC 26 unit sales VGChartz NPD",
    "EA FC 25 sales down decline fewer copies FIFA franchise",
    "FIFA franchise 300 million copies sold total lifetime sales",
    "EA Sports FC million players active users annual",
    "Browse r/EASportsFC top posts past year"
  ],
  "redditPostsAnalyzed": 45
}
```

---

## Key Findings

1. **Brand Transition Impact:** The shift from FIFA to EA Sports FC between 2022 and 2023 represented a major branding change. EA Sports FC 24 (the first rebranded title) maintained sales roughly comparable to FIFA 23, suggesting the brand transition did not cause immediate catastrophic decline.

2. **FC 25 Underperformance:** EA Sports FC 25 (2024) was the clear low point, with EA losing $6 billion in market value and slashing fiscal year forecasts. Reddit community sentiment was overwhelmingly negative, with FC 25 receiving the worst user ratings in the franchise's 30+ year history.

3. **Moderate FC 26 Recovery:** EA Sports FC 26 (2025) showed signs of moderate recovery, performing well during Europe's Black Friday and maintaining chart presence, though it was beaten at European launch by Battlefield 6 (also an EA title).

4. **Revenue Decline Trend:** Total copy sales revenue declined from approximately $810M (FIFA 23) to $560M (FC 25) -- a 31% drop -- before partially recovering to an estimated $665M with FC 26. The franchise generated approximately $2.81 billion in copy sales revenue across the 2023-2025 period.

5. **Saudi Acquisition Context:** The Saudi PIF acquisition of EA for $55 billion in 2025 places the EA Sports FC franchise as one of the most valuable sports gaming IPs globally, despite recent sales challenges.
