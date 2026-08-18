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
| **Aug 2026** | **Aug 19** | 🟡 **TOMORROW (1d).** ✅ The Aug-05 weekly SOQ has been **GRADED** — see **Resolved** below (KB-VIO-196). |
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

| Date | Event | VIX Implication | VIOLET Checkpoint |
|------|-------|-----------------|-------------------|
| **Aug 19 (Wed, 1d)** | **VIX August expiration** | Standard monthly | 🟡 **IMMINENT.** ⚠️ **Directly relevant to the 8/17 front-led bid:** VIX9D rose **+16.8%** into a 2-day-out expiry, and **pin/roll mechanics are an untested alternative explanation to "fear"** (KB-VIO-193). **Discriminate before reading the front-end move as signal.** 8/19 carries the option size — call OI 3.63M vs put 1.25M. |
| **Aug 21 (Fri, 3d)** | **CFTC COT release — report-date 8/18** | Positioning | 🔴 **THE FIRST REPORT DATE THAT POST-DATES THE 8/17 VOL BID.** Latest (8/11) shows leveraged money **net SHORT −12,127** after a failed long round-trip (KB-VIO-194), so current positioning is **invisible** until this print. ⚠️ **Read the GROSS legs, not the net** — the 8/04 gross decomposition (93% new longs) reversed the interpretation of the same number. |
| **Sep 11 (Fri, 18d)** | **August CPI, 8:30 ET** | Macro trigger | 🟠 **HIGH. Date VERIFIED** (`PROME/DOCKET.tsv`; was carried fleet-wide as ~9/10). ⚠️ **Added to the feed 8/18** — it had been flagged VERIFIED since 8/4 but lived only inside another row's note field, which is not a feed. |
| **Sep 16 (Wed, 21d)** | **FOMC + SEP · AND VIX September quarterly expiration — same day** | Macro + OPEX | 🔴 **THE NEXT MAJOR DATED GATE.** First SEP after the 6/17 hike-signal flip; tests dot-plot follow-through. Quarterly expiry stacks on the same session. **9/16 call OI 3.36M with 65C at 251k (+312%) and 25C at 292k** — far-OTM call accumulation already building. |
| **Sep 29 (Tue, ~30d)** | **Micron (MU) FQ4 earnings — ⚠️ DATE ESTIMATED, NOT ANNOUNCED** | Path-B concentration trigger | 🟡 **MEDIUM.** From WALTER `SIG-W-20260807-001`: MU's fiscal Q4 ends ~09/03 and prints late September — **it does NOT report 8/4**, which four earlier signals had hung their sharpest listen-for on. ⚠️ **~9/29 is inferred from prior-year cadence (10-K period 2025-08-28 filed 2025-10-03), NOT published — re-check before it becomes load-bearing.** VULCAN owns the substance. |

## RESOLVED — fired catalysts and their grades

*Pruned from `workbook/CATALYSTS.tsv` on 2026-08-18. **Kept here because pruning has a trigger (the event fires) and grading has none** — an obligation that lives only on the row that gets deleted dies with it (KB-VIO-196).*

| Date | Event | Outcome |
|------|-------|---------|
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
| 20d SKEW avg + 5td_change | Per boot during knife-edge | inline calc / `skew_trajectory.py` | Recompute; ⚠️ **^SKEW publishes ~17:00 ET SAME-DAY** (KB-VIO-137) — before that, say "not yet published today," never "T+1." |
| Catalyst countdown | Every boot (auto) | `scripts/catalyst_countdown.py` | `workbook/CATALYSTS.tsv` (source of truth; this file is its human twin and must not diverge). |
| VIX options OI | Every boot (auto) | `scripts/vix_options.py` | `workbook/VIX_OPTIONS.tsv`. ⚠️ **After-hours runs print OI=0** — artifact; use the volume ratio or re-run intraday. |
| VX_DAILY time series | Daily (auto-append at boot; `--supersede` at EOD) | `scripts/thresholds.py`, `scripts/backfill.py` for gaps | `workbook/VX_DAILY.tsv`; gaps surfaced by `scripts/ledger_staleness.py VIOLET` at boot step 5b. |
| **Canaries — JPY / OVX / cheap-tail** | Every boot (auto) | `jpy_vol.py`, `ovx.py`, `cheap_tail.py` | `workbook/{JPY_VOL,OVX,CHEAP_TAIL}.tsv`. 🆕 **Upsert since 7/30 (KB-VIO-160)** — a re-run UPDATES today's row and prints `🔴 STATE CHANGED`; previously first-write-wins froze the day at its earliest read. |
| Implied correlation (KB-VIO-126) | Every boot (auto) | `scripts/implied_corr.py` | `workbook/IMPLIED_CORR.tsv`. ⚠️ **Cannot be backfilled** — yfinance has no `^COR*` daily history; the series only exists if boot runs. |
| CFTC COT VIX futures | Weekly Fri 3:30pm ET (auto) | `scripts/cftc_cot.py --boot` | `workbook/COT_VIX.tsv`; grade off the raw `f_disagg` file, not Socrata (which lags the 3:30 post). |
| VX term/settlement history | On demand (built 7/30) | `scripts/vx_history.py` | `workbook/VX_TERM_HISTORY.tsv` — 28,555 contract-days, 2013→current, **free** from CBOE's contract-keyed endpoint (KB-VIO-158). |
| NAAIM + ICI equity positioning | Weekly Wed/Thu | `scripts/equity_positioning.py` | **NOT BUILT / not wired.** Standing gap, carried deliberately. |

**Boot sequence:** `boot.py` runs thresholds → fred_fetch `--summary` (credit gate) → vix_options → cftc_cot → jpy_vol → ovx → cheap_tail → implied_corr → catalyst_countdown → CANARY_MAP staleness contract.

---

*Created: 2026-04-12*
*Last Updated: **2026-08-18 ~10:00 ET** (boot session. **Twin RECONCILED with `CATALYSTS.tsv` and verified via `catalyst_countdown.py`** — the two had genuinely diverged: this file still headed its forward table with "Aug 5 (tomorrow)" **thirteen days after the fact**, and carried 8/7 and 8/12 as live. Four fired rows pruned from the feed and moved to the new **RESOLVED** section — which exists because the 8/5 SOQ grade, pre-registered and marked 🔴 as SCRATCH's #1 priority, **went unexecuted for 13 days and would have been deleted along with its row.** Graded this session → KB-VIO-196. **Added:** COT report-date 8/18 (Fri 8/21 — first positioning read that post-dates the 8/17 vol bid), **Aug CPI 9/11** (verified since 8/4 but never promoted out of another row's note field into an actual row), and **MU FQ4 ~9/29 flagged DATE-ESTIMATED** per WALTER SIG-W-20260807-001. **Aug-19 expiry row now carries the pin/roll caveat** — VIX9D rose 16.8% two days out and expiry mechanics are an untested alternative to reading it as fear.)*

*Superseded stamp: **2026-08-04 ~15:15 ET** (full currency pass, Will-directed. **Forward set REPLENISHED, and the replenishment is the point:** July CPI **8/12** added on PROME's correction — my 8/4-AM note asserted "no confirmed date exists anywhere in the fleet" and `PROME/DOCKET.tsv:67` had carried it **DATE VERIFIED** the whole time. **Refusing to invent a date was right; not consulting the canonical fleet ledger was not.** Aug CPI **9/11** also date-verified, noted but outside the window. **COT 8/7 added** — the first report date post-dating the 7/30 yen move, i.e. the intervention-vs-unwind discriminator. **KB-VIO-174's credit discriminator added as a dated row** so the obligation is not carried by SCRATCH alone. **Resolved:** the KB-VIO-126 hook (graded, benign branch loses), the 7/31 COT (pulled), the 7/31 BOJ. ⚠️ **Twin verified against `CATALYSTS.tsv` with `catalyst_countdown.py` this session** — and I also fixed the NFP row's *note*, which had hardcoded the wrong July-CPI premise: the KB-VIO-169 stale-note class, caught in the same session that wrote it.)*

*Superseded stamp: **2026-07-31 ~14:20 ET** (scoped grading session. **Twin re-synced to `CATALYSTS.tsv` and verified with `catalyst_countdown.py`** — fired rows pruned (KB-VIO-127 resolution, 7/30 earnings, BOJ), **new 8/3 row added** so KB-VIO-126's hook does not leave the forward surface, **8/5 row's forward-beta figure corrected off the retracted 0.28.** ⚠️ **The twin divergence this session found ran the OTHER way from the usual one:** this file was CURRENT on 7/30 while `CATALYSTS.tsv` — the machine feed `boot.py` actually prints at grading time — was stale. **A twin check that only compares which rows exist will never catch that; the rot was in the notes.** → KB-VIO-169.)*

*Prior stamp: **2026-07-30 ~14:30 ET** (currency pass, Will-directed. **DATA REFRESH SCHEDULE rebuilt**: every row had read "2026-07-01" for a month while the pipelines under it ran green every boot — the hand-stamped `Last Updated` column is replaced by POINTERS to where each live vintage actually lives, because transcribed dates rot silently and content-derived vintages cannot. Table also gains the four instruments built since 7/01 that were absent from it entirely: the three canaries, implied-corr, and the VX term history. **BOJ row flipped 🟠→🔴** — the JPY canary took its first-ever FIRE (RV10 16.13%/p96.9, RV through IV) on a suspected MOF intervention, with the caveat that equity vol did NOT transmit in the same 30 minutes. **Karsan row**: the hold leg is gone, trending to the registered MISS. Jul VIX expiry retired to EXPIRED.)*
*Superseded stamp: 2026-07-27 (post-close settle boot: forward-catalyst set REBUILT — CATALYSTS.tsv carried only 3 forward rows while STATUS treated BOJ + the megacap cluster as live, a twin-divergence the protocol forbids. Added MSFT/META 7/29, **AMZN + AAPL 7/30** (Apple was absent fleet-wide; date verified by own web pull, and it is Cook's final call), BOJ 7/31, COT 7/31, KB-VIO-127 resolution 7/31. FOMC row updated with the live 34.3% July-hike odds per KB-VIO-128. Twin verified via catalyst_countdown.py same session. Prior: 7/23.)*
*Superseded stamp: 2026-07-23 (sit-rep boot: pruned fired July catalysts [7/2–7/16 + MOF 7/22] to Resolved; forward set now FOMC 7/29 (🔴, 4 td) → Aug expiry → Sep FOMC+SEP+quarterly. FOMC row gains the VIOLET crack-leg watch (VIX>20 + inversion <1.0, KB-VIO-122). Twin: CATALYSTS.tsv same-session. Prior: 7/01 five-day-gap boot.)*
