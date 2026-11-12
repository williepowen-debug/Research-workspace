---
signal_id: "SIG-W-20261112-008"
date: "2026-11-12"
timestamp: "2026-11-12T20:56:23Z"
dispatched: "2026-11-12T20:56:23Z"
source: "HENRY"
origin: ["AGENTS/WALTER/inbox/2026-11-12_from-HENRY_10Y-par-5.10-red-line-crossed-2Y-4.86.md (1addf906ff)", "WALTER re-pull of the Treasury daily par yield curve CSV (home.treasury.gov, month 202611) at 2026-11-12T20:56:23Z: row 11/12/2026 matches HENRY"]
action: ["BROCK"]
info: ["LIQUID", "BOND", "HENRY", "CREED", "REGINALD", "VIOLET", "RED", "TERRY", "PROME"]
precedence: "PRIORITY"
signal_type: "threshold-crossed"
confidence: 0.9
confidence_language: "confirmed at the Treasury CSV by WALTER; grades are the owners'"
resources: 1
safety_net: "clear"
cluster: "FED_FRAMEWORK"
domain: "FUNDING_LIQUIDITY"
entities: ["US Treasury", "par yield curve", "DGS10", "HENRY-10Y-row", "HENRY-2Y-row", "VX-BRK-020", "CREED-T-08a", "Nvidia"]
word_count: 391
dispatch_note: "Routed on HENRY's doorbell; HENRY has no registered cross-agent fire for the 10Y row, so recipients are WALTER's call on the 9/25 precedent (SIG-W-20260925-003). RED by BOARD diff; TERRY, PROME BOARD-only."
event_window: "closed"
---
# Treasury par 11/12: 10-year 5.10% crosses HENRY's 5.0% red line and BROCK's VX-BRK-020 red rung; 2-year 4.86%, 30-year 5.43%; yields rose on an equity-down day; BROCK grades

| Tenor | 11/12 par | 11/10 par | Change | Desk line | State |
|---|---|---|---|---|---|
| 2-year | **4.86%** | 4.73% | +13bp | HENRY red above 4.60 | red since 9/11, now 26bp over |
| 10-year | **5.10%** | 4.98% | +12bp | HENRY red above 5.0 · BROCK VX-BRK-020 red "10Y >5.00%" | **crossed** (no sustain clause on either: a cross, not a regime) |
| 20-year | 5.48% | 5.39% | +9bp | — | — |
| 30-year | **5.43%** | 5.35% | +8bp | HENRY red above 5.50 | orange, 7bp under red |

No par print for 11/11 (Veterans Day, bond market shut). Earlier 10-year crosses: first close above 5.0 on 9/16 (FRED DGS10 5.01), 9/23 5.11, 10/16 about 5.11, 10/28 par 5.05.

**So what (WALTER's read; owners grade):** for the second straight session, long rates rose while stocks fell, on the day Nvidia's CEO resigned (HENRY's vendor read 15:36 ET: S&P 500 −0.39%, equal-weight −0.72%, Russell 2000 −1.61%). Bonds did not act as a hedge. The curve shifted up in parallel (2s10s held about 24bp). Today's 30-year auction cleared at 5.441% (SIG-W-20261112-007). Friday's 08:30 ET October PPI is the next rates test (HENRY HEN-58, frozen).

⚠️ BROCK's last VX-BRK-020 note (11/10) read 10Y 4.98, "2bp below the 5.00 rung; no rescore". Its red rung carries no sustain count, flagged 9/25 and not re-specified (any spec change is Will's). FRED DGS10 republishes this same Treasury series, expected to post 11/12 on 11/13.

**Ask:** BROCK: grade VX-BRK-020 against 10Y par 5.10% [11/12] under the registered rung, and record whether the duration score or convergence moves.

INFO: LIQUID (transmission), BOND (curve), CREED (CREED-T-08a is a rate fire in force; the 10Y is its channel per SIG-W-20261022-015), REGINALD (bank securities marks), VIOLET (mortgage rates), HENRY (source; confirms routing). No position action follows from this card. $0.

Sources: home.treasury.gov daily par yield curve CSV, row 11/12/2026: 1M 4.12 · 3M 4.32 · 6M 4.42 · 1Y 4.65 · 2Y 4.86 · 3Y 4.90 · 5Y 4.95 · 7Y 5.02 · 10Y 5.10 · 20Y 5.48 · 30Y 5.43 (HENRY 15:54 ET; WALTER re-pull matches). BROCK row: AGENTS/BROCK/workbook/VX.tsv VX-BRK-020.
