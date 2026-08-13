# DR-4 — European energy aggregate baseline: what supplies Europe, what's impaired, and where storage breaks
**Date:** 2026-08-12 | **Mode:** Thesis | **Confidence:** High (storage/LNG/price arithmetic — all PRIMARY, reproducible) / **NOT ANSWERED** (channel-by-channel pipeline attribution — see §Gaps)
**Commission:** WALTER DR-4, `REQ-DEWEY-20260731-004` | **Consumers:** BRENT action; AEOLUS/HANS/CARL/MARCO info; DAEDALUS (org question)
**Engine:** primary-pull only (Will-ruled 2026-08-12 for this session's work). The `/deep-research` fan-out is re-gated to user-invoked, not removed — available had Will typed it.

---

## Key Finding

**The commission's central puzzle does not exist — it is an artifact of a one-week measurement window, and correcting it makes the picture worse, not better.** DR-4 was written to explain "THREE-PLUS impaired channels with TTF at €59 **FALLING**." The **level was exactly right** (TTF settled **€59.07 on 7/31**, the day the prompt was written) but the **direction is inverted**: TTF rose **+38.1% across July** (€42.78 → €59.07) and is **+83.3% year-on-year**, and on 7/31 it sat five sessions off a 52-week high of **€63.58** set 7/24. "Falling" described a one-week pullback inside a violent up-move. **It closed at €60.49 on 2026-08-12** [PRIMARY: ICE Dutch TTF future `TTF=F`, currency EUR/MWh, verified at instrument metadata]. There is no paradox to explain: impaired channels + rising price is coherent.

**The real finding is the storage trajectory, and it is worse than the puzzle framing implied.** EU storage is **59.32% full (670.4 of 1,130.2 TWh) as of gas day 2026-08-11** — **the lowest for that date in the five-year series, below even 2022**, the Russian-cutoff year. Demand-normalised, it is **19.05% of annual consumption vs 21.71% in 2022**. And the arithmetic to refill is brutal:

> **Reaching 90% requires 3.986 TWh/d for 87 straight days — 1.51× the current pace and 1.49× the best rate Europe has achieved in any of the last four years.** Reaching even the **80% deviation floor requires 2.687 TWh/d against a four-year best of 2.684 — a dead heat with the 2022 crisis-response maximum, sustained for three months.**

**Europe will not refill to target this year.** The landing zone is **77–80%**, and 80% is the ceiling, not the base case.

---

## Evidence

### (1) Storage: lowest for the date in five years

**EU storage, % full on the same calendar day** [PRIMARY: AGSI+ `agsi.gie.eu/api/data/eu`, updated 2026-08-12 18:20:03]

| date | 2022 | 2023 | 2024 | 2025 | **2026** |
|---|---|---|---|---|---|
| 06-01 | 47.8 | 69.0 | 70.1 | 48.9 | **40.8** |
| 07-01 | 58.5 | 77.3 | 77.7 | 59.1 | **49.3** |
| 08-01 | 70.2 | 85.8 | 85.2 | 68.8 | **57.2** |
| **08-11** | **73.6** | **88.6** | **87.7** | **72.3** | **59.3** |
| 11-01 | 95.0 | 99.3 | 95.2 | 82.8 | — |

2026 is **13.0pp below 2025** and **14.3pp below 2022** on the same date. This is the **second consecutive undershoot year** — 2025 peaked at only **83.2% (2025-10-12)**, itself far below the 95–99% of 2022-24.

**Demand-normalised (storage as % of annual consumption), Aug-11:** 2022 **21.71** · 2023 **28.78** · 2024 **28.37** · 2025 **23.33** · **2026 19.05**. Lowest in the series. ⚠️ *AGSI's `consumption` field is a **static annual reference** (3,519 TWh for 2024, 2025 **and** 2026 — identical), not an observed demand series. It normalises correctly but **cannot** be used to claim demand is flat.* (See §Gaps.)

### (2) The refill arithmetic — 90% is out of reach at any demonstrated pace

Storage does not inject to a regulatory date; it peaks and turns. Actual peaks: **2022-11-13 (95.7%)** · **2023-11-06 (99.5%)** · **2024-10-21 (95.3%)** · **2025-10-12 (83.2%)**. Median peak falls **87 days after Aug 11 ≈ 2026-11-06**, which is the window used below.

**Pace measured Aug-11 → that year's actual peak, applied to 2026:**

| year | realized pace | 2026 would land at |
|---|---|---|
| 2022 (crisis max) | **2.684 TWh/d** | **80.0%** |
| 2025 | 2.062 | 75.2 |
| 2023 | 1.488 | 70.8 |
| 2024 | 1.348 | 69.7 |
| **2026 current (30d)** | **2.646** | **79.7%** |
| 2026 current (14d / 7d) | 2.530 / 2.307 | 78.8 / 77.1 |

**Required pace from here:**

| target | needs | vs current | vs 4-yr best |
|---|---|---|---|
| **90%** | 3.986 TWh/d | **1.51×** | **1.49×** |
| **80%** | 2.687 TWh/d | 1.02× | **1.00× — a dead heat** |

**The binding rule:** the amended EU Gas Storage Regulation keeps the **90% target binding but flexible any time between 1 October and 1 December** (replacing the hard 1 November deadline), permits Member States to **deviate up to 10%** in unfavourable market conditions, and makes intermediate trajectories **indicative, not binding**. It was extended for 2025-2027 [[Council of the EU, 2025-07-18](https://www.consilium.europa.eu/en/press/press-releases/2025/07/18/gas-storage-council-greenlights-2-year-extension-of-reserves-filling-rules-to-safeguard-winter-supply/); [S&P Global, 2025-06-25](https://www.spglobal.com/energy/en/news-research/latest-news/natural-gas/062525-eu-gas-storage-rules-to-be-made-more-flexible-under-provisional-agreement); [European Parliament legislative train](https://www.europarl.europa.eu/legislative-train/package-clean-industrial-deal/file-amendment-to-gas-storage-regulation)]. **So the effective floor is ~80% — and the projection lands at or below it.**

### (3) The impairment is visible in LNG, and it is not a capacity problem

**EU LNG send-out, mean over the identical Jun-1→Aug-11 window** [PRIMARY: ALSI+ `alsi.gie.eu`]

| year | mean send-out | Aug-11 utilisation |
|---|---|---|
| 2022 | 3,669 GWh/d | 64.2% |
| 2023 | 3,746 | 46.9% |
| 2024 | 2,711 | 28.9% |
| **2025** | **3,885** | 42.7% |
| **2026** | **3,091** | **38.3%** |

**Send-out is −20.4% YoY (−794 GWh/d) in the year Europe most needs it** — and terminals are running at **38.3% of capacity, with 4,896 GWh/d of send-out capability idle.** **The constraint is cargoes, not regasification.** Over the 87-day window, the YoY send-out gap alone is **~69 TWh ≈ 6.1pp of EU storage** — most of the distance between the current trajectory and the 80% floor.

That is what "three-plus impaired channels" (Qatar FM in month 4, Libya/Greenstream post-Mellitah, Egypt post-Damietta) looks like measured at the receiving end.

### (4) The price already repriced — the market is not asleep

TTF dated closes [PRIMARY: `TTF=F`, EUR/MWh]: **7/1 42.78 → 7/24 63.58 (52wk high) → 7/31 59.07 → 8/5 52.40 → 8/12 60.49.** Trailing: **1m +18.0%, 3m +38.9%, 6m +80.6%, 1y +83.3%.** 52-week range **26.60–63.58** — today sits in the **top 5%** of it.

**The "impaired channels but calm prices" frame is false.** The market has repriced ~83% over twelve months. What it has *not* done is price a refill failure, because the refill failure has not happened yet — it becomes visible in October when injection stops short.

---

## Counter-Evidence

1. **Injection pace is not a constant, and I extrapolated it as one.** Pace responds to price spreads (summer-winter), weather, and cargo arbitrage vs Asia. A sustained JKM-TTF move toward Europe could lift pace above anything in the four-year sample. The projection is a *continuation* estimate, not a forecast.
2. **The 87-day window is a median of four observations** (62–94 days). Peak timing is weather-dependent; a mild October extends injection materially.
3. **80% may be an adequate landing.** 2025 peaked at 83.2% and Europe got through the winter. Low storage is dangerous *conditional on* a cold winter and tight LNG — it is not automatically a crisis, and I have not modelled the winter draw.
4. **The 10% deviation is conditional, not automatic.** It requires "unfavourable market conditions"; I have not verified whether the Commission has invoked or signalled it for 2026. **If it has not, 90% remains the formal bar and the miss is larger.**
5. **LNG send-out is a net measure.** A −20.4% YoY fall is consistent with impaired supply *and* with Europe being outbid by Asia *and* with lower European demand. The three are not separated here — the send-out number alone does not attribute cause.
6. **Two of the four prior years are structurally unlike 2026** (2022-23 crisis response, with emergency demand curtailment and record LNG pull). Using 2022 as "best achievable pace" may overstate what is achievable in a normal policy environment — which makes the 80% dead-heat *optimistic*.

**Explicit negative:** I found **no evidence** that the current TTF level reflects complacency about storage. The price action is directionally consistent with the impairment throughout. The commission's premise that these two facts conflict is **not supported.**

---

## Source Quality

All quantitative claims **[PRIMARY]**: GIE AGSI+ (storage) and ALSI+ (LNG) — the operator-reported EU aggregates, free API, no key; ICE Dutch TTF futures with instrument/currency verified at metadata; EU regulation via Council of the EU + European Parliament + S&P. Every figure reproducible from §Reproduction.

**Weakest links:** the 87-day injection window (n=4); the AGSI `consumption` static reference; and the absence of channel-level attribution, which means the *"what's impaired"* half rests on the LNG aggregate rather than a per-channel ledger.

---

## Gaps — this is a PARTIAL delivery on the "one ledger" ask

| Asked | Status |
|---|---|
| Storage math / TTF / the central puzzle | ✅ **answered, primary** |
| LNG channel (aggregate) | ✅ **answered, primary** |
| **Channel-by-channel pipeline attribution** — Norway, Algeria, Azeri, Russian residual | ❌ **NOT ANSWERED.** ENTSOG Transparency API is reachable (HTTP 200, `operationaldata.json`) but returns **point-level** records; attribution needs a border-point→channel mapping. That is a **build, not a pull** — logged to BACKLOG as `entsog_flows.py` |
| **Per-channel impairment quantification** — Qatar FM replaced share, Greenstream post-Mellitah, Egypt post-Damietta | ❌ **NOT QUANTIFIED at primary.** Visible only in the LNG aggregate |
| **Rhine logistics leg** (record freight) | ❌ **not pulled** |
| Demand side | ⚠️ **PARTIAL** — normalisation only; AGSI's reference is static, no observed demand series pulled (Eurostat/ENTSOG would be the source) |

**Four of six legs are unmet or partial. The two that are answered are the decision-critical ones** (the storage trajectory and the puzzle resolution), but this does **not** discharge the "one ledger" commission and should not be logged as if it did.

---

## For DAEDALUS — the org question, on evidence

DR-4 was also scoped to inform *agent-vs-no-agent* for Europe/gas. What this run learned about the **data layer**, offered as evidence rather than a recommendation:

- **The aggregate surfaces are excellent and cheap.** AGSI+ and ALSI+ are free, keyless, JSON, daily, operator-reported, with clean multi-year history. A daily storage/LNG monitor is a **low-cost, high-reliability** build — this entire storage analysis was ~6 API calls.
- **The channel layer is materially harder.** ENTSOG needs a maintained point→channel mapping; per-incident impairment (Mellitah, Damietta, Ras Laffan) is news-sourced and does not aggregate.
- **So the cost profile is barbelled:** the *aggregate* answer is nearly free and largely automatable; the *channel-by-channel* answer is where the recurring human/agent cost actually sits. If the org question is "does this need standing attention," the honest split is that the surface BRENT keeps needing (aggregate balance + trajectory) may be a **script**, while the part that needs judgement is incident attribution.

---

## Reproduction

```
AGSI+  storage : https://agsi.gie.eu/api/data/eu?from=YYYY-03-01&to=YYYY-11-15&size=300
ALSI+  LNG     : https://alsi.gie.eu/api/data/eu?from=YYYY-06-01&to=YYYY-08-11&size=100
                 (no API key required; browser UA advisable)
TTF            : yfinance ticker TTF=F — VERIFY currency at .info (EUR) before quoting a level
EU regulation  : consilium.europa.eu press 2025-07-18; europarl legislative-train
```
Fields: `full` (% of WGV) · `gasInStorage`/`workingGasVolume` (TWh) · `netWithdrawal` (GWh/d, negative = injecting) · ALSI `sendOut`/`dtrs` (GWh/d).
⚠️ **`consumption` is ANNUAL TWh, not daily GWh** — `consumptionFull` = `gasInStorage`/`consumption`. Verified on 6 records across 3 years.
⚠️ **AGSI/ALSI return HTTP 200 with `"total":0, "data":[]` on a malformed query** — a silent empty, not an error. Check `total` before trusting a result.

---

## Process Report

**Searches run:** 1 WebSearch (EU storage regulation). Primary pulls: 10 AGSI+/ALSI+ multi-year, 1 ENTSOG probe, TTF history + instrument metadata via yfinance.
**Data gaps:** ENTSOG channel mapping; per-channel impairment; Rhine freight; observed EU demand.
**Source frustrations:** ENTSOG is reachable but point-keyed — unusable without a mapping build. AGSI's silent-empty-at-200 (above) cost one confused probe.
**Errors caught in-run (3):** ① I initially projected injection to the **regulatory** date (Nov 1 / Dec 1) rather than the **physical peak** — storage turns to withdrawal before Dec 1, so extrapolating to it would have overstated the landing by several points; fixed by measuring actual peak dates. ② I mixed two window lengths when citing "best prior-year pace" (82d Aug→Nov1 = 2.959 vs 87d Aug→peak = 2.684) — the headline ratio is now on one consistent window. ③ **Treated AGSI `consumption` (annual TWh) as a daily GWh flow** and built a supply/demand balance on it; caught because the value was *identical* across 2024/2025/2026, which is implausible for a measured series. The invalid balance was discarded, not patched. *(③ is the same class as the H.8 $M-vs-$B error in the C3 run earlier today: two fields whose magnitudes are close enough that the wrong unit still looks sane.)*
**Confidence:** High on storage/LNG/price arithmetic. The projection is a continuation estimate with n=4 seasonality — **medium**, and stated as a range.
**If I had more time/tools:** build `entsog_flows.py` and close the channel ledger; pull Eurostat monthly demand to replace the static reference.
**Suggestions:** `entsog_flows.py` and a thin `gie_pull.py` (AGSI/ALSI) are the two builds this domain wants — both Will-gated per the build gate, **not** promoted unilaterally. Given how cheap AGSI/ALSI turned out to be, `gie_pull.py` is the higher ratio of value to effort.
