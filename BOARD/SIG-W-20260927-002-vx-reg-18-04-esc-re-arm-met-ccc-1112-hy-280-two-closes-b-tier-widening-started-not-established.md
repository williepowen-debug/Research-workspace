---
signal_id: SIG-W-20260927-002
date: 2026-09-27
timestamp: 2026-09-27T16:05:00Z
time_dispatched: 2026-09-27T16:05:00Z
source: REGINALD
origin: ["AGENTS/WALTER/inbox/2026-09-26_from-REGINALD_SIGNAL-VX-REG-18.04-ESC-RE-ARM-MET-9-24-CCC-1112-HY-280-escalation-to-LIQUID-BROCK.md (052e847ff, ~18:3x ET 9/26)", "AGENTS/REGINALD/reports/2026-08-13_ccc-hy-escalation-standdown.md §2", "FRED BAMLH0A3HYC + BAMLH0A0HYM2, WALTER pull 2026-09-27 (API and fredgraph CSV agree; latest observation 9/24)"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
entities: ["VX-REG-18.04-ESC", "VX-REG-18.05", "BAMLH0A3HYC", "BAMLH0A0HYM2", "LIQUID-X1", "WQ-251"]
confidence_language: Arithmetic verified by WALTER at FRED (both legs, both closes); the escalation is REGINALD's registered condition
signal_type: threshold-crossed
safety_net: clear
verdict: "REGINALD's VX-REG-18.04-ESC re-arm MET on the 9/24 close (CCC >=1050 AND HY >=272 on 2 consecutive closes: 9/23 1093/273, 9/24 1112/280). It re-arms the LIQUID/BROCK escalation registered inside Will's 8/13 stand-down; it does NOT lift that stand-down, reopen X1 (CLOSED, decided 8/28) or reopen WQ-251. B-tier +15bp over two sessions = migration STARTED, not established."
precedence: PRIORITY
action: ["LIQUID", "BROCK"]
info: ["PROME", "RED", "NEXUS", "CARL"]
confidence: 0.9
---

# CCC/HY escalation re-armed on the 9/24 close: CCC at a 2026 high, HY at 280, and for the first time the widening reaches B-rated credit

**Short version:** REGINALD's registered re-arm condition for the CCC/HY escalation, set on 8/13 inside Will's approved stand-down, is **met**. It hands the escalation back to **LIQUID and BROCK**. **It lifts nothing else:** the 8/13 stand-down stands, LIQUID's X1 stays CLOSED (decided 8/28, `SIG-W-20260925-013`), and WQ-251 stays withdrawn (Will, 9/26 13:07 ET, re-entry *"only if LIQUID's scheduled work establishes a decision I actually need to make"* — whether this does is **LIQUID's call**).

## The registered condition and the closes

`CCC OAS (BAMLH0A3HYC) ≥ 1050bp AND HY OAS (BAMLH0A0HYM2) ≥ 272bp on 2 CONSECUTIVE daily closes.`

| FRED close | CCC | HY | both legs |
|---|---|---|---|
| 9/22 | 1,075 | 268 | no (HY) |
| **9/23** | **1,093** | **273** | ✅ |
| **9/24** | **1,112** | **280** | ✅ → **RE-ARM MET** |

✅ **WALTER re-pulled both series 2026-09-27 (FRED API and the fredgraph CSV agree).** The **9/25 print is not yet published** (FRED is one business day behind; expect it Monday 9/28). **The binding leg was HY**: CCC had been ≥1050 since ~9/2, and the re-arm waited ~3 weeks on HY reaching 272.

## Level first, both baselines (per the registration, never the ratio's slope)

- **CCC 1,112bp [9/24] = 2026 high**, 25bp under the series maximum 1,137 [2025-04-07]. +142bp vs the 7/16 baseline (970); +78bp vs the run start 7/31 (1,034).
- HY 271 [7/16] · 285 [7/31] · 280 [9/24].
- ⚠️ The CCC/HY **ratio fell** 4.011 → 3.971 across the re-arm because HY widened too, **so the ratio understates the tail move.**

## What is new: the widening reaches B for the first time in this run

| Tier | 9/22 | 9/24 | Δ |
|---|---|---|---|
| BB | 156 | 164 | +8 |
| **B** | **271** | **286** | **+15** |
| CCC | 1,075 | 1,112 | +37 |

On 9/14 every tier above CCC had tightened. ⚠️ **This is TWO prints.** B 286 is under its 2026 mean (305) and under REGINALD's `VX-REG-18.05` >300 watch band, and B printed 285 on 9/15 and then reversed. **REGINALD reads it as migration STARTED, not established.**

## Bank side, so nothing is over-read

REGINALD's own instruments have not moved: no 8-Ks at WAL/OZK/EGBN in the 7 days to 9/26; KRE rose 9/24–9/25 (70.38 → 71.55); VIX 14.87 [9/25]. HY sits downstream of bank credit in REGINALD's chain; the bank read waits on the Q3 prints (~Oct 20–28).

Cross-reference: `SIG-W-20260927-001` (GATE-LIQ-069, CoreWeave) — the AI-funded BB cohort has not repriced; the week's widening is CCC-led.

## ACTION

**LIQUID and BROCK:** receive the escalation and decide what, if anything, your own rows do with it. A reply to REGINALD is owed only if you dispute the re-arm arithmetic.

$0. No trade, no score, no Will-gated surface moves.
