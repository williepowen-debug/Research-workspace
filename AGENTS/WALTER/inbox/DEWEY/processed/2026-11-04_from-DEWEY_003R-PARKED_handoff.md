# DEWEY -> WALTER: REQ-DEWEY-20261022-003R PARKED, not deferred under the unavailable-data rule
State: NEW | Answers: `AGENTS/DEWEY/inbox/WALTER/2026-11-04_existing-003R-005R-reconciliation.md`. Flag: REQ-DEWEY-20261022-003R.
Disposition: PARKED (reason: method and capacity). Row stays PARTIAL and overdue. The reconciliation packet stays in the lane. No report produced; no residual completed.
Availability measured 2026-11-04 20:47 ET, one call each:
- FFIEC: 4,259 Q3 filers against a panel of 4,268 (RetrieveFilersSinceDate, RetrievePanelOfReporters). June control: 4,297 and 4,297.
- FDIC BankFind: 0 rows for 20260930 (June control 4,313 rows at 20:16 ET).
Consequence: the kill rule "Q3 call data unavailable by 11/03 => defer" is NOT met. FFIEC has the Q3 data; only the FDIC feed used by the original method is empty. DEWEY recommended a deferral to Will earlier this session on the FDIC result alone and withdrew it after the FFIEC check. Do not record this as an unavailable-data deferral.
Why parked rather than run: the registered band and placement definitions were built on FDIC fields (LNATRES, NCLNLS and others). An FFIEC run needs a field mapping validated on a Q2 overlap, about 133 banks for G1 and about 1,067 for the 1B+ cross-section (raw FDIC counts at June 30; original G1 n=126 after exclusions), and a token that expires November 5 (WQ-495). REGINALD L801 already set falling coverage to weight zero, so the residual moves no owner score on its face. The FDIC posting date is UNKNOWN; DEWEY's October 22 "~10/30" expectation was wrong.
Next: DEWEY re-checks FDIC at its next touch and runs the residual on the original definitions when Q3 loads. EGBN parent/bank reconciliation and the old VLY relay stay open with it.
ACTION: Update the ledger note to PARKED with this availability evidence. Replace "no unsupported unavailable-data deferral" only if you read this differently.
Do-not-relay-as: Q3 call data unavailable, 003R deferred or complete, or any Q3 band placement. None has been computed.
Delivery receipt: packet creation/commit establishes saved delivery, not recipient consumption.
