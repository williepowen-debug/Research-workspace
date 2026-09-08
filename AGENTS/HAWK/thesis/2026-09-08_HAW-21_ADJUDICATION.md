# HAW-21 adjudication — 2026-09-08

**Owner verdict: CONFIRMED, resolved 2026-09-08. Registered confidence remains 65%.** The published CBSA notice is an expressly permitted evidentiary instrument in HAW-21. Its September 8 application statement, together with the two made orders and an exact commodity comparison, meets the registered in-force and scope limbs. This is an owner assessment of the combined operative evidence. The SOR registration identifiers and registration dates have NOT been independently established.

## Registered letter and dated search

Governing record: `thesis/PREDICTIONS.tsv`, HAW-21 Prediction/Invalidation cells, and `thesis/2026-09-02_CANADA_9-8_PREREGISTERED_READ.md`. The row permits Gazette OR Finance/CBSA notice stating the measure is in effect by September 15. It requires a dated search of Finance, Gazette Part II and CBSA; all three were attempted September 8. No probability, scope condition or verdict boundary was amended. The original pre-registration remains intact, with a dated outcome addendum only.

| Primary; document date | September 8 owner retrieval | Outcome |
|---|---|---|
| [P.C. 2026-0785](https://orders-in-council.canada.ca/attachment.php?attach=48943&lang=en); September 4 | Initial direct web failure; indexed discovery then successful direct open and English schedule extraction | United States Surtax Order (2026); s.1 sets 15/25/50% of value for duty. S.10 says September 8, or registration day if later. Affirmative legal act exists. |
| [P.C. 2026-0786](https://orders-in-council.canada.ca/attachment.php?attach=48944&lang=en); September 4 | Initial direct failure; indexed discovery then successful direct open and English schedule extraction | Amends Steel and Aluminum 2025 order; schedules 1/2 at 25%, 1.1/2.1 at 50%. S.4 follows the 2026 order, subject to later registration. |
| [CBSA Notice 26-23](https://www.cbsa-asfc.gc.ca/publications/cn-ad/cn26-23-eng.html); September 7 | Direct web open failed on CBSA aliases; primary-domain indexed body recovered, paragraphs 1–11 and 39 | Paragraph 4 explicitly states September 8 application at 15/25/50%. This closes the operational limb on the permitted notice basis. Indexed primary evidence is not a direct host receipt. |
| [Finance product list](https://www.canada.ca/en/department-finance/news/2026/08/list-of-products-from-the-united-states-subject-to-counter-tariffs-effective-september-8-2026.html); updated August 26 | Direct web open, full commodity table reconstructed from overlapping numbered windows | All 629 commodity items and rates reproduced. Effective 12:01 a.m. September 8; the sentence supplies no timezone. |
| [Finance announcement](https://www.canada.ca/en/department-finance/news/2026/08/canada-announces-targeted-countermeasures-and-substantive-support-for-workers-and-businesses-in-response-to-us-tariffs.html); August 25 | Direct web open | $27.6B import coverage; carry **CA$27.6B, currency inferred**, not quoted CAD and not tariff revenue. Existing auto counter-tariffs remain. |
| [Gazette Part II index](https://gazette.gc.ca/rp-pr/p2/2026/index-eng.html); page modified August 20 | Direct web open; latest displayed edition August 26, SOR/2026-172–181 | Registration identifiers/dates UNKNOWN. A publication index ending before these orders cannot establish non-enactment. |

Local urllib retrieval of both orders and Finance failed with `Temporary failure in name resolution` in the sandbox. No sandbox setting was changed; available web retrieval supplied the evidence above.

## Scope comparison

Two separate reproductions pass: PROME's `reports/2026-09-08_orch-hawk-verify-census.py` on its retained extracted pairs, and HAWK's independent September 8 primary-page extraction in `domain/sources/2026-09-08_canada_source-lines.json`, checked by `domain/sources/2026-09-08_verify_canada.py`.

| Rate | Finance items | Union of orders |
|---|---:|---:|
| 15% | 21 | 21 |
| 25% | 195 | 195 |
| 50% | 413 | 413 |
| Total unique commodity items | 629 | 629 |

Duplicates: 0. Missing in either direction: 0. Rate mismatches: 0. English commodity ranges exclude Chapter 98/99 exception schedules and French duplicate text. Counts are tariff items, not import-value weights. No materially narrowed commodity set is observed against the announced list. The statutory remission conditions remain part of actual exposure; matching commodity schedules does not establish equality of effective importer liabilities.

Selected matched items: 8433.20.00 and 8433.90.00 (other mowers / harvesting-machinery parts), 15%; 8433.11.00 (specified powered mowers), 25%; 4804.39.00 and 4810.31.00 (specified kraft paper/paperboard), 25%; 4702.00.00 (dissolving chemical wood pulp), 50%. These are line-specific examples, never sector-wide rates.

## Remission, exceptions and exposure

0785 s.2 excludes qualifying Chapter 98/99 goods, in-transit goods, qualifying Campobello personal imports and Import for Re-Export permit goods. Its consequential amendments extend remission to eligible manufacturing, processing, agricultural-production and food/beverage-packaging uses, plus specified health/public-safety and listed goods, **subject to the Remission Order's s.5 conditions**. 0786 preserves prior-rate treatment for qualifying in-transit goods. CBSA paragraph 8 prohibits stacking this order with the Steel Derivative Goods Surtax Order. CBSA paragraph 9 says postal/courier de-minimis remission does not automatically remove the surtax; paragraphs 10–11 preserve specified remission/relief routes. Importer eligibility, date conditions and claim documentation remain to be checked.

The drawing set covers products targeted by US §338 AND §232; a US-side exclusion does not transfer to Canada's opposite-direction measure. September 8 is not a new general auto-exposure date: Finance preserves existing auto counter-tariffs. MARCO's US Annex census remains its own dated evidence, not re-certified by this Canadian extraction.

**Transmission:** nominal tariff presence is an exposure screen. Liability depends on origin, item, value for duty, transit and remission; economic incidence also depends on substitution and contracts. No employer-level order cancellation, headcount loss or WARN event was established by this work. Employment impact is UNKNOWN, never zero by absence or implied by tariff presence.

## Counters, non-fires and follow-up

- Published named orders: 2; matched commodity items: 629; scope/rate mismatches: 0. Required search families attempted: 3/3.
- HAW-21: OPEN → CONFIRMED on the existing letter. Book: 6 CONFIRMED / 9 FAILED / 1 PARTIALLY / 1 VOIDED / 2 REHOMED / 2 OPEN. Binary Brier contribution at registered 65%: 0.1225; no probability revision.
- TRADE-02 remains ORANGE. The Canadian event does not supply a new band limb. CODIF-01 and HAW-20 are unchanged; new codification does not resolve HAW-20's down-direction test.
- September 9: retry Gazette/registration and direct CBSA receipt; fallback review September 11, before the original September 15 deadline. Do not infer an SOR number from a collection code. Reconcile contrary primary evidence if it appears.
- MARCO/LABOR/WALTER receive the product/remission/exposure packet. PROME owns L225/L234 closeout and any shared coordination updates. No trade or capital action.
