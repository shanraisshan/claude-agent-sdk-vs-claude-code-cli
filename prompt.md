# Ralph Loop Prompt

Execute `/execute-workflow` to run one complete research iteration.

The workflow handles everything autonomously:
- Generates FIFA/EA FC game research via CLI agent (MCP tools)
- Triggers SDK agent research via HTTP (localhost:3000)
- Compares both outputs using the comparator agent
- Evaluates similarity score against 90% threshold
- Updates agent prompts with discrepancy findings
- Commits all results to git
- Reports status

## Exit Conditions

The workflow will output one of:

- `<promise>COMPLETE</promise>` - Both agents converged (similarity >= 90%)
- `CONTINUING_RESEARCH` - Need more iterations (similarity < 90%)
