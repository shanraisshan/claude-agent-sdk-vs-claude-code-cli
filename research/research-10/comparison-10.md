# Comparison Report - Iteration 10

## Summary
- **Similarity Score**: 50%
- **Coverage Score**: 100%
- **Value Accuracy Score**: 0%
- **Converged**: no

## Coverage
- CLI found (ground truth): 3 games
- SDK found: 4 games
- Matched: 3 games

### Missing from SDK
- (none)

### Extra in SDK
- FIFA 23

## Value Discrepancies
| Game | CLI Revenue (Truth) | SDK Revenue | Difference |
|------|-------------------|-------------|------------|
| EA Sports FC 24 | $715,000,000 | $520,000,000 | 27.27% |
| EA Sports FC 25 | $525,000,000 | $292,500,000 | 44.29% |
| EA Sports FC 26 | $490,000,000 | $280,000,000 | 42.86% |

## Raw Comparison Data
```json
{
  "iteration": 10,
  "similarityScore": 50,
  "coverageScore": 100,
  "valueAccuracyScore": 0,
  "converged": false,
  "cli": {
    "totalGames": 3,
    "games": [
      {"name": "EA Sports FC 24", "estimatedRevenue": 715000000},
      {"name": "EA Sports FC 25", "estimatedRevenue": 525000000},
      {"name": "EA Sports FC 26", "estimatedRevenue": 490000000}
    ]
  },
  "sdk": {
    "totalGames": 4,
    "games": [
      {"name": "FIFA 23", "estimatedRevenue": 600000000},
      {"name": "EA Sports FC 24", "estimatedRevenue": 520000000},
      {"name": "EA Sports FC 25", "estimatedRevenue": 292500000},
      {"name": "EA Sports FC 26", "estimatedRevenue": 280000000}
    ]
  },
  "matched": [
    {"name": "EA Sports FC 24", "cliRevenue": 715000000, "sdkRevenue": 520000000, "differencePercent": 27.27, "valueMatched": false},
    {"name": "EA Sports FC 25", "cliRevenue": 525000000, "sdkRevenue": 292500000, "differencePercent": 44.29, "valueMatched": false},
    {"name": "EA Sports FC 26", "cliRevenue": 490000000, "sdkRevenue": 280000000, "differencePercent": 42.86, "valueMatched": false}
  ],
  "missingFromSdk": [],
  "extraInSdk": ["FIFA 23"]
}
```
