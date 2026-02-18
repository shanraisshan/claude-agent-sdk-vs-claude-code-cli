# SDK Evolution Hints

This file contains findings from comparison rounds that help align both agents' outputs.

## Iteration 1 Findings (Score: 68.3%)

### Game Coverage
- Both agents found identical 60 games — no missing games from either side.

### Revenue Methodology Alignment Needed
- The CLI agent estimated base game sales only (copies x retail price)
- The SDK agent estimated total franchise revenue per title (game sales + FUT + live services)
- **Both agents must use the same methodology**: Estimate TOTAL revenue per title including Ultimate Team / FUT microtransactions, live services, and DLC
- Key revenue benchmarks to calibrate against:
  - FUT revenue: $1.62B in FY2021, $1.71B in FY2024
  - Total FIFA franchise: ~$500M in FY2010, ~$2B by FY2020, ~$7B by FY2023
  - FIFA Mobile: $1B+ lifetime revenue
  - FIFA Online 4: Major Asian market revenue driver for Nexon

### Specific Revenue Corrections Needed
For pre-FUT titles (before FIFA 09/2008), base game sales estimates are likely correct and both agents agree.
For post-FUT titles (FIFA 09 onwards), revenue should include FUT microtransactions which grew from small amounts in 2009 to $1.7B+ annually by 2024.

### Revenue Discrepancies to Resolve
| Game | CLI Revenue | SDK Revenue | Target |
|------|------------|------------|--------|
| FIFA 06 | $200M | $300M | Align to one figure |
| FIFA 07 | $220M | $350M | Align to one figure |
| FIFA 08 | $250M | $400M | Align to one figure |
| FIFA 09 | $300M | $450M | Align to one figure |
| FIFA 14 | $700M | $900M | Align to one figure |
| FIFA 15 | $725M | $1,000M | Align to one figure |
| FIFA 16 | $550M | $1,100M | Align to one figure |
| FIFA 17 | $650M | $1,200M | Align to one figure |
| FIFA 19 | $1,000M | $1,600M | Align to one figure |
| FIFA 20 | $800M | $1,800M | Align to one figure |
| FIFA 21 | $1,000M | $2,000M | Align to one figure |
| FIFA 22 | $900M | $2,200M | Align to one figure |
| FIFA 23 | $1,100M | $2,600M | Align to one figure |
| EA Sports FC 24 | $1,050M | $2,500M | Align to one figure |
| EA Sports FC 25 | $900M | $2,200M | Align to one figure |
| EA Sports FC 26 | $600M | $1,500M | Align to one figure |
