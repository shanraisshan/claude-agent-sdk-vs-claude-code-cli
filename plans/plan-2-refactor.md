# Plan 2 — Major Refactor: FastAPI + Reddit-Only + New Directory Structure

## Context

Iteration 1 completed with 68.33% similarity. Before continuing iterations, the user wants to refactor the system:
1. Replace the Next.js SDK app with a **FastAPI Python** app
2. Restructure research output into **per-iteration directories** under `research/`
3. Remove **Tavily**, use **Reddit-only** research for both agents
4. Each iteration produces separate `reddit-data-{n}.md` and `research-{n}.md` files
5. Comparison report lives inside the iteration folder

---

## New Directory Structure

```
research/
  research-1/
    claude-code-cli/
      research-1.md            # Synthesized research with JSON block
      reddit-data-1.md         # Raw Reddit data collected
    claude-agent-sdk/
      research-1.md            # Synthesized research with JSON block
      reddit-data-1.md         # Raw Reddit data collected
    comparison-1.md            # Comparison report
  research-2/
    ...same structure...
  research-workflow-state.yaml   # Stays at research/ root
  research-iterations.yaml       # Stays at research/ root
  research-status.json           # Stays at research/ root
```

---

## Implementation Steps

### Step 1: Delete Next.js App & Old Outputs

**Delete:**
- `claude-agent-sdk/` — entire directory contents (app/, lib/, node_modules/, package.json, etc.)
- `claude-code-cli/research-1-output.md` — old output
- `claude-agent-sdk/research-1-output.md` — old output
- `research/comparison-1.md` — old comparison
- `research/sdk-evolution-hints.md` — old hints

**Command:** `rm -rf claude-agent-sdk/* claude-agent-sdk/.next claude-agent-sdk/.gitignore claude-code-cli/research-1-output.md research/comparison-1.md research/sdk-evolution-hints.md`

---

### Step 2: Create FastAPI Python Project

**Directory:** `claude-agent-sdk/`

**Create `claude-agent-sdk/requirements.txt`:**
```
anthropic>=0.40.0
fastapi>=0.115.0
uvicorn>=0.32.0
httpx>=0.27.0
python-dotenv>=1.0.0
```

**Create `claude-agent-sdk/main.py`:**
- FastAPI app with single `POST /research` endpoint (accepts `{"iteration": int}`)
- `GET /health` endpoint for status checks
- Swagger UI auto-available at `/docs`
- Loads `.env` from project root using `python-dotenv`
- Port: **8000** (FastAPI default)

**Create `claude-agent-sdk/agent.py`:**
- Uses `anthropic` Python SDK with agentic tool_use loop
- Two tools: `reddit_search` (calls Reddit public JSON API via `httpx`) and `write_output`
- `reddit_search`: hits `https://www.reddit.com/search.json` or `https://www.reddit.com/r/{subreddit}/search.json`
- `write_output`: writes files to `research/research-{n}/claude-agent-sdk/`
- Reads evolution hints from `research/sdk-evolution-hints.md` if exists
- Agent must produce TWO files: `reddit-data-{n}.md` (raw data) then `research-{n}.md` (synthesized + JSON)
- Model: `claude-sonnet-4-20250514`, max_tokens: 8192

---

### Step 3: Update MCP Config — Remove Tavily

**Modify:** `.mcp.json`
- Remove `tavily-web-search` entry
- Keep `playwright` and `reddit-mcp-server`

---

### Step 4: Update `.env` and `.gitignore`

**Modify `.env`:** Remove `TAVILY_API_KEY` line, keep `ANTHROPIC_API_KEY`

**Modify `.gitignore`:** Add Python artifacts:
```
__pycache__/
*.pyc
.venv/
venv/
```

---

### Step 5: Rewrite CLI Research Agent

**Modify:** `.claude/agents/opus-cli-researcher.md`

Key changes:
- **Tools:** Reddit MCP only (remove all Tavily references)
- **Search strategy:** Reddit-only — search r/FIFA, r/EASportsFC, r/gaming, r/Games
- **Output:** TWO files in `research/research-{n}/claude-code-cli/`:
  1. `reddit-data-{n}.md` — raw Reddit search results
  2. `research-{n}.md` — synthesized research with JSON block
- **Keep** the Findings Log section (with iteration 1 findings intact)

---

### Step 6: Update Comparator Agent

**Modify:** `.claude/agents/opus-comparator.md`

Path changes only:
- CLI input: `research/research-{n}/claude-code-cli/research-{n}.md`
- SDK input: `research/research-{n}/claude-agent-sdk/research-{n}.md`
- Output: `research/research-{n}/comparison-{n}.md`

Scoring methodology unchanged.

---

### Step 7: Rewrite Execute-Workflow Orchestrator

**Modify:** `.claude/commands/execute-workflow.md`

Phase-by-phase updates:
- **PHASE 2 (GENERATE CLI):** Reddit MCP only, new output paths, must create both `reddit-data-{n}.md` and `research-{n}.md`
- **PHASE 3 (GENERATE SDK):** Change endpoint from `localhost:3000/api/research` to `localhost:8000/research`, new output verification paths
- **PHASE 4 (COMPARE):** Update all three paths (CLI input, SDK input, comparison output)
- **PHASE 7 (COMMIT):** Change `git add` to `git add research/ .claude/agents/ shared/`
- Phases 1, 5, 6, 8: minimal or no changes

---

### Step 8: Update prompt.md

**Modify:** `prompt.md`
- Change `localhost:3000` reference to `localhost:8000`
- Change "Tavily + Reddit MCP" to "Reddit MCP only"

---

### Step 9: Update shared/types.ts

**Modify:** `shared/types.ts`
- Add `RedditPost` interface
- Add `redditPostsAnalyzed?: number` to `ResearchOutput`

---

### Step 10: Update CLAUDE.md

**Modify:** `CLAUDE.md`
- Architecture: "FastAPI Python app" instead of "Next.js app"
- Key Directories: Show new `research/research-{n}/` structure
- Running: `cd claude-agent-sdk && pip install -r requirements.txt && uvicorn main:app --reload --port 8000`
- Remove Tavily mentions throughout

---

### Step 11: Reset State for Clean Start

**Modify:** `research/research-workflow-state.yaml` — reset to iteration 0, phase IDLE
**Modify:** `research/research-iterations.yaml` — keep iteration 1 as historical record

---

## Files Summary

| Action | File |
|--------|------|
| DELETE | `claude-agent-sdk/*` (all Next.js files) |
| DELETE | `claude-code-cli/research-1-output.md` |
| DELETE | `research/comparison-1.md`, `research/sdk-evolution-hints.md` |
| CREATE | `claude-agent-sdk/main.py` |
| CREATE | `claude-agent-sdk/agent.py` |
| CREATE | `claude-agent-sdk/requirements.txt` |
| MODIFY | `.mcp.json` — remove Tavily |
| MODIFY | `.env` — remove TAVILY_API_KEY |
| MODIFY | `.gitignore` — add Python ignores |
| MODIFY | `.claude/agents/opus-cli-researcher.md` — Reddit-only, new paths |
| MODIFY | `.claude/agents/opus-comparator.md` — new paths |
| MODIFY | `.claude/commands/execute-workflow.md` — new paths, FastAPI endpoint |
| MODIFY | `prompt.md` — port 8000, Reddit-only |
| MODIFY | `shared/types.ts` — add RedditPost |
| MODIFY | `CLAUDE.md` — update docs |
| MODIFY | `research/research-workflow-state.yaml` — reset |

---

## Verification

1. `cd claude-agent-sdk && pip install -r requirements.txt`
2. `uvicorn main:app --reload --port 8000` — verify Swagger at `http://localhost:8000/docs`
3. POST `{"iteration": 1}` to `http://localhost:8000/research` — verify output files created at `research/research-1/claude-agent-sdk/`
4. Single iteration test: `claude --dangerously-skip-permissions -p "$(cat prompt.md)" --output-format text`
5. Verify CLI outputs at `research/research-1/claude-code-cli/research-1.md` and `reddit-data-1.md`
6. Verify SDK outputs at `research/research-1/claude-agent-sdk/research-1.md` and `reddit-data-1.md`
7. Verify comparison at `research/research-1/comparison-1.md`
8. Full loop: `./ralph.sh 100`
