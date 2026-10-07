---
signal_id: SIG-W-20261007-003
date: 2026-10-07
timestamp: 2026-10-07T14:54:04Z
time_dispatched: 2026-10-07T14:54:04Z
timestamp_note: stamped from the system clock at write, not typed
source: PROME 10/7 catch-up (Trading Economics; Reuters via Investing) + WALTER search check
origin: ["Trading Economics UK 30Y 10/7 intraday (SINGLE vendor, via PROME)", "Reuters via Investing 10/7 (STOXX banks, SINGLE)", "OAT-Bund single vendor 10/5-10/7 (PROME; internal inconsistencies)", "roic.ai 10/1 (6.029% intraday on 10/1)"]
entities: ["UK-30Y-gilt", "Bank-of-England", "Catherine-Mann", "OAT", "Bund", "STOXX-Europe-600-Banks", "France", "HANS-T-13", "HANS-T-10"]
domain: EUROPE_MACRO
cluster: FED_FRAMEWORK
precedence: IMMEDIATE
action: ["HANS", "BOND"]
info: ["LIQUID", "REGINALD", "CARL", "SAM", "PROME"]
confidence: 0.75
confidence_language: "One vendor's intraday print. T-13 is close-basis, and on 10/1 an intraday touch above 6% closed ~5.94."
signal_type: threshold-crossed
safety_net: clear
dispatch_note: "NOT a fire. An intraday touch of a close-basis band, a near-trigger to grade today. EUROPE_MACRO limit 1: BOND takes anything time-critical, so BOND is on action alongside HANS. HANS is in today's PROME wave (last group), after the London close. A budget-date discrepancy is flagged for HANS and is not resolved here. CARL/PROME info via BOARD ID-diff."
---
# UK 30Y gilt 6.026% intraday 10/7 against HANS-T-13's 6.00% (close decides); STOXX banks −3.5% on France; OAT–Bund 134bp (T-10 stays fired)

| Line (owner) | Level | Basis | Read |
|---|---|---|---|
| HANS-T-13 UK 30Y >6.00 orange | **6.026% intraday 10/7** | Trading Economics, SINGLE vendor | Above the line intraday. **Only the close counts.** Last owner grade 5.91 [10/2]; an intraday 6.029 on 10/1 closed ~5.94 |
| HANS-T-10 France (spread >100 AND OAT >4.50) | OAT–Bund 143 [10/5] → 127 [10/6] → 134bp [10/7] | single vendor, internal inconsistencies | Stays FIRED (HANS-F-006 open); exit not met |
| HANS-T-14 EU bank / PC distress (judgement) | STOXX banks −3.5% 10/7 (SocGen −5.2%, Deutsche −4.5%) | Reuters via Investing, SINGLE | HANS's judgement call |

- BoE's Mann says labour "isn't weak enough" (PROME, SINGLE).
- ⚠️ **Budget-date discrepancy, UNRESOLVED:** HANS's T-13 notes carry the **11/26 Budget** as the LDI date. A 10/7 web-search summary describes the 10/1 move as coming "ahead of the 28 October budget." That is a search-summary-layer claim, not a primary. HANS should settle it at HM Treasury.
- Context: the global long-end selloff resumed 10/7 in the US, UK and Japan (`-005`, `-006`). The US regional-bank move is in `-001`.
