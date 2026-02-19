# Comparison Report - Iteration 2

## Summary
- **Similarity Score**: 62.5%
- **Coverage Score**: 100%
- **Value Accuracy Score**: 25%
- **Converged**: no

## Coverage
- CLI found (ground truth): 4 games
- SDK found: 5 games
- Matched: 4 games

### Missing from SDK
- (none)

### Extra in SDK
- EA Sports FC Mobile

## Value Discrepancies
| Game | CLI Revenue (Truth) | SDK Revenue | Difference |
|------|-------------------|-------------|------------|
| FIFA 23 | $630,000,000 | $660,000,000 | 4.76% |
| EA Sports FC 24 | $665,000,000 | $812,500,000 | 22.18% |
| EA Sports FC 25 | $490,000,000 | $617,500,000 | 26.02% |
| EA Sports FC 26 | $455,000,000 | $630,000,000 | 38.46% |

## Raw Comparison Data
```json
{
  "iteration": 2,
  "similarityScore": 62.5,
  "coverageScore": 100,
  "valueAccuracyScore": 25,
  "converged": false,
  "cliGames": [
    {"name": "FIFA 23", "estimatedRevenue": 630000000},
    {"name": "EA Sports FC 24", "estimatedRevenue": 665000000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 490000000},
    {"name": "EA Sports FC 26", "estimatedRevenue": 455000000}
  ],
  "sdkGames": [
    {"name": "FIFA 23", "estimatedRevenue": 660000000},
    {"name": "EA Sports FC 24", "estimatedRevenue": 812500000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 617500000},
    {"name": "EA Sports FC 26", "estimatedRevenue": 630000000},
    {"name": "EA Sports FC Mobile", "estimatedRevenue": 0}
  ],
  "matchedGames": [
    {"name": "FIFA 23", "cliRevenue": 630000000, "sdkRevenue": 660000000, "differencePercent": 4.76, "valueMatched": true},
    {"name": "EA Sports FC 24", "cliRevenue": 665000000, "sdkRevenue": 812500000, "differencePercent": 22.18, "valueMatched": false},
    {"name": "EA Sports FC 25", "cliRevenue": 490000000, "sdkRevenue": 617500000, "differencePercent": 26.02, "valueMatched": false},
    {"name": "EA Sports FC 26", "cliRevenue": 455000000, "sdkRevenue": 630000000, "differencePercent": 38.46, "valueMatched": false}
  ],
  "missingFromSdk": [],
  "extraInSdk": ["EA Sports FC Mobile"]
}
```
