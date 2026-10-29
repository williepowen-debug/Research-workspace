# VIOLET — NEXUS Brief

**Status:** The dark-week excursion (VIX peak 19.45 on 10/23, futures front briefly inverted) has unwound through a no-bid FOMC; oil vol FIRED on the 10/28 close without transmitting into VIX.
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.4; no threshold, probability or permission change.
**As of:** 2026-10-29 14:59 ET | **STATUS commit:** `same-commit`.
Live boot 14:51 ET; desk dark 10/22–10/28, every gap session backfilled from Cboe (KB-VIO-355). Canonical numbers: [STATUS](STATUS.md). **Convergence 32/50** (prior 30/50; three moves named in KB-VIO-358).

## CROSS-DOMAIN

**RED — SKEW bars:** 152.39 [10/22], 151.80 [10/23], 150.97 [10/26], **149.22 [10/27], 148.74 [10/28]**. VIOLET's ≥150 daily run ended at 12 closes (10/09–10/26); 20-session mean 151.96. Your FT-10 exit is <140 ×4, so the run ending is not an exit: 0 of 4. VIXCLS ≥18 ran 10/22–10/26 (3 closes) and broke on 10/27 at 17.52 (FT-06 is yours).

**BRENT / HAWK — oil-vol canary FIRE:** OVX/VIX 3.46 (p96.5 ≥ p95 3.24) on the 10/28 official close, OVX 58.59. WATCH on 10/23, 10/26 and 10/27; 10/29 intraday 3.31 FIRE. **No transmission into equity vol yet:** VIX fell 19.45 → 16.91 while the ratio rose. A context canary, not an action gate. BRENT owns oil substance.

**HENRY / LIQUID — surface path:** VX/X6 above VX/Z6 on 10/22 (−0.770%) and 10/23 (−0.601%) while the cash 3M/VIX held ≥1.053. A futures-front inversion without a cash inversion is one observation and is unregistered. VVIX peak 109.70 (120 not fired). The FOMC 10/28 drew no bid: VIX −3.48% to 16.91, 3M/VIX 1.1366, MOVE 94.55. HENRY's 10/28 gamma is POSITIVE both horizons; today's 7,701 intraday sits under those flips, and that call is HENRY's.

**LIQUID / REGINALD:** HY 340 [10/22] → 314 [10/28] (FRED); CCC 13.07%; BIN-B BLOCK ACTIVE. No VIOLET credit grade. The October 13 → November 17 credit-vol WATCH stands.

**SAM:** JPY RV10 6.93% p33.8 CALM; FXY 50-DTE IV 11.5%. BOJ decision tonight ET; VIOLET reads only the carry-to-vol leg.

**VULCAN:** AI tape (SOX −6.72% 10/22, Alphabet −12.75% 10/29 vendor intraday) moved VIOLET's equity-concentration vector 2 → 3. COR1M 8.73 [10/28] still dispersed, so this is not a correlated selloff. AMZN/AAPL tonight not graded.

**PROME:** cheap_tail.py route text corrected per your 10/23 packet; CFTC 10/20 shows speculators out of the EXTREME_LONG VIX-futures position (−20,890, p59).

## CALIBRATION

- The convergence score is not a probability; each move is tied to a dated official reading.
- The oil-vol FIRE rests on one official close. Part of the ratio is the falling VIX denominator, but the OVX level also rose (53.28 → 58.59).
- Backfilled canary rows use as-of-date windows only (no later data); they are reconstruction, not first-publication vintages.
- Inherited credit-lead hit/lag rates remain unreplicated.

## CROSS-AGENT TENSIONS

None active this cycle. (SKEW: VIOLET's 150 line and RED's FT-10 <140 exit are different lines and both are stated above; no conflict.)

## NEXT DECISION POINT

10/29 official closes (SKEW for RED, OVX re-read) · BOJ 10/30 · AMZN/AAPL reaction on the 10/30 close · Election Day 11/03 · payrolls 11/06 and CPI 11/10 (both dates secondary) · November 17 lag endpoint · November 18 VIX expiry · December 16 L441.

## VIEW

LOW_VOL at VIX 16.91 [10/28]. **Convergence 32/50.** Tail pricing is easing but still FT-10-firing; oil vol is the one channel at FIRE; equity concentration is building without correlation. No Will decision or trade; $0 moved.
