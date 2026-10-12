# DR-4 storage rerun — November 1 remains below 80% on observed pace

**Date:** 2026-10-12 | **Mode:** Thesis | **Commission:** HANS HNS-07 / PROME DOCKET L566; Will authorized queue execution 10/12 | **Confidence:** High (retrieved stock/pace arithmetic); Medium (conditional projection); no outcome grade.

## Key finding

EU storage is **73.61% full on gas day 2026-10-10**. Continuing the trailing 7/14/30-day stock-change rates gives **76.92/77.76/77.91% on gas day November 1**, all below HNS-07's 80% line. Reproducing DR-4's physical-peak method gives **76.47–77.32% at the corrected median historical peak, October 29**. These are conditional extrapolations, not proof the target cannot be reached. [PRIMARY: GIE AGSI+ EU API, retrieved 2026-10-12; calculations below.](https://agsi.gie.eu/api?continent=eu&from=2026-05-01&to=2026-10-12&size=200)

For HANS: the refreshed DR-4 instrument is on the **MISS side**. HANS's 10/01 instrument was also on that side, but it must be refreshed at the **10/15 checkpoint** before applying rule (b). HANS owns that confidence decision; this delivery does not re-mark 65%, resolve HNS-07 early, or move its November-1 gas-day resolver. Both models use GIE stock observations: agreement is methodological convergence, not independent source confirmation. [OWNER: HANS `workbook/PREDICTIONS.tsv#HNS-07`, inspected 10/12.]

## Evidence and comparable arithmetic

Source: GIE AGSI+ EU aggregate, 163 consecutive gas days May 1–October 10, retrieved October 12. No October-11 or October-12 observation was returned; publication lag is not added to the forecast horizon. Current stock **831.8602 TWh**, working volume **1,130.1222 TWh**, stock/volume **73.60799%** (published `full` rounds to 73.61%). The November-1 horizon is **22 gas days**. Fixed current capacity is assumed throughout. [PRIMARY: API above; archived public source rows in `research/2026-10-12_dr4/`.]

| Pace basis | Observed TWh/day | Nov-1 projection | Oct-29 physical-peak sensitivity |
|---|---:|---:|---:|
| Stock change, trailing 7 days | 1.70389 | 76.92% | 76.47% |
| Stock change, trailing 14 days | 2.13054 | 77.76% | 77.19% |
| Stock change, trailing 30 days | 2.20989 | 77.91% | 77.32% |

`pace = (stock_today − stock_N_days_ago)/N`; `projection = 100 × (stock_today + pace × horizon)/current_working_volume`. Exact-date endpoints are used, not the last N returned rows. Reaching 80% needs **72.23756 TWh more**, or **3.28353 TWh/day** over 22 days: **1.54×** the trailing-14-day stock pace. [DERIVED from PRIMARY GIE rows.]

The comparable percentage-point method used by HANS gives `(73.61−70.88)/14 = 0.19500 pp/day`, hence **77.90%** on November 1. This differs slightly from the TWh method because working volume changed. Required pace is **0.29045 pp/day**, below the season's best observed trailing-14-day pace **0.31071 pp/day ending June 4**. The hit path therefore does **not** require an unprecedented seasonal pace. [DERIVED from same source; not a HANS rule grade.]

### Historical peak correction and seasonal check

Fresh GIE May–November histories reproduce the four physical stock peaks: **2022 Nov-13, 2023 Nov-6, 2024 Oct-21, 2025 Oct-12** (214 rows per year). Their mapped 2026 median date is **October 29**, 19 days beyond October 10. August DR-4 incorrectly labelled November 6 / 87 days beyond August 11 as the median; the actual August horizon is **79 days**. Its dependent projections and categorical ceiling claim have been explicitly corrected at the original report. The helper's November-6 default is a convention, not an empirical median. [PRIMARY: GIE historical API queries; DERIVED calendar arithmetic.]

As a different sensitivity, adding each prior year's *actual stock change from October 10 to November 1* to today's stock gives **77.36% (2022), 76.03% (2023), 74.03% (2024), 73.60% (2025)**. This includes withdrawals after an early peak and also sits below 80%; it does not estimate probabilities. The low starting fill in 2026 gives more physical headroom than those mostly full years. [DERIVED from archived GIE rows.]

### Measurement caveat

On October 10, reported stock falls **0.0872 TWh** while reported working volume falls **2.2700 TWh** and published fill rises **0.14pp**. Reported injection minus withdrawal is nevertheless **+1.99823 TWh**. These fields are not a perfectly reconciled daily stock-flow account; the cause of the difference is not established. Do not classify this observation as the start of a physical withdrawal regime from stock alone. Integrating reported injection minus withdrawal over the same 7/14/30 days instead yields November-1 estimates **77.47/77.84/77.94%**: the measurement choice does not change the side of 80%. [PRIMARY GIE fields; DERIVED integration.]

## Counter-evidence and limits

- Faster injections can occur. Seasonal best is not a ceiling; current pace alone cannot resolve a future outcome.
- Four historical seasons are a small, regime-mixed sample. A mild late October or altered LNG/demand balance can move both pace and peak date. No weather or winter-withdrawal forecast was made.
- Capacity/reporting changes affect percentage-point pace; the stock-flow discrepancy remains unattributed. Historical peaks are data-vintage dependent.
- The 10/15 checkpoint needs fresh readings. The latest available gas day here is 10/10; this does not prove a permanent D+2 publication rule.

## Source quality, reproduction and process

All quantitative inputs are **PRIMARY GIE AGSI+**; derived estimates are labelled. Public rows and SHA-256 provenance are preserved in `AGENTS/DEWEY/research/2026-10-12_dr4/`. Repeat `python3 AGENTS/DEWEY/scripts/gie_pull.py series --dataset agsi --from 2026-05-01 --to 2026-10-12 --size 200 --json`; for 2022–2025 use each year's May 1–November 30 and size 250. Sort by gas day, enforce daily continuity, take the maximum `gasInStorage` for each historical season, map dates to 2026, and take their median. Use the equations above; units are TWh stocks and GWh/day flows divided by 1,000. The annual `consumption` field is unused.

**Process:** five successful series pulls; direct sandbox pull failed DNS, authorized network execution succeeded. Web opened GIE pages/API documentation, but could not read the API endpoint; calculations use the actual direct JSON pulls. Fresh numerical results replace stale research context for this question. No fan-out engine used. Gaps: cause of the stock-flow/capacity discrepancy; weather and causal supply attribution outside the rerun's scope. Suggestion: HANS should compare updated instruments on the same gas day at October 15, retaining the fixed resolver and shared-source caveat.
