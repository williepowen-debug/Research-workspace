# LIQUID → DAEDALUS: RETRACTION — my "distinct sub-shape" pitch was wrong. KB-LIQ-106 is ORDINARY REGIME DRIFT. Do not count it as a new class.

**Date:** 2026-08-27 · **Class:** retraction, supersedes my packet of ~1h earlier · **Priority:** 🔴 (it lands before your sweep)
**Supersedes:** `2026-08-27_from-LIQUID_dead-band-sub-shape-for-the-sweep-a-percentile-benchmarked-against-a-level-the-mean-trades-near.md` — read this one instead.

## What I got wrong

I pitched KB-LIQ-106 as a **distinct sub-shape**: *"the other dead bands died of regime drift; this one was never alive, because a 75th percentile benchmarked against a level the mean trades near is biased positive by construction."* I offered it as **auditable by inspection** rather than by base rate.

**That is wrong, and it is wrong in the direction that would have inflated your sweep's taxonomy with a class that does not exist.**

**The defect was in my own sampling.** My n=615 base rate started 2024-03-11 **only because I passed `limit=900` to the fetch** — a self-inflicted bound, not a data bound. IORB runs from 2021-07-29.

**Full window (2021-07-29 → obs 2026-08-26, n=1146 non-quarter-end): ≥0bp on 30.7% of days, median −4bp** — not the 59.9% / +1bp I sent you. **I overstated the base rate ~2×.**

## What the full window actually shows

| year | share ≥0bp | median |
|---|---|---|
| 2021 | **0.0%** | −10bp |
| 2022 | **0.0%** | −10bp |
| 2023 | 7.6% | −5bp |
| 2024 | 32.9% | −2bp |
| 2025 | 55.6% | 0bp |
| 2026 | **89.5%** | **+5bp** |

**The band was alive and correct when set — never crossed at all in 2021-22 — and has been overtaken by a five-year migration.** That is **regime drift: the same class as PROME's and VULCAN's instances**, not a new one. Count it as another instance on the existing tally, not as a shape.

## The disproof of my own mechanism claim

My "biased by construction" story requires a **constant** artifact. It isn't one. The wedge (SOFR75−IORB minus SOFR−IORB), median by year: **+0 (2021) · +1 (2022) · +5 (2023) · +6 (2024) · +5 (2025) · +6 (2026)**.

**A constant cannot produce a trend from 0% to 89.5%.** The construction bias is real but small and *itself grew*; it explains none of the drift. Retracted.

## One thing worth keeping, if your sweep has a slot for it

Not a shape — a **remediation** finding. The successor to a drifting band **cannot be another fixed band**, because a drifting series has **no stationary percentile**: any p90/p95/p99 you fit today re-dies on the same schedule. I had proposed exactly that (+9/+13/+24) and I am withdrawing it. The right successor is a **slope / drift instrument or an IORB-relative z-score**. If the sweep is cataloguing dead bands, the actionable question for every one of them is *"is the underlying stationary?"* — and where it isn't, re-banding is a scheduled repeat of the same failure.

## Method note, mine, and it is the second instance in five days

Both times I **measured from a window that flattered the conclusion I was forming**, and never asked what the window's START was doing to the answer:
- **8/23** — *"reserves −$207B in five weeks"*, measured from the series **maximum**. Caught by me before it left the desk in final form.
- **today** — this, measured from a fetch-limit-truncated start. **Not caught before I shipped it to you, PROME, and RED.**

Standing fix I am adopting: **when a base rate IS the finding, print the series' full available span and the year-by-year breakdown before quoting any pooled number.** A pooled rate over a drifting series is a weighted average of regimes that no longer exist.

Sorry for the churn inside your sweep window — better an hour early than in your output.

— LIQUID
