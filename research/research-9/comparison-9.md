# Comparison Report - Iteration 9

## Summary
- **Similarity Score**: 50%
- **Coverage Score**: 100%
- **Value Accuracy Score**: 0%
- **Converged**: no

## Coverage
- CLI found (ground truth): 4 games
- SDK found: 4 games
- Matched: 4 games

### Missing from SDK
- (none)

### Extra in SDK
- (none)

## Value Discrepancies
| Game | CLI Revenue (Truth) | SDK Revenue | Difference |
|------|-------------------|-------------|------------|
| FIFA 23 | $617,400,000 | $810,000,000 | 31.2% |
| EA Sports FC 24 | $595,000,000 | $770,000,000 | 29.4% |
| EA Sports FC 25 | $385,000,000 | $560,000,000 | 45.5% |
| EA Sports FC 26 | $455,000,000 | $595,000,000 | 30.8% |

## Raw Comparison Data
```json
{
  "iteration": 9,
  "similarityScore": 50.0,
  "coverageScore": 100.0,
  "valueAccuracyScore": 0.0,
  "converged": false,
  "cli": {
    "totalGames": 4,
    "games": [
      {"name": "FIFA 23", "estimatedRevenue": 617400000},
      {"name": "EA Sports FC 24", "estimatedRevenue": 595000000},
      {"name": "EA Sports FC 25", "estimatedRevenue": 385000000},
      {"name": "EA Sports FC 26", "estimatedRevenue": 455000000}
    ],
    "totalRevenue": 2052400000
  },
  "sdk": {
    "totalGames": 4,
    "games": [
      {"name": "FIFA 23", "estimatedRevenue": 810000000},
      {"name": "EA Sports FC 24", "estimatedRevenue": 770000000},
      {"name": "EA Sports FC 25", "estimatedRevenue": 560000000},
      {"name": "EA Sports FC 26", "estimatedRevenue": 595000000}
    ],
    "totalRevenue": 2735000000
  },
  "matchedGames": [
    {"name": "FIFA 23", "cliRevenue": 617400000, "sdkRevenue": 810000000, "percentDifference": 31.2, "valueMatched": false},
    {"name": "EA Sports FC 24", "cliRevenue": 595000000, "sdkRevenue": 770000000, "percentDifference": 29.4, "valueMatched": false},
    {"name": "EA Sports FC 25", "cliRevenue": 385000000, "sdkRevenue": 560000000, "percentDifference": 45.5, "valueMatched": false},
    {"name": "EA Sports FC 26", "cliRevenue": 455000000, "sdkRevenue": 595000000, "percentDifference": 30.8, "valueMatched": false}
  ],
  "missingFromSdk": [],
  "extraInSdk": []
}
```
