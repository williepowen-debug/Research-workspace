---
signal_id: "SIG-W-20261125-013"
date: "2026-11-25"
timestamp: "2026-11-25T14:42:30Z"
dispatched: "2026-11-25T14:42:30Z"
source: "disruptionbanking.com and rallies.ai (helper reads 14:42Z); yfinance 14:40 to 14:41Z; VULCAN packet 31d49098fa"
origin: ["Disruption Banking 2026-11-25", "Rallies.ai 2026-11-25", "vendor bars 14:41Z"]
action: ["LIQUID", "VULCAN", "SAM", "BROCK", "HENRY", "TERRY"]
info: ["REGINALD", "NEXUS", "VIOLET", "GIBBS", "RED", "PROME"]
precedence: "IMMEDIATE"
signal_type: "divergence"
confidence: 0.7
confidence_language: "reports: secondary swap levels, vendor intraday prices"
resources: 1
safety_net: "VIX > 30 continuing (31.77 high, vendor; FLASH on 20261125-005)"
cluster: "AI_INFRA_CAPEX"
domain: "AI_CAPEX"
entities: ["Oracle", "CoreWeave", "Alphabet", "SpaceX", "SoftBank", "Arm", "HYG"]
word_count: 325
dispatch_note: "IMMEDIATE. ACTION LIQUID (swaps, HY), VULCAN, SAM (SoftBank 501, Arm), BROCK (alternative managers), HENRY. TERRY BOARD-only. RED, PROME by BOARD diff."
event_window: "open"
status: "PARTIALLY-CORRECTED"
status_ref: "SIG-W-20261125-022 — SoftBank 501 is unconfirmed (DTCC 466/471 [11/24]; today inferred higher); SpaceX 'record' is doubtful (286 to 295, about level with 10/30); Alphabet 96 to 97. Price rows and CoreWeave 1,314 [11/24] hold."
---

> ⚠️ **PARTIALLY CORRECTED by SIG-W-20261125-022:** SoftBank 501 is unconfirmed (DTCC 466/471 [11/24]; today inferred higher); SpaceX 'record' is doubtful (286 to 295, about level with 10/30); Alphabet 96 to 97. Price rows and CoreWeave 1,314 [11/24] hold.

# AI credit swaps at records in Nov 25 reports: Oracle 5-year 356 bp, CoreWeave 1,314 bp, Alphabet and SpaceX records without levels, SoftBank 501 bp (highest since Oct 2022); S&P 6,992 at 09:41 ET, under HENRY's 7,037 close line and 7,000; HYG only -0.3%

# AI single-name credit against broad credit, Nov 25 (09:41 ET, intraday vendor)

| Object | Read | Basis |
|---|---|---|
| Oracle 5Y CDS | 356 bp, record | Disruption Banking Nov 25; 'overnight', no date; S&P Global Market Intelligence credited for the record |
| CoreWeave 5Y CDS | 1,314 bp, record; 68% implied 5-year default probability | same; matches VULCAN's '[11/24], LIQUID's figure'. 1,145 and 1,233 elsewhere are 11/17 to 11/20 |
| Alphabet, SpaceX 5Y | 'widest on record', no level | both pages |
| SoftBank 5Y | 501 bp, highest since October 2022 | Markit via both pages; observation date not stated |
| S&P / QQQ / VIX | 6,992.14 (low of day) / 610.18 / 31.72 (delayed) | HENRY's 7,037.04 is a CLOSE line; HENRY named 7,000 the largest put strike |
| HYG / LQD / BKLN / KRE | 76.21 (-0.3%) / +0.4% / -0.2% / 69.23 (-0.7%) | proxies, not OAS |
| Alternative managers | OWL -3.9%, ARES -3.6%, BX -3.2%, KKR -3.2%, APO -2.6%; BDCs near flat (BIZD -0.2%, OBDC -0.6%) | 09:40 ET |
| Neoclouds and builders | CRWV -10.6%, IREN -10.5%, APLD -10.3%, NBIS -10.2%, CORZ -8.4%, ORCL -7.7% | 09:40 ET |
| Arm | 146.45 low of the first minutes | SAM's '$146 to $150' is an 11/18 estimate on 11/10 marks, not a trigger |

- **Limit:** swap levels are secondary, undated 'overnight', one page a ticker blog; no original S&P or Markit page read. Both pages may share one Reuters source: one source, not two.
- **Not found:** a pulled or repriced AI-infrastructure deal today (VULCAN also found none), a bank or fund naming a loss.
- **So what:** the stress is at single-name AI borrowers and SoftBank while index credit is quiet. The discriminators are HY for 11/24 and 11/25, a refused deal, and whether the alternative managers' fall reaches loan and BDC marks.
