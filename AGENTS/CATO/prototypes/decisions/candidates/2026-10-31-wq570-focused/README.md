# Decisions WQ-570 focused repair

Candidate `1296e8bcb5ab3c8ea3e1c3750de05fa2f417b556`; tree `6cc6bf487809c6bfaf76d5b43fb60ef67ce99c8b`; previous reviewed candidate `a859a531d42f706cec3817c0a53907cbd49b0166`; base `3a9e489ba2acd3aa4e448f6c497caa14bca4ae82`. Author code and tests, not independent acceptance. Live installed app unchanged.

Will approved targeted repair, one focused independent recheck, and PROME installation/acceptance if it passes; chat confirmation stays required for every answer (WQ-571 A). Context: `PROME/inbox/2026-10-31_from-CATO_WQ570-571-approved.md`.

Use candidate.bundle in an isolated clone with base available; verify manifest SHA-256s, commit and tree. focused.patch is only the change from the previously reviewed candidate. candidate.patch is cumulative from base and includes only Decisions paths. Do not replace the live tree with a stale clone. No package applies itself.

## Focused closure conditions

- W-J: exactly one child commit with exactly the two selected event/packet paths and exact bytes, before publication and after fetch. Extra commit or same-commit third path refuses privately.
- W-J: reject unpinned executable hooks in source and remote base before enabling hooks. Repin claim_check.py and orphan_check.sh, plus existing transport helpers; preserve their runtime checks.
- W-I: a delayed push may land after timeout. Report unknown until fetched evidence establishes publication; retry does not duplicate.
- W-H: clean shared checkout can fast-forward. Busy/diverged checkout remains untouched, with exact heads, ahead/behind counts and owner recovery instructions. Recovery may still be necessary before later desk pushes.
- Partial older publication cannot satisfy the two-changed-path contract: preserve its words, disable that Send, save a replacement version and Send the new pair. This deliberate compatibility change is covered by Python and native browser checks.

Retain W-H through W-Q and all prior named residue in candidate release-review.json. W-L pending delivered answers and W-P staged/committed legacy exports must be reconciled by PROME before installation. No manual reply staging/deletion. One focused independent recheck, no broader second review.

Author evidence: 123 of 124 Python tests passed in the full run; one was blocked only by sandbox socket policy and then passed on its isolated rerun. Eight targeted counterexamples include a real delayed local push. Native Chrome: 38 assertions. No live reply was sent. Browser evidence pins 22 build dependencies. Original full review remains `PROME/reports/2026-10-31_decisions-batch-review-ledger.md`.
