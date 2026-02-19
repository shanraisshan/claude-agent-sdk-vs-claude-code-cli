# Research Report: FIFA / EA Sports FC Game Sales (2023-2025)
## Iteration 6 -- Claude Agent SDK

---

## Executive Summary

Three premium FIFA/EA Sports FC titles were actively sold during the 2023-2025 period: **FIFA 23** (released Sept 2022, active through Sept 2023), **EA Sports FC 24** (released Sept 2023, active through Sept 2024), and **EA Sports FC 25** (released Sept 2024, active through 2025). EA does not publicly disclose exact unit sales for individual titles. Estimates below are derived from Reddit-sourced GSD (European retail tracking) relative percentage data, franchise trajectory analysis, and qualitative sales descriptions. The franchise showed a declining sales trajectory: FIFA 23 was a record-breaking high boosted by the 2022 FIFA World Cup, FC 24 declined ~10% at launch, and FC 25 declined a further ~5% while being labeled as "underperforming" by EA.

---

## A. Revenue Table

Revenue = copies sold x average retail price. **Only** physical + digital copy sales. No microtransactions, DLC, loot boxes, Ultimate Team packs, or in-app purchases.

| # | Title | Year | Copies Sold | Avg Price | Revenue (USD) | Confidence |
|---|-------|------|-------------|-----------|---------------|------------|
| 1 | FIFA 23 | 2022 (active 2023) | 11.0M | $60 | $660,000,000 | Medium |
| 2 | EA Sports FC 24 | 2023 | 10.0M | $70 | $700,000,000 | Medium |
| 3 | EA Sports FC 25 | 2024 | 9.5M | $70 | $665,000,000 | Medium |
| **TOTAL** | | | **30.5M** | | **$2.03B** | |

### Estimation Methodology

**FIFA 23 (11.0 million copies)**
- Record-breaking launch; described as "an absolute monster" in Reddit discussions citing European sales data.
- Fastest-selling game in Europe; served as the benchmark that all other games (including Hogwarts Legacy) are measured against.
- Massively boosted by the 2022 FIFA World Cup in Qatar (Nov-Dec 2022), with a free World Cup mode update driving sales and engagement into 2023.
- The FIFA franchise has 325+ million lifetime copies sold over ~30 years (~10.8M average/year), with recent entries trending higher. FIFA 23's World Cup boost places it at the upper end.
- Released before 2023, so priced at $60 (standard last-gen/cross-gen price point per rules).
- **Confidence: Medium** -- No exact figure found on Reddit; estimated from franchise trajectory, qualitative "record-breaking" descriptions, and the fact that FC 24 (10% below) still dominated European charts.

**EA Sports FC 24 (10.0 million copies)**
- European launch sales were approximately **10% below FIFA 23** per GSD (Games Sales Data) tracking cited in r/pcgaming (Post 4, Oct 2023).
- Calculation: 11.0M × 0.90 = 9.9M, rounded to 10.0M.
- Despite the 10% decline, FC 24 was the #1 selling game in Europe in September 2023 (beating Starfield) and the #1 best-selling game in Germany for 2024.
- Reddit commenters noted the 10% decline was "not bad at all given the complete name change" and that FC 24 was "probably doing better than FIFA 22."
- Priced at $70 (2023+ title on current-gen consoles).
- **Confidence: Medium** -- The 10% relative decline from FIFA 23 is sourced from GSD European tracking data cited on Reddit. Global sales may differ from European patterns, but Europe is the franchise's largest market.

**EA Sports FC 25 (9.5 million copies)**
- Sold approximately **5% fewer copies than FC 24** per GSD data cited in r/gaming (Post 7, Jan 2025).
- Calculation: 10.0M × 0.95 = 9.5M.
- Described as "underperforming" by EA, contributing to **$6 billion in market value loss** (Jan 2025) and **slashed fiscal year guidance** (Posts 1, 2, 3).
- EA Q3 FY2025 revenue fell to $1.88B from $1.94B YoY, with FC weakness cited as a primary driver.
- Per rules: titles described as "underperforming" with slashed forecasts and billions in market cap loss should use the **lower end** of estimate ranges. The 9.5M figure already reflects the measured 5% GSD decline; global decline may be steeper given the severity of EA's financial warnings.
- Despite underperformance vs. EA's expectations, FC 25 was still the **#1 best-selling game in Europe for H1 2025**, topping all 17 tracked European countries.
- Community reception was severely negative: "probably the least effort EA has ever put in" (517 upvotes), "deserves to have flopped" (189 upvotes).
- Priced at $70 (2024+ title on current-gen consoles).
- **Confidence: Medium** -- The 5% relative decline is from GSD data cited on Reddit. The "underperformance" label suggests EA's internal targets were much higher, but actual unit sales were only modestly below FC 24.

### Pricing Notes
- **$60** used for FIFA 23 (released Sept 2022, before the 2023+ $70 standard).
- **$70** used for FC 24 and FC 25 (released 2023+; primary sales volume on PS5/Xbox Series X at $70 price point).
- FIFA Mobile / EA Sports FC Mobile are **excluded** as free-to-play titles with no copy sales.
- Nintendo Switch "Legacy Edition" (~$40) represents a small fraction of total sales and is absorbed into the average.

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
      "copiesSold": 11000000,
      "estimatedRevenue": 660000000,
      "revenueSource": "Reddit: Described as record-breaking 'absolute monster' in r/pcgaming; fastest-selling in Europe; FC 24 was 10% below it per GSD data (r/pcgaming Post 4); World Cup boost widely discussed across r/Games, r/gaming, r/EASportsFC",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 10000000,
      "estimatedRevenue": 700000000,
      "revenueSource": "Reddit: ~10% below FIFA 23 launch in Europe per GSD data cited in r/pcgaming (Oct 2023); #1 in Europe Sept 2023 (r/pcgaming Post 4); #1 in Germany 2024 (r/gaming Post 9)",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 9500000,
      "estimatedRevenue": 665000000,
      "revenueSource": "Reddit: ~5% below FC 24 per GSD data cited in r/gaming (Jan 2025, Post 7); 'underperformance' caused $6B market cap loss (r/Games Post 1, 1956 upvotes); EA slashed fiscal year guidance (r/pcgaming Post 2); still #1 in Europe H1 2025 (r/Games Post 8)",
      "confidence": "medium"
    }
  ],
  "totalRevenue": 2025000000,
  "totalGamesFound": 3,
  "searchQueries": [
    "FIFA 23 sales numbers copies sold",
    "EA Sports FC 24 sales copies sold",
    "EA Sports FC 25 sales numbers",
    "FIFA copies sold 2023 2024 2025",
    "EA FC sales disappointing",
    "EA Sports FC player count million",
    "FIFA franchise sales decline rebrand",
    "EA FC 24 how many copies sold million",
    "EA FC 25 sales launch disappointing underperformance",
    "EA Sports FC revenue earnings quarterly billion",
    "FIFA 23 best selling game UK Europe 2022 record",
    "EA FC 24 launch first week sales Europe number one",
    "EA earnings report FC 25 net bookings decline lower guidance",
    "FIFA 23 best selling game 2022 2023 sales record",
    "EA FC 24 11 million players first week rebrand success",
    "FIFA 23 World Cup mode 30 million players record breaking",
    "best selling video game franchise ever FIFA total sales 325 million",
    "EA FC 25 5% less 5% fewer FC 24 GSD sales data",
    "EA quarterly earnings FC soccer football net bookings 2024 2025",
    "FIFA 23 World Cup boost fastest selling biggest launch ever"
  ],
  "redditPostsAnalyzed": 21
}
```

---

## C. Key Data Sources from Reddit

| Post | Subreddit | Score | Key Data Point |
|------|-----------|-------|----------------|
| EA lost $6B in market value (FC 25 underperformance) | r/Games | 1,956 | FC 25 underperformance was "most of" the reason for $6B loss |
| Jason Schreier: EA slashing forecast | r/pcgaming | 1,008 | EA slashed FY guidance due to FC 25 + Dragon Age |
| EA Q3 FY2025 revenue fell to $1.88B | r/Games | 262 | Revenue down YoY, weakness attributed to FC |
| FC 24 topped European sales (Sept 2023) | r/pcgaming | 0 | FC 24 was ~10% below FIFA 23 launch (GSD data) |
| EA pulls FIFA games from storefronts | r/gaming | 6,162 | FIFA 23 delisted when FC 24 launched |
| Hogwarts Legacy fastest-selling non-FIFA game | r/Games | 5,085 | FIFA benchmark dominance in Europe |
| Sports Games (FC 25 underperformance) | r/gaming | 0 | FC 25 sold ~5% less than FC 24 (GSD data) |
| FC 25 + AC Shadows top Europe H1 2025 | r/Games | 191 | FC 25 was #1 in all 17 tracked European countries |
| Best-selling games 2024 Germany | r/gaming | 569 | EA Sports FC was #1 in Germany 2024 |

---

## D. Limitations and Caveats

1. **No exact unit sales disclosed by EA.** All copy-sold figures are estimates derived from relative percentage comparisons (GSD data) and franchise trajectory analysis.
2. **GSD data is European-only.** The 10% and 5% decline figures come from European retail tracking. Global patterns may differ, though Europe is the franchise's dominant market.
3. **"Players" ≠ copies sold.** EA reports "player" counts that include EA Play, Xbox Game Pass, PS Plus trial users. Reddit discussions frequently conflate these numbers.
4. **Franchise baseline uncertainty.** The 11M estimate for FIFA 23 is the anchor for all subsequent calculations. If FIFA 23 actually sold 10M or 13M, all downstream estimates shift proportionally.
5. **Revenue is copy sales only.** The FIFA/EA FC franchise generates substantial additional revenue from Ultimate Team microtransactions, which is explicitly excluded per research scope.
6. **The "underperformance" of FC 25** was relative to EA's internal expectations, not necessarily an absolute decline. EA expected growth; they got a 5% decline. The $6B market cap loss reflects investor disappointment with the trajectory, not catastrophic sales failure.

---

*Research completed on 2026-02-19 | Iteration 6 | Claude Agent SDK*
*Raw data: research/research-6/claude-agent-sdk/reddit-data-6.md*
*Final report: research/research-6/claude-agent-sdk/research-6.md*
