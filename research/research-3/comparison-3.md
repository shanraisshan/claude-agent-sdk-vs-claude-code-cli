# Comparison Report - Iteration 3

## Summary
- **Similarity Score**: 83.33%
- **Coverage Score**: 100%
- **Value Accuracy Score**: 66.67%
- **Converged**: no

## Coverage
- CLI found (ground truth): 3 games
- SDK found: 3 games
- Matched: 3 games

### Missing from SDK
- (none)

### Extra in SDK
- (none)

## Value Discrepancies
| Game | CLI Revenue (Truth) | SDK Revenue | Difference |
|------|-------------------|-------------|------------|
| EA Sports FC 24 | $735,000,000 | $693,000,000 | 5.71% |
| EA Sports FC 25 | $420,000,000 | $441,000,000 | 5.00% |
| EA Sports FC 26 | $455,000,000 | $335,000,000 | 26.37% |

## Raw Comparison Data
```json
{
  "iteration": 3,
  "similarityScore": 83.33,
  "coverageScore": 100,
  "valueAccuracyScore": 66.67,
  "converged": false,
  "cliGames": [
    {"name": "EA Sports FC 24", "estimatedRevenue": 735000000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 420000000},
    {"name": "EA Sports FC 26", "estimatedRevenue": 455000000}
  ],
  "sdkGames": [
    {"name": "EA Sports FC 24", "estimatedRevenue": 693000000},
    {"name": "EA Sports FC 25", "estimatedRevenue": 441000000},
    {"name": "EA Sports FC 26", "estimatedRevenue": 335000000}
  ],
  "matchedGames": [
    {
      "name": "EA Sports FC 24",
      "cliRevenue": 735000000,
      "sdkRevenue": 693000000,
      "percentDifference": 5.71,
      "valueMatched": true
    },
    {
      "name": "EA Sports FC 25",
      "cliRevenue": 420000000,
      "sdkRevenue": 441000000,
      "percentDifference": 5.0,
      "valueMatched": true
    },
    {
      "name": "EA Sports FC 26",
      "cliRevenue": 455000000,
      "sdkRevenue": 335000000,
      "percentDifference": 26.37,
      "valueMatched": false
    }
  ],
  "missingFromSdk": [],
  "extraInSdk": []
}
```
