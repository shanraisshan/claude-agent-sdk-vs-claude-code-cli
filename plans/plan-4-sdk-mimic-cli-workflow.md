# Plan 4: Refactor SDK to Mimic CLI Workflow Using MCP, Subagents & Task Tool

## Problem

The current SDK (`agent.py`) does NOT replicate the CLI workflow. It pastes the agent instructions into a system prompt and asks a single Claude session to do everything in one shot. The CLI uses a 2-step architecture:

1. **Spawn** the `reddit-game-research-agent` subagent via Task tool → writes `reddit-data-{n}.md`
2. **Synthesize** the raw data into `research-{n}.md` with revenue table + JSON

The SDK should use the **exact same architecture**.

## Research Findings

The Claude Agent SDK (`claude-agent-sdk` v0.1.38) officially supports:

| Feature | Support | Docs |
|---------|---------|------|
| MCP Servers | `mcp_servers` param in `ClaudeAgentOptions` | [MCP Docs](https://platform.claude.com/docs/en/agent-sdk/mcp) |
| Subagents | `agents` param with `AgentDefinition` | [Subagents Docs](https://platform.claude.com/docs/en/agent-sdk/subagents) |
| Task Tool | Subagents invoked via Task tool (must be in `allowed_tools`) | Same as above |
| `.mcp.json` auto-load | SDK auto-loads `.mcp.json` from `cwd` | [MCP Docs](https://platform.claude.com/docs/en/agent-sdk/mcp) |

## What Changes

### File: `claude-agent-sdk/agent.py` (full rewrite)

**Before (current):**
- Loads agent instructions as text, pastes into system prompt
- Single Claude session does everything (no subagent)
- MCP config loaded manually and passed as dict
- No Task tool, no AgentDefinition

**After (new):**
- Defines `reddit-game-research-agent` as an `AgentDefinition` with proper tools
- Main query uses `Task` tool to spawn the subagent (same as CLI)
- MCP server config passed via `mcp_servers` param
- 2-step workflow: subagent collects data → main agent synthesizes report

### File: `claude-agent-sdk/main.py`

No changes needed. It just calls `run_research_agent(iteration)`.

## Implementation Steps

### Step 1: Rewrite `_run_research()` in `agent.py`

```python
import asyncio
import json
import re
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition, AssistantMessage, ResultMessage, TextBlock

PROJECT_ROOT = Path(__file__).parent.parent


def load_problem() -> dict:
    problem_path = PROJECT_ROOT / "problem-statement" / "problem-statement.json"
    if problem_path.exists():
        return json.loads(problem_path.read_text(encoding="utf-8"))
    return {"game": "FIFA", "start_year": 1990, "end_year": 2026}


def load_agent_prompt() -> str:
    """Load the reddit-game-research-agent prompt (strip YAML frontmatter)."""
    agent_path = PROJECT_ROOT / ".claude" / "agents" / "reddit-game-research-agent.md"
    if agent_path.exists():
        content = agent_path.read_text(encoding="utf-8")
        # Strip YAML frontmatter (between --- markers)
        match = re.match(r"^---\n.*?\n---\n(.*)", content, re.DOTALL)
        return match.group(1).strip() if match else content
    return ""


def load_mcp_config() -> dict:
    mcp_path = PROJECT_ROOT / ".mcp.json"
    if mcp_path.exists():
        data = json.loads(mcp_path.read_text(encoding="utf-8"))
        return data.get("mcpServers", {})
    return {}


async def _run_research(iteration: int) -> dict:
    """Run research using the same workflow as the CLI command."""
    problem_data = load_problem()
    game = problem_data["game"]
    start_year = problem_data["start_year"]
    end_year = problem_data["end_year"]

    agent_prompt = load_agent_prompt()
    mcp_servers = load_mcp_config()

    # Ensure output directory exists
    output_dir = PROJECT_ROOT / "research" / f"research-{iteration}" / "claude-agent-sdk"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Define the reddit research agent as an AgentDefinition (same as CLI's .claude/agents/)
    reddit_agent = AgentDefinition(
        description="Reddit research agent. Searches Reddit for game release lists and copy sales data for a given franchise/era. Writes raw Reddit data to reddit-data file.",
        prompt=agent_prompt,
        tools=[
            "Read", "Write",
            "mcp__reddit-mcp-server__search_reddit",
            "mcp__reddit-mcp-server__get_post_details",
            "mcp__reddit-mcp-server__browse_subreddit",
            "mcp__reddit-mcp-server__user_analysis",
            "mcp__reddit-mcp-server__reddit_explain",
        ],
        model="opus",
    )

    # System prompt mirrors the CLI's workflow-research-cli.md command
    system_prompt = f"""You are the CLI research orchestrator (SDK version). You follow the exact same workflow as the CLI /workflow-research-cli command.

## STEP 1: SPAWN THE REDDIT RESEARCH AGENT

Use the Task tool to spawn the reddit-game-research-agent subagent with this prompt:

> You are the Reddit Research Agent. Your iteration number is {iteration}.
> Research the following: Find all {game} games released from {start_year} to {end_year}, and find how many copies each title sold (physical + digital sales only, no in-app purchases).
> Write your output to: research/research-{iteration}/claude-agent-sdk/reddit-data-{iteration}.md

Wait for the subagent to complete.

## STEP 2: SYNTHESIZE RESEARCH REPORT

Read research/research-{iteration}/claude-agent-sdk/reddit-data-{iteration}.md (the raw Reddit data).
Using the data, build a final research report and write it to research/research-{iteration}/claude-agent-sdk/research-{iteration}.md

The research report must contain:

**A. Revenue Table**

Calculate revenue as: copies sold x average retail price at time of release. Only count copy sales (physical + digital). Do NOT include microtransactions, DLC, loot boxes, or in-app purchases.

| # | Title | Year | Copies Sold | Revenue (USD) | Confidence |
|---|-------|------|-------------|---------------|------------|
| 1 | ... | ... | ... | ... | ... |
| **TOTAL** | | | | **$X.XX B** | |

**B. JSON Data Block**

```json
{{
  "games": [
    {{
      "name": "string",
      "year": "number",
      "platform": "string",
      "publisher": "string",
      "copiesSold": "number",
      "estimatedRevenue": "number (USD)",
      "revenueSource": "string (Reddit source summary)",
      "confidence": "low | medium | high"
    }}
  ],
  "totalRevenue": "number (USD)",
  "totalGamesFound": "number",
  "searchQueries": ["array of search queries used"],
  "redditPostsAnalyzed": "number"
}}
```

## STEP 3: REPORT

Output: SDK_RESEARCH_COMPLETE iteration={iteration}"""

    prompt = f"Execute the research workflow for iteration {iteration}. Spawn the reddit-game-research-agent subagent first, then synthesize the report."

    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        mcp_servers=mcp_servers,
        allowed_tools=[
            "Read", "Write", "Glob", "Grep", "Task",
            "mcp__reddit-mcp-server__*",
        ],
        agents={
            "reddit-game-research-agent": reddit_agent,
        },
        permission_mode="bypassPermissions",
        cwd=str(PROJECT_ROOT),
        max_turns=30,
    )

    final_text = ""
    cost = 0.0

    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    final_text += block.text
        elif isinstance(message, ResultMessage):
            cost = getattr(message, "total_cost_usd", 0.0) or 0.0

    research_file = output_dir / f"research-{iteration}.md"
    reddit_file = output_dir / f"reddit-data-{iteration}.md"

    return {
        "success": research_file.exists(),
        "outputFile": str(research_file.relative_to(PROJECT_ROOT)) if research_file.exists() else "",
        "redditDataFile": str(reddit_file.relative_to(PROJECT_ROOT)) if reddit_file.exists() else "",
        "summary": f"Research iteration {iteration} complete (cost: ${cost:.4f})"
        if research_file.exists()
        else "Output file not created by agent",
    }


def run_research_agent(iteration: int) -> dict:
    """Sync wrapper for the async research agent."""
    return asyncio.run(_run_research(iteration))
```

### Step 2: Verify `requirements.txt` has correct dependencies

```
claude-agent-sdk>=0.1.38
fastapi
uvicorn[standard]
```

No `anthropic` package needed — the `claude-agent-sdk` handles everything.

### Step 3: Remove unused imports and functions

Remove from `agent.py`:
- `load_evolution_log()` — evolution log is a self-evolving loop concern, not the agent's
- `load_agent_instructions()` → replaced by `load_agent_prompt()` (strips frontmatter)

## Architecture Comparison

### Before (SDK v3)
```
FastAPI POST /research-claude-agent-sdk
  └── agent.py: _run_research()
        └── query() with system_prompt containing agent instructions
              └── Single Claude session does everything
                    ├── Searches Reddit (maybe)
                    └── Writes both files (maybe)
```

### After (SDK v4 — this plan)
```
FastAPI POST /research-claude-agent-sdk
  └── agent.py: _run_research()
        └── query() with Task tool + AgentDefinition
              ├── STEP 1: Task tool spawns reddit-game-research-agent
              │     └── Subagent searches Reddit via MCP
              │     └── Writes reddit-data-{n}.md
              └── STEP 2: Main agent reads raw data
                    └── Synthesizes research-{n}.md
```

This matches the CLI workflow exactly:
```
/workflow-research-cli
  └── STEP 2: Task tool spawns reddit-game-research-agent
  │     └── Subagent searches Reddit via MCP
  │     └── Writes reddit-data-{n}.md
  └── STEP 3: Command reads raw data
        └── Synthesizes research-{n}.md
```

## What Does NOT Change

- `.claude/agents/reddit-game-research-agent.md` — never modified (ground truth)
- `.mcp.json` — same MCP config, auto-loaded by SDK
- `problem-statement/problem-statement.json` — same problem source
- `main.py` — no changes, just calls `run_research_agent()`
- Output file structure — same `reddit-data-{n}.md` + `research-{n}.md`
- CLI workflow — completely untouched

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| `AgentDefinition` import may not exist in v0.1.38 | Check installed package; upgrade if needed |
| `bypassPermissions` may not be a valid mode | Fallback to `dangerouslySkipPermissions` |
| MCP wildcard `mcp__reddit-mcp-server__*` may not work | List individual tool names explicitly |
| Subagent may not write to correct directory | Explicit path in prompt + verify after |
