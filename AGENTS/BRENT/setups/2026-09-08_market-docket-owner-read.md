# BRENT market docket — owner read, 2026-09-08

STATUS: COMPLETE_TO_AVAILABLE_EVIDENCE. Owner implementation; source gaps remain open. No trade, order, new proposal, threshold, probability or band change. WQ-189/192 STAND DOWN remains binding.

## L198: port totals and the positive control

① MIRROR, direction only: Reuters reporting dated September 8 attributes full-August Sidi Kerir exports of 2.139 mb/d to provisional Kpler data. Against the existing 2.17 mb/d port-total benchmark this is approximately −1.4%, superseding the August-to-date 2.3 / +6% comparison. These are different observation windows: this does not establish a sequential decline of 0.161 mb/d. Full-month port-total rerouting remains consistent with northern outlets absorbing flow; this does not independently establish Saudi production loss or a westbound constraint. The benchmark is specifically Vortexa (George Morris via MarineLink), WEEK COMMENCING AUGUST 3, all-destination total liftings, as documented in setups/2026-08-17_petroline-ras-tanura-discriminator.md §2 and its August 21 amendment. It is neither a Kpler baseline nor a full-August average. The existing amended lag test REQUIRES the same tracker, weekly cadence, total perimeter and a published completed-week observation. Kpler full-August fails the tracker and cadence limbs: formal lag-test result = NOT RUNNABLE — NO-VERDICT. The −1.4% arithmetic is context only, not a like-for-like delta or a grade. Next source is a published completed-week Vortexa Sidi Kerir total-liftings observation in the registered lag window; no conversion or respec. No independent Vortexa series was obtained. Multiple Reuters relays are one Kpler/wire lineage, effective n=1.

Source read September 8: [Reuters via Business Standard](https://www.business-standard.com/markets/commodities/why-brent-crude-is-below-100-despite-disruptions-to-gulf-oil-flows-126090800091_1.html), [same wire via RTE](https://www.rte.ie/news/business/2026/0908/1590715-why-isnt-oil-above-100-despite-supply-disruptions/). Primary tracker access remains UNKNOWN.

② UNKNOWN / PENDING PUBLICATION in the last successful capture; owner's present availability retry BLOCKED. Parent's official PortWatch capture at 20:50:15Z September 8 ends August 30: n_tanker=2, capacity_tanker=42,932 dwt, n_total=6. August 29=1/9,744/3; August 28=0/0/7; August 27=2/4,989/2; August 26=2/0/5. Date-descending latest-five query. The required August 31–September 1 rows are absent from that successful response. The transfer-limit flag reflects the five-row limit; it is not evidence of a newer row hidden behind those older rows.

Exact retry (once in web access, once in host access; no altered window):
`https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?where=portid%3D%27chokepoint6%27&outFields=date%2Cn_tanker%2Ccapacity_tanker%2Cn_total&orderByFields=date+DESC&resultRecordCount=5&f=json&returnGeometry=false`

Web returned a non-retryable safe-open error; host urllib at 22:18:51Z returned Errno −3, Temporary failure in name resolution. Therefore this session cannot independently assert the endpoint still ends August 30. Owner result is UNKNOWN, not a coverage-defect grade. August 30 is not substituted for the target. No new control observation/counter increment. Existing named-positive Sidr / Senegal Prosperity and ≥~500k / <250k dwt rules remain exactly as registered; vessel evidence is carried from FALCON VI-2026-0020/0021, not reauthenticated here. Next source action: same query at next desk boot; grade only when the target window exists and provenance matches. No unilateral target-window change.

Evidence: `PROME/reports/2026-09-08_orch-brent-portwatch_latest.txt`, parent's fetch JSON and owner's `outbox/2026-09-08_owner-fetch-evidence.json`.

## L140: Q1 instrument / Q2 flow / Q3 crack

Q1 = UNKNOWN-AT-PRIMARY. Improved evidence: [GARANT transcription](https://www.garant.ru/products/ipo/prime/doc/414729929/) and [ConsultantPlus transcription](https://www.consultant.ru/document/cons_doc_LAW_543093/) agree on resolution No.1097 dated August 28 amending No.954 dated July 30: paragraph 4 changes September 1 to October 1; paragraph 5 changes August 31 to September 30. The text makes effectiveness depend on official publication. This is instrument-text transcription, stronger than minister guidance or a wire description, but neither an authenticated official copy nor an official publication receipt.

Documented primary `https://government.ru/docs/59723/` was inaccessible through web and failed host DNS. Official-publication fallback `https://publication.pravo.gov.ru/` and domain-restricted search did not recover the instrument. This is an access/retrieval failure, never evidence that no decree exists. GARANT posting August 31 is not an effective date. Secondary reported publication dates do not authenticate publication.

Exact missing limbs: official No.1097 text and publication receipt/effective-date authentication; original No.954 paragraphs 4/5 to authenticate the amended scope. The ConsultantPlus embedded reference did not recover that original text in this session. Reported direction opposes the September 1 opening; October 1 is a TRANSCRIBED SUCCESSOR ONLY. Existing Q1 test date September 1 and full-read October 1 remain as registered; no imported date or flow-window change.

Q2 = UNKNOWN, OSPREY-owned Russian diesel/gasoil four-weeks-after versus four-weeks-before September 1. Crude flows are not diesel flows. OSPREY's carried 3.46 mb/d crude series through August 23 is not a substitute, and a next crude weekly observation was not found on its owner carriers. Q3 = UNKNOWN for a fresh matched diesel crack; it remains a separate product-price test and cannot be graded from the Q1 transcription or a crude headline. Next: recover official text/publication and OSPREY's specified series; full registered read October 1. Do not infer physical easing from a policy date.

## Physical / paper and named contracts

PRIMARY EIA [Europe Brent spot history](https://www.eia.gov/dnav/pet/hist/RBRTED.htm), opened September 8: September 1 physical observation $96.02/bbl; release stamp September 2, next update September 10. The table provides no newer observation in that week. EIA/FRED are the same measurement lineage. This is not a direct licensed Platts assessment.

Parent's saved Yahoo chart responses were independently parsed by this owner. They are MIRROR vendor daily bars, not authenticated exchange settlements:

| Date | BZX26 (Nov) | BZZ26 (Dec) | BZF27 (Jan) | CLV26 (Oct) | CLX26 (Nov) | BZX26−BZF27 |
|---|---:|---:|---:|---:|---:|---:|
| September 1 | 94.65 | 91.57 | 88.67 | 90.22 | 87.75 | 5.98 |
| September 2 | 95.63 | 92.09 | 88.98 | 91.01 | 88.28 | 6.65 |
| September 3 | 95.52 | 91.63 | 88.32 | 91.30 | 88.03 | 7.20 |
| September 4 | 96.28 | 92.32 | 89.15 | 91.48 | 88.57 | 7.13 |

September 1: 96.02 − 94.65 = $1.37/bbl VENDOR-CLOSE PROXY ONLY. Official matched benchmark remains UNKNOWN. Retire the archived intraday 95.22 / 0.80 comparison from live use. TRACKER's September 1 +6.98 is an arithmetic/carrier error: the named-contract inputs give +5.98. Older September 2 captures 95.23 / 88.80 / +6.43 are superseded vendor snapshots, not a market movement from one capture to the next.

September 8 parent snapshots are LIVE: BZX26=99.29 at 20:40:01Z; BZZ26=95.43 at 20:39:57Z; BZF27=92.11 at 20:38:45Z; CLV26=94.24 at 20:40:11Z; CLX26=91.25 at 20:40:06Z. Illustrative BZX−BZF=7.18; X−Z=3.86; Z−F=3.32; November WTI−Brent=−8.04. The legs are not precisely synchronous. None is a September 8 settlement, even though timestamps follow the equity close. No continuous-roll delta and no close-counter increment.

Official [CME settlement page](https://www.cmegroup.com/markets/energy/crude-oil/brent-crude-oil-last-day.settlements.html) and [ICE Brent data page](https://www.ice.com/products/219/Brent-Crude-Futures/data) did not expose a dated matched settlement in accessible output. Own named-contract Yahoo host requests failed DNS; web history fallback did not recover bars. Official September 1 matched settlement and September 8 closes remain UNKNOWN. No threshold grade from those failures.

Saved bar sources: `PROME/reports/2026-09-08_orch-brent-{BZX26,BZZ26,BZF27,CLV26,CLX26}-NYM.txt`. Owner web output is retained in `outbox/2026-09-08_web-source-evidence.json`.

## Calendar and position obligations

PRIMARY [EIA WPSR holiday schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php), read September 8, places the week-ending September 4 release on Thursday September 10 at NOON ET because of Labor Day. September 9 on BRENT's live calendar was wrong. This corrects publication timing only. Read SPR, refinery utilization, PADD 3 inputs and product stocks at that release; existing SPR/Edouard bands are unchanged. The two-print SPR verdict cannot be taken from the first print.

Source/spec gap sent to PROME: the frozen letter calls the named weeks ending September 4 and September 11 “entirely in September,” although the September 4 survey week spans August. Preserve the explicit named windows; do not silently repair the binding letter or certify an unpublished DOE delivery schedule. A final schedule-interpretation claim remains conditional on resolving that wording and the existing secondary-only delivery-window premise.

TERRY's September 8 packet and owner cards govern implementation. XLE regular-session September 8 vendor close 64.77 is below existing 66.50; it selects the approved September 9 open exit of both September 30 65 calls, even on a red open. A rebound does not replace the September 8 close test. TERRY tracks implementation; Will verifies live broker holdings/orders/bid and executes. BRENT has no broker receipt and records no sale. L253 stays receipt-pending for PROME.

USO October 16 135C: one contract sold September 2 per Will's direct confirmation reproduced in TERRY's card; one remains. First-sale price permanently UNKNOWN under WQ-167; no re-ask. A=NO-VERDICT, no second $14.25 target. B=official USO close <135 -> next-open exit of the remainder; September 8 vendor close 146.03 does not select that exit on available mirror evidence. Official exchange-close authentication was not newly obtained. C=October 9 before-close unconditional time stop; no roll. September 18 150/165 spread HOLD through expiry under WQ-168. USO share scaffold remains unratified; refiners fill status UNKNOWN. No new Will question.

## Owner judgment and limits

Available evidence supports continued prompt tightness and rerouting rather than an authenticated easing event; it does not establish a new deployment condition. WQ-189/192 STAND DOWN remains binding, with existing confirmed-destroyed-capacity frame-breaker handling unchanged. No regime/probability/band change; no independent witness added by repeated wire relays or EIA/FRED retrievals. Friday September 11 Baker Hughes and COT are the next registered pair; preserve the September 6 grades until new dated primaries arrive. Boot's stale local EIA data and network failures are not fresh no-breach grades.

