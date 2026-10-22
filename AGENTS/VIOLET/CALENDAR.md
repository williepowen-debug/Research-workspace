# VIOLET CALENDAR

Updated October 21, 2026 (22:2x ET); canonical dated rows [CATALYSTS](workbook/CATALYSTS.tsv). Closeout contract: at least one HIGH/MEDIUM row within 14 calendar days (`scripts/forward_calendar_check.py`, KB-VIO-353). Fired rows preserved in research/2026-10-19_official-followthrough/catalysts-fired.tsv and research/2026-10-21_catchup/catalysts-fired.tsv.

## ACTIVE FORWARD CATALYSTS

| Date | Event | Impact | VIOLET checkpoint |
|---|---|---|---|
|Oct 28 (Wed)|FOMC decision Oct 27-28, no SEP|HIGH|Existing event; HENRY owns the policy path.|
|Oct 29 (Thu)|Q3 GDP advance + September PCE, 08:30 ET|MEDIUM|BEA primary. Day after FOMC; read the surface reaction only.|
|Oct 30 (Fri)|BOJ decision (Oct 29-30) + Outlook Report|MEDIUM|BOJ primary. Lands the evening of Oct 29 ET; SAM owns substance, VIOLET the carry-to-vol read.|
|Nov 3 (Tue)|US midterm Election Day|MEDIUM|Statutory date. Check whether VX/X6 carries an event kink over VX/Z6.|
|Nov 6 (Fri)|October payrolls, 08:30 ET|MEDIUM|SECONDARY date (LABOR register; bls.gov 403 on 10/21) - verify before any grade keys on it.|
|Nov 18 (Wed)|VIX November expiration AM SOQ|MEDIUM|Record contract pair; adjusted helper switches inside DTE<5.|
|Dec 16 (Wed)|M1:M2 historical-average recheck KB-VIO-310|LOW|Existing L441; re-measure before any approved numerical update.|

## RESOLVED — fired catalysts and their grades

- **October 21 VIX October expiration (AM SOQ):** VX/V6 final settlement **16.82** vs prior settle 17.2209 (−2.33%); spot VIX 17.31 → 16.68. Orderly expiry into easing; adjusted X6/Z6 +1.686% after the roll. No live VIOLET letter touched. KB-VIO-352.
- **October14SKEW:** official157.30 completes4/4; RED graded FIRING. October15/16final160.45/168.59extend same run, no second fire. Observation obligation behindL667complete; publication hour unassumed.
- **October15PPI /October16funding/CFTC:** BOND owns post-PPI rates; LIQUID LIQ07RESOLVED S2. CFTC October13report recoveredOctober19, original release vintage unverified. [Follow-through](research/2026-10-19_official-followthrough/REPORT.md).

- **October 14 08:30 ET September CPI:** releasedBLS; pre-CPI alert event window ended. Actual priorWQ418decisionPASSED/no trade, not pending. [Post-CPI assessment](research/2026-10-14_post-CPI/REPORT.md). OfficialOctober14 SKEWgrade subsequently recorded byRED; seeOctober19follow-through.
- **October 12 Columbus Day:** equity/options session confirmed by official Cboe bar; do not remove that observation from the SKEW count. ICE holiday rows are dated publications, not fresh cash-credit witnesses.

- **October 7 close — Q2 transmission-test window (DOCKET L477):** **CLOSED, NOT FIRED.** CBOE SETTLE 9/24–10/07: VIX3M/VIX min 1.1242 (9/30), VVIX max 92.01 (10/01) — neither leg near `≤1.00 AND >120`. Disconfirmer (b) met (VVIX 82.59 / 83.18 on 10/06–10/07 with MOVE 105.20 / 102.56). Graded late on 10/10 (VIOLET dark). → KB-VIO-323.
- **September 30 Micron (MU) FQ4:** fired after the close. VULCAN graded its own rows (VULCAN-11 FALSIFIED, S2 3 → 2; packet 10/01). VIX 16.34 [9/30] → 16.39 [10/01], +0.3%. The cheap-tail alert's next dated catalyst after MU was missing from this calendar — that gap is KB-VIO-324.
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
