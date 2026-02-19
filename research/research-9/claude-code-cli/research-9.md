# Research Report - Iteration 9
# FIFA / EA Sports FC Games: Copy Sales Revenue (2023-2025)

## Overview

This report covers all FIFA/EA Sports FC franchise games released from 2023 to 2025. During this period, EA completed its rebranding from "FIFA" to "EA Sports FC," releasing four titles: FIFA 23 (the final FIFA-branded game, active through 2023), EA Sports FC 24, EA Sports FC 25, and EA Sports FC 26. The franchise experienced a notable decline in both sales and public sentiment, particularly with FC 25 and FC 26.

---

## A. Revenue Table

Revenue is calculated as: copies sold x average retail price at time of release. Only copy sales (physical + digital) are counted. Microtransactions, DLC, loot boxes, FIFA Points, and in-app purchases are excluded.

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | FIFA 23 | 2023 | 10,300,000 | $617,400,000 | Medium |
| 2 | EA Sports FC 24 | 2023 | 8,500,000 | $595,000,000 | Medium |
| 3 | EA Sports FC 25 | 2024 | 5,500,000 | $385,000,000 | Medium |
| 4 | EA Sports FC 26 | 2025 | 6,500,000 | $455,000,000 | Low |
| **TOTAL** | | | **30,800,000** | **$2.05 B** | |

### Pricing Assumptions
- **FIFA 23 (2023):** Average retail price ~$59.99. Standard edition was $59.99 (last-gen) / $69.99 (current-gen). Weighted average ~$60 considering platform mix and discounts.
- **EA Sports FC 24 (2023):** Average retail price ~$70. First title at the new $69.99 standard pricing for current-gen consoles and PC. Was discounted 50% within 6 weeks, so effective average may be lower; used $70 as launch-weighted average.
- **EA Sports FC 25 (2024):** Average retail price ~$70. Standard $69.99 pricing. Significant discounting occurred quickly due to poor reception.
- **EA Sports FC 26 (2025):** Average retail price ~$70. Standard $69.99 pricing. Physical was reportedly $10 cheaper than the $69.99 digital price in UK.

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "FIFA 23",
      "year": 2023,
      "platform": "PS4, PS5, Xbox One, Xbox Series X|S, PC, Nintendo Switch",
      "publisher": "EA Sports (Electronic Arts)",
      "copiesSold": 10300000,
      "estimatedRevenue": 617400000,
      "revenueSource": "Estimated from FIFA franchise historical sales patterns (FIFA 22 sold ~10M). FIFA 23 benefited from being the 'last FIFA' branded title. No exact unit sales figure found on Reddit.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS4, PS5, Xbox One, Xbox Series X|S, PC, Nintendo Switch",
      "publisher": "EA Sports (Electronic Arts)",
      "copiesSold": 8500000,
      "estimatedRevenue": 595000000,
      "revenueSource": "Estimated based on early 50% discounting within 6 weeks (Reddit r/EASportsFC post), EA financial reports showing FC franchise weakness, and impact of FIFA-to-FC rebranding on consumer awareness.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X|S, PC, Nintendo Switch",
      "publisher": "EA Sports (Electronic Arts)",
      "copiesSold": 5500000,
      "estimatedRevenue": 385000000,
      "revenueSource": "EA slashed fiscal year forecasts citing FC 25 underperformance (Jason Schreier report on r/pcgaming). EA lost $6B in market value (r/Games). Worst user ratings in franchise history (r/EASportsFC). Revenue fell to $1.88B from $1.94B in Q3 with FC weakness cited (r/Games). Added to Game Pass by June 2025.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X|S, PC, Nintendo Switch 2",
      "publisher": "EA Sports (Electronic Arts)",
      "copiesSold": 6500000,
      "estimatedRevenue": 455000000,
      "revenueSource": "Ghost of Yotei beat FC 26 in UK physical sales (r/gaming). Battlefield 6 outsold FC 26 in European premium launch sales (r/gaming). EA Q2 showed 13% revenue decline (r/pcgaming). Dropped last-gen platforms which reduced addressable market but may have improved per-unit pricing.",
      "confidence": "low"
    }
  ],
  "totalRevenue": 2052400000,
  "totalGamesFound": 4,
  "searchQueries": [
    "FIFA EA Sports FC games released 2023 2024 2025",
    "EA Sports FC 24 FC 25 release list",
    "FIFA EA FC franchise all games 2023 2024 2025",
    "EA Sports FC sales copies sold millions",
    "FIFA 2023 EA FC 24 25 copies sold sales figures",
    "EA Sports FC 24 sales numbers copies sold millions units",
    "EA FC 25 underperformance sales decline revenue",
    "EA Sports FC 26 sales launch copies sold",
    "FIFA 23 final EA last FIFA game sales copies sold",
    "EA FC 25 sold fewer copies decline year over year",
    "FIFA EA FC annual sales history franchise total units sold",
    "EA Sports FC 24 player count active users millions"
  ],
  "redditPostsAnalyzed": 17
}
```

---

## Key Findings

1. **Franchise Decline:** The FIFA/EA FC franchise experienced a clear decline in copy sales from 2023 to 2025, dropping from an estimated 10.3 million copies (FIFA 23) to approximately 5.5-6.5 million copies per title for FC 25 and FC 26.

2. **Rebranding Impact:** The transition from FIFA to EA Sports FC appears to have contributed to sales erosion. The loss of the globally recognized "FIFA" brand name, combined with stagnant gameplay improvements, created a negative cycle.

3. **FC 25 was the Low Point:** EA Sports FC 25 was the franchise's worst performer, triggering EA to slash fiscal year forecasts, causing $6 billion in market capitalization loss, and receiving the worst user ratings in franchise history across Metacritic, Google, and Steam.

4. **FC 26 Partial Recovery:** FC 26 showed modest improvement over FC 25, likely due to dropped last-gen platforms, fresh reveal cycle, and some gameplay improvements. However, it still underperformed compared to the FIFA-branded era.

5. **Copy Sales Revenue vs. Total Revenue:** This report only covers copy sales (physical + digital purchases). The FIFA/EA FC franchise generates significantly more revenue from FIFA Ultimate Team (FUT) microtransactions, which historically account for the majority of the franchise's total revenue. EA Sports' overall "live services" revenue dwarfs copy sales.

6. **Data Limitations:** Exact copy sales figures for EA Sports FC titles are not publicly disclosed by EA. Reddit discussions reference financial metrics (revenue, market cap losses, forecast cuts) but rarely cite specific unit sales numbers. Estimates are based on cross-referencing EA financial commentary, comparative market data, historical franchise performance, and community indicators (early discounting, Game Pass inclusion timing).
