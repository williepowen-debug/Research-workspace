# Decisions work-reduction candidate

Will approved points 1–3 and one independent review in CATO chat on October 31, 2026. This package contains the frozen replacement; the installed app remains at its previously accepted code. Nothing here enables app-only answers or replaces live acceptance.

- Candidate commit: `a859a531d42f706cec3817c0a53907cbd49b0166`.
- Base commit: `3a9e489ba2acd3aa4e448f6c497caa14bca4ae82`.
- Complete candidate tree: `825366d353c8a2f55a1ec59f751e1daba19713e3`.
- `manifest.json`: artifact SHA-256 values, critical build hashes and author check counts.
- `candidate.bundle`: portable Git commit with the base as prerequisite.
- `candidate.patch`: readable full-index patch; independently reconstructed tree equals the bundle tree.
- `confirmation-proposal.md`: the separate point 4 choice for Will after review; no waiver implemented.

The candidate commit is carried **inside this bundle**, not merged into live master. Do not look for changed app files at the packaging commit. Review in a separate clone, never by applying this patch to the running installation.

## Reproduce the frozen target

From the workspace root, use a new temporary clone and its own index. Replace the example destination if already present:

```sh
git clone --no-hardlinks --no-checkout /home/willi/Research-workspace /tmp/decisions-independent-review
git -C /tmp/decisions-independent-review fetch /home/willi/Research-workspace/AGENTS/CATO/prototypes/decisions/candidates/2026-10-31-work-reduction/candidate.bundle refs/heads/master:refs/heads/cato-candidate
git -C /tmp/decisions-independent-review switch cato-candidate
git -C /tmp/decisions-independent-review remote set-url --push origin DISABLED-REVIEW-ONLY
```

Check HEAD equals the candidate commit. The candidate's `mvp/release-review.json` is the review/acceptance template, and its README documents the changed behavior and limits. CATO's original development clone at `/tmp/cato-decisions-batch-20261031` is also frozen, with its remote push target disabled. Both are author artifacts; an independent reviewer must devise its own cases.

## Author evidence

From the candidate `AGENTS/CATO/prototypes/decisions/mvp` directory:

```sh
python3 -B -m unittest test_mvp test_pilot_files test_pilot_launch test_desk test_desk_review test_revision_delivery test_batch -q
```

Result: **116 PASS**, 86.041 seconds. From the candidate root:

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_desk_browser.py
```

Result: **38 PASS**: 10 desktop, 10 narrow, four recorded-answer, four revision-restore, four missing-packet recovery, six real WQ-558 read-only history. `desk-validation.json` in the candidate contains matching final hashes. A Windows HTTP probe disconnected once and the server logged BrokenPipe; all browser assertions completed and the runner exited zero. No real answer, owner receipt, ruling or acceptance was written. Prior launcher smoke is reused because the launcher is unchanged.

The full-repository temporary publication preparation took 0.40 seconds in one local read-only smoke check, materializing 62 files while preserving the entire Git tree. This excludes network push latency and is not an ordinary-use productivity result.

## What to review

A refused post-commit Send must never leave its candidate on shared master or in the shared index. Unsent words must stay out of ordinary staging; delivery must require the exact packet and event. Include old unignored/staged/committed exports, concurrent source or answer changes, refusing hooks, non-fast-forward, push success followed by timeout, and foreign staged work. No shared-HEAD rollback, stash or forced push is used. A legacy unpublished reply commit is refused for owner reconciliation.

Owner intake must reject stale/superseded/ambiguous replies, isolate malformed items, preserve an already prepared uncommitted owner receipt, and avoid duplicate received receipts on retries. It cannot see private drafts on another computer. Received is not ruled or implemented. Canonical ruling interpretation and matching chat confirmation remain PROME's duties.

Advisory date/orphan code changes no longer change the acceptance hash; their commands, required input checks and failure handling remain. Parser, receipt, publication, hook and account safeguards remain fingerprinted. Original blockers and the revised-never-sent-answer flow must still hold. Full named residue is in the candidate manifest/README, including the final check-to-push interval, disconnected histories and legacy receipt-semantic limits.

## Installation boundary

This package does not install itself. PROME owns the newly authorized single independent review and returns the result plus the point 4 proposal. Installation must be coordinated with current saved drafts and the live owner checkout; use the reviewed candidate bytes and a matching acceptance, preserving event/receipt history. Do not merge the stale base's owner records or apply an entire foreign tree over live master. Old saved answers may need re-review against the updated presentation before Send. Code changes without matching acceptance make replies read-only by design.
