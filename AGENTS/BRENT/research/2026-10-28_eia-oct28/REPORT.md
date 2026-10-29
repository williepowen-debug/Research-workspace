# EIA week ending October 23, 2026 (released October 28): owner read and BRT-31 week three

**Captured:** 2026-10-28 23:48 ET, release-day current files from `ir.eia.gov/wpsr` (signed redirect to `/secure/wpsr/`) and EIA retail `pswrgvwall.xls` (saved here as `eia-retail.xls`). The sha256 of every input is in `evaluation.json`. All figures are [CONF EIA] for week ending October 23 unless marked. This read verifies the 11:24 ET Wednesday routine (`demand_destruction/data/eia_2026-10-28.md`); it does not replace it.

## Five findings

| # | Finding | Source |
|---|---|---|
| 1 | **Gasoline demand is not weakening on the BRT-31 test.** The exact four-week product-supplied comparison is **−0.6762%** YoY (8,629.25 vs 8,688.0 thousand barrels/day), short of the −1.5% bar. Week three is NON-QUALIFYING and the streak stays 0. The single week printed 8,358, down 624 from 8,982, while gasoline stocks rose 3.870M bbl. | psw01 `WGFUPUS2` |
| 2 | **Pump prices are still ~41% above a year ago** ($4.269 on October 26 vs $3.035 on October 27, 2025: +40.66%), so the BRT-31 precondition holds (counter 0 of 3). | EIA `EMM_EPMR_PTE_NUS_DPG` |
| 3 | **Cushing posted its first draw after five builds** (−0.624M to 26.970M). It is still about 7M above the 20.0M line. A one-week turn is not a trend. | table1 |
| 4 | **Distillate stays tight:** 102.824M bbl, about 10% below the five-year average and −8.3% YoY, while utilization slipped to 92.8%. That fits the diesel-led crack, but the December crack *fell* on October 27–28 (see the catch-up report), so stocks alone do not set the margin. | summary.txt, table1 |
| 5 | **US was a bigger net exporter:** total net imports −4.839M b/d (crude exports 4.854M, +1.412M WoW). Domestic production printed 13.992M (+0.723M WoW), a single-week swing; the four-week average is +0.7% YoY. The STATUS export-sign warning applies: higher exports do not by themselves show more supply. | table1 |

## BRT-31 week three, by the letter

| Field | Value |
|---|---|
| Current four weeks (w/e 10/23, 10/16, 10/09, 10/02) | 8358, 8982, 8408, 8769 → mean 8629.25 |
| Base four weeks (364 days earlier: 2025-10-24, 10-17, 10-10, 10-03) | 8924, 8454, 8455, 8919 → mean 8688.0 |
| Exact YoY | **−0.6762200736648250%** → NON-QUALIFYING (needs ≤ −1.5%) |
| Revisions vs 10/21 capture | none |
| Price leg, Monday after data week | 10/26 $4.269 vs 2025-10-27 $3.035 = +40.66% (≥ +20%, counter 0 of 3) |
| Streak / terminal event | 0 / none. OPEN at 40%. All three window prints > −1.0% |

**Rounding note:** the routine's "−0.679%" divided EIA's rounded averages (8,629/8,688). The letter grades the unrounded mean, −0.6762%. Both are non-qualifying, so nothing changes; the record carries the exact figure.

**Hoarding caveat (HOARDING.md, LESSONS #9):** inputs and output up while single-week supplied fell. That is the input-versus-supplied divergence the caveat names, and BRT-31 uses the four-week average for exactly that reason. No stockpiling conclusion.

**Not done:** contamination screening (it can only refuse NOT MET; the 10/20 bounded-review caveat stands); the post-grade monthly MGFUPUS2 record check (due after the window).

Reproduce: `evaluate.py` under the project venv (adapted from `../2026-10-21_eia-oct21/evaluate.py`; the diff is only the dates, labels and prior-capture path).
