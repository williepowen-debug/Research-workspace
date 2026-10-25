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

## Review history and unreviewed residue — October 25 closeout

- Pre-edit conditions above were written by TERRY before the code edit in the
  same owner session. No independent plan reader was run for this IDEA change.
- Implementation `3be3db220`; author suite 111 assertions (10 added), plus live
  A–H clean. Full output `LEDGER_SELFTEST.txt`. No independent result reader or
  PROME acceptance of this IDEA delta is recorded at this closeout.
- Prior repair `fda97c793` was independently accepted October 14 by PROME at
  `PROME/reports/2026-10-14_TERRY-acceptance/disposition.json` (`92ae2b847`), owner
  uptake `dddfab918` / filing `7016acae0`. That was inbox/state/MGMT reader and Git
  repair scope. It does NOT accept the later IDEA change or certify missing
  historical review metadata.
- Author-tested delta: INDEX/TRADE_BOOK now include IDEA; H uses the complete
  shared TRY/MGMT/IDEA ID pattern (therefore MGMT count extraction is also in its
  perimeter). Existing state compatibility and count policy were not relaxed.
- Unreviewed residue: no completed independent counterexample result received for the new namespace/
  full-ID behavior; no claim of all possible legacy-ID joins or completeness of
  unregistered cards. Check C remains TRY-only. Unknown quote timestamps and
  broker-position discrepancies are outside this guard's acceptance.

At the 12:43 EDT owner check, PROME ORCH_LOG shows `terry-guard-review` in flight (`/root/terry_guard_review`, gpt-6.1-sol high). No result received by TERRY; no reviewer contact. PROME owns that acceptance step.
