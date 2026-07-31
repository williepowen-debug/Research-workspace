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
| **Aug 2026** | **Aug 19** | Next monthly. ⚠️ **Aug-05 weekly SOQ (8/5) is the live one** — the pre-registered grader for `TRY-VIOLET-VIXCS`. |
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

| Date | Event | VIX Implication | VIOLET Checkpoint |
|------|-------|-----------------|-------------------|
| **Jul 31 (today)** | COT release **15:30 ET** (report-date 7/28) | Positioning | 🟡 **Releases after the 7/31 session closed — pull it at the next boot.** Did the lev-money unwind continue through FOMC? ⚠️ **The 7/28 report date PREDATES the 7/30 yen move, so it cannot speak to the carry leg** — the **8/4-data** print is the first that can. KB-VIO-144 confirm-2 rematch (needs pct3y ≥95; last 92.9). |
| **Aug 3 (Mon)** | 🆕 **KB-VIO-126 implied-corr falsification hook grades** (window closed 8/1) | Suppression-mechanism test | 🟠 **Grade the REGISTERED two conditions on 8/1-CLOSE values, not on ticks and not on a paraphrase (KB-VIO-156).** Hook: *correlations RISE and single-stock vol FALLS through the 7/29–8/1 cluster → the benign typical-earnings pattern wins.* ⚠️ **Condition 1 has run against the benign branch every session: COR1M 11.97 → 8.43 → 7.06 → 6.78 [7/31].** Row added to `CATALYSTS.tsv` 7/31 when the fired 7/30 earnings row was pruned. |
| **Aug 5** | **VIX Aug-05 weekly SOQ — the PRE-REGISTERED grader for `TRY-VIOLET-VIXCS`** | Counterfactual line **20.45** | 🔴 **Registered BEFORE the 7/30 exit** (TERRY card 11.C; TERRY P≈20%). Holding beat exiting **iff SOQ >20.45**. ⚠️ **Does NOT grade the exit rule** — the exit was at fair two-sided price, so it is **EV-neutral by construction** and a rule needs n>1. **It DOES grade: my KB-VIO-144 fade verdict · my no-re-entry call · TERRY's forward-beta finding · HENRY's short-gamma steelman.** ⚠️ **CITE THE CORRECTED BETA, NOT 0.28** — TERRY self-audited 0.28 → 0.53 and I re-derived it independently (n=246 OLS, DTE-bucketed): **0.274 @21–35 · 0.505 @11–20 · 0.591 @≤10**. At the SOQ's ≤10 DTE the registered figure is **~0.59**; grading against 0.28 would score a retracted number (KB-VIO-154/169). Score all four, including against me. |
| Aug 19 | VIX August expiration | Standard monthly | ⚪ Low. |
| Sep 16 | FOMC + SEP + VIX Sep quarterly expiry | Quarterly dot-plot convergence | 🟠 Next major gate. |

**Resolved (7/31):** **KB-VIO-127 (Karsan month-end vol-shock call) → MISS**, the registered base case. ≥23 touch never happened (window max **20.88 [7/29]** = episode max); the >20 settle-and-hold leg **fired its settle half** (20.66 [7/29], the episode's only one) and **broke its hold half** the next session (17.09). Fall-flows half **formally dropped** per the registration's own terms → KB-VIO-169. · **BOJ MPM decided** (~22:30–23:00 ET 7/30 = 7/31 JST) — **VIOLET did not read the outcome and does not relay it; SAM owns it.** What I measured: **USD/JPY 158.19, RV10 16.71%/p97.7, RV back through IV, canary 🔴 FIRE a second session** — the move **did not** round-trip — **while index vol printed episode lows** (VIX 16.57 / VVIX 90.84). "Loaded and not transmitting" now n=2, having survived the event that could have broken it → KB-VIO-171. · **AMZN/AAPL AH results are in but NOT graded here** — the KB-VIO-126 hook grades 8/3 on 8/1-close values.

**Resolved (7/29–7/30) — the FOMC week:** **FOMC 7/29** held 9-3 with three hawkish dissents, guidance withdrawn; VIX 17.45→**20.88**, settle **20.66** = the first >20 settle of the episode (KB-VIO-143/144; **KB-VIO-128 resolved CORRECT** — it said 65.7% HOLD). · **MSFT +3% / META −10% AH** = maximum dispersion, KB-VIO-126 now 2-for-2 that megacap violence arrives *divergently* and index vol does not follow. · **SK hynix Q2** (VULCAN owns). · **`TRY-VIOLET-VIXCS` CLOSED 7/30, −$111.60 / −38.8%** — zero of five stand-downs ever tripped; closed by its dated mandate (KB-VIO-154).

**Resolved (7/2–7/22):** June jobs 7/2 (Gate B NO-FIRE, KB-VIO-111) · post-DISH CCC 7/2 · SK Hynix ADR ~7/10 · June CPI 7/14 · VIX July expiry 7/15 · Japan TIC/MOF/BoK 7/16 · **MOF ITS 7/22 — passed clean (USDJPY 163.82 weakened, no carry unwind; jpy_vol canary CALM).**

**Note:** the Path-B unwind is **unresolved and broadened** (KB-VIO-106) — bear case now oversupply-2028 + demand-destruction + antitrust, with a standing offshore mechanical amplifier (KOSPI 2x single-stock ETFs, ~$9B, jawboning-only response). Undated watch lines: KOSPI 8,200 (crash close — break re-opens contagion) · Korea FSS leveraged-ETF ruling (vol-suppressing if it lands) · SKEW >150 sustain count (1/4 td toward prediction-#6 re-arm).

**Resolved (7/2):**
- **7/2 June employment (8:30 ET):** +57K big miss / net revisions −74K / U-3 4.2% via participation −0.3pp (supply artifact) / AHE 3.5%↑ = **stagflationary mix**; tape evolved dovish-muted → hawkish-lean (10Y 4.50 +3bp) — absorbed by the freshly-POSITIVE gamma regime (+$35B, HENRY). **Gate B NO-FIRE (KB-VIO-111).** Candidate MOF yen strike on the 8:30 bar (162.5→160.7, UNCONFIRMED — SAM). +57K single-source, re-verify.

**Resolved (6/24-6/30) — the gap window:**
- **6/24 MU Q3 AH:** blowout beat (rev $41.46B vs $35.69B est; HBM booked thru CY2027) → MU +15.7% 6/25 — then the sector relapsed 6/26 (Samsung/SK-Hynix capex-leak oversupply read) and again 7/1 (MU −10.6%, below its 6/23 panic close). The fork "cleared" for one session; unwind unresolved (KB-VIO-106).
- **6/25 May PCE:** headline 4.1% YoY in-line / core 3.4% (+0.1); monthly prints soft → read softer-than-feared; 10Y to 4.36% by 6/29 — then re-hawked 6/30-7/1 (Warsh Sintra, ISM 53.3): 10Y ~4.50, ~70% Sep-hike odds (KB-VIO-109).
- **6/30 Quarter-end rebalance:** front-ran itself into the 6/23-6/26 chop, absorbed via rotation — SPX +1.18%/+0.79% on the peak-flow days; Q2 closed +14.9% (best since 2020), SOX +87.8%. Mechanical-flow excuse for SKEW extension now CLEARED (KB-VIO-108).

**Resolved (6/16-17) — the catalyst window:**
- **6/16 BOJ MPM:** As-priced 1.00% hike (7-1, Asada dovish dissent); yen WEAKENED to ~160.4, NO carry unwind (Aug-2024 analog did not replay). Carry → Sep-18 convexity tail (SAM; 60d unwind 24-28%). Vol-DEFUSED.
- **6/17 FOMC + SEP (Warsh's first) + VIX June quarterly + M1 expiry:** see FOMC table. Hawkish dot-flip, +12% spike faded, counter 0/5, Fed-HIKE regime. Expiries clean.

**Resolved (6/10):**
- **6/10 May CPI:** NON-TAIL — headline in-line, core soft; energy +3.9% m/m = >60% of the increase (oil→Fed channel, KB-VIO-080). Print = vol relief; concurrent Iran escalation kept the front bid (KB-VIO-081).

**Resolved (6/6):**
- **6/05 R12 knife-edge:** RE-ESTABLISHED 6/05 via 20d-avg 140.16, concurrent with VIX +40% NFP-shock (KB-VIO-067/072).
- **6/15 KB-VIO-031 60d-window checkpoint:** RESOLVED HIT via 6/05 VIX +39.7% (Scenario B at td-58).

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
*Last Updated: **2026-07-31 ~14:20 ET** (scoped grading session. **Twin re-synced to `CATALYSTS.tsv` and verified with `catalyst_countdown.py`** — fired rows pruned (KB-VIO-127 resolution, 7/30 earnings, BOJ), **new 8/3 row added** so KB-VIO-126's hook does not leave the forward surface, **8/5 row's forward-beta figure corrected off the retracted 0.28.** ⚠️ **The twin divergence this session found ran the OTHER way from the usual one:** this file was CURRENT on 7/30 while `CATALYSTS.tsv` — the machine feed `boot.py` actually prints at grading time — was stale. **A twin check that only compares which rows exist will never catch that; the rot was in the notes.** → KB-VIO-169.)*

*Prior stamp: **2026-07-30 ~14:30 ET** (currency pass, Will-directed. **DATA REFRESH SCHEDULE rebuilt**: every row had read "2026-07-01" for a month while the pipelines under it ran green every boot — the hand-stamped `Last Updated` column is replaced by POINTERS to where each live vintage actually lives, because transcribed dates rot silently and content-derived vintages cannot. Table also gains the four instruments built since 7/01 that were absent from it entirely: the three canaries, implied-corr, and the VX term history. **BOJ row flipped 🟠→🔴** — the JPY canary took its first-ever FIRE (RV10 16.13%/p96.9, RV through IV) on a suspected MOF intervention, with the caveat that equity vol did NOT transmit in the same 30 minutes. **Karsan row**: the hold leg is gone, trending to the registered MISS. Jul VIX expiry retired to EXPIRED.)*
*Superseded stamp: 2026-07-27 (post-close settle boot: forward-catalyst set REBUILT — CATALYSTS.tsv carried only 3 forward rows while STATUS treated BOJ + the megacap cluster as live, a twin-divergence the protocol forbids. Added MSFT/META 7/29, **AMZN + AAPL 7/30** (Apple was absent fleet-wide; date verified by own web pull, and it is Cook's final call), BOJ 7/31, COT 7/31, KB-VIO-127 resolution 7/31. FOMC row updated with the live 34.3% July-hike odds per KB-VIO-128. Twin verified via catalyst_countdown.py same session. Prior: 7/23.)*
*Superseded stamp: 2026-07-23 (sit-rep boot: pruned fired July catalysts [7/2–7/16 + MOF 7/22] to Resolved; forward set now FOMC 7/29 (🔴, 4 td) → Aug expiry → Sep FOMC+SEP+quarterly. FOMC row gains the VIOLET crack-leg watch (VIX>20 + inversion <1.0, KB-VIO-122). Twin: CATALYSTS.tsv same-session. Prior: 7/01 five-day-gap boot.)*
