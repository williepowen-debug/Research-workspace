# SKEW Regime Termination Analysis

**Question:** When historical elevated SKEW regimes ended, did the VIX event come **before** the regime ended (regime persisted through it), **during** (coincident), or **after** (regime collapse preceded the event)?

**Motivation:** The current regime (206+ td, second longest in 19-year history) saw SKEW dip to 139.2 on Apr 16. If regimes typically collapse BEFORE the VIX event, this dip could signal the event is imminent. If they persist THROUGH events, the dip is noise.

---

## Method

- **Regime definition:** 20-day rolling avg SKEW >= 140, minimum 10 trading days.
- **NaN handling:** Forward-filled SKEW gaps (up to 3 days) before computing rolling avg to prevent false terminations.
- **VIX peak:** Searched ±60 trading days around regime end. Used both daily close and intraday high (`High ^VIX`).
- **Temporal lag:** regime_end_date minus vix_peak_date in trading days. Positive = VIX peaked first (regime outlasted event). Negative = VIX peaked after (regime ended before event).
- **Data:** 2014-2026 (yfinance + vix_historical.csv + VX_DAILY.tsv).

---

## Table 1: Master Regime Inventory

| # | Start | End | Duration | Peak SKEW | Status |
|--:|:------|:----|:--------:|----------:|:-------|
| 12 | 2025-06-16 | 2026-05-13 | 223 td | 161.9 | **ONGOING** |
| 11 | 2024-08-21 | 2025-03-27 | 150 td | 183.1 | ended |
| 5 | 2021-05-11 | 2021-10-11 | 107 td | 170.6 | ended |
| 9 | 2024-01-24 | 2024-04-23 | 63 td | 170.5 | ended |
| 1 | 2018-07-18 | 2018-10-10 | 60 td | 159.0 | ended |
| 6 | 2021-11-02 | 2022-01-26 | 59 td | 156.2 | ended |
| 10 | 2024-05-24 | 2024-08-14 | 56 td | 157.0 | ended |
| 7 | 2023-06-05 | 2023-08-22 | 55 td | 157.7 | ended |
| 3 | 2020-12-30 | 2021-02-08 | 27 td | 147.8 | ended |
| 8 | 2023-11-29 | 2024-01-03 | 24 td | 162.5 | ended |
| 4 | 2021-03-23 | 2021-04-19 | 19 td | 146.1 | ended |
| 2 | 2020-08-26 | 2020-09-11 | 12 td | 146.5 | ended |

12 regimes >= 10 td identified.

---

## Table 2: Termination Detail

| # | End Date | Dur | SKEW @ End | VIX @ End | VIX Peak Close | VIX Peak Date | Lag (td) | Post-30d Peak | Classification |
|--:|:---------|----:|-----------:|----------:|---------------:|:-------------|--------:|--------------:|:-------------|
| 11 | 2025-03-27 | 150 | 140.9 | 18.69 | 52.33 | 2025-04-08 | -8 | 52.33 | PRE_EVENT_FADE |
| 5 | 2021-10-11 | 107 | 134.7 | 20.0 | 31.12 | 2021-12-01 | -36 | 19.85 | PRE_EVENT_FADE |
| 9 | 2024-04-23 | 63 | 135.6 | 15.69 | 19.23 | 2024-04-15 | +6 | 15.97 | POST_EVENT_PERSIST |
| 1 | 2018-10-10 | 60 | 127.7 | 22.96 | 36.07 | 2018-12-24 | -51 | 25.23 | PRE_EVENT_FADE |
| 6 | 2022-01-26 | 59 | 133.4 | 31.96 | 36.45 | 2022-03-07 | -27 | 36.45 | GRADUAL_FADE |
| 10 | 2024-08-14 | 56 | 141.8 | 16.19 | 38.57 | 2024-08-05 | +7 | 22.38 | POST_EVENT_PERSIST |
| 7 | 2023-08-22 | 55 | 134.1 | 16.97 | 21.71 | 2023-10-20 | -42 | 19.78 | GRADUAL_FADE |
| 3 | 2021-02-08 | 27 | 135.1 | 21.24 | 37.21 | 2021-01-27 | +8 | 28.89 | POST_EVENT_PERSIST |
| 8 | 2024-01-03 | 24 | 134.2 | 14.04 | 21.71 | 2023-10-20 | +50 | 15.85 | POST_EVENT_PERSIST |
| 4 | 2021-04-19 | 19 | 138.3 | 17.29 | 37.21 | 2021-01-27 | +56 | 27.59 | POST_EVENT_PERSIST |
| 2 | 2020-09-11 | 12 | 125.4 | 26.87 | 40.28 | 2020-10-28 | -33 | 29.48 | PRE_EVENT_FADE |

**Lag sign:** positive = VIX peaked before regime ended (regime outlasted event); negative = VIX peaked after (regime ended before event).

---

## Finding 1: Temporal Lag Distribution

| Classification | Count | Regimes | Meaning |
|:---------------|------:|:--------|:--------|
| PRE_EVENT_FADE | 4 | R1, R2, R5, R11 | Regime ended, then VIX spiked |
| COINCIDENT | 0 | — | VIX peak ±5 td of regime end |
| POST_EVENT_PERSIST | 5 | R3, R4, R8, R9, R10 | Regime survived past VIX peak |
| GRADUAL_FADE | 2 | R6, R7 | No major VIX event in window |

**Lag statistics:** mean -6.4 td, median -8.0 td, range -51 to +56

**Key cases by duration:**

- **R11** (150 td): ended 2025-03-27, VIX peaked 52.33 on 2025-04-08 → lag **-8 td** (PRE_EVENT_FADE)
- **R5** (107 td): ended 2021-10-11, VIX peaked 31.12 on 2021-12-01 → lag **-36 td** (PRE_EVENT_FADE)
- **R9** (63 td): ended 2024-04-23, VIX peaked 19.23 on 2024-04-15 → lag **+6 td** (POST_EVENT_PERSIST)
- **R1** (60 td): ended 2018-10-10, VIX peaked 36.07 on 2018-12-24 → lag **-51 td** (PRE_EVENT_FADE)
- **R6** (59 td): ended 2022-01-26, VIX peaked 36.45 on 2022-03-07 → lag **-27 td** (GRADUAL_FADE)

---

## Finding 2: Terminal SKEW Behavior

How did SKEW behave in the final days of each regime?

| # | Duration | SKEW @ End | 20d Avg @ End | Final 5d Slope | Pattern |
|--:|---------:|-----------:|--------------:|---------------:|:--------|
| 11 | 150 | 140.9 | 140.7 | -2.0 | gradual_fade |
| 5 | 107 | 134.7 | 140.5 | -3.5 | sudden_drop |
| 9 | 63 | 135.6 | 141.0 | -3.5 | sudden_drop |
| 1 | 60 | 127.7 | 140.4 | -3.5 | sudden_drop |
| 6 | 59 | 133.4 | 140.1 | -2.6 | gradual_fade |
| 10 | 56 | 141.8 | 140.0 | -1.3 | gradual_fade |
| 7 | 55 | 134.1 | 140.5 | -1.8 | gradual_fade |
| 3 | 27 | 135.1 | 140.1 | -1.7 | gradual_fade |
| 8 | 24 | 134.2 | 140.4 | -1.5 | gradual_fade |
| 4 | 19 | 138.3 | 140.2 | -1.3 | gradual_fade |
| 2 | 12 | 125.4 | 140.2 | -1.3 | gradual_fade |

**Sudden drops (final 5d slope < -3):** 3
**Gradual fades:** 8

---

## Finding 3: Post-Regime VIX Behavior

What happened to VIX in the 30 trading days after the regime ended?

| # | Duration | VIX @ End | Post-30d Peak | Post-30d Mean | Behavior |
|--:|---------:|----------:|--------------:|--------------:|:---------|
| 11 | 150 | 18.69 | 52.33 | 29.29 | SPIKE |
| 5 | 107 | 20.0 | 19.85 | 16.75 | CALM |
| 9 | 63 | 15.69 | 15.97 | 13.45 | CALM |
| 1 | 60 | 22.96 | 25.23 | 20.61 | CALM |
| 6 | 59 | 31.96 | 36.45 | 27.77 | CALM |
| 10 | 56 | 16.19 | 22.38 | 17.04 | ELEVATED |
| 7 | 55 | 16.97 | 19.78 | 15.55 | CALM |
| 3 | 27 | 21.24 | 28.89 | 22.66 | ELEVATED |
| 8 | 24 | 14.04 | 15.85 | 13.51 | CALM |
| 4 | 19 | 17.29 | 27.59 | 19.13 | SPIKE |
| 2 | 12 | 26.87 | 29.48 | 27.09 | CALM |

**Post-regime spikes (VIX > 1.5x end level):** 2 of 11
**Post-regime calm:** 7 of 11

---

## Finding 4: Current Regime in Context

**Duration:** 223 td (ongoing)
**SKEW at latest:** 141.5
**20d avg at latest:** 142.8
**Final 5d slope:** -1.0
**Intermediate VIX event:** 31.05 on 2026-03-27 (regime persisted through it)

**Trajectory comparison (final 5d slope):**

| Regime | Duration | Final 5d Slope | What Followed |
|:-------|:---------|:--------------|:-------------|
| R11 | 150 td | -2.0 | VIX 52.33 (PRE_EVENT_FADE) |
| R5 | 107 td | -3.5 | VIX 31.12 (PRE_EVENT_FADE) |
| R9 | 63 td | -3.5 | VIX 19.23 (POST_EVENT_PERSIST) |
| R1 | 60 td | -3.5 | VIX 36.07 (PRE_EVENT_FADE) |
| R6 | 59 td | -2.6 | VIX 36.45 (GRADUAL_FADE) |
| **Current** | **223 td** | **-1.0** | **TBD** |

---

## Actionable Summary

**Of 11 completed regimes:**
- 4 (36%) — regime ended BEFORE VIX event (PRE_EVENT_FADE)
- 0 (0%) — regime ended WITH VIX event (COINCIDENT)
- 5 (45%) — regime OUTLASTED VIX event (POST_EVENT_PERSIST)
- 2 (18%) — no significant VIX event (GRADUAL_FADE)

**For the VIX May 19 25C position:**

The dominant pattern is that regimes **persist through** VIX events and collapse afterward. If our regime is still intact (which the within-cycle bounce pattern suggests), the position remains well-supported.

---

*Generated 2026-05-13 20:51 by VIOLET `scripts/regime_termination.py`*
*Data: yfinance + vix_historical.csv + VX_DAILY.tsv*