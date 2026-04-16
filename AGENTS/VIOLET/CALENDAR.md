# VIOLET CALENDAR

VIX-specific catalysts and monitoring schedule.

---

## VIX EXPIRATION DATES (Monthly)

VIX futures and options expire on the **Wednesday 30 days prior to the third Friday of the following month**.

| Month | Expiration Date | Notes |
|-------|-----------------|-------|
| Apr 2026 | Apr 15 | EXPIRED |
| May 2026 | May 20 | FOMC May 6-7 — vol event risk |
| Jun 2026 | Jun 17 | Quarterly expiration — high volume. **60d window expiry checkpoint** |
| Jul 2026 | Jul 15 | — |
| Aug 2026 | Aug 19 | — |
| Sep 2026 | Sep 16 | Quarterly expiration |

**Pin risk:** VIX tends to drift toward strikes with high open interest near expiration.

---

## FOMC MEETINGS (Vol Events)

| Date | Meeting | VIX Watch |
|------|---------|-----------|
| Apr 29-30, 2026 | FOMC | Rate decision + Powell presser |
| Jun 17-18, 2026 | FOMC + SEP | Quarterly — dot plot |
| Jul 29-30, 2026 | FOMC | — |
| Sep 16-17, 2026 | FOMC + SEP | Quarterly — critical |

**Pattern:** VIX typically rises into FOMC, drops on outcome if no surprise.

---

## EARNINGS SEASONS (Vol Supply)

| Quarter | Peak Earnings | VIX Impact |
|---------|---------------|------------|
| Q1 2026 | Apr 15-May 2 | Vol supply — VIX tends to fall |
| Q2 2026 | Jul 15-Aug 1 | — |
| Q3 2026 | Oct 15-Nov 1 | — |
| Q4 2026 | Jan 15-Feb 1 | — |

**Pattern:** Earnings season = vol supply as single-stock vol gets realized.

---

## KNOWN CATALYSTS (Forward)

| Date | Event | VIX Implication | VIOLET Checkpoint |
|------|-------|-----------------|-------------------|
| ~~Apr 15~~ | ~~VIX expiration~~ | PASSED | — |
| Apr 16 | OZK earnings | Regional bank vol | — |
| Apr 21 | WAL earnings | Regional bank vol | — |
| Apr 23-24 | BOJ meeting | Carry unwind risk (yen analog) | — |
| **Apr 29-30** | **FOMC** | **Rate vol. C/P OI 9.01 on this expiry** | **🔴 SKEW Scenario A/B early read** |
| May 1 | US payrolls | Macro vol | — |
| May 6-7 | FOMC (no presser) | Vol event risk | — |
| ~May 15-27 | — | — | **Central-case VIX peak window (median timing)** |
| **Jun 15** | — | — | **🔴 60d window expiry — full scenario resolution** |

---

## WEEKLY MONITORING SCHEDULE

| Day | Task |
|-----|------|
| Sunday | Review week ahead, check VIX expiration proximity |
| Monday | Update VIX data, check term structure |
| Tuesday | Monitor VVIX, SKEW |
| Wednesday | VIX expiration day (if applicable) — watch pinning |
| Thursday | Check credit-vol divergence post-VIX expiry |
| Friday | Week-end summary, update regime status |

---

## DATA REFRESH SCHEDULE

| Data Source | Frequency | Tool | Last Updated |
|-------------|-----------|------|--------------|
| VIX/VIX3M/VVIX/SKEW spot | Daily | `scripts/thresholds.py` | 2026-04-15 |
| VIX futures M1/M2 | Daily | `FORGE/tools/market-data/vix_futures.py` | 2026-04-15 |
| VIX options OI | Per session | `scripts/vix_options.py` | 2026-04-15 |
| VX_DAILY.tsv time series | Daily | `scripts/thresholds.py` → append | 2026-04-15 (100 rows backfilled) |
| FRED credit (HY/IG/CCC OAS) | Per session | `scripts/fred_fetch.py` | 2026-04-16 |
| FRED rates (2Y/10Y/TIPS) | Per session | `scripts/fred_fetch.py` | 2026-04-16 |
| Catalyst countdown | Per session | `scripts/catalyst_countdown.py` | 2026-04-15 |

**Boot sequence:** `python3 scripts/boot.py` runs thresholds + vix_options + catalyst_countdown.

---

*Created: 2026-04-12*
*Last Updated: 2026-04-16*
