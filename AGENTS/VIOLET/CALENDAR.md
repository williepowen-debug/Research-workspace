# VIOLET CALENDAR

VIX-specific catalysts and monitoring schedule. **Source of truth for dated catalysts: `workbook/CATALYSTS.tsv`** (machine feed for `scripts/catalyst_countdown.py`). This file is the human twin and must not diverge.

---

## VIX EXPIRATION DATES (Monthly)

VIX futures and options expire on the **Wednesday 30 days prior to the third Friday of the following month**.

| Month | Expiration Date | Notes |
|-------|-----------------|-------|
| ~~Apr 2026~~ | Apr 15 | EXPIRED |
| ~~May 2026~~ | May 20 | EXPIRED. Episode-17 VIX 25C expired worthless 5/19 (VIX ~18 vs strike 25). |
| **Jun 2026** | **Jun 17** | **Quarterly — high volume. Same day as FOMC + SEP. Critical convergence.** |
| Jul 2026 | Jul 15 | FOMC Jul 29-30 same week |
| Aug 2026 | Aug 19 | — |
| Sep 2026 | Sep 16 | Quarterly (same day as FOMC + SEP) |

**Pin risk:** VIX tends to drift toward strikes with high open interest near expiration.

---

## FOMC MEETINGS (Vol Events)

| Date | Meeting | VIX Watch |
|------|---------|-----------|
| ~~Apr 28-29, 2026~~ | FOMC | DONE — held 3.50-3.75%, 4 dissents (most since Oct 1992). VIX did NOT spike. |
| **Jun 17, 2026** | **FOMC + SEP** | **Primary vol catalyst gate. First post-Apr-dissent dot plot. Coincides with VIX June quarterly expiration + 60d window expiry on KB-VIO-031. FedWatch ~80% hold (verify at boot).** |
| Jul 29-30, 2026 | FOMC | No SEP. Powell presser only. |
| Sep 16-17, 2026 | FOMC + SEP | Quarterly — critical |

**Pattern:** VIX typically rises into FOMC, drops on outcome if no surprise. In current regime (5+ consecutive catalyst absorption per KB-VIO-062), pattern may be muted by GEX-suppression mechanism — refresh hypothesis on each FOMC outcome.

---

## EARNINGS SEASONS (Vol Supply)

| Quarter | Peak Earnings | VIX Impact |
|---------|---------------|------------|
| ~~Q1 2026~~ | Apr 15-May 2 | DONE — vol supply realized, VIX did not spike |
| Q2 2026 | Jul 15-Aug 1 | — |
| Q3 2026 | Oct 15-Nov 1 | — |
| Q4 2026 | Jan 15-Feb 1 | — |

**Pattern:** Earnings season = vol supply as single-stock vol gets realized.

---

## ACTIVE FORWARD CATALYSTS

| Date | Event | VIX Implication | VIOLET Checkpoint |
|------|-------|-----------------|-------------------|
| **Jun 05** | **R12 regime re-establishment knife-edge (5td path)** | If SKEW holds 144 daily, 20d-avg crosses 140; regime re-establishes | 🟡 Daily refresh through 6/10. KB-VIO-061. |
| **Jun 09-10** | **R12 re-establishment knife-edge (8td path)** | Latest realistic re-establishment timing before catalyst gate | 🟡 Knife-edge binary resolved by this date. |
| **Jun 12** | **May CPI release** | First named macro test post-R11-window. Hot print = potential vol catalyst. | 🟠 Pre-mortem due 6/08-6/10. |
| Jun 15 | VIOLET SKEW scenario full checkpoint | 60-day window closes on Apr 13 SKEW divergence | 🟡 Scenario A/B/C resolution per KB-VIO-031 |
| **Jun 17** | **FOMC + Powell + SEP + VIX June quarterly expiration** | **Primary vol catalyst gate convergence — 4 events same day** | 🔴 Highest-priority forward gate. |
| Jul 15 | VIX July expiration | — | — |
| Jul 29 | FOMC (no SEP) | — | — |

---

## WEEKLY MONITORING SCHEDULE

| Day | Task |
|-----|------|
| Sunday | Review week ahead, check VIX expiration proximity |
| Monday | Update VIX data, check term structure, FRED credit refresh |
| Tuesday | Monitor VVIX, SKEW, 20d-avg sensitivity |
| Wednesday | VIX expiration day (if applicable) — watch pinning |
| Thursday | Check credit-vol divergence post-VIX expiry |
| Friday | Week-end summary, update regime status, COT data (when wired) |

---

## DATA REFRESH SCHEDULE

| Data Source | Frequency | Tool | Last Updated |
|-------------|-----------|------|--------------|
| VIX/VIX3M/VVIX/SKEW spot | Daily | `scripts/thresholds.py` or yfinance | 2026-06-01 |
| FRED credit (HY/IG/CCC OAS) | Per boot | `scripts/fred_fetch.py` | 2026-06-01 (data through 5/31; T+1 publish lag) |
| FRED rates (2Y/10Y/TIPS) | Per boot | `scripts/fred_fetch.py` | 2026-06-01 |
| 20d SKEW avg + 5td_change | Per boot during knife-edge | inline calc | 2026-06-01 |
| Catalyst countdown | Per boot | `scripts/catalyst_countdown.py` | 2026-06-01 |
| VIX options OI | When notable | `scripts/vix_options.py` | 2026-04-17 (overdue) |
| VX_DAILY.tsv time series | Daily | `scripts/thresholds.py` → append; `scripts/backfill.py` for gaps | 2026-06-01 (backfilled 5/14 → 6/1 EOD; SKEW 6/1 pending T+1) |
| CFTC COT VIX futures | Weekly Fri | `scripts/cftc_cot.py` (**not yet built**) | Not wired |
| NAAIM + ICI equity positioning | Weekly Wed/Thu | `scripts/equity_positioning.py` (**not yet built**) | Not wired |

**Boot sequence:** `python3 scripts/boot.py` runs thresholds + vix_options + catalyst_countdown.

---

*Created: 2026-04-12*
*Last Updated: 2026-06-01 (catch-up session closeout — calendar reconciled with workbook/CATALYSTS.tsv; June 17 FOMC+SEP+VIX quarterly convergence flagged as highest forward gate; knife-edge dates 6/05-6/10 added. Intra-day pass 3: VX_DAILY backfilled 5/14 → 6/1.)*
