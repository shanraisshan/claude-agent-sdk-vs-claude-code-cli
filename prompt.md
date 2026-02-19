# Self-Evolving Loop Prompt

Execute `/self-evolving-workflow` to run one complete iteration.

This orchestrates the full autonomous workflow:
1. Generates CLI research (ground truth) via `/research-claude-code-cli`
2. Triggers SDK research via HTTP (localhost:8000/research-claude-agent-sdk)
3. If SDK fails, fixes the FastAPI code and retries
4. Compares both outputs via `/compare-research` (CLI = ground truth)
5. If < 90% similarity, evolves the SDK code to improve its output
6. Commits all results to git

## Exit Conditions

- `<promise>COMPLETE</promise>` - SDK output matches CLI at 90%+ similarity
- `CONTINUING_RESEARCH` - SDK needs more evolution (similarity < 90%)
