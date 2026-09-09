# BRENT batch 2 — September 8, 2026 evening evidence pass

## Result and scope

The five airline candidates have received a second, bounded source review. A fuel-linked Air France-KLM group announcement is supported; three additional eligible named carriers are still not established. Lufthansa's identifiable fleet-cut package predates the window. Air New Zealand's annual-result narrative does not establish a new August decision. These are evidence dispositions, not an early final prediction grade or a claim that a worldwide search found zero events.

BRT-12 now has 124 matched November-contract vendor observations and a reproducible diagnostic. The original futures construction and upstream E&P OAS history remain missing. FRED explicitly rejects the energy-series identifier in the April build plan; the valid broad-HY control works. Scheduled September 9–11 releases remain future work. All research stayed inside BRENT; no external send, trade, confidence, threshold or deadline change.

## BRT-29: announcement review

Read the complete canonical row and [mandatory note](../../thesis/prediction_notes/BRT-29.md). The historical baseline is Virgin Atlantic July 15 / Aer Lingus July 16; registration was July 21. No new July-21-only eligibility floor was imposed. Cuts can be announced before they take effect; future implementation alone is not an exclusion. Parent announcements are not multiplied into subsidiary counts.

| Candidate / announcement | Evidence and source dates | Bounded disposition |
|---|---|---|
| Southwest, July 22 results / July 23 call | Issuer filing lowers annual capacity growth to 1.5% from 2%, with Q3 flat to −1%. Fuel volatility is discussed, but the filing does not explicitly connect that reduction to fuel/war economics. A secondary call transcript also emphasizes network profitability and capacity discipline without establishing that causal link. | New lower guidance verified; required cause not established. Not counted. |
| Air France-KLM, July 30 | Issuer reduces FY growth to 2–3% from 2–4%; network short/medium haul becomes about −1% from stable. Bloomberg's firsthand report attributes European flight removals to fuel costs and pricing pressure and cites the group's media representative on London/Stuttgart/Bristol/Belfast reductions, mainly Q4. | Supported group-level fuel/economics announcement. At most one group event in this review; it does not establish three individual carriers. KLM's own same-day release supplies no separate named cut. No inferred Air France/KLM/Transavia multiplication. |
| IAG, July 31 | Recovered the issuer-hosted 18-page call transcript. At 00:29:27 management says the main reason for flat guidance is Middle East cancellations; other reductions protect margins. At 01:04:24 winter reductions are discussed alongside uncertainty and possible competitor cuts under high fuel prices. BA describes redeployments to India and Nairobi. | Improved primary evidence, but no separately attributable new non-baseline carrier cut tied specifically to fuel/war economics established. Aer Lingus is already in the baseline. Neither suspended routes nor anticipated competitor cuts fill the count. |
| Lufthansa Group, August 4 | H1 charts link Q2 Eurowings reductions to fuel and Middle East cancellations; Q2 is historical. The identifiable CityLine, four A340-600, two B747-400 and five-short/medium-haul-aircraft package was announced on April 16, explicitly citing kerosene and labor costs. | That package is excluded as pre-baseline. Updated August guidance alone does not prove an additional new package. Do not recast a report date as the original announcement date. |
| Air New Zealand, August 28 annual results | Annual release discusses fuel-related capacity reductions for the fiscal year ended June 30. Issuer's May 14 market update, preserved in its June operational filing, already described three consolidations reducing capacity around 3–5%; potential future updates were conditional. | Historical cuts established; a new eligible August decision is not established by the annual narrative. Do not count May cuts again. This is not proof that no later announcement exists. |

**Sources:** [Southwest issuer 8-K](https://investors.southwest.com/sec-filings/all-sec-filings/content/0000092380-26-000074/0000092380-26-000074.pdf), [secondary Southwest call locator](https://transcripts.platformaeronaut.com/transcripts/LUV-2Q26-transcript); [AF-KLM issuer release](https://www.globenewswire.com/news-release/2026/07/30/3335784/0/en/Air-France-KLM-Q2-2026-Results.html), [Bloomberg firsthand reporting](https://news.bloomberglaw.com/mergers-and-acquisitions/air-france-klm-trims-capacity-outlook-on-high-fuel-prices), [KLM primary release](https://news.klm.com/klm-half-year-results-improved-but-not-sufficient-for-the-long-term/); [IAG primary transcript](https://www.iairgroup.com/media/ymmjb2dv/iag-h1-2026-results-call-transcript.pdf), saved locally; [Lufthansa April announcement](https://newsroom.lufthansagroup.com/en/lufthansa-group-accelerates-strategy-implementation/), [August issuer charts, pages 6 and 10](https://investor-relations.lufthansagroup.com/fileadmin/downloads/en/charts-speeches/LH-QR-2026-2-charts.pdf); [Air NZ August annual release](https://www.airnewzealandnewsroom.com/press-release-2026-air-new-zealand-announces-2026-annual-results), [issuer May update republished in filing, pages 4–5](https://company-announcements.afr.com/asx/aiz/28542f8b-5e12-11f1-a05a-a62d6643211b.pdf), saved locally. Secondary transcripts are locators, not authenticated issuer records. Repeated wire relays are one lineage.

An additional [Air Canada August 11 issuer release](https://www.aircanada.com/media/air-canada-reports-second-quarter-2026-financial-results/) was screened: reinstated capacity guidance is below its suspended April guidance, but this release does not establish the first announcement date and explicit fuel cause of additional cuts. Not counted; no broader airline census is claimed.

**Mechanism disposition:** not established by this bounded review. The paired EIA jet/gasoline result remains in [the prior reproducible comparison](../2026-09-08_catchup/brt29-eia-comparison.csv): intermittent leadership, with “during” still lacking a registered duration/count. Neither group-count discretion nor a new duration rule may manufacture a pass. A final MISS is also not justified merely by unfinished event coverage. BRT-29 remains OPEN to its registered final boundary; M remains a separately disclosed unresolved elapsed obligation.

## BRT-12: recovered diagnostic and invalid source claim

FRED's authenticated metadata endpoint returned HTTP 400, **series does not exist**, for `BAMLH0A0E2Y`. The same session returned HTTP 200 for `BAMLH0A0HYM2`, titled ICE BofA US High Yield Index Option-Adjusted Spread, units percent. See [saved metadata receipt](fred-metadata-probes.json). Initial sandbox connection failure was retried successfully with network access; this is a verified bad identifier, not a credential or FRED outage. It does not prove no licensed energy index exists elsewhere.

The April [build plan](../../scripts/BUILD_PLAN.md) wrongly advertises this feed and proposes continuous `BZ=F / RB=F / HO=F` crack legs. A historical warning now marks those claims. Runtime already uses correctly labeled broad HY, and `HY-ENERGY-OAS` was retired August 7 for lack of an instrument. No runtime repair or resurrection is required. Broad energy credit would still need its constituent perimeter checked before being treated as upstream E&P-only. BRT-11's historical grade was not reopened by this investigation.

**Recovered prices:** Yahoo chart API, explicit `BZX26.NYM`, `RBX26.NYM`, `HOX26.NYM`, each November 2026. Query1 returned 429; query2 with browser user agent returned successful JSON. Raw responses are saved. [Reproducer](reproduce_cracks.py) joins local exchange dates, excludes missing/nonpositive-volume rows and dates after September 4, and never forward-fills. September 8 product rows have zero reported volume and Brent lacks the comparable midnight bar; the final live records are excluded. Volume presence is a data-quality screen, not settlement certification or proof of synchronized trades.

Formula in dollars per barrel: `(2 × 42 × RBOB + 42 × heating oil) / 3 − Brent`. Product inputs are dollars/gallon; Brent is dollars/barrel. This is a theoretical price spread, not realized refinery profitability. See [124-row CSV](fixed-november-cracks.csv) and [validation / exclusions](crack-validation.json).

| Historical date | Fixed-November 3-2-1, $/bbl |
|---|---:|
| March 27 | 24.9714 |
| April 30 | 30.4822 |
| May 29 | 31.5156 |
| June 11 | 33.4766 |
| June 30 | 35.2368 |
| July 31 | 43.6110 |
| August 31 | 49.9314 |
| September 4 | 49.4698 |

This common-maturity diagnostic is generally wider across those selected month-end observations; it does not show monotonic daily widening or establish that compression never occurred. The March 27 value does **not** reproduce the original 41.37 recomputation and cannot replace that baseline. November was selected now for available matched history, not pre-registered. It must not be chosen retrospectively as the winning BRT-12 instrument. Original contract IDs/roll rules, authenticated settlements, upstream issuer/OAS history and an interpretable event-onset comparison remain outstanding. Missing measurement is not the August 13 ruling's “neither signal” outcome.

## September 9–11 release preparation

These are availability checks on September 8 evening ET, not new observations or a new automation. Existing [CATALYSTS](../../docket/CATALYSTS.tsv) owns the schedule; existing letters own grading.

| Read | Last published issue verified | Next authorized read / exact comparison |
|---|---|---|
| EIA retail fuel | September 1 release, August 31 observation | September 9 ~10:00 ET: confirm September 7 observation in regular gasoline and diesel; retain observation vs release date. BRT-29 premise is already closed. |
| EIA STEO | **August 11 release; forecast completed August 6** | September 9 noon–12:15 ET: save September vintage before comparing `COPS_OPEC` Q3/Q4 with the prior owner-recorded August estimate. August 13 was BRENT's grading/read date, not the issue date. Match definitions; forecast spare capacity is not observed flow. |
| EIA WPSR | September 2 release, week ending August 28 | September 10 noon ET: verify week September 4; table 1 gasoline/jet supplied, stocks/SPR, utilization; table 2 PADD 3 inputs and production. Reuse the paired-YoY method. Preserve the frozen September 4/11 SPR windows and existing two-print rule. |
| Baker Hughes / CFTC | Prior September 6 owner grades carried, not regraded here | September 11 after ~13:00 / ~15:30 ET: primary rigs and raw CFTC `f_disagg.txt`, as-of September 8. Run existing `cot_grade.py --expect 2026-09-08` after release; exit 3 means WAIT. Friday's 14:00 routine precedes COT publication. |

Primary availability pages: [retail fuel](https://www.eia.gov/petroleum/gasdiesel/), [STEO](https://www.eia.gov/outlooks/steo/), [WPSR](https://www.eia.gov/petroleum/supply/weekly/), [WPSR holiday schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php). The forthcoming releases cannot be processed before publication. No unattended follow-up or remote schedule change was installed.

## Inbox and operational closeout

OSPREY's new September 8 packet was read and logged. Its October 1 Q2 retiming is an owner proposal/state, not authority to alter BRENT's frozen September 1 comparison. Cross-owner clock disagreement remains explicit. Crude exports do not substitute for diesel/gasoil; packet values retain their attributed dates and were not newly verified here. Its Urals differential request is deferred because this pass recovered no dated same-basis differential; no reply sent.

Network boot: threshold/EIA checks ran successfully; instrument warnings remain for aged observations/incidents. Ledger Nudge reported FINDINGS, so the boot was not clean. Closeout updates the mail ledger and explains unchanged registry, TRADE and lesson index in the commit: no registered level, position receipt or lesson change occurred. A stamp would not resolve those subjects. Historical incident backlog is not cleared by this research.

Next research work is narrowly defined: authenticate the original BRT-12 contract construction and upstream credit history; complete BRT-29 event coverage without double counting; then read releases at their publication dates. Scheduled-release work remains pending, not completed.
