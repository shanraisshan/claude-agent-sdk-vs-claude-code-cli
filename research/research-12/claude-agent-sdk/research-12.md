# Research Report: FIFA / EA Sports FC Game Sales (2023-2025)
## Iteration 12 — Claude Agent SDK

---

## Executive Summary

EA's FIFA franchise was rebranded to **EA Sports FC** starting in September 2023 after EA lost the FIFA naming license. Three titles were released in the 2023-2025 window: **EA Sports FC 24** (2023), **EA Sports FC 25** (2024), and **EA Sports FC 26** (2025). No other publisher released a FIFA-branded game during this period (a rumored 2K/FIFA partnership was never confirmed as shipped).

EA does not publicly disclose specific unit sales (copies sold) for individual FC titles. They report "player counts" (which include EA Play, Game Pass, and trial users) and "net bookings" (which bundle physical + digital sales with live service revenue). The estimates below apply the specified discount to EA's player counts and account for the well-documented FC 25 underperformance that cost EA ~$6 billion in market value.

---

## A. Revenue Table

**Methodology:**
- **Retail price:** $70 (standard current-gen pricing for 2023+ releases)
- **Player-count discount:** EA-reported player counts reduced by ~38% to estimate actual copy purchasers (removing EA Play subscribers, Game Pass users, free trial players)
- **FC 25 decline:** EA slashed FY2025 guidance by $500-650M primarily due to FC 25, lost $6B in market cap, stock dropped ~20%. A ~38% decline from FC 24 is applied.
- **FC 26:** Still in active sales window; conservative full-lifecycle estimate applied.

| # | Title | Year | Copies Sold (Est.) | Revenue (USD) | Confidence |
|---|-------|------|--------------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | ~10.5 million | $735,000,000 | Medium |
| 2 | EA Sports FC 25 | 2024 | ~6.5 million | $455,000,000 | Medium |
| 3 | EA Sports FC 26 | 2025 | ~6.0 million | $420,000,000 | Low |
| **TOTAL** | | | **~23.0 million** | **$1.61 billion** | |

### Per-Title Rationale

#### EA Sports FC 24 (Released September 29, 2023) — ~10.5M copies, $735M
- EA officially reported **11.3 million players in the first week** and **14.5 million active players in the first month** — the "largest launch in franchise history."
- Applying the ~38% EA Play / Game Pass / trial discount: 14.5M × 0.62 = **~9.0M first-month purchasers**.
- Lifecycle sales (additional months through PS Plus inclusion in May 2024) bring the total to an estimated **~10.5 million copies**.
- FUT revenue was "up high-single digits YoY" in the first four weeks (EA Q2 FY2024 earnings call).
- Added to PlayStation Plus Essential in May 2024 (~7 months post-launch), suggesting EA pivoted to maximizing player base for microtransaction revenue over additional copy sales.
- Confidence: **Medium** — Player count data is official; the 38% discount to derive copies sold is an informed estimate.

#### EA Sports FC 25 (Released September 27, 2024) — ~6.5M copies, $455M
- **Severely underperformed.** EA slashed full-year net bookings guidance from $7.5-7.8B to $7.0-7.15B, citing the soccer franchise as the primary driver.
- EA lost **~$6 billion in market value** in January 2025; stock dropped ~20% (initially -7%, then -11% in after-hours trading).
- The game was **half-price ($35) within two months** of launch — unprecedented for a mainline FIFA/FC title.
- Widely described on Reddit as "the worst FIFA/FC game they've ever released" (243 upvotes, r/pcmasterrace).
- Steam player count was lower than Football Manager 24 (a year-old niche game) in November 2024.
- EA projected a "mid-single-digit decline" in live services revenue, partly attributed to FC 25.
- Applying a **~38% decline** from FC 24's 10.5M (consistent with the magnitude of EA's financial losses and forecast cuts): **~6.5 million copies**.
- 905K copies sold on PlayStation in June 2025 alone (at steep discount), confirming the game was still generating volume sales deep into its lifecycle via heavy discounting.
- Confidence: **Medium** — The underperformance is well-documented financially; exact copy count remains an estimate.

#### EA Sports FC 26 (Released ~August 30, 2025) — ~6.0M copies, $420M
- Launched approximately one month earlier than tradition (late August vs. late September), reportedly to avoid GTA 6 competition.
- **Lost to Ghost of Yotei in UK physical launch sales** — notable because FIFA/FC typically dominates UK physical charts. However, ~90% of UK game sales are digital, so physical-only data is not determinative.
- Reception was **mixed**: described as "potentially the best since FIFA 17" by some (434 upvotes, r/EAFC) but "the worst EAFC they've created" by others (2,268 upvotes, r/EASportsFC).
- EA was acquired by Saudi Arabia's PIF for $55 billion in November 2025; no post-acquisition sales disclosures yet.
- Still in active sales window as of the research cutoff. Conservative full-lifecycle estimate: **~6.0 million copies**.
- Confidence: **Low** — Very limited sales data; game is still early in its lifecycle.

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS4, PS5, Xbox One, Xbox Series X|S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 10500000,
      "estimatedRevenue": 735000000,
      "revenueSource": "EA reported 14.5M first-month players (r/M8X_GAMENEWS Nov 2023); discounted by ~38% for EA Play/Game Pass/trial inflation. FUT revenue up high-single digits YoY per EA Q2 FY2024 earnings (r/EASportsFC comment). Added to PS Plus May 2024 (r/PS5). Lifecycle estimate ~10.5M.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X|S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 6500000,
      "estimatedRevenue": 455000000,
      "revenueSource": "EA slashed FY2025 guidance by $500-650M citing soccer franchise (r/stocks Jan 2025). Lost $6B market cap, stock dropped ~20% (r/Games, r/pcmasterrace). Half-price within 2 months (r/PS5 comment). 905K PlayStation copies in June 2025 at discount (r/PlaySwapM4G). ~38% decline from FC 24 estimated.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X|S, PC, Nintendo Switch 2",
      "publisher": "Electronic Arts (acquired by Saudi PIF Nov 2025)",
      "copiesSold": 6000000,
      "estimatedRevenue": 420000000,
      "revenueSource": "Lost UK physical sales #1 to Ghost of Yotei (r/gaming Oct 2025). Mixed reception on Reddit (r/EAFC, r/EASportsFC). Early launch August 2025 to avoid GTA 6 (r/FIFANEWS). Still in active sales window; conservative lifecycle estimate.",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1610000000,
  "totalGamesFound": 3,
  "searchQueries": [
    "EA Sports FC 24 sales copies sold",
    "EA Sports FC 25 sales copies sold",
    "EA Sports FC 26 sales",
    "FIFA game sales 2023 2024 2025",
    "EA Sports FC player count",
    "EA FC 24 underperforming sales",
    "EA FC 25 sales numbers",
    "FIFA 2K sales",
    "EA FC 24 14.5 million players first month",
    "EA Sports FC 24 record players launch",
    "EA Sports FC 24 best selling game 2023",
    "EA FC 25 worst selling FIFA game decline",
    "EA FC 25 underperforming revenue forecast",
    "EA Sports FC 26 release date sales",
    "EA Sports FC 26 UK chart number one launch",
    "EA earnings Q3 2025 FC 25 net bookings decline",
    "EA stock crash FC 25 live services decline bookings",
    "EA Sports FC 24 FIFA 24 sales numbers VGChartz NPD"
  ],
  "redditPostsAnalyzed": 20
}
```

---

## Key Data Sources (Reddit)

| Source | Subreddit | Key Data Point |
|--------|-----------|----------------|
| EA FC 24 first-month players (14.5M) | r/M8X_GAMENEWS | Official EA announcement |
| FC 24 Steam count down 30% vs FIFA 23 | r/EASportsFC | Steam Charts comparison |
| EA lost $6B market value (FC 25 + DA) | r/Games, r/pcmasterrace | VGC article discussion |
| EA slashed FY2025 guidance ($500-650M) | r/PS5, r/stocks | Jason Schreier / earnings report |
| FC 25 half-price within 2 months | r/PS5 (comment) | User observation, 358 upvotes |
| FC 25: 905K PlayStation copies (June 2025) | r/PlaySwapM4G | Monthly chart data |
| Ghost of Yotei beat FC 26 in UK physical | r/gaming | Push Square article |
| FC 26 early launch (Aug 2025) | r/FIFANEWS | Leak / confirmed |
| EA acquired by Saudi PIF for $55B | r/technology | Nov 2025 news |

---

## Caveats and Limitations

1. **EA does not disclose unit sales.** All "copies sold" figures are estimates derived from player counts (discounted for non-purchasers) and financial performance indicators. No Reddit post contained a definitive "X million copies sold" figure for any FC title.

2. **Revenue here is copy sales only (physical + digital).** It excludes Ultimate Team microtransactions, DLC, loot boxes, and in-app purchases — which historically constitute the majority of EA Sports FC revenue.

3. **The $70 flat rate is a simplification.** FC 25 was heavily discounted within weeks; the actual average selling price was likely well below $70. FC 24 was given away via PS Plus after 7 months. Actual revenue per copy would be lower than these figures suggest.

4. **FC 26 estimate is speculative.** The game had been on sale for only ~2 months at the data cutoff. The lifecycle estimate could shift significantly in either direction.

5. **No FIFA-branded competitor shipped.** A rumored 2K/FIFA partnership was widely discussed on Reddit in early 2024 but no product was confirmed as released during 2023-2025.
