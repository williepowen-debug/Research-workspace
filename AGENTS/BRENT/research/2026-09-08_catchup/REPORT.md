# BRENT catch-up — first implementation pass, September 8, 2026

**Completed:** current thesis/reference reconciliation, BRT-29 threshold provenance and reproducible jet/gasoline comparison. **Advanced:** named-carrier tally, CPC/Jazan event state, overdue catalysts and SPR primary-source review. Remaining evidence gaps are explicit below; no final prediction, probability, trade rule or broker receipt changed.

## A01 / A10 — current readers replaced

THESIS now gives the v5.8 interpretation and dated forecast, with current quantities/positions at their canonical owners. June draw pace, Cushing-at-floor, contango, retired deployment tiers, XLE LAPSE and stale OPEN prediction states no longer sit in its current reader paths. Reference tables now separate stable arithmetic from operational estimates requiring a date and source. Neither cleanup produces fresh capacity, quota, breakeven or price estimates. Complete originals are in [the hashed archive](../../archive/2026-09-08_thesis-reconciliation/manifest.json).

The v5.8 frame and September 2 probabilities are retained as dated assessments. Its mid-November SPR calculation is demoted to conditional arithmetic, not a verified deadline. WQ-189/192 remain STAND DOWN; complete trade readers govern decisions.

## A02 — BRT-29 registration provenance

First registration: commit `995a35bdfcc62d6ac24833af0a09d01af2c502b1`, July 21 at 23:44:24 ET. Both the Prediction's `≤−3.0%` and Invalidation's `never ≤−1.5%` appeared then and persist through all eight row-history revisions inspected. [Saved history](brt29-registration-history.json). This is not migration damage.

**Logical reconciliation:** the invalidation gives a sufficient failure condition; it does not state that reaching −1.5% passes T. A path never reaching −1.5% also cannot reach −3.0%. Therefore the two numeric clauses are compatible, despite the audit's earlier description of them as a conflict. Reaching −2.0% can avoid that particular failure condition while still missing the explicit T requirement. Reaching −3.0% alone still does not settle M or price-collapse contamination.

| Hypothetical path (not an observation or grade) | Numeric interpretation |
|---|---|
| Best qualifying reading −1.0% | Meets the explicit sufficient-failure condition if premise holds; canonical text calls mechanism and threshold failed. |
| Best qualifying reading −2.0% | T not met; absence of the −1.5% invalidation is not a pass. Grade M on its own evidence. |
| Qualifying reading −3.1% | T magnitude met; still check registered week, causal contamination and M. |

No field or threshold is rewritten. The week-ending September 25 boundary for T and September 30 final boundary remain. Other ambiguities are not solved by this logic: the word “during” supplies no duration/count for jet leadership, and named cuts require event eligibility rather than aggregate capacity evidence. The mandatory prediction note now carries this reconciliation and the remaining evidence result.

## A03 — jet/gasoline comparison and carrier tally

EIA primary workbooks [gasoline](https://www.eia.gov/dnav/pet/hist_xls/WGFUPUS2w.xls) and [jet](https://www.eia.gov/dnav/pet/hist_xls/WKJUPUS2w.xls), retrieved September 8, latest observation August 28. Each series is weekly product supplied in thousand barrels/day. Four-week means are compared with the four corresponding weeks 364 days earlier. Saved workbooks, [calculation](reproduce_eia.py), [CSV](brt29-eia-comparison.csv) and [validation](eia-validation.json) make the result reproducible. This is one EIA measurement lineage, not two independent witnesses; retrieved historical data may include revisions.

| Week ending | Gasoline 4wk YoY % | Jet 4wk YoY % | Jet below gasoline? |
|---|---:|---:|---|
| July 17 — pre-registration context | +1.452 | +9.127 | No |
| July 24 | −0.252 | +5.800 | No |
| July 31 | +0.603 | +3.602 | No |
| August 7 | −0.487 | +3.776 | No |
| August 14 | −0.858 | −6.298 | Yes |
| August 21 | −1.094 | −2.318 | Yes |
| August 28 | −1.605 | −0.559 | No |

**Observed result:** jet leads in two of six post-registration survey weeks and two of the three mid-August onward weeks; not in the final week. LESSONS #9 excludes treating early shock weeks as clean demand evidence. Thus intermittent leadership is observed; continuous or end-window leadership is not. No retrospective “any week” or “all weeks” rule is imposed on “during.” August 28 was the last in-window survey week; the September 4 survey is outside the August mechanism window even though its publication is delayed.

The carrier leg requires at least three additional named carriers, beyond Virgin Atlantic July 15/Aer Lingus July 16, announcing capacity cuts citing fuel/war economics by August 31. The existing August 21 note requires announcements after that baseline. Registration time is recorded separately; no extra start-date restriction is imposed here. A reduction versus prior schedule can coexist with positive YoY growth, but a YoY number alone does not prove a new cut or its cause. Parent-group announcements are not multiplied into subsidiary carriers.

| Primary announcement inspected | Date | What it establishes | Tally disposition |
|---|---|---|---|
| [United results, SEC](https://www.sec.gov/Archives/edgar/data/100517/000010051726000135/ual_erx06302026xex992.htm) | July 15 | Capacity/fuel commentary predates the named baseline. | Excluded by date; publication-index freshness is irrelevant. |
| [Alaska results](https://news.alaskaair.com/company/alaska-air-group-reports-second-quarter-2026-results/) | July 21 | Q3 capacity growth 2–3%, North America roughly flat, high fuel costs. | No distinct new fuel-caused cut established by this release. |
| [Southwest 8-K](https://investors.southwest.com/sec-filings/all-sec-filings/content/0000092380-26-000074/0000092380-26-000074.pdf) | July 22 | FY capacity growth forecast reduced from 2% to about 1.5%; Q3 −1% to flat. | Candidate: reduction confirmed; explicit attribution of this cut to fuel/war economics still needed. Fuel-cost and cut paragraphs alone are not the causal statement. |
| [JetBlue investor update, SEC](https://www.sec.gov/Archives/edgar/data/1158463/000115846326000076/ex992-investorupdateq22026.htm) | July 28 | Q3 growth 3–6%, FY 1.5–3.5%, with fuel assumptions. | No distinct new fuel-caused cut established here. |
| [Air France-KLM issuer release](https://www.globenewswire.com/news-release/2026/07/30/3335784/0/en/Air-France-KLM-Q2-2026-Results.html) | July 30 | FY group outlook narrows from +2–4% to +2–3%; network/Transavia revisions; fuel mitigation also includes surcharges and reallocations. | Candidate group; explicit cause and carrier attribution incomplete. Not automatically Air France + KLM + Transavia. |
| [IAG H1 issuer report via RNS](https://www.rns-pdf.londonstockexchange.com/rns/6982O_1-2026-7-31.pdf) | July 31 | Fuel pressure and capacity outlook; historical subsidiary results are not new cuts. | Candidate group; distinct qualifying named-carrier events still unproved. Aer Lingus remains baseline-excluded. |
| [Lufthansa Group results](https://newsroom.lufthansagroup.com/en/lufthansa-group-benefits-from-strong-demand-for-air-travel-and-achieves-an-operating-profit-of-383-million-euros-despite-significantly-higher-fuel-costs/) | August 4 | FY capacity expected flat; Q2 network declines include strikes and CityLine changes; Eurowings mixes Gulf suspensions and replacement routes. | Candidate; do not count prior April decisions or airspace suspensions as new fuel-economic cuts. |
| [Air New Zealand results](https://www.airnewzealandnewsroom.com/press-release-2026-air-new-zealand-announces-2026-annual-results) | August 28 | Explicit fuel-related capacity response, but financial-year history and general continuation language. | Candidate; no separately dated new cut established. A fresh publication of prior reductions is not a new event. |

**Bounded tally result: three qualifying carrier events are not yet established.** This is an eight-release evidence audit, not an exhaustive worldwide zero-event finding. Five candidate entries need the original schedule-change/earnings-call statement or issuer notice. Mechanism remains **unresolved on available evidence**, with its elapsed deadline explicitly carried; neither aggregate OAG seats nor these candidates are silently counted to reach three. Final BRT-29 remains open to September 30, with T still ungraded.

## A05 / A06 — CPC, Jazan and Treasury

**CPC recovery:** S&P Global's August 10 report uses its own Commodities at Sea tracking: loadings averaged 1.41 mbpd in the week from August 3, versus 1.16 mbpd July 28–August 2 and 0.163 mbpd July 21–27; YTD averaged 1.43 mbpd. This is primary tracker evidence that loading resumed, not owner certification of every buoy or September operations. [S&P source](https://www.spglobal.com/energy/en/news-research/latest-news/crude-oil/081026-cpc-crude-loadings-recover-as-high-tanker-rates-entice-shipowners).

RF-038 changes to PARTIAL_RESTART on that dated evidence. Its current outage estimate becomes UNKNOWN rather than continuing to advertise July's 1.3 mbpd loss; the exact old quantities survive in its note and the archived row. `last_verified` uses the explicit August 3 observation-period start, conservatively; report publication is August 10, retrieval September 8. Neither is laundered into a September operating observation. RF-042's July 30 SPM-3 re-halt remains a separate historical event: terminal-total loadings cannot prove that specific buoy repaired/reopened or independently measure an incremental outage. It is not counted twice.

**CPC August 17 understanding:** marked unresolved historical review. Source attribution, cargo origin/sanctions and event coverage remain necessary; recovery through early August does not prove no breach through August 17. The stored SKIROS cargo-origin correction survives. No pass from absence of logged strikes; no transfer of this agreement to Hormuz.

**Jazan:** the August 10 [Reuters report of IIR's note](https://www.boursorama.com/bourse/actualites-amp/saudi-aramco-reporte-au-30-aout-la-remise-en-service-de-la-raffinerie-de-jazan-selon-une-note-d-iir-f6b33fe86a72fcac1ba5b9c1427eae80) revises the estimate to August 30. It is not an Aramco promise or an actual restart. Searches of Aramco publications and dated restart reporting in this pass did not establish post-August 30 unit state. RF-039's note is reconciled to that missed verification date without restamping its old operating evidence. RF-044 retains ZERO-NODOUBLECOUNT; that zero does not establish undamaged or restored capacity. The catalyst now says restart UNRESOLVED. An unverified newer secondary assertion was not promoted to a primary restart/slip confirmation. Earlier eleven incident gaps and Port Arthur are not resolved by this targeted pass.

**Treasury August 24:** official Bessent remarks identify **Operation Economic Outcast**, announce five sectoral determinations and more than 60 designated entities/individuals/vessels, and describe pressure on countries hosting Bank Melli. This resolves what was announced and corrects the operation name. The statement alone does not authenticate all operative instruments, buyer/STS scope, effective dates or realized loss of oil flow. Docket status becomes **announcement observed / mechanism review partial**, preserving its registered requirement to grade published mechanisms rather than the conference alone. [Treasury primary](https://home.treasury.gov/news/press-releases/sb0614). No old Iranian loading estimate is refreshed, and the earlier “largely symbolic” assessment is not re-certified.

## A13 — SPR primary-source review

[DOE March 11](https://www.energy.gov/articles/united-states-release-172-million-barrels-oil-strategic-petroleum-reserve) announced 172 million barrels beginning the following week, with approximately 120 days to deliver at planned discharge rates. This was a plan, not proof of completed deliveries or a later fixed August cutoff.

[DOE April 9](https://www.energy.gov/hgeo/opr/articles/energy-department-continues-initiating-strategic-petroleum-reserve-emergency) explicitly describes emergency exchanges and premium-barrel returns by the following year for that solicitation. [DOE June 10](https://www.energy.gov/hgeo/opr/articles/energy-department-issues-rfp-advance-president-trumps-172-million-barrel) solicits up to 40 million barrels and attributes a 26% return premium to **earlier exchanges**. It does not state a 26% final award term for the new June tranche. Neither supports a universal 1.18–1.24 multiplier. Do not add overlapping solicitation ceilings or mix delivery and repayment dates.

The [linked SPR solicitation index](https://www.spr.doe.gov/doeec/ActiveDocs.htm?type=exchange) returned navigation without a usable contract attachment in the web retrieval. The exact contract delivery timetable and amendments therefore remain unrecovered; there is no claim that DOE publishes no 2026 records or that the documents do not exist.

The [official 2023 US Code edition, §6241](https://www.govinfo.gov/content/pkg/USCODE-2023-title42/pdf/USCODE-2023-title42-chap77-subchapI-partB-sec6241.pdf), places 252.4 million barrels specifically under subsection (h)(2), limited drawdown, separately from subsection (d)'s emergency provisions. This proves the scope of that edition, not current-law completeness or the precise authority of every 2026 contract. Current-edition web retrieval did not succeed. It does not establish a universal inventory floor or a physical depletion limit. Existing September 4/11 observations and numerical bands remain unchanged; the first week spans August, and arithmetic on those prints cannot prove a contract deadline without the contract.

## Remaining priorities / next concrete reads

| Audit | State after this pass | Next required evidence/action |
|---|---|---|
| A01 | Completed current-reader reconciliation | Maintain canonical pointers; no historical state reintroduced. |
| A02 | Numeric logic/provenance reconciled | Read full letter at final scoring; no −1.5% shortcut. |
| A03 | Partial: weekly comparison complete, carrier evidence unresolved | Recover explicit announcements for the five candidates; preserve August deadline and source dates. |
| A04 | Open measurement gap | Original matched futures crack history over Q2–Q3 plus upstream E&P OAS/refiner-stress evidence. FRED search recovered broad HY, not the needed upstream series. No proxy grade or neither-event inference. |
| A05 | Partial, targeted four-row review | CPC unit-level follow-up; Aramco/IIR dated Jazan restart state; remaining eleven plus Port Arthur. |
| A06 | Three old rows dispositioned, all retain unresolved limbs | CPC coverage/provenance; operative OFAC documents/flow effects; Jazan actual restart. None pruned as fully graded. |
| A07 | Calendar repaired in prior audit; release pending | September 9 fuel ~10:00 ET and STEO noon–12:15 ET, from official issue. |
| A08 | Open, not newly solved | Vortexa weekly Sidi; Russian official instruments, product flow windows and floating-stock update. No crude/product or monthly/weekly substitutions. |
| A09 | Owner dependency | TERRY/Will live broker check and selected September 9 XLE exit receipt; no execution inferred. |
| A10 | Completed reference-reader reconciliation | Re-source any numerical estimate before reuse. |
| A11 | Schedule gap identified, owner reads queued | September 10 noon WPSR; September 11 post-15:30 COT. Remote scheduler not changed. |
| A12 | Completed correction of local access claims | Required PortWatch observations and current freight/premium quotes still absent. |
| A13 | Partial: primary program and statutory scope recovered | Exact delivery contract/amendments, current authority, and existing two-print interpretation remain unresolved. |

No cross-agent files edited or external messages sent. Frozen ledgers, registered letters, trade specs and probabilities are preserved. Validation and closeout results are recorded in validation.json in this directory.
