# PROME disposition — acceptance PASS; installation proposed, not authorized

Candidate `5a2edeec2c7414c612478d59e32883bb527cef40`. One authorized independent reviewer returned PASS and explicit closeout. PROME consumed REPORT.md, independent-policy.log, independent-integration.log, regressions.log, historical.log and before/after/tested-copy integrity evidence. No blocking finding, candidate correction or additional review. Shared rejected candidate files and production schema-2 receipt/baseline hashes rechecked unchanged. L835 remains OPEN until Will explicitly authorizes closure.

Recommendation: approve a controlled installation of this exact candidate, subject to the migration prerequisites below. This is not installed and the acceptance report does not certify a new operational freeze. Known Git-inventory blind spots remain.

## Proposed cutover for separate approval

1. Pause the PROME closeout transition during cutover. Capture the actual deployment HEAD, exact source/document bytes, perimeter, baseline and live schema-2 receipt with hashes. Archive the historical receipt unchanged outside its live path. Preserve the rejected dirty candidates separately; stop on conflicting edits instead of overwriting or sweeping another owner's work.
2. Confirm deployment drift against the accepted candidate and baseline. Recheck supported policy syntax and the actual ARGUS Standard/Light consumer with intended inputs in isolation. Drift requiring implementation changes stops the cutover for a decision; no silent repair or baseline advance.
3. Apply the accepted exact-path source/document/test change only: policy, scope, contract and gate modules; ARGUS_CONTRACT.md and CLOSEOUT_PROCEDURES.md; the candidate's relevant tests and historical-test relocation. Do not merge the candidate branch wholesale into current master. Preserve unrelated current changes.
4. Expect the old schema-2 receipt to return CANNOT-EVALUATE (rc 2). Run a real `argus_scope.py --record-review --contract PLAN` with an explicit delivery/evidence/observation plan. Verify schema 3, argus-path-v1, ordered policy/source digest binding, FROZEN state and zero legacy review reuse.
5. Obtain the authorized actual audit of that new frozen content before mark-reviewed; acceptance of this software is not that audit. Then require the actual Standard ARGUS consumer, commit/ref/snapshot and delivery protections to pass. Only then resume ordinary Standard closeout. No production auditor was commissioned during this acceptance assignment; permission for that operational review must be covered by the installation approval or existing applicable audit authority.
6. Return the installation/verification receipts to Will. Do not close L835 without his explicit closure instruction.

## Failure / rollback

Stop on any failed prerequisite or check and preserve diagnostics. Prefer leaving Standard withheld. Any separately authorized reversal restores the exact captured pre-cutover source bytes through exact-path changes, preserving both receipts and immutable delivery IDs. Do not relabel schemas/digests/verdicts or force history. A restored schema-2 approval is historical evidence, never approval of post-cutover work; fresh review is required where content/policy/baseline/inventory changed. Restoring vulnerable old code is not a security correction.

Detailed accepted candidate procedure: `/home/willi/l835-phase2/PROME/proposals/2026-11-04_L835-phase2-MIGRATION.md` at the exact candidate commit. Production cutover/rollback are NOT EXECUTED.

## Evidence limits

259 current regressions, four independently written integration tests and the independent policy experiment passed. The 37 historical tests ran on old code only. Full unrelated Standard/Light closeout checks, actual deployment-input reconciliation, production migration and operational audit remain unperformed by design. Known self-hidden controls, local/global Git exclusions and index flags remain outside the visibility guarantee; skip-worktree was not separately replayed in this review. Test harness setup/quoting failures were preserved; they were corrected without touching candidate code.

Lifecycle: reviewer `/root/l835_acceptance` explicitly asked to close after delivery, then confirmed all evidence saved, no pending assignment work, no candidate/production changes, no further agents and no further task. Partial runtime capacity interruption was recovered in the same reviewer. This is a bounded task completion, not a full PROME boot or Standard closeout.

The existing orchestration reader identifies this reviewer as ASKED_RECEIPT. Its overall rc 1 includes pre-existing historical identity/inventory debt outside this bounded review; no fleet-wide lifecycle clearance is claimed or repair attempted.
