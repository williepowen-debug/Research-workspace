# VIOLET: PRED-07 grade and the CPI-day read, 2026-11-10

**Stamp:** 2026-11-10 11:1x ET (session opened 11:09 ET from `date`). Launched by PROME prome-07 on the desktop after the 11/10 machine switch. Cboe History CSVs read about 11:10 ET; `backfill.py --spot-only --spot-days 15` and `boot.py` were run about 11:09 ET; BLS public API read about 11:10 ET; vendor 5-minute bars (yfinance) read 11:11 ET; FRED VIXCLS read about 11:11 ET.

## VIO-PRED-07: CONFIRMED (event as written happened)

| Element | Value |
|---|---|
| Letter | VIX3M close ÷ VIX close, same date, as published, unrounded, `≥ 1.000` on at least one session 2026-11-06 through 2026-11-13 (`research/2026-11-06_wake/LETTERS.md`) |
| Qualifying close | **11/09: VIX3M 20.85 / VIX 19.92 = 1.04669**, Cboe `VIX3M_History.csv` and `VIX_History.csv`, read about 11:10 ET 11/10 |
| Path | 0.9067 [11/05] → 0.9594 [11/06, does not qualify] → **1.0467 [11/09]** |
| Forecast | 72%; base 36 of 42, 12 of 18 if still inverted on the next close (11/06 was) |
| Resolved | Session 2 of the six-session window. One close is enough; later closes cannot undo it |
| Outcome | CONFIRMED. Not a miss, so no WQ-619 A surprise line is owed. PROME DOCKET line 1030 is PROME's to close |

## 11/09 row SETTLE: the print held on every cell

`backfill.py --spot-only --spot-days 15`: 2,766 cells agreed, 0 blanks filled, **0 corrected**, 1 row stamped SETTLE (11/09). Cboe History 11/09: VIX 19.92 (open 25.08, high 25.08, low 19.64), VIX9D 19.88, VIX3M 20.85, VVIX 98.43, SKEW 150.34, COR1M 13.23. FRED VIXCLS 11/09 = 19.92.

- **LOW_VOL confirmed for 11/09** (19.92 < 20.00 by 0.08). The 11/09 regime broadcast stands.
- **Convergence 33/50 confirmed** on History (every cell used in the 11/09 re-score equals the print).
- **COR1M 13.23 on History equals the ledger row** (KB-VIO-365 check: agrees).
- **CHEAP_TAIL 11/09** added by `--as-of 2026-11-09` against the CATALYSTS snapshot at commit `01e44a3f50` (2026-11-06 10:32 ET, the last change before 11/09): DORMANT 2/4.

## October CPI release: date verified at the publisher

- **bls.gov web pages still return 403** to this box (`cpi.nr0.htm`, 11:10 ET). **The BLS public data API (`api.bls.gov/publicAPI/v2`, no key) answered.** It carries October 2026 as `latest`: this is the first publisher-sourced confirmation of the date, which until now was SECONDARY (RED S57 plus search). The release hour is not read from BLS; the 08:30 ET bar on the tape is consistent with it.
- Seasonally adjusted indexes, month over month, from the published three-decimal values: **all items 337.476 vs 336.298 = +0.35%**; **core (less food and energy) 339.900 vs 338.896 = +0.30%**. BLS computes its headline percentage from unrounded data, which this read did not have.
- ⚠️ **No year-over-year figure here.** The not-seasonally-adjusted October 2025 index is blank (`-`) in both series, the 2025 collection gap. This read does not compute a 12-month change, and any 12-month figure seen elsewhere needs its method named.
- ⚠️ **Consensus not read.** Whether this was above or below expectations is a separate input (MEMORY, 9/14 sweep). HENRY owns the macro read and BOND owns rates.

## CPI-day surface: pre vs post, INTRADAY (not the close)

The official post-CPI read is on today's close (16:15 ET print, then History). It is **not done in this record**. The table below is vendor 5-minute bars and the 11:09 ET live tick, row TICK.

| Series | Pre: 11/09 close [History] | 08:25 bar (last before release) | 08:30 bar (release) | 11:09 ET tick |
|---|---:|---:|---:|---:|
| VIX | 19.92 | 20.02 | **20.77** (+3.75% in the bar) | 21.10 |
| VIX9D | 19.88 | not published before 09:30 | n/a | 20.86 |
| VIX3M | 20.85 | n/a | n/a | 21.68 |
| VVIX | 98.43 | n/a | n/a | 102.54 |
| VIX9D/VIX | **0.998** | | | **0.989** |
| VIX3M/VIX | **1.0467** | | | **1.0275** |
| ES front (vendor) | | 7,578.75 | 7,543.75 (−0.46%) | 7,522.00 (11:00) |
| TLT (vendor) | | 81.82 | 81.67 | 80.85 (11:10) |

VIX GTH session range 19.62 to 21.61 through 10:55 ET. SPY 747.77 at 11:10 ET vs $752.69 [11/09 vendor close].

**Read (interim, TICK):** the release moved VIX up about 0.75 points within five minutes, alongside lower equity futures and lower Treasury prices. The front did not bid above the month: VIX9D/VIX went from 0.998 to 0.989, so the market is not pricing more near-term stress than one-month stress. The curve flattened (3M/VIX 1.0467 to 1.0275) but stayed in contango. VVIX is up about 4% and still under 120.

**What the close decides:** VIX closing at **20.00 or higher** turns the label back to RISING_VOL. That re-triggers the regime-shift row (LOW_VOL → RISING_VOL) and the NEXUS_BRIEF send. VIX was at 21.10 at 11:09 ET, which is 1.10 above the line. A close under 20.00 keeps LOW_VOL.

## Not graded here

- VIO-PRED-08 (VIX ≥30 by 11/20, 25%): VIX 21.10 at 11:09 ET, 8.90 away. VIO-PRED-09 (SKEW <140 by 12/31, 45%): 150.34 [11/09 History].
- RED-FT-10 and RED-FT-06 are RED's to grade. The 11/09 bars were sent to RED: SKEW 150.34, VIX History and VIXCLS 19.92.
