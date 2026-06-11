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
| Jul 28-29, 2026 | FOMC | No SEP. Powell presser only. Decision Wed Jul 29. |
| Sep 15-16, 2026 | FOMC + SEP | Quarterly — critical. Decision Wed Sep 16 = same day as VIX Sep quarterly expiry. *(Day-counts corrected 6/10 vs Fed calendar — were listed Jul 29-30 / Sep 16-17.)* |

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
| **Jun 16** | **BOJ MPM** (carry-unwind vol channel) | As-priced 1.00% hike = priced/non-event; hawkish-of-pricing → Aug-2024-style yen-carry unwind = tail vol catalyst on elevated front-end | 🟡 Vol-transmission edge via SAM (fuel-load 72%→85% danger zone). SAM owns policy call. |
| **Jun 17** | **FOMC + Powell + SEP + VIX June quarterly expiration** | **Primary vol catalyst gate convergence — 4 events same day** | 🔴 Highest-priority forward gate. |
| Jul 15 | VIX July expiration | — | — |
| Jul 29 | FOMC (no SEP) | — | — |

**Resolved (6/10):**
- **6/10 May CPI:** RESOLVED NON-TAIL — headline 0.5/4.2 in-line, core 0.2 SOFT of 0.3 est; energy +3.9 m/m = >60% of the monthly increase (oil→Fed channel confirmed, KB-VIO-080). Print itself = vol relief; concurrent Iran escalation kept the front bid (KB-VIO-081). Row pruned from CATALYSTS.tsv.

**Resolved (6/6):**
- **6/05 R12 knife-edge (5td & 8td paths):** RE-ESTABLISHED 6/05 via 20d-avg = 140.16. Concurrent with VIX +40% NFP-shock (KB-VIO-067 L1 fired forward simultaneously). See KB-VIO-072.
- **6/15 KB-VIO-031 60d-window checkpoint:** RESOLVED HIT via 6/05 VIX +39.7% (Scenario B confirmed at td-58 of the 60d window).

---

## WEEKLY MONITORING SCHEDULE

| Day | Task |
|-----|------|
| Sunday | Review week ahead, check VIX expiration proximity |
| Monday | Update VIX data, check term structure, FRED credit refresh |
| Tuesday | Monitor VVIX, SKEW, 20d-avg sensitivity |
| Wednesday | VIX expiration day (if applicable) — watch pinning |
| Thursday | Check credit-vol divergence post-VIX expiry |
| Friday | Week-end summary, update regime status, COT release intake (auto via `cftc_cot.py --boot` in boot.py) |

---

## DATA REFRESH SCHEDULE

| Data Source | Frequency | Tool | Last Updated |
|-------------|-----------|------|--------------|
| VIX/VIX9D/VIX3M/VVIX/SKEW spot | Every boot (auto in boot.py) | `scripts/thresholds.py` / yfinance | 2026-06-10 (intraday; SKEW T+1) |
| FRED credit (HY/IG/CCC OAS) | Per boot | `scripts/fred_fetch.py` / boot.py | 2026-06-10 (data through 6/8; T+1 publish lag) |
| FRED rates (2Y/10Y/TIPS) | Per boot | `scripts/fred_fetch.py` | ⚠️ series lagging — cache ends 6/5 on 6/9 fetch; diagnosis queued (SCRATCH item 7f) |
| 20d SKEW avg + 5td_change | Per boot during knife-edge | inline calc | 2026-06-09 (thru 6/9 close; margin +0.59) |
| Catalyst countdown | Every boot (auto in boot.py) | `scripts/catalyst_countdown.py` | 2026-06-10 |
| VIX options OI | Every boot (auto in boot.py; evening runs print OI=0 after hours — artifact, use intraday) | `scripts/vix_options.py` | 2026-06-10 |
| VX_DAILY.tsv time series | Daily (auto-append at boot; **EOD `--supersede` run after 16:15 ET on AM-boot days**; gap-check after skipped days, KB-VIO-076) | `scripts/thresholds.py` (schema v2: basis TICK/SETTLE + m1m2_settle_date — m1m2 is T-1 vs row date by tool design, KB-VIO-092); `scripts/backfill.py` for gaps | 2026-06-11 (TICK row; EOD supersede owed) |
| CFTC COT VIX futures | Weekly Fri 3:30pm ET (Tue position-snap; auto in boot.py) | `scripts/cftc_cot.py` (`--boot` freshness-gated; `--backfill` rebuild) | 2026-06-05 release (6/2 positions); next Fri 6/12 |
| NAAIM + ICI equity positioning | Weekly Wed/Thu | `scripts/equity_positioning.py` (**not yet built**) | Not wired |

**Boot sequence:** `python3 scripts/boot.py` runs thresholds + vix_options + cftc_cot + catalyst_countdown.

---

*Created: 2026-04-12*
*Last Updated: 2026-06-10 (housekeeping item 4: CPI resolved-section added AM; FOMC day-counts corrected vs Fed calendar — Jul 28-29, Sep 15-16, decision days unchanged in CATALYSTS.tsv which was already correct; Data Refresh table re-stamped to actual (boot.py automates most rows — "overdue"/"when wired" framings removed); FRED-rates lag flagged. Prior: 6/6 Saturday org session; 6/7 CPI date fix 6/12→6/10.)*
