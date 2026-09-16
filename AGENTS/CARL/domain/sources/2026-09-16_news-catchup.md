# CARL: September 11–16 news catch-up

Evidence cutoff: September 16, 2026, approximately 12:30 ET, BEFORE the FOMC decision. Research by CARL through Codex/Astra. Source vintages and reproducible calculations: `research/2026-09-16_news-catchup/`. No prediction probability, vector score, instrument definition or capital approval changed. Convergence remains 53/70, thesis v2.6.6.

**Judgment:** September fuel pressure intensified, but August spending rebounded broadly and issuer credit evidence is mixed. These releases weaken an imminent aggregate retrenchment claim. They do not identify the bottom-60% household outcome, and August spending cannot test September's energy shock.

## Spending: meaningful counterevidence

[Census CB26-153](https://www.census.gov/retail/marts/www/marts_current.pdf), released September 16, measures August. Nominal seasonally adjusted sales rose **1.2% MoM**, including **1.2% excluding autos and gasoline**; July headline revised to **−0.5%**. CARL independently verified PROME's handoff at Table 1 and reproduced the control group: **+1.36% August**, after **−0.44% July**. Excluding nonstore retailers as well, control rose **0.75%**, after **+0.21% July**. Total August sales stood **0.70% above June**. The rebound is neither solely fuel inflation nor solely online sales; the level comparison also limits extrapolation from one strong month. These are nominal measures, not real PCE or household-cohort evidence.

Source correction: `RSXFS` excludes **food services**, not food. The prior CARL dashboard's “ex-food” wording was wrong. Grocery stores remain inside that series.

### Registered Tier-1 trade-down tests: still three against

Recomputed on September 16 FRED vintage, using the instruments already registered in `thesis/TRADEDOWN_INSTRUMENTS.md`. Price-adjusted growth = `(sales_t/sales_t-12)/(CPI_t/CPI_t-12)-1`; not literal units or a household panel.

| Test | July, current vintage | August |
|---|---:|---:|
| Grocery proxy, real YoY | −2.02% | **−1.61%** |
| Restaurants, real YoY | +1.74% | **+2.40%** |
| Grocery less restaurant growth | −3.76pp | **−4.01pp** |
| General merchandise share, year-ago → current | 12.234% → 12.087% | **12.191% → 12.018%** |
| Apparel, real YoY | +0.57% | **+0.62%** |

[Retail](https://fred.stlouisfed.org/series/RSDBS), [restaurant sales](https://fred.stlouisfed.org/series/RSFSDP), [food-at-home CPI](https://fred.stlouisfed.org/series/CUSR0000SAF11), [food-away CPI](https://fred.stlouisfed.org/series/CUSR0000SEFV), [general merchandise](https://fred.stlouisfed.org/series/RSGMS), [retail denominator](https://fred.stlouisfed.org/series/RSXFS), [apparel sales](https://fred.stlouisfed.org/series/RSCCAS), [apparel CPI](https://fred.stlouisfed.org/series/CPIAPPSL). RSDBS includes beverages, so the grocery deflator is a proxy. Tier 1 only disconfirms; it cannot confirm bottom-cohort trade-down. DG Tier 2 remains in-sample, awaiting Q3. V8 stays 4 on its other evidence; this leg contributes no support. September 28 historical revisions are a vintage check, not another observation.

## Credit: mixed, not synchronized deterioration

| Issuer / August observation | Change | Interpretation |
|---|---|---|
| Capital One domestic cards | 30+ performing delinquency **3.48% → 3.57%**; NCO **4.12% → 4.16%**, July→August | Modest sequential deterioration; delinquent dollars also rose $9.014B→$9.297B. |
| Capital One auto | 30+ performing delinquency **4.39% → 4.54%**; NCO **1.48% → 1.66%** | Adverse monthly direction; not a quarterly CRL verdict. |
| Synchrony | 30+ **4.2%**, unchanged MoM, vs4.3% year ago; NCO **4.7%→4.9%**, vs5.1% year ago | Adjusted NCO **4.9%→4.9%**: reported rise disappears after issuer recovery allocation. Avoid calling this broad acceleration. |
| Bread Financial | 30+ **5.36% vs5.84% YoY**; net principal loss rate **6.40% vs7.57%** | Improvement includes delinquent principal **$885M vs$934M**, not denominator growth alone. |

Primaries: [Capital One August](https://investor.capitalone.com/static-files/0191ea61-5769-40a9-b1fe-300682ded325), [July](https://www.sec.gov/Archives/edgar/data/927628/000092762826000093/ex991july2026creditmetrics.htm), [Synchrony September 14 exhibit](https://www.sec.gov/Archives/edgar/data/1601712/000160171226000037/creditstatsfinancialtables.htm), [Bread September 15 release](https://investor.breadfinancial.com/node/30721/pdf). These issuer portfolios differ; monthly rates are not seasonally adjusted household measures. Synchrony warns recovery timing and charge-off cycles affect monthly comparisons. No CRL-20/21 resolution follows from a monthly release. Bread was readable through web during research; later re-open and direct download failed, so no local PDF receipt is claimed.

## Fuel and credit pricing

[AAA September 16](https://gasprices.aaa.com/): regular **$4.3672/gal**, +14.27¢ week-over-week; diesel **$6.3103**, +36.79¢, AAA's recorded high. Regular remains **13.28¢ below $4.50**. The sustained clock is not satisfied; CRL-08 stays at its carried 7% pending the touch-versus-sustained ruling. A lag-model cutoff is not itself a realized outcome. Do not present September 11 crude as current or revise the registered lag here. HENRY's September 13 correction is integrated: higher airfares can mean airline fare recapture, adverse to HEN-46's margin-compression thesis; CPI is not RASM. WALTER's September 14 “diesel futures fell 7%” headline was retracted for an October→November contract-roll break; do not use it as physical relief.

September 15 [HY OAS](https://fred.stlouisfed.org/series/BAMLH0A0HYM2) **276bp**, [CCC](https://fred.stlouisfed.org/series/BAMLH0A3HYC) **1,085bp**, [BB](https://fred.stlouisfed.org/series/BAMLH0A1HYBB) **161bp**. Gap **924bp**, ratio **3.93×**. Gap is wider than September 10's915bp, but below September 11's926bp; not a new maximum. Latest day all three widened, while the gap narrowed1bp. Quality bifurcation persists; broad HY calm is not proof of household health.

## The +83% household-card-debt chart fails verification

WALTER's SIG-W-20260915-008 asks whether an unsourced chart ($6,100 in2022 → $11,149 in2025) can be verified. **It cannot on the identified source.** [WalletHub](https://wallethub.com/edu/credit-card-debt-report/127704) in the retained September16 HTML labels **$11,313 for Q2 2026, inflation-adjusted**, with a September8 publication date. **Correction during the key-file audit:** the earlier $11,153/Q1-2026 attribution came from an unretained web rendering and cannot be reproduced from the saved article; it is withdrawn as verified evidence. Article and embedded-array vintages must remain separate. Within the SAME retrieved arrays, Q4-2022→Q4-2025 household debt rose **15.12% nominal** ($9,953.65→$11,458.63), **5.44% inflation-adjusted** ($11,198.57→$11,807.42). Neither establishes the chart's claimed “households carrying a balance” denominator. The $6,100 starting figure remains untraced. Reject this chart as verified CARL evidence; original provenance remains **INDETERMINATE**, not proof that every other household-debt series is false. Preserve these source-vintage distinctions rather than splice near-matching endpoints.

## Next tests and boundaries

- FOMC September16: not released at cutoff. V12 already5; sellside hike votes cannot raise it. Registered easing condition requires two consecutive meetings; a survey is not a meeting. No market-implied probability independently verified here.
- September25 UMich final; September28 Census historical revisions (tentative10am); October15 September retail (8:30am): the next spending observation bearing on September pump pressure. Census release supplies both dates.
- RED's September14 CRL-10 review accepts the reachability arithmetic and retracts its one-sided revision allegation. Full revision-denominator audit remains backlog, not completed here.
- This is a focused news pass, not all228 incoming BOARD items substantively reviewed. Claude doorbell/session tools remain unavailable. Existing approvals, frozen workbooks and other sessions' edits are preserved.
