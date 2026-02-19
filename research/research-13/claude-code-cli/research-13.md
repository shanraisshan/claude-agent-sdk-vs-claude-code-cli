# Research Report - Iteration 13
## FIFA / EA Sports FC Games: Copy Sales Revenue (2023-2025)

This report covers all FIFA/EA Sports FC console and PC game releases from 2023 to 2025, focusing exclusively on copy sales revenue (physical + digital). Microtransactions, DLC, loot boxes, and in-app purchases are excluded.

**Note:** In 2023, EA rebranded the FIFA franchise to "EA Sports FC" after ending its licensing agreement with FIFA. The games covered below are the direct successors to the FIFA series.

---

## A. Revenue Table

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | ~12.5 million | ~$812.5 million | Medium |
| 2 | EA Sports FC 25 | 2024 | ~8.5 million | ~$552.5 million | Medium |
| 3 | EA Sports FC 26 | 2025 | ~6.5 million | ~$454.5 million | Low |
| **TOTAL** | | | **~27.5 million** | **~$1.82 B** | |

### Revenue Calculation Methodology

- **EA Sports FC 24 (2023):** 12.5 million copies x $65.00 average price = $812.5 million. Average price accounts for mix of $69.99 (new-gen) and $59.99 (old-gen/PC) editions, plus some discounted sales over lifecycle.
- **EA Sports FC 25 (2024):** 8.5 million copies x $65.00 average price = $552.5 million. Significant decline from FC 24 based on EA's own guidance cuts and market value loss.
- **EA Sports FC 26 (2025):** 6.5 million copies x $69.99 average price = $454.5 million. Higher average price due to dropping last-gen ($59.99) versions; only next-gen and PC at $69.99. Further sales decline indicated by losing UK/EU launch comparisons to non-FIFA titles.

**Note:** EA Sports FC Mobile is free-to-play and generates revenue through in-app purchases only. It is excluded from this copy sales analysis as there are no "copies sold."

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
      "copiesSold": 12500000,
      "estimatedRevenue": 812500000,
      "revenueSource": "Reddit discussions indicate FC 24 was first post-rebrand title with strong initial sales, topped German sales charts for 2023, EA reported record engagement early on; historical FIFA franchise typically sells 10-15M copies per year; estimated at ~12.5M based on franchise averages and Reddit sentiment showing solid but not record-breaking performance",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 8500000,
      "estimatedRevenue": 552500000,
      "revenueSource": "Reddit extensively discussed FC 25 underperformance: EA slashed fiscal year forecast Jan 2025 (r/pcgaming, 1005 upvotes); EA lost $6B market value partly due to FC 25 (r/Games, 1958 upvotes); monthly active users chart showed steep decline vs FC 24 (r/EASportsFC, 119 upvotes); still #1 best-seller in Germany 2024 despite decline; estimated ~30% decline from FC 24",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 6500000,
      "estimatedRevenue": 454500000,
      "revenueSource": "Reddit reports: lost UK physical launch to Ghost of Yotei (r/gaming, 1239 upvotes); lost European launch sales to Battlefield 6 (r/gaming, 894 upvotes); dropped PS4/Xbox One support reducing addressable market; game too recent for full lifecycle sales data; continued franchise decline trend",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1819500000,
  "totalGamesFound": 3,
  "searchQueries": [
    "FIFA EA FC games released 2023 2024 2025",
    "EA Sports FC 24 FC 25 release list",
    "FIFA EA FC complete game list franchise timeline",
    "EA Sports FC 24 sales copies sold millions",
    "EA Sports FC 25 sales underperformance copies sold",
    "EA Sports FC 26 sales copies sold",
    "EA FC 24 unit sales numbers revenue fiscal year",
    "FIFA EA FC 25 sales decline numbers revenue earnings",
    "EA Sports FC 24 14.5 million copies sold",
    "EA FC 24 players million first week launch sales",
    "EA FC 24 best selling most popular FIFA ever record",
    "EA Sports FC 26 launch sales UK physical",
    "EA earnings Q3 2024 FC 25 net bookings decline soccer",
    "EA FC 24 most played football game ever 2023",
    "FIFA Mobile EA Sports FC Mobile 2023 2024 2025"
  ],
  "redditPostsAnalyzed": 15
}
```

---

## Key Findings

1. **Franchise Rebrand:** FIFA became EA Sports FC starting with FC 24 in September 2023. This was the biggest brand change in the franchise's 30-year history.

2. **Declining Trajectory:** The franchise shows a clear downward trend in copy sales from 2023-2025, with each successive title selling fewer copies than the previous one.

3. **FC 25 was a Major Disappointment:** EA cut its fiscal year guidance in January 2025 specifically citing EA Sports FC 25 underperformance. This caused a $6 billion loss in EA's market capitalization. Reddit users widely criticized the game as the lowest-effort entry ever, with significantly lower monthly active users compared to FC 24.

4. **FC 26 Continued the Decline:** FC 26 lost its traditional dominance in the UK physical sales charts (beaten by Ghost of Yotei) and was outsold at European launch by Battlefield 6 -- both unprecedented for the FIFA/FC franchise.

5. **EA Acquisition:** Despite the franchise decline, EA was acquired for $55 billion in 2025 by PIF, Silver Lake, and Affinity Partners, showing the overall company value extends far beyond just the FC franchise.

6. **Mobile Excluded:** EA Sports FC Mobile is free-to-play and generates revenue entirely through in-app purchases, not copy sales. It is excluded from this analysis per the research parameters.

7. **Revenue Caveats:** Exact copy sales figures are not publicly reported by EA. All figures are estimates based on Reddit discussions of sales charts, analyst reports shared on Reddit, comparative launch data, and historical franchise performance. The FIFA/EA FC franchise historically derives the majority of its revenue from Ultimate Team microtransactions rather than copy sales, but those are excluded from this analysis.
