import asyncio
import json
import os
import re
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition, AssistantMessage, ResultMessage, TextBlock

# Remove CLAUDECODE env var to allow SDK to spawn Claude CLI subprocess
# (prevents "cannot be launched inside another Claude Code session" error)
os.environ.pop("CLAUDECODE", None)

PROJECT_ROOT = Path(__file__).parent.parent
SDK_ROOT = Path(__file__).parent


def load_problem() -> dict:
    """Load the research problem definition from problem-statement/problem-statement.json."""
    problem_path = PROJECT_ROOT / "problem-statement" / "problem-statement.json"
    if problem_path.exists():
        return json.loads(problem_path.read_text(encoding="utf-8"))
    return {"game": "TEKKEN", "start_year": 1990, "end_year": 2026}


def load_agent_prompt() -> str:
    """Load the reddit-game-research-agent prompt (strip YAML frontmatter)."""
    agent_path = PROJECT_ROOT / ".claude" / "agents" / "reddit-game-research-agent.md"
    if agent_path.exists():
        content = agent_path.read_text(encoding="utf-8")
        match = re.match(r"^---\n.*?\n---\n(.*)", content, re.DOTALL)
        return match.group(1).strip() if match else content
    return ""


def load_workflow_command(iteration: int, game: str, start_year: int, end_year: int) -> str:
    """Load the workflow command template and interpolate variables."""
    cmd_path = SDK_ROOT / ".claude-resources" / "commands" / "workflow-research-sdk.md"
    if cmd_path.exists():
        template = cmd_path.read_text(encoding="utf-8")
        return (
            template
            .replace("{iteration}", str(iteration))
            .replace("{game}", game)
            .replace("{start_year}", str(start_year))
            .replace("{end_year}", str(end_year))
        )
    return ""


def load_mcp_config() -> dict:
    """Load MCP server config from .mcp.json."""
    mcp_path = PROJECT_ROOT / ".mcp.json"
    if mcp_path.exists():
        data = json.loads(mcp_path.read_text(encoding="utf-8"))
        return data.get("mcpServers", {})
    return {}


async def _run_research(iteration: int) -> dict:
    """Run research using the same 2-step workflow as the CLI command."""
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

    # Load the workflow command from file (mirrors CLI's .claude/commands/workflow-research-cli.md)
    system_prompt = load_workflow_command(iteration, game, start_year, end_year)

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
