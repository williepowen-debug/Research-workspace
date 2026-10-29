# CARL L842 — Q3 GDP advance + September personal income and outlays

Read 2026-10-29 09:01–09:05 ET by CARL (session carl-1029am), against the prep card written BEFORE release (`research/2026-10-26_L786/GDP_PCE_OCT29_PREP.md`). Primary sources: BEA 26-46 *Personal Income and Outlays, September 2026* and BEA 26-45 *GDP (Advance Estimate), 3rd Quarter 2026*, both released 2026-10-29 08:30 ET; release PDFs, historical-comparison workbooks and the release pages are saved in `source/` with `SHA256SUMS.txt`. Monthly levels from FRED (same-day vintage, pulled 09:02 ET through `FORGE/tools/market-data/fetch.py`, `source/fred_pull.json`). Descriptive read only: no new forecast, threshold, score rule or capital instruction. HENRY grades core PCE; CARL does not duplicate that grade.

## 1. Revisions first (old vintage = BEA 9/30, saved 10/26; new vintage = BEA 10/29)

| Series | July old → new | August old → new | Note |
|---|---|---|---|
| Real PCE (PCEC96, $bn chained 2017, SAAR) | 16,862.5 → 16,882.2 | 16,955.3 → 16,975.0 | Both months +19.7 up. August m/m now +0.5497% (BEA: 0.5; old vintage rounded 0.6) |
| Real DPI (DSPIC96) | 18,415.4 → 18,414.1 | 18,410.5 → 18,416.2 | August m/m −0.027% → +0.011% (still "0.0") |
| Saving rate (PSAVERT) | 4.6% → 4.5% | 4.1% → 4.0% | Revised down 0.1 point both months |
| PCE price index (PCEPI) | 131.172 → 131.187 | 131.579 → 131.611 | August m/m +0.32% (0.3, unchanged at precision) |
| Core PCE price (PCEPILFE) | 130.133 → 130.148 | 130.455 → 130.489 | August m/m +0.2474% → +0.262% (BEA now prints 0.3 vs 0.2) |
| Q2 monthly real PCE (Apr/May/Jun) | 16,727.4 / 16,784.6 / 16,854.0 | unchanged | Q2 base for the quarterly guard unchanged |

BEA attributes the July/August income revisions to revised BLS CES data and newly available Fiscal Service monetary-interest data (release text).

## 2. September monthly — volume, income, buffer (separated from prices)

| Measure | September | Basis |
|---|---|---|
| Nominal PCE | **+0.5% (+$113.1B SAAR)**: goods +$35.1B, services +$78.1B | BEA release |
| PCE price index | **+0.49% m/m; 3.6% y/y** (core +0.32% m/m, 3.1% y/y — HENRY grades core) | BEA; FRED levels |
| **Real PCE** | **+0.015% m/m (+$2.6B chained), BEA "less than 0.1 percent" / 0.0** | BEA; FRED 16,975.0 → 16,977.6 |
| Real goods | **−0.30%** (durables −0.80%; nondurables −0.03%) | FRED DGDSRX1 / PCEDGC96 / PCENDC96 |
| Real services | **+0.16%** | FRED PCESC96 |
| Nominal DPI | +0.2% (+$52.7B) | BEA |
| **Real DPI** | **−0.27% m/m (−$50.1B chained)**; BEA −0.3, the same size as 2022M06; last larger fall 2026M04 (−0.4) | BEA historical comparisons |
| **Saving rate** | **3.8%** vs August revised 4.0% (prior vintage 4.1%); **lowest since October 2022 (3.6%)**; personal saving −$60.2B to $911.1B | BEA historical comparisons |

**Where the nominal dollars went (BEA chart, labels mapped by sorted order and verified: goods items sum to +35.1, services to +78.1):** gasoline and other energy goods **+$45.7B** (40% of the whole nominal rise), transportation services +18.4, housing and utilities +17.8, food services and accommodations +15.5, health care +13.0, financial services and insurance +11.1, other services +6.4, food and beverages (off-premises) +1.5, other nondurables +0.8, clothing +0.7, furnishings +0.6, recreational goods −0.0, other durables −0.2, nonprofit final expenditures −0.9, recreation services −3.2, **motor vehicles and parts −$14.0B**.

**Read (prep step 2):** spending held flat in volume while real income fell and saving dropped. The prep card's own reading rule applies: *"falling saving with spending/income weakness indicates buffer drawdown."* Nominal spending rose on the pump (gasoline is the largest single line, consistent with September CPI gasoline +9.09%, KB-531), and goods volume — led by vehicles — fell. This is the aggregate shape of a cost squeeze being financed out of saving. ⚠️ It does not identify WHO drew down: the bottom 60% is not measured by these data, and a falling aggregate saving rate can come from either end.

## 3. Q3 quarterly — consumption versus headline GDP

| Component (Q3 2026 advance, SAAR) | Value | Q2 |
|---|---|---|
| Real GDP | **+3.4%** | +2.2% |
| **Real PCE** | **+3.8%** (goods +3.0%, durables +2.3%, nondurables +3.4%; services +4.1%) | +3.8% |
| PCE contribution | **+2.52 pp** (goods 0.63, services 1.89) | 2.51 pp |
| Change in private inventories | **+1.61 pp** | −0.53 pp |
| Net exports | **−3.32 pp** (exports −0.68; imports −2.64, goods imports +26.4%) | −1.10 pp |
| Government | +0.90 pp (federal nondefense, Strategic Petroleum Reserve sales accounting per BEA text) | −0.01 pp |
| Fixed investment | +1.66 pp (equipment +1.16, information processing led) | 1.35 pp |
| Final sales of domestic product | **+1.7%** | 2.8% |
| Final sales to private domestic purchasers | +4.9% | 4.6% |
| Real DPI (quarterly) | +2.3% | −0.2% |
| PCE price index (quarterly average) | +2.1% (core 2.5%) | 5.0% (core 3.3%) |

Arithmetic check: Q3 average real PCE (16,882.2 + 16,975.0 + 16,977.6)/3 = 16,944.93 vs Q2 16,788.67 → **+3.775% annualized**, matching BEA 3.8. The prep guard said a flat September would give about +3.27% at the old vintage; the upward July/August revisions (+19.7 each) add the rest. **Q3's consumption strength is July–August carry; September itself was flat.** Headline GDP is flattered by inventories (+1.61 pp) and SPR accounting (government); final sales of domestic product grew only 1.7%. A strong headline GDP print is not evidence of consumer strength beyond the 3.8% PCE line itself.

The quarterly PCE price figure (2.1% SAAR) is a quarter-average comparison and is not the September monthly rate (+0.49% m/m) or the 3.6% y/y; do not splice them.

## 4. What this does and does not establish (10/12 scope judgment, both directions)

| Claim | Effect |
|---|---|
| Broad aggregate spending collapse | **Still NOT established.** Q3 real PCE +3.8%; September real PCE flat, not negative. One flat month is not a contraction. |
| Cost squeeze financed from buffers | **Strengthened in aggregate.** Real DPI −0.27%, saving rate 3.8% (lowest since Oct 2022), nominal growth led by gasoline, vehicles down. |
| Bottom-60 / cohort convergence | **Not addressed.** Aggregate national accounts carry no cohort split; the 60/40 framing remains an assumption. |
| Healthcare services (DOC-P10 source feed) | BEA text: within Q3 services, **"the increase was led by health care (mainly hospitals and outpatient services)"**; September health care +$13.0B nominal. Passed to DOC as source evidence. **DOC grades DOC-P10**; this read is adverse to DOC's written pre-release expectation of health care growing slower than total services, but the category growth rate itself (NIPA Table 2.4.1/2.3.x) was not retrieved here — DOC must read the table before grading. |

## 5. Existing letters — exact consequences

| Letter | Consequence |
|---|---|
| Any OPEN CARL prediction (thesis/PREDICTIONS.tsv) | None is keyed to BEA PCE, DPI, saving rate or GDP. **No prediction resolved or moved.** |
| V6 downgrade trigger (continuing claims drop AND no DQ/spending exhaustion signal Jun–Aug 2026) | Window closed; not re-applied from a September print. No change. |
| V8 K-shape | Governed by `thesis/TRADEDOWN_INSTRUMENTS.md` (Census/issuer instruments), not BEA aggregates. No change. |
| V12 Fed-locked | Un-fire letter is the Fed's own easing language, not a PCE print. Core PCE 3.1% y/y noted; HENRY owns that grade. Score 5 unchanged. |
| Full-thesis kill (v2.6.6) | Keyed to claims and NY Fed Page 14 card flow; untouched. |
| **Convergence score** | **53/70 v2.6.6 unchanged.** |

No capital meaning. No threshold moved.
