# CLAUDE.md

## Project: Self-Evolving Dual-Agent FIFA Research System

This project compares **Claude Code CLI** vs **Claude Agent SDK** by having both independently research FIFA/EA FC game releases and revenue data, then autonomously iterating until outputs converge to 90%+ similarity. Uses the **Ralph Wiggum Bash Loop** pattern for fully autonomous operation.

---

## Prompt Logging Rule

**Whenever the user provides a new prompt or instruction, append it to `prompt/prompts.md`** with an incremented heading number. Format:

```
# {next_number}
{user's prompt text}
```

Always check the last heading number in `prompt/prompts.md` and increment by 1.

---

## Architecture

- **Ralph Wiggum Loop**: `ralph.sh` spawns fresh `claude -p` each iteration, checks for `<promise>COMPLETE</promise>`
- **Workflow**: `/execute-workflow` slash command — 7-phase state machine (generate CLI → generate SDK → compare → evaluate → update agents → commit → report)
- **CLI Agent**: `.claude/agents/opus-cli-researcher.md` — evolving agent using Tavily + Reddit MCP
- **SDK Agent**: Next.js app (`claude-agent-sdk/`) with `@anthropic-ai/sdk` tool_use
- **Comparator**: `.claude/agents/opus-comparator.md` — fuzzy matching + revenue comparison
- **State**: `research/research-workflow-state.yaml` — resumable state machine

## Key Directories

```
ralph.sh                          → Bash loop entry point
prompt.md                         → Loop prompt (triggers /execute-workflow)
.claude/commands/execute-workflow.md → State machine orchestrator
.claude/agents/                   → Evolving agent definitions
claude-code-cli/                  → CLI agent output files
claude-agent-sdk/                 → Next.js app + SDK agent output files
research/                         → State files, comparison reports, iteration history
shared/                           → Types, constants
prompt/prompts.md                 → All user prompts (append new ones here)
plans/                            → Implementation plans
```

## Running

```bash
# Terminal 1: Start SDK app
cd claude-agent-sdk && npm run dev

# Terminal 2: Run autonomous loop
./ralph.sh 100
```

## Self-Evolving Loop

1. `ralph.sh` spawns fresh Claude instance each iteration (no context pollution)
2. `/execute-workflow` runs all 7 phases autonomously
3. CLI agent uses MCP tools, SDK agent uses HTTP tool_use — both produce standardized JSON
4. Comparator scores similarity (50% game coverage + 50% revenue accuracy)
5. If < 90%: agent files updated with discrepancy findings, loop continues
6. If ≥ 90%: outputs `<promise>COMPLETE</promise>`, ralph.sh stops
7. Every iteration auto-committed to git for permanent record

## Output Format

Both agents must produce markdown with embedded JSON following `shared/types.ts` schema:
- `games[]` with name, year, platform, publisher, estimatedRevenue, revenueSource, confidence
- `totalGamesFound`, `searchQueries`, `sources`

## Rules

- Never modify the research goal (FIFA/EA FC games + revenue from 1990s to FC 26)
- Always write outputs to the correct directory with iteration numbering
- Keep standardized JSON output format consistent between both agents
- Agent files evolve by appending findings — never delete prior learnings
- Every iteration must be git committed before reporting
