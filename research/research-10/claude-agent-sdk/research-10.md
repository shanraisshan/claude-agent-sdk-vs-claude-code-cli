# Research Report: FIFA / EA Sports FC Game Sales (2023–2025)
## Iteration 10 — Claude Agent SDK
## Date: 2026-02-19

---

## A. Revenue Table

Revenue is calculated as **copies sold × average retail price at time of release**. Only physical + digital copy sales are counted. Microtransactions, DLC, Ultimate Team (FUT) purchases, loot boxes, and in-app purchases are **excluded**.

### Important Methodology Notes

EA does not publicly disclose per-title unit sales for the FIFA/FC franchise. EA reports "players" (which includes EA Play trial users, Game Pass subscribers, and PS Plus claimants) rather than copies sold. No official copies-sold figures for any individual title in this period were found on Reddit. All estimates below are derived conservatively from Reddit-sourced data: first-week player counts, UK physical sales trends, chart positions, EA earnings guidance revisions, and community/analyst commentary.

### Key Assumptions
- EA's "players" counts are inflated by EA Play/Game Pass trial users; actual purchasers are estimated at ~65-70% of reported first-week player counts.
- Lifetime sales multiples are conservative (~1.4-1.5× first-week purchasers for modern FIFA/FC, reflecting heavy front-loading).
- For FC 25, a substantial decline (~44%) is applied given EA's forecast slash, $6B market cap loss, half-price within 7 weeks, and worst-ever user ratings.
- For FC 26, a conservative full-lifecycle projection is used given the title is still in its active sales window (~5 months old) but is not charting in the US top 10 for 2025.

| # | Title | Year | Copies Sold | Avg. Price (USD) | Revenue (USD) | Confidence |
|---|-------|------|-------------|------------------|---------------|------------|
| 1 | FIFA 23 | 2022 (active 2023) | 10,000,000 | $60 | $600,000,000 | Medium |
| 2 | EA Sports FC 24 | 2023 | 8,000,000 | $65 | $520,000,000 | Medium |
| 3 | EA Sports FC 25 | 2024 | 4,500,000 | $65 | $292,500,000 | Low |
| 4 | EA Sports FC 26 | 2025 | 4,000,000 | $70 | $280,000,000 | Low |
| **TOTAL** | | | **26,500,000** | | **$1.69 B** | |

---

## Per-Title Rationale

### 1. FIFA 23 — 10M copies, $600M revenue (Medium confidence)
- **10.3 million players in first week** per EA press release (cited r/pcgaming post 173ttp3). This includes EA Play trial users — conservatively ~7M were actual purchasers in week one.
- Boosted by 2022 FIFA World Cup (Qatar) in-game mode, which drove significant Q4 2022 and Q1 2023 engagement.
- Described as Europe's fastest-selling franchise (r/Games post 11ky1mc).
- Delisted from digital storefronts September 2023 (r/gaming post 16to3kb), ending new sales.
- Last FIFA-branded title — brand recognition at peak.
- 10M lifetime estimate reflects strong launch + World Cup tail, conservative given EA Play inflation of "players" count.
- Average retail price: $60 (standard edition at launch, Sept 2022).

### 2. EA Sports FC 24 — 8M copies, $520M revenue (Medium confidence)
- **11.3 million first-week players** including EA Play (r/pcgaming post 173ttp3) — up 10% from FIFA 23.
- However, **UK physical sales down 30%** vs FIFA 23 (r/XboxSeriesX post 16xtqme).
- **Steam concurrent players down ~30%** vs FIFA 23 at comparable lifecycle points (r/EASportsFC post 18toyd1).
- EA is ~80% digital on console (r/XboxSeriesX comment), so physical declines partially offset by digital shift, but Steam data (30% decline) suggests real underlying weakness.
- Higher launch "players" may reflect more EA Play trial access rather than actual purchasers.
- EA's November 2023 earnings call: "double-digit growth in new players, FUT revenue up high-single digits YoY first 4 weeks" (r/EASportsFC comment kffb5bm) — but "new players" likely includes trials.
- #1 best-selling game in Germany for 2024 (r/gaming post 1hwk2zb).
- Added to PlayStation Plus after just 7 months (May 2024, r/PS5 post 1chp0eh), suggesting paid sales lifecycle was considered complete.
- 8M estimate reflects name-change confusion, physical/Steam declines, offset by strong European markets.
- Average retail price: $65 (blended next-gen $70 / last-gen $60).

### 3. EA Sports FC 25 — 4.5M copies, $292.5M revenue (Low confidence)
- **Severely underperforming** per EA itself (January 2025 earnings guidance revision).
- EA slashed full-year net bookings guidance from $7.5–7.8B to $7.0–7.15B — a $350–650M miss primarily attributed to FC 25 (r/stocks post 1i7tlu8).
- **EA lost $6 billion in market value** following the announcement; commenters noted most of the loss was attributed to FC 25, not Dragon Age (r/Games post 1i8x6am).
- **Half-price within 7 weeks of launch** (r/PS5 post 1i7m1am comment) — unprecedented for a FIFA/FC title.
- **Worst user-rated game in franchise history** across Metacritic, Google, and Steam (r/EASportsFC post 1n7ixhg).
- EA Q3 FY25 revenue fell to $1.88B from $1.94B YoY (r/Games post 1ihva33).
- Added to Xbox Game Pass via EA Play just 8.5 months after launch (June 2025, r/Games post 1l3yklu).
- Per research rules: "For titles described as severely underperforming (EA slashing forecasts, losing billions in market value), estimate a substantial decline from prior year." A ~44% decline from FC 24's 8M to 4.5M reflects the severity.
- Average retail price: $65 (blended next-gen/last-gen at launch, before rapid discounting).

### 4. EA Sports FC 26 — 4M copies projected lifecycle, $280M revenue (Low confidence)
- Released September 2025; still in active sales window (~5 months old at research date).
- **Lost UK physical launch sales to Ghost of Yotei** (r/gaming post 1nzc677) — historically unprecedented for FIFA/FC.
- **Not in September 2025 Circana monthly top-seller** (Borderlands 4 was #1, r/Games post 1od7v2m) — historically FIFA frequently topped its launch month.
- **Not in the US top 10 best-selling games of 2025** per Circana full-year data (r/gaming post 1qpfsp3), though only had ~3 months of 2025 sales.
- Ongoing input delay issues reported (r/EASportsFC posts 1npg5mw, 1olq87u).
- Released same week as EA's $55B acquisition announcement (r/gaming post 1ntgb12).
- Per research rules: "For games still in their active sales window, estimate the full lifecycle total but remain conservative." 4M lifecycle projection reflects continued franchise decline and weak chart performance.
- Average retail price: $70 (next-gen standard; PS4/Xbox One editions unclear).

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
      "copiesSold": 10000000,
      "estimatedRevenue": 600000000,
      "revenueSource": "Reddit: 10.3M first-week players per EA press release (r/pcgaming 173ttp3); EU fastest-selling franchise (r/Games 11ky1mc); World Cup 2022 boost; delisted Sept 2023 (r/gaming 16to3kb). No official copies-sold figure disclosed. Conservative estimate based on player-to-purchaser ratio and franchise historical norms.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 8000000,
      "estimatedRevenue": 520000000,
      "revenueSource": "Reddit: 11.3M first-week players incl. EA Play (r/pcgaming 173ttp3); UK physical sales -30% vs FIFA 23 (r/XboxSeriesX 16xtqme); Steam players -30% (r/EASportsFC 18toyd1); #1 Germany 2024 (r/gaming 1hwk2zb); added to PS Plus May 2024 (r/PS5 1chp0eh). No official copies-sold figure disclosed.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 4500000,
      "estimatedRevenue": 292500000,
      "revenueSource": "Reddit: EA slashed FY guidance by $350-650M citing FC 25 underperformance (r/stocks 1i7tlu8); EA lost $6B market value (r/Games 1i8x6am); half-price within 7 weeks (r/PS5 1i7m1am); worst user-rated in franchise history (r/EASportsFC 1n7ixhg); EA Q3 FY25 revenue $1.88B down from $1.94B (r/Games 1ihva33). Substantial decline estimated per severity of underperformance signals.",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, PS4, Xbox One",
      "publisher": "Electronic Arts",
      "copiesSold": 4000000,
      "estimatedRevenue": 280000000,
      "revenueSource": "Reddit: Lost UK physical launch to Ghost of Yotei (r/gaming 1nzc677); not in Sept 2025 Circana top-seller (r/Games 1od7v2m); not in US top 10 for 2025 (r/gaming 1qpfsp3); ongoing input delay issues (r/EASportsFC 1npg5mw, 1olq87u). Still in active sales window — conservative lifecycle projection.",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1692500000,
  "totalGamesFound": 4,
  "searchQueries": [
    "FIFA 23 copies sold sales numbers million",
    "EA Sports FC 24 sales copies sold million",
    "EA Sports FC 25 sales copies sold",
    "EA FC sales million players revenue",
    "FIFA 23 10 million players sold best selling",
    "EA Sports FC 24 11 million players launch",
    "EA earnings report FC 25 underperformance revenue fiscal year",
    "EA Sports FC 26 release date 2025",
    "EA FC 24 FC 25 revenue net bookings billion quarterly",
    "FIFA 23 total lifetime sales 20 million copies",
    "EA Sports FC 26 release September 2025 sales launch week",
    "EA FC 25 worst lowest player count Steam dead game decline",
    "EA Sports FC 24 best selling 2024 top game chart NPD Circana",
    "EA acquired PIF Saudi 55 billion FC franchise future",
    "FIFA video game franchise total sales all time history copies",
    "FIFA 23 World Cup sold copies revenue earnings EA report"
  ],
  "redditPostsAnalyzed": 25
}
```

---

## C. Key Findings & Caveats

### Franchise Trajectory (2023–2025)
The FIFA / EA Sports FC franchise showed a **clear downward trajectory** in copy sales across this period:
- **FIFA 23** benefited from brand recognition + World Cup 2022 → estimated ~10M copies
- **EA Sports FC 24** saw the FIFA-to-FC rebrand cause confusion; physical/PC metrics dropped ~30% → estimated ~8M copies
- **EA Sports FC 25** was a catastrophic underperformer by EA's own admission, triggering a $6B market cap loss → estimated ~4.5M copies (~44% decline)
- **EA Sports FC 26** continued the decline, failing to chart in the US top 10 → estimated ~4M projected lifecycle

### Revenue Excludes Microtransactions
These figures represent **copy sales revenue only** ($1.69B total). The FIFA/FC franchise generates enormous additional revenue from FIFA Ultimate Team (FUT) microtransactions — historically estimated at $1.5–2B+ annually across the franchise. That revenue is explicitly excluded per the research scope.

### Data Quality Limitations
- EA does not disclose per-title unit sales; all estimates are derived from indirect Reddit-sourced data
- "Players" figures from EA include free trial users (EA Play, Game Pass, PS Plus) and significantly overstate actual purchasers
- UK physical sales data is the most granular available but represents a shrinking ~15-20% of total sales
- Steam data represents a small fraction of total players (most play on console or EA App)

---

*Research completed using Reddit data from 25 posts across r/gaming, r/Games, r/EASportsFC, r/PS5, r/XboxSeriesX, r/pcgaming, r/stocks, and r/wallstreetbets. 16 unique search queries were executed.*
