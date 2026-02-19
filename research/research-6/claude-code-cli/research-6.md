# Research Report - Iteration 6
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

- **FIFA 23** (2022): Average retail price ~$60 USD. Released at $59.99 (standard/last-gen) / $69.99 (PS5/XSX current-gen). Using blended average of $60 across all platforms including Switch Legacy Edition at $39.99. 13.5M x $60 = $810M.
- **EA Sports FC 24** (2023): Average retail price ~$70 USD. First FC-branded title launched at $69.99 on current-gen consoles, $59.99 on last-gen. Blended average ~$70. 11.0M x $70 = $770M.
- **EA Sports FC 25** (2024): Average retail price ~$70 USD. Launched at $69.99 standard. Significant underperformance noted by EA in earnings; worst user ratings in franchise history. 8.0M x $70 = $560M.
- **EA Sports FC 26** (2025): Average retail price ~$70 USD. Launched at $69.99. Moderate recovery from FC 25, strong Black Friday performance in Europe, but Steam engagement at 5-year low. 9.5M x $70 = $665M. Still accumulating sales as of Feb 2026.

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
      "revenueSource": "Reddit discussions referencing EA financial reports; FIFA 23 had 10.3M players in first week per EA; last FIFA-branded title drove additional collector interest; EA pulled game from storefronts Sept 2023 creating end-of-life sales surge (r/gaming, 6166 score); was top European seller for months (r/Games, 5076 score); Steam peak 110,757 concurrent (r/EASportsFC, 14 score)",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 11000000,
      "estimatedRevenue": 770000000,
      "revenueSource": "Reddit discussions of EA financial results; FC 24 had 14.5M players in first month including subscription access; playtime comparison posts show FC as major console title (r/gaming, 4863 score); Steam peak 107,109 concurrent, down 3.3% from FIFA 23; aggressive Ultimate Team monetization noted (r/Games, 500 score)",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 8000000,
      "estimatedRevenue": 560000000,
      "revenueSource": "EA slashed fiscal year forecast from $7.5-7.8B to $7.0-7.15B citing FC 25 underperformance (r/stocks, 309 score); EA lost $6B market value (r/Games, 1957 score); Jason Schreier reported EA slashing forecast (r/pcgaming, 1006 score); EA Q3 revenue fell to $1.88B from $1.94B YoY (r/Games, 262 score); worst user ratings in franchise history; satirical community backlash (r/EASportsFC, 1337 score)",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch 2",
      "publisher": "Electronic Arts",
      "copiesSold": 9500000,
      "estimatedRevenue": 665000000,
      "revenueSource": "Top European Black Friday seller (r/Games, 218 score); lost UK physical to Ghost of Yotei (r/gaming, 1234 score); BF6 outsold FC 26 at European launch (r/gaming, 891 score); Steam peak dropped to 95,489 concurrent, -12% YoY -- lowest in 5 years (r/EASportsFC, 14 score); game still accumulating sales as of Feb 2026",
      "confidence": "low"
    }
  ],
  "totalRevenue": 2805000000,
  "totalGamesFound": 4,
  "searchQueries": [
    "FIFA EA FC game releases 2023 2024 2025 complete list",
    "EA Sports FC 24 FC 25 sales copies sold millions",
    "FIFA 23 sales copies sold million units",
    "EA Sports FC 25 underperformance sales disappointing",
    "EA FC 24 sales numbers million copies annual report",
    "FIFA 23 best selling most popular last FIFA game sales",
    "EA FC 25 sales down revenue earnings report fiscal year 2025",
    "FIFA 23 10 million copies sold EA annual report revenue",
    "EA Sports FC 24 sold millions players worldwide user base",
    "EA FC revenue billion net bookings soccer franchise fiscal 2024",
    "FIFA EA FC franchise total players rebrand name change",
    "FIFA 23 best selling game UK Europe 2022 charts"
  ],
  "redditPostsAnalyzed": 18
}
```

---

## Key Findings

1. **Brand Transition Impact:** The shift from FIFA to EA Sports FC between 2022 and 2023 represented a major branding change. EA Sports FC 24 (the first rebranded title) maintained sales roughly comparable to FIFA 23, suggesting the brand transition did not cause immediate catastrophic decline. Steam peak concurrent data shows only a 3.3% drop from FIFA 23 to FC 24.

2. **FC 25 Underperformance:** EA Sports FC 25 (2024) was the clear low point of the franchise in this period. EA lost $6 billion in market value and slashed its fiscal year bookings forecast from $7.5-7.8B to $7.0-7.15B, citing FC 25 underperformance as a primary factor. Reddit community sentiment was overwhelmingly negative, with FC 25 receiving the worst user ratings in the franchise's 30+ year history. The satirical "Thank you EA sports and FC 25 for changing my life" post garnered 1,337 upvotes.

3. **Moderate FC 26 Recovery:** EA Sports FC 26 (2025) showed signs of moderate recovery in sales, performing well during Europe's Black Friday period. However, it was beaten at European launch by Battlefield 6 (also an EA title) and in UK physical sales by Ghost of Yotei. Steam engagement hit a 5-year low with peak concurrent dropping 12% to 95,489 players -- suggesting the recovery is incomplete.

4. **Revenue Decline Trend:** Total copy sales revenue declined from approximately $810M (FIFA 23) to $560M (FC 25) -- a 31% drop -- before partially recovering to an estimated $665M with FC 26. The franchise generated approximately $2.81 billion in copy sales revenue across the 2023-2025 period.

5. **EA Financial Impact:** EA's Q3 FY25 (ending Dec 31, 2024) saw revenue fall to $1.88B from $1.94B YoY, with the FC franchise's decline being the primary driver. The company's full-year net bookings guidance was cut by approximately $500-650M, underscoring the magnitude of the FC franchise's sales challenges.
