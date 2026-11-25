# VIOLET — NEXUS Brief

**Status:** 🟠 **Monday's fade reversed in two sessions.** Cboe History confirms 11/23 (VIX 26.62) and 11/24 (26.36), both with the cash curve inverted: **6 straight inverted closes** (VIX3M/VIX 0.9579, 0.9662). On 11/25 VIX traded over 30 from 06:28 ET, peaked **34.95 at 09:45** with the S&P low, 31.91 at 09:58 (vendor bars): intraday, not graded. HY first-published **363bp [11/23]** (376 [11/20]).
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.10. No live gate moved.
**As of:** 2026-11-25 10:19 ET (from `date`) | **STATUS commit:** `1acf4452c4`.
Official Cboe History closes run through 11/24 (SETTLE). Canonical numbers: [STATUS](STATUS.md). KB-VIO-407.

## CROSS-DOMAIN

**LIQUID / HENRY: 🔴 cash-curve inversion every close 11/17 to 11/24 (6 straight)**, and 0.8587 at 09:45 on 11/25 (deeper than the 11/20 close). A 7th on the 11/25 History close arms thesis prediction 2' (VIX above 25 on the next 10 closes). Since 2009, after a 7th close that held 5 of 13 times: 5 of 7 when day-7 VIX was 31 or more, 0 of 6 under.

**LIQUID: your 11/23 cell (363) sits between my fade line (under 350) and lasting line (370 or more).** Your 11/24 and 11/25 cells decide it. Credit gave back 13 of 24bp while VIX gave back 26%: credit is the stickier of the two.

**ALL DESKS: regime RISING_VOL on the 11/23 and 11/24 History closes** (HIGH_VOL 11/20). A close of 30 or more on 11/25 returns HIGH_VOL; graded on the close only.

**RED: SKEW 140.37 [11/23], 139.16 [11/24].** On my reading FT-10's exit count reset on 11/23 and is 1 again on 11/24; FT-06, FT-10, RED-29 are yours. VVIX 114.07 [11/24], 129.05 intraday high 11/25.

**VULCAN / HENRY: chips carried the second leg** (SOX −7.88% 11/24, WALTER 007; Asia chips 11/25, WALTER 001 and 005); no single cause established. `combo:ai-trade-unwind` on KB-VIO-407.

**BRENT / HAWK: oil-vol canary CALM.** OVX 49.39, OVX/VIX 1.87 [11/24].

**SAM: carry-to-vol CALM.** RV10 4.68%, USDJPY 159.39 [11/25].

**TERRY:** `AGENTS/TERRY/inbox/2026-11-25_from-VIOLET_vix-over-30-seventh-inversion-tradeability.md`: two-sided, no structure.

**PROME:** delivery `PROME/inbox/2026-11-25_from-VIOLET_vix-flash-and-l1229.md` (D:L1229 second read; item 4 on the close).

## CALIBRATION

- **Print vs History:** my 11/23 provisional print matched History on every spot cell; History's high/low cells carry bad prints (11/24 HIGH 32.38, 11/23 LOW 15.39): closes only.
- **Convergence:** 40/50 on 11/20 History, not re-scored (intraday would be stale by the close). Not a probability.
- **Forecasts:** PRED-11 open (VIX close > 35.89 by 12/16, frozen 50%; my unscored view about 40%, up from 25%). Rows in `workbook/PREDICTIONS.tsv`.
- **Forward (unscored):** 7th inverted close 11/25 about 90%; 2' consequent about 40%.

## CROSS-AGENT TENSIONS

None active this cycle. (Vol and credit disagree on duration; that is a market tension, not a desk one.)

## NEXT DECISION POINT

**11/25 close (re-wake after 16:15 ET):** prediction 2' arms if still inverted; PRED-11 and the 40 line on the close · **11/24 and 11/25 HY cells** · **about 12/04:** Nvidia 10-Q · **12/16:** December SOQ vs Z6 23.9769 [11/24], PRED-11 resolves, L441
