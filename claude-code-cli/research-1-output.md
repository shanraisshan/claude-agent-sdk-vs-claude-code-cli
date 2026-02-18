# FIFA/EA FC Game Research - Iteration 1 (CLI Agent)

## Summary

This research covers the complete FIFA/EA Sports FC video game franchise from 1993 through EA Sports FC 26 (2025). The franchise has sold over **325 million copies** as of 2021 and generated over **$7 billion annually** by fiscal year 2023, making it the best-selling sports video game franchise in the world (Guinness World Records).

### Key Findings

- **Main Series**: 32 annual releases from FIFA International Soccer (1993) through EA Sports FC 26 (2025)
- **FIFA World Cup Tie-ins**: 6 dedicated World Cup games (1998-2014)
- **FIFA Street Series**: 4 games (2005-2012)
- **FIFA Online Series**: 4 games (2006-2018), primarily Asian markets
- **FIFA Manager Series**: 9 games under FIFA Manager branding (2005-2013), plus earlier Total Club Manager/FA Premier League titles
- **FIFA Mobile**: Launched 2016, rebranded to EA FC Mobile; surpassed $1 billion lifetime revenue
- **Ultimate Team**: Generates approximately $1.5-1.7 billion annually, accounting for 73-75% of franchise revenue

### Revenue Notes

- Total franchise revenue exceeds $20 billion lifetime (conservative estimate based on 30 years of sales + microtransactions)
- FIFA 23 was the most successful launch in franchise history
- EA Sports FC 24 earned more revenue than FIFA 23 despite selling ~5% fewer copies
- EA Sports FC 26 sold 10 million copies in under two weeks

---

```json
{
  "games": [
    {
      "name": "FIFA International Soccer",
      "year": 1993,
      "platform": "Sega Genesis/Mega Drive, SNES, Game Boy, Amiga, DOS, Master System, Game Gear",
      "publisher": "EA Sports",
      "estimatedRevenue": 50000000,
      "revenueSource": "Estimated from 500K+ copies sold in first 4 weeks at ~$50 MSRP; total lifetime sales likely 1M+",
      "confidence": "low"
    },
    {
      "name": "FIFA Soccer 95",
      "year": 1994,
      "platform": "Sega Genesis/Mega Drive, SNES, Game Boy, Game Gear",
      "publisher": "EA Sports",
      "estimatedRevenue": 40000000,
      "revenueSource": "Estimated based on franchise growth trajectory; limited public sales data",
      "confidence": "low"
    },
    {
      "name": "FIFA Soccer 96",
      "year": 1995,
      "platform": "Sega Genesis/Mega Drive, SNES, PlayStation, Saturn, Game Boy, Game Gear, DOS, Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 75000000,
      "revenueSource": "Estimated; first entry on PlayStation expanded market significantly",
      "confidence": "low"
    },
    {
      "name": "FIFA 97",
      "year": 1996,
      "platform": "PlayStation, Sega Saturn, SNES, Genesis, Windows, Game Boy",
      "publisher": "EA Sports",
      "estimatedRevenue": 80000000,
      "revenueSource": "Estimated based on growing PlayStation installed base and franchise popularity",
      "confidence": "low"
    },
    {
      "name": "FIFA: Road to World Cup 98",
      "year": 1997,
      "platform": "PlayStation, Nintendo 64, Windows, SNES, Sega Saturn, Game Boy",
      "publisher": "EA Sports",
      "estimatedRevenue": 150000000,
      "revenueSource": "Estimated; World Cup tie-in year boosted sales significantly; one of the most popular early entries",
      "confidence": "low"
    },
    {
      "name": "FIFA 99",
      "year": 1998,
      "platform": "PlayStation, Nintendo 64, Windows, Game Boy Color",
      "publisher": "EA Sports",
      "estimatedRevenue": 120000000,
      "revenueSource": "Estimated based on late-90s franchise trajectory",
      "confidence": "low"
    },
    {
      "name": "FIFA 2000",
      "year": 1999,
      "platform": "PlayStation, Windows, Game Boy Color",
      "publisher": "EA Sports",
      "estimatedRevenue": 120000000,
      "revenueSource": "Estimated based on franchise trajectory",
      "confidence": "low"
    },
    {
      "name": "FIFA 2001",
      "year": 2000,
      "platform": "PlayStation, PlayStation 2, Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 130000000,
      "revenueSource": "Estimated; PS2 launch year expanded market",
      "confidence": "low"
    },
    {
      "name": "FIFA Football 2002",
      "year": 2001,
      "platform": "PlayStation, PlayStation 2, Windows, GameCube, Xbox",
      "publisher": "EA Sports",
      "estimatedRevenue": 150000000,
      "revenueSource": "Estimated; World Cup year boost, multi-platform expansion",
      "confidence": "low"
    },
    {
      "name": "FIFA Football 2003",
      "year": 2002,
      "platform": "PlayStation, PlayStation 2, Windows, GameCube, Xbox, Game Boy Advance",
      "publisher": "EA Sports",
      "estimatedRevenue": 160000000,
      "revenueSource": "Estimated based on growing console market",
      "confidence": "low"
    },
    {
      "name": "FIFA Football 2004",
      "year": 2003,
      "platform": "PlayStation, PlayStation 2, Windows, GameCube, Xbox, Game Boy Advance",
      "publisher": "EA Sports",
      "estimatedRevenue": 170000000,
      "revenueSource": "Estimated based on franchise growth",
      "confidence": "low"
    },
    {
      "name": "FIFA Football 2005",
      "year": 2004,
      "platform": "PlayStation 2, Windows, Xbox, GameCube, Game Boy Advance, PSP, Nintendo DS",
      "publisher": "EA Sports",
      "estimatedRevenue": 225000000,
      "revenueSource": "4.5 million+ copies sold at ~$50 MSRP; VGChartz and Video Game Sales Wiki",
      "confidence": "medium"
    },
    {
      "name": "FIFA 06",
      "year": 2005,
      "platform": "PlayStation 2, Xbox, Xbox 360, GameCube, Windows, PSP, Game Boy Advance, Nintendo DS",
      "publisher": "EA Sports",
      "estimatedRevenue": 200000000,
      "revenueSource": "Estimated; first entry on Xbox 360",
      "confidence": "low"
    },
    {
      "name": "FIFA 07",
      "year": 2006,
      "platform": "PlayStation 2, Xbox 360, Windows, PSP, Nintendo DS, Wii, Game Boy Advance",
      "publisher": "EA Sports",
      "estimatedRevenue": 220000000,
      "revenueSource": "Estimated based on franchise trajectory and next-gen console growth",
      "confidence": "low"
    },
    {
      "name": "FIFA 08",
      "year": 2007,
      "platform": "PlayStation 2, PlayStation 3, Xbox 360, Wii, Windows, PSP, Nintendo DS",
      "publisher": "EA Sports",
      "estimatedRevenue": 250000000,
      "revenueSource": "Estimated; PS3 and Xbox 360 growing installed base",
      "confidence": "low"
    },
    {
      "name": "FIFA 09",
      "year": 2008,
      "platform": "PlayStation 2, PlayStation 3, Xbox 360, Wii, Windows, PSP, Nintendo DS",
      "publisher": "EA Sports",
      "estimatedRevenue": 300000000,
      "revenueSource": "Estimated based on growing franchise sales",
      "confidence": "low"
    },
    {
      "name": "FIFA 10",
      "year": 2009,
      "platform": "PlayStation 2, PlayStation 3, Xbox 360, Wii, Windows, PSP, iOS",
      "publisher": "EA Sports",
      "estimatedRevenue": 535000000,
      "revenueSource": "10.72 million copies sold at ~$50 avg; VGChartz data",
      "confidence": "medium"
    },
    {
      "name": "FIFA 11",
      "year": 2010,
      "platform": "PlayStation 2, PlayStation 3, Xbox 360, Wii, Windows, PSP, Nintendo DS, iOS",
      "publisher": "EA Sports",
      "estimatedRevenue": 800000000,
      "revenueSource": "16 million copies sold at ~$50 avg; Game Rant / VGChartz best-selling rankings",
      "confidence": "medium"
    },
    {
      "name": "FIFA 12",
      "year": 2011,
      "platform": "PlayStation 2, PlayStation 3, Xbox 360, Wii, Windows, PSP, PS Vita, Nintendo 3DS, iOS",
      "publisher": "EA Sports",
      "estimatedRevenue": 650000000,
      "revenueSource": "13.06 million copies sold; set EA Sports sales record at launch; Game Rant",
      "confidence": "medium"
    },
    {
      "name": "FIFA 13",
      "year": 2012,
      "platform": "PlayStation 2, PlayStation 3, Xbox 360, Wii, Wii U, Windows, PSP, PS Vita, Nintendo 3DS, iOS",
      "publisher": "EA Sports",
      "estimatedRevenue": 725000000,
      "revenueSource": "14.5 million units sold at ~$50 avg; FIFA Infinity / VGChartz",
      "confidence": "medium"
    },
    {
      "name": "FIFA 14",
      "year": 2013,
      "platform": "PlayStation 3, PlayStation 4, Xbox 360, Xbox One, Windows, PS Vita, Nintendo 3DS, iOS, Android",
      "publisher": "EA Sports",
      "estimatedRevenue": 700000000,
      "revenueSource": "14 million copies sold; first entry on PS4/Xbox One; Video Game Sales Wiki",
      "confidence": "medium"
    },
    {
      "name": "FIFA 15",
      "year": 2014,
      "platform": "PlayStation 3, PlayStation 4, Xbox 360, Xbox One, Windows, PS Vita, Nintendo 3DS, iOS, Android",
      "publisher": "EA Sports",
      "estimatedRevenue": 725000000,
      "revenueSource": "14.5 million units sold at ~$50 avg; Game Rant rankings",
      "confidence": "medium"
    },
    {
      "name": "FIFA 16",
      "year": 2015,
      "platform": "PlayStation 3, PlayStation 4, Xbox 360, Xbox One, Windows, iOS, Android",
      "publisher": "EA Sports",
      "estimatedRevenue": 550000000,
      "revenueSource": "11 million+ copies sold at ~$50 avg; some sources cite up to 18.79M; using conservative figure",
      "confidence": "medium"
    },
    {
      "name": "FIFA 17",
      "year": 2016,
      "platform": "PlayStation 3, PlayStation 4, Xbox 360, Xbox One, Windows, Nintendo Switch",
      "publisher": "EA Sports",
      "estimatedRevenue": 650000000,
      "revenueSource": "13 million units sold at ~$50 avg; Game Rant / FIFA Infinity",
      "confidence": "medium"
    },
    {
      "name": "FIFA 18",
      "year": 2017,
      "platform": "PlayStation 3, PlayStation 4, Xbox 360, Xbox One, Windows, Nintendo Switch",
      "publisher": "EA Sports",
      "estimatedRevenue": 1320000000,
      "revenueSource": "26.4 million units sold (best-selling FIFA ever by units) at ~$50 avg; Game Rant",
      "confidence": "medium"
    },
    {
      "name": "FIFA 19",
      "year": 2018,
      "platform": "PlayStation 3, PlayStation 4, Xbox 360, Xbox One, Windows, Nintendo Switch",
      "publisher": "EA Sports",
      "estimatedRevenue": 1000000000,
      "revenueSource": "20 million+ units sold at ~$50 avg; sports-king.com / Game Rant",
      "confidence": "medium"
    },
    {
      "name": "FIFA 20",
      "year": 2019,
      "platform": "PlayStation 4, Xbox One, Windows, Nintendo Switch",
      "publisher": "EA Sports",
      "estimatedRevenue": 800000000,
      "revenueSource": "Estimated ~15M copies based on franchise trend; limited specific public data",
      "confidence": "low"
    },
    {
      "name": "FIFA 21",
      "year": 2020,
      "platform": "PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S, Windows, Nintendo Switch, Stadia",
      "publisher": "EA Sports",
      "estimatedRevenue": 1000000000,
      "revenueSource": "25 million+ players; EA fiscal Q4 2021 showed $1.34B revenue contribution; Goal.com / EA IR",
      "confidence": "medium"
    },
    {
      "name": "FIFA 22",
      "year": 2021,
      "platform": "PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S, Windows, Nintendo Switch, Stadia",
      "publisher": "EA Sports",
      "estimatedRevenue": 900000000,
      "revenueSource": "9.1 million copies in first 10 days; total ~18M estimated; VGChartz / Statista",
      "confidence": "medium"
    },
    {
      "name": "FIFA 23",
      "year": 2022,
      "platform": "PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S, Windows, Nintendo Switch",
      "publisher": "EA Sports",
      "estimatedRevenue": 1100000000,
      "revenueSource": "10.3M copies first week; outsold FIFA 22 lifetime in 6 months; record launch; VGChartz / EA IR",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 24",
      "year": 2023,
      "platform": "PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S, Windows, Nintendo Switch",
      "publisher": "EA Sports",
      "estimatedRevenue": 1050000000,
      "revenueSource": "6.8M early access copies; ~5% fewer total sales than FIFA 23 but higher revenue from UT; EA IR / GagaGadget",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 25",
      "year": 2024,
      "platform": "PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S, Windows, Nintendo Switch",
      "publisher": "EA Sports",
      "estimatedRevenue": 900000000,
      "revenueSource": "19.2M PlayStation sales; underperformed expectations per EA guidance cut Jan 2025; Accio / PocketGamer",
      "confidence": "medium"
    },
    {
      "name": "EA Sports FC 26",
      "year": 2025,
      "platform": "PlayStation 5, Xbox Series X/S, Windows, Nintendo Switch 2",
      "publisher": "EA Sports",
      "estimatedRevenue": 600000000,
      "revenueSource": "10M copies in under 2 weeks; fastest-selling sports game 2025; still accumulating revenue; KitGuru / NotebookCheck",
      "confidence": "low"
    },
    {
      "name": "1998 FIFA World Cup",
      "year": 1998,
      "platform": "PlayStation, Windows, Nintendo 64",
      "publisher": "EA Sports",
      "estimatedRevenue": 60000000,
      "revenueSource": "Estimated; first officially licensed World Cup game; Wikipedia",
      "confidence": "low"
    },
    {
      "name": "2002 FIFA World Cup",
      "year": 2002,
      "platform": "PlayStation, PlayStation 2, Xbox, GameCube, Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 80000000,
      "revenueSource": "Estimated based on World Cup game popularity",
      "confidence": "low"
    },
    {
      "name": "2006 FIFA World Cup",
      "year": 2006,
      "platform": "PlayStation 2, Xbox, Xbox 360, GameCube, Windows, PSP, Nintendo DS, Game Boy Advance",
      "publisher": "EA Sports",
      "estimatedRevenue": 100000000,
      "revenueSource": "Estimated; released April 2006 with strong multi-platform presence",
      "confidence": "low"
    },
    {
      "name": "2010 FIFA World Cup South Africa",
      "year": 2010,
      "platform": "PlayStation 3, Xbox 360, Wii, PSP",
      "publisher": "EA Sports",
      "estimatedRevenue": 120000000,
      "revenueSource": "Estimated based on growing franchise and next-gen console adoption",
      "confidence": "low"
    },
    {
      "name": "2014 FIFA World Cup Brazil",
      "year": 2014,
      "platform": "PlayStation 3, Xbox 360",
      "publisher": "EA Sports",
      "estimatedRevenue": 80000000,
      "revenueSource": "Estimated; limited to last-gen consoles only",
      "confidence": "low"
    },
    {
      "name": "FIFA Street (2005)",
      "year": 2005,
      "platform": "PlayStation 2, Xbox, GameCube",
      "publisher": "EA Sports BIG",
      "estimatedRevenue": 60000000,
      "revenueSource": "Estimated based on EA Sports BIG franchise performance",
      "confidence": "low"
    },
    {
      "name": "FIFA Street 2",
      "year": 2006,
      "platform": "PlayStation 2, Xbox, GameCube, PSP, Nintendo DS",
      "publisher": "EA Sports BIG",
      "estimatedRevenue": 50000000,
      "revenueSource": "Estimated; sequel with wider platform support",
      "confidence": "low"
    },
    {
      "name": "FIFA Street 3",
      "year": 2008,
      "platform": "PlayStation 3, Xbox 360, Nintendo DS",
      "publisher": "EA Sports BIG",
      "estimatedRevenue": 40000000,
      "revenueSource": "Estimated; next-gen exclusive limited audience",
      "confidence": "low"
    },
    {
      "name": "FIFA Street (2012)",
      "year": 2012,
      "platform": "PlayStation 3, Xbox 360",
      "publisher": "EA Sports",
      "estimatedRevenue": 70000000,
      "revenueSource": "Estimated; reboot with strong reviews",
      "confidence": "low"
    },
    {
      "name": "FIFA Online",
      "year": 2006,
      "platform": "PC (South Korea)",
      "publisher": "EA Sports / Neowiz",
      "estimatedRevenue": 20000000,
      "revenueSource": "Estimated; free-to-play with microtransactions; limited market",
      "confidence": "low"
    },
    {
      "name": "FIFA Online 2",
      "year": 2007,
      "platform": "PC (Asia)",
      "publisher": "EA Sports / Neowiz",
      "estimatedRevenue": 30000000,
      "revenueSource": "Estimated; expanded Asian market presence",
      "confidence": "low"
    },
    {
      "name": "FIFA Online 3",
      "year": 2012,
      "platform": "PC (South Korea, China, Southeast Asia)",
      "publisher": "EA Sports / Tencent / Garena",
      "estimatedRevenue": 500000000,
      "revenueSource": "Estimated; #1 online sports game in Korea by revenue; Tencent published in China 2014; operated until 2021; N4G / Yahoo Finance",
      "confidence": "low"
    },
    {
      "name": "FIFA Online 4",
      "year": 2018,
      "platform": "PC (South Korea, China, Southeast Asia)",
      "publisher": "EA Sports / Nexon / Tencent",
      "estimatedRevenue": 800000000,
      "revenueSource": "Estimated; drove Nexon record-breaking Q1 2023 revenue; major revenue driver in Asian markets; MMOBomb",
      "confidence": "low"
    },
    {
      "name": "FIFA Mobile / EA FC Mobile",
      "year": 2016,
      "platform": "iOS, Android",
      "publisher": "EA Sports",
      "estimatedRevenue": 1200000000,
      "revenueSource": "Surpassed $1B lifetime revenue threshold; $172M in 2024 alone; PocketGamer / Sensor Tower",
      "confidence": "medium"
    },
    {
      "name": "FIFA Manager 06",
      "year": 2005,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 15000000,
      "revenueSource": "Estimated; niche management sim market",
      "confidence": "low"
    },
    {
      "name": "FIFA Manager 07",
      "year": 2006,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 15000000,
      "revenueSource": "Estimated; niche management sim market",
      "confidence": "low"
    },
    {
      "name": "FIFA Manager 08",
      "year": 2007,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 12000000,
      "revenueSource": "Estimated; declining interest in EA manager games",
      "confidence": "low"
    },
    {
      "name": "FIFA Manager 09",
      "year": 2008,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 10000000,
      "revenueSource": "Estimated; niche PC-only title",
      "confidence": "low"
    },
    {
      "name": "FIFA Manager 10",
      "year": 2009,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 10000000,
      "revenueSource": "Estimated; niche PC-only title",
      "confidence": "low"
    },
    {
      "name": "FIFA Manager 11",
      "year": 2010,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 10000000,
      "revenueSource": "Estimated; niche PC-only title",
      "confidence": "low"
    },
    {
      "name": "FIFA Manager 12",
      "year": 2011,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 8000000,
      "revenueSource": "Estimated; declining series",
      "confidence": "low"
    },
    {
      "name": "FIFA Manager 13",
      "year": 2012,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 8000000,
      "revenueSource": "Estimated; declining series",
      "confidence": "low"
    },
    {
      "name": "FIFA Manager 14",
      "year": 2013,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 6000000,
      "revenueSource": "Estimated; final entry in series, limited market",
      "confidence": "low"
    },
    {
      "name": "FIFA Soccer Manager",
      "year": 1997,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 5000000,
      "revenueSource": "Estimated; early management game with limited market",
      "confidence": "low"
    },
    {
      "name": "Total Club Manager 2003",
      "year": 2002,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 8000000,
      "revenueSource": "Estimated; predecessor to FIFA Manager series",
      "confidence": "low"
    },
    {
      "name": "Total Club Manager 2004",
      "year": 2003,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 8000000,
      "revenueSource": "Estimated; predecessor to FIFA Manager series",
      "confidence": "low"
    },
    {
      "name": "Total Club Manager 2005",
      "year": 2004,
      "platform": "Windows",
      "publisher": "EA Sports",
      "estimatedRevenue": 8000000,
      "revenueSource": "Estimated; predecessor to FIFA Manager series",
      "confidence": "low"
    }
  ],
  "totalGamesFound": 58,
  "searchQueries": [
    "complete list all FIFA video games EA Sports 1993 to EA FC 26",
    "FIFA game franchise total revenue sales by title EA Sports annual",
    "FIFA Street 1 2 3 game releases years platforms",
    "FIFA Online 1 2 3 4 game releases revenue China Korea",
    "FIFA Mobile EA FC Mobile revenue 2024 2025 lifetime",
    "FIFA Manager series all games list releases",
    "FIFA 23 FIFA 22 FIFA 21 FIFA 20 individual game sales copies sold revenue",
    "EA Sports FC 24 FC 25 FC 26 sales copies sold revenue 2025",
    "FIFA 14 15 16 17 18 19 copies sold sales each title",
    "FIFA 96 97 98 99 2000 2001 2002 2003 2004 2005 copies sold sales",
    "FIFA International Soccer 1993 1994 copies sold revenue early FIFA games sales",
    "best selling FIFA games ranked all time complete list units sold",
    "FIFA World Cup games 1998 2002 2006 2010 2014 EA Sports releases"
  ],
  "sources": [
    "https://en.wikipedia.org/wiki/FIFA_(video_game_series)",
    "https://easportsfc.fandom.com/wiki/List_of_FIFA_games",
    "https://vgsales.fandom.com/wiki/FIFA",
    "https://vgsales.fandom.com/wiki/EA_Sports_FC",
    "https://gamerant.com/fifa-games-best-selling-ranked-sales/",
    "https://www.fifa-infinity.com/fifa-23/top-10-best-selling/",
    "https://arthnova.com/how-ea-fifa-made-7-billion-before-rebrand/",
    "https://www.goal.com/en-us/news/how-much-money-does-ea-sports-make-from-fifa--ultimate-team/r1tbutqcbjhx19gkz54rtrp68",
    "https://ir.ea.com/press-releases/press-release-details/2023/Electronic-Arts-Reports-Q4-and-FY23-Results/default.aspx",
    "https://www.pocketgamer.biz/fifa-mobile-passes-1bn-revenue-threshold/",
    "https://sensortower.com/blog/ea-sports-mobile-revenue-1-billion",
    "https://en.wikipedia.org/wiki/FIFA_World_Cup_video_games",
    "https://en.wikipedia.org/wiki/FIFA_Manager",
    "https://www.vgchartz.com/gamedb/?name=fifa",
    "https://www.accio.com/business/best-selling-ea-sports-fc-25-sales-numbers",
    "https://www.kitguru.net/tech-news/mustafa-mahmoud/ea-sports-fc26-has-reportedly-sold-over-10-million-copies-already/",
    "https://www.mmobomb.com/news/nexon-reports-record-breaking-first-quarter-revenue-backs-of-fifa-online-4-fifa-mobile",
    "https://www.pcgamer.com/ea-earnings-call-show-ea-sports-fc-was-a-game-of-two-halves-as-it-fails-to-out-sell-the-last-fifa-but-still-makes-more-money/",
    "https://gagadget.com/en/games-announce/329628-number-of-copies-of-ea-sports-fc-24-sold-exceeds-68-million/"
  ]
}
```
