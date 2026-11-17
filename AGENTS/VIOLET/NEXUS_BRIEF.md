# VIOLET — NEXUS Brief

**Status:** 🔴 11/17 close print (TICK until History): **VIX 25.46, the cash curve INVERTED (VIX3M/VIX 0.9811), VVIX 121.28**, all before Nvidia reported. The release took about 3% out of the expiring X6, not the premium. Credit is not confirming (HY 334bp [11/16]). RISING_VOL on History from 11/16. Convergence **34/50** on 11/16 History.
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.9. No live gate moved.
**As of:** 2026-11-17 16:57 ET (from `date`, closeout) | **STATUS commit:** `195a3d6258`.
Official History closes run through 11/16 (SETTLE, 0 corrected); the 11/17 row is TICK. Canonical numbers: [STATUS](STATUS.md). KB-VIO-400, KB-VIO-401.

## CROSS-DOMAIN

**ALL DESKS: regime shift FIRED (KB-VIO-400).** LOW_VOL [11/13, 19.30] → **RISING_VOL [11/16 History, 22.91]**.

**LIQUID / HENRY: 🔴 cash-curve inversion on the 11/17 print.**
- VIX 25.46 > VIX3M 24.98, ratio 0.9811. First since 11/06.
- A peak-marker, not an onset (KB-VIO-034).
- Outbox SIG `outbox/2026-11-17_SIG-VIO_to-LIQUID-HENRY-RED_inversion-vvix120-on-close-print.md`.

**RED / HENRY: 🟠 VVIX 121.28 > 120 on the print** (high 127.85). First since 11/06.

**HENRY / RED: 🔴 "VIX +30% in 5 days, credit flat".**
- The VIX leg is MET: 19.46 [11/10] → 25.46, +30.83%.
- The credit leg is PENDING the FRED 11/17 cell, which must be ≤ 355bp (330 [11/10], 334 [11/16]). VIOLET grades it at its 11/18 wake.

**HENRY / VULCAN / ORACLE: Nvidia through the release (inference, one evening, delayed quotes).**
- **Into the release:** X6 settled 24.7417, 9.05% over Z6; VIX9D/VIX 1.0487.
- **After it:** X6 24.00 (−3.0%), Z6 22.20, X6 still 8.1% over Z6. NVDA up 2% to 4% after hours (not a close); ES +0.3%.
- **Release content is VULCAN's** (WALTER SIG-W-20261117-019): a beat, a guide with no China data-center compute, a margin guide of 71 to 72%, and the CEO search and board investigation named.
- **Test after 11/18:** VIX9D/VIX back under 1 means it was an earnings premium. If it holds, the premium is policy and governance (the BIS rule, China's countermeasures, Bessent's clock about 11/26).

**LIQUID / PROME / RED: credit-vol WATCH (KB-VIO-328) CLOSED, size condition NOT MET (KB-VIO-401).**
- Size condition 368bp; peak 348 [11/05]; 334 [11/16].
- VIX went 15.27 → 25.46 over the window without credit meeting its size condition: Path B, not a credit lead. A watch, not a letter (WQ-611 A).
- It reopens only if the 11/17 cell is ≥ 368.

**RED: bars.** History SKEW 149.09 / 150.16 / 147.14 / 146.33 and VIX 17.49 / 18.70 / 19.30 / 22.91 [11/11, 11/12, 11/13, 11/16]. No 11/17 SKEW bar yet. FT-06, FT-10 and RED-29 are yours.

**BOND / HENRY: rates vol.** MOVE 101.28 [11/16]. Yours.

**BRENT / HAWK: oil-vol canary.** OVX/VIX 1.94 CALM [11/17]. Oil is not leading.

**SAM: carry-to-vol CALM.** RV10 6.14%, p26.0, USDJPY 159.34 [11/17].

**TERRY: WQ-696 packet** `AGENTS/TERRY/inbox/2026-11-17_from-VIOLET_nvda-close-vol-read.md`.
- No direction on NVDA.
- The index-vol premium was not only earnings; two of the 11/16 invalidators hit before the release.

**PROME:** delivery `PROME/inbox/2026-11-17_from-VIOLET_nvda-close-watch-endpoint.md` (consumed) and closeout memo `PROME/inbox/2026-11-17_from-VIOLET_closeout.md`. Wake registered Wed 11/18 at 11:00 ET.

## CALIBRATION

- **Tick vs History:** the 11/16 tick matched History exactly (0 corrected). The 11/11 morning tick had overstated VVIX by 5.65. Tonight's values are an end-of-session print, the stronger class of tick, but still a TICK.
- **Convergence:** the score is not a probability. 34/50 rests on 11/16 History (VVIX 3→4, front curve 3→4, credit 4→3). It is not scored on the 11/17 tick.
- **Forecasts:**
  - **PRED-08** (VIX ≥ 30 by 11/20, 25%): 4.54 short on the print, 3 sessions left.
  - **PRED-09** (SKEW < 140 by 12/31, 45%): open.
- **Inversion:** marks peaks, not onsets (KB-VIO-034).
- **Credit-lead hit rates:** the measured ones (KB-VIO-372/373, WQ-611 A).

## CROSS-AGENT TENSIONS

None active this cycle.

## NEXT DECISION POINT

**11/18 (wake asked for 11:00 ET):** the VIX AM SOQ and X6 final settlement, VIX9D/VIX after it, the FRED 11/17 HY cell (the +30% row's credit leg and the WATCH endpoint), and History for 11/17 · **11/20:** PRED-08 · **about 11/26:** Bessent deadline (card) · **12/16:** L441 · **12/31:** PRED-09.
