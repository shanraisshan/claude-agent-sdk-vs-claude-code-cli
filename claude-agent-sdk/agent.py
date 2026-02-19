import asyncio
import json
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage, TextBlock

PROJECT_ROOT = Path(__file__).parent.parent


def load_problem() -> str:
    """Load the research problem definition from problem-statement/problem-statement.md."""
    problem_path = PROJECT_ROOT / "problem" / "problem.md"
    if problem_path.exists():
        return problem_path.read_text(encoding="utf-8")
    return "No problem definition found. Check problem-statement/problem-statement.md."


def load_agent_instructions() -> str:
    """Load the same agent instructions used by CLI (claude-code-cli-games-revenue-researcher.md)."""
    agent_path = PROJECT_ROOT / ".claude" / "agents" / "claude-code-cli-games-revenue-researcher.md"
    if agent_path.exists():
        return agent_path.read_text(encoding="utf-8")
    return ""


def load_evolution_log() -> str:
    """Load SDK evolution log if it exists."""
    log_path = PROJECT_ROOT / "research" / "sdk-evolution-log.md"
    if log_path.exists():
        return log_path.read_text(encoding="utf-8")
    return ""


def load_mcp_config() -> dict:
    """Load MCP server config from .mcp.json."""
    mcp_path = PROJECT_ROOT / ".mcp.json"
    if mcp_path.exists():
        data = json.loads(mcp_path.read_text(encoding="utf-8"))
        return data.get("mcpServers", {})
    return {}


async def _run_research(iteration: int) -> dict:
    """Run the research agent using Claude Agent SDK (uses Max subscription)."""
    problem = load_problem()
    agent_instructions = load_agent_instructions()
    evolution_log = load_evolution_log()
    mcp_servers = load_mcp_config()

    # Ensure output directory exists
    output_dir = PROJECT_ROOT / "research" / f"research-{iteration}" / "claude-agent-sdk"
    output_dir.mkdir(parents=True, exist_ok=True)

    evolution_section = ""
    if evolution_log:
        evolution_section = f"\n\n## SDK Evolution Log (learnings from previous iterations)\n{evolution_log}"

    system_prompt = f"""You are a Research Agent (SDK version). You must produce the SAME output as the CLI Research Agent would produce. Use the same research approach and methodology.

## Research Problem

{problem}

## Agent Instructions (same as CLI agent)

{agent_instructions}

## Output Instructions

You MUST write TWO files:

1. First write `research/research-{iteration}/claude-agent-sdk/reddit-data-{iteration}.md` — Save ALL raw Reddit posts/data you collected. Include post titles, content snippets, scores, and subreddits.

2. Then write `research/research-{iteration}/claude-agent-sdk/research-{iteration}.md` — Your synthesized research with a markdown summary followed by a JSON code block matching the output schema from the research problem.

Write reddit-data FIRST, then the research file.{evolution_section}"""

    prompt = f"Research iteration {iteration}: Execute the research problem. Use the Reddit MCP tools to find data. Produce output matching the CLI agent format exactly. Write reddit-data-{iteration}.md first, then research-{iteration}.md to research/research-{iteration}/claude-agent-sdk/."

    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        allowed_tools=["Read", "Write", "Edit", "Bash", "Glob", "Grep", "mcp__reddit-mcp-server"],
        permission_mode="dangerouslySkipPermissions",
        cwd=str(PROJECT_ROOT),
        mcp_servers=mcp_servers,
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
