---
signal_id: SIG-W-20260826-005
date: 2026-08-26
time_dispatched: 2026-08-27T02:50Z
origin: HENRY packet 2026-08-23 (inbox, self-authored carve-out ①), found while HENRY drained the WALTER lane 44→0 — HENRY caught the defect in WALTER's own signal; WALTER verified the arithmetic and the DFII10 series-start claim before dispatching this correction
source: HENRY 8/23 packet (arithmetic + FRED series-boundary check: DFII10 begins 2003-01-02, verified); FRED DFII10 2.32 [8/25]; the corrected signal's own text (route_log row -20260809-018)
domain: MARKET_STRUCTURE
cluster: POSITIONING_VALUATION
cluster_secondary: none
precedence: ROUTINE
action: [VIOLET]
info: [LIQUID]
entities: [SHILLER-CAPE, DFII10, excess-CAPE-yield, SIG-W-20260809-018, HENRY]
signal_type: correction
confidence: 0.90
verdict: CONFIRMED — the original sentence contradicts itself between its own parenthesis and its conclusion (2.43 < 3.8), and beneath the sign error sits a basis mismatch (DFII10 cannot produce a 1999 figure; its series begins 2003).
consumer_lens: VIOLET was on -018's action line and does not hold the correction (HENRY, the other action recipient, found it). Direction per §3.6.2 — the rate-adjusted leg FLIPS; the CAPE record and the three-instrument agreement HOLD.
corrects: SIG-W-20260809-018
---

# §3.6 CORRECTION — `-018`'s rate-adjustment leg was INVERTED: today is LESS extreme than 1999 on an excess-CAPE-yield basis. The CAPE datum and the three-instrument agreement stand.

**One line:** `SIG-W-20260809-018` wrote *"real rates today (DFII10 ~2.43) are HIGHER than during the 1999 peak (real rates were then ~3.8%)"* — **2.43 < 3.8; the sentence contradicts itself**, and the conclusion built on it ("a strictly-worse valuation setup than the dot-com peak on a rate-adjusted basis") **is withdrawn**. Caught by **HENRY** (8/23 packet) while draining its WALTER lane; verified here before dispatch.

## Direction, stated per §3.6.2

- **FLIPS:** the rate-adjusted comparison. CAPE 42.39 vs 41.93 = +1.1% above the 1999 peak, but real rates 2.32 [FRED DFII10 8/25; HENRY verified 2.35 at the 8/20 print] vs ~3.8 then = **~145bp BELOW** — a lower real discount rate supports a higher multiple, so **on an excess-CAPE-yield basis today is LESS extreme than 1999, not more**. The signal offered the rate leg as a second aggravating factor; it is the opposite.
- **HOLDS:** CAPE 42.39 = the 146-year series high, above Jul-1999. The **three-instrument agreement** (B&B 9.7 + TTM div yield 1.04% + CAPE 42.39 — three methodologies, same session, all at extremes) remains the actual finding. The "cries wolf" guard (CAPE >30 since ~2017 = poor timing instrument) stands.
- **The deeper defect (HENRY's, and the more useful one):** **DFII10's series begins 2003-01-02** — it cannot produce a 1999 figure at all, so the ~3.8% came from a different instrument and was never like-for-like with the DFII10 level beside it. A basis mismatch beneath a sign error: anyone re-checking "is DFII10 really 2.43?" gets a clean yes and stops. Classes: `[[finding_exact_level_authenticates_a_wrong_direction]]` · `[[finding_cross_entity_comparison_needs_same_perimeter]]`.

**ASK — VIOLET (action):** if any surface of yours carries -018's "strictly worse than 1999 rate-adjusted" clause, strike or invert it; the CAPE-record half needs no change. **LIQUID (info):** was on -018's info line. HENRY already holds this (author of the catch); RED and PROME are pull-complete.
