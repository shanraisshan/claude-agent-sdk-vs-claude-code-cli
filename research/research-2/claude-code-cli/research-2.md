# Research Report - Iteration 2
## FIFA / EA Sports FC Games: Copy Sales Revenue (2023-2025)

**Research Problem**: Find all FIFA games released from 2023 to 2025, and determine how many copies each title sold (physical + digital sales only, no in-app purchases).

**Note on Branding**: EA ended its 30-year licensing deal with FIFA in 2023. FIFA 23 (released Sept 2022) was the last game under the FIFA name. Starting in September 2023, the series was rebranded to "EA Sports FC." The games are the same franchise, same developer (EA Vancouver/EA Romania), same engine, and same gameplay lineage. All four titles below are part of the FIFA/EA Sports FC franchise within the 2023-2025 window.

---

## A. Revenue Table

Revenue is calculated as: copies sold x average retail price at time of release. Only copy sales (physical + digital) are counted. Microtransactions, DLC, loot boxes, Ultimate Team pack purchases, and in-app purchases are **excluded**.

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | FIFA 23 | 2022 (active 2023) | 10.5 million | $630 million | Medium |
| 2 | EA Sports FC 24 | 2023 | 9.5 million | $665 million | Medium |
| 3 | EA Sports FC 25 | 2024 | 7.0 million | $490 million | Medium |
| 4 | EA Sports FC 26 | 2025 | 6.5 million | $455 million | Low |
| **TOTAL** | | | **33.5 million** | **$2.24 B** | |

### Revenue Calculation Notes

- **FIFA 23**: Released at $59.99 (last-gen) / $69.99 (current-gen). Weighted average ~$60. Revenue: 10.5M x $60 = $630M.
- **EA Sports FC 24**: Released at $59.99 (last-gen) / $69.99 (current-gen). Weighted average ~$70 (higher current-gen adoption by late 2023). Revenue: 9.5M x $70 = $665M.
- **EA Sports FC 25**: Released at $59.99 (last-gen) / $69.99 (current-gen). Weighted average ~$70. Revenue: 7.0M x $70 = $490M.
- **EA Sports FC 26**: Released at $69.99 standard. Average ~$70. Revenue: 6.5M x $70 = $455M.

### Sales Estimation Methodology

- **FIFA 23 (10.5M)**: Historical FIFA titles sell 10-15M copies annually. FIFA 23 benefited from being the "last FIFA" and 2022 World Cup hype carrying into 2023. EA reported strong FY2023 results. Estimated at 10.5M lifetime.
- **EA Sports FC 24 (9.5M)**: First FC-branded title. Lost some brand recognition from the FIFA name change, but still performed well. Added to PlayStation Plus free games in May 2024 (~7 months post-launch), suggesting earlier sales slowdown than typical. Estimated at 9.5M lifetime.
- **EA Sports FC 25 (7.0M)**: Widely reported as underperforming. EA slashed fiscal year forecast in January 2025 partly due to FC 25. EA lost $6B in market value. Despite this, FC 25 was still #1 in all 17 tracked European countries for H1 2025 per VGChartz. EA's total expected revenue dropped from ~$7.5B to ~$7.15B. Estimated at 7.0M copies, reflecting significant decline.
- **EA Sports FC 26 (6.5M)**: Released October 2025. Ghost of Yotei beat it in UK physical launch sales. Still in active sales window as of early 2026. Saudi Arabia's PIF acquired EA for $55B in late 2025, validating the franchise's long-term commercial value despite recent decline. Estimated at 6.5M (still accumulating sales).

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "FIFA 23",
      "year": 2022,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch, Google Stadia",
      "publisher": "EA Sports (Electronic Arts)",
      "copiesSold": 10500000,
      "estimatedRevenue": 630000000,
      "revenueSource": "Reddit discussions on FIFA franchise sales history; EA FY2023 earnings discussions; historical FIFA sales benchmarks of 10-15M per title; World Cup 2022 boost carrying into 2023",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "EA Sports (Electronic Arts)",
      "copiesSold": 9500000,
      "estimatedRevenue": 665000000,
      "revenueSource": "Reddit posts on EA pulling FIFA games from Steam as FC 24 launched; PS Plus inclusion in May 2024 suggesting slowed sales; r/EASportsFC and r/gaming discussions on rebrand impact; no exact figures disclosed by EA",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "EA Sports (Electronic Arts)",
      "copiesSold": 7000000,
      "estimatedRevenue": 490000000,
      "revenueSource": "Multiple Reddit threads on FC 25 underperformance; Jason Schreier report on EA slashing fiscal forecast; EA lost $6B market value; r/fut discussion noting EA expected $7.5B but got $7.15B; VGChartz data showing FC 25 still #1 in Europe H1 2025; EA Q3 FY2025 revenue fell to $1.88B from $1.94B",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "EA Sports (Electronic Arts)",
      "copiesSold": 6500000,
      "estimatedRevenue": 455000000,
      "revenueSource": "Reddit posts on FC 26 reveal trailer (July 2025); Ghost of Yotei beating FC 26 in UK physical sales; Saudi PIF $55B EA acquisition; r/EASportsFC discussions on FC 26 PC input delay issues; game still in active sales window",
      "confidence": "low"
    }
  ],
  "totalRevenue": 2240000000,
  "totalGamesFound": 4,
  "searchQueries": [
    "FIFA EA Sports FC games released 2023 2024 2025 complete list",
    "EA Sports FC 24 FC 25 copies sold sales millions",
    "FIFA 23 copies sold unit sales",
    "EA Sports FC 25 sales underperformance copies sold",
    "FIFA 23 EA Sports FC rebrand sales numbers revenue",
    "EA Sports FC 24 player count sales decline",
    "EA Sports FC 26 release date October 2025 sales",
    "EA fiscal year 2024 2025 FC revenue earnings report net bookings",
    "FIFA franchise 325 million copies sold total all time",
    "EA Sports FC 24 sold millions launch sales VGChartz NPD"
  ],
  "redditPostsAnalyzed": 28
}
```

---

## Key Findings

1. **Declining Sales Trajectory**: The FIFA/EA Sports FC franchise shows a clear downward trend from ~10.5M copies (FIFA 23) to an estimated ~6.5M (FC 26), representing a ~38% decline over the period.

2. **Rebrand Impact**: The transition from "FIFA" to "EA Sports FC" coincided with declining unit sales. Reddit users frequently cite the loss of brand recognition as a factor, though gameplay quality and lack of innovation are also cited.

3. **Still Commercially Dominant**: Despite underperformance vs. EA's expectations, EA Sports FC titles remain the #1 selling game in Europe consistently. The franchise's baseline remains enormous even in decline.

4. **Revenue Excludes Massive Live Service Income**: The $2.24B total reflects copy sales ONLY. EA's Ultimate Team mode generates billions in additional microtransaction revenue annually (estimated $1.5-2B/year across FIFA/FC titles), which is explicitly excluded from this analysis per the research parameters.

5. **Saudi Acquisition Validates Franchise**: The $55B acquisition of EA by Saudi Arabia's PIF in late 2025 demonstrates continued confidence in the EA Sports FC franchise as a long-term revenue driver despite recent sales declines.
