# Comparison Report - Iteration 6

## Summary
- **Similarity Score**: 54.17%
- **Coverage Score**: 75%
- **Value Accuracy Score**: 33.33%
- **Converged**: no

## Coverage
- CLI found (ground truth): 4 games
- SDK found: 3 games
- Matched: 3 games

### Missing from SDK
- EA Sports FC 26

### Extra in SDK
- (none)

## Value Discrepancies
| Game | CLI Revenue (Truth) | SDK Revenue | Difference |
|------|-------------------|-------------|------------|
| FIFA 23 | $810,000,000 | $660,000,000 | 18.52% |
| EA Sports FC 24 | $770,000,000 | $700,000,000 | 9.09% |
| EA Sports FC 25 | $560,000,000 | $665,000,000 | 18.75% |

## Raw Comparison Data
```json
{
  "iteration": 6,
  "similarityScore": 54.17,
  "coverageScore": 75,
  "valueAccuracyScore": 33.33,
  "converged": false,
  "cliGames": [
    {"name": "FIFA 23", "estimatedRevenue": 810000000},
    {"name": "EA Sports FC 24", "estimatedRevenue": 770000000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 560000000},
    {"name": "EA Sports FC 26", "estimatedRevenue": 665000000}
  ],
  "sdkGames": [
    {"name": "FIFA 23", "estimatedRevenue": 660000000},
    {"name": "EA Sports FC 24", "estimatedRevenue": 700000000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 665000000}
  ],
  "matchedGames": [
    {"name": "FIFA 23", "cliRevenue": 810000000, "sdkRevenue": 660000000, "differencePercent": 18.52, "valueMatched": false},
    {"name": "EA Sports FC 24", "cliRevenue": 770000000, "sdkRevenue": 700000000, "differencePercent": 9.09, "valueMatched": true},
    {"name": "EA Sports FC 25", "cliRevenue": 560000000, "sdkRevenue": 665000000, "differencePercent": 18.75, "valueMatched": false}
  ],
  "missingFromSdk": ["EA Sports FC 26"],
  "extraInSdk": []
}
```
