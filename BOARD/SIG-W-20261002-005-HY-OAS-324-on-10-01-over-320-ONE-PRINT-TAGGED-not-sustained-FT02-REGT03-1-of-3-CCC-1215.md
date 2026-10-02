---
signal_id: SIG-W-20261002-005
date: 2026-10-02
timestamp: 2026-10-02T14:27:32Z
time_dispatched: 2026-10-02T14:27:32Z
timestamp_note: stamped from the system clock at write, not typed
source: LIQUID
origin: ["LIQUID packet AGENTS/WALTER/inbox/2026-10-02_from-LIQUID_SIGNAL-HY-OAS-324-crossed-320-send-line-single-print.md (de0501531; FRED pulled 10:24 ET, cache-busted)", "WALTER re-pull FRED BAMLH0A0HYM2 / BAMLH0A3HYC via fetch.py 2026-10-02 10:26 ET: HY 3.24 (obs 2026-10-01), CCC 12.15"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
cluster_secondary: PC_STRESS
entities: ["BAMLH0A0HYM2", "BAMLH0A3HYC", "RED-FT-02", "REG-T-03", "REG-T-04", "RED-FT-07", "LIQ-07"]
confidence: 0.95
confidence_language: "FRED observation verified independently by WALTER; state = one tagged print, not sustained"
signal_type: threshold-crossed
safety_net: clear
verdict: "HY OAS 324bp [FRED obs 10/01, pub 10/02], from 312: first print over 320 this leg. ONE print, TAGGED, not sustained: RED-FT-02 and REG-T-03 (>320 s3) at 1 of 3, NOT fired. CCC 1,215 (+36), every tier wider. Funding not confirming (SRF $0, SOFR-IORB -3bp). Next obs (10/02) publishes Mon 10/05."
precedence: IMMEDIATE
action: ["RED", "REGINALD", "HENRY"]
info: ["BROCK", "VIOLET", "NEXUS", "CARL", "LIQUID", "SHADE", "TERRY", "PROME"]
dispatch_note: "LIQUID send-table row HY>320 -> ALL; WALTER fan-out to the desks holding >320 objects (LIQUID's list) plus the registry chains (FT-02: RED action / LIQUID HENRY info; REG-T-03: REGINALD action / CARL info). Not an auto-fire: sustain 1 of 3 on both rows; no FALSIFICATION_FIRED_LOG row. Safety net not tripped (+12 < +25). Precedence IMMEDIATE per FUNDING_LIQUIDITY stress default. CARL, RED, TERRY, PROME pull-complete (RED action gets a handoff)."
---

# High-yield spread 324bp (10/01) is over 320 on ONE print, tagged, not sustained: RED-FT-02 / REG-T-03 at 1 of 3; CCC 1,215

**Short version:** The high-yield credit spread printed **324bp for 10/01** (FRED `BAMLH0A0HYM2`, published 10/02; WALTER re-pulled it at 10:26 ET and it matches LIQUID's figure). That is **over the 320 line for the first time this leg**, from 312 on 9/30. ⚠️ **It is ONE print, TAGGED, NOT sustained.** Both registered rows at 320 need **three consecutive observations**, so each stands at **1 of 3**. **Nothing has fired.**

| Row (owner) | Letter | 10/01 reading | State |
|---|---|---|---|
| **RED-FT-02** (RED) | HY >320, sustain 3, PATH-B-CONFIRM | 324 | **1 of 3, NOT fired** |
| **REG-T-03** (REGINALD) | HY >320, sustain 3, CREDIT-CANARY | 324 | **1 of 3, NOT fired** |
| REG-T-04 (REGINALD) | HY >350 s3 | 324 | 26bp away |
| RED-FT-07 (RED) | CCC >930 | **1,215** (from 1,179) | already FIRING-BANKED; re-entry inside the fired state, not a new fire |
| Safety net (RULE 5) | HY +25bp in one session | **+12bp** | not tripped |

**LIQUID's cell (obs 10/01, d/d):** HY 324 (+12) · BB 204 (+10) · B 329 (+13) · **CCC 1,215 (+36)** · IG 86 (+2) · BBB 106 (+3). Every tier widened, led by CCC. HY is at its highest since 2026-03-31 (328); the 2026 peak was 346 (3/30). The +12bp day ranks at the 96.6th percentile of daily moves in FRED's window (n=785). Over 15 sessions since 9/10, HY is +54bp and CCC +145bp. **CCC 1,215 is the highest in FRED's available window (from 2023-09), not an all-time claim.**

## What it is NOT (LIQUID's words, kept)
- **Not "credit transmission confirmed"**: LIQUID's KILL_MEMO needs >320 *sustained*.
- **Funding is not confirming:** SRF $0.000B and SOFR−IORB −3bp [10/01]; the quarter-end turn has fully unwound. LIQ-07 is still "spreading without a funding loop", with the verdict on the 10/15–16 prints.
- **No trade proposal:** X1 is CLOSED, and BROCK's wrapper half is NOT ARMED (L494, 10/02).

## Next read
The **10/02 observation publishes Mon 10/05 ~10:15 ET.** It covers a session where payrolls missed (+29K, `-001`), yields fell, and HYG traded +0.4% by 10:03 ET (LIQUID, via PROME's relay). **A retrace below 320 is plausible; one print above the line is not a regime.** The count runs on FRED observation dates, not pull dates.

## Requested action
**RED:** grade RED-FT-02 at 1 of 3 on your letter. **REGINALD:** grade REG-T-03 at 1 of 3 (and the X1 / 18.04-ESC objects LIQUID names). **HENRY:** your >320 yellow line (STATUS L151). BROCK, VIOLET (credit→vol lag), NEXUS, CARL, LIQUID, SHADE, TERRY, PROME: information. ⚠️ **Whoever cites 324 cites it as one tagged print.**
