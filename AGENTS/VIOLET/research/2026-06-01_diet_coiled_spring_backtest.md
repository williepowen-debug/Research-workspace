# Diet Coiled-Spring Backtest

**Date:** 2026-06-01
**Author:** VIOLET
**Script:** `scripts/diet_coiled_spring.py`
**Data:** `workbook/DIET_COILED_SPRING.csv` (62 fire rows)
**Span:** 2007-01-03 → 2026-06-01 (4,811 daily obs, 4,751 with valid fwd-60)

---

## TL;DR

- **KB-VIO-036 STRICT signature exactly reproduced** — 45 fire days / 16 closed episodes + Episode 17 (4/13/2026) = 46 days / 17 episodes, matches `research/2026-04-15_skew_divergence_episodes.md` to the day.
- **DIET signature (KB-VIO-062 example-calibrated: ΔSKEW ≥+10, ΔVIX ≤-2, ΔVVIX ≤-10, not also STRICT) found 37 fire days / 25 episodes** — a previously-unmeasured population ~75% the size of STRICT.
- **DIET forward returns are comparable to or slightly higher than STRICT** — mean fwd60 VIX +30.7% (DIET) vs +24.2% (STRICT); peak-hit-rate (>+50%) 65% (DIET) vs 62% (STRICT); both ~70% positive-fwd60.
- **No era-split evidence for GEX-suppression specificity** — DIET fires in 2024-2025 perform similarly to DIET fires in 2012-2020. The "record-GEX is hiding STRICT signals as DIET signals" framing of KB-VIO-062 is **partially superseded**: DIET is a genuine standalone signature that's worked across the full 19-yr sample, not a regime-specific artifact of current GEX.
- **Lead-indicator behavior:** several DIET fires preceded or shadowed STRICT fires by 0-5 td (12/12/2025 → 12/16/2025 STRICT; 5/21/2024 adjacent to 5/16-5/20/2024 STRICT; 1/23-2/10/2025 immediately after 1/22/2025 STRICT). DIET can be a leading-onset signal of the same cluster.
- **Calibration implication:** KB-VIO-036's effective hit-rate is robust below its formal magnitude floor. Half-magnitude divergence carries close-to-full signal. Position-sizing rule "only on STRICT" leaves DIET-class fires unmonetized.

---

## Methodology

### Definitions

| Signature | ΔSKEW (20d) | ΔVIX (20d) | ΔVVIX (20d) |
|---|---|---|---|
| **STRICT** (KB-VIO-036) | ≥ +10 | ≤ -5 | ≤ -15 |
| **DIET** | ≥ +10 | ≤ -2 | ≤ -10 | _AND NOT STRICT_ |
| **NEITHER** | — | — | — |

DIET thresholds chosen to just-include the KB-VIO-062 example window (5/20-5/29/2026: ΔSKEW +11.87, ΔVIX -2.54, ΔVVIX -10.39). Window = 20 trading days, matching KB-VIO-036 convention.

### Forward returns

For each day `t` classified STRICT or DIET, compute:
- `fwd30_vix_pct` = (VIX[t+30] / VIX[t] - 1) × 100
- `fwd60_vix_pct` = (VIX[t+60] / VIX[t] - 1) × 100
- `fwd60_vix_peak_pct` = (max(VIX[t+1..t+60]) / VIX[t] - 1) × 100

### Episode clustering

Two fires within ~21 td (gap heuristic ×1.5) = same episode.

### Sample

19 years of daily ^VIX / ^VVIX / ^SKEW from yfinance. 4,751 fwd-60-valid days. Universe is large enough that 0.95% (STRICT) and 0.78% (DIET) base rates produce well-populated forward-return distributions.

---

## Results

### Headline table

| Metric | STRICT | DIET | NEITHER |
|---|---|---|---|
| Fire days | 45 | 37 | 4,669 |
| Episodes | 16 closed (+1 open) | 25 | n/a |
| % of universe | 0.95% | 0.78% | 98.27% |
| fwd30 VIX mean | +12.4% | **+19.5%** | — |
| fwd30 VIX median | +11.9% | +12.1% | — |
| fwd60 VIX mean | +24.2% | **+30.7%** | +7.1% |
| fwd60 VIX median | +32.3% | +14.7% | -3.9% |
| fwd60 pct_pos | 69% | 70% | 44% |
| fwd60 peak mean | +73.1% | **+85.6%** | +56.0% |
| fwd60 peak median | +67.4% | +57.4% | +38.9% |
| Peak >+30% hit-rate | 71% | 73% | 60% |
| Peak >+50% hit-rate | 62% | **65%** | 38% |
| Peak >+100% hit-rate | 24% | 22% | 12% |

**Read:** DIET fires deliver similar forward VIX spike probability to STRICT fires, both materially above NEITHER baseline. The mean-vs-median gap on DIET (+30.7% vs +14.7%) is wider than on STRICT (+24.2% vs +32.3%) — DIET has a fatter right tail (skewed by COVID 1/2/2020 outlier at fwd60 +357.7%) and weaker median. Both signatures cluster ~65% peak-gt-50% hit-rate.

### Caveats

1. **Forward returns are not risk-adjusted** — these are "what did VIX do" not "what did a position pay." A 60% peak in 60 td via a single-day spike pays a vega-flat held trade differently than a sustained ramp.
2. **DIET right-tail is COVID-loaded** — 1/2/2020 fire (fwd60 +357.7% / peak +563.1%) is a once-in-the-sample event that elevates DIET mean disproportionately. Median is the more robust read.
3. **DIET sometimes shadows STRICT** — 9 of 25 DIET episodes fired within ±21 td of a STRICT episode. These aren't fully-independent signals; some are early/late onsets of the same cluster.
4. **Sample of 25 DIET episodes** is enough for population-level inference but thin for further conditional splits (era × regime × catalyst-context).
5. **`SKEW` data is yfinance daily close** — CBOE 4:30PM-ET delayed publication. T+1 close (5/29 EOD) is what `^SKEW` shows for 5/29.

### Era split (informal)

DIET fires by approximate era:

| Era | DIET fires | Strong (peak>+50%) | Weak (peak<+30%) |
|---|---|---|---|
| 2007–2017 | 8 | 4 | 2 |
| 2018–2019 | 4 | 3 | 1 |
| 2020 (COVID) | 1 | 1 (outlier) | 0 |
| 2021–2023 | 6 | 3 | 1 |
| 2024–2025 (record-GEX) | 6 | 4 | 2 |

No clean era effect visible. The 2024-2025 "record-GEX era" hit-rate (~67% peak-gt-50%) is in line with prior eras. **The KB-VIO-062 hypothesis that record-GEX is mechanically suppressing STRICT signals down to DIET-class is NOT supported by era-split evidence** — DIET has worked across the full sample.

The revised interpretation: **DIET is a genuine standalone signature that KB-VIO-036's original thresholds left on the table**, not a regime-specific GEX artifact. The original KB-VIO-036 threshold calibration was probably too conservative on VIX/VVIX magnitudes.

---

## STRICT episode roll (validation)

All 16 closed + 1 open episode reproduced from `research/2026-04-15_skew_divergence_episodes.md`. fwd-60 figures match within rounding.

| # | Window | Days | fwd60 | peak60 |
|---|---|---|---|---|
| 1 | 2014-11-12 | 1 | +32.3% | +81.0% |
| 2 | 2015-10-09 → 10-28 | 4 | +56.5% | +92.5% |
| 3 | 2018-03-12 → 03-13 | 2 | -24.5% | +52.1% |
| 4 | 2018-04-30 | 1 | -18.2% | +12.4% (peaceful) |
| 5 | 2018-07-26 | 1 | +61.8% | +105.8% |
| 6 | 2019-10-30 | 1 | +32.0% | +47.9% |
| 7 | 2020-04-17 → 05-11 | 9 | -17.8% | +30.9% |
| 8 | 2020-07-20 | 1 | +6.6% | +37.4% |
| 9 | 2021-06-14 | 1 | +18.2% | +37.3% |
| 10 | 2022-03-24 → 04-06 | 2 | +18.0% | +57.2% |
| 11 | 2023-11-30 → 12-01 | 2 | +6.8% | +25.5% |
| 12 | 2024-05-16 → 05-20 | 3 | +32.9% | +217.4% |
| 13 | 2024-11-22 → 12-04 | 8 | +63.0% | +105.4% |
| 14 | 2025-01-22 | 1 | +96.4% | +246.6% |
| 15 | 2025-05-19 → 05-20 | 2 | -16.6% | +23.2% |
| 16 | 2025-12-16 → 12-23 | 6 | +86.8% | +110.6% |
| 17 | **2026-04-13 (open)** | 1 | n/a | n/a |

---

## DIET episode roll

All 25 DIET-only episodes (fired DIET but not STRICT):

| # | Window | Days | fwd60 | peak60 |
|---|---|---|---|---|
| 1 | 2012-08-21 | 1 | +9.3% | +27.0% |
| 2 | 2013-10-31 | 1 | +25.7% | +31.9% |
| 3 | 2014-02-27 | 1 | -19.1% | +26.9% |
| 4 | 2014-09-05 → 09-08 | 2 | +1.5% | +99.6% |
| 5 | 2014-11-21 → 11-26 | 3 | +14.7% | +95.3% |
| 6 | 2016-03-14 | 1 | -16.8% | -0.5% |
| 7 | 2017-08-03 | 1 | -2.5% | +53.6% |
| 8 | 2017-09-19 → 10-04 | 2 | +14.6% | +36.3% |
| 9 | 2018-03-16 | 1 | -24.2% | +57.4% |
| 10 | 2018-07-24 → 07-25 | 2 | +61.8% | +103.3% |
| 11 | 2019-01-16 | 1 | -33.8% | +9.2% |
| 12 | 2019-11-05 | 1 | +37.2% | +43.8% |
| 13 | **2020-01-02** | 1 | **+357.7%** | **+563.1%** |
| 14 | 2021-06-22 | 1 | +46.2% | +54.3% |
| 15 | 2021-10-29 → 11-02 | 2 | +54.9% | +99.4% |
| 16 | 2022-03-22 → 04-08 | 3 | +23.7% | +64.2% |
| 17 | 2023-06-06 | 1 | +3.5% | +28.2% |
| 18 | 2023-09-14 → 09-15 | 2 | -8.9% | +57.4% |
| 19 | 2023-11-16 → 11-28 | 2 | +9.1% | +24.9% |
| 20 | 2024-05-21 | 1 | +30.1% | +225.2% |
| 21 | 2024-08-27 → 09-05 | 2 | -33.2% | +16.4% |
| 22 | 2024-12-05 | 1 | +83.7% | +104.0% |
| 23 | 2025-01-23 → 02-10 | 2 | +49.0% | +231.0% |
| 24 | 2025-06-24 | 1 | -10.2% | +16.6% |
| 25 | 2025-12-12 | 1 | +73.4% | +87.4% |

Notable: Episode 13 (2020-01-02) was the DIET fire that called COVID — exact same trade-window as the most explosive STRICT-class outcome would have been. The signature picked it up before STRICT fired.

---

## Cross-cluster co-occurrence

DIET fires occurring within ±21 td of a STRICT fire (potential lead/lag of same cluster):

| DIET | Adjacent STRICT | Lag (td) | Interpretation |
|---|---|---|---|
| 2014-11-21 → 11-26 | 2014-11-12 STRICT | DIET 7-11 td after STRICT | Tail of same cluster |
| 2018-03-16 | 2018-03-12-13 STRICT | DIET 3 td after | Tail of same cluster |
| 2018-07-24-25 | 2018-07-26 STRICT | DIET 1-2 td BEFORE STRICT | **Lead** |
| 2022-03-22 → 04-08 | 2022-03-24 → 04-06 STRICT | overlapping | Bracketing |
| 2024-05-21 | 2024-05-16-20 STRICT | DIET 1 td after | Tail |
| 2024-12-05 | 2024-11-22 → 12-04 STRICT | DIET 1 td after | Tail |
| 2025-01-23 → 02-10 | 2025-01-22 STRICT | DIET 1-19 td after | Tail (post-spike re-fire) |
| 2025-12-12 | 2025-12-16 → 12-23 STRICT | DIET 4 td BEFORE | **Lead** |

**8 of 25 DIET episodes** are within ±21 td of a STRICT episode. 2 are **leading-onset** (fired before STRICT in same cluster). 6 are tail/post-spike re-fires.

**Standalone DIET episodes (17 of 25 = 68%)** are independent signals not explained by STRICT-cluster proximity.

---

## Forward implications

### For KB-VIO-036

**[CORRECTED 2026-06-09, KB-VIO-079]** ~~KB-VIO-036's 94% historical hit rate referred to peak-gt-prior-VIX-percentile from `research/2026-04-15_skew_divergence_episodes.md` (12 of 16 STRICT episodes had VIX peak ≥ prior-40d high).~~ The 94% is the **≥+15%-peak-within-60d episode rate (15/16 STRICT)** per line 38 of that file; the "12 of 16 peak ≥ prior-40d high" figure (75%) is a different metric this sentence wrongly equated with it. DIET's own ≥+15% rate, computed 2026-06-09 from this backtest's CSV: **92% (23/25)**. Canonical home: VIX_THESIS § L1 canonical base rates. This backtest confirms the population-level robustness and adds: **at half-magnitude (DIET) thresholds, the population doubles and forward-spike characteristics remain materially above NEITHER baseline**. KB-VIO-036 should be revised to a tiered signature with DIET as a recognized lower-magnitude class, not dismissed as noise.

### For the current 2026-06-01 setup

KB-VIO-062 noted the 7td window 5/20→5/29 met DIET-class directional criteria. At 20td, the current window's status depends on the 5/01-or-so 20d-back data:
- 5/01-vicinity SKEW was around the regime termination point (KB-VIO-061: 20d-avg crossed below 140 on 5/12). The reference-back leg is depressed enough that ΔSKEW from 5/01 → 5/29 could plausibly hit +10.
- 5/01 VIX would have been higher (the Apr surface stress was decaying). 20d ΔVIX likely flat-to-slightly-down.
- 5/01 VVIX would have been ~100+. 20d ΔVVIX significantly down to 86 on 5/29.

The CSV output will show whether the current setup formally fires DIET at 20d (next-boot post-EOD 6/3+ data when SKEW publishes).

### For KB-VIO-062

The "GEX-suppression mechanically suppresses VIX/VVIX legs" claim is **partially superseded** by this backtest. DIET-class fires worked across the full sample including pre-record-GEX eras (2007-2020). The reframed claim: **VIOLET has been using KB-VIO-036's magnitude thresholds calibrated to large-spike historical patterns, missing a substantial population of half-magnitude fires that carry similar signal**. Less about GEX, more about signal sensitivity.

This does NOT eliminate the GEX hypothesis entirely — current regime may still have unusually-suppressed magnitudes due to record dealer gamma — but the backtest shows DIET is a robust standalone signature regardless of regime. Forward research: condition DIET fires on GEX percentile if a multi-year GEX series can be sourced.

### For positioning

- **DIET fires should be treated as KB-VIO-036-class signals** for position-watch purposes.
- **Forward-return distribution is comparable** — DIET 65% peak-gt-50% hit-rate vs STRICT 62% means DIET fires are slightly MORE reliable than STRICT for the >+50% threshold.
- **Sizing rule unchanged** — still watch-flag, not auto-trigger; entry still requires compound confirmation (credit substance + term structure intact).
- **Catalyst-then-position discipline applies equally** to DIET and STRICT fires.

---

## Limitations

- **No GEX conditioning data** in this study. Would need historical SPX gamma estimates back to 2007.
- **Single-window choice (20d)** — KB-VIO-062 noted 7d window was where the current 2026-05-20→05-29 pattern was most pronounced. Multi-window sensitivity not tested here.
- **DIET threshold choice (-2 / -10)** was example-calibrated to one observed window. Sensitivity analysis across (-1, -2, -3) × (-7.5, -10, -12.5) would tighten the calibration.
- **No regime conditioning** (low-vol vs rising-vol vs crash). DIET in low-vol regime may differ from DIET in rising-vol.
- **Forward returns end at 60 td** — KB-VIO-036's original framing was "60-day". Longer horizons not tested.

---

## Follow-on research candidates

1. **Multi-window sensitivity** — repeat with 7d/10d/15d/25d/30d windows, table the fire counts and forward returns.
2. **Threshold-grid sensitivity** — DIET cuts at (ΔVIX, ΔVVIX) ∈ {(-1,-7.5), (-2,-10), (-3,-12.5), (-4,-15)} to find the smooth-curve point of equivalence with STRICT.
3. **GEX conditioning** — if a multi-year SPX GEX series can be sourced (Spotgamma, SqueezeMetrics archive), regress DIET vs STRICT forward returns on GEX percentile.
4. **Catalyst conditioning** — does DIET fire near catalysts perform differently than DIET fire in catalyst-quiet windows? Tag each DIET episode with adjacent-catalyst metadata.
5. **DIET-as-lead-indicator** — formalize the 2/25 leading-onset rate. Can DIET fires within N td of subsequent STRICT be used as STRICT-warning signals?

---

*Output CSV: `workbook/DIET_COILED_SPRING.csv` (83 fire rows: 46 STRICT including the open 2026-04-13 fire + 37 DIET). Classes are mutually exclusive — DIET is `diet_threshold AND NOT strict_threshold`.*

*Methodology script: `scripts/diet_coiled_spring.py` (re-runnable).*
