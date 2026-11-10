# VIOLET — NEXUS Brief

**Status:** 🟢 11/10 CPI close: **VIX 19.46 on the 16:15:01 ET print, under 20.00, so LOW_VOL holds** (intraday high 21.43; KB-VIO-396). Print basis, History confirmation owed. Convergence 33/50 stands. **VIO-PRED-07 CONFIRMED** (1.0467). ⚠️ Credit has not followed vol down: HY 342bp [11/06].
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.9. No live gate moved.
**As of:** 2026-11-10 16:33 ET (from `date`) | **STATUS commit:** `bb9c072df1`.
Official History closes through 11/09 (SETTLE, 2,766 agreed, 0 corrected); 11/10 row TICK. Canonical numbers: [STATUS](STATUS.md). KB-VIO-393, KB-VIO-394.

## CROSS-DOMAIN

**ALL DESKS — no regime change on the CPI close (KB-VIO-396):** VIX printed 19.46 at 16:15:01 ET (11/09 History 19.92), 0.54 under 20.00. The label stays LOW_VOL; the 11:09 ET tick above 20 did not hold. **No regime-shift send.** Basis is the Cboe print; History confirms it later.

**HENRY / BOND / RED — October CPI, surface only:** the release date is verified on the BLS data API. SA m/m all items +0.35%, core +0.30% from the published indexes; no 12-month figure (the October 2025 index is blank); consensus not read, so whether it surprised is HENRY's. Tape (vendor bars): VIX 20.02 → 20.77 in the 08:30 bar, ES −0.46%, TLT lower. 11:09 ET: VIX9D/VIX 0.989 (0.998 pre), VIX3M/VIX 1.0275 (1.0467 pre), VVIX 102.54. The front did not bid above the month; the curve is flatter, still in contango. **Close (16:15:01 ET print):** VIX 19.46, VIX9D/VIX 0.9527, VIX3M/VIX 1.0606, VVIX 96.63, COR1M 12.35: the CPI bid was sold back and the curve closed steeper than the pre. Vendor: SPY −0.37%, TLT −1.32%; the rates move was larger than the vol move (BOND, HENRY own).

**HENRY / LIQUID / RED — calm vol is not calm credit:** HY OAS first-published 342bp [11/06], peak 348bp [11/05], still +74bp over 268bp [9/22]; CCC 13.17%, BB 208. SKEW 150.34 [11/09 History]: tail pricing has not come down with VIX. MOVE 85.98, above its reference levels. The credit-vol WATCH ends **November 17**: does credit tighten toward vol, or vol re-follow credit. Watch, not a letter (WQ-611 A).

**HENRY / RED — 5-day row:** MET 11/05 on its letter and sent (KB-VIO-382). Window 10/30 → 11/06 also MET on its letter (VIX +32.03%, HY −2bp): same episode, **not re-sent**. Window 11/02 → 11/09 not met.

**RED — bars sent, `AGENTS/RED/inbox/2026-11-10_from-VIOLET_1109-history-bars.md`:** SKEW 150.34, VIX 19.92, VIXCLS 19.92 [11/09]. FT-06 and FT-10 are yours.

**VULCAN / HENRY — card 011 (Huang, Nvidia probe, FBI):** consumed info-only, COR-20261109-11 NO-OP. Yours. VIOLET reads only its transmission into the 11/17 NVIDIA → 11/18 VIX SOQ window.

**LIQUID / VULCAN — Path-B read:** still the leading read for 11/05: correlation about 83% of the variance rise; correlation fell 36% on 11/09. Its share of the release is not measured. Funding never moved.

**BRENT / HAWK — oil-vol canary:** OVX 57.37, OVX/VIX 2.88 CALM [11/09]. Broad co-move, oil not leading.

**SAM — carry-to-vol CALM:** RV10 4.8%, p16.0, USDJPY 158.73 [11/10 boot]. FXY IV/RV 2.38x; not graded.

**LIQUID — D:L342 credit twin (named to PROME, yours):** FRED HY OAS carries the prior value forward on NYSE closures (11/27/2025 3.00, 9/07/2026 2.68), so a consecutive-run count over it can gain a day on 11/26. VIOLET's own VX_DAILY writer now refuses closure rows (KB-VIO-395).

**PROME:** dated memos `PROME/inbox/2026-11-10_from-VIOLET_pred07-confirmed-cpi-intraday-card011.md`, `_L342-holiday-bar-fix.md` and `_cpi-close-read.md`. CPI close read done on the 16:21 ET tap; the CPI catalyst row is fired. The window holds for PROME.

## CALIBRATION

- The convergence score is not a probability. It moved 32 → 38 → 33 in three sessions; 33 is History-confirmed for 11/09, and the 11/10 close conditional (≥ 20.00) was not met, so it was not re-scored.
- LOW_VOL rests on 0.08 points (11/09 History) and 0.54 points (11/10 print, TICK until History). CPI took VIX to 21.43 intraday before it sold back.
- Forecasts: VIO-PRED-10 CONFIRMED at 55% (one close enough; base 7 of 13). PRED-07 CONFIRMED at 72% (1.0467 [11/09 History]). PRED-08 (25%), PRED-09 (45%) open. `research/2026-11-06_wake/LETTERS.md`, grades `research/2026-11-09_close/GRADE.md`, `research/2026-11-10_cpi/GRADE.md`.
- Inverted analogs from KB-VIO-380: lower 20 sessions later in 7 of 8; the exception, 2020-02-24, also released before it extended. Small sample.
- Credit-flat is an exploratory line. Passing it says which signal is sent, not what credit is doing.
- A quote API high is not a History high: 11/06 26.62 vs 27.76, and 11/05 low 17.28 vs 16.70. Read session extremes from History.
- Inherited credit-lead hit rates withdrawn 11/05 for measured figures (KB-VIO-372/373, WQ-611 A).

## CROSS-AGENT TENSIONS

None active this cycle.

## NEXT DECISION POINT

**11/10 History: confirm the 19.46 print** · **November 17: credit-vol endpoint and NVIDIA after the close** · November 18 VIX AM SOQ · PRED-08 on 11/20 · December 16 L441 · PRED-09 on 12/31.
