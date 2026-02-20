# Research Report - Iteration 14
## FIFA / EA Sports FC Games: Copy Sales Revenue (2023-2025)

This report covers all FIFA/EA Sports FC console and PC game releases from 2023 to 2025, focusing exclusively on copy sales revenue (physical + digital). Microtransactions, DLC, loot boxes, and in-app purchases are excluded.

**Note:** In 2023, EA rebranded the FIFA franchise to "EA Sports FC" after ending its licensing agreement with FIFA. The games covered below are the direct successors to the FIFA series.

---

## A. Revenue Table

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | ~13 million | ~$845.0 million | Medium |
| 2 | EA Sports FC 25 | 2024 | ~8 million | ~$520.0 million | Medium |
| 3 | EA Sports FC 26 | 2025 | ~6.5 million | ~$454.9 million | Low |
| **TOTAL** | | | **~27.5 million** | **~$1.82 B** | |

### Revenue Calculation Methodology

- **EA Sports FC 24 (2023):** 13 million copies x $65.00 average price = $845.0 million. Average price accounts for mix of $69.99 (new-gen) and $59.99 (old-gen/PC) editions, plus discounted sales over lifecycle. FC 24 attracted 11.3 million players in its first week (vs FIFA 23's 10.3 million), and historical FIFA franchise sales of 10-15 million per title support the 13 million estimate.
- **EA Sports FC 25 (2024):** 8 million copies x $65.00 average price = $520.0 million. Significant decline from FC 24 based on EA slashing fiscal year guidance in January 2025, $6 billion market cap loss, and Q3 revenue falling from $1.94B to $1.88B year-over-year. Added to Game Pass by June 2025 indicating abandoned premium sales.
- **EA Sports FC 26 (2025):** 6.5 million copies x $69.99 average price = $454.9 million. Higher average price due to dropping last-gen ($59.99) versions; only next-gen and PC at $69.99. Lost UK physical launch to Ghost of Yotei and European launch sales to Battlefield 6. Game still recent, full lifecycle data unavailable.

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
      "copiesSold": 13000000,
      "estimatedRevenue": 845000000,
      "revenueSource": "Reddit discussions: FC 24 attracted 11.3M players in first week including EA Play (r/pcgaming, VGC article), beating FIFA 23's 10.3M first-week players; was among most-played console games in late 2023-early 2024 (r/gaming, 4870 upvotes); added to PS Plus May 2024 indicating strong early sales captured; historical FIFA franchise sells 10-15M copies per year",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS4, PS5, Xbox One, Xbox Series X/S, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 8000000,
      "estimatedRevenue": 520000000,
      "revenueSource": "Reddit extensively discussed FC 25 underperformance: EA slashed fiscal year forecast Jan 2025 citing FC 25 (r/pcgaming, 1007 upvotes); EA lost $6B market value (r/Games, 1952 upvotes); Q3 revenue fell $1.94B to $1.88B citing FC weakness (r/Games, 256 upvotes); widely criticized as lowest-effort entry (r/EASportsFC, 512 upvotes); satirical quit post got 1331 upvotes; added to Game Pass June 2025; estimated ~35-40% decline from FC 24",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 6500000,
      "estimatedRevenue": 454930000,
      "revenueSource": "Reddit reports: lost UK physical launch to Ghost of Yotei (r/gaming, 1237 upvotes); lost European launch sales to Battlefield 6 (r/gaming, 893 upvotes); dropped PS4/Xbox One reducing addressable market; performed well during Black Friday 2025 in Europe (r/Games, 217 upvotes); game too recent for full lifecycle data; continued franchise decline trend",
      "confidence": "low"
    }
  ],
  "totalRevenue": 1819930000,
  "totalGamesFound": 3,
  "searchQueries": [
    "FIFA EA FC sales copies sold 2023 2024 2025",
    "FIFA 23 EA Sports FC 24 FC 25 sales numbers copies",
    "EA Sports FC 24 25 sales figures revenue million copies",
    "EA FC best selling game copies 2023 2024",
    "FIFA 23 sales copies sold million EA",
    "EA Sports FC 25 underperformance sales decline copies",
    "FIFA 23 10 million 11 million copies sold best selling",
    "EA FC 24 14 million players launch first week",
    "EA Sports FC 25 sales dropped decline revenue underperformed"
  ],
  "redditPostsAnalyzed": 16
}
```

---

## Key Findings

1. **Franchise Rebrand:** FIFA became EA Sports FC starting with FC 24 in September 2023. This was the biggest brand change in the franchise's 30-year history. Despite concerns about brand recognition loss, FC 24's first-week player count (11.3 million) actually exceeded FIFA 23's (10.3 million).

2. **Declining Trajectory:** The franchise shows a clear downward trend in copy sales from 2023-2025, with each successive title selling fewer copies than the previous one. Estimated total copies across all three titles: ~27.5 million.

3. **FC 25 was a Major Disappointment:** EA cut its fiscal year guidance in January 2025 specifically citing EA Sports FC 25 underperformance. This caused a $6 billion loss in EA's market capitalization. EA's Q3 FY2025 revenue fell from $1.94 billion to $1.88 billion year-over-year. Reddit users widely criticized the game as the lowest-effort entry ever, with the community expressing mass dissatisfaction through satirical posts and gameplay complaints.

4. **FC 26 Continued the Decline:** FC 26 lost its traditional dominance in the UK physical sales charts (beaten by Ghost of Yotei) and was outsold at European launch by Battlefield 6 -- both unprecedented for the FIFA/FC franchise. The removal of last-gen console support (PS4/Xbox One) further reduced the addressable market. However, the game still performed well during Black Friday 2025 in Europe.

5. **Mobile Excluded:** EA Sports FC Mobile is free-to-play and generates revenue entirely through in-app purchases, not copy sales. It is excluded from this analysis per the research parameters.

6. **Revenue Caveats:** Exact copy sales figures are not publicly reported by EA. All figures are estimates based on Reddit discussions of sales charts, analyst reports shared on Reddit, comparative launch data, and historical franchise performance. The FIFA/EA FC franchise historically derives the majority of its revenue from Ultimate Team microtransactions rather than copy sales, but those are excluded from this analysis. EA reports "players" rather than "copies sold," which inflates figures by including EA Play and Game Pass subscribers.

7. **Total Estimated Revenue from Copy Sales:** Approximately $1.82 billion across the three console/PC titles released between 2023 and 2025.
