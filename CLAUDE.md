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
| `/research-claude-code-cli` | Generates CLI research (ground truth). Never modified by the self-evolving process. |
| `/compare-research` | Compares CLI output (truth) vs SDK output. Measures how close SDK is to CLI. |
| `/self-evolving-workflow` | Full orchestrator — generates CLI research, hits SDK API, compares, and **evolves SDK code** if < 90%. |

### Components

- **Ralph Wiggum Loop**: `ralph.sh` spawns fresh `claude -p` each iteration, triggers `/self-evolving-workflow`
- **Research Problem**: `problem-statement/problem-statement.md` — single source of truth for what to research
- **CLI Agent (🔴 Red)**: `.claude/agents/claude-code-cli-games-revenue-researcher.md` — produces ground truth output (never modified)
- **SDK Agent**: `claude-agent-sdk/` — FastAPI Python app using **Claude Agent SDK** (`claude-agent-sdk` package). Runs on Max subscription (no API key needed). Evolves each iteration. Uses the same agent definition as CLI (`code-cli-researcher.md`)
- **Comparator (🔵 Blue)**: `.claude/agents/research-compare.md` — measures SDK closeness to CLI
- **State**: `research/research-workflow-state.yaml` — resumable state machine

### What Evolves

- `claude-agent-sdk/agent.py` — system prompt, search queries, output formatting
- `claude-agent-sdk/main.py` — endpoint logic, error handling
- `research/sdk-evolution-log.md` — documents changes made each iteration

### What NEVER Changes

- `.claude/agents/claude-code-cli-games-revenue-researcher.md` — CLI agent definition (ground truth)
- `problem-statement/problem-statement.md` — research problem definition
- CLI research output files

## Key Directories

```
ralph.sh                                    → Bash loop entry point
prompt.md                                   → Loop prompt (triggers /self-evolving-workflow)
problem-statement/problem-statement.md                          → Research problem definition
.claude/commands/
  research-claude-code-cli.md               → CLI research command (ground truth)
  compare-research.md                       → Comparison command
  self-evolving-workflow.md                 → Full orchestrator (evolves SDK)
.claude/agents/
  claude-code-cli-games-revenue-researcher.md → CLI research agent 🔴 Red (never modified)
  research-compare.md                        → Comparison agent 🔵 Blue
claude-agent-sdk/                           → FastAPI Python app (EVOLVES each iteration)
  main.py                                   → POST /research-claude-agent-sdk
  agent.py                                  → SDK agent (Claude Agent SDK, Max subscription)
research/
  research-{n}/                             → Per-iteration folder
    claude-code-cli/                        → CLI outputs (ground truth)
    claude-agent-sdk/                       → SDK outputs (evolving)
    comparison-{n}.md                       → Comparison report
  research-workflow-state.yaml              → State machine
  research-iterations.yaml                  → Score history
  research-status.json                      → Status for ralph.sh
  sdk-evolution-log.md                      → Log of SDK changes per iteration
user-prompts/user-prompts.md                → All user prompts
plans/                                      → Implementation plans
```

---

## Running

### Option 1: CLI Research Only (Ground Truth)

```bash
claude --dangerously-skip-permissions -p "Execute /research-claude-code-cli" --output-format text
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
2. `/self-evolving-workflow` orchestrates all steps
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
- The research problem is defined in `problem-statement/problem-statement.md` — never hardcode it
- Only Reddit is used for research — no Tavily or other web search tools
