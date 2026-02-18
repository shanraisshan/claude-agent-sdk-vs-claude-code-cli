# Comparison Report - Iteration 1

## Summary
- **Similarity Score**: 68.33%
- **Game Coverage Score**: 100.00%
- **Revenue Accuracy Score**: 36.67%
- **Converged**: No

## Game Coverage
- CLI found: 60 games
- SDK found: 60 games
- Matched: 60 games
- Total unique: 60 games

Both agents found the exact same set of 60 games after name normalization. The alias map correctly resolved "FIFA Street (2005)" from CLI to "FIFA Street" from SDK, and "FIFA Online 4 / FC Online" from SDK to "FIFA Online 4" from CLI. Game coverage is perfect at 100%.

### Missing from CLI
- (none)

### Missing from SDK
- (none)

## Revenue Discrepancies

38 out of 60 matched games have revenue differences greater than 10%, resulting in only 22 revenue-matched games (36.67% accuracy).

The core disagreement is in **revenue methodology**: the CLI agent estimates revenue based primarily on **unit sales x retail price** (game sales revenue only), while the SDK agent estimates **total franchise revenue per title year** including Ultimate Team microtransaction revenue. This explains why modern titles (FIFA 16 onwards) diverge massively -- FUT revenue dwarfs base game sales for recent titles.

| Game | CLI Revenue | SDK Revenue | Difference |
|------|------------|------------|------------|
| 1998 FIFA World Cup | $60,000,000 | $80,000,000 | 25.00% |
| 2002 FIFA World Cup | $80,000,000 | $100,000,000 | 20.00% |
| 2006 FIFA World Cup | $100,000,000 | $120,000,000 | 16.67% |
| 2010 FIFA World Cup South Africa | $120,000,000 | $150,000,000 | 20.00% |
| 2014 FIFA World Cup Brazil | $80,000,000 | $130,000,000 | 38.46% |
| EA Sports FC 24 | $1,050,000,000 | $2,500,000,000 | 58.00% |
| EA Sports FC 25 | $900,000,000 | $2,200,000,000 | 59.09% |
| EA Sports FC 26 | $600,000,000 | $1,500,000,000 | 60.00% |
| FIFA 06 | $200,000,000 | $300,000,000 | 33.33% |
| FIFA 07 | $220,000,000 | $350,000,000 | 37.14% |
| FIFA 08 | $250,000,000 | $400,000,000 | 37.50% |
| FIFA 09 | $300,000,000 | $450,000,000 | 33.33% |
| FIFA 11 | $800,000,000 | $550,000,000 | 31.25% |
| FIFA 14 | $700,000,000 | $900,000,000 | 22.22% |
| FIFA 15 | $725,000,000 | $1,000,000,000 | 27.50% |
| FIFA 16 | $550,000,000 | $1,100,000,000 | 50.00% |
| FIFA 17 | $650,000,000 | $1,200,000,000 | 45.83% |
| FIFA 18 | $1,320,000,000 | $1,500,000,000 | 12.00% |
| FIFA 19 | $1,000,000,000 | $1,600,000,000 | 37.50% |
| FIFA 20 | $800,000,000 | $1,800,000,000 | 55.56% |
| FIFA 21 | $1,000,000,000 | $2,000,000,000 | 50.00% |
| FIFA 22 | $900,000,000 | $2,200,000,000 | 59.09% |
| FIFA 23 | $1,100,000,000 | $2,600,000,000 | 57.69% |
| FIFA Football 2003 | $160,000,000 | $200,000,000 | 20.00% |
| FIFA Football 2004 | $170,000,000 | $220,000,000 | 22.73% |
| FIFA Manager 06 | $15,000,000 | $20,000,000 | 25.00% |
| FIFA Manager 07 | $15,000,000 | $18,000,000 | 16.67% |
| FIFA Manager 08 | $12,000,000 | $15,000,000 | 20.00% |
| FIFA Manager 09 | $10,000,000 | $12,000,000 | 16.67% |
| FIFA Manager 13 | $8,000,000 | $6,000,000 | 25.00% |
| FIFA Manager 14 | $6,000,000 | $5,000,000 | 16.67% |
| FIFA Soccer 96 | $75,000,000 | $60,000,000 | 20.00% |
| FIFA Soccer Manager | $5,000,000 | $10,000,000 | 50.00% |
| FIFA Street | $60,000,000 | $80,000,000 | 25.00% |
| FIFA Street 2 | $50,000,000 | $60,000,000 | 16.67% |
| Total Club Manager 2003 | $8,000,000 | $15,000,000 | 46.67% |
| Total Club Manager 2004 | $8,000,000 | $15,000,000 | 46.67% |
| Total Club Manager 2005 | $8,000,000 | $12,000,000 | 33.33% |

## Revenue-Matched Games (within 10% threshold)

These 22 games have revenue estimates that agree between CLI and SDK:

| Game | CLI Revenue | SDK Revenue | Difference |
|------|------------|------------|------------|
| FIFA 10 | $535,000,000 | $500,000,000 | 6.54% |
| FIFA 12 | $650,000,000 | $700,000,000 | 7.14% |
| FIFA 13 | $725,000,000 | $800,000,000 | 9.38% |
| FIFA 2000 | $120,000,000 | $130,000,000 | 7.69% |
| FIFA 2001 | $130,000,000 | $140,000,000 | 7.14% |
| FIFA 97 | $80,000,000 | $80,000,000 | 0.00% |
| FIFA 99 | $120,000,000 | $120,000,000 | 0.00% |
| FIFA Football 2002 | $150,000,000 | $150,000,000 | 0.00% |
| FIFA Football 2005 | $225,000,000 | $250,000,000 | 10.00% |
| FIFA International Soccer | $50,000,000 | $50,000,000 | 0.00% |
| FIFA Manager 10 | $10,000,000 | $10,000,000 | 0.00% |
| FIFA Manager 11 | $10,000,000 | $10,000,000 | 0.00% |
| FIFA Manager 12 | $8,000,000 | $8,000,000 | 0.00% |
| FIFA Mobile | $1,200,000,000 | $1,200,000,000 | 0.00% |
| FIFA Online | $20,000,000 | $20,000,000 | 0.00% |
| FIFA Online 2 | $30,000,000 | $30,000,000 | 0.00% |
| FIFA Online 3 | $500,000,000 | $500,000,000 | 0.00% |
| FIFA Online 4 | $800,000,000 | $800,000,000 | 0.00% |
| FIFA Soccer 95 | $40,000,000 | $40,000,000 | 0.00% |
| FIFA Street (2012) | $70,000,000 | $70,000,000 | 0.00% |
| FIFA Street 3 | $40,000,000 | $40,000,000 | 0.00% |
| FIFA: Road to World Cup 98 | $150,000,000 | $150,000,000 | 0.00% |

## Key Findings for Agent Evolution

1. **Revenue methodology mismatch is the primary issue.** The CLI agent focuses on unit sales revenue (copies sold x price), while the SDK agent includes Ultimate Team / microtransaction revenue in its per-title estimates. This creates massive divergence for titles from FIFA 15 onwards where FUT revenue exceeds base game sales.

2. **Pre-2005 titles largely agree.** Both agents converge on early titles where there was no microtransaction revenue -- the disagreements there are minor estimation differences.

3. **FIFA 16-23 and FC 24-26 have the largest gaps (45-60%).** The SDK estimates are roughly 2x the CLI estimates for modern titles, suggesting the SDK is counting total EA Sports FIFA segment revenue while CLI counts only game sales.

4. **Spin-off titles (Online, Mobile, Street) mostly agree.** These categories show high convergence since neither agent has strong data and both rely on similar estimation approaches.

5. **Both agents need to align on what "estimatedRevenue" means.** Either both should report game sales revenue only, or both should report total revenue including microtransactions. The current mismatch makes convergence impossible for modern titles.

## Recommendations for Iteration 2

- **CLI Agent**: Should be updated to include FUT/microtransaction revenue in estimates for titles from FIFA 09 onwards (when Ultimate Team was introduced), matching the SDK's methodology of total per-title-year revenue.
- **SDK Agent**: Should verify its estimates against EA's actual financial reports and ensure the growth curve is realistic (e.g., the smooth linear growth from $300M to $2.6B seems over-simplified).
- **Both Agents**: Should explicitly define "estimatedRevenue" as total revenue generated by that title including base game sales, DLC, and in-game microtransactions (Ultimate Team, etc.).

## Raw Comparison Data
```json
{
  "similarityScore": 68.33,
  "gameCoverageScore": 100.0,
  "revenueAccuracyScore": 36.67,
  "converged": false,
  "cliGamesCount": 60,
  "sdkGamesCount": 60,
  "matchedGamesCount": 60,
  "totalUniqueGames": 60,
  "matchedGames": [
    "1998 FIFA World Cup",
    "2002 FIFA World Cup",
    "2006 FIFA World Cup",
    "2010 FIFA World Cup South Africa",
    "2014 FIFA World Cup Brazil",
    "EA Sports FC 24",
    "EA Sports FC 25",
    "EA Sports FC 26",
    "FIFA 06",
    "FIFA 07",
    "FIFA 08",
    "FIFA 09",
    "FIFA 10",
    "FIFA 11",
    "FIFA 12",
    "FIFA 13",
    "FIFA 14",
    "FIFA 15",
    "FIFA 16",
    "FIFA 17",
    "FIFA 18",
    "FIFA 19",
    "FIFA 20",
    "FIFA 2000",
    "FIFA 2001",
    "FIFA 21",
    "FIFA 22",
    "FIFA 23",
    "FIFA 97",
    "FIFA 99",
    "FIFA Football 2002",
    "FIFA Football 2003",
    "FIFA Football 2004",
    "FIFA Football 2005",
    "FIFA International Soccer",
    "FIFA Manager 06",
    "FIFA Manager 07",
    "FIFA Manager 08",
    "FIFA Manager 09",
    "FIFA Manager 10",
    "FIFA Manager 11",
    "FIFA Manager 12",
    "FIFA Manager 13",
    "FIFA Manager 14",
    "FIFA Mobile",
    "FIFA Online",
    "FIFA Online 2",
    "FIFA Online 3",
    "FIFA Online 4",
    "FIFA Soccer 95",
    "FIFA Soccer 96",
    "FIFA Soccer Manager",
    "FIFA Street",
    "FIFA Street (2012)",
    "FIFA Street 2",
    "FIFA Street 3",
    "FIFA: Road to World Cup 98",
    "Total Club Manager 2003",
    "Total Club Manager 2004",
    "Total Club Manager 2005"
  ],
  "missingFromCli": [],
  "missingFromSdk": [],
  "revenueDiscrepancies": [
    {"name": "1998 FIFA World Cup", "cliRevenue": 60000000, "sdkRevenue": 80000000, "percentDifference": 25.0},
    {"name": "2002 FIFA World Cup", "cliRevenue": 80000000, "sdkRevenue": 100000000, "percentDifference": 20.0},
    {"name": "2006 FIFA World Cup", "cliRevenue": 100000000, "sdkRevenue": 120000000, "percentDifference": 16.67},
    {"name": "2010 FIFA World Cup South Africa", "cliRevenue": 120000000, "sdkRevenue": 150000000, "percentDifference": 20.0},
    {"name": "2014 FIFA World Cup Brazil", "cliRevenue": 80000000, "sdkRevenue": 130000000, "percentDifference": 38.46},
    {"name": "EA Sports FC 24", "cliRevenue": 1050000000, "sdkRevenue": 2500000000, "percentDifference": 58.0},
    {"name": "EA Sports FC 25", "cliRevenue": 900000000, "sdkRevenue": 2200000000, "percentDifference": 59.09},
    {"name": "EA Sports FC 26", "cliRevenue": 600000000, "sdkRevenue": 1500000000, "percentDifference": 60.0},
    {"name": "FIFA 06", "cliRevenue": 200000000, "sdkRevenue": 300000000, "percentDifference": 33.33},
    {"name": "FIFA 07", "cliRevenue": 220000000, "sdkRevenue": 350000000, "percentDifference": 37.14},
    {"name": "FIFA 08", "cliRevenue": 250000000, "sdkRevenue": 400000000, "percentDifference": 37.5},
    {"name": "FIFA 09", "cliRevenue": 300000000, "sdkRevenue": 450000000, "percentDifference": 33.33},
    {"name": "FIFA 11", "cliRevenue": 800000000, "sdkRevenue": 550000000, "percentDifference": 31.25},
    {"name": "FIFA 14", "cliRevenue": 700000000, "sdkRevenue": 900000000, "percentDifference": 22.22},
    {"name": "FIFA 15", "cliRevenue": 725000000, "sdkRevenue": 1000000000, "percentDifference": 27.5},
    {"name": "FIFA 16", "cliRevenue": 550000000, "sdkRevenue": 1100000000, "percentDifference": 50.0},
    {"name": "FIFA 17", "cliRevenue": 650000000, "sdkRevenue": 1200000000, "percentDifference": 45.83},
    {"name": "FIFA 18", "cliRevenue": 1320000000, "sdkRevenue": 1500000000, "percentDifference": 12.0},
    {"name": "FIFA 19", "cliRevenue": 1000000000, "sdkRevenue": 1600000000, "percentDifference": 37.5},
    {"name": "FIFA 20", "cliRevenue": 800000000, "sdkRevenue": 1800000000, "percentDifference": 55.56},
    {"name": "FIFA 21", "cliRevenue": 1000000000, "sdkRevenue": 2000000000, "percentDifference": 50.0},
    {"name": "FIFA 22", "cliRevenue": 900000000, "sdkRevenue": 2200000000, "percentDifference": 59.09},
    {"name": "FIFA 23", "cliRevenue": 1100000000, "sdkRevenue": 2600000000, "percentDifference": 57.69},
    {"name": "FIFA Football 2003", "cliRevenue": 160000000, "sdkRevenue": 200000000, "percentDifference": 20.0},
    {"name": "FIFA Football 2004", "cliRevenue": 170000000, "sdkRevenue": 220000000, "percentDifference": 22.73},
    {"name": "FIFA Manager 06", "cliRevenue": 15000000, "sdkRevenue": 20000000, "percentDifference": 25.0},
    {"name": "FIFA Manager 07", "cliRevenue": 15000000, "sdkRevenue": 18000000, "percentDifference": 16.67},
    {"name": "FIFA Manager 08", "cliRevenue": 12000000, "sdkRevenue": 15000000, "percentDifference": 20.0},
    {"name": "FIFA Manager 09", "cliRevenue": 10000000, "sdkRevenue": 12000000, "percentDifference": 16.67},
    {"name": "FIFA Manager 13", "cliRevenue": 8000000, "sdkRevenue": 6000000, "percentDifference": 25.0},
    {"name": "FIFA Manager 14", "cliRevenue": 6000000, "sdkRevenue": 5000000, "percentDifference": 16.67},
    {"name": "FIFA Soccer 96", "cliRevenue": 75000000, "sdkRevenue": 60000000, "percentDifference": 20.0},
    {"name": "FIFA Soccer Manager", "cliRevenue": 5000000, "sdkRevenue": 10000000, "percentDifference": 50.0},
    {"name": "FIFA Street", "cliRevenue": 60000000, "sdkRevenue": 80000000, "percentDifference": 25.0},
    {"name": "FIFA Street 2", "cliRevenue": 50000000, "sdkRevenue": 60000000, "percentDifference": 16.67},
    {"name": "Total Club Manager 2003", "cliRevenue": 8000000, "sdkRevenue": 15000000, "percentDifference": 46.67},
    {"name": "Total Club Manager 2004", "cliRevenue": 8000000, "sdkRevenue": 15000000, "percentDifference": 46.67},
    {"name": "Total Club Manager 2005", "cliRevenue": 8000000, "sdkRevenue": 12000000, "percentDifference": 33.33}
  ]
}
```
