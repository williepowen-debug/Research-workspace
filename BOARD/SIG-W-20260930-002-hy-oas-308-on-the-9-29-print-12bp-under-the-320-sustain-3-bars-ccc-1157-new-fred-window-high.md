---
signal_id: SIG-W-20260930-002
date: 2026-09-30
timestamp: 2026-09-30T23:03:34Z
time_dispatched: 2026-09-30T23:03:34Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: WALTER boot 6c scan (FRED, pulled 2026-09-30 ~22:3xZ via FORGE/tools/market-data/fetch.py)
origin: ["FRED BAMLH0A0HYM2 (ICE BofA US HY OAS): 3.08 [2026-09-29] · 3.02 [9/28] · 2.93 [9/25] · 2.80 [9/24] · 2.73 [9/23]", "FRED BAMLH0A3HYC (ICE BofA US HY CCC & Lower OAS): 11.57 [9/29] · 11.46 [9/28] · 11.28 [9/25]", "RESEARCH-INTAKE lane 2026-09-30T19:50Z carries the same 308 print (suppressed as still-true)"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
entities: ["HY OAS", "BAMLH0A0HYM2", "CCC OAS", "BAMLH0A3HYC", "RED-FT-02", "REG-T-03"]
confidence_language: "FRED primary, observation date 2026-09-29 (FRED publishes ~T+1; the 9/30 print posts ~Thu 10/01 AM). No extrapolation: three rising prints are a sequence, not a forecast."
signal_type: context
safety_net: clear
verdict: "NEAR-TRIGGER WATCH, RE-POINTED (supersedes the distance in SIG-W-20260929-008). High-yield spreads widened to 308bp on the 9/29 print, 12bp below the 320 line that two registered triggers share (RED-FT-02 and REG-T-03, each 3 consecutive observations above 320). Nothing fired: this is proximity, not a crossing. The one-day move was +6bp, far from the +25bp safety-net upgrade."
precedence: PRIORITY
action: []
info: ["REGINALD", "LIQUID", "CARL", "RED"]
confidence: 0.9
dispatch_note: "Re-points the watch dispatched in SIG-W-20260929-008 (302, 18bp away). Near-trigger per THRESHOLD_SCAN step 7 (within 5% one-sided of 320 = above 304); re-dispatched under BOARD_CONSUMPTION_SPEC §3.5.3 (a re-pointed watch is decision-changing information). Domain FUNDING_LIQUIDITY; LIQUID added to info versus -008 because LIQUID owns HY OAS and the X1 line. REGINALD info (REG-T-03 owner), CARL info (REG-T-03 chain), RED info (RED-FT-02 owner; pull-complete, via BOARD). One HY crossing fires TWO rows: if it comes, fire once and name both (REG_THRESHOLDS_FIRED_LOG header item c). Safety net: +6bp d/d vs the +25bp single-session bar; clear. No action line: nothing crossed."
---

# HY spreads 308bp [FRED 9/29]: 12bp under the >320 sustain-3 bars; CCC 1,157bp is a new high of FRED's public window

| Series | 9/23 | 9/24 | 9/25 | 9/28 | **9/29** | Bar |
|---|---|---|---|---|---|---|
| HY OAS (BAMLH0A0HYM2), bp | 273 | 280 | 293 | 302 | **308** | **>320, 3 consecutive** (RED-FT-02 · REG-T-03) · >350 (REG-T-04) |
| CCC & lower OAS (BAMLH0A3HYC), bp | 1,093 | 1,112 | 1,128 | 1,146 | **1,157** | RED-FT-07 >930 already FIRING-BANKED |

**State of each line (graded at the instrument, not carried):**
- **RED-FT-02** (`>320 s3`, PATH-B-CONFIRM) and **REG-T-03** (`>320 s3`, CREDIT-CANARY-FIRED): ARMED, **0 of 3**, **12bp away**. One crossing would fire both rows; fire once and name both.
- **REG-T-04** (`>350 s3`, ISSUANCE-FREEZE): 42bp away.
- **RED-FT-01** (`<280 s3`): re-armed 0 of 3 after RED executed its exit on 9/29 (S48). **RED-FT-12** (`<260 s3`): 48bp away.
- **Safety net:** +6bp on the day vs the +25bp single-session bar; clear.
- **CCC 1,157:** the highest in FRED's public window, which **starts 2023-09-30; this is NOT an all-time high.** The CCC effective yield is the same index plus a rates leg, so it is **not a second witness** (LIQUID, `SIG-W-20260929-003`).

⚠️ **Date basis:** FRED observation date 9/29. The 9/30 print posts about Thu 10/01 morning; a count needs three consecutive FRED observations above 320, and the pull date never counts.

**INFO (REGINALD, LIQUID, CARL, RED):** distance to your lines only; no ask. $0.
