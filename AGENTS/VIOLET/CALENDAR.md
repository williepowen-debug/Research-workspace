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
| **Jul 2026** | **Jul 15** | Standard monthly. FOMC Jul 29 same month. |
| Aug 2026 | Aug 19 | — |
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

**Pattern:** Earnings season = vol supply as single-stock vol gets realized. **Concentration watch:** with record AI/semi concentration (47%) + record levered-ETF exposure ($464bn), a single AI-name earnings gap is the most likely Path-B vol trigger this cycle.

---

## ACTIVE FORWARD CATALYSTS

| Date | Event | VIX Implication | VIOLET Checkpoint |
|------|-------|-----------------|-------------------|
| Jun 30 | Quarter-end rebalance (~$165B equity sell, JPM) | Recognized near-month-end vol-bump into a record-levered tape | 🟡 Watch (HENRY owns flows; WALTER SIG-008). |
| Jul 15 | VIX July expiration | Standard monthly | ⚪ Low. |
| Jul 29 | FOMC (no SEP, Warsh) | Tests 6/17 dot-flip follow-through | 🟠 First gate of the Fed-HIKE regime. |
| Sep 16 | FOMC + SEP + VIX Sep quarterly expiry | Quarterly dot-plot convergence | 🟠 Next major gate. |

**Note:** the dominant near-term tail is now UNSCHEDULED — the Path-B concentration/leverage unwind (record $464bn levered-long, AI 47% concentration, negative gamma). No calendar date; external trigger.

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

| Data Source | Frequency | Tool | Last Updated |
|-------------|-----------|------|--------------|
| VIX/VIX9D/VIX3M/VVIX/SKEW spot | Every boot (auto in boot.py) | `scripts/thresholds.py` / yfinance | 2026-06-23 (boot, TICK; SKEW T+1) |
| FRED credit (HY/IG/CCC + ladder BB/B/BBB + global Euro/EM) | **Manual session step**; print lands ~11:30 AM ET T+1 | `scripts/fred_fetch.py --force` | ⚠️ **2026-06-23 BROKEN** — HY+IG frozen at 2025-04-01; CCC/BB/B/BBB stuck at 6/11; only EuroHY reached 6/22. **Fix queued 🔴 (KB-VIO-103). Reference LIQUID for HY.** |
| FRED rates (2Y/10Y/TIPS) | Manual session step | `scripts/fred_fetch.py` | 2026-06-23 (fetched; 10Y owned by HENRY) |
| 20d SKEW avg + 5td_change | Per boot during knife-edge | inline calc | ⚠️ recompute owed (daily series backfilled thru 6/18; R12 regime intact, 140+) |
| Catalyst countdown | Every boot (auto in boot.py) | `scripts/catalyst_countdown.py` | 2026-06-23 (boot — next 7/15) |
| VIX options OI | Every boot (auto in boot.py; evening runs print OI=0) | `scripts/vix_options.py` | 2026-06-23 (boot) |
| VX_DAILY.tsv time series | Daily (auto-append at boot; EOD `--supersede` after 16:15 ET) | `scripts/thresholds.py` / `scripts/backfill.py` for gaps | 2026-06-23 TICK row; 6/15-6/18 backfilled. **6/22 absent (yf companion ^-indices lag; re-backfill).** |
| CFTC COT VIX futures | Weekly Fri 3:30pm ET (auto in boot.py) | `scripts/cftc_cot.py` | 2026-06-23 boot pulled 6/16 positions (Lev Money −13,295 / 79.5 ELEVATED_LONG — war now in data); next Fri 6/26 (6/23 positions) |
| NAAIM + ICI equity positioning | Weekly Wed/Thu | `scripts/equity_positioning.py` (**not yet built**) | Not wired |

**Boot sequence:** `python3 scripts/boot.py` runs thresholds + vix_options + cftc_cot + catalyst_countdown.

---

*Created: 2026-04-12*
*Last Updated: 2026-06-23 (boot after 9-day dark: catalyst window 6/16-17 moved to Resolved; Powell→Warsh corrected throughout — Warsh chaired the 6/17 hawkish dot-flip; forward catalysts refreshed (next 7/15, 7/29 Warsh, 9/16); Jun 30 quarter-end rebalance added; Data Refresh re-stamped incl. fred_fetch BROKEN flag. Prior: 6/14 stale-data audit.)*
