# Comparison Report - Iteration 7

## Summary
- **Similarity Score**: 62.5%
- **Coverage Score**: 100%
- **Value Accuracy Score**: 25%
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
| FIFA 23 | $810,000,000 | $810,000,000 | 0.00% |
| EA Sports FC 24 | $770,000,000 | $875,000,000 | 13.64% |
| EA Sports FC 25 | $560,000,000 | $665,000,000 | 18.75% |
| EA Sports FC 26 | $665,000,000 | $490,000,000 | 26.32% |

## Raw Comparison Data
```json
{
  "iteration": 7,
  "similarityScore": 62.5,
  "coverageScore": 100,
  "valueAccuracyScore": 25,
  "converged": false,
  "cliGames": [
    {"name": "FIFA 23", "estimatedRevenue": 810000000},
    {"name": "EA Sports FC 24", "estimatedRevenue": 770000000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 560000000},
    {"name": "EA Sports FC 26", "estimatedRevenue": 665000000}
  ],
  "sdkGames": [
    {"name": "FIFA 23", "estimatedRevenue": 810000000},
    {"name": "EA Sports FC 24", "estimatedRevenue": 875000000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 665000000},
    {"name": "EA Sports FC 26", "estimatedRevenue": 490000000}
  ],
  "matchedGames": [
    {"name": "FIFA 23", "cliRevenue": 810000000, "sdkRevenue": 810000000, "percentDiff": 0.0, "valueMatch": true},
    {"name": "EA Sports FC 24", "cliRevenue": 770000000, "sdkRevenue": 875000000, "percentDiff": 13.64, "valueMatch": false},
    {"name": "EA Sports FC 25", "cliRevenue": 560000000, "sdkRevenue": 665000000, "percentDiff": 18.75, "valueMatch": false},
    {"name": "EA Sports FC 26", "cliRevenue": 665000000, "sdkRevenue": 490000000, "percentDiff": 26.32, "valueMatch": false}
  ],
  "missingFromSdk": [],
  "extraInSdk": []
}
```
