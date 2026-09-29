# VIOLET CALENDAR

Updated September 28, 2026 (Q2 transmission-test window close 10/7 added; Cboe confirmed the 9/23 leg-2 close). Dated events: `workbook/CATALYSTS.tsv`; countdowns are computed by `scripts/catalyst_countdown.py`.

## ACTIVE FORWARD CATALYSTS

| Date | Event | Impact | VIOLET checkpoint |
|---|---|---|---|
| **Sep 30 (Wed)** | **Micron (MU) FQ4 earnings** | MEDIUM | Confirmed after close 16:30 ET; VULCAN owner. Outside frozen letter's leg 2 window. |
| Oct 7 (Wed) | Q2 transmission-test window closes (DOCKET L477) | LOW | Last of 10 sessions off the 9/23 MOVE spike: VIX3M/VIX ≤1.00 AND VVIX >120 on two consecutive closes, else ordinary repricing. |
| Dec 16 (Wed) | M1:M2 historical-average re-check (KB-VIO-310, PROME L441) | LOW | December VIX expiry: re-measure; replace 5.6 if the full-history median differs by >0.5pp |

## RESOLVED — fired catalysts and their grades

- **September 23 close — VIO-FOMC-0916 leg 2:** **KILL.** VIX 17.71 [9/16 CBOE] → 15.18 [9/23; yfinance at grade, **Cboe SETTLE confirmed 9/28, no correction**] = **−14.29%** vs kill < −1.41%. Whole letter FAILED: 0 CONFIRM · 2 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect. Record: `research/2026-09-24_VIO-FOMC-0916_GRADE_part3.md`.

- **September 18 BOJ decision:** fired 23:00 ET Sep 17 — **HIKED +25bp to 1.25%, vote 7–2** (Asada, Sato dissenting for HOLD); USD/JPY 156.75. SAM owns policy substance. ⭐ **VIOLET's JPY carry-vol canary STOOD DOWN on the print** — RV10 15.15% (p94.8, WATCH) → **11.1% (p72.6, CALM)**. The event-conditioned watch **resolved without firing**; one observation against a naive reading of H-carry.
- **September 18 SPX quarterly OPEX (triple witching):** fired. **The vol crush ran straight through it** — VIX 15.44 → **14.83** (−3.95%), VIX9D 13.39 → **12.28** (−8.29%), term structure re-steepening a 3rd session to **1.2299**. HENRY's post-opex gamma board (**L411**) had **not landed** as of 16:2x ET 9/18; his next board landed **9/21** (`59b96cfd2`, sign flipped POSITIVE) and no HENRY board commit was found 9/18–9/20 (checked 9/28). Read gamma only from HENRY's current brief; his 9/17 pre-opex board (negative a 3rd session, deeper, no wall publishable) carries a one-session shelf life by his own statement and ⛔ must not be read as current for 9/18. **LEG 3 GRADED on this close: CONFIRM branch B / MISS OF THE MAP** — the Fed hiked and the surface printed the HOLD-branch signature; branch A failed 0/3. Grade record: `research/2026-09-18_VIO-FOMC-0916_GRADE_part2.md`.
- **September 16 VIX quarterly expiration:** fired. VX/U6 final settlement (SOQ) **16.79** vs 17.032 the prior settle (−1.42%); spot VIX closed the same session **17.71** (+2.97%). Matched Oct/Nov pair +2.436% → +2.381% (flat): letter leg 5 **HELD with the §5 roll-date defect disclosed** (not a clean pass). Grade record: `research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md`.
- **September 16 FOMC + SEP:** fired — **HIKE +25bp to 3.75–4.00%, 12–0** (federalreserve.gov, verified 9/17). Letter part 1 graded on the 9/16 close: **leg 1 VOID** (VIX 17.20 at the 9/15 close >16), **leg 4 KILL** (MOVE +16.26% < VIX +22.05%), **leg 5 HELD-with-defect**; **leg 3 first read: no branch at 2/3** — **GRADED 9/18: CONFIRM branch B / MISS OF THE MAP**, ratio 1.2299 >1.20 and VVIX 87.63 <92 while branch A failed 0/3 after a 12–0 HIKE; leg 2 pending 9/23. F-B: see STATUS gate table.
- **September 11 CPI:** BLS actuals confirmed. Friday VIX 15.84 and SKEW 154.49 close captured and archive-confirmed. The old “settle still owed” statement is closed. The unqualified “in line” consensus assertion is withdrawn; falling annual core and an upside monthly surprise can coexist. F-B still requires the full window.
- **August 5 VIX exit counterfactual:** VIOLET recorded its retrospective grade August 18 in KB-VIO-196; no capture is newly owed by this calendar. The historical use of a spot high as a SOQ proxy is not a fresh independent SOQ verification.
- Earlier event outcomes and the full provenance trail are preserved in `archive/sweep_2026-09-14/CALENDAR.md`. Past events are not future reminders.

## DATA REFRESH SCHEDULE

| Feed | Required evidence |
|---|---|
| Spot VIX complex | Cboe quote's own timestamp; archive-confirm dated closes; populate all six spot fields |
| SKEW | Grade when dated archive bar exists; no guaranteed publication hour |
| VX futures | Keep settlement date and both contract symbols; compare matched pairs across rolls |
| MOVE | investing.com primary; mirror is cross-check; retain actual observation date |
| FRED credit/rates | Inspect each series' frontier; never carry an outage across a later successful pull |
| CFTC positioning | Report date and actual release availability; no synthesized holiday schedule |
| VIX OI / FXY IV | Regular-hours usable chain; zero OI and stale quotes do not support a conclusion |
| Registered reads | `workbook/PREDICTIONS.tsv` points to frozen criteria; future evidence remains pending |

Sources: [Fed](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm), [BOJ](https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm), [Citadel](https://www.citadelsecurities.com/news-and-insights/global-market-intelligence/september-setup/), [BLS](https://www.bls.gov/news.release/archives/cpi_09112026.htm).
