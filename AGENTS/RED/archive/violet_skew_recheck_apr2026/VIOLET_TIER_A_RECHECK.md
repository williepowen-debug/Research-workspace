# RED Tier A Re-check of VIOLET's SKEW-Divergence Base Rate

**Date:** 2026-04-19 | **Author:** RED | **Target:** VIOLET `2026-04-15_skew_divergence_episodes.md` and `2026-04-15_vix_target_distribution.md`
**Status:** Complete — Tier A (A1, A2, A3). Tier B/C/D pending Will's call.

---

## TL;DR

VIOLET's headline "94% saw ≥15% rise / 81% ≥30% / 56% ≥50% within 60d" is **directionally correct but uses intraday peak measurement.** When you re-cut the same data using a tradeable definition (sustained close ≥25 for 3-5 consecutive days), the rates drop by roughly half. When you also restrict to the option-specific 36-day horizon (May 19 from Apr 13 fire), they drop further. The 2024-26 cluster — which VIOLET argues represents the "current regime" — has produced **zero of five episodes** with sustained close ≥25 for 3d within a 36-day window.

| Measure | VIOLET headline (60d) | RED sustained (60d) | RED sustained (36d) |
|---|---:|---:|---:|
| Stress base rate (n=14, all) | **71%** intraday >+50% | **29%** sust close ≥25 5d | **21%** sust close ≥25 3d |
| Ex-2024-26 cluster (n=9) | 67% | 33% | **33%** |
| Only 2024-26 cluster (n=5) | 80% | 20% | **0%** |

**Bottom line:** the option-position-specific probability of a sustained VIX move (May 19 25C) lands in the **20-33% range**, not the 56-80% range VIOLET's published distribution implies.

---

## Method

- **Data:** VIOLET's `workbook/vix_historical.csv` (2018-01-02 to 2026-04-10). Only goes back to 2018, so episodes #1 (2014-11) and #2 (2015-10) from VIOLET's table are excluded — n=14 here vs VIOLET's n=16. Both excluded episodes were STRESS outcomes, so my exclusion is conservative against my own argument (i.e., includes them and headline rates rise).
- **Pattern definition (reproduced exactly from VIOLET):** 20-day rolling change where SKEW rose ≥10pts AND VIX fell ≥5pts AND VVIX fell ≥15pts.
- **Episode clustering:** consecutive fire days within 20 days grouped into one episode.
- **Forward window:** N trading days starting day after fire.
- **Sustained:** closing VIX ≥ X for ≥ N consecutive trading days. **Intraday:** any high print ≥ X.
- **Cluster split:** episodes after 2024-01-01 = "2024-26 cluster"; before = ex-cluster.
- **Code:** `research/violet_skew_recheck.py`. Per-episode results: `research/violet_skew_recheck_results.csv`.

### Sample reproduction sanity check

I recovered 14 episodes; VIOLET listed 16 minus 2 pre-2018 = 14 expected. SKEW peaks within 1-2 of VIOLET's table on every episode I cross-checked. Pattern detection matches.

---

## A1 — Ex-cluster base rate (n=9 vs n=5)

The criticism: 5 of VIOLET's 16 episodes came from the 2024-26 cluster. If that cluster is non-iid (shared driver — 0DTE dealer dynamics, post-pandemic liquidity, persistent crash bid), pulling it out should change the base rate.

**Result:** ex-cluster intraday rates are only modestly lower than full sample. The 2024-26 cluster is NOT inflating the headline number much. **My initial guess of "36% ex-cluster" was wrong.**

| Metric (60d) | All (n=14) | Ex-cluster (n=9) | Cluster (n=5) |
|---|---:|---:|---:|
| Intraday peak >+30% | 86% | 78% | 100% |
| Intraday peak >+50% | 71% | 67% | 80% |
| Intraday peak VIX ≥25 | 79% | 67% | 100% |
| Intraday peak VIX ≥30 | 43% | 33% | 60% |

**Interpretation:** VIOLET's intraday-peak headline rates are real and replicated. Ex-cluster intraday rates are 67-78% — only ~10-15pp lower than full sample. This *partially* concedes the cluster-contamination argument: it's there, but smaller than I initially claimed.

**This narrows my A1 challenge** from "headline is wrong by 20pp" to "headline is wrong by 5-15pp on the intraday measure." The bigger problem is what comes next.

---

## A2 — Sustained vs intraday (the real lever)

The criticism: "peak VIX" includes single-print intraday spikes that immediately revert. The Aug 2024 yen carry hit ~66 intraday but settled back below 25 within 2 days. For a held option, this matters enormously.

**Result:** the gap between intraday-peak and sustained-close is the biggest single distortion in VIOLET's reporting.

| Metric (60d horizon, n=14) | Hit rate |
|---|---:|
| Intraday peak ≥25 (any high print, 1 minute) | **79%** |
| Closing peak ≥25 (any close) | **50%** |
| Sustained close ≥25 for 3 consecutive days | **29%** |
| Sustained close ≥25 for 5 consecutive days | **29%** |
| Sustained close ≥30 for 3 consecutive days | **29%** |

**The intraday rate (79%) is 2.7× the sustained-5d rate (29%).** Most of VIOLET's published "stress" outcomes are intraday peaks that did not sustain.

This is the single most important finding of the re-check. VIOLET's distribution analysis (`vix_target_distribution.md`) computed central case "VIX 28-38 within 60d" using **peak intraday VIX**. For an option holder waiting for VIX to settle ≥25 for several days, the relevant rate is roughly **half** what VIOLET published.

---

## A3 — 36-day option-specific horizon

The criticism: May 19 expiry is 36 trading days from the Apr 13 fire date. VIOLET's analysis used 60d. Episodes that took 50+ days to peak don't matter for this position.

**Result:** the 36d window further compresses the rates, especially on the sustained measure.

| Metric (36d horizon, n=14) | Hit rate |
|---|---:|
| Intraday peak ≥25 | **57%** (was 79% at 60d) |
| Closing peak ≥25 | **36%** (was 50% at 60d) |
| Sustained close ≥25 for 3 td | **21%** (was 29% at 60d) |
| Sustained close ≥25 for 5 td | **21%** (was 29% at 60d) |

**Cross-tab — A3 (36d window) split by cluster:**

| Cohort | n | Sust ≥25 5d | Sust ≥25 3d | Intraday ≥25 |
|---|---:|---:|---:|---:|
| Ex-cluster | 9 | 33% | 33% | 56% |
| 2024-26 cluster | 5 | **0%** | **0%** | 60% |

**This is the killer finding.** If the 2024-26 regime really is the appropriate prior (VIOLET's own argument), the historical base rate for sustained-VIX-close ≥25 within a 36-day window is **0 of 5 episodes**. The recent cluster has been entirely intraday spike-and-revert.

The 2025-01 episode that drove VIOLET's "1-in-5 tail to 50+" (peak VIX 52.33) actually peaked 53 trading days after the fire date — *outside* a 36-day option window. The Apr 8 2025 spike was caught by 60-day options, not 35-day options.

---

## Reconciling RED's prior estimate vs the data

| Measure | RED initial guess (Apr 18) | Data result |
|---|---:|---:|
| VIX sustained >25 for 5d in next 60d | 35-45% | **29%** |
| VIX sustained >25 for 5d by May 19 (36d) | 18-25% | **21%** |
| Tail to 50+ (sustained) | 5-8% | **7%** (1 of 14 sustained close ≥50) |

My initial estimates were close. The data confirms them. The May-19-specific sustained-25 rate is ~21% — well below VIOLET's implied "central case 28-38, 1-in-5 to 50+" framing.

---

## What this DOESN'T do to the thesis

1. **Direction is still right.** The pattern fires before stress 67-79% of the time on intraday measure. Vol IS underpriced relative to latent risk. VIOLET's qualitative thesis stands.
2. **Position is not invalidated.** VIX May 19 25C can pay on intraday spikes too — it depends on the holder's exit discipline and the path. A 60-second print to VIX 35 *can* be exercised/sold. So the relevant rate isn't strictly "sustained close" — it's somewhere between intraday-touch and sustained-close, weighted by realistic execution.
3. **The 60d-window analysis is fine for a position that captures 60d.** The criticism is specifically about the May 19 option being too short to harvest the full distribution.
4. **The framework of "credit-vs-vol divergence as a precursor" is empirically valid.** Re-running the same data confirms that.

## What this DOES do

1. **VIOLET's "central case 28-38, tail to 50+" distribution is a peak-intraday distribution.** Reading it as a sustained-regime distribution overstates by ~2-3×.
2. **The 2024-26 cluster argument cuts both ways.** It pushes intraday rates UP (5/5 hit ≥25 intraday) but it pushes sustained rates DOWN to 0/5 in the 36-day window. VIOLET cites the cluster as evidence FOR the position; on the sustained measure, the cluster argues against it.
3. **The May 19 25C is a bet on an intraday spike, not a regime shift.** That's still a tradeable thesis but it's a different thesis from "VIX 28-38 sustained." Premium needs to reflect this.

---

## Asks for VIOLET (refined from Apr 18)

| # | Original Apr 18 ask | Refined ask post-data |
|---|---|---|
| 1 | "Publish ex-cluster base rate" | Modest issue (only 5-15pp difference on intraday). De-prioritize. |
| 2 | "Split intraday vs sustained" | **CRITICAL.** This is the dominant distortion (2.7× gap). Re-publish the target distribution split into sustained-close vs intraday-peak. |
| 3 | "Pre-commit single falsifiable prediction for May 19 window" | Still wanted. My estimate: 21% sustained ≥25 by May 19. VIOLET's number? |
| 4 | "Reconcile 56% (SKEW) vs 18% (regime termination)" | Still important. Both methods, when run on sustained-close 3d, converge to ~21-29%. The 56% was an intraday number; 18% was sustained. They're measuring different things. |
| 5 | "Credit-led vs positioning-led classification" | Pending Tier B execution. |

---

## Updated RED probability bands

| Outcome | RED estimate | Confidence |
|---|---:|:---:|
| **VIX sustained close ≥25 for 3d by May 19** | **20-25%** | Medium-high (data driven, n=14) |
| VIX sustained close ≥25 for 3d by Jun 12 (60d) | 25-32% | Medium-high |
| VIX sustained close ≥30 for 3d by May 19 | 12-18% | Medium |
| VIX intraday print ≥25 by May 19 | 50-60% | Medium |
| VIX intraday print ≥30 by May 19 | 25-35% | Medium |
| VIX sustained close ≥40 by Jun 12 (tail) | 5-8% | Low (n=1) |

**For a 25C option held to expiry:** sustained close ≥25 doesn't matter — what matters is whether VIX trades ≥25 *at any point with enough time/vega for the option to print profit*. That's closer to the 50-60% intraday rate, but the option premium is priced for that path. The asymmetry is in the sustained-30-40 zone, where the historical rate (12-18%) may be cheaper than premium implies.

---

## Tier B/C/D status

- **Tier B (credit-led vs positioning-led classification, ~60 min):** Recommended next step. Could materially change the prior depending on current credit setup.
- **Tier C (pre-2014 OOS validation, ~45 min):** Need yfinance pull or another data source. SKEW data exists back to 1990.
- **Tier D (formal challenge to VIOLET's inbox, ~30 min):** Wait for Tier B before issuing — combined challenge is stronger.

---

*RED Apr 19. Numbers will be updated if VIOLET pushes back with corrections to the pattern reproduction or measurement choices.*
