# VIOLET grade and close read, 2026-11-09

**Stamp:** 2026-11-09 20:17 ET (from `date`). Will's word "go" 20:16 ET on the boot report. Cboe History CSVs read 20:13 and 20:17 ET; boot.py 20:11 ET; FRED VIXCLS read 20:18 ET; vendor ETF closes via `FORGE/tools/market-data/fetch.py` 20:16 ET.

## VIO-PRED-10: CONFIRMED (event as written happened)

| Element | Value |
|---|---|
| Letter | VVIX close `< 100.00` on at least one session 2026-11-06 through 2026-11-20 (`research/2026-11-06_wake/LETTERS.md`) |
| Qualifying close | **98.43 [11/09]**, Cboe `VVIX_History.csv`, as first published, read 20:13 and 20:17 ET |
| Path | 134.99 [11/05] → 121.94 [11/06] → 98.43 [11/09] |
| Forecast | 55%; base 7 of 13 within 11 sessions |
| Resolved | Session 2 of the 11-session window. One close is enough, no reset, so later closes cannot undo it |
| Outcome | CONFIRMED. Not a miss, so no WQ-619 A surprise line is owed |

## VIO-PRED-07: NOT YET GRADED

Letter: VIX3M close ÷ VIX close `≥ 1.000` on at least one session 11/06–11/13. VIX3M History 11/09 = **20.85** posted. VIX History still ends 11/06 at 20:17 ET. On the 16:15 ET print VIX was 19.92, ratio **1.0467**. The letter fails for 11/09 only if History VIX is above 20.85, 0.93 over the print. Grade at the next read after VIX History posts 11/09. 11/06 History ratio 24.60 / 25.64 = 0.9594, inverted, does not qualify.

## VIO-PRED-08 / 09: OPEN

VIX 30 needs +10.08 from 19.92. SKEW <140 needs −10.34 from 150.34 [11/09 quote]; 153.55 [11/06 History].

## 11/06 row SETTLE

`backfill.py --spot-only --spot-days 15`: 2,763 cells agreed, 1 blank filled (SKEW 153.55), **0 corrected**, row stamped SETTLE. VIX 25.64 and SKEW 153.55 at History equal the print and the 11/06 quote. KB-VIO-387's figures and KB-VIO-389's −2.54 stand. CHEAP_TAIL 11/06 added by `--as-of` against the CATALYSTS snapshot at commit `3920dc20ee`: DORMANT 2/4.

## 11/09 close read (print, row TICK)

| Series | 11/06 History | 11/09 | Change | Basis |
|---|---:|---:|---:|---|
| VIX | 25.64 | **19.92** | −22.31% | print; History not posted |
| VIX9D | 27.18 | 19.88 | −26.86% | History |
| VIX3M | 24.60 | 20.85 | −15.24% | History |
| VIX6M | 24.70 | 22.22 | | print |
| VVIX | 121.94 | **98.43** | −19.28% | History |
| SKEW | 153.55 | 150.34 | | quote |
| VIX3M/VIX | 0.9594 | **1.0467** | | print VIX |
| VIX9D/VIX | 1.0601 | **0.998** | | print VIX |
| M1:M2 adj. | −6.376% | −2.572% | | VX/X6→VX/Z6 settle |
| COR1M | 20.76 | 13.23 | −36.27% | ledger stamps SETTLE by clock, KB-VIO-365 class; History check owed |
| MOVE | 92.77 | 85.98 | −7.32% | investing.com primary, mirror agrees |
| OVX / OVX:VIX | 58.29 / 2.27 | 57.37 / 2.88 | | CALM, broad co-move |
| JPY RV10 | 3.13% | 5.06%, p18.5 | | CALM; FXY IV/RV 2.22x on stale off-hours quotes |

Vendor ETF closes, not official records: SPY $752.69 (+2.37%), QQQ $679.35 (+3.54%), RSP $220.95 (+2.27%), HYG $77.51 (+0.36%), KRE $73.45 (+1.73%). HENRY owns equity.

**Regime:** RISING_VOL → **LOW_VOL** on the print, VIX 0.08 under the 20 line. Inversion ended (first contango close since 11/04). VVIX back under 120. The regime-shift outbound row is met on the print; delivered by NEXUS_BRIEF CROSS-DOMAIN (🟠, no outbox).

**Pre-CPI (10/2026 CPI, 11/10 08:30 ET, date SECONDARY):** VIX9D/VIX 0.998. The front no longer prices the CPI week above the month, against 1.0601 [11/06]. Post-CPI read owed 11/10.

**Credit (LIQUID owns):** HY OAS first-published **342bp [11/06]**, −6bp; CCC 13.17%; BB 208. 5-day row, window 10/30 → 11/06: VIX +32.03% (19.42 → 25.64, History), HY 344 → 342, −2bp: **MET on its letter**, same episode as the 11/05 send; not re-sent. Window 11/02 → 11/09: VIX −5.81% on the print, not met. HY is still +74bp over the 268bp [9/22] base; the credit-vol WATCH endpoint is 11/17.

**FT-06 context (RED grades):** FRED VIXCLS 28.18 [11/05], 25.64 [11/06]; 11/09 not yet on FRED at 20:18 ET.

## Convergence re-score (print basis; confirm on VIX History)

38 → **33/50**. VVIX 5 → 3 (98.43, under 120, over the 90s it left). Front curve 5 → 3 (contango 1.0467, 9D/VIX 0.998, M1:M2 −2.572%). Implied correlation 4 → 3 (COR1M 13.23, from 22.84 [11/05], still above 9.53 [11/04]). No other vector moved: MOVE still above its reference levels, credit 342bp near the run peak, SKEW FT-10 still RED's FIRING, equity concentration is HENRY's read. The score is not a probability.
