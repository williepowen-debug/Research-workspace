# VIOLET CALENDAR

VIX-specific catalysts and monitoring schedule.

---

## VIX EXPIRATION DATES (Monthly)

VIX futures and options expire on the **Wednesday 30 days prior to the third Friday of the following month**.

| Month | Expiration Date | Notes |
|-------|-----------------|-------|
| Apr 2026 | Apr 15 | EXPIRED |
| May 2026 | May 20 | **🔴 VIX May 19 25C expires day before (May 19) — open position** |
| Jun 2026 | Jun 17 | Quarterly expiration — high volume. **60d window expiry checkpoint** (FOMC + SEP same date) |
| Jul 2026 | Jul 15 | FOMC Jul 29-30 same week | 
| Aug 2026 | Aug 19 | — |
| Sep 2026 | Sep 16 | Quarterly expiration (FOMC + SEP same date) |

**Pin risk:** VIX tends to drift toward strikes with high open interest near expiration.

---

## FOMC MEETINGS (Vol Events)

| Date | Meeting | VIX Watch |
|------|---------|-----------|
| ~~Apr 28-29, 2026~~ | FOMC | **DONE — Held 3.50-3.75%, 4 dissents (most since Oct 1992). Hawkish-leaning forward language. VIX did NOT spike (16.99 May 3).** |
| Jun 16-17, 2026 | FOMC + SEP | **First post-Apr-dissent dot plot — 60d window expiry checkpoint** |
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
| ~~Apr 22~~ | ~~SKEW>145 FADE_RERAMP gate~~ | **❌ FAILED — never breached** | — |
| ~~Apr 28~~ | ~~BOJ~~ | **DONE — hawkish hold + 3 dissents, VIX absorbed** | — |
| ~~Apr 28-29~~ | ~~FOMC~~ | **DONE — 4-dissent hawkish hold, VIX absorbed** | — |
| ~~May 1~~ | ~~BOJ Rate Decision~~ | per boot, was IMMINENT — outcome to verify | — |
| ~~May 1~~ | ~~NFP April~~ | per boot, released — outcome to verify | — |
| **May 13** | — | 30d post-fire central VIX ~25 target | **🟠 Trade-thesis early read** |
| **May 19** | **VIX 25C expires** | — | **🔴 OPEN POSITION expiry — close/roll/let-run decision needed before** |
| May 16 | OPEX (May monthly) | — | — |
| **Jun 12-15** | **60d post-fire window close** | — | **🔴 Full scenario resolution. Coincides with Jun 16-17 FOMC + SEP.** |

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
| VIX/VIX3M/VVIX/SKEW spot | Daily | `scripts/thresholds.py` | 2026-04-17 (close) |
| VIX futures M1/M2 | Daily | `FORGE/tools/market-data/vix_futures.py` | 2026-04-17 |
| VIX options OI | Per session | `scripts/vix_options.py` | 2026-04-17 |
| VX_DAILY.tsv time series | Daily | `scripts/thresholds.py` → append | 2026-04-17 |
| FRED credit (HY/IG/CCC OAS) | Per session | `scripts/fred_fetch.py` | 2026-04-17 (data through Apr 16) |
| FRED rates (2Y/10Y/TIPS) | Per session | `scripts/fred_fetch.py` | 2026-04-17 |
| Catalyst countdown | Per session | `scripts/catalyst_countdown.py` | 2026-04-17 |
| CFTC COT VIX futures | Weekly Fri | `scripts/cftc_cot.py` (**Phase 1 — to build**) | Not yet wired |
| NAAIM + ICI equity positioning | Weekly Wed/Thu | `scripts/equity_positioning.py` (**Phase 2 — to build**) | Not yet wired |

**Boot sequence:** `python3 scripts/boot.py` runs thresholds + vix_options + catalyst_countdown.

---

*Created: 2026-04-12*
*Last Updated: 2026-04-17 (EOD refresh pass — data refresh dates current; Phase 1/2 positioning sources flagged for next session)*
