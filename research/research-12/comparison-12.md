# Comparison Report - Iteration 12

## Summary
- **Similarity Score**: 58.33%
- **Coverage Score**: 66.67%
- **Value Accuracy Score**: 50.00%
- **Converged**: No

## Coverage
- CLI found (ground truth): 3 games
- SDK found: 3 games
- Matched: 2 games

### Missing from SDK
- FIFA 23

### Extra in SDK
- EA Sports FC 26

## Value Discrepancies
| Game | CLI Revenue (Truth) | SDK Revenue | Difference |
|------|-------------------|-------------|------------|
| EA Sports FC 24 | $812,500,000 | $735,000,000 | 9.54% |
| EA Sports FC 25 | $552,500,000 | $455,000,000 | 17.65% |

## Raw Comparison Data
```json
{
  "iteration": 12,
  "similarityScore": 58.33,
  "coverageScore": 66.67,
  "valueAccuracyScore": 50.0,
  "converged": false,
  "cli": {
    "totalGames": 3,
    "games": [
      {"name": "FIFA 23", "estimatedRevenue": 715000000},
      {"name": "EA Sports FC 24", "estimatedRevenue": 812500000},
      {"name": "EA Sports FC 25", "estimatedRevenue": 552500000}
    ]
  },
  "sdk": {
    "totalGames": 3,
    "games": [
      {"name": "EA Sports FC 24", "estimatedRevenue": 735000000},
      {"name": "EA Sports FC 25", "estimatedRevenue": 455000000},
      {"name": "EA Sports FC 26", "estimatedRevenue": 420000000}
    ]
  },
  "matched": [
    {
      "game": "EA Sports FC 24",
      "cliRevenue": 812500000,
      "sdkRevenue": 735000000,
      "percentDifference": 9.54,
      "valueMatched": true
    },
    {
      "game": "EA Sports FC 25",
      "cliRevenue": 552500000,
      "sdkRevenue": 455000000,
      "percentDifference": 17.65,
      "valueMatched": false
    }
  ],
  "missingFromSdk": ["FIFA 23"],
  "extraInSdk": ["EA Sports FC 26"]
}
```
