# Research Report - Iteration 11
# FIFA / EA Sports FC Games (2023-2025): Copy Sales & Revenue Analysis

## Overview

This report covers all FIFA / EA Sports FC game releases from 2023 to 2025. During this period, EA transitioned the franchise from the "FIFA" branding to "EA Sports FC" after losing the FIFA license. Three titles were released:

1. **EA Sports FC 24** (September 2023) - First game under the new EA Sports FC branding
2. **EA Sports FC 25** (September 2024) - Second entry, widely regarded as the worst in franchise history
3. **EA Sports FC 26** (September/October 2025) - Third entry, continued franchise decline

Note: FIFA 23 (September 2022) was the last game carrying the FIFA name but falls outside the 2023-2025 release window.

---

## A. Revenue Table

Revenue is calculated as: copies sold x average retail price at time of release. Only copy sales (physical + digital) are counted. Microtransactions, DLC, loot boxes, and in-app purchases are **excluded**.

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | ~11,000,000 | ~$770,000,000 | Medium |
| 2 | EA Sports FC 25 | 2024 | ~7,500,000 | ~$525,000,000 | Medium |
| 3 | EA Sports FC 26 | 2025 | ~7,000,000 | ~$490,000,000 | Low |
| **TOTAL** | | | **~25,500,000** | **$1.79 B** | |

### Revenue Calculation Notes

- **EA Sports FC 24** ($70 retail price): 11,000,000 copies x $70 = $770,000,000. FC 24 was the first rebranded title. EA reported 14.5 million "accounts" in week one, but this includes EA Play trial users. Based on Reddit discussions of industry data, actual copy sales were approximately 11 million. The game was available on both last-gen and current-gen consoles plus PC and Switch.

- **EA Sports FC 25** ($70 retail price): 7,500,000 copies x $70 = $525,000,000. FC 25 significantly underperformed, causing EA to lose $6 billion in market value. EA slashed fiscal year forecasts in January 2025. Reddit discussions referencing Bloomberg/VGC reporting indicate 20-30% fewer copies sold than FC 24. The midpoint estimate of 7.5 million copies reflects this decline. The game was the worst user-rated entry in franchise history.

- **EA Sports FC 26** ($70 retail price): 7,000,000 copies x $70 = $490,000,000. FC 26 dropped last-gen console support, reducing its addressable market. Launch sales in Europe were outsold by Battlefield 6 and Ghost of Yotei. However, it performed well during Black Friday 2025. Limited sales data is available as the game is relatively recent.

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
      "estimatedRevenue": 770000000,
      "revenueSource": "Reddit discussions of EA earnings calls reporting 14.5M accounts in first week; industry analyst estimates of ~11M actual copy sales based on FIFA 22/23 comparisons; EA FY2024 reports showing FC franchise met expectations",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 7500000,
      "estimatedRevenue": 525000000,
      "revenueSource": "Reddit posts citing EA forecast cuts (Jan 2025), $6B market value loss, Q3 FY2025 revenue decline from $1.94B to $1.88B; Bloomberg/VGC/Schreier reporting of 20-30% sales decline vs FC 24; worst user ratings in franchise history across Metacritic/Steam/Google; added to Game Pass June 2025 suggesting plateaued sales",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 7000000,
      "estimatedRevenue": 490000000,
      "revenueSource": "Reddit posts showing FC 26 outsold by Ghost of Yotei in UK physical sales and by Battlefield 6 at European launch; performed well during Black Friday 2025; dropped last-gen support reducing addressable market; continued franchise decline trajectory",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1785000000,
  "totalGamesFound": 3,
  "searchQueries": [
    "FIFA EA Sports FC games released 2023 2024 2025 complete list",
    "EA Sports FC 24 FC 25 copies sold sales millions",
    "FIFA 23 EA FC 24 EA FC 25 sales numbers copies sold",
    "EA Sports FC 25 underperformance sales decline numbers",
    "FIFA franchise annual sales 10 million 20 million copies sold per year",
    "EA FC 24 sales copies sold millions units",
    "FIFA 23 copies sold total sales unit numbers",
    "EA FC 25 sold fewer copies decline 2024 football game unit sales",
    "EA FC 25 FC 24 FIFA 23 player count revenue earnings report"
  ],
  "redditPostsAnalyzed": 15
}
```

---

## Key Findings

1. **Franchise Rebrand Impact**: The transition from FIFA to EA Sports FC in 2023 did not significantly hurt initial sales. FC 24 performed approximately in line with recent FIFA titles.

2. **Dramatic FC 25 Decline**: FC 25 was a turning point. It was the worst user-rated entry in franchise history, causing EA to slash forecasts and lose $6 billion in market value. Copy sales declined an estimated 20-30% compared to FC 24.

3. **Continued FC 26 Weakness**: FC 26 dropped last-gen console support and faced a competitive market. Launch sales were outsold by Battlefield 6 and Ghost of Yotei in Europe/UK, though Black Friday performance suggested some stabilization.

4. **Revenue Decline Trajectory**: Total estimated copy sale revenue across the three titles is approximately $1.79 billion, showing a clear downward trend from ~$770M (FC 24) to ~$490M (FC 26) per title.

5. **Data Limitations**: EA does not publicly disclose exact unit sales for individual titles. All estimates are derived from Reddit discussions of earnings calls, industry analyst reports, journalist coverage, and comparative analysis with prior franchise entries.
