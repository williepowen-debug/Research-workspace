# L758 — USDA ERS release date and 2027 input-cost attribution

**Read:** 2026-10-27T02:37:39+00:00. **Boot clock:** 2026-10-26 22:35 Monday. **Task:** Will requested verification of the actual release date, then assessment of whether inputs caused the 2027 food-at-home revision. No gate-letter change or trade.

## Verdict

**October 23, 2026 is the supported release day. The 2027 food-at-home forecast fell from 1.8% to 1.0% (-0.8 percentage points). Input-cost causation is NOT ESTABLISHED. L758's upward-revision-citing-inputs signal is NOT FIRING.**

The startup report had promoted a page's Updated stamp into release-date verification without a separate schedule check. That evidence was insufficient. This pass supplies the independent schedule and forecast-vintage evidence; the date value agrees, but its verification basis changes.

## Release-date evidence — distinct from page freshness

| Evidence | Finding | What it establishes |
|---|---|---|
| [USDA agency release calendar, filtered October 19–26](https://www.usda.gov/about-usda/reports-and-data/agency-reports?field_publish_date_value%5Bmin%5D=2026-10-19&field_publish_date_value%5Bmax%5D=2026-10-26) | **Fri, 10/23/2026 → 11:00 am → Food Price Outlook → ERS**. Fetched directly at usda.gov, HTTP 200; snapshot `usda-schedule-oct19-26.html` and text copy | The agency's named scheduled release day and time, independent of ERS's summary-page stamp. The single-day filter returned no report; the weekly range returns the named row. |
| [ERS product page](https://www.ers.usda.gov/data-products/food-price-outlook) — Consumer Price Index, Producer Price Index and Historical Data download cards | Each current forecast file last updated **10/23/2026**; next update **11/24/2026** | Matching published data-file vintage and the next stated release, replacing FERT's November 25 estimate. |
| [ERS October Summary Findings](https://www.ers.usda.gov/data-products/food-price-outlook/summary-findings) | October edition; September 2026 CPI/PPI data; Updated 10/23/2026 | The forecast edition is present, rather than only a scheduled event. |
| [Feed & Grain, dated October 23](https://www.feedandgrain.com/business-markets/commodities/news/15838361/food-price-growth-slows-to-17-in-2027) — opening paragraph | Reports ERS released the October outlook that Friday, with the same 2027 forecast | Contemporaneous secondary corroboration that the scheduled release occurred. Not used instead of reachable USDA evidence. |

Together these establish the release **day**. **11:00 am is the scheduled time; no actual upload timestamp was recovered.** The ERS calendar endpoint still returns Error/No results. That client limitation does not make USDA's separate agency release calendar unreachable; requests with a browser user agent reached the original USDA page, while web.open sometimes returned 403.

## Forecast revision — compare the same horizon

PRIMARY: [ERS Historical CPI forecast series](https://www.ers.usda.gov/media/6464/historical-consumer-price-index-cpi-forecast-series.csv?v=71962); filtered on Consumer Price Index item = **Food at home**, Year of forecast = **2026**, Year being forecast = **2027**, Month of forecast = **9 or 10**. Complete extract: `forecast-vintages-2027.csv`; source bytes and retrieval metadata in `manifest.json`.

| Forecast vintage | Target / measure | Midpoint | 95% interval |
|---|---|---|---|
| September 2026 | 2027 calendar-year-average food-at-home inflation | **1.8%** | **-5.0% to 9.2%** |
| October 2026 | Same target and measure | **1.0%** | **-5.2% to 7.5%** |
| Change | October minus September, same series | **-0.8 percentage points** | Not a causal decomposition |

The current CPI CSV independently matches October's midpoint and bounds. This is neither September's observed 1.8% year-over-year inflation nor a forecast of one month's inflation.

## Did inputs cause the change?

**No published attribution establishes that.** The [October summary](https://www.ers.usda.gov/data-products/food-price-outlook/summary-findings), forecast-method paragraph, states that forecasts are statistical models fitted to recent data trends. [ERS documentation](https://www.ers.usda.gov/data-products/food-price-outlook/documentation), current methodology and Background sections, describes category-specific time-series forecasts using BLS indexes. Price data are model inputs; that is not evidence of fertilizer, fuel or other production-cost pass-through.

The read October summary contains no fertilizer, input-cost, energy-cost or fuel explanation. Its economic discussion names cattle supply, avian influenza/egg recovery, milk output and wheat output. Those mostly explain observed category prices and 2026 forecasts; **they do not quantify the causes of the 2027 aggregate forecast revision**. It would overstate the evidence to say that lower fertilizer costs, cheaper energy, or egg/milk supply caused the entire -0.8 point revision.

Historical-table context, all **2027** forecasts, September → October: beef/veal **4.7% → 2.4%**, dairy **1.5% → -0.6%**, cereals/bakery **2.4% → 0.7%**, eggs **0.8% → -0.8%**. These are parallel forecast revisions, **not weighted contributions or a causal explanation of the aggregate**. No model rerun or causal coefficient was produced.

**L758 test:** upward revision to 2027 food-at-home **AND** cited input costs. Direction is down; input attribution is absent. Neither condition is satisfied. **NOT FIRING** means this edition supplies no confirmation of the fertilizer-to-food channel; it does not prove input costs have zero economic effect or close the broader transmission question.

## Owner record and handoff

T2 next check corrected to **2026-11-24**, the ERS product page's stated next update. KB-FERT-088 records the release evidence; KB-FERT-089 records the vintage comparison and attribution limit. KB-FERT-083 retains the unchanged October forecast values and points to this stronger verification. STATUS/VX/FLOW updated without changing state or score. Dated packet asks PROME to strengthen L758's receipt and replace its next-date estimate; FERT does not edit PROME's docket.

Git sync remains deferred under the dirty-owner rule. Exact artifacts are committed locally; recipient notification acceptance and consumption remain separate.

## Validation

Verified the exact USDA calendar row in the saved original-host response; all downloaded snapshot hashes match the manifest. Historical forecast filter gives six aggregate records (two vintage months × midpoint/lower/upper) and the -0.8 pp difference; the current CPI file independently agrees with October 1.0% and its bounds. TSV widths and unique IDs, read-cap and weekday checks passed. Scoped `git diff --check -- AGENTS/FERT` passed; peer-owned whitespace findings from the global check were excluded and left to their owner.

Next-date consumer scans were run across peers and self. Cross matches concerned other events (FDIC, VIX, Deere, etc.), not the ERS release. Own matches included raw diagnostic captures and FERT-12's November 25 prediction window, which is a separate historical contract and remains unchanged. Diagnostics are marked FROZEN; old ERS estimates in dated history are retained with supersession notes. The live T2/STATUS/KB next-check date is November 24. PROME's stale November 25 estimate is explicitly covered by the delivery packet.
