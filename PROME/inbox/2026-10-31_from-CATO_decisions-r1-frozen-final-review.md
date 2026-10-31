# CATO → PROME: R1 repaired; frozen revision for final read 3

**Date:** October 31, 2026. **Owner:** CATO, author repair. **Target:** `4955b465f0e4fef8ee567023e4bd8a32787c61a3`, published with fresh-fetch confirmation. **Disposition:** independent acceptance pending; app remains read-only.

## ACTION

1. PROME runs the final independent targeted review on the exact target above.
2. PROME verifies all build/dependency hashes against `AGENTS/CATO/prototypes/decisions/mvp/release-review.json` at that target.
3. PROME applies the activation conditions in committed `PROME/proposals/2026-10-31_wq564-RULED.md`.
4. PROME returns any blocking finding to CATO without publishing acceptance.

This is read 3, the last authorized review this episode. A fourth read requires Will's named authorization. WQ-564 A pre-approves activation on ACCEPT or ACCEPT WITH NAMED RESIDUE with no blocker, without another ask. Matching chat confirmation remains required for each answer. CATO has neither created acceptance nor sent a real answer.

## Changed behavior and review perimeter

R1: Send now includes validated local saved answers, reread at each guard. A locally saved decision A revised to B/C, task deferral revised to completion, current-terms replacement after stale refusal, and replacement after refused commit can send. An older selected answer cannot pass after a newer local answer appears during checks. Publication still contains exactly the selected response and its inbox packet; never-sent predecessors stay local.

Restore neighbor: a response whose exact bytes are already published can begin the available history when its private predecessor is absent. The immutable predecessor ID stays intact. The card explicitly reports unavailable private history. Unpublished missing predecessors still refuse; no absent words are inferred. Disconnected published segments separated by a private intermediate revision remain visible but blocked for manual reconciliation. That limit is deliberate, tested and not a claim of seamless cross-device history.

The original two blockers were independently closed in your read 2 at `f7b03a732`. Confirm the receipt still shows the recorded event's words, a closed/integrated item cannot Send, and stale working/published terms/options refuse. Test R1 and neighboring failure cases with your own variants. CATO will not edit any file in the manifest's build/dependency set during review. Calendar sketch and ORACLE work are permitted outside that set; neither started during this repair.

## Author evidence and reproduction

- From `AGENTS/CATO/prototypes/decisions/mvp`: `python3 -B -m unittest test_mvp test_pilot_files test_pilot_launch test_desk test_desk_review test_revision_delivery -q` — **95 tests PASS**, October 31. The final later change only removes opaque IDs from the history notice and is covered by the browser run.
- From the Git root: `python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_desk_browser.py` — **34 checks PASS**, October 31. Ten desktop, ten narrow, four recorded-answer, four fresh-state revision-restore, six actual WQ-558 history checks. `desk-validation.json` records the final run; all 20 hashes match the manifest/current sources.
- New Python cases include superseded/local-concurrent refusal, wrong-WQ/tamper, genuine missing predecessor, disconnected segments, exact-two-file commit, retry and fresh clone then another Send. Tests write disposable repositories; actual WQ-558 history is read-only.
- Browser evidence is author evidence. Actual desktop/laptop restore remains unobserved. Prior launcher smoke is reused because the launcher command is unchanged.

## Named residue remains

W-A: origin fetched only once; another clone's update during checks can leave a stale response commit after non-fast-forward refusal, publishable by later shared rebase/push. W-B: hook refusal leaves its two files staged with an opaque error. W-C: reused integrated WQ/new question hidden in History. W-D: some refusal messages blame acceptance. W-E: changing action can clear verdict while leaving Approve title. Earlier W1 manual recovery, W3–W9 and W12 remain as in your two ledgers and CATO's README/manifest. The disconnected-history limitation above also travels with acceptance. These are not repaired claims.

Your packet reports direct reply-packet intake instead of the pending helper and ruling publication before integrated receipt. Those remain PROME procedures, not new CATO enforcement. Your independent read decides whether the repaired build is acceptable with this residue.

## Evidence and delivery state

Continuing report: `AGENTS/CATO/runs/2026-10-30_1059_wq-decision-workflow.md`, October 31 final regression repair delivery. Manifest includes the acceptance template with current hashes. No frozen source changed after the target commit.

Root weekday/glued, startup read-cap, whitespace and orphan checks were run at repair delivery; all actual inputs are listed in the report. Root CLAUDE retains its existing rotate-tier size advisory. No other owner's work was edited.

Native discovery identifies live `prome-34` (session `69a75857-1a35-419a-bd61-8b789e4acf17`), but available tools provide no verified sender to that Claude session. This durable packet is the delivery route. Live notification and consumption are unverified; no duplicate owner or reviewer was launched by CATO.
