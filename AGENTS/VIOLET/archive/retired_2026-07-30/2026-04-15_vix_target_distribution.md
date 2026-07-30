# Where does VIX go if the pattern repeats?

**Date:** 2026-04-15
**Fire date:** 2026-04-13 (SKEW-VIX-VVIX divergence, episode #17)
**Spot at analysis:** VIX 18.09
**Prior 40d VIX peak:** 31.05 (Mar 27)
**SKEW peak in window:** 156.9

## Method

Using the 16 completed historical SKEW divergence episodes (from `2026-04-15_skew_divergence_episodes.md`), apply each episode's *next-60d peak VIX % change* to today's spot of 18.09 to get an implied peak-VIX distribution for the current fire.

Then condition on two subsets:
1. **High-SKEW cohort (SKEW peak >150):** episodes #2, #9, #13, #14, #16 — closest match to our 156.9
2. **Back-to-back analogs (fire within 90d of prior fire):** episodes #4, #8, #14, #16 — closest match to our Mar-27 → Apr-13 sequence

## Unconditional distribution (all 16 completed episodes)

| Statistic | % change | Implied VIX peak |
|-----------|---------:|-----------------:|
| Min | +12.4% | 20.3 |
| 25th percentile | +33.4% | 24.1 |
| **Median** | **+54.6%** | **28.0** |
| Mean | +79.1% | 32.5 |
| 75th percentile | +107.0% | 37.5 |
| 90th percentile | +180% | 50.7 |
| Max (#14, 2025-01) | +246.6% | 62.7 |

**Read:** ~75% of the mass sits between **VIX 24 and 38**, with a meaningful right tail reaching **50-63** driven by back-to-back divergence clusters (2024-11 / 2025-01).

## Conditional — High-SKEW (>150) cohort (n=5)

| # | Episode | % change 60d | Implied VIX peak |
|---|---------|-------------:|-----------------:|
| 2 | 2015-10 | +92.5% | 34.8 |
| 9 | 2021-06 | +37.3% | 24.8 |
| 13 | 2024-11 | +105.4% | 37.2 |
| 14 | 2025-01 | +246.6% | 62.7 |
| 16 | 2025-12 | +110.6% | 38.1 |

- Median: **+105.4% → VIX 37.2**
- Mean: **+118.5% → VIX 39.5**
- 4 of 5 cluster in a **34-38 band**; one outlier at 62.7

**Read:** SKEW-peak >150 historically raises both the center and the tail. Central case from this subset is **VIX 35-40**, with the back-to-back tail at **62**.

## Conditional — Back-to-back / cluster analogs (n=3, dropping the peaceful #4)

| # | Episode | Days since prior fire | % change 60d | Implied VIX peak |
|---|---------|----------------------:|-------------:|-----------------:|
| 8 | 2020-07 | ~90 | +37.4% | 24.8 |
| 14 | 2025-01 | ~62 | +246.6% | 62.7 |
| 16 | 2025-12 | ~210 | +110.6% | 38.1 |

- Median: **+110.6% → VIX 38.1**
- Mean: **+131.5% → VIX 41.9**

**Read:** When divergence fires early in the decay of a prior vol event (which is OUR exact setup — 17 days after Mar 27 peak), historical range is **25-63 with a 38 midpoint**. The tightest analog by time-structure is #14 (fired 2 months into the tail of #13 which peaked at 23.2). Ours is even tighter temporally — fired 17 days after a 31.05 peak.

## Near-term vs terminal

The 60-day window understates how fast this could move. Using the 30-day stats from the same 16-episode base:

- Median 30d peak change: **+37.3% → VIX 24.8**
- 75th percentile 30d: **+64.7% → VIX 29.8**

So the first leg (by ~May 15) plausibly lands **VIX 24-30**; the terminal peak (by ~Jun 15) pushes **28-40 central, 50+ tail**.

## Cross-check with market-implied levels

Today's VIX_OPTIONS.tsv snapshot (2026-04-15):
- **Apr 29 (FOMC) expiry:** C/P OI 9.01 — top call strikes 25, 30, 24, 18, 20. Call-wall center of gravity ~**25-30**.
- **May 19 expiry:** 3.24M call OI — top strikes 35, 25, 70, 45, 28. Options market pricing heavy wing risk to **35**, with notable tail OI at **45 and 70**.

Options market and historical analogs agree on a **25-35 central scenario** for the 30-60d peak. Both datasets identify the **40-50+ tail** as non-trivial.

## Synthesis — Where does VIX land if the pattern continues?

| Horizon | Central (median) | Base case range | Tail scenario |
|---------|-----------------:|-----------------:|---------------:|
| 30-day peak | **VIX ~25** | 22-30 | 38+ |
| 60-day peak (unconditional) | **VIX ~28** | 24-38 | 50-63 |
| 60-day peak (high-SKEW cohort) | **VIX ~37** | 34-40 | 62+ |
| 60-day peak (back-to-back cluster) | **VIX ~38** | 25-63 | 62+ |

**Point estimate:** If the pattern continues, highest-probability peak is **VIX 28-38 within 60 days**, which is consistent with the May 19 call-wall at 35 and with SKEW-peak-conditioned historicals. Tail risk to **50+** is a one-in-five event driven by the specific 2025-01 analog.

**What would shift the distribution:**
- SKEW rolling down below 140 → falls into low-SKEW cohort, central case drops to **22-26**
- Another divergence fire within 30 days → promotes us firmly into back-to-back cluster, tail toward **45-55** becomes modal
- Term structure inversion without spot spike → signals peak is imminent (per thesis v3.1 falsification), central stays 28-38 but timing compresses

## Caveats

- n=16 is small; confidence intervals are wide
- "Peak VIX" in historical record can be a single intraday print, not a sustained regime
- 2024-2026 has been an outlier-dense period; five of the 16 episodes came in 24 months
- Current SKEW has already dropped to 149.94 from its 156.9 peak — if we're on the downslope, shift the read toward the 140-150 cohort (central **26-29**)

*VIOLET 2026-04-15. Input data: `research/2026-04-15_skew_divergence_episodes.md`, `workbook/VIX_OPTIONS.tsv`.*
