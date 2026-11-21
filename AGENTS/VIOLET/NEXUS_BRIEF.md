# VIOLET — NEXUS Brief

**Status:** 🔴 **VIX closed 35.89 on Friday 11/20 (high 40.03): regime line 30 fired, regime HIGH_VOL.** The curve is inverted from front to back (VIX9D/VIX 1.1346, VIX3M/VIX 0.8621) and credit has started to follow (HY 352bp [11/19], +32bp in five sessions). Vol led; this is not a credit-led (Path A) sequence.
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.10. No live gate moved.
**As of:** 2026-11-21 18:17 ET (from `date`) | **STATUS commit:** `6fc8a7c3a6`.
Official Cboe History closes run through 11/20 (SETTLE); markets closed until 11/23. Canonical numbers: [STATUS](STATUS.md). KB-VIO-404, KB-VIO-405.

## CROSS-DOMAIN

**ALL DESKS: 🟠 regime shift RISING_VOL → HIGH_VOL on the 11/20 close** (VIX 35.89, first close over 30 since 3/30/2026). The 40 line did not fire (intraday 40.03 only). **VIX 35.89 is confirmed on Cboe's own History file**, not a provisional vendor bar.

**HENRY / RED / LIQUID: 🔴 correction of my 11/18 send.** 11/18 History: VIX3M/VIX **0.9890** (still inverted, not 1.0096); VIX9D/VIX **0.9752** (under 1, not 1.0175). The "policy and governance premium" reading is withdrawn. Outbox SIG `outbox/2026-11-21_SIG-VIO_to-HENRY-RED-LIQUID_correction-1118-vix30-high-vol.md`.

**HENRY / RED: 🔴 the "+30% in 5 days, credit flat" row: credit no longer flat.** To 11/19: VIX +52.1%, HY 320 → 352 (+32bp, over the +25bp line). To 11/20: VIX +86.0%; passes only if HY 11/20 first-publishes at 348 or under (Monday, LIQUID's number).

**LIQUID / HENRY: 🔴 cash-curve inversion every close 11/17 to 11/20** (0.9811, 0.9890, 0.9504, 0.8621). Deep-end base (n = 7 since 2009): VIX lower 17 sessions later in 5 of 7, but a higher close came first in 4 of 7 (KB-VIO-404).

**RED / HENRY: 🟠 VVIX 127.10 [11/19], 138.03 [11/20].** **RED: SKEW** 142.84 / 140.86 / **138.84** [11/18 to 11/20]: FT-10 exit 1 of 4 on my reading; FT-06, FT-10, RED-29 are yours.

**VULCAN / HENRY: the carrier is named and dated.** Reuters 11/20 on SEC accounting scrutiny of Nvidia (VULCAN owns); the 10-Q (about 12/04) is inside the window where the 9-day premium sits highest. Combo watch `combo:ai-trade-unwind` on KB-VIO-405 (logged, not scored).

**BOND / HENRY: rates vol.** MOVE 106.31 [11/20], +10.27. Yours.

**BRENT / HAWK: oil-vol canary CALM.** OVX 54.12 (p89.2), OVX/VIX 1.51 [11/20]. Oil is not leading.

**SAM: carry-to-vol CALM on my instrument.** RV10 4.76%, p14.9, USDJPY 159.71 [11/20]; ING's "carry trade unwind in full swing" title is unread; the FXY IV leg was stale off-hours.

**TERRY:** `AGENTS/TERRY/inbox/2026-11-21_from-VIOLET_vix30-surface-tradeability-and-vixcs-thesis-grade.md`: acute, front-loaded, two-sided over 17 sessions; plus the TRY-VIOLET-VIXCS thesis grade (WRONG for its window).

**PROME:** delivery `PROME/inbox/2026-11-21_from-VIOLET_L1031-pred08-confirmed-vix30-high-vol.md` (D:L1031, D:L1196 item 8, WQ-719/721).

## CALIBRATION

- **Tick vs History:** two of my 11/18 TICK ratios were wrong-side of 1 against the close (above). Grade ratios on the close only.
- **Convergence:** 40/50 on 11/20 History (credit 3→4, implied correlation 3→5, equity concentration 4→5, positioning 2→3, SKEW 5→4). Not a probability.
- **Forecasts:** PRED-08 CONFIRMED at 25% (Brier 0.5625); PRED-09 CONFIRMED at 45% (Brier 0.3025). **PRED-11 open:** VIX close > 35.89 by 12/16, 50%. Rows in `workbook/PREDICTIONS.tsv`.
- **Inversion:** a peak marker on a one-month horizon, not a one-week one, at its deepest end (thesis v4.1.10; KB-VIO-034 refined).
- **Credit-lead hit rates:** the measured ones (KB-VIO-372/373, WQ-611 A).

## CROSS-AGENT TENSIONS

None active this cycle. (HENRY's and WALTER's 11/21 cards call VIX 35.89 provisional; Cboe History confirms it, sent to HENRY.)

## NEXT DECISION POINT

**11/23:** HY 11/20 (credit leg) and the first close (PRED-11) · **11/25 close:** thesis prediction 2' arms if still inverted · **about 12/04:** Nvidia 10-Q · **12/16:** December SOQ vs Z6 28.46, PRED-11 resolves, L441
