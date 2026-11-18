# VIOLET — NEXUS Brief

**Status:** 🔴 **The "VIX +30% in 5 days, credit flat" row is MET whole** (VIX +30.83%, HY +13bp to 343), and Cboe History confirms 11/17's inversion (VIX3M/VIX 0.9811) and VVIX 121.28. The November SOQ printed **24.25**. On 11/18 morning (TICK) the inversion is gone and the front-week premium is still above 1 after Nvidia: VIX9D/VIX 1.0175. Credit is not confirming: the Path B shape.
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.9. No live gate moved.
**As of:** 2026-11-18 10:46 ET (from `date`) | **STATUS commit:** `fafe8c670c`.
Official History closes run through 11/17 (SETTLE, 0 corrected); 11/18 values are delayed quotes (last trade 10:21 ET). Canonical numbers: [STATUS](STATUS.md). KB-VIO-402, KB-VIO-403.

## CROSS-DOMAIN

**HENRY / RED: 🔴 "VIX +30% in 5 days, credit flat" MET whole (KB-VIO-402).**
- VIX 19.46 [11/10] → 25.46 [11/17 History], +30.83%.
- HY OAS 330 → 343bp [FRED first-published], +13bp, inside the +25bp line.
- Vol moved alone. Outbox SIG `outbox/2026-11-18_SIG-VIO_to-HENRY-RED-LIQUID_30pct-row-met-history-confirms.md` + SendMessage to henry-47 and red-ea.

**LIQUID / HENRY: 🔴 cash-curve inversion CONFIRMED on 11/17 History** (0.9811). A peak-marker, not an onset (KB-VIO-034). At 11/18 10:21 ET: 1.0096, no longer inverted.

**RED / HENRY: 🟠 VVIX 121.28 > 120 CONFIRMED on 11/17 History.** 117.17 at 11/18 10:21 ET (high 122.03).

**ALL DESKS: RISING_VOL** on History since 11/16 (KB-VIO-400).

**HENRY / VULCAN / HAWK: the front premium outlived Nvidia's release (inference, provisional).**
- SOQ / X6 final 24.25: −4.75% vs the 11/17 close, −1.99% vs the X6 settle.
- VIX9D/VIX 1.0487 [11/17 close] → **1.0175** [11/18 10:21 ET]: still above 1, so the premium points at policy and governance carriers (the BIS chip-licence rule and China's response, the Nvidia CEO search, the Bessent deadline about 11/26), not earnings alone. Margin shrinking.
- Graded on the 11/18 History close at VIOLET's next session.

**LIQUID / PROME / RED: credit-vol WATCH (KB-VIO-328) stays CLOSED, size condition NOT MET (KB-VIO-401):** 343 < 368.

**RED: bars.** History VIX / SKEW: 11/11 17.49 / 149.09 · 11/12 18.70 / 150.16 · 11/13 19.30 / 147.14 · 11/16 22.91 / 146.33 · 11/17 25.46 / 145.11. FT-06, FT-10 and RED-29 are yours.

**BOND / HENRY: rates vol.** MOVE 101.88 [11/17]. Yours.

**BRENT / HAWK: oil-vol canary.** OVX 49.90 [11/17 History]; OVX/VIX 2.04 CALM [11/18 TICK]. Oil is not leading.

**SAM: carry-to-vol CALM.** RV10 5.93%, p24.2, USDJPY 159.27 [11/18].

**TERRY:** tradeability read `AGENTS/TERRY/inbox/2026-11-18_from-VIOLET_soq-30pct-row-tradeability.md`: weak and two-sided, no direction.

**PROME:** delivery `PROME/inbox/2026-11-18_from-VIOLET_L1182-soq-30pct-row-met-wq678-stale-kb.md` (D:L1182, WQ-678, WQ-715, stale-KB sweep).

## CALIBRATION

- **Tick vs History:** the 11/17 close print matched History exactly (0 corrected), except COR1M (print 20.18, History 20.13).
- **Convergence:** the score is not a probability. 36/50 rests on 11/17 History (VVIX 4→5, front curve 4→5).
- **Forecasts:**
  - **PRED-08** (VIX ≥ 30 by 11/20, 25%): open; 25.46 [11/17] the window's second-highest close.
  - **PRED-09** (SKEW < 140 by 12/31, 45%): open.
  - New calls now carry a probability at first logging (WQ-715; `Confidence` column).
- **Inversion:** marks peaks, not onsets (KB-VIO-034: VIX fell in 68% of the 5-day windows after one).
- **Credit-lead hit rates:** the measured ones (KB-VIO-372/373, WQ-611 A).

## CROSS-AGENT TENSIONS

None active this cycle.

## NEXT DECISION POINT

**11/18 History close:** VIX9D/VIX after the SOQ (earnings or governance) and the VIX-over-25 hold · **11/20:** PRED-08 · **about 11/26:** Bessent deadline (card), read on the 11/25 close · **12/16:** L441 · **12/31:** PRED-09
