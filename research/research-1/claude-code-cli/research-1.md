# FIFA Franchise Revenue Research Report — Iteration 1

**Date:** 2026-02-19
**Source:** Reddit MCP (17 search queries, 17 posts analyzed)
**Problem:** Find all FIFA games released from 1990 to 2026 and calculate revenue from copy sales (physical + digital only).

---

## A. Revenue Table

Revenue calculated as: copies sold × average retail price at time of release. Only copy sales (physical + digital). No microtransactions, DLC, loot boxes, or in-app purchases.

**Retail price assumptions based on era:**
- 1993–1995: $50 (16-bit era)
- 1996–2005: $50 (PS1/PS2 era)
- 2006–2012: $60 (HD era)
- 2013–2025: $60–$70 (PS4/PS5 era, $70 from ~2023)

**Note:** Reddit provided specific sales data for only 4 titles (FIFA 12, 13, 18, 19). For all other titles, estimates are based on franchise trajectory, UK market extrapolation (UK ≈ 8–10% of global sales for FIFA), and the commonly cited ~325M total franchise figure. These estimates are marked as "low" confidence.

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | FIFA International Soccer | 1993 | 1,500,000 | $75,000,000 | low |
| 2 | FIFA Soccer 95 | 1994 | 1,000,000 | $50,000,000 | low |
| 3 | FIFA Soccer 96 | 1995 | 2,000,000 | $100,000,000 | low |
| 4 | FIFA 97 | 1996 | 2,500,000 | $125,000,000 | low |
| 5 | FIFA: Road to World Cup 98 | 1997 | 4,000,000 | $200,000,000 | low |
| 6 | FIFA 99 | 1998 | 3,500,000 | $175,000,000 | low |
| 7 | FIFA 2000 | 1999 | 3,500,000 | $175,000,000 | low |
| 8 | FIFA 2001 | 2000 | 4,000,000 | $200,000,000 | low |
| 9 | FIFA Football 2002 | 2001 | 5,000,000 | $250,000,000 | low |
| 10 | FIFA Football 2003 | 2002 | 5,500,000 | $275,000,000 | low |
| 11 | FIFA Football 2004 | 2003 | 6,000,000 | $300,000,000 | low |
| 12 | FIFA Football 2005 | 2004 | 6,500,000 | $325,000,000 | low |
| 13 | FIFA 06 | 2005 | 7,000,000 | $350,000,000 | low |
| 14 | FIFA 07 | 2006 | 8,000,000 | $480,000,000 | low |
| 15 | FIFA 08 | 2007 | 9,000,000 | $540,000,000 | low |
| 16 | FIFA 09 | 2008 | 10,000,000 | $600,000,000 | low |
| 17 | FIFA 10 | 2009 | 10,000,000 | $600,000,000 | low |
| 18 | FIFA 11 | 2010 | 11,000,000 | $660,000,000 | low |
| 19 | FIFA 12 | 2011 | 10,000,000 | $600,000,000 | medium |
| 20 | FIFA 13 | 2012 | 14,500,000 | $870,000,000 | high |
| 21 | FIFA 14 | 2013 | 14,000,000 | $840,000,000 | low |
| 22 | FIFA 15 | 2014 | 15,000,000 | $900,000,000 | low |
| 23 | FIFA 16 | 2015 | 16,000,000 | $960,000,000 | low |
| 24 | FIFA 17 | 2016 | 17,000,000 | $1,020,000,000 | low |
| 25 | FIFA 18 | 2017 | 24,000,000 | $1,440,000,000 | medium |
| 26 | FIFA 19 | 2018 | 22,000,000 | $1,320,000,000 | medium |
| 27 | FIFA 20 | 2019 | 20,000,000 | $1,200,000,000 | low |
| 28 | FIFA 21 | 2020 | 20,000,000 | $1,200,000,000 | low |
| 29 | FIFA 22 | 2021 | 18,000,000 | $1,080,000,000 | low |
| 30 | FIFA 23 | 2022 | 17,000,000 | $1,190,000,000 | low |
| 31 | EA Sports FC 24 | 2023 | 14,000,000 | $980,000,000 | low |
| 32 | EA Sports FC 25 | 2024 | 12,000,000 | $840,000,000 | low |
| 33 | EA Sports FC 26 | 2025 | 10,000,000 | $700,000,000 | low |
| **TOTAL** | | | **325,500,000** | **$20,470,000,000** | |

### Key Data Points from Reddit (high/medium confidence):
- **FIFA 12:** Implied >10M copies (r/Games post 11780i) → estimated 10M
- **FIFA 13:** 14.5M copies per EA Q4 FY13 official results (r/Games post 1dvvz0) → **highest confidence**
- **FIFA 18:** 2.7M in UK alone (r/EASportsFC post ac4ccd) → UK ≈ ~10% of global → ~24M global estimate
- **FIFA 19:** 2.5M in UK alone (r/EASportsFC post ac4ccd) → UK ≈ ~10% of global → ~22M global estimate

---

## B. JSON Data Block

```json
{
  "games": [
    {
      "name": "FIFA International Soccer",
      "year": 1993,
      "platform": "Sega Genesis, SNES, DOS, Game Boy, 3DO, Amiga",
      "publisher": "EA Sports",
      "copiesSold": 1500000,
      "estimatedRevenue": 75000000,
      "revenueSource": "No Reddit data; estimated from early franchise trajectory",
      "confidence": "low"
    },
    {
      "name": "FIFA Soccer 95",
      "year": 1994,
      "platform": "Sega Genesis, SNES, DOS, Game Boy",
      "publisher": "EA Sports",
      "copiesSold": 1000000,
      "estimatedRevenue": 50000000,
      "revenueSource": "No Reddit data; estimated",
      "confidence": "low"
    },
    {
      "name": "FIFA Soccer 96",
      "year": 1995,
      "platform": "PlayStation, Sega Genesis, SNES, DOS, Saturn",
      "publisher": "EA Sports",
      "copiesSold": 2000000,
      "estimatedRevenue": 100000000,
      "revenueSource": "No Reddit data; estimated (first PS1 entry boosted sales)",
      "confidence": "low"
    },
    {
      "name": "FIFA 97",
      "year": 1996,
      "platform": "PlayStation, Saturn, DOS, Windows, SNES, Genesis",
      "publisher": "EA Sports",
      "copiesSold": 2500000,
      "estimatedRevenue": 125000000,
      "revenueSource": "No Reddit data; estimated",
      "confidence": "low"
    },
    {
      "name": "FIFA: Road to World Cup 98",
      "year": 1997,
      "platform": "PlayStation, N64, Windows, Saturn, Game Boy",
      "publisher": "EA Sports",
      "copiesSold": 4000000,
      "estimatedRevenue": 200000000,
      "revenueSource": "No Reddit data; estimated (World Cup year boost)",
      "confidence": "low"
    },
    {
      "name": "FIFA 99",
      "year": 1998,
      "platform": "PlayStation, N64, Windows, Game Boy Color",
      "publisher": "EA Sports",
      "copiesSold": 3500000,
      "estimatedRevenue": 175000000,
      "revenueSource": "No Reddit data; estimated",
      "confidence": "low"
    },
    {
      "name": "FIFA 2000",
      "year": 1999,
      "platform": "PlayStation, Windows, Game Boy Color",
      "publisher": "EA Sports",
      "copiesSold": 3500000,
      "estimatedRevenue": 175000000,
      "revenueSource": "No Reddit data; estimated",
      "confidence": "low"
    },
    {
      "name": "FIFA 2001",
      "year": 2000,
      "platform": "PlayStation, PS2, Windows, GBA",
      "publisher": "EA Sports",
      "copiesSold": 4000000,
      "estimatedRevenue": 200000000,
      "revenueSource": "No Reddit data; estimated (first PS2 entry)",
      "confidence": "low"
    },
    {
      "name": "FIFA Football 2002",
      "year": 2001,
      "platform": "PS2, Xbox, GameCube, PS1, Windows, GBA",
      "publisher": "EA Sports",
      "copiesSold": 5000000,
      "estimatedRevenue": 250000000,
      "revenueSource": "No Reddit data; estimated (World Cup 2002 proximity)",
      "confidence": "low"
    },
    {
      "name": "FIFA Football 2003",
      "year": 2002,
      "platform": "PS2, Xbox, GameCube, PS1, Windows, GBA",
      "publisher": "EA Sports",
      "copiesSold": 5500000,
      "estimatedRevenue": 275000000,
      "revenueSource": "No Reddit data; estimated",
      "confidence": "low"
    },
    {
      "name": "FIFA Football 2004",
      "year": 2003,
      "platform": "PS2, Xbox, GameCube, PS1, Windows, GBA",
      "publisher": "EA Sports",
      "copiesSold": 6000000,
      "estimatedRevenue": 300000000,
      "revenueSource": "No Reddit data; estimated",
      "confidence": "low"
    },
    {
      "name": "FIFA Football 2005",
      "year": 2004,
      "platform": "PS2, Xbox, GameCube, Windows, PSP, DS, GBA",
      "publisher": "EA Sports",
      "copiesSold": 6500000,
      "estimatedRevenue": 325000000,
      "revenueSource": "No Reddit data; estimated",
      "confidence": "low"
    },
    {
      "name": "FIFA 06",
      "year": 2005,
      "platform": "PS2, Xbox 360, Xbox, GameCube, Windows, PSP, DS, GBA",
      "publisher": "EA Sports",
      "copiesSold": 7000000,
      "estimatedRevenue": 350000000,
      "revenueSource": "No Reddit data; estimated (first Xbox 360 entry)",
      "confidence": "low"
    },
    {
      "name": "FIFA 07",
      "year": 2006,
      "platform": "PS2, Xbox 360, Wii, Windows, PSP, DS, GBA",
      "publisher": "EA Sports",
      "copiesSold": 8000000,
      "estimatedRevenue": 480000000,
      "revenueSource": "No Reddit data; estimated (World Cup 2006 year)",
      "confidence": "low"
    },
    {
      "name": "FIFA 08",
      "year": 2007,
      "platform": "PS3, PS2, Xbox 360, Wii, Windows, PSP, DS",
      "publisher": "EA Sports",
      "copiesSold": 9000000,
      "estimatedRevenue": 540000000,
      "revenueSource": "No Reddit data; estimated (first PS3 entry)",
      "confidence": "low"
    },
    {
      "name": "FIFA 09",
      "year": 2008,
      "platform": "PS3, PS2, Xbox 360, Wii, Windows, PSP, DS",
      "publisher": "EA Sports",
      "copiesSold": 10000000,
      "estimatedRevenue": 600000000,
      "revenueSource": "No Reddit data; estimated",
      "confidence": "low"
    },
    {
      "name": "FIFA 10",
      "year": 2009,
      "platform": "PS3, PS2, Xbox 360, Wii, Windows, PSP",
      "publisher": "EA Sports",
      "copiesSold": 10000000,
      "estimatedRevenue": 600000000,
      "revenueSource": "No Reddit data; estimated",
      "confidence": "low"
    },
    {
      "name": "FIFA 11",
      "year": 2010,
      "platform": "PS3, PS2, Xbox 360, Wii, Windows, PSP, 3DS",
      "publisher": "EA Sports",
      "copiesSold": 11000000,
      "estimatedRevenue": 660000000,
      "revenueSource": "No Reddit data; estimated (World Cup 2010 year)",
      "confidence": "low"
    },
    {
      "name": "FIFA 12",
      "year": 2011,
      "platform": "PS3, PS2, Xbox 360, Wii, Windows, PSP, 3DS, Vita",
      "publisher": "EA Sports",
      "copiesSold": 10000000,
      "estimatedRevenue": 600000000,
      "revenueSource": "Reddit r/Games post 11780i: 'Like FIFA 12, its likely to sell more than 10 million copies'",
      "confidence": "medium"
    },
    {
      "name": "FIFA 13",
      "year": 2012,
      "platform": "PS3, PS2, Xbox 360, Wii, Wii U, Windows, PSP, 3DS, Vita",
      "publisher": "EA Sports",
      "copiesSold": 14500000,
      "estimatedRevenue": 870000000,
      "revenueSource": "Reddit r/Games post 1dvvz0: EA Q4 FY13 official results: FIFA 13 - 14.5M copies",
      "confidence": "high"
    },
    {
      "name": "FIFA 14",
      "year": 2013,
      "platform": "PS4, PS3, PS2, Xbox One, Xbox 360, Windows, PSP, 3DS, Vita",
      "publisher": "EA Sports",
      "copiesSold": 14000000,
      "estimatedRevenue": 840000000,
      "revenueSource": "No Reddit data; estimated similar to FIFA 13 (cross-gen launch)",
      "confidence": "low"
    },
    {
      "name": "FIFA 15",
      "year": 2014,
      "platform": "PS4, PS3, Xbox One, Xbox 360, Windows, 3DS, Vita",
      "publisher": "EA Sports",
      "copiesSold": 15000000,
      "estimatedRevenue": 900000000,
      "revenueSource": "No Reddit data; estimated (World Cup 2014 boost, growing PS4/XB1 install base)",
      "confidence": "low"
    },
    {
      "name": "FIFA 16",
      "year": 2015,
      "platform": "PS4, PS3, Xbox One, Xbox 360, Windows",
      "publisher": "EA Sports",
      "copiesSold": 16000000,
      "estimatedRevenue": 960000000,
      "revenueSource": "No Reddit data; estimated (franchise at peak growth period)",
      "confidence": "low"
    },
    {
      "name": "FIFA 17",
      "year": 2016,
      "platform": "PS4, PS3, Xbox One, Xbox 360, Windows",
      "publisher": "EA Sports",
      "copiesSold": 17000000,
      "estimatedRevenue": 1020000000,
      "revenueSource": "No Reddit data; estimated (Frostbite engine debut, The Journey mode)",
      "confidence": "low"
    },
    {
      "name": "FIFA 18",
      "year": 2017,
      "platform": "PS4, PS3, Xbox One, Xbox 360, Windows, Switch",
      "publisher": "EA Sports",
      "copiesSold": 24000000,
      "estimatedRevenue": 1440000000,
      "revenueSource": "Reddit r/EASportsFC post ac4ccd: 2.7M UK copies (phys+digital); UK ~10% of global → ~24M global",
      "confidence": "medium"
    },
    {
      "name": "FIFA 19",
      "year": 2018,
      "platform": "PS4, PS3, Xbox One, Xbox 360, Windows, Switch",
      "publisher": "EA Sports",
      "copiesSold": 22000000,
      "estimatedRevenue": 1320000000,
      "revenueSource": "Reddit r/EASportsFC post ac4ccd: 2.5M UK copies (phys+digital); UK ~10% of global → ~22M global",
      "confidence": "medium"
    },
    {
      "name": "FIFA 20",
      "year": 2019,
      "platform": "PS4, Xbox One, Windows, Switch",
      "publisher": "EA Sports",
      "copiesSold": 20000000,
      "estimatedRevenue": 1200000000,
      "revenueSource": "No Reddit data; estimated (slight decline trend from FIFA 19)",
      "confidence": "low"
    },
    {
      "name": "FIFA 21",
      "year": 2020,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, Windows, Switch",
      "publisher": "EA Sports",
      "copiesSold": 20000000,
      "estimatedRevenue": 1200000000,
      "revenueSource": "No Reddit data; estimated (COVID boost to gaming, cross-gen launch)",
      "confidence": "low"
    },
    {
      "name": "FIFA 22",
      "year": 2021,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, Windows, Switch, Stadia",
      "publisher": "EA Sports",
      "copiesSold": 18000000,
      "estimatedRevenue": 1080000000,
      "revenueSource": "No Reddit data; estimated",
      "confidence": "low"
    },
    {
      "name": "FIFA 23",
      "year": 2022,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, Windows, Switch",
      "publisher": "EA Sports",
      "copiesSold": 17000000,
      "estimatedRevenue": 1190000000,
      "revenueSource": "No Reddit total; UK #1 per VGChartz (r/GameGazette post 12rmslr). $70 price point.",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, Windows, Switch",
      "publisher": "EA Sports",
      "copiesSold": 14000000,
      "estimatedRevenue": 980000000,
      "revenueSource": "No Reddit data; estimated (rebrand impact, $70 price)",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PS5, PS4, Xbox Series X/S, Xbox One, Windows, Switch",
      "publisher": "EA Sports",
      "copiesSold": 12000000,
      "estimatedRevenue": 840000000,
      "revenueSource": "No Reddit data; estimated (continued post-rebrand decline per community sentiment)",
      "confidence": "low"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PS5, Xbox Series X/S, Windows, Switch 2",
      "publisher": "EA Sports",
      "copiesSold": 10000000,
      "estimatedRevenue": 700000000,
      "revenueSource": "Reddit: outsold by Ghost of Yotei in UK launch week (r/gaming 1nzc677); top seller Black Friday Europe (r/Games 1pfo1ph)",
      "confidence": "low"
    }
  ],
  "totalRevenue": 20470000000,
  "totalGamesFound": 33,
  "searchQueries": [
    "FIFA complete game list every release history",
    "FIFA copies sold million sales figures",
    "FIFA best selling game UK NPD 2016",
    "FIFA 23 copies sold million",
    "\"FIFA\" million sold copies",
    "EA Sports FC FIFA sales revenue best selling",
    "FIFA 19 sales in the UK are down on FIFA 18",
    "FIFA series total sales 325 million 300 million",
    "FIFA International Soccer 1993 1994 FIFA 95 96 97 98 99 sales",
    "VGChartz FIFA sales data",
    "EA Sports FC 24 25 26 sales copies sold million",
    "FIFA 2001 2002 2003 2004 2005 World Cup game sales",
    "EA annual report FIFA units sold earnings",
    "FIFA game every year release list nostalgia history",
    "FIFA 10 11 12 sales million NPD chart",
    "FIFA 20 sales EA quarterly results million",
    "EA Sports FC 24 sales disappointing decline player count"
  ],
  "redditPostsAnalyzed": 17
}
```

---

## Data Quality Notes

- **High confidence (1 title):** FIFA 13 — 14.5M copies from EA's official FY13 quarterly report posted to r/Games
- **Medium confidence (3 titles):** FIFA 12 (>10M implied), FIFA 18 (2.7M UK extrapolated), FIFA 19 (2.5M UK extrapolated)
- **Low confidence (29 titles):** Estimated based on franchise growth trajectory, era pricing, and the commonly cited ~325M total franchise sales figure
- **Spin-offs excluded from main table:** World Cup games (5), FIFA Street (4), UEFA games (3), FIFA Online series — no Reddit sales data available for any spin-offs
- **Revenue is copy sales only** — excludes FIFA Ultimate Team microtransactions (which EA has reported as generating billions annually since ~2015)

---

*CLI Research Report — Iteration 1*
