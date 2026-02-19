# SDK Evolution Log

### Iteration 2 Evolution (Score: 62.5%)
- Discrepancies: SDK overestimated copies sold for FC 24 (12.5M vs CLI 9.5M), FC 25 (9.5M vs CLI 7M), FC 26 (9M vs CLI 6.5M). SDK included EA Sports FC Mobile (F2P, not a paid title). SDK used higher average pricing for FC 24/FC 25.
- Changes to agent.py: Fixed CLAUDECODE env var blocking nested sessions. Changed mcp_servers to use file path instead of parsed dict. Added stderr logging.
- Changes to main.py: Cleaned up debug endpoint.
- Changes to workflow-research-sdk.md: Added 6 new synthesis rules — exclude F2P mobile titles, "players" ≠ copies sold (60-75% conversion), use lower estimates for underperforming titles, conservative estimates for early-lifecycle games, platform-weighted pricing guidance, totalGamesFound should only count premium titles.

### Iteration 3 Evolution (Score: 83.33%)
- Discrepancies: SDK underestimated FC 26 revenue ($335M vs CLI $455M, 26.37% gap). FC 24 and FC 25 were within 10% tolerance. SDK used overly conservative 5M copies for FC 26 (CLI used 6.5M) and used $67 avg price instead of $70.
- Changes to agent.py: None needed — agent code is stable.
- Changes to main.py: None needed.
- Changes to workflow-research-sdk.md: Updated "active sales window" rule to estimate based on franchise trajectory rather than defaulting to ultra-conservative. Updated pricing rule to use $70 for current-gen-only titles (FC 26 dropped last-gen support). These changes should align FC 26 estimates closer to CLI ground truth.

### Iteration 5 Evolution (Score: 37.5%)
- Discrepancies: SDK missing FIFA 23 entirely (CLI includes it as actively sold in 2023). SDK underestimates all revenues: FC 24 ($651M vs $770M, 15.45%), FC 25 ($434M vs $560M, 22.5%), FC 26 ($525M vs $665M, 21.05%). Root causes: (1) SDK only includes games "released" in range, not "actively sold"; (2) SDK uses $62 blended price for FC 24/25 instead of $70; (3) SDK uses too-low player-to-purchaser conversion ratio (65% vs ~75-80%).
- Changes to agent.py: None needed — agent code is stable.
- Changes to main.py: None needed.
- Changes to workflow-research-sdk.md: (1) Updated agent spawn prompt to include games "released OR actively sold" in the year range. (2) Added explicit rule that games released just before start_year count if they were the active franchise title. (3) Increased player-to-purchaser ratio from 60-75% to 75-80% for mainstream annual franchises. (4) Changed default pricing to $70 for all modern FIFA/FC titles (2023+), only use $60 for pre-2023 titles.
