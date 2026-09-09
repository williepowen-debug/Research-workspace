# BRENT — Reference definitions and source map

**Reconciled September 8, 2026.** This replaces the March tables as a current reader. Their full historical values and source descriptions are preserved in [the before-image](../archive/2026-09-08_thesis-reconciliation/domain/REFERENCE_TABLES.md), verified by [manifest](../archive/2026-09-08_thesis-reconciliation/manifest.json). None of those estimates becomes current merely because this file was edited.

## Stable arithmetic and definitions

| Item | Definition / restriction |
|---|---|
| Petroleum volume | 1 US petroleum barrel = 42 US gallons. Convert a product quote in dollars/gallon before subtracting crude dollars/barrel. |
| Simple product crack | `42 × product price ($/gal) − crude price ($/bbl)`. Name both series, location, maturity, date and price type. |
| 3-2-1 gross crack | `(2 × 42 × gasoline + 42 × distillate − 3 × crude) / 3`, per barrel of crude input. A modeled gross margin, not a refinery's realized net profit. |
| Four-week product-supplied YoY | Four-week average versus the comparable prior-year four-week average, then percentage change. Pair EIA weekly dates explicitly; do not substitute a single week's change or a percent-of-capacity measure. |
| Flow versus stock | bpd/mbpd measure rate; barrels/million barrels measure inventory. Neither a tanker count nor dwt directly measures barrels delivered. |
| Capacity versus loss | Design/nameplate capacity, currently usable capacity, observed throughput and event-attributed outage are distinct. Repeat strikes are not additive. |

Arithmetic is stable; prices, survey inputs, operating capacities and seasonality are not. BRT-29's current calculation and exact comparison dates are in [the catch-up evidence](../research/2026-09-08_catchup/REPORT.md). Crack construction must also satisfy the specific registered test; these formulas do not authorize a new proxy or threshold.

## Measures that require a source vintage

| Measure | Required source and basis | Current reader / unresolved issue |
|---|---|---|
| Hormuz throughput | Named tracker, cargo/vessel perimeter, observation window, coverage and denominator | [Transit baseline](HORMUZ_TRANSIT_BASELINE.md); [owner evidence](../setups/2026-09-08_market-docket-owner-read.md). Retired daily-count thresholds remain retired. |
| Gulf storage/runway | Facility/country stock, usable capacity, net inflow and observation date | March “days left” are historical. No current Gulf runway is established by the old table. |
| OPEC spare capacity | Issue date, member set, sustainable response horizon, definition and deliverability | [STATUS](../STATUS.md). March OPEC+ and August EIA effective OPEC are different perimeters. September STEO scheduled September 9 requires a fresh same-definition read. |
| OPEC quotas | Official decision, effective production month, member commitments and compensation | [CATALYSTS](../docket/CATALYSTS.tsv). A quota change is not a measured supply change. |
| Petroline / ADCOP / Kirkuk-Ceyhan | Operator capacity by product, terminal constraints, domestic offtake, actual loading data and date | Historical design figures are not current operating ceilings. The March “combined realistic max” and ADCOP impaired-state table are withdrawn from current use; later operating evidence is in the incident ledger and THESIS. No new unsourced replacement ceiling. |
| US production, rigs, DUCs | EIA series/issue and Baker Hughes dated oil count, not total rigs | [TRACKER](../demand_destruction/TRACKER.md) and PREDICTIONS BRT-26; weekly estimates, monthly actuals and forecasts must remain separate. |
| Shale breakevens | Survey/operator date, basin, existing-well versus new-well economics and cost assumptions | March ranges are unrefreshed estimates, not constants. Do not infer current capex merely from price above a carried breakeven. |
| Crack percentiles | Matched spread history, frequency, sample window and construction | March percentile/“record” labels are not maintained. BRT-12 requires the original ordering evidence; HO or refiner equity alone does not supply it. |
| Pump transmission | Wholesale/retail dates, taxes, distribution, pass-through lag and regime | Old March scenarios and a psychological round number do not establish a current causal threshold. BRT-29's registered letter governs. |
| Freight / war-risk | Named route, ship size, quote date, WS benchmark-year or dollar basis and policy terms | No current quote obtained. JWC listing verification is not rate verification; retired Worldscale tripwires are not reinstated. |
| LNG | Hub, currency, energy unit, delivery month and regional fundamentals | March JKM/TTF/HH and marketing-share figures are historical. Capacity outage is not a fixed price premium. |
| Energy credit | Index/company universe, OAS methodology, maturity, observation date and primary series | March sector-OAS values are unverified carry. Broad HY, energy-sector HY and upstream E&P OAS are not interchangeable. |
| Refinery facts | Operator/site/unit, nameplate versus throughput, event attribution and dated restart evidence | [INCIDENTS](../refinery_damage/INCIDENTS.tsv) is an event record, never a summable capacity table. Old Kirishi exclusivity and export-share claims remain unverified historical assertions. |
| SPR | Actual balances, delivery versus return schedule, legal authority and physical limits | No universal legal floor or operational deadline is certified by the old table. See [SPR source review](../research/2026-09-08_catchup/REPORT.md). |

## Where current state belongs

[STATUS](../STATUS.md) owns dated market/physical state; [REGISTRY](../workbook/REGISTRY.tsv) owns registered instruments and numeric letters; [THESIS](../thesis/THESIS.md) owns interpretation; [TRADE](../TRADE.md) and its complete specs own position/action rules. Source access, freshness and inference are separate checks. An old estimate retained for context must carry its original vintage and uncertainty.
