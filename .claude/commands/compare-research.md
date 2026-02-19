# Compare Research

You are the research comparator. Your ONLY job is to compare the CLI output (ground truth) against the SDK output for a given iteration and write a comparison report. You do NOT generate any research and you do NOT modify any agent code.

**Important:** The CLI output is the **ground truth** (100% correct). The comparison measures how close the SDK output is to matching the CLI output.

---

## STEP 1: DETERMINE ITERATION

1. Read `research/research-workflow-state.yaml` to get the current iteration number
2. Use that iteration number for all file paths below

---

## STEP 2: VERIFY INPUTS EXIST

1. Check that BOTH research files exist:
   - `research/research-{iteration}/claude-code-cli/research-{iteration}.md` (ground truth)
   - `research/research-{iteration}/claude-agent-sdk/research-{iteration}.md` (SDK output)
2. If either file is missing, output `COMPARE_ERROR: Missing input files for iteration {iteration}` and stop

---

## STEP 3: RUN COMPARISON

1. Read `.claude/agents/research-compare.md` for comparison instructions
2. Use the Task tool to spawn a comparator subagent (subagent_type: "general-purpose"):
   - Tell it: "You are the Research Comparator. Compare iteration {iteration} outputs. The CLI output is the ground truth — measure how close the SDK output is to it."
   - Include the **full contents** of research-compare.md instructions
   - Tell it to read:
     - CLI output (ground truth): `research/research-{iteration}/claude-code-cli/research-{iteration}.md`
     - SDK output: `research/research-{iteration}/claude-agent-sdk/research-{iteration}.md`
   - Tell it to write comparison to `research/research-{iteration}/comparison-{iteration}.md`
3. Wait for completion
4. Verify `research/research-{iteration}/comparison-{iteration}.md` exists

---

## STEP 4: COMMIT COMPARISON

1. Stage the comparison file:
   ```
   git add research/research-{iteration}/comparison-{iteration}.md
   ```
2. Commit with message:
   ```
   comparison({iteration}): comparison report generated
   ```

---

## STEP 5: REPORT

1. Read `research/research-{iteration}/comparison-{iteration}.md` and parse the similarity score from the JSON block
2. Output: `COMPARISON_COMPLETE iteration={iteration} similarity={score}%`

---

## Critical Rules

- CLI output is the **ground truth** — never suggest changes to it
- Do NOT generate any research — only compare existing outputs
- Do NOT trigger the CLI or SDK agents
- Do NOT modify agent files, SDK code, or evolution hints — that is handled by self-evolving-workflow
- If either input file is missing, report the error and stop
- Always include the full ComparisonResult JSON in the comparison report
