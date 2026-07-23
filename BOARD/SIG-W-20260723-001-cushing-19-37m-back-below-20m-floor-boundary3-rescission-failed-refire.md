---
signal_id: SIG-W-20260723-001
dispatched: 2026-07-23T22:50:00Z
origin: RESEARCH-INTAKE lane (EIA feed, run 2026-07-23T16:23Z) + FORGE market-data dashboard 6c boot scan
source: EIA WPSR wk-ending 2026-07-17 (released 7/22), Cushing series W_EPC0_SAX_YCUOK_MBBL — primary
signal_type: threshold-crossed
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
cluster_secondary: IRAN_HORMUZ
signal_role: primary_substance
precedence: IMMEDIATE
to: BRENT
info: [LIQUID, HENRY, RED]
confidence: 0.95
verify_verdict: PRIMARY-DATA (EIA series via two independent live tool paths — intake lane EIA feed + FORGE dashboard EIA v2 API; BRENT independently read the same print 7/23 AM and converged)
boundary_ref: ROUTING_TABLE By Boundary Threshold #3 (Cushing <20M single print → IMMEDIATE → BRENT → LIQUID, HENRY, RED) — RE-FIRE on re-cross per the table's re-fire convention
---

# Cushing 19.37M (EIA wk-7/17) — BACK BELOW the 20M operational floor; Boundary #3 rescission FAILED at week 1 of 2. WTI dislocation risk re-opens.

## Substance (EIA primary, 0.95)

**Cushing crude stocks = 19.37M bbl, wk ending 7/17 (EIA WPSR released 7/22), −0.67M WoW from 20.044M.** This is a **re-cross below the ~20M operational bottom** (tank-bottom/suction-line minimum below which withdrawal degrades — the registered Boundary #3 level):

- **6/24-26:** Boundary #3 **first fired** at 18.957M (BRENT-primary fire, in BRENT's ledger; no BOARD dispatch existed for it — this signal is also the BOARD's first record of that fire history).
- **wk-7/10:** 20.044M — back ABOVE the floor; BRENT opened a **rescission clock (2 consecutive weeks >20M required)**.
- **wk-7/17: 19.37M — rescission FAILED at week 1 of 2.** The boundary state is re-asserted on the first post-Hormuz-closure inventory read.

Same-print context (all EIA, wk-7/17): **SPR 311.4M (draw RE-ACCELERATED −5.06M WoW)** · commercial crude **+2.01M build** · refinery utilization **96.1%** · gasoline demand +1.45% (BRENT reads hoarding, no demand destruction yet).

## Precision caveats (BRENT's own, carried so info recipients don't over-read)

- **Brent trades $8+ over WTI** → check **export-pull** before reading the Cushing draw as pure domestic tightness (the wide arb pulls barrels out through the Gulf; this was also the June-fire adjudication: STRUCTURAL, export-driven).
- This is an **inventory/operational-mechanics** datum. Today's Brent >$100 move (+6.8% 7/23) is attributed by wires to **risk-premium** (Red Sea kinetic escalation + Hormuz + 12th strike night), NOT to this print — do not weld the two into one mechanism.

## Recipients

**BRENT (action) — OWNER-AHEAD, confirm-only:** BRENT read this print 7/23 AM and already adjudicated it (STATUS banner: "Boundary #3 rescission FAILED... WTI dislocation risk re-opens"). No new information for BRENT; this dispatch closes the BOARD/info-leg gap, not BRENT's.

**LIQUID (info):** WTI delivery-point dislocation = funding/basis-relevant if a hub squeeze develops. LIQUID's last activity predates the 7/22 release. Note the June first-fire likely never reached you either (no BOARD record existed).

**HENRY (info):** WTI structure dislocation macro read; pairs with the 10Y at YTD highs + Brent >$100 inflation-repricing tape.

**RED (info, pull-complete §3.5 — BOARD-diff is your delivery):** RED-FT-03 (BRENT-PAPER >130) and RED-FT-04 (<75) both far; this is the physical-tightness leg of the oil complex, relevant to steelmanning "premium vs physical" on the $100 print.

## AIGs / cross-refs

- SIG-W-20260618-004 (Cushing AT the bottom, 20.03M — the near-trigger dispatch that pre-registered this fire path)
- SIG-W-20260702-005 (Dario forced tank-bottom refill counter-read vs BRENT reopening-barrels)
- SIG-W-20260721-005 (SPR 70M INOCULATION — §6241 statutory floor 252.4M stands; SPR now 311.4M)
- BRENT STATUS 7/23 (current, holds this print + adjudication)

## Provenance

- Intake: RESEARCH-INTAKE lane NEW-breach flag (onset-dedup: key cleared at wk-7/10 >20M, re-appeared = fresh onset) + 6c boot scan confirmation
- Pipeline: lane flag → dashboard EIA confirm → BRENT-current check (owner-ahead confirmed) → re-fire per Boundary #3 re-cross convention → IMMEDIATE dispatch
- No verify-spawn: primary-data class (EIA series), two independent tool paths + owner convergence
