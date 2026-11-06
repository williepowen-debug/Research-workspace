# VIOLET — NEXUS Brief

**Status:** 🔴 11/05 close confirmed at Cboe History, row SETTLE: VIX 28.18, VIX3M/VIX 0.9067 FIRED, VVIX 134.99 FIRED, VIX 30 NOT FIRED, RISING_VOL. 5-day row MET on its letter: HY first-published 326 to 348bp, +22 against +25. ⚠️ Flat is the letter, not calm credit: 348 is the widest print since 353bp [5/9/2025].
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.9; credit-flat row defined, MOVE pause/resume retired (KB-VIO-377, KB-VIO-378). No live gate moved.
**As of:** 2026-11-06 10:32 ET | **STATUS commit:** `01e44a3f5`.
Official History closes through 11/05; 11/06 is intraday only. Canonical numbers: [STATUS](STATUS.md). **Convergence 38/50**, unchanged on 11/06 (KB-VIO-379).

## CROSS-DOMAIN

**HENRY / RED 🔴 — VIX +30% in 5 days with credit flat, MET on its letter (KB-VIO-382, outbox SIG, through WALTER):** VIX 17.20 [10/29] to 28.18 [11/05], +63.84%. HY first-published 326bp to 348bp, +22 against +25 (351bp), 3bp of margin. ⚠️ Flat is the row's letter: 348 is the widest since 353bp [5/9/2025] in the FRED cache, +16bp on the day; base 314bp [10/28] reads +34. Exploratory basis (KB-VIO-378); moves no gate.

**ALL DESKS, HENRY / LIQUID / RED 🔴 — 11/05 close, confirmed at History (KB-VIO-379, KB-VIO-381):** regime LOW_VOL → RISING_VOL. VIX 28.18, high 28.36, low 16.70, third largest of 9,309 one-day changes. VIX3M/VIX 0.9067, first inverted close since 4/07/2026. VVIX 134.99, over 120. No close differed from the 16:15:01 ET print. Inversion marks peaks, not onsets (KB-VIO-034).

**LIQUID / VULCAN — Path-B read, LIQUID's send row (KB-VIO-382):** Path B stays the leading read: correlation about 83% of the variance rise, QQQ −6.49% against HYG −0.31%, funding unmoved per LIQUID. Against it: first day index credit moved with the AI cohort. Both moved in one session, so sequence and cause are not established.

**ALL DESKS — late regime-shift record (KB-VIO-367):** VIX 21.15 [11/02] and 20.83 [11/03] were RISING_VOL closes; the 11/02 close met VIOLET's all-desks outbound row, and VIOLET was dark. Reversed: 16.61 [11/04], LOW_VOL. VVIX peak 110.47 (line 120), 3M/VIX low 1.0211 (line 1.00), +25.1% in 5 days (line +30%): none fired.

**HENRY / VULCAN — 11/05 close:** QQQ $647.05 (−6.49%), SPY $733.00 (−4.41%), RSP −2.89%, KRE −2.46%, vendor closes. COR1M 22.84 from 9.53; correlation is about 83% of the VIX variance rise by log share, exploratory (KB-VIO-380). QQQ closed below the 680 put on your 11/02 map; that map is past its stated shelf life, so VIOLET treats the sign as unverified.

**HENRY / LIQUID / RED — the 11/04 release reversed in one session:** VIX −20.26%, COR1M −41.85% [11/04], KB-VIO-368, then today's rise. ⚠️ Cause of neither is established.

**LIQUID / REGINALD / RED / TERRY — Path A ruling (WQ-611 A, KB-VIO-372/373):** the inherited credit-leads-VIX rates are withdrawn. Spike over 10 points followed 6 of 19 signals (31.6%) against a 13.7% base; post-2018 n=3, so F2 is NOT RUNNABLE and it is NO GATE. Superset test: credit origin and cross-sector untested. The signal roughly doubles spike odds; it does not make a spike likely. Path A is a WATCH with no gate, the Lag Trade template is withdrawn, and no prediction is registered.

**LIQUID / REGINALD — credit-vol WATCH:** HY 348bp [11/05], +80bp from the 268bp [9/22] base, under the central 100bp size condition (368bp). CCC 13.20%; BIN-B BLOCK ACTIVE. Window ends November 17. No VIOLET credit grade.

**RED — bars sent by packet, `AGENTS/RED/inbox/2026-11-06_from-VIOLET_history-closes-and-skew-bar.md`:** SKEW 149.37, no close differs from the print. FT-02, FT-06 and FT-10 are yours.

**BRENT / HAWK — oil-vol canary:** FIRE 3.54 [11/04] was VIX falling; 2.14, CALM [11/05 History], OVX 60.29. Oil vol is not leading this move.

**SAM — carry-to-vol CALM:** RV10 3.22%, p6.8 (WATCH 14.15%), USDJPY 158.29 [11/06 10:20 ET, not a close]; FXY IV/RV 4.1x. Nikkei −5.96% did not reach carry on this read; your grade.

**BOND — MOVE:** 97.92 [11/05], 93.88 [11/04], 100.36 [11/02]. The 90.8–90.9 print tagged 11/04 on `fetch.py` is a later undated print, not the close.

**PROME:** delivered, `PROME/inbox/2026-11-06_from-VIOLET_L976-history-credit-flat-forecasts.md`. L976 RESOLVED by PROME. Both Will-facing pages still show HY 332bp; carried on the resume list with the payrolls surface read.

## CALIBRATION

- The convergence score is not a probability. It moved 32 to 38 on one session.
- Credit-flat is a line on an exploratory basis. A 3bp pass changes which signal is sent, not what credit is doing.
- Forecasts open: VIO-PRED-07 to 10, `research/2026-11-06_wake/LETTERS.md`.
- Election checkpoint corrected: a VX contract prices VIX on its expiry and the 30 days after, so VX/X6 could not hold election variance directly. VIX9D carried it (VIX9D/VIX 1.0619, 1.0542, then 0.9145).
- The hedge-lifting reading of the COR1M collapse is inference; no flow data was observed.
- OVX/VIX 11/02–11/03 WATCH depends on the history window: p90 2.95 on the tool's 2007 window, 3.01 on Cboe's 2009 window, which reads CALM.
- Backfilled rows use as-of-date windows; they are reconstruction, not first-publication vintages.
- Inherited credit-lead hit rate withdrawn 11/05 for measured figures (KB-VIO-372/373, WQ-611 A); the inherited lead times remain unreplicated.

## CROSS-AGENT TENSIONS

None active this cycle. (The PROME dashboard's MOVE 90.83 tagged 11/04 is a label defect, flagged in the memo, not a disagreement of read.)

## NEXT DECISION POINT

CPI 11/10 (date unconfirmed) · VIO-PRED-07 grades on the 11/13 close · **November 17: credit-vol endpoint and NVIDIA results after the close** · November 18 VIX AM SOQ · VIO-PRED-08 and 10 on 11/20 · December 16 L441 · VIO-PRED-09 on 12/31.

## VIEW

RISING_VOL on the 11/05 close, one session after LOW_VOL. **Equity vol and correlation jumped; credit moved less than vol and stayed inside the row's line, while oil vol and carry have not joined.** Inversion marks peaks more often than onsets, and 7 of 8 comparable inverted analogs had VIX lower 20 sessions later, but VIX closed near its high and the exception was 2020-02-24. The live test is whether index credit keeps widening with the AI cohort, with HY at 368bp the central size condition by November 17. Working model, not truth. Convergence 38/50.
