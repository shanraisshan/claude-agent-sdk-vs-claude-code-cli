# Research Report: FIFA / EA Sports FC Games (2023–2025)
## Iteration 11 — Claude Agent SDK

---

## Overview

This report covers all FIFA / EA Sports FC titles released or actively sold during the 2023–2025 window. In 2023, EA rebranded the franchise from "FIFA" to "EA Sports FC" after ending its licensing agreement with FIFA. Four titles fall within this period:

1. **FIFA 23** — Released September 30, 2022 (the final FIFA-branded game; active through 2023)
2. **EA Sports FC 24** — Released September 29, 2023 (first EA Sports FC-branded title)
3. **EA Sports FC 25** — Released September 27, 2024
4. **EA Sports FC 26** — Released September/October 2025

### Critical Data Caveat

**EA does not publicly disclose per-title unit sales** for the FIFA/EA Sports FC franchise. Instead, EA reports "players" (which includes EA Play trial users, Game Pass subscribers, and other non-purchasers). The only concrete player-count figure found on Reddit was **14.5 million players** for EA Sports FC 24 in its first month. All copy-sold estimates below are inferred from Reddit-sourced context including Steam engagement data, chart performance, EA earnings reports, and community analysis.

---

## A. Revenue Table

Revenue is calculated as: **Copies Sold × Average Retail Price at Release**. Only physical + digital copy sales are counted. **No microtransactions, DLC, loot boxes, or in-app purchases are included.**

| # | Title | Year | Copies Sold (Est.) | Avg. Retail Price | Revenue (USD, Est.) | Confidence |
|---|-------|------|--------------------|-------------------|---------------------|------------|
| 1 | FIFA 23 | 2022 (active 2023) | ~11.0M | $65.00 | ~$715M | Low |
| 2 | EA Sports FC 24 | 2023 | ~12.5M | $65.00 | ~$813M | Low–Medium |
| 3 | EA Sports FC 25 | 2024 | ~9.5M | $65.00 | ~$618M | Low |
| 4 | EA Sports FC 26 | 2025 | ~7.5M | $70.00 | ~$525M | Low |
| **TOTAL** | | **2022–2025** | **~40.5M** | | **~$2.67B** | **Low** |

### Methodology Notes

- **FIFA 23 (~11M):** Peaked at the highest Steam concurrent player count in franchise history (110,757). Boxed UK launch beat FIFA 22. Described as franchise popularity peak. Estimated at midpoint of 10–12M range.
- **EA Sports FC 24 (~12.5M):** 14.5M players in first month (confirmed), adjusted downward ~15% to account for EA Play trial and subscription users. Midpoint of 11–14M range.
- **EA Sports FC 25 (~9.5M):** Confirmed commercial disappointment — EA lost $6B market value, slashed fiscal year forecast, Q3 revenue fell YoY. EA notably never released any player count or milestone. Midpoint of 8–11M range.
- **EA Sports FC 26 (~7.5M):** Steam peak down 12% YoY. Outsold at launch by Ghost of Yotei (UK physical) and Battlefield 6 (Europe). Discounted 50% within 3 months. Still early in lifecycle. Conservative estimate reflecting continued decline.
- **Average retail prices:** FIFA 23 and FC 24/25 had cross-gen pricing ($59.99 last-gen / $69.99 current-gen), averaged to ~$65. FC 26 dropped last-gen support, priced at $69.99.

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
      "copiesSold": 11000000,
      "estimatedRevenue": 715000000,
      "revenueSource": "Reddit: Highest Steam peak in franchise history (110,757 concurrent), UK boxed sales beat FIFA 22, topped UK/EU charts, described as franchise popularity peak. No official unit sales disclosed by EA.",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 12500000,
      "estimatedRevenue": 812500000,
      "revenueSource": "Reddit: 14.5M players in first month (r/gamernews, Nov 2023) — adjusted downward ~15% for EA Play trial/subscription users. Steam peak 107,109. Top console engagement title alongside CoD, GTA, Roblox.",
      "confidence": "low-medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 9500000,
      "estimatedRevenue": 617500000,
      "revenueSource": "Reddit: Confirmed underperformance — EA lost $6B market value, slashed fiscal year forecast (r/Games, r/pcgaming, Jan 2025). EA Q3 FY2025 revenue fell $1.94B→$1.88B. EA never released player count. Worst user-rated game in franchise history. Added to Game Pass 9 months post-launch.",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch 2",
      "publisher": "Electronic Arts",
      "copiesSold": 7500000,
      "estimatedRevenue": 525000000,
      "revenueSource": "Reddit: Steam peak 95,489 (-12% YoY). Outsold by Ghost of Yotei (UK physical) and Battlefield 6 (EU launch). 50% off within 3 months. Community calls it worst in franchise. Released under new PIF/Silver Lake ownership.",
      "confidence": "low"
    }
  ],
  "totalRevenue": 2670000000,
  "totalGamesFound": 4,
  "searchQueries": [
    "FIFA EA Sports FC game releases 2023 2024 2025 list",
    "FIFA 23 copies sold sales numbers millions",
    "EA Sports FC 24 sales copies sold million",
    "EA FC 25 sales figures copies sold",
    "EA FC 25 underperformance sales decline",
    "EA Sports FC 24 million players sold units",
    "FIFA 23 last FIFA game sales record",
    "EA Sports FC 24 14 million players launch first month",
    "FIFA 23 EA FC 24 best selling UK Europe chart 2023 2024",
    "FIFA 23 10 million players best selling",
    "EA FC 25 sales down decline fewer copies sold compared FIFA",
    "EA Sports FC copies sold units sold million sold",
    "EA fiscal year 2024 2025 FC soccer football game bookings net revenue decline",
    "FIFA franchise 325 million copies sold best selling sports",
    "FIFA 23 10.3 million copies sold revenue billion EA earnings",
    "EA Sports FC sales numbers revenue fiscal year earnings"
  ],
  "redditPostsAnalyzed": 27
}
```

---

## C. Key Findings from Reddit Research

### Franchise Trajectory (2023–2025)

1. **FIFA 23 represented the franchise peak.** The last FIFA-branded game achieved the highest Steam concurrent players ever (110,757), beat its predecessor in UK physical sales, and benefited from nostalgia as the "last FIFA."

2. **EA Sports FC 24 held steady.** Despite the rebrand, FC 24 attracted 14.5M players in its first month and maintained strong engagement. EA saved on FIFA licensing fees, potentially improving margins despite a small Steam dip (-3.3%).

3. **EA Sports FC 25 was a commercial disaster.** EA lost $6 billion in market value, slashed its fiscal year forecast, and saw Q3 revenue decline. Critically, EA never released any player count or sales milestone — a first for the franchise, strongly indicating disappointing numbers.

4. **EA Sports FC 26 shows continued decline.** Steam engagement dropped 12%, the title was outsold at launch by multiple competitors (unprecedented for FIFA/FC in Europe), and it was discounted 50% within 3 months.

### Data Limitations

- All copy-sold figures are **estimates** — EA does not disclose per-title unit sales
- "Players" figures include non-purchasers (EA Play trials, Game Pass subscribers)
- Steam data (~10-15% of total player base) may not perfectly represent console trends
- Reddit discussions skew toward engaged/frustrated users, potentially amplifying negative sentiment
- Revenue estimates exclude Ultimate Team microtransactions, which historically generate 2-3x copy sale revenue

---

*Research conducted via Reddit MCP tools. 16 search queries executed across r/EASportsFC, r/Games, r/gaming, r/pcgaming, r/gamernews. 27 Reddit posts analyzed in detail.*
