# Plan: Thin Orchestrator Refactor

## Context

The `/self-evolving-workflow` command is a 187-line monolith that copy-pastes the full logic of `/research-claude-code-cli` (Phase 2) and `/compare-research` (Phase 4) inline. This means any change to CLI research or comparison logic requires updating two files. The user wants the orchestrator to be a thin delegator that only manages state and invokes the other commands — zero duplicated logic.

## Changes

### 1. Rewrite `.claude/commands/self-evolving-workflow.md` (primary change)

Strip out all inlined CLI research and comparison logic. The new orchestrator has 6 phases:

| Phase | What it does | Owns vs Delegates |
|-------|-------------|-------------------|
| 1. Initialize | Read state, increment iteration, write state | **Owns** |
| 2. CLI Research | Spawn Task subagent: "Read `.claude/commands/research-claude-code-cli.md` and follow it" | **Delegates** |
| 3. SDK Research | `curl POST localhost:8000` with iteration; if fail → read/fix `agent.py`+`main.py`, retry 3x | **Owns** (SDK is an external service) |
| 4. Compare | Spawn Task subagent: "Read `.claude/commands/compare-research.md` and follow it" | **Delegates** |
| 5. Evaluate & Evolve | If < 90% → evolve SDK code; if >= 90% → converged | **Owns** |
| 6. Update State | Write state files, commit, output COMPLETE or CONTINUING | **Owns** |

**What gets removed:** All logic for reading `problem-statement.json`, reading CLI agent instructions, spawning/instructing CLI research subagent directly, reading `research-compare.md`, spawning comparator subagent directly. The orchestrator no longer creates iteration directories (sub-commands handle their own).

**Delegation pattern:**
```
Spawn subagent (subagent_type: "general-purpose"):
  "Read `.claude/commands/research-claude-code-cli.md` and follow its instructions exactly.
   The current iteration is set in `research/self-evolving-state.yaml`."
Wait for output containing CLI_RESEARCH_COMPLETE.
```

### 2. Rename state file: `research/research-workflow-state.yaml` → `research/self-evolving-state.yaml`

Use `git mv`. Content unchanged. More accurate name since it tracks the self-evolving loop state, not a generic workflow.

### 3. Update `.claude/commands/research-claude-code-cli.md`

- Replace all references to `research/research-workflow-state.yaml` → `research/self-evolving-state.yaml`
- No logic changes — this command is already self-contained

### 4. Update `.claude/commands/compare-research.md`

- Replace all references to `research/research-workflow-state.yaml` → `research/self-evolving-state.yaml`
- No logic changes — already self-contained

### 5. Update `CLAUDE.md`

- State file reference: `research-workflow-state.yaml` → `self-evolving-state.yaml`
- Architecture description: note that `/self-evolving-workflow` is a thin orchestrator that delegates to sub-commands
- Key Directories section

### 6. Update `README.md`

- Project Structure section: rename state file reference

## Files NOT changing

- `.claude/agents/claude-code-cli-games-revenue-researcher.md` — ground truth, never modified
- `.claude/agents/research-compare.md` — already self-contained
- `claude-agent-sdk/agent.py` — already a replica of CLI (reads same agent instructions, same MCP, same problem file)
- `claude-agent-sdk/main.py` — no changes needed
- `ralph.sh`, `prompt.md` — no changes needed

## Implementation Order

All changes in a single commit since the state file rename is a breaking change if done partially:

1. Update `research-claude-code-cli.md` (state file reference)
2. Update `compare-research.md` (state file reference)
3. Rewrite `self-evolving-workflow.md` (thin orchestrator)
4. `git mv research/research-workflow-state.yaml research/self-evolving-state.yaml`
5. Update `CLAUDE.md`
6. Update `README.md`
7. Single commit: `refactor: thin orchestrator — self-evolving-workflow delegates to sub-commands`

## Verification

1. Run `/research-claude-code-cli` standalone — should still produce ground truth output and commit
2. Manually check that `research/self-evolving-state.yaml` exists and is read correctly
3. Run `/compare-research` standalone (after both outputs exist) — should produce comparison report
4. Run one full iteration via `ralph.sh 1` to verify the thin orchestrator delegates correctly end-to-end
