# EagleBank's last $167K: not closable from public sources, and too small to change any 003R result

**Date:** 2026-11-16 | **Mode:** Thesis | **Request:** REQ-DEWEY-20261022-003R residual / PROME DOCKET L1119 (review date today) | **Confidence:** High on the refetched filing cells and arithmetic; the exact bridge stays UNKNOWN. **State:** residual CLOSED as unresolvable from public sources; the UNKNOWN is carried, not removed.

## Key finding

**The exact EagleBank bridge cannot be built from any public source, and the missing piece cannot move any 003R result.** The bank has not amended its September 30 Call Report: today's refetch is byte-identical to the November 11 copy, last updated October 29. Eagle Bancorp has filed no amended 10-Q or 8-K since November 11, only ownership forms. The unexplained amount is $167K of $179.7M nonaccrual loans (0.09%) at September 30, and $135K (0.10%) at June 30. Removing it would lift EagleBank's coverage from 67.20% to 67.27%. Its Q3 percentile would stay at 12.4, 125 of 1,012 banks. [S1–S4]

This is descriptive only. Low coverage has no demonstrated standalone predictive value, and completing this residual is not a trading signal (Will, 2026-11-11 14:02 ET, carried on L1119).

## Evidence

All amounts $ thousands. Bank = EagleBank, RSSD 2652092.

| Check, 2026-11-16 | Result | Source |
|---|---|---|
| Fresh FFIEC download of the 9/30/2026 Call Report | SHA-256 `a4b07063…f991`, identical to the 11/11 copy; every row's last-update field 20261029 | S1 |
| Eagle Bancorp SEC filings since 11/11 | Two 13G/A, three Form 4, one Form 144; no 10-Q/A, 8-K or other accounting disclosure | S2 |
| Gap to explain: RC-N total nonaccrual less RC-R 5.c and 4.c | 135 (6/30), 167 (9/30), unchanged from 11/11 | S1; `output/2026-11-11_003R-historical-placement-and-bridge.md` §2 |
| Candidate cell: RC-R 5.a residential mortgage, 100% risk weight (RCONS443) | 104 (6/30), 76 (9/30) | S1 |
| Candidate cell: RC-N guaranteed portion (RCONK041) | 48 (6/30), 46 (9/30) | S1 |
| Both candidates together | 152 vs 135; 122 vs 167. **No fit at either date**, alone or combined | arithmetic |
| RC-N 1-to-4-family nonaccrual (5400 + C229 + C230) | 5,641 (6/30), 4,907 (9/30) | S1 |
| Coverage sensitivity, 9/30 (allowance 120,781) | 67.204% as filed; 67.267% with the 167 removed | S1, arithmetic |
| Coverage sensitivity, 6/30 (allowance 121,141) | 88.479% as filed; 88.566% with the 135 removed | S1, arithmetic |
| Q3 placement sensitivity | No other bank lies between 67.204% and 67.267%; percentile unchanged at 12.4 | S3 |

**What the new cell read adds.** RC-N reports 4,907 of one-to-four-family nonaccrual loans at September 30. Only 76 sits in RC-R's residential-mortgage 100% column. The rest of the nonaccrual book therefore appears to sit inside RC-R 5.c, even though the form text routes qualifying residential mortgage exposures elsewhere. The 46 guaranteed portion likewise has no visible home in 5.c's 0% and 20% columns. These are **scope questions about how the bank sorts loans between schedules, not a bridge**. No loan-level crosswalk is published. This read does not assert a reporting error.

## Counter-evidence and limits

- **"Immaterial" is a statement about this study only.** The $167K cannot change the 003R ratio, percentile or group triggers. It does not show that EagleBank's schedules are consistent, and the zero held-for-sale nonaccrual memo (RCONC226) is still unexplained beside $13.5M of held-for-sale nonaccrual in the RC-R regulatory-capital schedule.
- **Only two routes could close it:** an answer from the issuer, or a future amended or new filing that discloses the crosswalk. An issuer inquiry is an external send. That is Will's call and was not made. The next filing that could change these cells is the December 31 Call Report (due 2027-01-30) or the 2026 10-K. Neither is a registered watcher: Will's limit on L1119 rules out a new deadline, watcher or broader study.
- Do not assign the gap to fees, rounding, parent consolidation, principal-versus-carrying-value accounting or misstatement. None is evidenced.

## Source quality assessment

Primary regulatory filings and SEC records, retrieved today. The arithmetic is reproducible from saved files. The bridge is a disclosure gap, not a data-quality problem in the retrieved cells.

## References

- **S1 PRIMARY:** FFIEC CDR Public Web Service, RetrieveFacsimile, RSSD 2652092, periods 6/30/2026 and 9/30/2026, SDF. Saved copies `research/2026-11-11_003R-next-pass/egbn-6-30-2026.sdf` and `egbn-9-30-2026.sdf`. Today's refetch hash and the tested cells are in `research/2026-11-16_003R/bridge-recheck.json`.
- **S2 PRIMARY:** SEC EDGAR submissions, Eagle Bancorp CIK 1050441, https://data.sec.gov/submissions/CIK0001050441.json, read 2026-11-16 15:1x UTC.
- **S3 PRIMARY, derived:** `research/2026-11-11_003R-population/current-bank-rows.tsv`, with eligibility and percentile rules from that folder's `METHOD.md`.
- **S4:** prior reports `output/2026-11-11_003R-historical-placement-and-bridge.md`, `output/2026-11-11_003R-source-and-definition-check.md` and `output/2026-11-11_003R-full-population-refresh.md`.

## Process report

**Searches run:** no web search. One FFIEC facsimile pull, one SEC submissions read, cell arithmetic on saved filings, and one placement recount. The FFIEC "filers since date" call timed out; the facsimile's identical hash and last-update field answered the same question.
**Data gaps:** a loan-level or issuer-provided crosswalk between RC-N and RC-R. It does not exist publicly.
**Confidence:** High that the residual is immaterial to 003R. The cause remains UNKNOWN.
**Suggestions:** none. A watcher would breach Will's limit and is not proposed.

**Do-not-relay-as:** an exact EagleBank bridge, evidence of misstatement, a reason for the gap, a new EagleBank signal, or a trading signal.
