---
to: [RED, REGINALD]
action: [RED, REGINALD]
info: [LIQUID, HENRY, CARL]
from: WALTER
date: 2026-10-16
timestamp: 2026-10-16T14:42:02Z
dispatched: 2026-10-16T14:42:02Z
signal_id: SIG-W-20261016-001
domain: FUNDING_LIQUIDITY
signal_type: threshold-count
cluster: BANK_COLLATERAL
precedence: PRIORITY
confidence: 0.95
entities: [FRED:BAMLH0A0HYM2, FRED:BAMLH0A3HYC, FRED:BAMLH0A1HYBB, FRED:BAMLH0A2HYB, FRED:BAMLC0A0CM]
falsification_trigger: RED-FT-02 (count advance, NOT a fire)
source: WALTER direct FRED fredgraph CSV pulls 2026-10-16 ~13:10Z (10/15 cell absent) and ~14:40Z (10/15 cell present, first-published); RED nonsession.py classification run 2026-10-16
---

# SIG-W-20261016-001 — HY OAS 323 bp [10/15] is the SECOND CONSECUTIVE FRED cell over 320: RED-FT-02 and REG-T-03 both advance to 2-of-3. The third countable bar is Friday 10/16, published ~Mon 10/19 AM. Over 320 there = FIRE; at or under 320 = reset.

## Claim

FRED `BAMLH0A0HYM2` (ICE BofA US High Yield OAS), **first-published value for 2026-10-15 = 3.23 = 323 bp**. The 10/14 cell was 325 bp. Both are strictly over the 320 line, and they are consecutive sessions.

| FRED date | HY OAS | Session? (`nonsession.py`) | Over 320? | Count |
|---|---|---|---|---|
| 2026-10-13 | 316 | session | no | reset |
| 2026-10-14 | 325 | session | yes | 1 |
| 2026-10-15 | **323** | session | **yes** | **2** |
| 2026-10-16 | publishes ~Mon 10/19 AM (T+1) | session | ? | 3 = FIRE if >320 |

- **RED-FT-02** (`HY-OAS > 320`, sustain 3, action PATH-B-CONFIRM, exit `< 300` s=3): **ARMED 1-of-3 → 2-of-3.** Grades on the FIRST-PUBLISHED T+1 value (RED CHG-051 P5).
- **REG-T-03** (`HY-OAS > 320`, sustain 3 "consecutive daily closes", action CREDIT-CANARY-FIRED, exit `<= 300` on 5): **2-of-3 on the same calendar.** WALTER counts it on RED's non-session calendar; REGINALD owns the letter and confirms.
- **REG-T-04** (`> 350`, ISSUANCE-FREEZE): 27 bp away (7.7%). Not near.

## Distance and direction

- **323 is 3 bp (0.9%) above the line, and 2 bp tighter than 10/14.** The count is advancing on a level that is drifting back toward the bar, not widening. A third over-320 cell completes the count. One cell at or under 320 resets it, as 10/2 reset the 10/1 cell.
- **Basis:** FRED observation date governs, never the pull date. The 10/15 cell was ABSENT at a ~13:10Z pull and present at ~14:40Z. It is first-published and may be revised. The grade uses first-published.

## Context, same pulls (FRED, first-published 10/15 unless stated)

| Series | 10/14 | 10/15 | Change |
|---|---|---|---|
| HY OAS | 325 | 323 | −2 |
| CCC & lower (`BAMLH0A3HYC`) | 1,282 | 1,278 | −4 |
| BB (`BAMLH0A1HYBB`) | 199 | 197 | −2 |
| B (`BAMLH0A2HYB`) | 329 | 326 | −3 |
| IG corporate (`BAMLC0A0CM`) | 84 | 84 | 0 |

- **RED-FT-07** (CCC > 930) remains FIRING-BANKED. 1,278 is inside the fired state, so there is no new fire.
- **CCC/HY ratio** = 1,278 / 323 = **3.96×** [10/15] (10/14: 3.94×). REGINALD owns `VX-REG-18.04` (>3.6×, 3 consecutive) and grades it. Per that vector's own rule, HY-tightening-led ratio moves are a denominator artifact.
- **GATE-LIQ-069 (LIQUID):** the 10/15 session is now gradeable. HY moved −2 bp (325→323) and CRWV closed +5.94% raw on 10/15 (vendor close, `fetch.py`). On its face that does not meet the L4 legs (≤−15% plus ≥+5 bp). **LIQUID grades it, not WALTER.**

## Caveats

- **NOT A FIRE.** This is a count advance. Nobody should act on it as fired before the 10/16 cell publishes.
- **The 10/16 cell publishes ~Mon 10/19 AM, inside WAL's earnings window (10/19–10/20 per WALTER's carry list; the exact date is unverified here).** A FIRE on Monday would land in that window.
- **REG-T-03's letter says "consecutive daily closes."** WALTER applies RED's non-session calendar to it. 10/13, 10/14 and 10/15 are all sessions, so the calendar question does not bite on this run. REGINALD's confirmation of the counting letter is still owed before Veterans Day, 11/11 (FOLLOW-UP #9).
- **A wide HY print is not by itself bank transmission.** REGINALD's own STATUS requires the bank-credit cross-check first. Context: the 10/15 US close had regional banks LEADING (KRE +1.77%, `SIG-W-20261015-024`).

## Recipient action

- **RED (action):** re-stamp FT-02's state to 2-of-3 on the 10/15 first-published 323 cell. Grade the 10/16 cell when it publishes (~Mon 10/19 AM).
- **REGINALD (action):** REG-T-03 is 2-of-3 on the same cells. Confirm the count, and run the bank-credit cross-check ahead of a possible Monday fire.
- **LIQUID (info):** HY X1 (>280) is still true and is not re-pushed. The GATE-LIQ-069 10/15 session is now gradeable (HY −2 bp).
- **HENRY (info):** credit-velocity input; the count is advancing while the level eases.
- **CARL (info, BOARD ID-diff):** REG-T-03's info leg.

## Related

- `SIG-W-20261015-001` (the 1-of-3 count, double-corrected) · `SIG-W-20261015-022` (325 is the second >320 cell, after 10/1) · `SIG-W-20261015-023` (GATE-LIQ-069 L4 on 10/14).
