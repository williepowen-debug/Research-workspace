# Reviewer bundle 2, v4 — PROME assessment

**Disposition: PASS for the reviewed implementation scope; ready for adoption.** The last reproduced fail-open defect is fixed. This is a review disposition, not an application of the patch or adoption of a numerical cap.

Compared the supplied consolidated v4 patch with v3. Only the consumer parser and its declaration tests changed, as represented in the addendum. `git apply --check` passes against the current shared checkout. Applied only to disposable export `/tmp/prome-review2-v4-sv4zkt6g`; production implementation unchanged, no fleet launched.

## Verification

- Declaration suite: 16 PASS.
- Repeat-boot suite: 33 PASS.
- Boot-coverage suite: 21 PASS.
- All 70 tests ran with ResourceWarning treated as error. The other four suites remain supported by their v3 results, not represented as rerun under v4.
- Independently exercised the actual `run_script()` wrapper with injected subprocess output/status, rather than replacing that wrapper as the supplied new test does. Candidate-only output at rc 1 and rc 2 now yields UNKNOWN and a failed own-directory blocking row. Consumer gate aggregate rc is 1 in both cases.
- Candidate-only output at rc 0 remains advisory, aggregate rc 0. A stale footer at rc 1 still blocks. Clean output at rc 0 passes. Missing verdict at rc 2 blocks as UNKNOWN.
- Six independent case receipts: `/tmp/prome-review2-v4-sv4zkt6g/v4-probes.json`.

No further revision requested for this bounded fix. This does not assert exhaustive validation of arbitrary malformed output: v4 implements the minimum correction requested, ensuring nonzero exit without a stale footer cannot pass. A positive stale verdict remains blocking regardless of exit code.

## Separate follow-up scope

The cap value remains unset and requires Will's choice. Classification of the proposed undated rule-class rows is separate semantic work. Laptop hook installation requires checking that host after its next pull. Candidate verification receipts and the DAEDALUS C2 issue remain separate improvements. Applicable mirror-map checks still require their separate canonical invocation; fleet advisory findings do not discharge packet obligations automatically.

Prior assessments remain as review history; v4 supersedes their hold recommendation for the reviewed bundle. No hooks installed, policy activated, packet sent, commit made or production patch applied during this review.
