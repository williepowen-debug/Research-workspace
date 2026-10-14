# WAL FFIEC deep read — October 14, 2026

**Result: fresh access works; the missing history is now extracted.** Eight complete Western Alliance Bank Call Reports cover September 2024 through June 2026. Seven quarters carry the newer NDFI detail. Seventy named fields and 8,702 supporting schedule rows are saved with definitions, units and source hashes. This improves the evidence behind the existing thesis, but establishes neither a persistent new loss trend nor an expectations gap. V3 remains 3/5; all weights, targets, prediction grades, frozen frames and trade rules are unchanged.

**Authority:** Will: “Can we look into these now? Do you have access to pull this data?” One bounded WAL study of NDFI commitments/credit, modifications and losses, mortgage activity, capital and contingent exposures. No additional bank, recurring monitor or peer/funding study. REGINALD retains funding/cohort/severity ownership.

## Access, source and reproducibility

The desktop credential fields exist and an authenticated **curl** request returned HTTP200 with a valid June facsimile. Python urllib returned403; this was not proof of an expired credential. No secret is printed or copied to the research files. Eight periods retrieved successfully; the September30 2026 request returned **HTTP500**. **Q3 was not retrieved; the server error does not establish whether WAL has filed it.** Renewal around November1, before the recorded November5 expiry, remains separate from today's demonstrated access.

Entity throughout: **Western Alliance Bank, ID_RSSD3138146**. Monetary raw fields are **USD thousands**, converted below to millions/billions. These are bank observations, not automatically listed-parent EPS or capital. Files: `../sources/ffiec_2026-10-14/`; dated retrieval receipts retain status/date/hash/row count. `2026-10-14_FFIEC-metrics.json` supplies formulas, missing values and source manifest; `.tsv` is the compact series; `2026-10-14_FFIEC-selected-fields.tsv` preserves supporting schedule rows and their exact locators.

Reproduce offline: `python3 AGENTS/WAL/scripts/ffiec_wal_analyze_20261014.py` from root. Validation includes seven funded-NDFI subtype ties, seven unused-subtype ties and eight CET1 numerator/RWA ties. Q2 bank NCO computes to **$55.027M**, reproducing issuer **$55.0M** at its printed precision. Fresh March/June originals also reproduce the previously saved files byte-for-byte. No tolerance was widened to resolve a substantive disagreement: the comparison uses the issuer's $0.1M precision.

## 1. NDFI: credit trouble is measured, but the path is episodic

RC-N Memo9 `RCONPV25`, divided by same-quarter RC-C9a `RCONJ454`:

| Quarter end | Funded NDFI, $B | NDFI nonaccrual, $M | Nonaccrual / NDFI |
|---|---:|---:|---:|
| 2024-12-31 | 11.797 | 0.590 | 0.005% |
| 2025-03-31 | 12.576 | 0.595 | 0.005% |
| 2025-06-30 | 12.961 | 1.073 | 0.008% |
| 2025-09-30 | 13.577 | 99.524 | 0.733% |
| 2025-12-31 | 14.672 | 99.133 | 0.676% |
| 2026-03-31 | 14.928 | 71.304 | 0.478% |
| 2026-06-30 | 15.812 | 122.456 | 0.774% |

September2024 has the aggregate NDFI balance but lacks these newer detail fields: **missing, not zero**. June2026 is the highest nonaccrual balance and rate in this seven-observation series, up **$51.152M /71.74% QoQ**. NDFI30–89 and90+ accruing balances are both zero in June. The sequence is a large late2025 step, a decline and a rebound; it is not a monotonic acceleration. Borrower identity, reclassifications, cures and loss attribution remain unknown. **Do not attribute the balance or increase to the $99M loan, Cantor or LAM by matching magnitudes.** Historical fraud realizations may matter, but the aggregate field cannot identify their contribution.

**Corrected evidence state:** the June level is now directly verified at primary, with seven observations. The carried “one quarter/no trajectory” description is superseded. This removes an evidence-access gap, not the need to explain the loans or seek Q3 confirmation. The live score stays3/5; this study neither changes nor retroactively interprets the registered score-change conditions.

### Commitments and a historical composition trap

RC-L1e3 total unusedNDFI is **$4.884B**, versus March$4.744B. Funded plus unused contractual face amounts total **$20.696B**, +5.21% QoQ; this is neither expected loss nor risk-weighted exposure, and does not establish that all commitments will be drawn.

| NDFI borrower type, June2026 | Funded, $B | Unused, $B |
|---|---:|---:|
| Mortgage credit intermediaries | 10.895 | 1.681 |
| Business credit intermediaries | 3.459 | 2.660 |
| Private equity funds | 1.457 | 0.544 |
| Consumer / other | 0 | 0 |

Unused business-intermediary commitments increased **17.44% QoQ**, while funded business loans rose about1.29%. That is available contractual exposure, not observed borrower draw pressure. The all-NDFI funding ratio is an aggregate stock proxy; it is not a tracked utilization rate for a fixed cohort of credit lines.

**Historical caution:** June→September2025 business-intermediary loans jump **$0.217B→$3.329B**, while “other NDFI” falls **$2.660B→$0**. Aggregate NDFI increases only **$0.617B**. Consequently the entire business-line jump cannot be treated as net new aggregate NDFI exposure. Reclassification, runoff and new lending cannot be separated from these endpoints. Keep the offset visible before fitting subtype growth or private-credit acceleration.

## 2. Modifications and arrears: a mixed picture, with important population controls

| Bank measure, $M | March2026 | June2026 |
|---|---:|---:|
| Modified loans complying with modified terms (`HK25`) | 176.064 | 232.291 |
| Modified loans30–89 days past due (`HK26`) | 3.369 | 2.680 |
| Modified loans90+ accruing (`HK27`) | 105.834 | 42.325 |
| Modified loans on nonaccrual (`HK28`) | 55.043 | 56.475 |
| Sum of the reported modification populations | 340.310 | 333.771 |

Performing modifications rise **31.94%**, but the combined reported balance falls **1.92%** and modified90+ accruing loans decline sharply. The stock therefore shifts toward compliance with modified terms. **That does not establish cures or successful repayments:** these are not loan-level transition cohorts, and the current RC-C instruction includes modifications made during the previous12months. Expirations from that window, charges, sales and reclassifications can change the populations. Historical definition changes must be considered before fitting one long modification trend.

Within other nonfarm nonresidential CRE, performing modifications rise **$39.909M→$72.736M**; nonaccrual modifications are **$51.198M→$51.545M**. This is broad CRE, **not Office classified** and not a carrier for WAL-01 or the migration count.

**Avoid a false arrears alarm:** raw bank90+ accruing loans are **$1,285.415M**, but **$1,222.895M** is the separately reported rebookedGNMA population. The residual is **$62.520M**, versus March$64.555M; residual does not mean wholly unguaranteed. The GNMA line includes loans repurchased **or eligible for repurchase**. It cannot be called a new cash repurchase, realized loss or unprotected bank NPL solely from this report. Nonaccrual loans$564.365M also include$1.960M in the government-guaranteed/insured population; retain the issuer's own denominator and scope when comparing its rounded$562M measure.

June RC-NM7 reports **$234.493M additions to nonaccrual assets duringH1**; M8 reports **$0 sold nonaccrual balances duringH1**. These fields are **semiannual, June/December only**; missing March/September is notzero. M8 is balance sold, not proceeds, and zero does not prove no cures, payoffs, foreclosures or charge-offs. A complete loan-level entry/exit bridge is still unavailable.

RI-B is year-to-date: June less March yields Q2NCO$55.027M. The bank's broader “all other loans” loss line is not a separate NDFI-only loss series; no inferred fraud adjustment or loan identification is made. RI-C provides broad allowance pools, not an NDFI-specific reserve. No reported pool reserve is mechanically allocated by NDFI balance share.

## 3. Mortgage activity: more sales, less reported bank income

| RC-P / RC-M measure | March2026 | June2026 |
|---|---:|---:|
| Mortgage loans sold during quarter, $B | 14.034 | 16.170 |
| Mortgage sale/securitization/servicing income during quarter, $M (`RIADHT85`) | 72.659 | 45.723 |
| Repurchases/indemnifications during quarter, principal/commitments $M | 21.505 | 23.880 |
| Total representation/warranty reserve, $M | 2.463 | 3.288 |
| Mortgage servicing assets carrying value, $M | 1,515.565 | 1,499.649 |

Sales volume rises **15.21% QoQ**, while this bank-income line falls **37.07%**. Against June2025, however, the income line is **up5.27%**; the QoQ decline is not evidence of a newly unprecedented earnings collapse. This is useful evidence to investigate pricing, servicing, valuation and hedge components rather than assuming higher originations yield proportionate earnings.

**Model boundary:** RC-P's$45.723M is not a replacement for the parent's Q2$53.4M origination/sale and$31.3M servicing lines. Its definition selects particular bank RI categories and does not provide a complete parent classification/entity bridge. Do not insert the$26.936M bank-line decline into the FY2027 EPS bridge as recurring pretax drag. Additional parent disclosure, fair-value/hedge attribution and component reconciliation are needed. Dividing this income by sales would not produce a clean gain-on-sale margin.

Repurchases/indemnifications report principal or commitments, **not losses**; June$23.880M is below June2025$39.851M. The reserve is a different stock and population, so its ratio to quarterly repurchases is not a recovery/coverage verdict. Reserve subitems are blank while the total is reported: preserve that missing detail. June servicing without recourse is$75.682BUPB; assets sold with recourse/max reported credit exposure are each$963.969M. Those two equal recourse columns describe the same reporting row's population, not two additive exposures. Neither is automatically an incremental loss or a separate amount to add to NDFI.

## 4. Capital and contingent exposure: measured, not a new cliff

Bank CET1 rises **$7,445.588M→$7,651.672M (+2.77%)**, while RWA rises **$64,129.120M→$66,063.310M (+3.02%)**. The reported ratio moves **11.6103%→11.5823%**, down2.80bp. This is RWA growing slightly faster than capital, not evidence here of a capital failure. The bank is not the listed parent; parent capital, equity and AOCI retain their own bases. REGINALD's funding/capital integration remains authoritative in its lane.

JuneMSA threshold deduction is **$0**, despite **$1.500B** mortgage servicing assets. Zero threshold deduction is not zero valuation sensitivity or zero RWA. RC-RII other on-balance securitization exposure is **$10.662B**, associated SSFA RWA **$2.124B**; off-balance securitization exposure is **$2.180B**, SSFA RWA **$0.436B**. Locator: RC-RII9d/10, columnsA/T (`S490/S493`, `S495/S498`); form labels distinguish exposure and RWA. The on-balance SSFA average is about19.9%, not a market loss estimate. These rows do not identify all underlying borrowers and cannot be added to NDFI or recourse totals without an overlap bridge. **Do not rebrand every SSFA dollar as private credit or hidden CRE.**

RC-V shows nonzero consolidated-VIE cash/other assets/liabilities, but no loan-level connection to the tracked credits. Detailed derivative and fair-value schedules are extracted for inspection; their notionals/levels do not supply net duration, net credit risk or an earnings shock. No new generic derivative alarm is inferred.

## 5. How to use this at the existing Q3 disclosures

1. **Credit:** quarter-match the NDFI nonaccrual/rate and unused subtype balances; seek attributed borrower entries/exits/losses. Preserve the September2025 composition offset. No new scored band.
2. **Mortgage earnings:** reconcile production, sales, bank income, parent income, servicing/FV/hedges and repurchases. Treat volume and valuation separately before changing sustainable earnings.
3. **Modification/arrears quality:** read compliant and delinquent modifications together, strip out the separately identified GNMA population for a labelled comparison, and keep the frozen nonaccrual/full-NPL denominators intact. Do not await an RC-NM7/M8 quarterly print that does not exist.
4. **Capital:** reconcile actual parent earnings, payouts, AOCI and shares; compare bank CET1/RWA on the bank basis. Do not convert the bank's regulatory exposure/RWA ratio into an equity loss assumption.

The existing October19 release/October20 call and later10-Q/CallReport remain the carriers. **No demonstrated expectations gap** remains the conclusion: better historical evidence has not established persistent earnings near$8, a new office migration, the $99M appraisal result or an unpriced loss. Affiliated borrower attribution, net duration, all-in funding optimization and matched analyst component forecasts remain gaps. UBPR peer work would be a separate REGINALD-owned reuse/check, not an independent confirmation or a new peer study here.

## Sources and limits

Authenticated FFIEC CDR `RetrieveFacsimile`, SDF, RSSD3138146; eight fresh originals and dated request receipts under `sources/ffiec_2026-10-14/`. [Official current form](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC041_202609_f.pdf), [official instructions](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_FFIEC041_202609_i.pdf): RC-CMemo1 pp190–193, RC-NMemo7/8/9 p352, GNMA p346, RC-P p399–400, MSA p315–316; form RC-RIIp70/printedRC-56. Current instructions explain the current population; they do not erase prior taxonomy/definition changes. Older subtype blanks and non-quarterly fields stay explicit. No new current market quote, Q3 actual or option mark supplied.
