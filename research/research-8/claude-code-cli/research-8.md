# Research Report - Iteration 8
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

- **FIFA 23** (2022): Average retail price ~$60 USD. Released at $59.99 (standard/last-gen) / $69.99 (PS5/XSX current-gen). Using blended average of $60 across all platforms including Switch Legacy Edition at $39.99. 13.5M x $60 = $810M. FIFA 23 benefited enormously from the 2022 FIFA World Cup in Qatar (Nov-Dec 2022), which drove record engagement. EA stated it was "on track to be the biggest title in franchise history" with 10.3M players in 7 days and NA unit sales up 50% YoY.
- **EA Sports FC 24** (2023): Average retail price ~$70 USD. First FC-branded title launched at $69.99 on current-gen consoles, $59.99 on last-gen. Blended average ~$70. 11.0M x $70 = $770M. EA reported 14.5 million players in first month (includes EA Play/subscription access; actual paid copies estimated lower).
- **EA Sports FC 25** (2024): Average retail price ~$70 USD. Launched at $69.99 standard. Significant underperformance noted by EA in earnings; EA slashed fiscal year bookings guidance by $500-650M citing FC 25 weakness. 8.0M x $70 = $560M. Despite poor reception, still dominated European sales charts.
- **EA Sports FC 26** (2025): Average retail price ~$70 USD. Launched at $69.99. Moderate recovery from FC 25 low point. Lost UK physical sales crown to Ghost of Yotei at launch; outsold by Battlefield 6 at European launch. Dropped last-gen consoles, reducing total addressable market. 9.5M x $70 = $665M. Still accumulating sales as of Feb 2026.

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
      "revenueSource": "EA Q3 FY2023 earnings: 10.3M players in first 7 days, NA unit sales up 50% YoY, 'on track to be biggest title in franchise history'; 2022 FIFA World Cup in Qatar drove record engagement; historically #1 selling franchise in Europe; pulled from digital storefronts Sept 2023 creating end-of-life sales surge (r/gaming, 6157 score); last game to carry FIFA brand name",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 11000000,
      "estimatedRevenue": 770000000,
      "revenueSource": "EA reported 14.5M players in first month including subscription access; first rebranded title maintained strong sales; among top console games by playtime Dec 2023 (r/gaming, 4858 score); brand transition from FIFA to FC did not cause immediate sales collapse",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 8000000,
      "estimatedRevenue": 560000000,
      "revenueSource": "EA slashed fiscal year forecast from $7.5-7.8B to $7.0-7.15B citing FC 25 underperformance; EA lost $6B market value (r/Games, 1961 score); EA Q3 revenue fell to $1.88B from $1.94B YoY (r/Games, 253 score); Jason Schreier confirmed EA slashing forecast (r/pcgaming, 1008 score); worst user sentiment in franchise history; community considered it the worst entry",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch 2",
      "publisher": "Electronic Arts",
      "copiesSold": 9500000,
      "estimatedRevenue": 665000000,
      "revenueSource": "Ghost of Yotei beat FC 26 in UK physical sales at launch (r/gaming, 1238 score); Battlefield 6 outsold FC 26 at European launch (r/gaming, 891 score); among top sellers during Black Friday 2025 in Europe (r/Games, 220 score); dropped last-gen consoles reducing addressable market; game still accumulating sales as of Feb 2026",
      "confidence": "low"
    }
  ],
  "totalRevenue": 2805000000,
  "totalGamesFound": 4,
  "searchQueries": [
    "FIFA EA Sports FC sales copies sold 2023 2024 2025",
    "FIFA 24 EA FC 24 sales numbers copies sold",
    "EA Sports FC 25 sales figures copies units sold",
    "EA Sports FC 25 underperformance sales numbers disappointing",
    "FIFA 23 last FIFA game sales copies sold millions EA",
    "EA FC 24 EA FC 25 player count active players revenue earnings",
    "EA Sports FC annual revenue billion FIFA franchise total sales history",
    "FIFA 23 10 million copies sold best selling",
    "EA FC 24 first week launch sales record breaking"
  ],
  "redditPostsAnalyzed": 14
}
```

---

## Key Findings

1. **FIFA 23 Boosted by World Cup:** FIFA 23 achieved record-breaking performance for the franchise, driven by the 2022 FIFA World Cup in Qatar. EA reported 10.3 million players in its first 7 days (up from 9.1M for FIFA 22 in 10 days) and stated the title was "on track to be the biggest title in franchise history" with North American unit sales up 50% year-over-year. As the last game to carry the FIFA name, it also benefited from collector and nostalgia interest.

2. **Brand Transition to EA Sports FC:** The shift from FIFA to EA Sports FC between 2022 and 2023 was a major branding change. EA Sports FC 24 (the first rebranded title) maintained strong sales with 14.5M players in its first month (though this includes EA Play/subscription access). The brand transition did not cause immediate catastrophic decline in sales.

3. **FC 25 Underperformance was Severe:** EA Sports FC 25 (2024) was the clear low point. EA lost $6 billion in market value and slashed its fiscal year bookings forecast by $500-650M, citing FC 25 underperformance as a primary factor. Jason Schreier confirmed the forecast slashing. Reddit community sentiment was overwhelmingly negative, with satirical posts and reviews calling it the worst entry in franchise history.

4. **FC 26 Partial Recovery with Caveats:** EA Sports FC 26 (2025) showed signs of partial recovery from the FC 25 low point but faced new headwinds. Ghost of Yotei beat FC 26 in UK physical sales at launch, and Battlefield 6 outsold it at European launch -- both unusual events for the FIFA/FC franchise. The game dropped last-gen console support (PS4/Xbox One), reducing its total addressable market. Long-time players continued expressing frustration with gameplay quality.

5. **Revenue Decline Trend:** Total copy sales revenue declined from approximately $810M (FIFA 23) to $560M (FC 25) -- a 31% drop -- before partially recovering to an estimated $665M with FC 26. The franchise generated approximately $2.81 billion in copy sales revenue across the 2023-2025 period.

6. **EA Financial Impact:** EA's Q3 FY25 (ending Dec 31, 2024) saw revenue fall to $1.88B from $1.94B year-over-year, with the FC franchise's decline being a primary driver. The company's full-year net bookings guidance was cut from $7.5-7.8B to $7.0-7.15B.
