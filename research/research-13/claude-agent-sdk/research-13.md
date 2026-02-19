# Research Report: FIFA / EA Sports FC Games (2023-2025) — Copy Sales & Revenue
## Iteration 13 | Claude Agent SDK

---

## Executive Summary

EA rebranded its iconic FIFA franchise to **EA Sports FC** starting in September 2023. Two mainline titles were released in the 2023-2025 window: **EA Sports FC 24** (Sep 2023) and **EA Sports FC 25** (Sep 2024). EA does not publicly disclose unit sales for the FC/FIFA franchise, preferring "players" and "net bookings" metrics. The estimates below are derived from a combination of Reddit community data, third-party analytics (Alinea Analytics, VGChartz, Circana/NPD), EA earnings calls, and industry reporting.

**Key limitation:** EA deliberately obscures unit sales. All copy-sold figures below are estimates with noted confidence levels. Revenue is calculated as copies sold × MSRP at launch ($69.99 USD for both titles). Actual average selling prices are lower due to discounts and regional pricing, so the revenue figures represent theoretical maximum from copy sales at launch price. Microtransactions, DLC, loot boxes, and in-app purchases (including FIFA Ultimate Team/FUT revenue) are **excluded**.

---

## A. Revenue Table

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | EA Sports FC 24 | 2023 | ~20,000,000 | ~$1.40 B | Medium-Low |
| 2 | EA Sports FC 25 | 2024 | ~26,000,000 | ~$1.82 B | Low |
| **TOTAL** | | | **~46,000,000** | **~$3.22 B** | **Low** |

### Methodology Notes

**Copies Sold Estimates:**

- **EA Sports FC 24 (~20M):** EA reported 6.8 million copies sold during the early access period (Ultimate Edition), 11.3 million players in the first week, and 14.5 million players in the first month. EA stated FC 24 sold ~5% fewer copies than FIFA 23 in the initial period. Historical franchise norms place annual FIFA/FC titles at 20-25 million copies lifetime. The 6.8M early access figure alone (just Ultimate Edition buyers) strongly suggests a total well above 10M. Estimate: ~20 million lifetime across all platforms.

- **EA Sports FC 25 (~26M):** Third-party analytics firm Alinea Analytics estimated FC 25 exceeded 19.2 million units sold on PlayStation alone by June 2025 (9 months post-launch), with 905K copies sold on PS in June 2025 at a $13.99 price point. PlayStation historically represents ~70-75% of FIFA/FC console+PC sales. Extrapolating: ~26-28M total across all platforms. Despite "underperforming" EA's internal expectations (which triggered a $6B market cap loss and slashed fiscal year forecasts), FC 25 was still the #1 best-selling game in Europe for H1 2025 across all 17 tracked countries. The "underperformance" was primarily in net bookings (which includes FUT microtransactions), not purely unit sales.

**Revenue Calculation:**
- Both titles launched at a Standard Edition MSRP of **$69.99 USD** (PS5/Xbox Series X/PC). Ultimate Edition was $99.99.
- Revenue = Copies Sold × $69.99 (launch MSRP)
- **Important caveat:** Actual average revenue per copy is significantly lower than $69.99 due to:
  - Deep discounting (FC 25 was $13.99 by June 2025; FC 24 also saw rapid price drops)
  - Regional pricing differences (lower prices in many markets)
  - Platform-specific pricing (last-gen versions at $59.99)
  - Bundle deals and EA Play subscriptions
- These revenue figures represent **theoretical maximum from copy sales at launch price only**

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
      "revenueSource": "Reddit: r/gamernews reported 14.5M players first month (pcgamesinsider.biz); r/gaming noted EA Play transition; Web: EA confirmed 6.8M early access sales, ~5% below FIFA 23; VGChartz tracked FIFA 23 at 10.3M (physical-heavy); historical franchise norms 20-25M/year",
      "confidence": "medium-low"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X|S, Xbox One, PC, Nintendo Switch",
      "publisher": "Electronic Arts",
      "copiesSold": 26000000,
      "estimatedRevenue": 1819740000,
      "revenueSource": "Reddit: r/Games reported $6B market cap loss from underperformance (VGC); r/gamernews reported US launch revenue record (Circana); r/Games reported #1 in Europe H1 2025 (VGChartz); Web: Alinea Analytics estimated 19.2M+ copies on PlayStation alone by June 2025 (KitGuru/ResetEra)",
      "confidence": "low"
    }
  ],
  "totalRevenue": 3219540000,
  "totalGamesFound": 2,
  "searchQueries": [
    "EA Sports FC 24 sales copies sold",
    "EA Sports FC 25 sales copies sold",
    "FIFA 2023 2024 2025 sales numbers",
    "EA FC sales figures million copies",
    "EA Sports FC commercial success",
    "EA FC 24 FC 25 revenue copies",
    "EA Sports FC 24 FC 25 player count decline underperformance",
    "EA FC 25 revenue record soccer launch Circana NPD",
    "EA FC 24 best selling football game copies units sold",
    "EA earnings Q3 2025 FC 25 net bookings decline",
    "EA FC 25 worst selling FIFA decline sales drop",
    "EA FC 24 record launch biggest football game ever players",
    "EA Sports FC 24 total copies sold all platforms lifetime sales estimate",
    "EA Sports FC 25 copies sold unit sales million 2024 2025",
    "EA Sports FC 24 FC 25 retail price launch standard edition USD"
  ],
  "redditPostsAnalyzed": 17
}
```

---

## C. Per-Game Detail

### 1. EA Sports FC 24 (Released: September 29, 2023)

| Metric | Value | Source |
|--------|-------|--------|
| Early Access Sales | 6.8 million (Ultimate Edition) | EA official announcement |
| First-Week Players | 11.3 million | EA press release |
| First-Month Players | 14.5 million | r/gamernews → pcgamesinsider.biz |
| vs. FIFA 23 | ~5% fewer copies (initial period) | PC Gamer / EA earnings call |
| Estimated Lifetime Copies | ~20 million | Extrapolation from above data |
| Launch MSRP | $69.99 (Standard) / $99.99 (Ultimate) | EA Store |
| Estimated Copy Revenue | ~$1.40 billion (at MSRP) | Calculated |

**Key context from Reddit:**
- First game under EA Sports FC branding after dropping FIFA license (~$150M/year savings)
- Reddit consensus: rebrand was a non-issue for sales; EA made more profit without FIFA license fee
- EA pulled old FIFA games from digital storefronts as FC 24 launched (r/gaming, 6,159 upvotes)
- FC 24 was second-biggest physical launch in UK in 2023, though physical sales down 30% vs FIFA 23

### 2. EA Sports FC 25 (Released: September 27, 2024)

| Metric | Value | Source |
|--------|-------|--------|
| US Launch Revenue | Record for soccer games | r/gamernews → Circana/gamesindustry.biz |
| PlayStation Sales (through Jun 2025) | ~19.2 million units | Alinea Analytics via KitGuru/ResetEra |
| PlayStation Sales (June 2025 alone) | ~905,000 units (at $13.99) | Alinea Analytics |
| Europe H1 2025 Ranking | #1 best-selling game (all 17 countries) | r/Games → VGChartz |
| EA Impact | $6B market cap loss; fiscal year forecast slashed | r/Games → VGC; r/pcgaming → Jason Schreier |
| EA Q3 FY2025 Revenue | $1.88B (down from $1.94B YoY) | r/Games → Hollywood Reporter |
| User Ratings | Worst in franchise history (Metacritic, Google, Steam) | r/EASportsFC |
| Estimated Lifetime Copies | ~26 million (all platforms) | Extrapolation from Alinea PS data |
| Launch MSRP | $69.99 (Standard) / $99.99 (Ultimate) | EA Store / dotesports |
| Estimated Copy Revenue | ~$1.82 billion (at MSRP) | Calculated |

**Key context from Reddit:**
- Broke US launch revenue record but then significantly underperformed EA's internal expectations
- "Underperformance" was primarily in **net bookings** (copy sales + microtransactions combined), not purely unit sales
- Aggressive discounting: price dropped to $13.99 by June 2025, driving high unit volumes at low margins
- Despite poor user reviews and EA's disappointment, still dominated European sales charts
- Reddit community consensus: FC 25 was poorly received but franchise momentum carried it (r/EASportsFC)

### Games NOT Found / Out of Scope

- **No new FIFA-branded games** were released 2023-2025 (last FIFA game was FIFA 23, Sep 2022)
- **EA Sports FC Mobile** operates as a live-service title without discrete copy sales
- **EA Sports FC 26** (Sep 2025) was outside the research window but showed further franchise decline indicators

---

## D. Data Quality & Confidence Assessment

| Factor | Assessment |
|--------|-----------|
| Official unit sales disclosure | **None** — EA does not disclose unit sales for FC/FIFA |
| Reddit data quality | **Medium** — Community discussions reflect industry reporting but no primary unit sales data |
| Third-party analytics | **Medium-Low** — Alinea Analytics provides PS estimates; VGChartz undercounts digital |
| Earnings call data | **Medium** — Revenue figures available but include microtransactions |
| Price assumptions | **Low accuracy** — $69.99 MSRP significantly overstates average selling price |
| FC 24 copy estimate confidence | **Medium-Low** — Multiple corroborating data points but no definitive total |
| FC 25 copy estimate confidence | **Low** — Relies heavily on single third-party PS estimate extrapolated to all platforms |

### Known Biases & Limitations

1. **EA's "players" metric inflates engagement appearance** — includes EA Play trial users who didn't purchase the game
2. **VGChartz significantly undercounts digital sales** — FIFA 23 tracked at 10.3M likely represents mostly physical sales in a market that is ~80-90% digital
3. **Alinea Analytics is third-party estimation** — the 19.2M PS figure for FC 25 is modeled, not from EA's books
4. **Revenue at MSRP is theoretical maximum** — actual copy revenue is substantially lower due to rapid and steep discounting, regional pricing, and platform variations
5. **Reddit discussions heavily skew toward English-speaking markets** — FC/FIFA sells disproportionately in non-English European and Latin American markets that are underrepresented in Reddit data

---

## E. Sources

### Reddit Posts Analyzed (17 total)

| # | Post Title | Subreddit | Score | Relevance |
|---|-----------|-----------|-------|-----------|
| 1 | 14.5m people played EA Sports FC its first month | r/gamernews | 118 | HIGH |
| 2 | EA Sports FC 25 launch breaks revenue record for soccer games | r/gamernews | 0 | HIGH |
| 3 | EA lost $6 billion in market value, following FC 25 & Dragon Age | r/Games | 1,959 | HIGH |
| 4 | Jason Schreier: EA is slashing its forecast... FC 25 | r/pcgaming | 1,004 | HIGH |
| 5 | Electronic Arts saw revenue fall to $1.88 billion in Q3 | r/Games | 258 | HIGH |
| 6 | FC 25 and AC Shadows top best selling games in Europe H1 2025 | r/Games | 187 | HIGH |
| 7 | FC 25 Is the Worst User-Rated Game in Franchise History | r/EASportsFC | 624 | MEDIUM |
| 8 | Battlefield 6 sold more copies than EA Sports FC 26 at launch | r/gaming | 895 | MEDIUM |
| 9 | Ghost of Yotei Beats EA Sports FC 26 in UK Physical Sales | r/gaming | 1,237 | MEDIUM |
| 10 | EAFC 26's release saw a significant drop in Twitch viewers | r/EASportsFC | 238 | MEDIUM |
| 11 | PS5, EA Sports FC 26 and Hogwarts Legacy top Europe's Black Friday | r/Games | 218 | MEDIUM |
| 12 | Fortnite playtime > CoD + EA Sports FC + GTA 5 + Roblox combined | r/gaming | 4,864 | LOW |
| 13 | EA pulls FIFA games from digital storefronts as FC 24 arrives | r/gaming | 6,159 | LOW |
| 14 | EA Sports FC 24 Players Say $30 Launch Week Loot Box... | r/Games | 492 | LOW |
| 15 | EA officially sold for $55 billion | r/EASportsFC | 462 | LOW |
| 16 | Balatro dev swings at PEGI... FC 25 microtransactions | r/pcgaming | 24,456 | LOW |
| 17 | EA had a Record FY Q1 with net booking growing 21% YoY | r/pcgaming | 124 | LOW |

### Web Sources

- [EA Sports FC 24 Ultimate Edition Sold Over 6.8 Million Units — GamingBolt](https://gamingbolt.com/ea-sports-fc-24-ultimate-edition-sold-over-6-8-million-units)
- [EA earnings call: FC was a game of two halves — PC Gamer](https://www.pcgamer.com/ea-earnings-call-show-ea-sports-fc-was-a-game-of-two-halves-as-it-fails-to-out-sell-the-last-fifa-but-still-makes-more-money/)
- [EA Sports FC 25 has sold almost 20 million copies on PlayStation alone — KitGuru](https://www.kitguru.net/tech-news/mustafa-mahmoud/ea-sports-fc-25-has-sold-almost-20-million-copies-on-playstation-alone/)
- [Alinea Analytics: EA FC 25 on PlayStation exceeded 19.2M units — ResetEra](https://www.resetera.com/threads/alinea-analytics-ea-fc-25-on-playstation-has-sold-an-estimated-905k-copies-in-june-alone-game-estimated-to-have-exceeded-19-2m-units-sold-on-ps.1241097/)
- [EA Sports FC 24 — VGChartz](https://www.vgchartz.com/game/234109/ea-sports-fc-24/)
- [EA Sports FC — Video Game Sales Wiki (Fandom)](https://vgsales.fandom.com/wiki/EA_Sports_FC)
- [EA Sports FC 25 Sales Numbers — Accio](https://www.accio.com/business/best-selling-ea-sports-fc-25-sales-numbers)
- [EA Sports FC 25 launch breaks revenue record — gamesindustry.biz](https://www.gamesindustry.biz/ea-sports-fc-25-launch-breaks-revenue-record-for-soccer-games-us-monthly-charts)

---

*Report generated: February 20, 2026 | Iteration 13 | Claude Agent SDK*
*Revenue calculation: Copies sold × $69.99 MSRP (launch retail price). Excludes all microtransactions, DLC, loot boxes, FUT packs, and in-app purchases.*
