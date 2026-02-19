# Research Report - Iteration 10
# FIFA / EA Sports FC Games: Copy Sales Revenue (2023-2025)

## Overview

This report covers all FIFA/EA Sports FC franchise game releases from 2023 to 2025. In 2023, EA rebranded the FIFA series to "EA Sports FC" after ending its licensing deal with FIFA. Three titles were released in this period: EA Sports FC 24 (2023), EA Sports FC 25 (2024), and EA Sports FC 26 (2025). The franchise experienced a notable decline in sales over this period, with FC 25 being the worst user-rated entry in franchise history and causing EA to lose $6 billion in market value.

---

## A. Revenue Table

Revenue is calculated as: copies sold x average retail price at time of release. Only copy sales (physical + digital) are counted. Microtransactions, DLC, loot boxes, FIFA Points/FC Points, and in-app purchases are excluded.

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | 11,000,000 | $715,000,000 | Medium |
| 2 | EA Sports FC 25 | 2024 | 7,500,000 | $525,000,000 | Medium |
| 3 | EA Sports FC 26 | 2025 | 7,000,000 | $490,000,000 | Low |
| **TOTAL** | | | **25,500,000** | **$1.73 B** | |

### Revenue Calculation Notes

- **EA Sports FC 24** ($65 avg): Launched at $69.99 (PS5/Xbox Series X) and $59.99 (PS4/Xbox One/PC). The Switch Legacy Edition was $39.99. Weighted average ~$65 accounting for platform mix and discounts during the sales cycle.
- **EA Sports FC 25** ($70 avg): Standard edition launched at $69.99 across current-gen platforms. Ultimate Edition was $99.99. Weighted average ~$70 reflecting the shift toward current-gen pricing.
- **EA Sports FC 26** ($70 avg): Launched at $69.99 standard, dropped last-gen consoles (PS4/Xbox One). Average price ~$70.

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 11000000,
      "estimatedRevenue": 715000000,
      "revenueSource": "Reddit discussions of EA earnings calls, industry analyst estimates, comparisons to FIFA 23 sales (~10-11M first year). EA reported 14.5M accounts in first week but this includes EA Play trial users. Franchise met initial expectations per EA FY2024 earnings.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 7500000,
      "estimatedRevenue": 525000000,
      "revenueSource": "Reddit posts citing Bloomberg/Jason Schreier reporting on EA slashing fiscal forecasts due to FC 25 underperformance. EA lost $6B in market value. Worst user-rated game in franchise history per Metacritic/Steam/Google. Revenue fell from $1.94B to $1.88B in Q3 FY2025. Added to Game Pass June 2025 suggesting sales dried up. Estimated 20-30% decline from FC 24.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 7000000,
      "estimatedRevenue": 490000000,
      "revenueSource": "Reddit posts showing Ghost of Yotei and Battlefield 6 outsold FC 26 at launch in UK/Europe. EA Q2 FY2026 showed continued revenue decline partly attributed to FC franchise. Dropped last-gen consoles reducing addressable market. Franchise trajectory suggests continued but stabilizing decline.",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1730000000,
  "totalGamesFound": 3,
  "searchQueries": [
    "FIFA EA Sports FC games released 2023 2024 2025",
    "EA Sports FC 24 FC 25 sales copies sold millions",
    "EA Sports FC 24 25 copies sold unit sales",
    "EA Sports FC 24 sales numbers players",
    "FC 25 underperformance sales decline EA revenue",
    "EA Sports FC 24 million copies sold unit sales VGChartz",
    "FIFA EA FC 24 first week launch copies sold 11 million 14 million",
    "FC 25 sales drop FIFA rebrand worst selling"
  ],
  "redditPostsAnalyzed": 14
}
```

---

## Key Findings

1. **The FIFA-to-FC rebrand (2023)** did not significantly hurt initial sales for FC 24, which performed roughly in line with prior FIFA titles at ~11 million copies.

2. **FC 25 was a turning point** -- it was the worst user-rated game in franchise history across Metacritic, Google, and Steam. EA slashed its fiscal year forecast and lost $6 billion in market value. Sales declined an estimated 20-30% from FC 24.

3. **FC 26 continued the decline** -- it was outsold at launch in multiple regions by non-sports titles (Ghost of Yotei, Battlefield 6). Dropping last-gen console support further reduced the addressable market.

4. **Total copy sales revenue for 2023-2025: approximately $1.73 billion** -- this excludes the franchise's much larger microtransaction/Ultimate Team revenue, which EA does not break out by title.

5. **Important caveat:** EA does not publicly disclose unit sales for individual titles. All figures are estimates derived from Reddit discussions of EA earnings calls, industry analyst reports, journalist reporting (Bloomberg, VGC, Jason Schreier), and comparisons to historical FIFA franchise data.
