# BRENT — September 9 approved review, before STEO publication

The strongest new evidence is a broad diesel-price increase alongside divergent product margins. It supports continued fuel-cost pressure, but does not measure a new aggregate loss of oil supply. Existing v5.8 calibration and WQ-189/192 STAND DOWN remain unchanged.

**Completed:** position reconciliation to available owner/broker mirrors, delayed option quotes, EIA retail validation, regional and refinery/terminal review, August STEO baseline, WPSR worksheet, and bounded airline/credit follow-up. **Pending:** XLE execution receipt; September STEO after publication; September 10 WPSR. At the 10:36 ET primary capture, STEO still showed its August 11 issue. Preparation is complete; future releases have not been graded.

## 1. Positions and existing instructions

BRENT's 35-share USO record was stale. The [September 3 broker transcription](../../../../PROME/data/2026-09-03_broker-capture-TRANSCRIPTION.md) shows **37 shares**, as does the [September 9 screenshot review](../../../../PROME/research/2026-09-09-xle-decision/README.md). This is a correction to BRENT's mirror, not a purchase today or a direct broker session. The Robinhood spread is absent from that Fidelity view; that absence establishes neither closure nor current ownership.

Read the complete [trade rules](../../setups/SPECS_TRADE_RULES.md), [USO owner card](../../../TERRY/setups/USO-135C_rule20-management_2026-09-01.md), and [XLE exit card](../../../TERRY/setups/XLE65C_approved-exit-tracking_2026-09-08.md). PROME records Will's intention to sell XLE; neither intention nor a position screenshot proves execution. Receipt remains pending. The earlier USO call-sale price remains permanently UNKNOWN and was not requested.

| Contract | Bid / ask | Midpoint | Last trade time, ET | Capture, ET |
|---|---:|---:|---|---|
| USO October 16 135C | 16.40 / 17.05 | 16.725 | 10:06 | 10:26:57 |
| USO September 18 150C | 3.50 / 3.70 | 3.600 | 10:06 | 10:26:59 |
| USO September 18 165C | 0.59 / 0.69 | 0.640 | 10:11 | 10:26:59 |
| XLE September 30 65C | 1.66 / 1.85 | 1.755 | 09:59 | 10:27:01 |

These are delayed Yahoo-chain observations, not executable broker quotes. Raw source metadata and selected rows are preserved. Existing chain checks found each requested strike with no defective-leg flags. [Cboe's delayed USO feed](https://cdn.cboe.com/api/global/delayed_quotes/options/USO.json) matched those USO bid/asks; its [XLE feed](https://cdn.cboe.com/api/global/delayed_quotes/options/XLE.json) showed 1.67/1.85. Cboe root snapshots read 14:26:12 and 14:26:13 without timezone labels; contract last-trade timestamps differ. Agreement across vendors is not proof of independent underlying measurements or synchronized execution.

The remaining October call has an indicative $1,640 bid value / $1,672.50 midpoint per contract. The September spread's leg-based liquidation indication is `(3.50−0.69)×100 = $281`; midpoint $296. This is not a quoted package market. No sleeve total or realized P/L is certified from incomplete holdings and asynchronous observations.

**Existing rules remain:** the September 8 XLE close selected sale of both calls at the September 9 open; a rebound does not cancel that instruction. Will must check current holdings/orders before execution. USO's remaining October call has no second 14.25 profit target; the official-close-below-135 rule and unconditional October 9 before-close stop survive, with no roll. The September spread remains HOLD through expiry. Share-risk scaffolding remains unratified. Current quotes do not create a new instruction. These structural states are written to [TRADE](../../TRADE.md); TERRY still needs the XLE fill quantity, price, time/account and remaining disposition.

## 2. Fuel: what is established and what is inference

The September 9 EIA release reports the **September 7 observation**, not a September 9 pump survey. Regular all-formulations gasoline and on-highway diesel agree between the HTML and full-history workbooks. National gasoline is **$4.157/gal**, up **8.6¢ / 2.11%** from August 31; diesel **$5.967**, up **36.8¢ / 6.57%**. Their retail price difference widened by 28.2¢ to $1.810/gal. These prices include taxes; the difference is not a refinery crack. [EIA retail release](https://www.eia.gov/petroleum/gasdiesel/)

| Region | Gasoline, $/gal | Weekly change, ¢ | Diesel, $/gal | Weekly change, ¢ |
|---|---:|---:|---:|---:|
| East Coast | 4.031 | +9.4 | 5.744 | +29.6 |
| Midwest | 3.894 | +4.7 | 5.946 | +37.5 |
| Gulf Coast | 3.685 | +6.7 | 5.754 | +39.4 |
| Rockies | 4.314 | +4.8 | 5.805 | +25.0 |
| West Coast | 5.362 | +15.6 | 6.987 | +49.0 |

Source: EIA [gasoline history](https://www.eia.gov/petroleum/gasdiesel/xls/pswrgvwall.xls), Data 3, `EMM_EPMR_PTE_*_DPG`; [diesel history](https://www.eia.gov/petroleum/gasdiesel/xls/psw18vwall.xls), Data 1, `EMD_EPD2D_PTE_*_DPG`. The parser matches series keys and the two observation dates; it does not confuse gasoline grades. All five regions increased. National distribution does not identify the fraction attributable to any refinery or exclude transmission from Gulf disruption.

The earlier [09:58 market capture](../2026-09-09_morning/REPORT.md) gives **matched November** indicative ULSD−WTI **$97.9358/bbl**, up **$2.5068**, while RBOB−WTI was **$35.2844**, down **$3.2682** against September 8 vendor daily bars. November WTI−Brent was −$8.14. Calculation: product dollars/gallon ×42 less same-month crude dollars/barrel. Leg timestamps and vendor-close limitations remain in that capture. These are theoretical futures margins, not cash assessments or realized refining profits. The diesel/gasoline divergence supports a product-specific pressure interpretation; this morning's futures cannot causally explain the earlier retail survey.

| Evidence | Established | Limit / implication |
|---|---|---|
| Valero Port Arthur, March incident | Valero's Q2 10-Q says normal refinery throughput returned during Q2, while repair/replacement work continued. | The old full-refinery loss cannot be carried into September. Normal throughput does not prove every distillate unit recovered. [SEC, Note 5](https://www.sec.gov/Archives/edgar/data/1035002/000162828026050937/vlo-20260630.htm). Existing RF-008 already contains this source; no new incident update. |
| Port Arthur storm disruption, September 1 | September 2 Reuters reporting described a partial blackout, smaller AVU-147 shut and larger AVU-146 at minimum runs. | Reported unit state, not verified September 9 state; no full-site capacity loss or restart date adopted. [Dated Reuters relay](https://energynews.oedigital.com/oil-refineries/2026/09/02/sources-say-that-valero-port-arthur-refinery-is-affected-by-a-power-outage-after-the-storm-edouard). |
| Sabine/Neches access | Moran's September 2 bulletin reported outbound movements restarted and inbound movements expected later that day; recovery conditions remained. | Counters an assumption of continuous port closure. Port access does not certify refinery restoration or a cleared queue. [Moran primary bulletin](https://www.moranshipping.com/news/bulletins/port-update-port-arthur-tx-slash-sabine-slash-neches-2026-09-02). |
| NORSI, August 26 | Reuters industry sources reported a processing halt after an attack. | No new operator-confirmed September 9 throughput or repair completion recovered. Nameplate capacity is not a present lost-volume estimate. [Dated Reuters relay](https://logistics.maritimeprofessional.com/transportation/2026/08/26/sources-say-that-russias-norsi-oil-refinery-has-halted-oil-processing-following-a-drone-attack). |
| Southern Saudi attacks, September 8 | Ministry-attributed reporting describes fires and some operational interruptions. | Named facilities, affected output and duration remain unspecified in the reporting read. No inferred Jazan-refinery loss. These attacks postdate the September 7 retail observation. [Saudi Gazette report](https://saudigazette.com.sa/article/664398/saudi-arabia/saudi-energy-facilities-targeted-in-southern-region-fires-halt-some-operations). |

**Judgment:** refinery/logistics constraints are a plausible contributor to the product pressure; quantified current losses and causal shares remain unestablished. Refinery outages can reduce crude demand and free crude for export while reducing product supply. Therefore recovering crude exports alone would not settle the diesel question. No new incident or summed outage figure is entered from these relays. September 8–9 attacks belong in the forward risk assessment, not the explanation of September 7 pump prices.

## 3. September STEO comparison is prepared, release pending

The saved primary publication check at **10:36 ET** still says August 11, forecast completed August 6, next release September 9. Normal release window is **noon–12:15 ET**. [EIA release schedule](https://www.eia.gov/outlooks/steo/release_schedule.php)

The [August workbook](https://www.eia.gov/outlooks/steo/archives/aug26_base.xlsx) is preserved with a SHA-256 receipt. [Extracted monthly and quarterly baseline](august-steo-baseline.json):

| August-vintage series | 2026 Q3 | 2026 Q4 | 2027 Q1 | 2027 Q2 |
|---|---:|---:|---:|---:|
| World liquid-fuel production, mb/d | 99.6651 | 103.6613 | 107.3306 | 109.5606 |
| World consumption, mb/d | 103.5105 | 104.2870 | 103.5330 | 104.9728 |
| World net inventory withdrawal, mb/d; positive = draw | 3.8454 | 0.6257 | −3.7976 | −4.5878 |
| OECD commercial inventory, quarter-end million barrels | 2527.2544 | 2476.9002 | 2563.3893 | 2688.1409 |
| OPEC+ liquid-fuel production, mb/d | 33.1284 | 35.8550 | 38.7114 | 39.7544 |
| OPEC surplus crude capacity `cops_opec`, mb/d | 0.020 | 0.020 | 0.030 | 2.380 |
| Middle East subset `cops_opec_r05`, mb/d | 0.000 | 0.000 | 0.000 | 2.350 |

Flows/capacity use simple monthly means, matching the existing [vintage ladder](../../setups/2026-08-13_STEO-vintage-ladder-P1.md); they are not claimed as EIA's day-weighted published quarterly cells. Stocks use September/December/March/June endpoints. Production and consumption balance to inventory withdrawals at each saved month. OPEC+ production is a broader liquid-fuel series than OPEC surplus crude capacity; they must not be subtracted to infer unused quota.

**Question to resolve:** August projected Q3→Q4 world supply rising about **4.00 mb/d**, consumption about **0.78 mb/d**, reducing the implied draw by about **3.22 mb/d**. Does September defer that recovery, reduce its size, change demand, or preserve it? Compare the same IDs/months, then read the narrative's shipping, production and recovery assumptions. Report absolute revisions and their contribution to balance changes. Separate forecast revision from observed delivery. Near-zero effective spare capacity is not permission to treat announced quota as available supply.

On publication: save the September issue, forecast-completion date and workbook in a new directory; check units/definitions; run the same extraction and verify monthly balance identities. Compare Q3/Q4 and the Q1→Q2 2027 recovery boundary before considering any thesis revision. No September value or verdict is filled in prematurely.

## 4. WPSR worksheet — first storm-period observation tomorrow

EIA confirms **Thursday September 10, noon ET**, for week ending September 4. The current WPSR homepage also lists a later **2 p.m. ET** release batch. Confirm each file's observation date; do not combine an updated table 1 with a stale table 2. [Holiday schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php), [release homepage](https://www.eia.gov/petroleum/supply/weekly/).

| Measure | August 28 baseline | September 4 read |
|---|---:|---|
| Commercial crude ex-SPR | 424.460M; weekly −4.450M | Level/change, separate from SPR |
| SPR | 286.604M; weekly −3.122M | First of named September 4/11 observations |
| Cushing | 22.508M; weekly +0.080M | Existing <20.0M line; no new threshold |
| US utilization | 98.0% | Change in percentage points and affected region |
| PADD 3 gross / crude inputs | 9.662 / 9.600 mb/d | Keep gross and crude definitions separate |
| Gasoline stocks | 205.669M; weekly −1.173M | Inventories with production/import/export context |
| Distillate stocks | 104.187M; weekly +0.796M | Same components; a draw alone does not establish outage cause |
| Jet stocks | 45.874M; weekly +0.180M | Product availability and demand separately |
| Four-week gasoline supplied | 8.905 mb/d vs 9.050 year earlier; published −1.6% | Reproduce existing paired 52-week comparison |
| Four-week jet supplied | 1.780 mb/d vs 1.790; published −0.6% | Same ending weeks; no mismatched YoY windows |
| Four-week distillate supplied | 3.660 mb/d vs 3.894; published −6.0% | Counterevidence to a simple demand-boom explanation |

Sources: saved [table 1](wpsr-table1.csv), [table 2](wpsr-table2.csv), [table 9](wpsr-table9.csv); original EIA URLs and hashes in [baseline manifest](baseline-fetch-manifest.json). Published changes can differ slightly from subtracting rounded displayed levels. Table 9 Cushing and table 1 national crude/SPR are separate rows.

Reuse [paired EIA reproducer](../2026-09-08_catchup/reproduce_eia.py): four contiguous weekly observations, matched 364-day comparison, no forward filling; use direct xlrd or a compatible environment for .xls. Gasoline T remains ≤−3.0% by the named September 25 observation. The September 7 retail print does not extend BRT-29's already-completed six-print premise window.

For SPR, save `Δ1 = SPR(Sep4) − 286.604` and `Δ2 = SPR(Sep11) − SPR(Sep4)`; assess their mean only after both releases. Frozen bands remain ≥−2.0M/week, ≤−4.0M/week and strictly between as NO-VERDICT. The existing named-week versus “entirely in September” wording conflict and unverified contract delivery-window premise survive. The arithmetic cannot authenticate that premise. No two-print verdict tomorrow.

The physical countercase remains visible: the last available week had a Cushing build, a distillate build and weaker distillate product supplied. It predates Edouard. Compare the new data against this baseline without attributing every change to the storm; maintenance, imports/exports, demand and measurement noise can also move the rows.

## 5. Bounded airline and historical-credit dispositions

Read BRT-29's complete row and mandatory note. Added two candidate checks to the earlier eight-release/five-candidate review:

- **Ryanair:** its issuer site dates the fuel-linked 216M→214M FY27 traffic reduction to **September 2**, after the August 31 M deadline. July 20 results still forecast 216M. This is useful subsequent transmission evidence, not an in-window event. [Issuer news](https://corporate.ryanair.com/?market=at), [July 20 results](https://investor.ryanair.com/wp-content/uploads/2026/07/Q1-FY27-Ryanair-Results.pdf).
- **Norse:** August 7's primary release explicitly links reduced July capacity to high fuel costs, but describes continuing reductions; the July 8 release already describes fuel-linked reductions in June. August 7 also discusses possible capacity additions. July 31's separate aircraft-redelivery announcement concerns the IndiGo ACMI agreement and does not establish a new own-network fuel cut. A distinct eligible post-baseline cut remains unestablished. [August 7](https://news.cision.com/norse-atlantic-airways-as/r/norse-atlantic-asa--record-unit-revenue-in-july-on-the-back-of-strong-demand,c4380887), [July 8](https://news.cision.com/norse-atlantic-airways-as/r/norse-atlantic-asa--all-time-high-unit-revenue-in-june,c4372208), [July 31](https://news.cision.com/norse-atlantic-airways-as/r/norse-atlantic-asa--operational-and-strategic-update,c4379131).

The AF-KLM group-level event remains supported; three additional eligible named carriers remain **NOT ESTABLISHED by this bounded review**, not proven zero. M stays explicitly unresolved; no premature final grade or new eligibility rule. Existing jet/gasoline leadership evidence and September 25/30 boundaries remain unchanged.

**BRT-12:** re-examined the archived March credit/crack research and current source gap. No recoverable original matched-contract construction or contemporaneous upstream E&P OAS history was established. Fresh web results largely return broad HY, old industry studies or sector discussion. None substitutes for upstream history. The saved November diagnostic remains diagnostic only; today's opposite gasoline/diesel margin moves reinforce why a generic crack label is insufficient. Next required evidence: original contracts/roll convention and a dated refiner-versus-upstream credit series or issuer record. Without those, no event-ordering grade and no inference that neither signal occurred. Existing September 30 disposition remains binding.

## Reproduction and remaining work

Run `.venv/bin/python3 AGENTS/BRENT/research/2026-09-09_squeeze-review/analyze.py` from the repository root. It reads preserved files offline, verifies retail dates/series, extracts seven STEO series, checks monthly balances, and validates selected quote rows. Both download manifests record retrieval timestamps and failures. Initial guessed WPSR XLS URLs returned 404; the successful CSV URLs were obtained from the primary page. Restricted chain access failed; approved network access succeeded. No secrets or broker access were used.

Priority remains: **XLE receipt → September STEO comparison at publication → September 10 WPSR → unresolved historical attribution/source work.** This pass prepares those releases and records the available evidence. It installs no unattended monitor and claims no future release completion. Findings persist in STATUS, TRADE, runtime TRACKER, catalyst state, prediction note and NEXUS brief; no external packet or trade order sent. [Consumer review](consumer-dispositions.md) preserves historical observations and records the remaining 35-share wording in TERRY's unratified scaffold for its owner.
