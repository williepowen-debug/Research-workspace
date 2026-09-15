# VIOLET CALENDAR

Updated September 14, 2026. Dated events: `workbook/CATALYSTS.tsv`; countdowns are computed by `scripts/catalyst_countdown.py`. Exact prediction rules live in their frozen registrations, not this calendar.

## ACTIVE FORWARD CATALYSTS

| Date | Event | Impact | VIOLET checkpoint |
|---|---|---|---|
| **Sep 16 (Wed)** | **VIX September expiration (quarterly)** | MEDIUM | AM SOQ before FOMC. Strict front roll occurs here; adjusted pair already changed Sep 14 under the DTE <5 rule. |
| **Sep 16 (Wed)** | **FOMC Rate Decision + SEP** | HIGH | Official Sep 15–16 meeting. Grade registered legs and F-B at their specified closes; Leg 1 void if Sep 15 VIX >16. |
| **Sep 18 (Fri)** | **Bank of Japan monetary policy decision** | HIGH | Official Sep 17–18 meeting, Japan time; no fixed announcement hour asserted. SAM owns policy; JPY-vol transmission watch. |
| **Sep 18 (Fri)** | **SPX September quarterly OPEX (triple witching)** | MEDIUM | HENRY gamma refresh; frozen letter leg 3 second read. Citadel's dated estimates remain estimates. |
| **Sep 23 (Wed)** | **VIO-FOMC-0916 leg 2 resolution** | LOW | Grade Sep 16→23 VIX move; checkpoint, not a new macro event. |
| **Sep 30 (Wed)** | **Micron (MU) FQ4 earnings** | MEDIUM | Confirmed after close 16:30 ET; VULCAN owner. Outside frozen letter's leg 2 window. |

## RESOLVED — fired catalysts and their grades

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
