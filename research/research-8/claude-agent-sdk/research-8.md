# Research Report: FIFA / EA Sports FC Copy Sales Revenue (2023-2025)
## Iteration 8 | Agent: Claude Agent SDK (Opus 4.6)
## Date: 2026-02-19

---

## Methodology

Revenue is calculated as **copies sold x average retail price at time of release**. Only physical + digital copy sales are counted. Microtransactions, DLC, loot boxes, Ultimate Team packs, and in-app purchases are **excluded**.

### Key Estimation Rules Applied:
1. **"Players" ≠ copies sold.** EA reports "player" counts that include EA Play, Game Pass, and PS Plus trial users. Actual purchasers are estimated at 75-80% of reported player counts (used 76% midpoint). This conversion already represents full lifecycle sales — no additional lifecycle bump applied.
2. **World Cup boost.** FIFA 23 coincided with the Qatar 2022 World Cup. Sales estimated at 20-25% above the ~10.8M franchise baseline → ~13M copies.
3. **Underperformance rule.** EA Sports FC 25 triggered EA's $500M+ fiscal year forecast slash and $6B market cap loss. Copies estimated at 70-73% of FC 24's ~11M → ~8M copies.
4. **Lifecycle projection.** EA Sports FC 26 (released Sep 2025, ~5 months ago) is projected for full annual lifecycle. No catastrophic financial signals (no forecast slash, no major market cap loss), suggesting slight recovery from FC 25's disaster → ~9M copies projected.
5. **Retail pricing.** $60 blended average for FIFA 23 (released 2022, when $60 was standard). $70 for all FC titles (2023+, current-gen console pricing).
6. **Free-to-play exclusion.** EA Sports FC Mobile is excluded — no copy sales revenue.

---

## A. Revenue Table

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | FIFA 23 | 2022 | 13,000,000 | $780,000,000 | Medium |
| 2 | EA Sports FC 24 | 2023 | 11,000,000 | $770,000,000 | Medium |
| 3 | EA Sports FC 25 | 2024 | 8,000,000 | $560,000,000 | Medium |
| 4 | EA Sports FC 26 | 2025 | 9,000,000 | $630,000,000 | Low |
| **TOTAL** | | | **41,000,000** | **$2.74B** | |

---

## Per-Game Analysis

### 1. FIFA 23 (Released Sep 30, 2022 — Active through Sep 2023)
- **Last FIFA-branded game** before EA/FIFA license split
- **World Cup boost**: Qatar 2022 (Nov-Dec 2022) drove record engagement and sales
- EA described it as their "biggest launch ever" at the time with record player counts
- Franchise baseline ~10.8M; World Cup years historically boost sales 20-25%
- **Estimate: 13M copies** (10.8M × 1.20 ≈ 13M)
- **Revenue: 13M × $60 = $780M** ($60 price point, pre-2023 release)
- Delisted from digital storefronts Sep 2023 when FIFA license expired
- **Confidence: Medium** — World Cup boost pattern is well-established; no exact figure found on Reddit

### 2. EA Sports FC 24 (Released Sep 29, 2023 — Active through Sep 2024)
- **First game under EA Sports FC brand** after FIFA license split
- EA publicly announced 14.5M "player accounts" in first week (referenced in Reddit data)
- Applying 76% purchaser conversion: 14.5M × 0.76 ≈ 11M copies (this IS the lifecycle estimate)
- Commercially successful — EA's biggest revenue driver during this period
- **Estimate: 11M copies**
- **Revenue: 11M × $70 = $770M**
- **Confidence: Medium** — EA's 14.5M player figure is well-documented; conversion ratio is an estimate

### 3. EA Sports FC 25 (Released Sep 27, 2024 — Active through Sep 2025)
- **Confirmed severe underperformer** across multiple Reddit posts:
  - EA slashed fiscal year forecast (Jan 2025) — Bloomberg reported "bookings slid on weakness in soccer"
  - EA lost $6B in market value (Jan 2025)
  - Q3 FY25 revenue fell from $1.94B to $1.88B YoY, partially attributed to FC 25
  - Worst user-rated game in franchise history (Metacritic, Steam, Google)
- Underperformance rule: 70-73% of prior year (FC 24's ~11M)
- **Estimate: 8M copies** (11M × 0.73 ≈ 8M)
- **Revenue: 8M × $70 = $560M**
- **Confidence: Medium** — Underperformance is thoroughly documented; magnitude of decline is estimated

### 4. EA Sports FC 26 (Released Sep 2025 — Currently Active)
- Revealed Jul 16, 2025; beta Jun 2025; launched Sep 2025
- **Launch signals mixed but not catastrophic:**
  - Beaten by Ghost of Yotei in UK physical sales (Oct 2025)
  - Beaten by Battlefield 6 in European launch sales (Oct 2025)
  - Significant gameplay complaints (input delay, quality issues)
  - Called "worst football game of all Fifa series" on r/EASportsFC
- **No EA forecast slash or major market cap event** (unlike FC 25)
- Suggests slight recovery from FC 25's disaster, not further collapse
- Full-lifecycle projection (only ~5 months since launch): ~9M copies
- **Estimate: 9M copies** (~12.5% above FC 25's 8M)
- **Revenue: 9M × $70 = $630M**
- **Confidence: Low** — Early in lifecycle; no financial reporting yet for FC 26 period; launch signals are mixed

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "FIFA 23",
      "year": 2022,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 13000000,
      "estimatedRevenue": 780000000,
      "revenueSource": "World Cup boost estimate (20-25% above 10.8M franchise baseline). EA called it 'biggest launch ever.' No exact Reddit sales figure found. Delisted Sep 2023 when FIFA license expired.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 11000000,
      "estimatedRevenue": 770000000,
      "revenueSource": "EA reported 14.5M player accounts in first week. Applied 76% purchaser conversion (14.5M x 0.76 = 11M). First EA Sports FC branded title. Reddit confirmed commercially successful.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 8000000,
      "estimatedRevenue": 560000000,
      "revenueSource": "Confirmed severe underperformer: EA slashed fiscal year forecast, lost $6B market cap (Jan 2025). Bloomberg reported bookings weakness in soccer. Worst user-rated in franchise history. Estimated at 73% of FC 24 (11M x 0.73 = 8M).",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 9000000,
      "estimatedRevenue": 630000000,
      "revenueSource": "Released Sep 2025, ~5 months old. Beaten by Ghost of Yotei (UK physical) and Battlefield 6 (European launch). Quality complaints but no EA forecast slash. Projected full lifecycle at slight recovery over FC 25 (~12.5% above 8M).",
      "confidence": "low"
    }
  ],
  "totalRevenue": 2740000000,
  "totalGamesFound": 4,
  "searchQueries": [
    "FIFA EA Sports FC games released 2023 2024 2025 complete list",
    "EA Sports FC 24 FC 25 release sales copies sold",
    "FIFA 23 copies sold million sales figures",
    "FIFA rebranding EA Sports FC timeline all games",
    "EA Sports FC 24 sales million copies sold units",
    "EA Sports FC 25 sales decline underperformance copies sold",
    "EA Sports FC 26 sales launch copies sold 2025",
    "FIFA 23 sales record copies sold best selling",
    "EA FC 24 14.5 million biggest launch football game ever",
    "EA Sports FC 25 7 million sold declining franchise football",
    "FIFA 23 10 million players sales record breaking launch",
    "EA FC 24 11 million players launch week first week",
    "EA earnings FIFA franchise 325 million copies total sold all time",
    "FIFA 23 best selling last FIFA game sales figures numbers",
    "EA FC Mobile FIFA Mobile 2023 2024 2025 downloads players",
    "FIFA 23 World Cup best selling ever players active users record",
    "EA fiscal year 2024 2025 FC net bookings decline football game sales numbers",
    "EA acquired PIF 55 billion Saudi Arabia EA Sports",
    "VGChartz FIFA EA FC sales data copies sold chart",
    "EA Sports FC 24 record breaking launch most played football game",
    "EA FC 25 worst sales flopped player count Steam decline numbers",
    "EA FC 26 UK sales chart launch physical digital first week October 2025"
  ],
  "redditPostsAnalyzed": 17
}
```

---

## Key Context from Reddit Research

### EA/FIFA License Split (2023)
- EA and FIFA officially parted ways in Summer 2023 after the FIFA 23 cycle ended
- EA was contractually required to delist all FIFA-branded games from digital storefronts (Sep 2023)
- The franchise continued as "EA Sports FC" starting with FC 24
- FIFA (the organization) licensed its name to 2K Sports for a competing game

### EA Acquisition (2025)
- EA announced acquisition by PIF (Saudi Arabia), Silver Lake, and Affinity Partners for $55 billion (Sep 29, 2025)
- Saudi Arabia would own 93.4% of EA under the buyout plan
- 99% of shareholders approved — deal underscores the enduring value of EA's sports franchises despite declining sales

### Franchise Sales Trajectory
The FIFA/EA Sports FC franchise shows a clear declining trend in copy sales during 2023-2025:
- **FIFA 23 (13M)** → Peak driven by World Cup
- **FC 24 (11M)** → Strong launch but normalized without World Cup
- **FC 25 (8M)** → Severe underperformance (-27% YoY), worst user ratings ever
- **FC 26 (9M est.)** → Slight recovery projected, but quality complaints persist

Total estimated copy sales revenue across the 2023-2025 window: **$2.74 billion**.

---

*Raw Reddit data: see `reddit-data-8.md` in this directory*
*Research conducted via Reddit MCP server across r/EASportsFC, r/gaming, r/Games, r/pcgaming, r/truegaming, r/dragonage*
