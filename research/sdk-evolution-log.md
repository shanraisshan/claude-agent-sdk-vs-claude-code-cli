# SDK Evolution Log

### Iteration 2 Evolution (Score: 62.5%)
- Discrepancies: SDK overestimated copies sold for FC 24 (12.5M vs CLI 9.5M), FC 25 (9.5M vs CLI 7M), FC 26 (9M vs CLI 6.5M). SDK included EA Sports FC Mobile (F2P, not a paid title). SDK used higher average pricing for FC 24/FC 25.
- Changes to agent.py: Fixed CLAUDECODE env var blocking nested sessions. Changed mcp_servers to use file path instead of parsed dict. Added stderr logging.
- Changes to main.py: Cleaned up debug endpoint.
- Changes to workflow-research-sdk.md: Added 6 new synthesis rules — exclude F2P mobile titles, "players" ≠ copies sold (60-75% conversion), use lower estimates for underperforming titles, conservative estimates for early-lifecycle games, platform-weighted pricing guidance, totalGamesFound should only count premium titles.
