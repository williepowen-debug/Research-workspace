# RED Tier C OOS Validation of VIOLET's SKEW-Divergence Pattern

**Date:** 2026-04-19 | **Author:** RED | **Target:** VIOLET SKEW-divergence base rate
**Status:** Complete — Tier C. Follows Tier A (`VIOLET_TIER_A_RECHECK.md`) and Tier B (`VIOLET_TIER_B_RECHECK.md`).

---

## TL;DR

I pulled ^SKEW / ^VIX / ^VVIX from yfinance back to the VVIX inception (2007-01-03) and replicated the pattern detection over the OOS window 2007-2017. Two episodes emerged — both are the pre-2018 episodes VIOLET listed in her table but didn't save to disk. **Neither sustained a close ≥25 for even 3 consecutive days, in any forward window.** The OOS data *worsens* VIOLET's sustained-stress base rate rather than corroborating her headline.

| Cohort | n | Intraday ≥25 (36d) | Sust close ≥25 3d (36d) | Sust close ≥25 5d (60d) |
|---|---:|---:|---:|---:|
| OOS 2007-2017 | 2 | 50% | **0%** | **0%** |
| In-sample 2018-2026 | 15 | 53% | 20% | 27% |
| **Pooled 2007-2026** | **17** | **53%** | **18%** | **24%** |
| Pooled ex-2024-26 | 11 | 55% | 27% | 27% |

**Bottom line:** the sustained-stress rate collapses to ~18% at the option-relevant 36-day horizon when OOS episodes are included. VIOLET's intraday-heavy "94%/81%/56%" framing does not survive OOS re-measurement on a sustained-close basis.

---

## Method

- **Data:** `research/skew_vix_vvix_full.csv`, fetched from yfinance (`^SKEW`, `^VIX`, `^VVIX`). Coverage 1990-01 to 2026-04-17, but VVIX restricts usable sample to 2007-01-03 onward.
- **Pattern definition:** identical to Tier A — 20-day rolling change with SKEW ≥+10, VIX ≤−5, VVIX ≤−15.
- **Clustering:** consecutive fires within 20 days merged into one episode.
- **Windows:** 36d (May-19-equivalent) and 60d forward.
- **Code:** `research/violet_skew_tier_c.py`. Results CSV: `research/violet_skew_tier_c_results.csv`.

### Sample reproduction vs VIOLET's published table

VIOLET's Ep #1 (2014-11-XX) and Ep #2 (2015-10-XX) — which did NOT appear in her saved `vix_historical.csv` — now appear in my OOS pull exactly where she listed them:
- Ep #1: fires 2014-11-12, SKEW peak 138.5, VIX at start 13.02
- Ep #2: fires 2015-10-09 through 10-28 (multi-day cluster), SKEW peak 151.2, VIX at start 17.08

So VIOLET's episode list is faithful; the issue is that the data she used to generate stats for these two episodes wasn't retained, so her published base rate cannot be reproduced without re-pulling.

---

## The OOS episodes one at a time

**Ep #1 — 2014-11-12 (the "October bounce" tail).** VIX was 13.02 at fire. Over the next 60d the intraday high touched **25.20 exactly once**, close peaked at 23.57. Sustained close ≥25: never. In the 36d window, the intraday touch is still there but close never crosses 25. → This is a 1-print intraday event; an option holder would have needed near-perfect intraday execution to monetize.

**Ep #2 — 2015-10-09 through 10-28 (post-"flash crash" aftermath).** VIX was 17.08 at fire. Over 60d the intraday high reached 27.08, close 27.01 — but only on late-cluster days (Dec 2015 Fed tightening + EM stress). In the **36d window**, neither intraday NOR close crossed 25. The peak came at day ~45-50 (classic "option expired before the peak" profile). Sustained close ≥25 for 3d: never.

**Both OOS episodes are classic "VIOLET direction right, VIOLET magnitude/timing wrong."** Both hit mild stress intraday; neither produced a sustained regime; both peak outside a 36-day option window.

---

## Why pooling weakens VIOLET's case

| Metric | In-sample only (n=15) | Pooled w/ OOS (n=17) | Change |
|---|---:|---:|---:|
| Sust close ≥25 3d, 36d | 20% | 18% | −2pp |
| Sust close ≥25 5d, 60d | 27% | 24% | −3pp |
| Intraday ≥25, 36d | 53% | 53% | 0pp |
| Intraday ≥25, 60d | 73% | 76% | +3pp |

Adding the two OOS episodes lowers the sustained rates and leaves intraday rates roughly flat. This is consistent with the Tier A finding: **the intraday-vs-sustained gap is the dominant distortion,** and it's *amplified* OOS — those two 2014-15 episodes are almost pure intraday spikes.

---

## The live Apr 13 episode so far

The Apr 13 fire (Ep #17 pooled) has 4 trading days of forward data as of Apr 17 close:

| Measure | Value |
|---|---|
| VIX at fire (Apr 13 close) | 19.12 |
| VIX intraday peak (Apr 14 - Apr 17) | 19.09 |
| VIX close peak (Apr 14 - Apr 17) | 18.36 |

**VIX has gone *down* since the fire, not up.** The 36-day window has 32 trading days remaining; the episode is live and could still spike. But through 4 days: zero directional confirmation, and a widening gap from VIOLET's "central case VIX 28-38."

This is useful real-time data for Tier D (pre-commit a specific May 19 probability and track it).

---

## Where the sustained hits actually came from

Of the 4 pooled episodes that sustained close ≥25 for 5d in 60d, all 4 are **event-driven recessions or genuine carry unwinds**:

| Ep | Start | Event | Sust 25_5d_60 | Sust 25_3d_36 |
|---|---|---|:---:|:---:|
| 7 | 2020-04-17 | COVID re-acceleration | ✅ | ✅ |
| 8 | 2020-07-20 | COVID summer wave | ✅ | ✅ |
| 10 | 2022-03-24 | Fed hiking cycle begins | ✅ | ✅ |
| 14 | 2025-01-22 | DeepSeek / Apr 2025 tariffs | ✅ (peaked day 53) | ❌ |

So the pattern's sustained hits concentrate in **three distinct macro regimes**: (1) pandemic 2020 (2 episodes), (2) Fed pivot 2022 (1 episode), (3) tariff shock 2025 (1 episode). All are regimes where credit is either *widening* or *just beginning to widen* at the time of the next stress event — i.e., credit-confirmation, not the current credit-tightening state.

**None sustained closes ≥25 in a 36d window from a credit-TIGHTENING starting state.** That remains 0 for 4 (ex-COVID) in the relevant prior cohort and 0 for 2 OOS.

---

## Updated RED probability bands (post-Tier-C)

Compared to the Tier A bands, the pooled OOS data corroborates the downward revision and narrows the uncertainty range slightly.

| Outcome | Tier A estimate | Tier C estimate | Notes |
|---|---:|---:|---|
| VIX sustained close ≥25 for 3d by May 19 | 20-25% | **15-22%** | Pooled 18% at 36d; Apr 13 tracking as dud at day 4 |
| VIX sustained close ≥25 for 3d by Jun 12 | 25-32% | 22-28% | Pooled 24% at 60d |
| VIX sustained close ≥30 for 3d by May 19 | 12-18% | 10-15% | Historical sustained-30 rate ~24% at 60d, mostly 2020 events |
| VIX intraday print ≥25 by May 19 | 50-60% | 45-55% | Pooled 53% at 36d |
| VIX intraday print ≥30 by May 19 | 25-35% | 22-30% | |

---

## What this does to the VIOLET challenge

Three Tier-A/B/C findings now stack:

1. **Tier A:** intraday-vs-sustained is a 2.7× distortion.
2. **Tier B:** the pattern has NEVER fired from a credit-widening state — it's a complacency detector, not a credit cascade signal.
3. **Tier C (new):** OOS episodes are pure intraday spikes and the Apr-13-type "VIX sub-20, credit-tight, not-ex-COVID" setup has a **0 of 4** sustained-close record in a 36-day window, now expanded to a **0 of 6** with the two OOS hits.

**Combined implication:** The May 19 25C is at best a ~15-22% event on the sustained-close framing, and the current "close-to-zero" forward performance (4 days in) is not a particularly encouraging start. An equivalent Jun 18 or Jul 18 tenor captures the historical peak window materially better at a relatively small premium difference.

---

## Asks for Tier D (formal challenge to VIOLET)

Refined asks, tightened from Tier A/B:

| # | Ask |
|---|---|
| 1 | **Pre-commit a single May 19 probability.** RED's number: 15-22% sustained close ≥25 for 3d by May 19. VIOLET's number? |
| 2 | **Re-publish target distribution split between "intraday peak" and "sustained close" measures.** The 2.7× gap is the single most important correction. |
| 3 | **Show the credit-state cross-tab.** Pattern fires predominantly in FLAT credit states. In TIGHTENING states the only sustained hits are COVID-era (2020); ex-COVID it's 0 of 4. |
| 4 | **Address the tenor mismatch.** Ep 12 (2025-01) peaked at day 53. Ep 14 (2025-12) peaked day 11. VIOLET's own "analog cluster" has multi-modal timing; a 36d option window has historically missed the peak more often than caught it. |
| 5 | **Stop citing "20-year backtest" until you save the data.** Tier C required me to re-pull your pre-2018 episodes. Your published episode list is right, but the stats were not reproducible without re-fetching. |

---

## What this DOESN'T do

- Does not invalidate the direction. Volatility IS underpriced relative to latent credit risk; 76% of episodes see intraday ≥25 within 60d.
- Does not invalidate the position entirely. A May 19 25C can still pay on intraday spikes; the holder's exit discipline matters.
- Does not rule out Path B (structural stress). A genuine credit-widening pivot in the next 2 weeks would make this pattern's TIGHTENING-state base rate *not* the relevant prior — because credit would no longer be tightening.

## What this DOES do

- Strengthens the Tier A finding that VIOLET's headline is an intraday distribution, not a sustained one.
- Strengthens the Tier B finding that current starting state (credit tightening, not ex-COVID) has zero sustained hits in a 36d window.
- Adds a live real-time test: the Apr 13 episode through Apr 17 is tracking as a dud so far.

---

*RED Apr 19. Tier D (formal challenge to VIOLET's inbox) now ready to execute with Will's approval.*
