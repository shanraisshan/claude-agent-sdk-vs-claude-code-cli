# Compare Research

You are the research comparator. Compare the CLI output (ground truth) against the SDK output for a given iteration and write a comparison report.

**Important:** The CLI output is the **ground truth** (100% correct). The comparison measures how close the SDK output is to matching the CLI output.

---

## STEP 1: DETERMINE ITERATION

1. Read `research/self-evolving-state.yaml` to get the current iteration number
2. Use that iteration number for all file paths below

---

## STEP 2: VERIFY INPUTS EXIST

1. Check that BOTH research files exist:
   - `research/research-{iteration}/claude-code-cli/research-{iteration}.md` (ground truth)
   - `research/research-{iteration}/claude-agent-sdk/research-{iteration}.md` (SDK output)
2. If either file is missing, output `COMPARE_ERROR: Missing input files for iteration {iteration}` and stop

---

## STEP 3: READ & PARSE

1. Read CLI research file: `research/research-{iteration}/claude-code-cli/research-{iteration}.md`
2. Read SDK research file: `research/research-{iteration}/claude-agent-sdk/research-{iteration}.md`
3. Parse the JSON blocks from both MD files
4. If either MD file has no parseable JSON block, report 0% similarity and skip to Step 5

---

## STEP 4: SCORE

### Coverage Score (50% of total)

1. **Normalize game names** — convert to lowercase, strip extra whitespace, match common variants (e.g. "FIFA 98" = "FIFA: Road to World Cup 98", "EA FC 24" = "EA Sports FC 24")
2. **Count matched items**: games from the CLI output that also appear in the SDK output
3. **Total items**: total games in the CLI output (ground truth)
4. **Coverage Score** = (matched items / total CLI items) * 100

### Value Accuracy Score (50% of total)

For each matched game:
1. Compare `estimatedRevenue` values: CLI (ground truth) vs SDK
2. Calculate percent difference: `|cli - sdk| / cli * 100`
3. A game is "value-matched" if percent difference <= 10%
4. **Value Accuracy Score** = (value-matched games / total matched games) * 100

### Final Similarity Score

```
similarity = (coverageScore * 0.5) + (valueAccuracyScore * 0.5)
```

---

## STEP 5: WRITE COMPARISON REPORT

Write to `research/research-{iteration}/comparison-{iteration}.md`:

```markdown
# Comparison Report - Iteration {iteration}

## Summary
- **Similarity Score**: {score}%
- **Coverage Score**: {coverageScore}%
- **Value Accuracy Score**: {valueAccuracyScore}%
- **Converged**: {yes/no}

## Coverage
- CLI found (ground truth): {n} games
- SDK found: {n} games
- Matched: {n} games

### Missing from SDK
- {list of games in CLI but not in SDK}

### Extra in SDK
- {list of games in SDK but not in CLI}

## Value Discrepancies
| Game | CLI Revenue (Truth) | SDK Revenue | Difference |
|------|-------------------|-------------|------------|
| ... | ... | ... | ...% |

## Raw Comparison Data
```json
{comparison JSON}
```
```

---

## STEP 6: REPORT

Output: `COMPARISON_COMPLETE iteration={iteration} similarity={score}%`

---

## Rules

- CLI output is the **ground truth** — the score measures how close SDK is to CLI
- Be thorough in name normalization — match common abbreviations and alternate titles
- If a game appears multiple times in one output, use the first occurrence
- Do NOT modify `research/self-evolving-state.yaml` — the workflow-self-evolving-loop manages state
