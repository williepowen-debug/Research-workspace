# IDEA identity coverage — acceptance before edit

TERRY, October 25, 2026. Carried owner repair: STATUS/MEMORY October 24 names
`ledger_sweep.py` checks A/G/H as owed. Scope: include IDEA IDs in existing
identity readers, without changing state compatibility, structure tests, count
policy, scoring, approvals or trade conditions.

Acceptance:

1. An IDEA card/INDEX/TRADE_BOOK state disagreement is detected by A.
2. An IDEA structure disagreement is detected by G.
3. H reads the FULL IDEA ID from OPEN real paper rows; rejects old counts on
   that ID's own rows, and does not borrow counts from a cross-card mention.
4. H still excludes CLOSED and paper-lane rows; TRY and MGMT parsing still works.
5. Matching IDEA surfaces pass. Existing selftests pass. Any newly exposed live
   mismatch is reconciled against the card/source, never by widening COMPATIBLE.

Validation results are recorded in REPORT.md after the edit. These are author
tests, not independent acceptance by PROME.
