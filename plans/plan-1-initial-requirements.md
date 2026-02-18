# Self-Evolving Dual-Agent FIFA Research System

## Context

This project demonstrates Course 9 (Self-Evolving Agentic Loops) principles by having **two AI agents** (Claude Code CLI and Claude Agent SDK) independently research FIFA/EA FC game releases and revenue, then **iteratively compare and refine** their outputs until they converge to 90%+ similarity. The self-evolving loop applies constitutional governance (fixed research goal), backpressure (similarity threshold), memory (discrepancy-driven prompt evolution), and convergence detection (max 5 iterations).

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                   ORCHESTRATOR                       │
│              orchestrator/run.ts                      │
│                                                       │
│  1. Generate evolution hints from prior discrepancies │
│  2. Trigger both agents in parallel                   │
│  3. Compare outputs (shared/comparator.ts)            │
│  4. If <90% similar → evolve prompts → loop           │
│  5. If >=90% or max iterations → stop                 │
└────────┬───────────────────────────────┬──────────────┘
         │                               │
    ┌────▼─────────┐            ┌────────▼──────────┐
    │ Claude Code   │            │ Claude Agent SDK   │
    │ CLI Agent     │            │ Web App            │
    │               │            │                    │
    │ /research cmd │            │ Express + Button   │
    │ Uses MCP:     │            │ Uses tool_use:     │
    │ - Tavily      │            │ - Tavily HTTP API  │
    │ - Reddit      │            │ - Reddit JSON API  │
    │               │            │                    │
    │ Output:       │            │ Output:            │
    │ claude-code-  │            │ claude-agent-sdk/  │
    │ cli/research- │            │ research-{n}-      │
    │ {n}-output.md │            │ output.md          │
    └──────────────┘            └────────────────────┘
```

---

## File Structure

```
/
├── .claude/commands/research.md     # /research slash command
├── .mcp.json                        # Tavily + Reddit MCP servers
├── .env                             # API keys (gitignored)
├── .gitignore
├── package.json                     # Root with all deps
├── tsconfig.json
├── shared/
│   ├── types.ts                     # GameEntry, ResearchOutput, ComparisonResult
│   ├── constants.ts                 # Game name aliases, thresholds
│   ├── comparator.ts                # Similarity scoring engine
│   └── prompt-evolver.ts            # Generate evolution hints from discrepancies
├── claude-code-cli/                 # Output directory (research-{n}-output.md)
├── claude-agent-sdk/                # Next.js app
│   ├── lib/agent.ts                 # Agent SDK agentic loop with tool_use
│   ├── app/api/research/route.ts    # Next.js API route
│   └── app/page.tsx                 # "Execute Research" button UI
├── orchestrator/
│   ├── run.ts                       # Main self-evolving loop entry point
│   └── state.json                   # Runtime iteration state (gitignored)
└── prompt/prompts.md                # (existing)
```

---

## Implementation Phases

### Phase 1: Foundation
1. Create `package.json` with deps: `@anthropic-ai/sdk`, `express`, `tsx`, `typescript`
2. Create `tsconfig.json`
3. Create `.env` (placeholder keys) + `.gitignore`
4. **User provides `.mcp.json`** with Tavily + Reddit MCP server configs (skip this step, user will supply)
5. Create `shared/types.ts` — `GameEntry`, `ResearchOutput`, `ComparisonResult` interfaces
6. Create `shared/constants.ts` — game name alias map, thresholds

### Phase 2: Claude Code CLI Agent
7. Create `.claude/commands/research.md` — slash command that instructs Claude to use Tavily + Reddit MCP tools, produce standardized JSON output in markdown
8. Create `claude-code-cli/` output directory

### Phase 3: Claude Agent SDK Next.js App
9. Initialize Next.js app in `claude-agent-sdk/` with `npx create-next-app`
10. Create `claude-agent-sdk/lib/agent.ts` — agentic loop using `@anthropic-ai/sdk` with `tool_use` for Tavily (HTTP) and Reddit (JSON API)
11. Create `claude-agent-sdk/app/api/research/route.ts` — API route handler (POST)
12. Create `claude-agent-sdk/app/page.tsx` — "Execute Research" button, iteration display, output viewer

### Phase 4: Comparison & Evolution Engine
12. Create `shared/comparator.ts` — fuzzy game name matching (via alias normalization) + revenue comparison (10% tolerance). Scoring: 50% game coverage + 50% revenue accuracy
13. Create `shared/prompt-evolver.ts` — takes `ComparisonResult`, generates targeted hints ("you missed FIFA 97", "revenue for FIFA 14 differs, investigate")

### Phase 5: Orchestrator (Self-Evolving Loop)
14. Create `orchestrator/run.ts`:
    - Read/create state.json (iteration, history)
    - Generate evolution hints (empty for iteration 1)
    - Trigger CLI agent via `claude -p` (piped mode)
    - Trigger SDK agent via HTTP POST to localhost
    - Run comparator on both outputs
    - If converged or max iterations (5): write final report
    - Else: **pause for human review** (show comparison summary, ask continue?)
    - On approval: evolve prompts, increment iteration, loop

---

## Course 9 Principles Applied

| Principle | Application |
|-----------|-------------|
| Constitutional Governance | Research goal (all FIFA games + revenue) is fixed and re-asserted every iteration |
| Backpressure | 90% similarity threshold drives improvement |
| Constraints Enable Creativity | Standardized JSON output format forces structured research |
| Memory/Accumulation | Each iteration's discrepancies feed into next iteration's hints |
| Convergence Detection | Stop at 90% similarity OR 5 max iterations |
| Trust Calibration | **Every iteration pauses for human review** before proceeding |

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
1. Run `npm install` to install all dependencies
2. Test CLI agent: run `/research` in Claude Code, check `claude-code-cli/research-1-output.md` has valid JSON
3. Test SDK agent: `npx tsx claude-agent-sdk/server.ts`, click button, check `claude-agent-sdk/research-1-output.md`
4. Test comparator: run with two sample outputs, verify similarity score
5. Test full loop: `npx tsx orchestrator/run.ts`, verify it iterates and converges
