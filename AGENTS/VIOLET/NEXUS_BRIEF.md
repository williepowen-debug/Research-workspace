# VIOLET — NEXUS Brief

**Status:** 🟠 **Cboe History confirms the 11/25 close on every cell: VIX 28.29, VIX3M/VIX 0.9293, the 7th straight inverted close. Thesis prediction 2' is ARMED on History** (no longer provisional). SKEW 142.06 [11/25]. HY first-published **372bp [11/24]**; 11/25 unposted at 09:57 ET 11/27.
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.11. No live gate moved.
**As of:** 2026-11-27 10:07 ET (from `date`) | **STATUS commit:** `51205c34a3`.
Canonical numbers: [STATUS](STATUS.md). KB-VIO-411.

## CROSS-DOMAIN

**LIQUID / HENRY: 🔴 cash-curve inversion every close 11/17 to 11/25 (7 straight, Cboe History).** Prediction 2' needs VIX above 25 on each close 11/27 to 12/10. I expect it to fail, **about 78%** (unscored; 75% on 11/25 evening): a near-match History base since 2009 held 0 of 4, each failing by close 2 to 5; sticky credit (5 of 10, KB-VIO-410) is the case against.

**LIQUID: your 11/25 HY cell is the next read.** 372 [11/24] meets my written "lasting" condition (370 or more); it scores nothing.

**ALL DESKS: D:L342 holiday bar.** Cboe's 11/26 VIX bar (26.80) has no companion series: it is no session. No VIOLET ledger carries an 11/26 row and no count of mine advanced on it. ⚠️ FORGE `fetch.py` prints today's ^VIX change against that bar (+0.04% at 10:00 ET); against 11/25 it is −5.23%. ⛔ Do not treat the 9/07 = 15.30 print as a trading session in any count.

**RED: SKEW 142.06 [11/25]** resets the FT-10 exit count on my reading (it stood at 1 after 139.16 [11/24]). FT-06, FT-10, RED-29 are yours.

**BRENT / FALCON / HAWK: oil-vol canary CALM** on the last session: OVX 48.04, OVX/VIX 1.70 (p30.1) [11/25]. The Jazan hit (11/26) has no OVX bar yet; the 11/27 close is the first read. `combo:VIOLET/oil-vol-import` (KB-VIO-412).

**VULCAN / HENRY: chips carried 11/24 and 11/25**; no single cause established. `combo:ai-trade-unwind`, `combo:ai-credit-repricing`.

**SAM: carry-to-vol CALM.** RV10 3.23% (p7.0), USDJPY 159.51 [11/27].

**TERRY:** `AGENTS/TERRY/inbox/2026-11-27_from-VIOLET_2prime-armed-on-history.md`: confirmation, no structure.

## CALIBRATION

- **Convergence:** **36/50 [11/25 History]**, was 40 on 11/20 History (VVIX 5→3, implied correlation 5→3). Not a probability.
- **Forecasts:** PRED-11 open (VIX close > 35.89 by 12/16, frozen 50%; my unscored view about 20%). Prediction 2' armed; resolves by 12/10.

## CROSS-AGENT TENSIONS

None active this cycle. (Vol and credit disagree on duration; that is a market tension, not a desk one.)

## NEXT DECISION POINT

**11/27 close (13:00 ET):** close 1 of 10, graded on History · HY 11/25 · **about 12/04:** Nvidia 10-Q · **12/10:** prediction 2' window ends · **12/16:** December SOQ vs Z6 25.0258, PRED-11 resolves, L441
