# Plan 1 - Initial Requirements (Updated: Ralph Wiggum Autonomous Loop)

## Context

This project demonstrates Course 9 (Self-Evolving Agentic Loops) principles by having **two AI agents** (Claude Code CLI and Claude Agent SDK) independently research FIFA/EA FC game releases and revenue, then **autonomously compare and refine** outputs until they converge to 90%+ similarity. The system uses the **Ralph Wiggum Bash Loop** pattern for fully autonomous operation — no human in the loop.

**Reference implementation**: `/Users/shayanraees/Documents/Github/novel-llm-26`

---

## Architecture Overview

```
ralph.sh (bash loop, N iterations)
  │
  └→ claude -p "$(cat prompt.md)" --output-format text
       │
       └→ /execute-workflow (slash command)
            │
            ├→ PHASE 1: GENERATE CLI RESEARCH
            │    └→ Spawn subagent: opus-cli-researcher
            │         Uses MCP: Tavily + Reddit
            │         Writes: claude-code-cli/research-{n}-output.md
            │
            ├→ PHASE 2: GENERATE SDK RESEARCH
            │    └→ HTTP POST to Next.js app (localhost:3000)
            │         Uses: @anthropic-ai/sdk tool_use
            │         Writes: claude-agent-sdk/research-{n}-output.md
            │
            ├→ PHASE 3: COMPARE
            │    └→ Spawn subagent: opus-comparator
            │         Reads both output files
            │         Fuzzy game name matching + revenue comparison
            │         Writes: research/comparison-{n}.md
            │
            ├→ PHASE 4: EVALUATE
            │    └→ Score ≥ 90%? → COMPLETE
            │       Score < 90%? → CONTINUING, evolve prompts
            │
            ├→ PHASE 5: UPDATE AGENTS
            │    └→ Append discrepancy findings to agent files
            │         .claude/agents/opus-cli-researcher.md
            │         Update SDK prompt evolution hints
            │
            ├→ PHASE 6: COMMIT
            │    └→ git add + commit + push
            │         "research({n}): {status} similarity={score}%"
            │
            └→ PHASE 7: REPORT
                 └→ Output <promise>COMPLETE</promise>
                    OR CONTINUING_RESEARCH
```

---

## File Structure

```
/
├── ralph.sh                              # Bash loop (spawns fresh claude -p each iteration)
├── prompt.md                             # Loop prompt (tells claude to run /execute-workflow)
├── CLAUDE.md                             # Project instructions for Claude Code
├── .mcp.json                             # Tavily + Reddit MCP servers (user provides)
├── .env                                  # API keys (gitignored)
├── .gitignore
├── .claude/
│   ├── commands/
│   │   └── execute-workflow.md           # Main orchestrator slash command (state machine)
│   ├── agents/
│   │   ├── opus-cli-researcher.md        # Evolving CLI research agent (uses MCP tools)
│   │   └── opus-comparator.md            # Comparison/evaluation agent
│   ├── settings.json                     # (existing)
│   └── hooks/                            # (existing)
├── claude-code-cli/                      # CLI agent outputs
│   └── research-{n}-output.md
├── claude-agent-sdk/                     # Next.js app + SDK agent outputs
│   ├── app/
│   │   ├── page.tsx                      # "Execute Research" button UI
│   │   └── api/research/route.ts         # API route handler
│   ├── lib/
│   │   └── agent.ts                      # Agent SDK agentic loop with tool_use
│   ├── package.json
│   └── research-{n}-output.md            # SDK agent outputs
├── research/                             # State & comparison tracking
│   ├── research-workflow-state.yaml      # State machine (phase, iteration, status)
│   ├── research-iterations.yaml          # All iterations with scores
│   ├── research-status.json              # Simple status for ralph.sh
│   └── comparison-{n}.md                 # Per-iteration comparison reports
├── shared/
│   ├── types.ts                          # GameEntry, ResearchOutput, ComparisonResult
│   └── constants.ts                      # Game name aliases, thresholds
├── prompt/
│   └── prompts.md                        # All user prompts (append new ones here)
└── plans/
    └── plan-1-initial-requirements.md    # This file
```

---

## Implementation Phases

### Phase 1: Foundation
1. Create `.gitignore` (node_modules, .env, orchestrator/state.json)
2. Create `.env` with placeholder API keys
3. Create `shared/types.ts` — `GameEntry`, `ResearchOutput`, `ComparisonResult` interfaces
4. Create `shared/constants.ts` — game name alias map, similarity threshold (90%), max iterations
5. Create `research/` directory with initial state files
6. **User provides `.mcp.json`** with Tavily + Reddit MCP server configs

### Phase 2: Ralph Wiggum Bash Loop
7. Create `ralph.sh` — bash loop that calls `claude -p "$(cat prompt.md)" --output-format text`, checks for `<promise>COMPLETE</promise>`
8. Create `prompt.md` — tells Claude to run `/execute-workflow`

### Phase 3: Execute Workflow Slash Command
9. Create `.claude/commands/execute-workflow.md` — state machine with 7 phases:
   - GENERATE_CLI → GENERATE_SDK → COMPARE → EVALUATE → UPDATE_AGENTS → COMMIT → REPORT
   - Reads/writes `research/research-workflow-state.yaml` for resumability
   - Outputs promise tag in REPORT phase

### Phase 4: CLI Research Agent
10. Create `.claude/agents/opus-cli-researcher.md` — evolving research agent that uses Tavily + Reddit MCP to find FIFA game data
11. The execute-workflow spawns this agent via Task tool during GENERATE_CLI phase
12. Agent writes standardized JSON output to `claude-code-cli/research-{n}-output.md`

### Phase 5: Claude Agent SDK Next.js App
13. Initialize Next.js app in `claude-agent-sdk/` with `npx create-next-app`
14. Create `claude-agent-sdk/lib/agent.ts` — agentic loop using `@anthropic-ai/sdk` with `tool_use` for Tavily (HTTP) and Reddit (JSON API)
15. Create `claude-agent-sdk/app/api/research/route.ts` — API route handler (POST), accepts iteration + evolution hints
16. Create `claude-agent-sdk/app/page.tsx` — "Execute Research" button, iteration display, output viewer
17. The execute-workflow triggers SDK agent via `fetch("http://localhost:3000/api/research")` during GENERATE_SDK phase

### Phase 6: Comparator Agent
18. Create `.claude/agents/opus-comparator.md` — reads both outputs, performs fuzzy game name matching (via alias normalization) + revenue comparison (10% tolerance), calculates similarity score
19. Scoring: 50% game coverage + 50% revenue accuracy
20. Writes comparison report to `research/comparison-{n}.md`

### Phase 7: Self-Evolution Logic
21. In execute-workflow UPDATE_AGENTS phase:
    - Read comparison discrepancies (missing games, revenue differences)
    - Append findings to `.claude/agents/opus-cli-researcher.md` (Findings Log section)
    - Generate SDK evolution hints stored in `research/sdk-evolution-hints.md`
    - Next iteration, both agents receive updated context

---

## Ralph Wiggum Loop Mechanics

### How `ralph.sh` works
```bash
#!/bin/bash
for ((i=1; i<=$1; i++)); do
  result=$(claude -p "$(cat prompt.md)" --output-format text 2>&1) || true
  if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
    echo "CONVERGED after $i iterations!"
    exit 0
  fi
done
echo "Reached max iterations ($1)"
exit 1
```

### Running it
```bash
# Start Next.js SDK app first (in separate terminal)
cd claude-agent-sdk && npm run dev

# Run the autonomous loop (up to 100 iterations)
./ralph.sh 100
```

### State persistence between iterations
Each `claude -p` spawns a **fresh** Claude session. State persists via files:
- `research/research-workflow-state.yaml` — current phase, iteration, status
- `research/research-iterations.yaml` — all iterations with scores
- `.claude/agents/opus-cli-researcher.md` — accumulated learnings (agent evolves itself)
- `research/sdk-evolution-hints.md` — hints passed to SDK agent next iteration

### Promise tag contract
- `<promise>COMPLETE</promise>` — similarity ≥ 90%, ralph.sh stops
- `CONTINUING_RESEARCH` — similarity < 90%, ralph.sh continues

---

## Course 9 Principles Applied

| Principle | Application |
|-----------|-------------|
| Constitutional Governance | Research goal (all FIFA games + revenue) is fixed and re-asserted every iteration in agent prompts |
| Backpressure | 90% similarity threshold is the evaluation pressure driving improvement |
| Constraints Enable Creativity | Standardized JSON output format forces structured, comparable research |
| Memory/Accumulation | Agent files grow with findings; each iteration builds on prior discrepancies |
| Convergence Detection | Stop at ≥90% similarity; state file tracks score history |
| Safety Architecture | Max iteration cap prevents infinite runs; git commits create rollback points |

---

## Standardized Output Format

Both agents write markdown with embedded JSON:

```json
{
  "games": [{
    "name": "FIFA International Soccer",
    "year": 1993,
    "platform": "Sega Genesis, SNES",
    "publisher": "EA Sports",
    "estimatedRevenue": 50000000,
    "revenueSource": "source URL or description",
    "confidence": "low|medium|high"
  }],
  "totalGamesFound": 32,
  "searchQueries": ["queries used"],
  "sources": ["URLs consulted"]
}
```

---

## Verification

1. `npm install` in `claude-agent-sdk/`
2. Start SDK app: `cd claude-agent-sdk && npm run dev`
3. Single iteration test: `claude -p "$(cat prompt.md)" --output-format text`
4. Verify CLI output exists: `claude-code-cli/research-1-output.md`
5. Verify SDK output exists: `claude-agent-sdk/research-1-output.md`
6. Verify comparison: `research/comparison-1.md`
7. Verify state updated: `research/research-workflow-state.yaml`
8. Full autonomous run: `./ralph.sh 100`
