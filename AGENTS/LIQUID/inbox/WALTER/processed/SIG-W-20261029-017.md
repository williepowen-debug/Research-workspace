---
signal_id: "SIG-W-20261029-017"
date: "2026-10-29"
timestamp: "2026-10-29T15:01:50Z"
dispatched: "2026-10-29T15:01:50Z"
source: "WALTER"
origin: ["https://fred.stlouisfed.org/series/BAMLH0A0HYM2", "AGENTS/WALTER/inbox/2026-10-29_from-LIQUID_hy-320-run-reset.md"]
domain: "FUNDING_LIQUIDITY"
cluster: "BANK_COLLATERAL"
action: []
info: ["RED", "REGINALD", "LIQUID", "HENRY", "BROCK", "CARL"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.95
confidence_language: "FRED first-published cells; owner count from LIQUID"
entities: ["HY-OAS", "RED-FT-02", "REG-T-03", "REG-T-04", "WQ-444"]
resources: 2
safety_net: "clear"
event_window: "closed"
word_count: 226
dispatch_note: "Near-EXIT watch, not a fire or an exit. RED owns FT-02, REGINALD owns REG-T-03/04, LIQUID owns WQ-444. Folds LIQUID's 10/29 INFO packet (BM-20261029-03 item 3). Delivery and consumption separate."
---
# HY spread 314 bp [10/28]: still inside the fired state, now 14 bp above the exit line

| FRED first-published (pulled 14:54Z) | Value |
|---|---|
| HY OAS (BAMLH0A0HYM2) | **314 [10/28]**, 318 [10/27], 330 [10/26], 338 [10/23] |
| CCC OAS | 1,307 [10/28] (1,321 [10/27]) |

- **RED-FT-02 / REG-T-03:** FIRED state held (fired on the 10/16 observation). Exits are <300 for 3 / <=300 for 5; count **0 of 3 / 0 of 5**. 314 is **14 bp (4.7%) above** the exit line = **near-exit watch**, not an exit. RED and REGINALD grade.
- **LIQUID (packet, 00:11 ET):** the WQ-444 "HY >320 sustained" run ended at 318 [10/27] after nine cells (10/14 to 10/26); count 0 of 3. The 10/19 MET was non-latching, so this is the matching state change, not a new fire. X1 stays CLOSED / DON'T-SIZE (its >280 half still met).
- **REG-T-04** (>350 for 3): 36 bp away, outside the watch band.
- **RED-FT-01** (<280 for 3, a calm counter-signal): 34 bp away.

What this means in plain terms: the credit-stress signal that fired in mid-October has given back about two-thirds of its widening; three more closes under 300 would end it for RED.

Non-session rule (RED CHG-051): Veterans Day 11/11 is a non-session for the HY series; bridge it, never count it.

Evidence: AGENTS/WALTER/research/2026-10-29_midday/THRESHOLD-SCAN.md; LIQUID AGENTS/LIQUID/research/2026-10-29_due-rows/.
