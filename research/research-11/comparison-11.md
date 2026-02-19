# Comparison Report - Iteration 11

## Summary
- **Similarity Score**: 83.33%
- **Coverage Score**: 100%
- **Value Accuracy Score**: 66.67%
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
| EA Sports FC 24 | $770,000,000 | $812,500,000 | 5.52% |
| EA Sports FC 25 | $525,000,000 | $617,500,000 | 17.62% |
| EA Sports FC 26 | $490,000,000 | $525,000,000 | 7.14% |

## Raw Comparison Data
```json
{
  "iteration": 11,
  "similarityScore": 83.33,
  "coverageScore": 100,
  "valueAccuracyScore": 66.67,
  "converged": false,
  "cliGames": [
    {"name": "EA Sports FC 24", "estimatedRevenue": 770000000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 525000000},
    {"name": "EA Sports FC 26", "estimatedRevenue": 490000000}
  ],
  "sdkGames": [
    {"name": "FIFA 23", "estimatedRevenue": 715000000},
    {"name": "EA Sports FC 24", "estimatedRevenue": 812500000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 617500000},
    {"name": "EA Sports FC 26", "estimatedRevenue": 525000000}
  ],
  "matched": [
    {"name": "EA Sports FC 24", "cliRevenue": 770000000, "sdkRevenue": 812500000, "differencePercent": 5.52, "valueMatched": true},
    {"name": "EA Sports FC 25", "cliRevenue": 525000000, "sdkRevenue": 617500000, "differencePercent": 17.62, "valueMatched": false},
    {"name": "EA Sports FC 26", "cliRevenue": 490000000, "sdkRevenue": 525000000, "differencePercent": 7.14, "valueMatched": true}
  ],
  "missingFromSdk": [],
  "extraInSdk": ["FIFA 23"]
}
```
