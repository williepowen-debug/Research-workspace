# VIOLET — NEXUS Brief

**As of:** 2026-09-28 20:50 ET (`date`), post-close, graded on the **September 28 close** (Cboe delayed-quote; Cboe history confirmed through 9/25). **STATUS commit:** `d179af27b`. Framework v4.1.1 (**unchanged**). Numerical dashboard: [STATUS](STATUS.md). Dark 9/25 03:00 → 9/28 20:39 ET; this cycle covers Fri 9/25 + Mon 9/28.

## CROSS-DOMAIN

🔴 **LIQUID / HENRY / RED: credit widened in every bucket while VIX stayed under 20 (KB-VIO-313).**
- FRED OAS 9/22 → 9/25: HY **2.68 → 2.93** (+25bp) · B 2.71 → 3.00 · BB **1.56 → 1.76** · CCC **10.75 → 11.28** (+53bp) · IG 0.77 → 0.81. **My 9/24 brief said "only CCC moved"; that was true on 9/23 FRED and is SUPERSEDED.**
- On 9/25, HY's biggest day (+13bp), **VIX fell 15.67 → 14.87 (−5.1%)**; VIX then 16.07 [9/28].
- Read against my central claim: VIX <20 ✅ · cross-sector ✅ · curve not inverted ✅ (2s10s +36bp, 9/25) · **credit-originated ❓** — widening began 9/23, the same session as the rates move (WALTER SIG-003: real-yield-led). Size ≈ ¼ of the claim's 100bp. Hit rates are inherited, not VIOLET-reproduced. **WATCH, not a Path-A fire. No threshold set.** LIQUID owns the credit read.

🟠 **LIQUID / VULCAN / NEXUS: GATE-LIQ-069 2-of-2, my Path-B leg (KB-VIO-315): no Path-B vol fire.** Path B = index vol fires *without* credit; now credit moves and index vol doesn't — the opposite shape. Dispersion precondition present: COR1M 9.03, constituent-vol [EST, direction-only] 47.0 [9/17] → 53.5 [9/28]. Read under WQ-301: CoreWeave ≈847bp **MODEL-DERIVED**; observed **11.82pt upfront** on 500bp [9/24]; ISDA gap UNMEASURED.

🔴 **HENRY / BOND: rates vol held.** MOVE 104.58 [9/24] → 96.00 [9/25] → **101.82** [9/28]. 10Y 5.17 [9/25 FRED]. Equity vol: VVIX **91.02** (highest since the Fed), VIX3M/VIX **1.1344** (flattest since 9/16, contango). Spread, not lead-lag — same framing as 9/24.

🟠 **LIQUID (Q2, L477): transmission test NOT FIRING, 3 of 10 sessions.** `VIX3M/VIX ≤1.00 AND VVIX >120` × 2 closes, window to **10/7**. None of disconfirmers (a)–(d) met.

🔴 **BRENT / HAWK:** OVX **56.11**, ratio 3.49 p97.1, FIRE since 9/18. Substance yours.

🟢 **SAM:** JPY RV10 7.03% p33.6 CALM; USDJPY 157.46.

**RED:** SKEW Cboe bars 9/24 **146.04** · 9/25 **144.91** · 9/28 146.25 [dq]. None ≥150 since 9/15. RED owns FT-10. RED-FT-06: VIX 16.07.

**PROME:** COR1M first-tell (KB-VIO-188) **FIRED 9/2, ungraded until tonight** (KB-VIO-314) — second registered line lost to memory-based grading (after KB-VIO-231). Mechanization asked.

## CALIBRATION

- ⭐ **A "only X moved" read expires with its data date.** 9/24's CCC-only framing was right on 9/23 FRED and wrong two prints later. The cross-sector condition is the one the central claim needs, so carrying the old read would have hidden the one condition that changed.
- ⭐ **A gate row deleted in a rewrite is invisible to every later session.** The COR1M first-tell fired the same day its STATUS row was dropped. No grader, no row, 26 days. Registered mechanical lines need a code grader at boot.
- ⭐ **`cftc_cot.py --boot` showed the 9/15 report after the 9/22 one was out**; a plain run fetched 9/22. Cause not yet diagnosed.
- **Unrecoverable dark-day rows:** OVX, JPY_VOL, IMPLIED_CORR have no 9/25 row (scripts have no dated backfill; COR1M recovered via prev_close only).
- Standing: RQ #8 PARKED — ***"The corrected ten-event sample does not establish a forward VIX signal in either direction."***

## CROSS-AGENT TENSIONS

None active this cycle. (My 9/24 "only CCC moved" is superseded by my own read above, not contested by LIQUID.)

## FORWARD CATALYSTS

Canonical: [CATALYSTS](workbook/CATALYSTS.tsv). Wed 9/30 MU FQ4 (cheap-tail catalyst) · Fri 10/2 CFTC (report 9/29, expected) · **Wed 10/7 Q2 window closes** · Wed 12/16 M1:M2 re-check.

## VIEW

- Book **FLAT**; $0; no proposal. Convergence **28 → 29/50** (credit 3 → 4).
- Regime **LOW_VOL** (16.07). The story is now **rates + credit moving with equity vol lagging both**. Cheap-tail read 4/4 on Friday's close and is likely 2/4 once Cboe posts 9/28. Operator surface only.
- WQ-259 done: both Will-facing artifacts republished to their standing URLs (v7).
