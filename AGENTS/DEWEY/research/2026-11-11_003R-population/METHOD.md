# 003R population refresh: reproduction method

Research-specific evidence for the existing Q3 historical-band/placement commission, November 11, 2026. This is not a production helper or scheduled collection job. Final completeness is determined by `population-validation.json`, not by this method document. While retrieval runs, intermediate tables are incomplete and must not be cited as population results.

## Current-quarter source

FFIEC Public Web Service base `https://ffieccdr.azure-api.us/public`, reporting period `9/30/2026`, data series `Call`. Authorized credentials are supplied privately; none is stored in evidence. Retrieve `RetrievePanelOfReporters`, then `RetrieveFacsimile` for every panel row whose `HasFiledForReportingPeriod` is true, using `fiIDType=ID_RSSD`, the row's RSSD and `facsimileFormat=SDF`. Decode the JSON base64 response. Requests are sequential with at least 1.55 seconds between starts; 031/041 forms are prioritized, followed by 051, with no prior-asset prefilter. A retrieval error stops the pass rather than being silently skipped. The panel, full compressed SDF sources, retrieval timestamps and decoded-source hashes are preserved.

Parse the semicolon-delimited SDF by MDRM. For each balance-sheet field, use a reported RCFD code if present, otherwise RCON; a reported zero is not a missing value. Verify the chosen codes and scope, particularly for 031 banks. All monetary values are $thousands.

| Derived field | SDF source |
|---|---|
| ASSET | 2170 |
| LNLSGR, gross loans including HFI/HFS | 2122 |
| LNATRES, allowance | 3123 |
| NALNLS, nonaccrual | 1403 |
| P9LNLS, 90+ days still accruing | 1407 |
| NCLNLS, noncurrent | 1403 +1407 |
| LNCRCD, credit-card loans | B538 |
| NTLNLS, YTD net charge-offs | RIAD4635 −RIAD4605 |
| ELNATR, YTD provisions for credit losses | RIADJJ33 |

For the last two fields, derive Q3 quarterly flows by subtracting June's FDIC YTD amount for the same certificate. Do not substitute RIAD4230 (loan-only provisions) for RIADJJ33: EagleBank's June values differ, and the FDIC ELNATR field matches JJ33. The de-cumulated current-quarter flows are calculated from these source fields; they are not represented as a direct retrieval of FDIC's unavailable Q3 quarterly fields. Mergers, reporting revisions and incomplete prior-quarter pairs are limitations to evaluate separately. Stock-ratio triggers do not depend on these flows.

Match certificate to the June FDIC BKCLASS; use the current FDIC institution record for new insured banks. Exclude OI/NC, as in the original study. Five new national trust banks absent from the June financial population are excluded on the NIC/OCC evidence in `new-trust-exclusions.json`. Paxos is the panel's sole unfiled reporter and is outside the insured-bank universe. Check that no June NC/OI institution has entered the current insured list; the November 11 check found none.

## Baselines and groups

FDIC BankFind financials endpoint `https://api.fdic.gov/banks/financials`, dates 20260630 and 20250930, plus 20260331 and 20250630 for average-loan flow denominators. Fields and exact queries are in each retrieval metadata file. Retrieve the whole date, limit 10000, and verify returned row count equals total. Q3's empty FDIC response is preserved as an availability observation, not substituted for the available FFIEC population.

Apply the original quarter-specific membership rules, excluding OI/NC:

- G1: assets [10,000,000,100,000,000] ($10–100 billion).
- G1x: G1, excluding banks with card loans greater than 25% of gross loans. Retain zero-card/zero-loan institutions; implementing exclusion as cards >0.25×loans reproduces the original count 122 for June.
- G1r: the G1 bounds multiplied by GDPDEF_t/133.411 (fixed 2026Q2 dollars).
- G2: assets [1,000,000,10,000,000) ($1–10 billion).

Coverage (%)=100×sum(allowance)/sum(noncurrent). Problem-loan share (%)=100×sum(noncurrent)/sum(gross loans). Quarterly annualized NCO/provision rates (%)=400×sum(quarterly flow)/sum((current+prior-quarter gross loans)/2), using current group members with complete pairs and reporting every exclusion. Never coerce missing fields to zero.

Quarterly/yearly trigger: current problem-loan share strictly greater than the relevant prior group's share AND current coverage strictly less than that prior group's coverage. Baselines are June 2026 and September 2025. Dynamic membership remains the original design; do not interpret group changes as a constant-bank panel.

## Historical comparison and individual placement

Freshly retrieve 1990Q1–2026Q2 (146 quarters) using the original FDIC asset query [500000,200000000] and fields CERT, REPDTE, BKCLASS, ASSET, LNATRES, NCLNLS, LNLSGR, LNCRCD. The query spans every nominal/real group used in this period. Apply the same group rules; GDPDEF comes from FRED's series, retrieved November 11. Preserve the fixed 133.411 reference. Calculate coverage for each group/date.

Compare Q3 coverage with this fixed historical set, separately all 146 quarters, pre-2020 (120 quarters), and 2020–2026Q2 (26 quarters). Percentile=100×number strictly lower/number of valid observations. Excluding the new Q3 point preserves the original comparison window. Reproduce June's original percentiles first; `historical-band-baseline-check.json` records that check. This does not re-estimate episode hit rates or predictive regressions.

Current bank comparison: assets ≥ $1 billion, gross loans≥10% of assets, positive noncurrent loans, reported allowance, insured-bank scope. Percentile is the proportion with strictly lower coverage. The original six certificate IDs are 33555,9396,6560,34742,58979,2270. A percentile is not a failure probability or predictive ranking.

## Integrity and completion

Verify panel/filed RSSD sets, uniqueness, reporting date and bank ID for every financial MDRM row, raw-source hashes, duplicate-code consistency, and extracted values against raw SDF. Free-text explanations can contain semicolons/newlines; they are not financial MDRM rows. Validate all eligible stock fields and each quarterly-flow pair. Reproduce June's group counts, coverage, problem-loan, charge-off and provision rates and the six previously retrieved Q3 ratios. Save the complete bank rows, aggregate numerators/denominators, member certificates, percentile lower counts and valid denominators.

Archive full raw sources and the manifest without credentials; preserve hashes of the uncompressed original content. Metadata hashes for reserialized FDIC JSON distinguish the original HTTP payload from the saved JSON file. An archive is complete only after its members and hashes have been verified. Intermediate validation files must be refreshed at download completion.

## Concentration diagnostic added after the full calculation

The large G2 move prompted a post-hoc contribution check, rather than an alteration to the registered group. Attribute the nominal G2 change in summed noncurrent loans to certificate 29566 using its current amount minus its June amount; retain the full group total change as denominator. Exclude that certificate at both dates for the separately labelled sensitivity, recomputing all sums and flow denominators. For the membership check, intersect the June and September G2 certificate sets and recompute both dates on those 874 banks. Exact figures are in `g2-sensitivity.json`. The fresh June SDF and Q3 explanatory field TEXT4769 are necessary context for this sensitivity; do not relay the concentration percentage without the cash-basis qualification.

## Preserved archive layout

`call-reports-sdf.tar.gz` contains the 4,267 original numbered `.sdf.gz` files; `manifest.jsonl.gz` preserves their timestamps, decoded-source hashes and fields. `history-json.tar.gz` contains the 146 historical `.json.gz` source files; `history/retrieval.jsonl` retains their query/hash records. Archive members and decompressed content hashes were checked before loose working copies were moved out of the repository. `archive-receipt.json` is the receipt. The separate June United Fidelity source remains directly available as `ufb-20260630.sdf.gz`.
