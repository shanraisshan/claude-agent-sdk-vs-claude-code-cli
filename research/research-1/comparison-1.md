# Comparison Report - Iteration 1

## Summary
- **Similarity Score**: 83.3%
- **Coverage Score**: 100.0%
- **Value Accuracy Score**: 66.7%
- **Converged**: No

## Coverage
- CLI found (ground truth): 3 games
- SDK found: 5 games
- Matched: 3 games

### Missing from SDK
- (none — all CLI games were found in SDK)

### Extra in SDK
- EA Sports FC Mobile (F2P, $0 revenue — excluded by CLI)
- EA Sports FC Online (F2P, $0 revenue — excluded by CLI)

## Value Discrepancies
| Game | CLI Revenue (Truth) | SDK Revenue | Difference |
|------|-------------------|-------------|------------|
| EA Sports FC 24 | $840,000,000 | $910,000,000 | 8.3% |
| EA Sports FC 25 | $600,000,000 | $600,000,000 | 0.0% |
| EA Sports FC 26 | $600,000,000 | $440,000,000 | 26.7% |

### Analysis

- **FC 24**: SDK used $65 avg price vs CLI's $60, inflating revenue by ~$70M. Within 10% threshold.
- **FC 25**: Perfect match. Both estimated 10M copies at $60.
- **FC 26**: Major discrepancy. SDK estimated only 8M copies at $55 avg price ($440M), while CLI estimated 10M copies at $60 ($600M). SDK was more pessimistic about FC 26's performance, citing UK physical sales losses and early discounting. CLI weighted the Black Friday #1 position more heavily. This 26.7% gap is the primary driver of the below-90% score.

## Raw Comparison Data
```json
{
  "iteration": 1,
  "similarityScore": 83.3,
  "coverageScore": 100.0,
  "valueAccuracyScore": 66.7,
  "converged": false,
  "cliGames": 3,
  "sdkGames": 5,
  "matchedGames": 3,
  "missingFromSdk": [],
  "extraInSdk": ["EA Sports FC Mobile", "EA Sports FC Online"],
  "valueComparisons": [
    {
      "game": "EA Sports FC 24",
      "cliRevenue": 840000000,
      "sdkRevenue": 910000000,
      "percentDifference": 8.3,
      "withinThreshold": true
    },
    {
      "game": "EA Sports FC 25",
      "cliRevenue": 600000000,
      "sdkRevenue": 600000000,
      "percentDifference": 0.0,
      "withinThreshold": true
    },
    {
      "game": "EA Sports FC 26",
      "cliRevenue": 600000000,
      "sdkRevenue": 440000000,
      "percentDifference": 26.7,
      "withinThreshold": false
    }
  ]
}
```
