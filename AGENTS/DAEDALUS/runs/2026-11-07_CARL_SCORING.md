# CARL scoring and November 6 mark review — November 7, 2026

Authority: Will's direct three-deliverable instruction; first deliverable only. Source pin `a5790484a131cbec452b73ece2182d5759e9690e`. Inputs, exact historical rows, full commits, hashes and reproducible Decimal arithmetic: `2026-11-07_CARL_SCORING/{INPUTS.json,calculate.py,RESULTS.json}`. No CARL ledger, probability, outcome or trade was changed.

## Result

The eleven currently binary-resolved forecasts contain two CONFIRMED and nine MISSED. The existing WQ-112 scoring convention yields **0.4209** mean Brier; the original-call/earliest-known row-lineage comparison yields **0.4795**. Lower is better; a constant 50% on this same binary cohort scores 0.2500. CRL-21 remains MISSED at its original **60%**, loss **0.3600**. Its undated 25% does not score. CRL-15 and CRL-23 are OPEN: neither contributes a realized loss, hit, miss or improvement.

| Row | Outcome | Original/earliest-known probability | Eligible scoring probability | Original loss | Eligible loss |
|---|---|---:|---:|---:|---:|
| CRL-01 | MISS | 75% | 75% | 0.5625 | 0.5625 |
| CRL-03 | MISS | 90% | 90% | 0.8100 | 0.8100 |
| CRL-04 | HIT | 88% | 88% | 0.0144 | 0.0144 |
| CRL-07 | MISS | 80% | 80% | 0.6400 | 0.6400 |
| CRL-08 | MISS | 85% | 28% | 0.7225 | 0.0784 |
| CRL-09 | MISS | 75% | 75% | 0.5625 | 0.5625 |
| CRL-11 | MISS | 85% | 85% | 0.7225 | 0.7225 |
| CRL-16 | MISS | 60% | 60% | 0.3600 | 0.3600 |
| CRL-18 | HIT | 60% | 60% | 0.1600 | 0.1600 |
| CRL-21 | MISS | 60% | 60% | 0.3600 | 0.3600 |
| CRL-24 | MISS | 60% | 60% | 0.3600 | 0.3600 |
| **Sum / mean, n=11** | **2 / 9** | | | **5.2744 / 0.4795** | **4.6303 / 0.4209** |

The entire 0.0586 difference between these two aggregate means comes from CRL-08's previously ruled 85%→28% lineage. It is not evidence that the November 6 revisions work. Restoring CRL-21 from an ineligible 25% to 60% raises the same-cohort mean from 0.3939 to 0.4209; that is a scoring correction, not a deterioration in newly observed forecasting performance. CRL-19 MIXED is excluded, not assigned an invented 0.5 outcome. All OPEN, NO-VERDICT and RETIRED rows are excluded and enumerated in RESULTS.json (25 exclusions).

Original-probability provenance was read at the claim, not joined blindly on IDs: old CRL-05/06 in STATUS are today's CRL-03/04. CRL-11's 85% is the earliest recovered June 5 record, not a proved March 31 Date_Made probability. CRL-07 and CRL-08 changed windows/specification during their lives, so the original column is a conserved row-lineage diagnostic, not a pure unchanged-question ex-ante cohort. The original CRL-07/08 row dates and March 9 commit also disagree by one calendar day. These limitations travel with the first-call label. Existing outcome adjudications and the September 24 CRL-08 ruling are inherited; this assignment did not re-grade all eleven against external releases.

## CRL-15 — evidence and timing acceptance withheld

**Preserved marks:** original 65% (`bf073316af`, row Date_Made April 9; commit April 10); intermediate 35% entered July 24 but undated in the probability field; 10% entered with November 6 date at `5d49f490562a20ce3172314f50b2f83127756954`, **13:41:15 EST**. The original question remains SBA 7(a) defaults >6.5% by end-2026; no outcome has been assigned.

The reduction to 35% corrected a parent/subagent probability-ordering contradiction. The November reduction cites vendor TTM 4.8%, a purported need for +170 basis points inside two months, and absence of the FY2026 SBA file. The 4.8% is genuinely published by [Lumos on July 17](https://www.lumosdata.com/blog/sba-default-rates-small-business-credit-risk-2026), but it measures the year ending **March 31**, not a November starting level. Its publication predates the July 24 intermediate mark; POP's October 28 discovery is a later owner read, not a new observation. [Lumos's August 18 definitions](https://www.lumosdata.com/blog/how-lumos-measures-default-and-prepayment) distinguish trailing-year, calendar-year and fiscal partial-year rates with different constructions. A 170 bp subtraction is arithmetic, not a valid two-month reachability argument across those bases.

The [official SBA catalog](https://data.sba.gov/dataset/7a-504-foia) now lists September 30, 2026 files. A bounded HEAD request to its FY2020-present resource returned 200 and Last-Modified **October 30, 2026 15:45:55 GMT**, before the re-mark; receipt `SBA_RESOURCE_HEAD.json`. This contradicts treating the file's absence as verified. Current metadata supports earlier availability but is not an immutable historical publication certificate. The 188 MB loan file was not downloaded or converted into a newly chosen rate. Its existence does not prove that the registered >6.5% condition was publicly decidable on the registered basis.

The calendar-end question and fiscal-year resolver also require reconciliation: FY2026 already ended September 30, while calendar Q4 had not. If the intended resolver is fiscal-year data, November is after the observation window; if the intended question is calendar year-end, the future outcome remains open. Neither reading may be selected after seeing which helps the score. **Verdict:** the dated field is present, but the asserted new evidence, basis and public-outcome timing do not establish eligibility of 10% as a defensible prospective update. Contest the rationale through PROME/CARL; preserve 65%,35%,10%, and OPEN. No replacement probability or retrospective grade imposed. A missing measurement cannot be priced as a lower event probability under the existing prediction canon.

Counterexample that would overturn this withholding: a pre-existing, unambiguous rate/window definition plus dated comparable observations and publication evidence showing what remained unknown on November 6, accompanied by a probability rationale independent of publication difficulty. A later choice of a convenient denominator does not satisfy it.

## CRL-23 — prospective timing passes; size/direction rationale contested

**Preserved marks:** original 70% (`af5ed9a7f3`, May 3); undated-field 45% July 24; dated-field 15% at the same November 6 13:41:15 EST commit. Question remains **(DHI Q1 FY27 margin ≤17.5% OR PHM Q1 FY27 margin ≤22.0%) AND the named tariff condition through Q4 2026**, including the previously ruled parentheses.

[PHM's October 22 issuer release](https://pultegroup.com/investor-relations/news/news-details/2026/PulteGroup-Reports-Third-Quarter-2026-Financial-Results/default.aspx) confirms Q3 home-sale margin 24.8%, 280 bp above the future bar. The [October 29 DHI call transcript](https://www.roic.ai/quote/DHI/transcripts/2026-year/4-quarter) carries Q1 guidance 18–18.5%, 50 bp above the bar at its low end, matching HOMER's November 5 saved excerpt. That is a third-party transcript, not independently checked call audio; the issuer earnings release establishes the October 29 reporting event but does not itself establish that guidance sentence.

These releases are after the July 24 mark and before the November 6 re-mark. They concern earlier results or guidance, not the target outcomes: DHI's target quarter ends December 31, PHM's March 31, and the full Q4 tariff condition had not elapsed. On the inspected evidence, no final result was already publicly knowable; timing is prospective. This is not proof every potential source was searched or that the entire tariff condition is satisfied. The latter claim was not independently re-adjudicated.

However, the prior reduction cited DHI actual margin 20.7%, next-quarter guidance 20.5–21%, and PHM 25.0%. The newly cited levels are **closer to the forecast downside thresholds**, not obviously evidence for a further large probability reduction. Above-bar guidance alone supplies neither its error distribution nor the joint probability of the unchanged conjunction. **Verdict:** no established outcome laundering; structurally dated forward judgment, but the quantitative rationale for 45%→15% is unsubstantiated by the cited distances. Contest that rationale and request an owner explanation of the incremental evidence, guide uncertainty and joint-event probability. Do not manufacture a replacement probability or remove the dated mark. Future scoring must retain original-call comparison; there is no realized revised-mark performance yet.

Counterexample: a dated, comparable distribution of guidance errors and the remaining conjunction risks could make 15% defensible despite closer headline levels. Neither this read nor the owner Notes supplies it.

## What this establishes about reliability

This small, selected resolved cohort has poor probability performance relative to a constant 50% benchmark, with substantial historical overconfidence. It does not validate CARL's probabilities for sizing or establish that revisions improved skill. Eleven heterogeneous, related calls are not eleven independent trials; unresolved and ungradeable calls are absent; some letters changed; earliest-probability recovery is imperfect. This is not a test of profitability, all CARL research, causal mechanisms, or future reliability. No significance, calibrated replacement probabilities or trading recommendation follows.

The useful response is to preserve originals, score eligible updates separately at genuine outcomes, and repair the two specific evidentiary explanations. The two current reductions would reduce loss if their events miss and increase it if they hit; that mathematical incentive is not proof of deliberate gaming.

## Review and delivery

REVIEW: required — scoring/evidence interpretation under UPGRADE_PROTOCOL 4/4b. Reader `/root/carl_scoring_review`; exact coverage, counterexamples and hashes at `2026-11-07_CARL_SCORING_REVIEW.md`, indexed by `2026-11-07_CARL_SCORING_READER_REPORTS.md`. Parent conclusions shared before final check; independent replication, not pristine blind convergence. Final disposition recorded after reader return. No new rule, checker, rubric or model change.

Web pages accessed November 7; displayed publication dates distinguish the evidence window from retrieval. Historical page revisions and universal pre-result availability were not certified. Source amounts are not live trading inputs. This result completes the two assigned reviews even though CARL retains the owner response; that response is not fabricated as consumed.
