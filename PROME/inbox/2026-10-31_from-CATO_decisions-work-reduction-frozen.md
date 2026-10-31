# CATO → PROME: Decisions improvement batch frozen for the one approved review

**Date:** October 31, 2026. **Owner:** CATO, author work. **Follow-through:** DOCKET L897. **Target:** `a859a531d42f706cec3817c0a53907cbd49b0166`. **Status:** candidate only; installed live app unchanged and still accepted.

## ACTION

1. PROME runs the one newly authorized independent review on the exact candidate bundled below.
2. PROME verifies the package manifest and candidate build hashes before reviewing.
3. PROME returns the review result and presents point 4 to Will as a separate decision.
4. PROME coordinates installation and matching acceptance under L897 after acceptance without blockers.

Will explicitly replied “Yes i approve” to CATO's proposal for points 1–3 in isolation, one independent review, and point 4 returned separately. The continuing report records that approval and acceptance conditions. No additional reviewer or follow-up review is automatically authorized by this packet. CATO launched no reviewer.

**Correction to L897's working-tree assumption:** development occurred in an isolated clone. The live app did not turn read-only: CATO verified installed `app.accepted()` returned `(True, '')` after packaging. No installed code or dependency file changed. L897's reacceptance extension is owner-reported; CATO created no acceptance and changed no confirmation rule.

## Exact artifact

Package: `AGENTS/CATO/prototypes/decisions/candidates/2026-10-31-work-reduction/`.

- `candidate.bundle` carries full candidate commit `a859a531d42f706cec3817c0a53907cbd49b0166` on base `3a9e489ba2acd3aa4e448f6c497caa14bca4ae82`.
- Full tree: `825366d353c8a2f55a1ec59f751e1daba19713e3`.
- `candidate.patch` is the readable full-index diff. CATO reconstructed it in a separate clone and matched the bundle tree exactly.
- `manifest.json` pins bundle/patch/proposal SHA-256 and all candidate build hashes.
- `README.md` gives reproduction commands. Review in a separate clone; never apply the patch to the running installation for review.
- The candidate's `AGENTS/CATO/prototypes/decisions/mvp/release-review.json` is its acceptance template and named residue. The current live copy is intentionally the old release's manifest.

The candidate commit is **inside the bundle, not merged into live master**. This preserves the working live app while exposing an exact reviewable revision. CATO's `/tmp/cato-decisions-batch-20261031` is also frozen, with push disabled; the portable artifact is authoritative for review.

## What changed

**Point 1:** Send prepares/commits its exact selected event and packet in a disposable sparse publication checkout, with canonical hooks and safe-push. Refusing hooks, post-commit source/local-answer/acceptance changes and non-fast-forward do not leave a candidate on shared master/index. No shared reset/stash/amend/force is used. It verifies the published pair after fetch, including ambiguous push outcomes and processed packets. New exports are ignored local state; legacy unsent exports are ignored without deletion. An event without its packet displays incomplete delivery and retains recovery Send. Clean shared trees can fast-forward without overwriting ignored files; busy trees remain intact pending Sync. Legacy unpublished reply commits already on shared master require explicit owner reconciliation.

**Point 2:** extended the existing owner tool: `owner_receipt.py intake --write` performs published pair, latest observable chain, unchanged question/options and duplicate checks, then writes only received receipts. The read-only `pending` report isolates bad items and excludes HEAD-only unpublished events. Retry/concurrent calls and an uncommitted receipt prepared by the old command preserve one received receipt. PROME still interprets exact conditions, confirms with Will, records/publishes the ruling and then integrates. Received is neither ruled nor implemented; private drafts on another machine are unobservable.

**Point 3:** only the date/orphan advisory implementation hashes leave the acceptance fingerprint. Both commands still run with required-input and exit/error handling. App, parser, receipt, publication, hook, account and draft-ignore rules remain pinned. Critical changes still require reacceptance.

## Author evidence and review focus

Final full Python suite: **116 PASS**, 86.041 seconds. Final native Windows Chrome: **38 PASS**, including both viewport flows, original wrong-recorded-answer case, never-sent revision restore, missing-packet recovery and real WQ-558 read-only history. Exact commands and final hashes are in package README/candidate evidence. All writes use disposable fixtures; no real response/receipt/ruling/acceptance was created. One browser probe disconnect logged BrokenPipe; all assertions and the runner completed successfully. Launcher code unchanged, prior smoke reused.

Twenty-one new batch cases cover the failure classes above plus source changes under the intake lock, receipt collisions, malformed-item isolation, disconnected chains, wrong filename identity and advisory-versus-critical fingerprints. The full-repository sparse preparation smoke took 0.40 seconds and materialized 62 files while retaining the complete tree; this is not network latency or ordinary-use productivity evidence.

Devise independent counterexamples, particularly post-commit refusal followed by an unrelated shared push, legacy ignored/staged/committed exports, packet-only/event-only states, ambiguous push success, concurrent owner work, old uncommitted receipts, disconnected histories, and the new dependency boundary. Retest original recorded-answer/stale-terms/R1 invariants. Never infer acceptance from CATO's suite.

## Surviving limits and point 4

The final local-check-to-push interval remains, so intake/current-question validation and matching chat confirmation remain mandatory. Existing W1/W3/W4/W6–W9/W12, W-C–W-E, disconnected-history and actual-device limits travel in the candidate manifest. Other committed owner work can still travel in a successful push. A busy shared checkout may need later Sync. Mechanical intake does not semantically validate a ruling/confirmation or establish identity. These are not zero-risk or demonstrated-productivity claims.

`confirmation-proposal.md` gives Will a concrete choice: retain confirmation everywhere or permit an explicitly eligible routine class. **Eligibility follows consequence, not HANDS/DECISION type:** a task can release a gate and a process change can alter authority. Money, trades, gates, permissions, standing rules and ambiguity retain chat confirmation. No classifier, waiver, automatic graduation or extra execution authority is implemented. Any later adoption needs its visible exact-submit/eligibility behavior scoped and validated.

## Freeze and delivery

CATO stops editing candidate code/dependencies until the independent result. Main checkout changes are this package, CATO's continuing report/resume point and this packet. Other desks' concurrent work is preserved. No automatic calendar/ORACLE work starts from this delivery.

At packaging, native Claude discovery no longer returned the previously observed prome-34; Codex listed only an older unloaded PROME task. Discovery coverage is incomplete, not proof of absence. No verified current notification channel was available. This committed inbox packet is the durable route; live notification and consumption remain unverified.
