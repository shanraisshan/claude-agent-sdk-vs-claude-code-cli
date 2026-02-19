# Comparison Report - Iteration 13

## Summary
- **Similarity Score**: 33.33%
- **Coverage Score**: 66.67%
- **Value Accuracy Score**: 0%
- **Converged**: no

## Coverage
- CLI found (ground truth): 3 games
- SDK found: 2 games
- Matched: 2 games

### Missing from SDK
- EA Sports FC 26

### Extra in SDK
- (none)

## Value Discrepancies
| Game | CLI Revenue (Truth) | SDK Revenue | Difference |
|------|-------------------|-------------|------------|
| EA Sports FC 24 | $812,500,000 | $1,399,800,000 | 72.28% |
| EA Sports FC 25 | $552,500,000 | $1,819,740,000 | 229.32% |

## Raw Comparison Data
```json
{
  "iteration": 13,
  "similarityScore": 33.33,
  "coverageScore": 66.67,
  "valueAccuracyScore": 0,
  "converged": false,
  "cliGames": [
    {"name": "EA Sports FC 24", "estimatedRevenue": 812500000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 552500000},
    {"name": "EA Sports FC 26", "estimatedRevenue": 454500000}
  ],
  "sdkGames": [
    {"name": "EA Sports FC 24", "estimatedRevenue": 1399800000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 1819740000}
  ],
  "matched": [
    {
      "game": "EA Sports FC 24",
      "cliRevenue": 812500000,
      "sdkRevenue": 1399800000,
      "percentDifference": 72.28,
      "valueMatched": false
    },
    {
      "game": "EA Sports FC 25",
      "cliRevenue": 552500000,
      "sdkRevenue": 1819740000,
      "percentDifference": 229.32,
      "valueMatched": false
    }
  ],
  "missingFromSdk": ["EA Sports FC 26"],
  "extraInSdk": []
}
```
