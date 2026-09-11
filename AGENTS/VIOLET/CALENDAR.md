# VIOLET CALENDAR

VIX-specific catalysts and monitoring schedule. **Source of truth for dated catalysts: `workbook/CATALYSTS.tsv`** (machine feed for `scripts/catalyst_countdown.py`). This file is the human twin and must not diverge.

---

## VIX EXPIRATION DATES (Monthly)

VIX futures and options expire on the **Wednesday 30 days prior to the third Friday of the following month**.

| Month | Expiration Date | Notes |
|-------|-----------------|-------|
| ~~Apr 2026~~ | Apr 15 | EXPIRED |
| ~~May 2026~~ | May 20 | EXPIRED. Episode-17 VIX 25C expired worthless 5/19. |
| ~~Jun 2026~~ | Jun 17 | EXPIRED — quarterly. Resolved clean alongside FOMC (no pin stress; VIX +12% on the hawkish dot, then faded). M1 (war-premium carrier) expired with it. |
| ~~Jul 2026~~ | Jul 15 | EXPIRED — clean, no pin stress. FOMC Jul 29 landed later the same month. |
| ~~Aug 2026~~ | Aug 19 | **EXPIRED 8/19 — and it settled the pin/roll question.** VIX9D fell INTO the expiry (13.59 [8/18] → 12.66 [8/19]) and jumped +13.7% to 14.39 the session AFTER the size cleared. **Expiry mechanics ruled OUT as the driver of the front-end bid** (KB-VIO-204). Aug-05 weekly SOQ graded 8/18 (KB-VIO-196). |
| Sep 2026 | Sep 16 | Quarterly (same day as FOMC + SEP). |

**Pin risk:** VIX tends to drift toward strikes with high open interest near expiration.

---

## FOMC MEETINGS (Vol Events)

| Date | Meeting | VIX Watch |
|------|---------|-----------|
| ~~Apr 28-29, 2026~~ | FOMC | DONE — held 3.50-3.75%, 4 dissents (most since Oct 1992, Powell's last cycle). VIX did NOT spike. |
| ~~Jun 17, 2026~~ | FOMC + SEP | **DONE — Kevin WARSH's first meeting as chair.** Held 3.5-3.75% **12-0**, but dot plot flipped HAWKISH: 2026 median **3.4→3.8%**, **9 of 18 project a hike** (6 project two); Warsh submitted no dot, 130-word statement, dropped forward guidance. VIX **+12% on the day (~18.44)** then faded (6/18 16.40). **Rate-shock leg RE-ARMED → Fed-HIKE regime.** |
| **Jul 28-29, 2026** | **FOMC** | No SEP. Warsh presser only. Decision Wed Jul 29. **First FOMC of the new Fed-HIKE regime — tests 6/17 dot-flip follow-through.** |
| Sep 15-16, 2026 | FOMC + SEP | Quarterly — critical. Decision Wed Sep 16 = same day as VIX Sep quarterly expiry. First SEP after the hike-signal flip. |

**Pattern:** VIX typically rises into FOMC, drops on outcome if no surprise. The GEX-era absorption held through 6/17 even on a hawkish surprise (+12% spike faded in a day, counter 0/5) — refresh hypothesis on each FOMC outcome.

---

## EARNINGS SEASONS (Vol Supply)

| Quarter | Peak Earnings | VIX Impact |
|---------|---------------|------------|
| ~~Q1 2026~~ | Apr 15-May 2 | DONE — vol supply realized, VIX did not spike |
| Q2 2026 | Jul 15-Aug 1 | — (overlaps Jul 15 VIX exp + Jul 29 FOMC) |
| Q3 2026 | Oct 15-Nov 1 | — |
| Q4 2026 | Jan 15-Feb 1 | — |

**Pattern:** Earnings season = vol supply as single-stock vol gets realized. **Concentration watch:** with record AI/semi concentration (47%) + the leveraged-ETF amplifier complex (US aggregate figure UNVERIFIED — the $464bn number is do-not-propagate per DEWEY 7/20, likely gross-AUM not net rebalance-demand; the demonstrated vehicle-scale case is Korea's ~$9-10bn 2× chip-ETF complex), a single AI-name earnings gap is the most likely Path-B vol trigger this cycle. Semis carry the 2nd-highest constituent-level IV on record into 7/29-8/1 (KB-VIO-126).

---

## ACTIVE FORWARD CATALYSTS

> **Source of truth is `workbook/CATALYSTS.tsv`** — this table mirrors it and must not diverge. **Reconciled 2026-08-18** after the two had drifted: this file still showed "Aug 5 (tomorrow)" thirteen days after the fact, and every fired row (8/5 SOQ, 8/7 NFP, 8/7 COT, 8/12 CPI) has now been pruned from the feed and recorded under **Resolved** below.

> ⚠️ **DAY-COUNTS REMOVED 2026-08-20, and the reason is that they had ALREADY ROTTED.** This table carried "(Fri, 3d)" / "(Wed, 6d)" / "(Thu, 7d)" stamped on **8/18** — by today those read 1d / 4d / 5d, so every countdown in the human twin was wrong by two days while the machine feed was exactly right. **A hand-typed countdown is a date that decays every single session**, which is the same lesson the DATA REFRESH SCHEDULE below already learned the hard way. **Dates are kept; countdowns come from `scripts/catalyst_countdown.py`, which derives them at run time and cannot rot.**

| Date | Event | VIX Implication | VIOLET Checkpoint |
|------|-------|-----------------|-------------------|
| **Sep 11 (Fri)** | **August CPI, 8:30 ET** | Macro trigger | 🟠 **HIGH. Date VERIFIED** (`PROME/DOCKET.tsv`; was carried fleet-wide as ~9/10). ⚠️ **Added to the feed 8/18** — it had been flagged VERIFIED since 8/4 but lived only inside another row's note field, which is not a feed. |
| **Sep 16 (Wed)** | **FOMC Rate Decision + SEP + dot plot, 14:00 ET** | Macro trigger | 🔴 **THE NEXT MAJOR DATED GATE.** First SEP after the 6/17 hike-signal flip; tests dot-plot follow-through. Quarterly expiry stacks on the same session. **Live OI belongs on STATUS, not here** — this row previously carried a hard 9/16 call-OI figure that was 2 weeks stale by 9/4. Current values: `STATUS.md` Signal Dashboard. |
| **Sep 16 (Wed)** | **VIX September expiration (quarterly) — AM settle** | OPEX | 🔴 **SPLIT OUT OF THE COMBINED ROW 2026-09-04** — `CATALYSTS.tsv` carries FOMC and the expiry as **two** rows and this file carried them as **one**, so a 1:1 twin check could not tell whether both were represented. **The expiry SETTLES IN THE MORNING, hours before the 14:00 statement** — the expiring VX/U6 cannot price the decision at all; the premium sits in **October (VX/V6), which becomes M1 that morning**. ⚠️ **`VX_DAILY.m1m2_adj_pct` BASIS BREAK here** (KB-VIO-218): the 9/15→9/16 change measures a **contract roll, not a market move**. |
| **Sep 18 (Fri)** | **SPX September quarterly OPEX — triple witching** | OPEX / dealer-gamma re-measure | 🟠 **MEDIUM, ADDED 2026-09-11 — and it was MISSING FROM BOTH FEEDS while HENRY carried it and WALTER routed a signal on it.** **~$9.6T of US options exposure expires between 9/10 and 9/18 (~35% of total US options exposure); ~$6.2T expires ON 9/18 (~23%)**, tracking to beat June's $7.7T record. ⚠️ **Provenance stated rather than assumed: this traces to a Citadel Securities publication, NOT merely the X post that relayed it — but a direct fetch of the Citadel page returned HTTP 403, so the 9.6/6.2 split is INFERRED from a search extract, not read at the primary. The shape (largest quarterly OpEx of the year) survives either way.** 🔑 **HENRY owns dealer gamma and its instruction is explicit: re-measure the board BEFORE this date** — its last measurement is 9/4 on the 9/3 close and its own finding is a one-session shelf life. **VIOLET owns only the transmission read; this is NOT a leg of any VIOLET gate — no base rate for it exists at this desk.** |
| **Sep 30 (Wed)** | **Micron (MU) FQ4 earnings — ✅ `date_class` CONFIRMED, AFTER THE CLOSE (16:30 ET)** | Path-B concentration trigger | 🟡 **MEDIUM.** ✅ **CORRECTED 2026-09-04 to Sep 30 — and the correction is against myself, twice over.** Micron announced it on **2026-08-26 16:01 ET**; I verified the release myself 9/4 rather than take the relay. ⚠️ **My ORIGINAL value was ~Sep 29 ESTIMATED — one day off. On 9/2 I "reconciled" it to VULCAN's ~9/22 derivation (8 days off), and on 9/4 I propagated that into this file as a "twin divergence fix." I overwrote the closer value with the further one TWICE, each time believing I was improving data quality.** VULCAN self-corrected the same 9/2 (their 91-day spacing silently assumed a 52-week FY; MU runs **52/53-week** and FY2026 is a **53-week** year ending 2026-09-03, so EDGAR `fiscalYearEnd=0903` was right all along) — **and that correction sat unread in my top-level inbox for 2 days while I made the second propagation.** 🔑 **Consequence: at 9/30 MU falls OUTSIDE `VIO-FOMC-0916` leg 2's grade window (9/16→9/23) — the named confound on leg 2 is WITHDRAWN and leg 2 grades clean.** The frozen letter never named MU (verified by grep), so this corrects my commentary, not the letter. ⚠️ **After the close on 9/30** — anything resolving *on* 9/30 off this print has ~0 hours headroom. VULCAN owns the substance. → KB-VIO-235 |

## RESOLVED — fired catalysts and their grades

*Pruned from `workbook/CATALYSTS.tsv` on 2026-08-18. **Kept here because pruning has a trigger (the event fires) and grading has none** — an obligation that lives only on the row that gets deleted dies with it (KB-VIO-196).*

| Date | Event | Outcome |
|------|-------|---------|
| **Sep 7 (Mon)** | Labor Day — US equity & options markets CLOSED | ✅ **FIRED AND GRADED — it did the one job it was added for, and the grade is RED's, not mine.** It was added 9/4 purely as sustain-count arithmetic, and the count it governs landed on the other side of it: **`^SKEW` 148.86 on 9/8 broke the 150.63 [9/3] · 151.58 [9/4] run ON ITS VALUE**, so RED's 9/9 ruling (FT-10 = **0-of-4**) never needed the bridge to be decisive. ✅ **The non-session ruling is nonetheless CORROBORATED AT THE PUBLISHER, found 2026-09-11: CBOE's `VIX_History.csv` carries a 09/07/2026 bar at 15.30 while `VIX9D`, `VIX3M`, `VVIX` and `SKEW` all OMIT it** — the grading source has no Labor Day bar, so it is a fact about the file rather than an interpretation. ⚠️ **Durable and unchanged: any desk deriving a SESSION CALENDAR from a CBOE index CSV will over-count by exactly the holidays** (14 such orphan-VIX dates now in the VIOLET window). `catalyst_countdown.py`'s NYSE holiday table stands. |
| **Aug 21** | CFTC COT release (report-date 8/18) | ⚠️ **FIRED. Moved out of ACTIVE FORWARD 2026-09-04** — it had sat under a forward heading for **14 days after firing**, found by `twin_check.py` on its first bidirectional run (external review, Codex). Positioning has been consumed since: current read is **−30,143 / p42.3 [8/25 report]**, third consecutive deepening. |
| **Aug 26** | NVIDIA Q2 FY2027 earnings (after close) | ⚠️ **FIRED. Moved out of ACTIVE FORWARD 2026-09-04**, same 14-day-stale batch. Not separately graded by VIOLET — no VIOLET gate was keyed to it beyond the Path-B concentration watch. **VULCAN owns the substance.** |
| **Aug 27** | Jackson Hole 8/27-29 — Warsh keynote 8/28 AM | ⚠️ **FIRED. Moved out of ACTIVE FORWARD 2026-09-04**, same batch. Not separately graded by VIOLET. The regime read it fed is carried in the thesis, not in this row. |
| **Aug 19** | **VIX August expiration (monthly)** | ✅ **FIRED — and it RESOLVED a registered open hypothesis, which is the only reason it is graded at all.** My 8/18 SCRATCH flagged *"pin/roll is an untested alternative to fear and I did not discriminate it."* The expiry discriminated it: **VIX9D 13.59 [8/18] → 12.66 [8/19, expiry] → 14.39 [8/20, +13.7%]** — the bid FELL into the pin and made a new high the session AFTER the 3.63M call OI cleared. **If pin/roll were the driver the bid dies with the expiry. It did not.** ⇒ expiry mechanics RULED OUT. → **KB-VIO-204** |
| **Aug 19** | **FOMC MINUTES — July 28-29 meeting, 14:00 ET** | ⚠️ **FIRED, NOT GRADED BY VIOLET, AND SAYING SO RATHER THAN IMPLYING A READ.** No VIOLET gate was keyed to the minutes. **The one fact I do own: vol FELL on the day** — VIX 15.84 [8/18] → **14.89 [8/19]**, VIX9D −6.8%, VVIX 92.87 → 86.53. ⚠️ **Do NOT read that as "the minutes were dovish"** — the same session carried the monthly expiry and a second day of the semis selloff, and I have not separated them. **Absorbed without a vol event; attribution not established.** CARL/HENRY own the policy content. |
| **Aug 5** | **VIX Aug-05 weekly SOQ — pre-registered grader for `TRY-VIOLET-VIXCS`** | ✅ **GRADED 8/18 (13 days late). Line >20.45 NOT MET, decisively** — ^VIX 8/5 opened 16.15 with a session **high of 18.43**, so the line sat 2.02 pts above the day's high and 4.30 pts (26.6%) above the open. **Exiting beat holding.** Scorecard: my KB-VIO-144 fade verdict ✅ · my no-re-entry call ✅ · TERRY's DTE-bucketed forward beta **NOT GRADED** (needs the M1 path, not pulled — recorded ungraded rather than scored by assertion) · HENRY's short-gamma steelman ⚠️ **PARTIAL** (the 18.43 intraday spike is the shape described; it retraced to a 15.81 close). ⚠️ **Does NOT grade the exit RULE** — EV-neutral by construction, needs n>1. → **KB-VIO-196** |
| **Aug 7** | NFP July + U-3 | Fired. Not separately graded by VIOLET; no VIOLET gate was keyed to it beyond boxing cheap-tail L4. |
| **Aug 7** | CFTC COT release (report-date 8/4) | ✅ **Consumed 8/18** — and it turned out the report was **never ingested into `COT_VIX.tsv`** (the ledger jumped 7/28 → 8/11) because no session ran to collect it. Recovered via `--backfill`; the gross legs answered WALTER's open question. → **KB-VIO-194** |
| **Aug 12** | July CPI | Fired. Not separately graded by VIOLET. |

---

## WEEKLY MONITORING SCHEDULE

| Day | Task |
|-----|------|
| Sunday | Review week ahead, check VIX expiration proximity |
| Monday | Update VIX data, check term structure, FRED credit refresh |
| Tuesday | Monitor VVIX, SKEW, 20d-avg sensitivity |
| Wednesday | VIX expiration day (if applicable) — watch pinning |
| Thursday | Check credit-vol divergence post-VIX expiry |
| Friday | Week-end summary, update regime status, COT release intake (auto via `cftc_cot.py --boot`) |

---

## DATA REFRESH SCHEDULE

> ⚠️ **This table went a month stale (every row read "2026-07-01" until 7/30) while the pipelines underneath it ran green every boot.** That is the failure mode it exists to prevent, so: **the `Last Updated` column is now a POINTER to where the live vintage actually lives, not a hand-copied date.** Hand-stamped dates in this table rot silently; the ledgers and `boot.py` carry their own content-derived vintages and cannot. Do not re-introduce transcribed values here.

| Data Source | Frequency | Tool | Where the live vintage lives |
|-------------|-----------|------|------------------------------|
| VIX/VIX9D/VIX3M/VVIX/SKEW spot | Every boot (auto in boot.py) | `scripts/thresholds.py` / yfinance | `workbook/VX_DAILY.tsv` last row + its `basis` (TICK/SETTLE) and `m1m2_settle_date` columns. ⚠️ **TICK ≠ the daily record** — EOD `--supersede` after 16:15 ET writes the SETTLE. |
| FRED credit (HY/IG/CCC + ladder + global) | Every boot (`--summary`; FRED lands ~11:30 ET **T+1**, KB-VIO-060) | `scripts/fred_fetch.py --summary` | boot.py credit-gate block prints the FRED **data-date** with the verdict. Never cite it as "today." |
| FRED rates (2Y/10Y/TIPS) | Manual session step | `scripts/fred_fetch.py` | Script output (10Y is HENRY-owned — reference, don't keep a copy). |
| 20d SKEW avg + 5td_change | Per boot during knife-edge | inline calc / `skew_trajectory.py` | Recompute; ⚠️ **^SKEW: same-day availability observed; publication timing UNVERIFIED (KB-VIO-269 scope-corrects the `~17:00` in KB-VIO-137). Grade when the dated CBOE bar is available; say "not yet published today," never "T+1" and never an assumed hour.** |
| Catalyst countdown | Every boot (auto) | `scripts/catalyst_countdown.py` | `workbook/CATALYSTS.tsv` (source of truth; this file is its human twin and must not diverge). |
| VIX options OI | Every boot (auto) | `scripts/vix_options.py` | `workbook/VIX_OPTIONS.tsv`. ⚠️ **After-hours runs print OI=0** — artifact; use the volume ratio or re-run intraday. |
| VX_DAILY time series | Daily (auto-append at boot; `--supersede` at EOD) | `scripts/thresholds.py`, `scripts/backfill.py` for gaps | `workbook/VX_DAILY.tsv`. ⚠️ **CORRECTED 2026-09-06 — this cell said "gaps surfaced by `ledger_staleness.py` at boot step 5b" and that was FALSE.** `ledger_staleness.py` measures **VINTAGE, NOT GAPS**: it reads the newest row's date, so a ledger appended-to today passes with any number of holes behind it. It ran rc=0 on 2026-09-06 while four sessions were missing (8/28 · 8/31 · 9/1 · 9/3) **inside the live FT-10 window**. Gaps are now surfaced by **`scripts/vx_daily_gapcheck.py`** — boot stage (warns) + `closeout_guard.py` 8th contract (BLOCKS). Values are reconciled separately by `skew_integrity.py` and by `backfill.py`'s CBOE pass; **a gap check and a value check are complements, and neither substitutes for the other.** |
| **Canaries — JPY / OVX / cheap-tail** | Every boot (auto) | `jpy_vol.py`, `ovx.py`, `cheap_tail.py` | `workbook/{JPY_VOL,OVX,CHEAP_TAIL}.tsv`. 🆕 **Upsert since 7/30 (KB-VIO-160)** — a re-run UPDATES today's row and prints `🔴 STATE CHANGED`; previously first-write-wins froze the day at its earliest read. |
| Implied correlation (KB-VIO-126) | Every boot (auto) | `scripts/implied_corr.py` | `workbook/IMPLIED_CORR.tsv`. ⚠️ **Cannot be backfilled** — yfinance has no `^COR*` daily history; the series only exists if boot runs. |
| CFTC COT VIX futures | Weekly Fri 3:30pm ET (auto) | `scripts/cftc_cot.py --boot` | `workbook/COT_VIX.tsv`; grade off the raw `f_disagg` file, not Socrata (which lags the 3:30 post). |
| VX term/settlement history | On demand (built 7/30) | `scripts/vx_history.py` | `workbook/VX_TERM_HISTORY.tsv` — 28,555 contract-days, 2013→current, **free** from CBOE's contract-keyed endpoint (KB-VIO-158). |
| NAAIM + ICI equity positioning | Weekly Wed/Thu | *(no tool — never built)* | **NOT BUILT / not wired.** Standing gap, carried deliberately. ⚠️ **This row named `scripts/equity_positioning.py` until 2026-08-18; that file has never existed anywhere in the repo** (PROME verified repo-wide 8/16 via `firetime_check.py --window 90`). The row was already annotated NOT BUILT, so the gap was disclosed — but the tool column still named a path, which reads as an instrument that could be run. **Naming a phantom tool beside an honest 'not built' label is worse than naming none.** |

**Boot sequence:** `boot.py` runs thresholds → fred_fetch `--summary` (credit gate) → vix_options → cftc_cot → jpy_vol → ovx → cheap_tail → implied_corr → catalyst_countdown → CANARY_MAP staleness contract.

---

*Created: 2026-04-12*
*Last Updated: **2026-09-11 ~01:3x ET** (PROME-spawned VECTOR-2 session. **Sep 7 Labor Day FIRED — graded into RESOLVED, pruned from the feed**, with the durable half kept: CBOE's `VIX_History.csv` publishes a holiday VIX bar the other five series omit, so a session calendar derived from a CBOE index CSV over-counts by exactly the holidays. **ADDED: Sep 18 SPX quarterly OPEX / triple witching** — it was absent from BOTH twins while HENRY carried it and WALTER routed a signal on it; magnitude ~$6.2T on the day / ~$9.6T from 9/10, traced to a Citadel Securities publication with the 403-fetch caveat stated on the row. Twin check 5/5 clean.)* Prior: **2026-08-18 ~10:00 ET** (boot session. **Twin RECONCILED with `CATALYSTS.tsv` and verified via `catalyst_countdown.py`** — the two had genuinely diverged: this file still headed its forward table with "Aug 5 (tomorrow)" **thirteen days after the fact**, and carried 8/7 and 8/12 as live. Four fired rows pruned from the feed and moved to the new **RESOLVED** section — which exists because the 8/5 SOQ grade, pre-registered and marked 🔴 as SCRATCH's #1 priority, **went unexecuted for 13 days and would have been deleted along with its row.** Graded this session → KB-VIO-196. **Added:** COT report-date 8/18 (Fri 8/21 — first positioning read that post-dates the 8/17 vol bid), **Aug CPI 9/11** (verified since 8/4 but never promoted out of another row's note field into an actual row), and **MU FQ4 ~9/22 flagged DATE-ESTIMATED** per WALTER SIG-W-20260807-001. **Aug-19 expiry row now carries the pin/roll caveat** — VIX9D rose 16.8% two days out and expiry mechanics are an untested alternative to reading it as fear.)*

*Superseded stamp: **2026-08-04 ~15:15 ET** (full currency pass, Will-directed. **Forward set REPLENISHED, and the replenishment is the point:** July CPI **8/12** added on PROME's correction — my 8/4-AM note asserted "no confirmed date exists anywhere in the fleet" and `PROME/DOCKET.tsv:67` had carried it **DATE VERIFIED** the whole time. **Refusing to invent a date was right; not consulting the canonical fleet ledger was not.** Aug CPI **9/11** also date-verified, noted but outside the window. **COT 8/7 added** — the first report date post-dating the 7/30 yen move, i.e. the intervention-vs-unwind discriminator. **KB-VIO-174's credit discriminator added as a dated row** so the obligation is not carried by SCRATCH alone. **Resolved:** the KB-VIO-126 hook (graded, benign branch loses), the 7/31 COT (pulled), the 7/31 BOJ. ⚠️ **Twin verified against `CATALYSTS.tsv` with `catalyst_countdown.py` this session** — and I also fixed the NFP row's *note*, which had hardcoded the wrong July-CPI premise: the KB-VIO-169 stale-note class, caught in the same session that wrote it.)*

*Superseded stamp: **2026-07-31 ~14:20 ET** (scoped grading session. **Twin re-synced to `CATALYSTS.tsv` and verified with `catalyst_countdown.py`** — fired rows pruned (KB-VIO-127 resolution, 7/30 earnings, BOJ), **new 8/3 row added** so KB-VIO-126's hook does not leave the forward surface, **8/5 row's forward-beta figure corrected off the retracted 0.28.** ⚠️ **The twin divergence this session found ran the OTHER way from the usual one:** this file was CURRENT on 7/30 while `CATALYSTS.tsv` — the machine feed `boot.py` actually prints at grading time — was stale. **A twin check that only compares which rows exist will never catch that; the rot was in the notes.** → KB-VIO-169.)*

*Prior stamp: **2026-07-30 ~14:30 ET** (currency pass, Will-directed. **DATA REFRESH SCHEDULE rebuilt**: every row had read "2026-07-01" for a month while the pipelines under it ran green every boot — the hand-stamped `Last Updated` column is replaced by POINTERS to where each live vintage actually lives, because transcribed dates rot silently and content-derived vintages cannot. Table also gains the four instruments built since 7/01 that were absent from it entirely: the three canaries, implied-corr, and the VX term history. **BOJ row flipped 🟠→🔴** — the JPY canary took its first-ever FIRE (RV10 16.13%/p96.9, RV through IV) on a suspected MOF intervention, with the caveat that equity vol did NOT transmit in the same 30 minutes. **Karsan row**: the hold leg is gone, trending to the registered MISS. Jul VIX expiry retired to EXPIRED.)*
*Superseded stamp: 2026-07-27 (post-close settle boot: forward-catalyst set REBUILT — CATALYSTS.tsv carried only 3 forward rows while STATUS treated BOJ + the megacap cluster as live, a twin-divergence the protocol forbids. Added MSFT/META 7/29, **AMZN + AAPL 7/30** (Apple was absent fleet-wide; date verified by own web pull, and it is Cook's final call), BOJ 7/31, COT 7/31, KB-VIO-127 resolution 7/31. FOMC row updated with the live 34.3% July-hike odds per KB-VIO-128. Twin verified via catalyst_countdown.py same session. Prior: 7/23.)*
*Superseded stamp: 2026-07-23 (sit-rep boot: pruned fired July catalysts [7/2–7/16 + MOF 7/22] to Resolved; forward set now FOMC 7/29 (🔴, 4 td) → Aug expiry → Sep FOMC+SEP+quarterly. FOMC row gains the VIOLET crack-leg watch (VIX>20 + inversion <1.0, KB-VIO-122). Twin: CATALYSTS.tsv same-session. Prior: 7/01 five-day-gap boot.)*
