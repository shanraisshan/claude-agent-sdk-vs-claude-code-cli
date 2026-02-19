# Comparison Report - Iteration 8

## Summary
- **Similarity Score**: 100%
- **Coverage Score**: 100%
- **Value Accuracy Score**: 100%
- **Converged**: yes

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
| FIFA 23 | $810,000,000 | $780,000,000 | 3.70% |
| EA Sports FC 24 | $770,000,000 | $770,000,000 | 0.00% |
| EA Sports FC 25 | $560,000,000 | $560,000,000 | 0.00% |
| EA Sports FC 26 | $665,000,000 | $630,000,000 | 5.26% |

## Raw Comparison Data
```json
{
  "iteration": 8,
  "similarityScore": 100,
  "coverageScore": 100,
  "valueAccuracyScore": 100,
  "converged": true,
  "cliGamesCount": 4,
  "sdkGamesCount": 4,
  "matchedGamesCount": 4,
  "missingFromSdk": [],
  "extraInSdk": [],
  "valueComparisons": [
    {
      "game": "FIFA 23",
      "cliRevenue": 810000000,
      "sdkRevenue": 780000000,
      "percentDifference": 3.70,
      "withinThreshold": true
    },
    {
      "game": "EA Sports FC 24",
      "cliRevenue": 770000000,
      "sdkRevenue": 770000000,
      "percentDifference": 0.00,
      "withinThreshold": true
    },
    {
      "game": "EA Sports FC 25",
      "cliRevenue": 560000000,
      "sdkRevenue": 560000000,
      "percentDifference": 0.00,
      "withinThreshold": true
    },
    {
      "game": "EA Sports FC 26",
      "cliRevenue": 665000000,
      "sdkRevenue": 630000000,
      "percentDifference": 5.26,
      "withinThreshold": true
    }
  ]
}
```
