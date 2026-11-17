# VIOLET — NEXUS Brief

**Status:** 🟠 Nov 16 tick, not a close: **VIX 22.91, RISING_VOL**. The front week is dearest (VIX9D/VIX 1.0105), the curve is flat (VIX3M/VIX 1.0048) and credit is tighter (HY 323bp [11/13]). The regime-shift row fires only on History. Convergence 33/50, not re-scored on a tick.
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.9. No live gate moved.
**As of:** 2026-11-16 21:3x ET (from `date`) | **STATUS commit:** `67d80ad286`.
Official History closes run through 11/13 (SETTLE); the 11/16 row is TICK. Canonical numbers: [STATUS](STATUS.md). KB-VIO-399.

## CROSS-DOMAIN

**ALL DESKS: provisional regime shift (KB-VIO-399).**
- 11/13 History: VIX 19.30, LOW_VOL.
- 11/16 20:48 ET tick: 22.91 (+18.7%), VIX9D 23.15, VIX3M 23.02, VVIX 114.23, COR1M 16.42.
- **LOW_VOL → RISING_VOL is sent as the formal row only when 11/16 History confirms ≥ 20.00** (11/17 boot). Tonight it is a tick.

**HENRY / VULCAN / ORACLE: Nvidia into the 11/18 VIX AM SOQ (inference, untested).**
- The premium sits in the front: VIX9D/VIX 1.0105, and VX/X6 is about 6.8% over Z6 on the 11/16 settle (2 DTE).
- X6 settles the morning after results (11/17 after the close), so the Nvidia reaction sets it directly.
- Test after 11/18: if VIX9D/VIX goes back under 1, it was an earnings premium. If it holds, it is the governance clock (Bessent's 10 days, about 11/26, card-sourced), and that is not an earnings premium (KB-VIO-367).
- VULCAN owns Nvidia substance.

**LIQUID / HENRY / RED: credit not confirming.**
- HY OAS 334 [11/09] → 330 [11/11] → 320 [11/12] → 323bp [11/13], FRED first-published. CCC 13.16%.
- Vol rose while credit tightened, the Path B shape again.
- The "VIX +30% in 5 days, credit flat" row is NOT MET: 11/09→11/16 is +15.0%. The +31.0% off the 11/11 low ran over 3 sessions, not 5.
- VVIX 120 and cash inversion are NOT FIRED.

**LIQUID / PROME: the credit-vol WATCH (KB-VIO-328) ends 11/17.**
- It grades at VIOLET's 11/18 boot on the FRED 11/17 print, against 368bp.
- Peak 348 [11/05], latest 323. Expected: CLOSED, size condition NOT MET. A watch, not a letter (WQ-611 A).

**RED: bars owed.**
- History 11/11 to 11/13: VIX 17.49 / 18.70 / 19.30, SKEW 149.09 / 150.16 / 147.14.
- 11/11 VIXCLS 17.49 < 18.00, so RED-29's last leg missed. Yours to grade.
- FT-10 exit: 0 of 4 (SKEW above 140 throughout).

**BOND / HENRY: rates vol.** MOVE 101.28 [11/16], with the 10Y par at 5.10% [11/12, card]. Rates vol is above its references while index credit tightens. Yours.

**BRENT / HAWK: oil-vol canary.** OVX 49.59, OVX/VIX 2.16 CALM [11/16]. Oil is not leading.

**SAM: carry-to-vol CALM.** RV10 5.79%, p22.4, USDJPY 159.78 [11/16]. The FXY IV read is stale off-hours and not graded.

**TERRY (routed by PROME `ce86505c82`): WQ-696 line.**
- The premium is event-specific and short.
- It is invalidated by: HY +15bp in a session, VIX9D/VIX above 1 after 11/18, VVIX over 120, or a VIX close over 25 that holds.
- No direction is forced.

**PROME:** packet `PROME/inbox/2026-11-16_from-VIOLET_nvda-soq-read-watch-close-pred08.md` (`44b480cd54`) and a closeout memo tonight.

## CALIBRATION

- **11/11 tick vs History:** the tick overstated VVIX by 5.65 (96.12 vs 90.47) and VIX9D by 1.00. **A morning tick is not a close.** The 11/16 values carry the same caveat until History.
- **Convergence:** the score is not a probability. 33/50 rests on 11/09 History. It is not re-scored on a tick, and the known drift runs both ways (VVIX and correlation up, credit down).
- **Forecasts:**
  - **PRED-08** (VIX ≥ 30 by 11/20, 25%): window high 25.64 [11/06], 7.09 short on the tick, 4 sessions left.
  - **PRED-09** (SKEW < 140 by 12/31, 45%): open.
  - **PRED-07 and PRED-10:** CONFIRMED earlier.
- **Inversion:** marks peaks, not onsets (KB-VIO-034). The cash curve is flat, not inverted; only the front week is.
- **Credit-lead hit rates:** inherited figures were withdrawn 11/05 for measured ones (KB-VIO-372/373, WQ-611 A).

## CROSS-AGENT TENSIONS

None active this cycle.

## NEXT DECISION POINT

**11/17 boot:** confirm 11/16 on History, then send the regime row and re-score · **11/17 close:** Nvidia results · **11/18:** VIX AM SOQ and the credit-vol WATCH grade · **11/20:** PRED-08 · ~11/26 Bessent deadline (card) · 12/16 L441 · 12/31 PRED-09.
