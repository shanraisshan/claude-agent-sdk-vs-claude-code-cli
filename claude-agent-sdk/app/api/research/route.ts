import { NextRequest, NextResponse } from "next/server";
import { runResearchAgent } from "@/lib/agent";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const iteration = body.iteration || 1;

    const result = await runResearchAgent(iteration);

    return NextResponse.json(result);
  } catch (error) {
    return NextResponse.json(
      {
        success: false,
        outputFile: "",
        summary: `Error: ${error instanceof Error ? error.message : String(error)}`,
      },
      { status: 500 }
    );
  }
}

export async function GET() {
  return NextResponse.json({
    status: "ready",
    message: "FIFA Research SDK Agent API. POST with {iteration: number} to run research.",
  });
}
