# Comparison Report - Iteration 5

## Summary
- **Similarity Score**: 37.5%
- **Coverage Score**: 75%
- **Value Accuracy Score**: 0%
- **Converged**: no

## Coverage
- CLI found (ground truth): 4 games
- SDK found: 3 games
- Matched: 3 games

### Missing from SDK
- FIFA 23

### Extra in SDK
- (none)

## Value Discrepancies
| Game | CLI Revenue (Truth) | SDK Revenue | Difference |
|------|-------------------|-------------|------------|
| EA Sports FC 24 | $770,000,000 | $651,000,000 | 15.45% |
| EA Sports FC 25 | $560,000,000 | $434,000,000 | 22.50% |
| EA Sports FC 26 | $665,000,000 | $525,000,000 | 21.05% |

## Raw Comparison Data
```json
{
  "iteration": 5,
  "similarityScore": 37.5,
  "coverageScore": 75,
  "valueAccuracyScore": 0,
  "converged": false,
  "cliGamesCount": 4,
  "sdkGamesCount": 3,
  "matchedGamesCount": 3,
  "valueMatchedGamesCount": 0,
  "missingFromSdk": ["FIFA 23"],
  "extraInSdk": [],
  "gameComparisons": [
    {
      "game": "EA Sports FC 24",
      "cliRevenue": 770000000,
      "sdkRevenue": 651000000,
      "percentDifference": 15.45,
      "valueMatched": false
    },
    {
      "game": "EA Sports FC 25",
      "cliRevenue": 560000000,
      "sdkRevenue": 434000000,
      "percentDifference": 22.5,
      "valueMatched": false
    },
    {
      "game": "EA Sports FC 26",
      "cliRevenue": 665000000,
      "sdkRevenue": 525000000,
      "percentDifference": 21.05,
      "valueMatched": false
    }
  ]
}
```
