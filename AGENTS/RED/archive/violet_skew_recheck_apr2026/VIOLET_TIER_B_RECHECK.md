# RED Tier B — Credit-State Classification of SKEW-Divergence Fires

**Date:** 2026-04-19 | **Author:** RED | **Target:** VIOLET SKEW-divergence pattern in context of credit state
**Status:** Complete

---

## TL;DR

The SKEW-divergence pattern has **never fired in a credit-widening state** (n=0 of 14). By construction it requires VIX to be falling — which tends to coincide with flat or tightening credit. Splitting the 14 historical fires by credit state:

| Credit state at fire | n | Sust ≥25 5d, 60d | Sust ≥25 3d, 36d | Character |
|---|---:|---:|---:|---|
| WIDENING (credit-led) | **0** | — | — | Pattern doesn't fire here |
| FLAT (positioning-led) | 8 | 12% | 12% | Spike-and-revert, transient |
| TIGHTENING (post-stress relief) | 6 | 50% | 33% | Bifurcated — COVID-inflated |
| **TIGHTENING ex-COVID (n=4)** | 4 | **25%** | **0%** | This is the current cohort |

**Current setup (Apr 13, HY OAS -29bps in 20d, -56bps off peak) maps to TIGHTENING.** Closest historical analog is **Ep 12 (2025-01-22): identical -29bps 20d change and similar trough level**. That episode produced a massive VIX print (intraday 60.13, close 52.33) — but the peak came at **53 trading days after fire**, *outside* a 36-day option window.

**The sharpened conclusion:** VIOLET's strongest analog for the current setup is real and produced a major VIX event, but at a timing that would have **missed a May 19 option** from an Apr 13 entry. The 36-day sustained hit rate in non-COVID TIGHTENING episodes is **0/4 = 0%.** The 60-day rate is **1/4 = 25%.**

---

## Method

For each of the 14 SKEW-divergence fires found in Tier A (2018-2026):

1. Computed HY OAS (FRED BAMLH0A0HYM2) level 20 calendar days prior to fire date.
2. Computed HY OAS level at fire date.
3. Classified:
   - **WIDENING**: 20d change ≥ +25 bps
   - **TIGHTENING**: 20d change ≤ −25 bps
   - **FLAT**: otherwise
4. Computed sustained-close rates within each cohort at 60d and 36d horizons.
5. Looked up current (Apr 13 2026) setup.

Code: `research/violet_skew_tier_b.py`. Full table: `research/violet_skew_tier_b_results.csv`.

---

## Episode classification table

| Ep | Date | SKEW peak | VIX @ start | HY @ fire | HY 20d chg | HY peak 25d | Trend | Sust25-5d 60 | Sust25-3d 36 | Intra peak |
|---:|---|---:|---:|---:|---:|---:|---|:---:|:---:|---:|
| 1 | 2018-03-12 | 147 | 15.8 | 355 | +7 | 365 | FLAT | ✗ | ✗ | 26.0 |
| 2 | 2018-04-30 | 133 | 15.9 | 346 | −6 | 364 | FLAT | ✗ | ✗ | 19.6 |
| 3 | 2018-07-26 | 154 | 12.1 | 342 | −32 | 378 | **TIGHT** | ✗ | ✗ | 28.8 |
| 4 | 2019-10-30 | 131 | 12.3 | 396 | −30 | 439 | **TIGHT** | ✗ | ✗ | 19.0 |
| 5 | 2020-04-17 | 133 | 38.1 | 731 | **−168** | 1087 | **TIGHT (COVID)** | ✓ | ✓ | 47.8 |
| 6 | 2020-07-20 | 146 | 24.5 | 554 | **−90** | 652 | **TIGHT (COVID)** | ✓ | ✓ | 38.3 |
| 7 | 2021-06-14 | 161 | 16.4 | 317 | −17 | 342 | FLAT | ✗ | ✗ | 25.1 |
| 8 | 2022-03-24 | 147 | 21.7 | 367 | −23 | 421 | FLAT | ✓ | ✓ | 36.6 |
| 9 | 2023-11-30 | 145 | 12.9 | 384 | −19 | 408 | FLAT | ✗ | ✗ | 17.9 |
| 10 | 2024-05-16 | 156 | 12.4 | 308 | −8 | 329 | FLAT | ✗ | ✗ | **65.7** |
| 11 | 2024-11-22 | 174 | 15.2 | 261 | −22 | 288 | FLAT | ✗ | ✗ | 28.3 |
| **12** | **2025-01-22** | **180** | **15.1** | **259** | **−29** | **294** | **TIGHT** | ✓ | ✗ | **60.1** |
| 13 | 2025-05-19 | 141 | 18.1 | 321 | −53 | 394 | **TIGHT** | ✗ | ✗ | 25.5 |
| 14 | 2025-12-16 | 162 | 16.5 | 298 | −2 | 319 | FLAT | ✗ | ✗ | 35.3 |

**Current Apr 13 2026:** HY OAS 290 bps, 20d change −29, off peak −56 bps → **TIGHTENING**.

---

## Finding 1 — The pattern doesn't fire in credit-widening regimes

**Zero of 14 historical fires occurred when HY OAS was widening ≥25 bps in the prior 20d.** This is mechanical: the SKEW-divergence pattern requires VIX to drop ≥5 points in 20 days, and sharp VIX drops rarely coincide with sharp credit widening. The pattern is either positioning-led (flat credit) or relief-led (tightening from prior stress).

**Implication:** VIOLET's v3.1 central claim ("HY OAS leads VIX by 2-6 weeks when credit-led") is technically irrelevant to this specific pattern's detection. The pattern itself is not a credit-led signal — it's a crash-bid / positioning signal that fires in the absence of active credit widening.

This doesn't invalidate VIOLET's qualitative framework. But it means we should stop describing SKEW-divergence fires as "credit-led" stress precursors. They are positioning signals that may precede vol events driven by OTHER things (exogenous shocks, unwinds, catalysts).

---

## Finding 2 — The TIGHTENING cohort has a bifurcated structure

| Sub-cohort | Episodes | Count | Sust 5d-60d | Sust 3d-36d |
|---|---|---:|---:|---:|
| COVID-era (extreme relief) | 5, 6 | 2 | 2/2 = 100% | 2/2 = 100% |
| Non-COVID (normal relief) | 3, 4, 12, 13 | 4 | 1/4 = 25% | 0/4 = 0% |
| All TIGHTENING | — | 6 | 3/6 = 50% | 2/6 = 33% |

**The COVID episodes (n=2) are not generalizable.** Both occurred during the fastest credit-spread tightening in history (−168 and −90 bps in 20 days), starting from crisis-level VIX (38.1 and 24.5). This is a crisis-recovery regime that does not match any current indicator.

**Ex-COVID TIGHTENING (n=4) is the relevant cohort.** Of those 4:
- **Ep 3, 4, 13**: sustained-close ≥25 never achieved in 60d window.
- **Ep 12 (2025-01-22)**: Sustained at 60d. But the peak (52.33 close) came at **53 trading days** after fire. At 36d horizon, it had not yet sustained.

**Net: non-COVID TIGHTENING produces 0/4 sustained 3d-close-≥25 in a 36-day window.** If you give 60 days it becomes 1/4 = 25%.

---

## Finding 3 — Current setup matches Ep 12, which supports VIOLET's direction but not her expiry

| Dimension | Ep 12 (2025-01-22) | Current (2026-04-13) |
|---|---:|---:|
| HY OAS 20d change | −29 bps | −29 bps |
| HY OAS at fire | 259 | 290 |
| HY OAS recent peak | 294 | 346 |
| HY OAS off-peak | −35 bps | **−56 bps** (more aggressive) |
| SKEW peak | 180 | 157 |
| VIX @ start | 15.1 | 18.1 |
| In-cluster? | Yes | Yes |

**This is a remarkably clean analog.** Same 20d credit move, similar regime character, same cluster. Ep 12's outcome:

- Intraday peak 60.13 (60 trading days later)
- Close peak 52.33 (53 trading days later, Apr 8 2025)
- Sustained close ≥25 for 3d: achieved at ~day 52-55
- **Sustained close ≥25 for 3d within 36 days: NO**

A May 19 option bought on Apr 13 would catch **36 trading days of forward path**. Applying Ep 12's trajectory to today:
- First 36 td: VIX drifted, no sustained event
- Days 50-55: the violent spike
- Apr 13 + 53 td ≈ early July. **Jun 18 and Jul 18 expiries would catch this. May 19 would not.**

---

## Finding 4 — FLAT cohort is where the big intraday spikes happen

The FLAT cohort (n=8) had the LOWEST sustained rate (12%) but contained the biggest intraday spike in the dataset: **Ep 10 (2024-05-16)**, the Aug 2024 yen carry, intraday peak 65.73. That episode *did not sustain* — within hours VIX was back below 25.

VIOLET's analog library already identified this: Feb 2018, Aug 2024 were both positioning-driven, both transient. My data confirms: FLAT credit setups produce spike-and-revert outcomes.

**The current setup is NOT FLAT.** Credit has moved materially (−56 bps off peak, −29 bps in 20 days). So the FLAT cohort's 12% rate is not the applicable prior for our fire.

---

## How Tier B changes my A1-A3 probabilities

My Tier A ranges were:

| Outcome | Tier A estimate |
|---|---:|
| Sustained close ≥25 for 3d by May 19 (36d) | 20-25% |
| Sustained close ≥25 for 3d by Jun 12 (60d) | 25-32% |
| Intraday print ≥25 by May 19 | 50-60% |

Tier B, applying the non-COVID TIGHTENING cohort (n=4) and Ep 12 analog:

| Outcome | Tier B refined |
|---|---:|
| Sustained close ≥25 for 3d by May 19 (36d) | **10-20%** (down — 0/4 historical at this horizon) |
| Sustained close ≥25 for 3d by Jun 12 (60d) | **25-35%** (unchanged — Ep 12 says yes here) |
| Sustained close ≥25 for 3d by Jul 18 (90d) | **35-50%** (NEW — captures the Ep 12 timing) |
| Intraday print ≥25 by May 19 | 45-60% (unchanged — spike-and-revert possible regardless) |

**The single biggest actionable insight: a Jun 18 or Jul 18 VIX 25C carries meaningfully higher sustained-event probability than May 19 25C, specifically because the closest historical analog (Ep 12) peaked at ~53 td.** If VIOLET is right that 2025-01 is the analog, the expiry is mis-timed by ~2 weeks.

---

## What I was wrong about in Apr 18 initial take

1. **"Positioning-led, therefore transient" was too strong.** The FLAT (positioning-led) cohort does produce transient spike-and-revert outcomes — that part was right. But the current setup is *not* FLAT. It's TIGHTENING. So the transience argument doesn't automatically apply.
2. **"Credit is tightening, therefore VIOLET's credit-leads thesis is violated" was imprecise.** The SKEW-divergence signal is not a credit-lead signal in the first place. The pattern fires in tight/flat credit regimes *by construction*. Criticizing its credit-state mismatch was partially off-base.
3. **"2025-01 analog shouldn't be iid" — stands.** That episode is in the TIGHTENING cohort and is the closest analog, but its outcome timing (day 53) tells us something specific: expiry matters more than probability.

---

## Refined asks for VIOLET

| # | Ask |
|---|---|
| 1 | Publish the credit-state breakdown explicitly. FLAT vs non-COVID TIGHTENING base rates are very different. |
| 2 | Acknowledge that the SKEW-divergence pattern is not itself a credit-lead signal — it's a positioning/structure signal that fires in tight-credit regimes. This matters for the thesis narrative in STATUS. |
| 3 | **Re-examine expiry choice.** If 2025-01 is the cited analog and it peaked at day 53, VIX May 19 25C is under-tenored. Jun 18 or Jul 18 25C captures the historical peak window better. |
| 4 | Pre-commit a falsifiable prediction for the May 19 window — specifically "sustained close ≥25 for 3d between Apr 14 and May 19, probability X%". |

---

## Updated probability bands (post Tier A+B)

| Outcome | RED estimate | Confidence |
|---|---:|:---:|
| **Sustained close ≥25 for 3d by May 19** | **12-18%** | Medium-high (n=4 non-COVID TIGHTENING) |
| **Sustained close ≥25 for 3d by Jun 18** | **25-35%** | Medium (Ep 12 analog, n=1 proper hit) |
| **Sustained close ≥25 for 3d by Jul 18** | **35-50%** | Medium (time-extended) |
| Intraday print ≥25 by May 19 | 45-60% | Medium |
| Intraday print ≥30 by May 19 | 25-35% | Medium |
| Sustained close ≥40 by Jul 18 (tail) | 8-12% | Low (n=1 in Ep 12) |

---

## Tier C / Tier D status

- **Tier C** (pre-2014 out-of-sample): still recommended but no longer critical. Would tell us if the pattern is overfit to 2018+ data. Since the TIGHTENING cohort has n=6 and ex-COVID has n=4, widening the sample would meaningfully reduce uncertainty.
- **Tier D** (formal challenge to VIOLET's inbox): ready to write. The combined Tier A + B findings are more targeted and more actionable than Apr 18 initial read.

---

*RED Apr 19. Tier B substantially refines Tier A and produces the single most actionable finding: if VIOLET's 2025-01 analog is right, the position expiry is under-tenored. Jun 18 or Jul 18 25C likely offers materially better risk-adjusted capture of the historical base rate.*
