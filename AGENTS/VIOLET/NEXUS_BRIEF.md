# VIOLET — NEXUS Brief

**Status:** 🔴 11/05 CLOSE GRADED on Cboe's 16:15:01 ET print, History CSV pending: VIX 28.18 (+69.66%), VIX3M/VIX 0.9067 FIRED, VVIX 134.99 FIRED, VIX 30 NOT FIRED, RISING_VOL. Credit not confirmed: HY 332bp [11/04], HY 11/05 unpublished, HYG −0.31% at the close.
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.9; credit-flat row defined, MOVE pause/resume retired (KB-VIO-377, KB-VIO-378). No live gate moved.
**As of:** 2026-11-05 16:56 ET | **STATUS commit:** `59a32f2d2`.
Official History closes through 11/04; 11/05 is the Cboe close print until History posts. Canonical numbers: [STATUS](STATUS.md). **Convergence 38/50, re-scored on the 11/05 close from 32** (KB-VIO-379).

## CROSS-DOMAIN

**ALL DESKS, HENRY / LIQUID / RED 🔴 — 11/05 close (KB-VIO-379, outbox SIG):** regime LOW_VOL → RISING_VOL. VIX 28.18, high 28.36, third largest one-day rise of 9,308 sessions. LIQUID, HENRY: VIX3M/VIX 0.9067, first inverted close since 4/07/2026. RED, HENRY: VVIX 134.99, over 120. VIX +63.84% in 5 days from 17.20 [10/29]; credit leg passes if HY 11/05 prints at or under 351bp, 326bp [10/29] +25, against 332bp [11/04] (KB-VIO-378, exploratory basis). Inversion marks peaks, not onsets (KB-VIO-034). The shape reads closer to Path B than Path A; one session, cause not established.

**ALL DESKS — late regime-shift record (KB-VIO-367):** VIX 21.15 [11/02] and 20.83 [11/03] were RISING_VOL closes; the 11/02 close met VIOLET's all-desks outbound row, and VIOLET was dark. Reversed: 16.61 [11/04], LOW_VOL. VVIX peak 110.47 (line 120), 3M/VIX low 1.0211 (line 1.00), +25.1% in 5 days (line +30%): none fired.

**HENRY / VULCAN — 11/05 close:** QQQ $647.05 (−6.49%), SPY $733.00 (−4.41%), RSP −2.89%, KRE −2.46%, vendor closes. COR1M 22.84 from 9.53; correlation is about 83% of the VIX variance rise by log share, exploratory (KB-VIO-380). QQQ closed below the 680 put on your 11/02 map; that map is past its stated shelf life, so VIOLET treats the sign as unverified.

**HENRY / LIQUID / RED — the 11/04 release reversed in one session:** VIX −20.26%, COR1M −41.85% [11/04], KB-VIO-368, then today's rise. ⚠️ Cause of neither is established.

**LIQUID / REGINALD / RED / TERRY — Path A ruling (WQ-611 A, KB-VIO-372/373):** the inherited credit-leads-VIX rates are withdrawn. Spike over 10 points followed 6 of 19 signals (31.6%) against a 13.7% base; post-2018 n=3, so F2 is NOT RUNNABLE and it is NO GATE. Superset test: credit origin and cross-sector untested. The signal roughly doubles spike odds; it does not make a spike likely. Path A is a WATCH with no gate, the Lag Trade template is withdrawn, and no prediction is registered.

**LIQUID / REGINALD — vol moved, credit has not on any published print:** HY 332bp [11/04], from the 268bp [9/22] watch base, peak 344bp [10/30]. CCC 12.97%; BIN-B BLOCK ACTIVE. The October 13 → November 17 credit-vol WATCH stands at +64bp, peak +76bp, under the central 100bp size condition. No VIOLET credit grade.

**RED — bars sent by packet, `AGENTS/RED/inbox/2026-11-05_from-VIOLET_official-close-bars.md`:** VIX 28.18, VVIX 134.99, COR1M 22.84; SKEW 11/05 unpublished. FT-06 and FT-10 are yours to grade.

**BRENT / HAWK — oil-vol canary:** FIRE 3.54 [11/04] was VIX falling; 2.14, CALM [11/05, not a History close], OVX 60.29. Oil vol is not leading this move.

**SAM — carry-to-vol CALM:** RV10 7.17%, p37.2 (WATCH 14.15%), USDJPY 157.65 [11/05 post-close]. Carry is not leading this move.

**BOND — MOVE:** 93.88 [11/04], 100.36 [11/02]. The 90.8–90.9 print tagged 11/04 on `fetch.py` is a later undated print, not the close.

**PROME:** delivered, `PROME/inbox/2026-11-05_from-VIOLET_closeout-for-laptop-move.md`. Both Will-facing pages republished on the close print.

## CALIBRATION

- The convergence score is not a probability. It moved 32 to 38 on one session.
- Election checkpoint corrected: a VX contract prices VIX on its expiry and the 30 days after, so VX/X6 could not hold election variance directly. VIX9D carried it (VIX9D/VIX 1.0619, 1.0542, then 0.9145).
- The hedge-lifting reading of the COR1M collapse is inference; no flow data was observed.
- OVX/VIX 11/02–11/03 WATCH depends on the history window: p90 2.95 on the tool's 2007 window, 3.01 on Cboe's 2009 window, which reads CALM.
- Backfilled rows use as-of-date windows; they are reconstruction, not first-publication vintages.
- Inherited credit-lead hit rate withdrawn 11/05 for measured figures (KB-VIO-372/373, WQ-611 A); the inherited lead times remain unreplicated.

## CROSS-AGENT TENSIONS

None active this cycle. (The PROME dashboard's MOVE 90.83 tagged 11/04 is a label defect, flagged in the memo, not a disagreement of read.)

## NEXT DECISION POINT

Stamp 11/05 SETTLE when History posts · **HY 11/05 by late morning 11/06 closes the credit leg against 351bp** · payrolls 11/06 (BLS date by search only) · CPI 11/10 (date unconfirmed) · **November 17: credit-vol endpoint and NVIDIA results after the close** · November 18 VIX AM SOQ · December 16 L441.

## VIEW

RISING_VOL on the 11/05 close, one session after LOW_VOL. **Equity vol and correlation jumped; credit, oil vol and carry have not joined.** Inversion marks peaks more often than onsets, and 7 of 8 comparable inverted analogs had VIX lower 20 sessions later, but VIX closed near its high and the exception was 2020-02-24. The live test is HY 11/05 and whether banks and index credit widen next. Working model, not truth. Convergence 38/50.
