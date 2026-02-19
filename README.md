# Self-Evolving Dual-Agent Research System

The **Claude Code CLI** produces ground-truth research output. The **Claude Agent SDK** (FastAPI Python app) is then autonomously evolved until its output matches the CLI at 90%+ similarity.

**Both agents run on your Claude Max subscription** — no API key costs.

## How It Works

1. A research problem is defined in [`problem-statement/problem-statement.json`](problem-statement/problem-statement.json)
2. The **CLI agent** (Claude Code CLI + Reddit MCP) produces the **ground truth** output
3. The **SDK agent** (FastAPI + Claude Agent SDK) independently produces its output — uses the same agent definition and Reddit MCP as CLI
4. A comparator measures how close the SDK output is to the CLI ground truth
5. If < 90% similarity, the self-evolving process **modifies the SDK code** (`agent.py`, `main.py`) to improve its output
6. If the SDK API **fails**, the process **fixes the code** — no mocking or fallbacks
7. Loop repeats until SDK matches CLI at 90%+ similarity
8. Every step is committed to git

## CLI Research Flow

<p align="center">
  <img src="docs/cli-research-flow.svg" alt="CLI Research Workflow" width="900"/>
</p>

## Self-Evolving Workflow

<p align="center">
  <img src="docs/self-evolving-workflow.svg" alt="Self-Evolving Workflow" width="960"/>
</p>

## Three Commands

| Command | Purpose |
|---------|---------|
| `/research-claude-code-cli` | CLI research only (ground truth) — never modified |
| `/compare-research` | Compare CLI (truth) vs SDK output — scores similarity |
| `/self-evolving-workflow` | Thin orchestrator — delegates to sub-commands, hits SDK API, evolves SDK |

## Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed (with Max subscription)
- Python 3.10+

No API key needed — both sides use your Claude Max subscription.

## Setup

```bash
# 1. Clone the repo
git clone <repo-url> && cd claude-agent-sdk-vs-claude-code-cli

# 2. Install SDK agent dependencies
cd claude-agent-sdk && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && cd ..
```

## Running

### CLI Research Only (Ground Truth)

```bash
claude --dangerously-skip-permissions -p "Execute /research-claude-code-cli" --output-format text
```

### SDK Research Only (Max subscription)

```bash
# Start the server (no API key needed)
cd claude-agent-sdk && source venv/bin/activate && uvicorn main:app --reload --port 8000

# Trigger via curl or Swagger UI (http://localhost:8000/docs)
curl -X POST http://localhost:8000/research-claude-agent-sdk \
  -H "Content-Type: application/json" \
  -d '{"iteration": 1}'
```

### Compare Only

After both agents have produced output:

```bash
claude --dangerously-skip-permissions -p "Execute /compare-research" --output-format text
```

### Full Autonomous Self-Evolving Loop

```bash
# Terminal 1: Start SDK FastAPI app
cd claude-agent-sdk && source venv/bin/activate && uvicorn main:app --reload --port 8000

# Terminal 2: Run the loop (up to 100 iterations)
./ralph.sh 100
```

Each iteration:
1. CLI agent produces ground truth research
2. SDK API is called (if it fails, the workflow fixes the code)
3. Both outputs are compared (CLI = truth)
4. If < 90%: SDK code is evolved to improve output
5. If >= 90%: convergence reached, loop stops

## What Evolves vs What Doesn't

| Evolves (SDK) | Never Changes (CLI) |
|---------------|-------------------|
| `claude-agent-sdk/agent.py` | `.claude/agents/claude-code-cli-games-revenue-researcher.md` |
| `claude-agent-sdk/main.py` | `problem-statement/problem-statement.json` |
| `research/sdk-evolution-log.md` | CLI research output files |

## Tech Stack

| Component | Technology | Auth |
|-----------|-----------|------|
| CLI Agent | Claude Code CLI + Reddit MCP | Max subscription |
| SDK Agent | `claude-agent-sdk` package + FastAPI | Max subscription (via Agent SDK) |
| Comparator | Claude Code subagent | Max subscription |

## Project Structure

```
ralph.sh                          — Bash loop entry point
prompt.md                         — Loop prompt (triggers /self-evolving-workflow)
problem-statement/problem-statement.json                — Research problem definition
.claude/commands/
  research-claude-code-cli.md     — CLI research (ground truth)
  compare-research.md             — Comparison command
  self-evolving-workflow.md       — Thin orchestrator (delegates to sub-commands)
  self-evolving-state.yaml        — Loop state machine
.claude/agents/
  claude-code-cli/claude-code-cli-games-revenue-researcher.md          — CLI agent definition 🔴 Red (never modified)
  research-compare.md             — Comparison agent 🔵 Blue
claude-agent-sdk/
  main.py                         — POST /research-claude-agent-sdk
  agent.py                        — SDK agent (Claude Agent SDK, Max sub)
research/
  research-{n}/                   — Per-iteration outputs
    claude-code-cli/              — CLI outputs (ground truth)
    claude-agent-sdk/             — SDK outputs (evolving)
    comparison-{n}.md             — Comparison report
  sdk-evolution-log.md            — Log of SDK changes
```

## Changing the Research Problem

Edit [`problem-statement/problem-statement.json`](problem-statement/problem-statement.json). Both agents read this file dynamically.
