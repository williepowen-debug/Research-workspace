---
signal_id: SIG-W-20260725-016
dispatched: 2026-07-26T00:10:00Z
origin: Will-Telegram image batch 2026-07-25 (~23:33Z) — a research-note excerpt with a Bloomberg-sourced chart, "Inflation Vol Is Picking Up Under the Surface." Publishing house NOT identified in the crop.
source: Chart source stated as **Bloomberg**. Series: *"Average Vol of All Underlying CPI Components (Std Dev of MoM Value Over Last 12 Months)."* ⚠️ **The commentary author is UNIDENTIFIED** — the crop shows the bullet text and chart but no masthead.
signal_type: threshold-crossed
domain: MACRO_INFLATION
cluster: CONSUMER_STAGFLATION
cluster_secondary: FED_FRAMEWORK
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: [CARL]
info: [HENRY, BOND, RED]
confidence: 0.72
confidence_note: The CHART is legible with a fully specified series definition and a ~27-year history, and the visual claim is unambiguous — the latest reading spikes from ~1.0 to ~1.45, approaching the 2020-2023 peaks of ~1.5-1.55 and exceeding the 2008 peak of ~1.3. The discount is that the COMMENTARY AUTHOR IS UNIDENTIFIED (no masthead in the crop), so this is an unattributed reading of a Bloomberg-derived series; and the series is a derived construct whose exact component set and weighting are not stated. Routed on the chart, not on the author.
verify_verdict: CHART-LEGIBLE, AUTHOR UNIDENTIFIED. Not verified against a BLS reconstruction.
routing_note: CARL action — CPI composition and inflation transmission are its lane. BOND info (the series bears on term premium and the inflation-risk-premium argument). HENRY info (Fed reaction function). RED §3.5 pull-complete → no handoff. **CARL is also §3.5 pull-complete** → BOARD + route_log only, no handoff written for it either; it reaches this via its own whole-INDEX diff.
dispatch_note: Routed because a DISPERSION measure says something a LEVEL measure cannot, and the fleet tracks levels. Whether headline CPI is 2.4% or 3.1% is a different question from whether the components underneath are moving coherently — and the second is what makes a level forecast reliable or useless.
---

# Inflation volatility is near pandemic-surge highs — underneath a headline nobody is calling volatile

**A dispersion statistic, not a level one. That's the reason it's worth a row: the fleet tracks the level, and this measures whether the level is trustworthy.**

## The datum

`[Chart source: Bloomberg. Series: Average Vol of All Underlying CPI Components — std dev of MoM value over the last 12 months]`

**Stated claim:** *"The pick-up in inflation vol is becoming increasingly apparent at the top level, but it is unmistakable under the surface. The average volatility across US CPI components is close to revisiting the highs of the pandemic price surge."*

**Reading the chart directly (≈1998→2026, % points):**

| Period | Level |
|---|---|
| Late 1990s–2007 baseline | ~1.0–1.2 |
| **2008-09 spike** | **~1.3** |
| 2010-2019 | ~0.9–1.2, **trough ~0.85 around 2014** |
| **2020-21 pandemic surge** | **~1.5** |
| **2022-23 second peak** | **~1.55 — the record on this series** |
| 2024–early 2026 decline | back to ~1.0-1.1 |
| **🔴 Latest** | **spikes to ~1.45** — approaching the pandemic highs, **already above the 2008 peak** |

**The move is a near-vertical reversal off a ~1.0 base, circled on the chart by the author.**

## 🔑 Why a dispersion measure is worth routing when a level measure wouldn't be

**Component-level volatility is a statement about the RELIABILITY of the aggregate, not about its direction.** Two things follow, and they cut opposite ways:

1. **Forecastability degrades.** When components move coherently, the aggregate is predictable from a few drivers. When component vol is at pandemic-era highs, **month-to-month CPI prints become noisier and single-month reads become less informative** — which is a direct caution on the fleet's own habit of grading off individual prints. → `[[feedback_single_month_subcomponent_skepticism]]`, which this signal supports with a measurement rather than an intuition.
2. **It is a precondition for regime change, not evidence of one.** High dispersion preceded and accompanied the 2021-22 surge — but it also just *describes* an economy absorbing heterogeneous shocks (tariffs, an oil shock, shelter normalising) without necessarily going anywhere. **It says the distribution is widening. It does not say the mean is moving.**

**CARL owns which of those it is.** The signal deliberately asserts neither.

## Where it lands

- **Tariffs and oil are both live component-level shocks right now** — the Canada 50% tariffs effective **8/19** (`SIG-W-20260720-002`) and the Iran-driven energy complex. **Both are exactly the kind of input that raises component dispersion without a clean read-through to the aggregate.** That is a plausible benign explanation and should be tested before anything more dramatic.
- **BOND's angle:** rising inflation dispersion is a standard argument for a **higher inflation risk premium**, which sits directly on the **30Y above 5% for the longest stretch since 2007** (`SIG-W-20260723-012`) and the **2Y/5Y 7/27, 7Y 7/28** auctions.
- **HENRY's angle:** a Fed reacting to noisier component data has a harder job — and **FOMC is 7/29**, with September-hike odds already above 80% (`SIG-W-20260723-012`).

## ⚠️ What would make this solid rather than suggestive

**The author is unidentified** — I read a cropped excerpt with no masthead, so this is an unattributed reading of a Bloomberg-derived series. **It is routed on the chart's legibility, not on anyone's authority.**

**It is reconstructible from primaries.** CPI component-level MoM data is public at BLS; a 12-month rolling std-dev across components is straightforward to rebuild. **If CARL wants to use this, it should be rebuilt rather than cited** — the component set and weighting are unstated here, and those choices drive the result. → `[[finding_loadbearing_number_must_be_reproducible]]`.

*Routed by WALTER 2026-07-25. Dispersion, not level — and the author is unnamed, which is stated rather than smoothed over.*
