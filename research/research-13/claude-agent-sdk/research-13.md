# Research Report: FIFA / EA Sports FC Games (2023–2025)
## Iteration 13 | Claude Agent SDK

---

## Executive Summary

This report covers all FIFA-franchise games released between 2023 and 2025. Following EA's split with FIFA (the governing body), the franchise was rebranded from "FIFA" to **EA Sports FC** starting September 2023. Three titles were released in the research window:

1. **EA Sports FC 24** (September 29, 2023)
2. **EA Sports FC 25** (September 27, 2024)
3. **EA Sports FC 26** (September 26, 2025)

**Critical Data Limitation:** EA does not publicly disclose unit sales (copies sold) for the FC/FIFA franchise. They report "players" (which includes EA Play trial users) and "net bookings" (which combines copy sales + microtransactions). No Reddit post contained a definitive "X million copies sold" figure for any FC title. All copy-sale estimates below are **inferred** from: EA earnings data, third-party tracking (Circana/NPD, GSD, Alinea Analytics), player-count announcements, historical franchise performance, and comparative market data discussed across **22 Reddit posts** analyzed.

---

## A. Revenue Table (Copy Sales Only — Physical + Digital)

> **Note:** Revenue = estimated unit sales × average retail price at launch. **Excludes** all microtransactions, Ultimate Team (FUT) spending, DLC, loot boxes, and in-app purchases.

| # | Title | Year | Copies Sold (Est.) | Revenue (USD, Est.) | Confidence |
|---|-------|------|--------------------|---------------------|------------|
| 1 | EA Sports FC 24 | 2023 | ~20,000,000 | ~$1.40B | Medium-Low |
| 2 | EA Sports FC 25 | 2024 | ~26,000,000 | ~$1.82B | Low |
| 3 | EA Sports FC 26 | 2025 | ~6,000,000 | ~$390M | Very Low |
| **TOTAL** | | | **~52,000,000** | **~$3.61B** | **Low** |

### Estimation Methodology

**EA Sports FC 24 (~20M copies, Medium-Low confidence):**
- EA reported **14.5 million players in the first month** (r/gamernews post 17mq3a1, citing pcgamesinsider.biz). "Players" includes EA Play trial users — not all purchasers.
- EA confirmed 6.8M Ultimate Edition copies sold during early access and 11.3M players first week (from EA earnings calls referenced in Reddit discussions).
- FC 24 reportedly sold ~5% fewer copies than FIFA 23 in the initial period, but FIFA franchise historically sells 20–25M copies lifetime per title.
- Reddit consensus: FC 24 was commercially successful; the rebrand from FIFA was smooth; EA saved ~$150M/year on licensing (r/gamernews comment by u/Gaudious).
- **Revenue calculation:** 20M × $69.99 MSRP = ~$1.40B (theoretical max at launch price).

**EA Sports FC 25 (~26M copies, Low confidence):**
- **Broke US launch revenue record** for soccer games per Circana (r/gamernews post 1gb1zth, Oct 2024). Note: includes $99.99 Ultimate Edition revenue.
- Third-party analytics firm Alinea Analytics estimated FC 25 exceeded **19.2M units sold on PlayStation alone** by June 2025 (referenced in web sources via Reddit discussions). PlayStation represents ~70-75% of FIFA/FC console+PC sales, extrapolating to ~26M total.
- FC 25 then **significantly underperformed** EA's internal expectations — EA slashed its fiscal year forecast and lost $6B in market cap (r/Games post 1i8x6am, r/pcgaming post 1i7m0ck, Jan 2025).
- Despite this, FC 25 was still **#1 best-selling game in Europe H1 2025** across all 17 tracked countries.
- FC 25 received the **worst user ratings in franchise history** on Metacritic, Google, and Steam (r/EASportsFC post 1n7ixhg).
- The "underperformance" was primarily in **net bookings** (copy sales + microtransactions), not purely unit sales. Reddit comment by u/BurzyGuerrero: "People aren't buyin the cards as much anymore."
- **Revenue calculation:** 26M × $69.99 MSRP = ~$1.82B (theoretical max at launch price).

**EA Sports FC 26 (~6M copies, Very Low confidence):**
- Released September 2025, within research window but very limited data.
- European launch sales **beaten by Battlefield 6**, which also beat COD: Black Ops 6 (r/gaming post 1o9atzm, GSD data — purely premium/paid sales).
- UK physical sales in week 2 **beaten by Ghost of Yotei** (r/PS5 post 1nyu1z1, Christopher Dring / GamesIndustry.biz).
- **50% discounted within 3 months** of release (Black Friday 2025).
- Twitch viewership dropped significantly vs. FC 25 and FC 24.
- Estimate reflects ~75% decline from FC 25 launch trajectory based on comparative European launch data, though lifetime sales could be higher.
- **Revenue calculation:** 6M × $64.99 (blended avg, accounting for rapid discounting) = ~$390M.

### Revenue Caveats

- **MSRP of $69.99** (PS5/Xbox Series X/PC Standard Edition) significantly overstates average selling price. FC 25 was available for $13.99 by June 2025; FC 26 was 50% off within 3 months.
- Last-gen versions (PS4/Xbox One) launched at $59.99; Switch version of FC 24 at $39.99.
- Regional pricing, bundles, and EA Play access further reduce effective average selling price.
- Actual copy revenue is likely **40-60% of the theoretical max** shown above.

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS5, PS4, Xbox Series X|S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 20000000,
      "estimatedRevenue": 1399800000,
      "revenueSource": "Reddit: 14.5M players in first month (r/gamernews post 17mq3a1 → pcgamesinsider.biz); EA confirmed 6.8M early access sales, 11.3M first-week players; ~5% below FIFA 23 initial period; historical franchise norm 20-25M/year lifetime",
      "confidence": "medium-low"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X|S, Xbox One, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 26000000,
      "estimatedRevenue": 1819740000,
      "revenueSource": "Reddit: Broke US launch revenue record (r/gamernews post 1gb1zth → Circana); EA slashed forecast, lost $6B market cap (r/Games post 1i8x6am, r/pcgaming post 1i7m0ck); #1 in Europe H1 2025; worst user ratings ever (r/EASportsFC post 1n7ixhg); Alinea Analytics est. 19.2M+ PS copies by Jun 2025",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X|S, PC",
      "publisher": "Electronic Arts",
      "copiesSold": 6000000,
      "estimatedRevenue": 390000000,
      "revenueSource": "Reddit: European launch sales beaten by BF6 (r/gaming post 1o9atzm → GSD data); UK physical sales beaten by Ghost of Yotei in week 2 (r/PS5 post 1nyu1z1); 50% off within 3 months; significant franchise decline trend; NOTE: game still in early lifecycle, limited data",
      "confidence": "very-low"
    }
  ],
  "totalRevenue": 3609540000,
  "totalGamesFound": 3,
  "searchQueries": [
    "EA Sports FC 24 sales copies sold",
    "EA Sports FC 25 sales copies sold",
    "FIFA 2023 2024 2025 sales numbers",
    "EA Sports FC copies sold millions",
    "EA FC 24 FC 25 sales figures",
    "FIFA sales decline EA Sports FC",
    "EA Sports FC 24 11.3 million copies first week",
    "EA FC revenue earnings report fiscal year 2024 2025",
    "EA FC 25 underperformance player count decline",
    "EA Sports FC 24 best selling football game ever",
    "'EA Sports FC' 'million copies' OR 'million units' sold",
    "EA FC 24 biggest fastest selling football game rebrand FIFA",
    "EA FC 25 revenue record soccer launch Circana September October",
    "EA Sports FC sales data unit copies VGChartz Circana",
    "EA Sports FC 24 14.5 million players record",
    "EA FC net bookings 5.4 billion live services Ultimate Team revenue",
    "EA FC 24 200 million accounts players total lifetime",
    "FIFA total franchise sales 325 million copies lifetime"
  ],
  "redditPostsAnalyzed": 22
}
```

---

## C. Key Findings & Context

### Franchise Trend: Clear Decline (2023→2025)

| Year | Title | Trajectory |
|------|-------|-----------|
| 2023 | FC 24 | ✅ Successful launch, smooth rebrand, 14.5M players in month 1 |
| 2024 | FC 25 | ⚠️ Record US launch revenue → severe underperformance; worst user ratings ever; EA slashed forecast |
| 2025 | FC 26 | ❌ Outsold at EU launch by BF6; beaten by Ghost of Yotei in UK; 50% off within 3 months |

### Copy Sales vs. Total Franchise Revenue

Reddit data reveals that copy sales represent a **minority** of the franchise's total revenue:

| Revenue Stream | Annual Amount | % of EA Total |
|---------------|--------------|---------------|
| EA FY2024 Total Revenue | ~$7.4B | 100% |
| Live Services (incl. FUT) | ~$5.4B | ~73% |
| FUT Alone (estimated) | ~$3.2–3.8B | ~43–51% |
| FC Mobile | >$1.0B | ~14% |
| Copy Sales (this report) | ~$0.5–0.7B/title | ~7–9% per title |

*Sources: r/EASportsFC post 1i8gjoo (EA Earnings Report and Player Engagement); r/EASportsFC post 1isw8ea (EA Business Model / Trends); r/EASportsFC post 1olq87u (references ~$2B EA Sports segment revenue)*

### EA Acquisition (2025)

EA was acquired for **$55 billion** by PIF (Saudi Arabia's Public Investment Fund), Silver Lake, and Affinity Partners in June 2025 (r/EASportsFC post 1ntgp6o). The FC/FIFA franchise — particularly its FUT microtransaction engine — was a major component of that valuation.

---

## D. Data Quality & Confidence Assessment

| Factor | Assessment |
|--------|-----------|
| Official unit sales disclosure | **None** — EA does not disclose unit sales for FC/FIFA |
| Reddit data quality | **Medium** — 22 posts analyzed reflect industry reporting but no primary unit sales data |
| Third-party analytics | **Medium-Low** — Alinea Analytics provides PS estimates; VGChartz undercounts digital |
| Earnings call data | **Medium** — Revenue figures available but include microtransactions |
| Price assumptions | **Low accuracy** — $69.99 MSRP significantly overstates average selling price |
| FC 24 estimate | **Medium-Low** — Multiple corroborating data points (14.5M players, 6.8M early access, historical norms) |
| FC 25 estimate | **Low** — Relies heavily on single third-party PS estimate extrapolated to all platforms |
| FC 26 estimate | **Very Low** — Game in early lifecycle; only comparative launch data available |

### Known Biases & Limitations

1. **EA's "players" metric inflates perceived engagement** — includes EA Play trial users who didn't purchase
2. **VGChartz significantly undercounts digital sales** — FIFA 23 tracked at 10.3M likely represents mostly physical in an 80-90% digital market
3. **Alinea Analytics is modeled estimation** — the 19.2M PS figure for FC 25 is not from EA's books
4. **Revenue at MSRP is theoretical maximum** — actual copy revenue is substantially lower (rapid discounting, regional pricing, platform variations)
5. **Reddit discussions skew English-speaking** — FC/FIFA sells disproportionately in non-English European and Latin American markets underrepresented on Reddit
6. **FC 26 data is preliminary** — game was only ~5 months old at time of research

---

## E. Reddit Posts Analyzed (22 total)

| # | Post Title | Subreddit | Score | Post ID | Relevance |
|---|-----------|-----------|-------|---------|-----------|
| 1 | 14.5m people played EA Sports FC its first month | r/gamernews | 118 | 17mq3a1 | HIGH |
| 2 | EA Sports FC 25 launch breaks revenue record for soccer games | r/gamernews | 0 | 1gb1zth | HIGH |
| 3 | EA lost $6 billion in market value, following FC 25 & Dragon Age | r/Games | 1,951 | 1i8x6am | HIGH |
| 4 | Jason Schreier: EA is slashing its forecast... FC 25 | r/pcgaming | 1,004 | 1i7m0ck | HIGH |
| 5 | EA Earnings Report and Player Engagement | r/EASportsFC | 127 | 1i8gjoo | HIGH |
| 6 | EA Business Model / Trends | r/EASportsFC | 54 | 1isw8ea | HIGH |
| 7 | 150ms input delay measured on FC26 Online (references ~$2B revenue) | r/EASportsFC | 1,062 | 1olq87u | HIGH |
| 8 | FC 25 Is the Worst User-Rated Game in Franchise History | r/EASportsFC | 625 | 1n7ixhg | MEDIUM |
| 9 | BF6 sold more copies in Europe at launch than COD and FC 26 | r/gaming | 897 | 1o9atzm | MEDIUM |
| 10 | Ghost of Yotei Beats FC 26, Super Mario Galaxy in UK Physical Sales | r/gaming | 1,240 | 1nzc677 | MEDIUM |
| 11 | Ghost of Yotei UK boxed launch beat second week of FC 26 | r/PS5 | 660 | 1nyu1z1 | MEDIUM |
| 12 | Hogwarts Legacy fastest-selling game in Europe (that isn't FIFA) | r/Games | 5,085 | 11ky1mc | MEDIUM |
| 13 | Best selling game of the year in US for past 2 decades (NPD) | r/gaming | 7,853 | 1munnz6 | MEDIUM |
| 14 | Fortnite playtime > CoD + EA Sports FC + GTA 5 + Roblox combined | r/gaming | 4,861 | 197cami | LOW |
| 15 | EA pulls its FIFA games from digital storefronts | r/gaming | 6,159 | 16to3kb | LOW |
| 16 | EA Sports FC 24 Players Say $30 Launch Week Loot Box... | r/Games | 499 | 16y02xe | LOW |
| 17 | EA sports officially sold for $55 billion | r/EASportsFC | 457 | 1ntgp6o | LOW |
| 18 | Balatro dev swings at PEGI... FC 25 microtransactions | r/pcgaming | 24,456 | 1hfjo7a | LOW |
| 19 | FC 25 is probably the least effort EA has ever put in | r/EASportsFC | 514 | 1em3old | LOW |
| 20 | Thank you EA sports and FC 25 for changing my life (satirical) | r/EASportsFC | 1,338 | 1lm4fvs | LOW |
| 21 | EA execs earned $60 million in 2024 despite layoffs | r/Games | 1,534 | 1dhxu1m | LOW |
| 22 | FIFA confirms it will create an EA Sports FC rival | r/Games | 2,844 | umrmmi | LOW |

---

## F. Files

- **Raw Reddit data:** `research/research-13/claude-agent-sdk/reddit-data-13.md`
- **This report:** `research/research-13/claude-agent-sdk/research-13.md`

---

*Report generated: February 20, 2026 | Iteration 13 | Claude Agent SDK*
*Revenue = copies sold × launch MSRP. Excludes all microtransactions, DLC, loot boxes, FUT packs, and in-app purchases.*
