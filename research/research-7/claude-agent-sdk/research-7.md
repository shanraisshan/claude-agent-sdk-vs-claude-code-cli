# Research Report: FIFA / EA Sports FC Games — Copy Sales & Revenue (2023–2025)
## Iteration 7 | Agent: Claude Agent SDK
## Date: 2026-02-19

---

## A. Revenue Table

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | FIFA 23 | 2022 (active into 2023) | 13.5M | $810,000,000 | Medium |
| 2 | EA Sports FC 24 | 2023 | 12.5M | $875,000,000 | Medium |
| 3 | EA Sports FC 25 | 2024 | 9.5M | $665,000,000 | Medium |
| 4 | EA Sports FC 26 | 2025 | 7.0M | $490,000,000 | Low |
| **TOTAL** | | | **42.5M** | **$2.84B** | |

---

## Estimation Methodology & Reasoning

### FIFA 23 — 13.5M copies, $810M revenue
- **World Cup boost**: FIFA 23 coincided with the Qatar 2022 FIFA World Cup (Nov–Dec 2022), a massive sales accelerator. Per estimation rules, World Cup year titles receive a 20–25% boost above the modern franchise average of ~10.8M copies/year. Applying this: 10.8M × 1.25 = 13.5M copies.
- **Supporting evidence**: FIFA 23 was Europe's undisputed #1 game — Hogwarts Legacy was described as "Europe's fastest-selling game (that isn't FIFA) for a generation" (r/Games, score: 5,086). FIFA 23 was among the top sellers on Steam at launch and featured a free World Cup mode update in November 2022 that drove massive engagement and purchases into early 2023.
- **Price**: $60 (released in 2022, when the standard retail price was $60 before the $70 price transition).
- **Revenue**: 13.5M × $60 = $810M.
- **Confidence**: Medium — no official per-title unit sales disclosed by EA, but World Cup performance and European dominance strongly support a figure in the 13–14M range.

### EA Sports FC 24 — 12.5M copies, $875M revenue
- **EA's "players" metric**: EA announced FC 24 attracted 14.5 million players in its first month, calling it "the biggest and fastest growing EA Sports FC game ever." However, EA counts EA Play, Game Pass, and PS Plus trial users as "players." Per estimation rules, actual purchasers are typically 75–80% of reported player counts.
- **Calculation**: 14.5M players × 0.775 (midpoint) = ~11.2M copies in the first month. Annual sports titles typically sell an additional 10–15% beyond their first-month peak, giving a full lifecycle estimate of ~12.5M copies.
- **Supporting evidence**: FC 24 was consistently referenced as the baseline against which FC 25 underperformed, and EA called it a "record." Fortnite playtime reports (Jan 2024) listed EA Sports FC among the top-played console games. The brand transition from FIFA to EA Sports FC did not appear to significantly hurt sales.
- **Price**: $70 (2023+ title, primary sales volume on current-gen consoles at $70).
- **Revenue**: 12.5M × $70 = $875M.
- **Confidence**: Medium — the 14.5M players figure provides a solid anchor after adjusting for non-purchasers.

### EA Sports FC 25 — 9.5M copies, $665M revenue
- **Underperformance rule**: FC 25 was widely described as a significant underperformance. EA slashed its fiscal year forecast by ~$500M+, lost $6B+ in market value (r/Games, score: 1,952), and Q3 FY2025 revenue fell to $1.88B from $1.94B due to FC weakness (r/Games, score: 254). Per estimation rules, when a title triggers forecast slashes of $500M+ and market cap losses of $6B+, copies sold should be estimated at 70–80% of the prior year's title.
- **Calculation**: FC 24 estimated at 12.5M × 0.76 (midpoint of 70–80%) = ~9.5M copies.
- **Supporting evidence**: Despite the underperformance, FC 25 was still #1 in all 17 tracked European countries for H1 2025 (r/Games, score: 190), confirming it still sold millions — just significantly fewer than expected. Community reception was extremely negative: "EA FC 25 is probably the least effort EA has ever put in" (r/EASportsFC, score: 510). A satirical post thanking FC 25 for curing a gaming addiction reached 1,331 upvotes.
- **Price**: $70 (2024+ title).
- **Revenue**: 9.5M × $70 = $665M.
- **Confidence**: Medium — EA's severity of response (forecast slash, market cap loss) clearly indicates a 20–30% drop, and European chart data confirms it was still a top seller despite the decline.

### EA Sports FC 26 — 7.0M copies (to date), $490M revenue
- **Still in active sales window**: FC 26 launched ~September 12, 2025 and is approximately 5 months old as of February 2026. Sales are still accumulating.
- **Launch performance**: FC 26 showed mixed signals — it lost UK physical launch sales to Ghost of Yotei (r/gaming, score: 1,242) and was beaten at European launch by Battlefield 6 (r/gaming, score: 895). However, it was a top seller during Europe's Black Friday 2025 (r/Games, score: 222).
- **Aggressive discounting**: FC 26 was 50% off within 3 months of release, suggesting EA was pushing volume to compensate for soft organic demand.
- **Estimation**: FC 26 appears to represent a slight recovery over the underperforming FC 25 (community reception was more positive: "Everything in this sounds super positive" — r/EASportsFC, score: 162). Per estimation rules, a sequel showing modest improvement over an underperforming predecessor should be estimated slightly above that predecessor but not at or near the franchise peak. At 5 months into its lifecycle (~70–80% of annual sales realized), an estimate of ~7M copies sold to date implies a full-year trajectory of ~9–10M, slightly above FC 25's 9.5M.
- **Price**: $70 (2025 title).
- **Revenue**: 7.0M × $70 = $490M.
- **Confidence**: Low — still in active sales window, and launch was disrupted by competition (BF6, Ghost of Yotei) and aggressive discounting.

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
      "revenueSource": "Reddit: No official per-title figure. Estimated via World Cup boost rule (20-25% above 10.8M franchise avg). Supported by European #1 dominance (r/Games 5086pts), Steam top seller at launch (r/pcgaming 5507pts), and World Cup mode driving Q1 2023 sales.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 12500000,
      "estimatedRevenue": 875000000,
      "revenueSource": "Reddit: EA claimed 14.5M players in first month (biggest/fastest FC ever). Adjusted to 75-80% for actual purchasers (~11.2M first month). Full lifecycle est. ~12.5M. Confirmed as record baseline vs FC 25 underperformance (r/Games 1952pts, r/pcgaming 1008pts).",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 9500000,
      "estimatedRevenue": 665000000,
      "revenueSource": "Reddit: Major underperformance — EA slashed fiscal forecast ~$500M+, lost $6B market cap (r/Games 1952pts). Q3 revenue fell $1.88B from $1.94B (r/Games 254pts). Still #1 in 17/17 European countries H1 2025 (r/Games 190pts). Estimated at 76% of FC 24 per underperformance rule.",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 7000000,
      "estimatedRevenue": 490000000,
      "revenueSource": "Reddit: ~5 months post-launch (Sept 2025). Lost UK physical launch to Ghost of Yotei (r/gaming 1242pts). BF6 beat European launch (r/gaming 895pts). Top seller Black Friday 2025 but 50% off within 3 months (r/Games 222pts). Estimated slight improvement over FC 25 trajectory, still accumulating.",
      "confidence": "low"
    }
  ],
  "totalRevenue": 2840000000,
  "totalGamesFound": 4,
  "searchQueries": [
    "FIFA EA Sports FC games complete list 2023 2024 2025",
    "EA Sports FC 24 25 FIFA 23 complete list games released",
    "FIFA EA Sports FC copies sold sales million units",
    "EA Sports FC rebrand FIFA name change 2023",
    "EA Sports FC 25 sales underperformance copies sold",
    "EA Sports FC 24 sales record launch copies sold",
    "FIFA 23 sales record best selling copies million",
    "EA Sports FC 26 release date launch sales",
    "FIFA 23 best selling game 2022 2023 sales record",
    "EA Sports FC 24 launch biggest fastest growing players",
    "EA quarterly earnings FIFA FC revenue net bookings 2023 2024",
    "EA Sports FC 24 14.5 million players fastest growing",
    "EA Sports FC 25 declined sales drop FIFA franchise struggling",
    "EA Sports FC million copies sold 2023 2024",
    "EA FC 25 sold fewer copies decline percentage compared FC 24",
    "FIFA franchise total sales 325 million copies history",
    "EA Sports FC 26 September 2025 release launch sales first week Europe UK",
    "FIFA Mobile EA Sports FC Mobile 2023 2024 downloads players",
    "EA FC 24 record-breaking fastest launch history FIFA",
    "FIFA 23 EA best selling game ever 10 million first week World Cup",
    "EA Sports FC 26 sales data September October 2025 million sold"
  ],
  "redditPostsAnalyzed": 29
}
```

---

## Notes

1. **EA does not publicly disclose per-title unit sales.** All copy estimates are derived from EA's "players" announcements (adjusted for non-purchasers), franchise historical averages, underperformance severity indicators, and European sales chart data found across Reddit.
2. **Revenue = copy sales only.** No microtransactions, Ultimate Team card packs, DLC, loot boxes, or in-app purchases are included. EA's actual franchise revenue (including Ultimate Team) is substantially higher — likely 2–3x the copy-sale revenue alone.
3. **EA Sports FC Mobile excluded.** It is a free-to-play title with no copy sales. Only premium paid titles are included.
4. **FC 26 estimate is preliminary.** The game is ~5 months old and still in its primary sales window. The 7M figure represents copies sold to date, not final lifetime sales.
5. **All prices reflect primary sales channel pricing.** FIFA 23 at $60 (2022 standard), FC 24/25/26 at $70 (2023+ current-gen standard). Actual blended ASP may be slightly lower due to sales, bundles, and regional pricing, but discounts are offset by Deluxe/Ultimate editions sold at $80–$100.

---

*Raw Reddit data: [reddit-data-7.md](reddit-data-7.md)*
