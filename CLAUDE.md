# CLAUDE.md

## Project: Self-Evolving Dual-Agent Research System

The **Claude Code CLI** produces ground-truth research output. The **Claude Agent SDK** (FastAPI Python app) is then autonomously evolved until its output matches the CLI at 90%+ similarity. Uses the **Ralph Wiggum Bash Loop** for fully autonomous operation.

**Key principle:** CLI output is always 100% correct. The self-evolving process only modifies the SDK code (`claude-agent-sdk/agent.py`, `claude-agent-sdk/main.py`) — never the CLI agent.

---

## Prompt Logging Rule

**Whenever the user provides a new prompt or instruction, append it to `user-prompts/user-prompts.md`** with an incremented heading number. Format:

```
# {next_number}
{user's prompt text}
```

Always check the last heading number in `user-prompts/user-prompts.md` and increment by 1.

---

## Architecture

### Three Commands

| Command | Purpose |
|---------|---------|
| `/workflow-research-cli` | Reads problem, spawns Reddit research agent for raw data, synthesizes final report |
| `/compare-research` | Compares CLI output (truth) vs SDK output. Measures how close SDK is to CLI. |
| `/workflow-self-evolving-loop` | Thin orchestrator — delegates to `/workflow-research-cli` and `/compare-research`, hits SDK API, and evolves SDK code if < 90%. |

### Components

- **Ralph Wiggum Loop**: `ralph.sh` spawns fresh `claude -p` each iteration, triggers `/workflow-self-evolving-loop`
- **Research Problem**: `problem-statement/problem-statement.json` — single source of truth for what to research
- **Reddit Research Agent (🔴 Red)**: `.claude/agents/reddit-game-research-agent.md` — searches Reddit for game lists and copy sales data, writes raw data to `reddit-data-{n}.md` (never modified)
- **SDK Agent**: `claude-agent-sdk/` — FastAPI Python app using **Claude Agent SDK** (`claude-agent-sdk` package). Runs on Max subscription (no API key needed). Evolves each iteration.
- **Comparator**: `/compare-research` command — measures SDK closeness to CLI (scoring logic inline, no separate agent)
- **State**: `research/self-evolving-state.yaml` — resumable state machine

### What Evolves

- `claude-agent-sdk/agent.py` — system prompt, search queries, output formatting
- `claude-agent-sdk/main.py` — endpoint logic, error handling
- `research/sdk-evolution-log.md` — documents changes made each iteration

### What NEVER Changes

- `.claude/agents/reddit-game-research-agent.md` — CLI agent definition (ground truth)
- `problem-statement/problem-statement.json` — research problem definition
- CLI research output files

## Key Directories

```
ralph.sh                                    → Bash loop entry point
prompt.md                                   → Loop prompt (triggers /workflow-self-evolving-loop)
problem-statement/
  problem-statement.json                    → Research problem definition
.claude/commands/
  workflow-research-cli.md               → CLI research orchestrator (reads problem, spawns agent, synthesizes report)
  compare-research.md                       → Comparison command
  workflow-self-evolving-loop.md                 → Thin orchestrator (delegates to sub-commands, evolves SDK)
.claude/agents/
  reddit-game-research-agent.md → Reddit research agent 🔴 Red (never modified)
claude-agent-sdk/                           → FastAPI Python app (EVOLVES each iteration)
  main.py                                   → POST /research-claude-agent-sdk
  agent.py                                  → SDK agent (Claude Agent SDK, Max subscription)
research/
  self-evolving-state.yaml                  → State machine
  research-iterations.yaml                  → Score history
  research-status.json                      → Status for ralph.sh
  sdk-evolution-log.md                      → Log of SDK changes per iteration
  research-{n}/                             → Per-iteration folder
    claude-code-cli/                        → CLI outputs (ground truth)
    claude-agent-sdk/                       → SDK outputs (evolving)
    comparison-{n}.md                       → Comparison report
user-prompts/user-prompts.md                → All user prompts
plans/                                      → Implementation plans
```

---

## Running

### Option 1: CLI Research Only (Ground Truth)

```bash
claude --dangerously-skip-permissions -p "Execute /workflow-research-cli" --output-format text
```

### Option 2: SDK Research Only (uses Max subscription)

```bash
# Start server (no API key needed — uses Max subscription via Agent SDK)
cd claude-agent-sdk && source venv/bin/activate && uvicorn main:app --reload --port 8000

# Trigger research
curl -X POST http://localhost:8000/research-claude-agent-sdk \
  -H "Content-Type: application/json" \
  -d '{"iteration": 1}'
```

### Option 3: Compare Only

After both agents have produced output:

```bash
claude --dangerously-skip-permissions -p "Execute /compare-research" --output-format text
```

### Option 4: Full Autonomous Self-Evolving Loop

```bash
# Terminal 1: Start SDK FastAPI app
cd claude-agent-sdk && source venv/bin/activate && uvicorn main:app --reload --port 8000

# Terminal 2: Run autonomous loop
./ralph.sh 100
```

Each iteration: CLI research (truth) → SDK research → compare → evolve SDK code if < 90% → repeat.

---

## Self-Evolving Loop

1. `ralph.sh` spawns fresh Claude instance each iteration
2. `/workflow-self-evolving-loop` orchestrates all steps
3. CLI agent produces ground truth using Reddit MCP
4. SDK API is called — if it **fails**, the workflow **fixes the code** (no fallbacks/mocks)
5. Comparator measures how close SDK is to CLI
6. If < 90%: SDK code (`agent.py`, `main.py`) is modified to improve output
7. If >= 90%: outputs `<promise>COMPLETE</promise>`, loop stops
8. Every step is individually committed to git

## Rules

- CLI output is **ground truth** — never modify CLI agent files
- SDK code evolves — `agent.py` and `main.py` are modified each iteration
- If SDK API fails, **fix the code** — never use fallback subagents
- The research problem is defined in `problem-statement/problem-statement.json` — never hardcode it
- Only Reddit is used for research — no Tavily or other web search tools
