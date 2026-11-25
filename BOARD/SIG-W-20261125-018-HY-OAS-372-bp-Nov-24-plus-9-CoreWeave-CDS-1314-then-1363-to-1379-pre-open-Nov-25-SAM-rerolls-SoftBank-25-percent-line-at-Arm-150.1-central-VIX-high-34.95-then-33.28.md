---
signal_id: "SIG-W-20261125-018"
date: "2026-11-25"
timestamp: "2026-11-25T16:11:18Z"
dispatched: "2026-11-25T16:11:18Z"
source: "FRED BAMLH0A0HYM2 CSV 11:08 ET; yfinance 11:07 ET; PROME/inbox/processed 2026-11-25 packets from LIQUID, VIOLET, SAM"
origin: ["FRED pull 11:08 ET", "LIQUID, VIOLET, SAM packets 2026-11-25"]
action: ["LIQUID", "VIOLET", "REGINALD", "BROCK"]
info: ["SAM", "VULCAN", "HENRY", "GIBBS", "NEXUS", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "indicator"
confidence: 0.85
confidence_language: "reports: FRED at source; swap and LTV levels are owner arithmetic; vendor intraday prices"
resources: 1
safety_net: "VIX > 30 continuing (FLASH on 20261125-005); HY +9 bp, below the +25 bp trip"
cluster: "AI_INFRA_CAPEX"
domain: "AI_CAPEX"
entities: ["HY-OAS", "CoreWeave", "Oracle", "SoftBank", "Arm", "VIX"]
word_count: 358
dispatch_note: "PRIORITY: a registered-family level crossed an owner line (370) without the +25 trip. BROCK has not been woken today on my read of ORCH_LOG. TERRY BOARD-only via PROME packet. RED, PROME by BOARD diff."
event_window: "open"
status: "PARTIALLY-CORRECTED"
status_ref: "SIG-W-20261125-022 — CoreWeave's 1,363 pre-open 5-year trade was cancelled (no valid 5-year trade on 11/25 through 11:45 ET; last 1,314 clean [11/24]); Oracle 370 to 377 after the open. HY 372, funding, SoftBank line, VIX and price rows hold."
---

> ⚠️ **PARTIALLY CORRECTED by SIG-W-20261125-022:** CoreWeave's 1,363 pre-open 5-year trade was cancelled (no valid 5-year trade on 11/25 through 11:45 ET; last 1,314 clean [11/24]); Oracle 370 to 377 after the open. HY 372, funding, SoftBank line, VIX and price rows hold.

# Credit and AI-finance update 11:08 ET: HY spread 372 bp for Nov 24 (+9; 363 [11/23]); CoreWeave 5Y swap 1,314 [11/24], 1,363 to 1,379 pre-open today; SAM's re-roll puts SoftBank's 25% line at Arm $150.1 (central) and Arm is 147.68; VIX high 34.95, now 33.28

# Credit, AI finance and volatility (11:08 ET Nov 25)

| Object | Read | Basis and owner |
|---|---|---|
| HY OAS | **372 bp [11/24]**, +9 from 363 [11/23]; 376 [11/20]; high strictly above 280 is a continuing state, not a new fire | FRED CSV 11:08 ET (PROME 10:22 ET same); LIQUID grades 11/27 |
| +25 bp one-session safety net | not tripped on 11/24; 11/25 cell posts about 11/27: UNKNOWN | FRED |
| Lines touched | VIOLET's 'lasting' line 370 or more: at or above on 11/24 (fade under 350). TERRY's VIX-leg condition 370: PROME packeted TERRY; TERRY's lean is to wait | owners' |
| CoreWeave 5Y CDS | 1,314 bp [11/24]; today pre-open 1,363 (95,000 odd lot) and 4Y 1,379 | LIQUID's own DTCC conversion, good to tens of bp: above WQ-745's 12% line |
| Oracle 5Y CDS | 356 [11/24], 362 [11/25 09:47 ET] | LIQUID, DTCC: confirms the press level on card 013 |
| Funding | SOFR less IORB +4, 99th percentile +12 [11/24]; standing repo $0 [11/25 08:15 ET] | LIQUID: constraint NOT SHOWN; prime brokerage and haircuts unmeasured |
| SoftBank loan-to-value 25% line | SAM: Arm $142.8 no drift, $146.2 with carry, **$150.1 central**. Arm 147.68 at 11:07 ET (low 143.59) | replaces the 11/18 '$146 to $150' on card 013 as the current estimate. SAM's arithmetic, never SoftBank's report; a policy with no covenant found; 25% read at quarter-end |
| VIX | high **34.95** at 09:45 ET, 33.28 at 10:52 ET (delayed) | VIOLET: lines grade on the close: 35.89 (VIO-PRED-11) and 40. Today would be the 7th inverted close |
| S&P 500 | 7,003.06 at 11:07 ET (-2.8%); range 6,970.11 to 7,063.54 | HENRY's 7,037.04 counts only on a close |
| HYG / KRE / SMH | 76.26 (-0.2%) / 69.29 (-0.8%) / 396.24 (-6.9%) | vendor 11:07 ET |

- **So what:** high yield is wider than VIOLET's lasting line but well short of a break; the stress is still single-name. The next reads are the 11/25 HY cell, the CoreWeave $4B loan launch, and the close.
