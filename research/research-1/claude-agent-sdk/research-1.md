# Research Report: FIFA / EA Sports FC Games (2023–2025)
## Iteration 1 — Claude Agent SDK

**Date:** 2026-02-19
**Source:** Reddit (35 posts analyzed across r/EASportsFC, r/gaming, r/Games, r/pcgaming, r/truegaming, r/FUTMobile, r/PS5, r/Steam)
**Scope:** All FIFA-branded and EA Sports FC games released 2023–2025, copy sales only (physical + digital). Excludes microtransactions, DLC, loot boxes, and in-app purchases.

---

## Critical Caveat

**EA does not publicly disclose unit sales (copies sold) for individual FIFA / EA Sports FC titles.** This is a well-documented pattern confirmed across 20+ Reddit search queries and 35 analyzed posts:

- EA reports "net bookings," "revenue," and "players" — never unit sales.
- The same pattern was confirmed for Battlefield 2042: "EA HAS REFUSED to give sale numbers" (r/pcgaming, 4,548 upvotes).
- Industry trackers (Circana/NPD, GSD/GfK) publish chart rankings but not absolute unit figures publicly.

All copies-sold and revenue figures below are **estimates** derived from: (1) historical FIFA franchise sales context discussed on Reddit (~10–20M+ copies/year), (2) relative performance comparisons between titles, (3) EA quarterly earnings data, and (4) industry analyst commentary referenced in Reddit threads.

---

## A. Revenue Table

| # | Title | Year | Copies Sold (est.) | Avg. Price (USD) | Revenue (USD, est.) | Confidence |
|---|-------|------|--------------------|-------------------|---------------------|------------|
| 1 | EA Sports FC 24 | 2023 | ~14M | $65 | ~$910M | Low |
| 2 | EA Sports FC 25 | 2024 | ~10M | $60 | ~$600M | Low |
| 3 | EA Sports FC 26 | 2025 | ~8M* | $55 | ~$440M | Low |
| — | EA Sports FC Mobile | 2023–25 | N/A (F2P) | N/A | N/A (MTX only) | — |
| — | EA Sports FC Online | 2023–25 | N/A (F2P) | N/A | N/A (MTX only) | — |
| **TOTAL** | | | **~32M** | | **~$1.95B** | **Low** |

\* FC 26 released September 2025 — only ~5 months of sales as of this report. Lifetime sales will be higher.

### Estimation Methodology

- **FC 24 (~14M):** "Record engagement" at launch per EA. Historically FIFA is the #1 seller in Europe annually ("Hogwarts Legacy is Europe's fastest-selling game *(that isn't FIFA)* for a generation" — r/Games, 5,087 pts). ~14.5M players reported in first week (industry figure referenced in Reddit discussions). Was NOT #1 in the US for 2023 (Hogwarts Legacy was), but only had 3 months of 2023 sales. Added to PS Plus May 2024, indicating premium sales window had concluded. Average price reflects mix of $69.99 current-gen, $59.99 last-gen, and later discounts.

- **FC 25 (~10M):** Confirmed major underperformer. EA Q3 FY25 revenue fell from $1.94B→$1.88B, attributed partly to FC 25. EA lost $6B in market value. Worst user ratings in franchise history (Metacritic, Google, Steam). EA slashed fiscal year forecast. Estimated ~25–30% decline from FC 24 baseline, but franchise inertia keeps it in multi-million range. Average price slightly lower due to weaker demand.

- **FC 26 (~8M to date):** Outsold at European launch by Battlefield 6. Beaten in UK physical sales by Ghost of Yotei ("Beating FIFA on sales in the UK is some feat" — 812 pts). Discounted 50% within 3 months of release. Still a European Black Friday chart-topper despite decline. Only 5 months of data; lifetime sales likely to reach 10M+. Average price reduced to reflect aggressive early discounting.

- **F2P titles excluded:** EA Sports FC Mobile (iOS/Android) and EA Sports FC Online (PC, Asian markets) are free-to-play and revenue is entirely microtransaction-driven. No "copies sold" metric applies. Per the research scope, these are excluded from revenue calculations.

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
      "copiesSold": 14000000,
      "estimatedRevenue": 910000000,
      "revenueSource": "Reddit: No verified unit sales disclosed by EA. Estimate based on historical FIFA franchise sales (~10-20M/year), record launch engagement reported by EA, 14.5M first-week players (industry figure), and consistent #1 European chart position. Added to PS Plus May 2024 indicating premium window concluded. Sources: r/Games (Hogwarts Legacy fastest-selling 'that isn't FIFA'), r/gaming (EA pulls FIFA from Steam, 6160 pts), r/PS5 (PS Plus addition, 1550 pts).",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 10000000,
      "estimatedRevenue": 600000000,
      "revenueSource": "Reddit: No verified unit sales disclosed by EA. Confirmed underperformer: EA Q3 FY25 revenue fell $1.94B→$1.88B (r/Games, 258 pts). EA lost $6B market value (r/Games, 1955 pts). EA slashed fiscal year forecast citing FC 25 (r/pcgaming, 1010 pts). Worst user ratings in franchise history (r/EASportsFC, 628 pts). Estimated ~25-30% decline from FC 24.",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 8000000,
      "estimatedRevenue": 440000000,
      "revenueSource": "Reddit: No verified unit sales disclosed by EA. Only ~5 months of sales data. Outsold at EU launch by Battlefield 6 (r/gaming, 897 pts). Beaten in UK physical sales by Ghost of Yotei (r/gaming, 1241 pts). 50% off within 3 months (r/Games, 222 pts). Still topped European Black Friday charts. Estimate reflects continued franchise decline and heavy early discounting.",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC Mobile",
      "year": 2023,
      "platform": "iOS, Android",
      "publisher": "Electronic Arts",
      "copiesSold": 0,
      "estimatedRevenue": 0,
      "revenueSource": "Free-to-play title. Revenue is entirely microtransaction-driven. Excluded per research scope (copy sales only). Active 2023-2025 per r/FUTMobile (447 pts, 220 pts).",
      "confidence": "high"
    },
    {
      "name": "EA Sports FC Online",
      "year": 2023,
      "platform": "PC (South Korea, China, Asian markets)",
      "publisher": "Electronic Arts",
      "copiesSold": 0,
      "estimatedRevenue": 0,
      "revenueSource": "Free-to-play title. Revenue is microtransaction-driven. Excluded per research scope. Referenced in South Korea loot box legislation discussions (r/EASportsFC, 495 pts).",
      "confidence": "high"
    }
  ],
  "totalRevenue": 1950000000,
  "totalGamesFound": 5,
  "searchQueries": [
    "FIFA EA Sports FC game releases 2023 2024 2025",
    "EA Sports FC 24 FC 25 release complete list",
    "FIFA rebranding EA Sports FC complete list all titles",
    "EA FC 25 EA FC 24 FIFA mobile release",
    "EA Sports FC 24 copies sold sales million units",
    "EA Sports FC 25 sales copies sold underperformance",
    "EA FC 26 sales copies sold units",
    "FIFA EA FC sales numbers VGChartz NPD data",
    "EA Sports FC 24 14.5 million players first week launch record",
    "FIFA franchise total copies sold all time history billion",
    "EA FC 24 14.5 million 11.3 million copies sold players",
    "EA FC 25 sales decline percent fewer copies revenue drop",
    "EA FC 24 best selling game 2023 chart Europe UK",
    "EA Sports FC 25 underperformance revenue decline earnings report",
    "FIFA EA FC mobile game release 2023 2024 2025",
    "EA Sports FC copies sold units sold million sold",
    "FIFA EA FC annual sales data every year how many copies sold each year",
    "EA FC 24 record launch players FIFA rebrand success",
    "EA FC 24 number one best selling game 2023 NPD Circana year end",
    "EA FC 25 Steam players lowest concurrent all time peak"
  ],
  "redditPostsAnalyzed": 35
}
```

---

## Key Reddit Sources

| Source | Subreddit | Score | Key Data Point |
|--------|-----------|-------|----------------|
| EA lost $6B in market value | r/Games | 1,955 | FC 25 underperformance confirmed |
| EA slashing fiscal year forecast | r/pcgaming | 1,010 | FC 25 named as cause |
| EA Q3 FY25 revenue fell to $1.88B | r/Games | 258 | Revenue decline quantified |
| Ghost of Yotei beats FC 26 in UK | r/gaming | 1,241 | FC 26 launch weakness |
| BF6 outsold FC 26 at EU launch | r/gaming | 897 | FC 26 franchise decline |
| Hogwarts Legacy fastest-selling (not FIFA) | r/Games | 5,087 | FIFA historically #1 in Europe |
| EA pulls FIFA games from Steam | r/gaming | 6,160 | FC 24 launch timing confirmed |
| FC 25 worst user-rated in history | r/EASportsFC | 628 | Quality decline documented |
| FC 26 50% off within 3 months | r/Games | 222 | Aggressive discounting |
| EA refused to give BF2042 sales | r/pcgaming | 4,548 | EA non-disclosure pattern |

---

## Confidence Assessment

**Overall Confidence: LOW**

All copy-sales figures are estimates. EA's deliberate non-disclosure of unit sales means no Reddit source (or any public source) contains verified copies-sold data for EA Sports FC 24, FC 25, or FC 26. The estimates above are informed by:

1. Historical franchise performance (~10–20M copies/year for FIFA)
2. Relative performance indicators (chart positions, competitor comparisons)
3. EA quarterly earnings data (revenue trends)
4. Reddit community analysis and industry journalist reporting

The revenue figures should be treated as order-of-magnitude estimates (±30–40%) rather than precise calculations. The total of ~$1.95B represents **copy sales revenue only** and excludes the substantial microtransaction/FUT revenue that typically doubles or triples EA's football game income.
