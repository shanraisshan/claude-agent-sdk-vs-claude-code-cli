"use client";

import { useState } from "react";

interface ResearchResult {
  success: boolean;
  outputFile: string;
  summary: string;
}

export default function Home() {
  const [iteration, setIteration] = useState(1);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<ResearchResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  const runResearch = async () => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch("/api/research", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ iteration }),
      });

      const data = await response.json();
      setResult(data);
      setIteration((prev) => prev + 1);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Request failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-950 text-white p-8">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-3xl font-bold mb-2">
          FIFA Research — SDK Agent
        </h1>
        <p className="text-gray-400 mb-8">
          Claude Agent SDK with tool_use for FIFA/EA FC game research
        </p>

        <div className="bg-gray-900 rounded-lg p-6 mb-6">
          <div className="flex items-center gap-4 mb-4">
            <label className="text-sm text-gray-400">Iteration:</label>
            <input
              type="number"
              value={iteration}
              onChange={(e) => setIteration(Number(e.target.value))}
              className="bg-gray-800 border border-gray-700 rounded px-3 py-1 w-20 text-white"
              min={1}
            />
          </div>

          <button
            onClick={runResearch}
            disabled={loading}
            className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 disabled:cursor-not-allowed px-6 py-3 rounded-lg font-medium transition-colors w-full"
          >
            {loading ? "Researching..." : "Execute Research"}
          </button>
        </div>

        {loading && (
          <div className="bg-gray-900 rounded-lg p-6 mb-6">
            <div className="flex items-center gap-3">
              <div className="animate-spin h-5 w-5 border-2 border-blue-500 border-t-transparent rounded-full" />
              <span className="text-gray-300">
                Agent is researching FIFA/EA FC games...
              </span>
            </div>
          </div>
        )}

        {error && (
          <div className="bg-red-900/30 border border-red-800 rounded-lg p-4 mb-6">
            <p className="text-red-400">{error}</p>
          </div>
        )}

        {result && (
          <div
            className={`rounded-lg p-6 mb-6 ${
              result.success
                ? "bg-green-900/30 border border-green-800"
                : "bg-yellow-900/30 border border-yellow-800"
            }`}
          >
            <h2 className="font-semibold mb-2">
              {result.success ? "Research Complete" : "Research Issue"}
            </h2>
            <p className="text-sm text-gray-300 mb-2">
              Output: {result.outputFile}
            </p>
            <p className="text-sm text-gray-400">{result.summary}</p>
          </div>
        )}
      </div>
    </div>
  );
}
