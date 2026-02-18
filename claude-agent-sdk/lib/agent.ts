import Anthropic from "@anthropic-ai/sdk";
import { writeFileSync, readFileSync, existsSync } from "fs";
import { join } from "path";

const client = new Anthropic();

const TAVILY_API_KEY = process.env.TAVILY_API_KEY || "";

const tools: Anthropic.Tool[] = [
  {
    name: "web_search",
    description:
      "Search the web for information about FIFA/EA FC games and revenue data using Tavily API",
    input_schema: {
      type: "object" as const,
      properties: {
        query: {
          type: "string",
          description: "Search query",
        },
      },
      required: ["query"],
    },
  },
  {
    name: "write_output",
    description: "Write the final research output to a markdown file",
    input_schema: {
      type: "object" as const,
      properties: {
        content: {
          type: "string",
          description: "The markdown content with embedded JSON to write",
        },
        filename: {
          type: "string",
          description: "The output filename",
        },
      },
      required: ["content", "filename"],
    },
  },
];

async function tavilySearch(query: string): Promise<string> {
  if (!TAVILY_API_KEY) {
    return JSON.stringify({
      error: "TAVILY_API_KEY not set",
      results: [],
    });
  }

  try {
    const response = await fetch("https://api.tavily.com/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        api_key: TAVILY_API_KEY,
        query,
        max_results: 10,
        include_answer: true,
      }),
    });

    if (!response.ok) {
      return JSON.stringify({ error: `Tavily API error: ${response.status}` });
    }

    const data = await response.json();
    return JSON.stringify(data);
  } catch (error) {
    return JSON.stringify({ error: `Search failed: ${error}` });
  }
}

function handleToolCall(
  toolName: string,
  toolInput: Record<string, string>
): Promise<string> | string {
  if (toolName === "web_search") {
    return tavilySearch(toolInput.query);
  }

  if (toolName === "write_output") {
    const projectRoot = join(process.cwd(), "..");
    const outputPath = join(projectRoot, "claude-agent-sdk", toolInput.filename);
    writeFileSync(outputPath, toolInput.content, "utf-8");
    return `Output written to ${outputPath}`;
  }

  return `Unknown tool: ${toolName}`;
}

export async function runResearchAgent(iteration: number): Promise<{
  success: boolean;
  outputFile: string;
  summary: string;
}> {
  const projectRoot = join(process.cwd(), "..");
  const outputFilename = `research-${iteration}-output.md`;
  const outputPath = join(projectRoot, "claude-agent-sdk", outputFilename);

  // Read evolution hints if they exist
  let evolutionHints = "";
  const hintsPath = join(projectRoot, "research", "sdk-evolution-hints.md");
  if (existsSync(hintsPath)) {
    evolutionHints = readFileSync(hintsPath, "utf-8");
  }

  const systemPrompt = `You are a FIFA/EA FC Research Agent (SDK version). Your task is to research ALL FIFA and EA Sports FC video game releases from the 1990s through EA Sports FC 26.

For each game, collect:
- name: Official game title
- year: Release year
- platform: Platform(s)
- publisher: Publisher
- estimatedRevenue: Estimated total revenue in USD
- revenueSource: Where the data came from
- confidence: "low", "medium", or "high"

Include main series, FIFA Street, FIFA Online, FIFA Mobile, and all official titles.

Your output MUST be a markdown file with a summary section followed by a JSON code block with this schema:
{
  "games": [{ "name", "year", "platform", "publisher", "estimatedRevenue", "revenueSource", "confidence" }],
  "totalGamesFound": number,
  "searchQueries": string[],
  "sources": string[]
}

Use the web_search tool to find data. When done, use write_output to save your research.
The output filename must be: ${outputFilename}

${evolutionHints ? `## Previous Iteration Findings\n${evolutionHints}` : ""}`;

  const messages: Anthropic.MessageParam[] = [
    {
      role: "user",
      content: `Research iteration ${iteration}: Find all FIFA/EA FC game releases and revenue data. Use web_search to gather data, then use write_output to save your complete research as "${outputFilename}".`,
    },
  ];

  let response = await client.messages.create({
    model: "claude-sonnet-4-20250514",
    max_tokens: 8192,
    system: systemPrompt,
    tools,
    messages,
  });

  // Agentic loop — keep processing tool calls until done
  while (response.stop_reason === "tool_use") {
    const toolUseBlocks = response.content.filter(
      (block): block is Anthropic.ContentBlock & { type: "tool_use" } =>
        block.type === "tool_use"
    );

    const toolResults: Anthropic.MessageParam = {
      role: "user",
      content: await Promise.all(
        toolUseBlocks.map(async (toolUse) => ({
          type: "tool_result" as const,
          tool_use_id: toolUse.id,
          content: await handleToolCall(
            toolUse.name,
            toolUse.input as Record<string, string>
          ),
        }))
      ),
    };

    messages.push(
      { role: "assistant", content: response.content },
      toolResults
    );

    response = await client.messages.create({
      model: "claude-sonnet-4-20250514",
      max_tokens: 8192,
      system: systemPrompt,
      tools,
      messages,
    });
  }

  // Extract text summary
  const textBlocks = response.content.filter(
    (block): block is Anthropic.TextBlock => block.type === "text"
  );
  const summary = textBlocks.map((b) => b.text).join("\n");

  const success = existsSync(outputPath);

  return {
    success,
    outputFile: outputFilename,
    summary: success
      ? `Research complete. Output written to ${outputFilename}`
      : `Agent finished but output file not found. Agent response: ${summary.slice(0, 500)}`,
  };
}
