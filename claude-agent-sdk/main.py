from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import run_research_agent
from pathlib import Path

app = FastAPI(
    title="Research SDK Agent",
    description="Claude Agent SDK-based research agent. Uses Max subscription via Claude Code. Reads problem from problem-statement/problem-statement.json.",
    version="4.0.0",
)


class ResearchRequest(BaseModel):
    iteration: int = 1


class ResearchResponse(BaseModel):
    success: bool
    outputFile: str
    redditDataFile: str
    summary: str


@app.post("/research-claude-agent-sdk", response_model=ResearchResponse)
async def research_claude_agent_sdk(request: ResearchRequest):
    try:
        result = run_research_agent(request.iteration)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health():
    return {
        "status": "ready",
        "auth": "Claude Max subscription (via Agent SDK)",
        "message": "Research SDK Agent. POST /research-claude-agent-sdk with {iteration: int}.",
    }
