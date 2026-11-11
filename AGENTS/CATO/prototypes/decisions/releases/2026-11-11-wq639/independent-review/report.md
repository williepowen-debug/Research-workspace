# Independent WQ-639 candidate review — November 11, 2026

**Verdict: BLOCK, one medium-severity release-contract defect (IR-639-1).** Correct the replacement patch's missing queue precondition before claiming this candidate satisfies its stated acceptance conditions. This is a bounded authoring reliability defect, not an observed approval or chat-confirmation bypass. The runtime refused the resulting obsolete card in both reproductions. No broad re-audit is recommended.

## Scope and independence

Reviewed the release artifacts committed at `2128b00222`, extracted with `git show`, and independently reconstructed the patch against pinned base `9cc3bfd7bf8f5a9898f206ca8f8e537ea97a8315`. Verified patch SHA-256, all nine changed-file hashes and all 27 runtime-map entries. See `hash-verification.txt`. Scope: card authoring, opt-in /3 binding, save/current-source/send/restore and historical replay, integrated-receipt recommendation controls, and owner release requirements in README/WQ638/WQ639. I did not implement or repair the candidate.

Runtime: OpenAI Codex thread-local independent reviewer `/root/wq639_independent_review`; exact model identifier not separately exposed. Execution tools: shell/Python/Node and parent collaboration channel. Root and CATO instructions were explicitly read; no assumption that Claude files auto-loaded. Shared checkout observed on master at `e668ba3f09f70cd29ce9bd68cd0cb22e8194b1d0`, with concurrent CARL/LIQUID/REGINALD/PROME changes and staged LIQUID moves. No pull, live file edits, commits, acceptance changes, owner messages, fleet launches, installation or real answers. Review reconstruction, scripts and report are under `/tmp/cato-wq639-independent-review/`; inherited tests used disposable fake Git remotes and temporary state. The shared checkout's later HEAD is not the reviewed candidate.

## IR-639-1 — replacement patch silently accepts an obsolete queue preimage

**Severity: medium; blocking the stated candidate acceptance, not a runtime authority bypass.**

Location: reconstructed `AGENTS/CATO/prototypes/decisions/mvp/author_card.py`, especially lines 49–50 and 76–81. Existing pointer means `updated = row['row']`; patch generation skips an unchanged queue. The generated manifest records `queue_preimage_sha256`, but the documented application command is plain `git apply card.patch`, which never consumes that manifest.

Reproduction, independently devised:

1. Start with an existing published /1 options source and its queue pointer.
2. Prepare a /3 replacement using `prepare(..., replace_source=True)`.
3. Change the queue question from `A: one task` to `A: TEN tasks`, leaving the source untouched.
4. Apply the prepared patch with the exact documented `git apply` workflow.
5. Observe **exit 0** and replacement of the source with a /3 binding to the obsolete question. The changed queue survives, but the installed source no longer binds it.
6. Publish only in the disposable fixture: `current_source` refuses with `Options do not bind this exact queue row`.

A second independent case closes the row between preparation and application: **git apply again exits 0** and replaces its source. `current_source` refuses the closed row afterward. See `independent_tests.py` tests `test_migration_patch_after_question_change` and `test_replacement_after_closed_row`, the retained patches, and `independent-tests-final.txt`.

The normal fresh-card stale test does not cover this branch: it includes a queue hunk, so an edited target row causes patch rejection. Replacement has no queue hunk. This violates OWNER_GUIDE/WQ639 acceptance that applying a stale patch refuses, and the owner instructions that stale row/source changes refuse. It can leave the owner with an accepted patch and an unusable card requiring reconciliation. It does **not** overwrite the newer queue question or enable an obsolete answer; downstream refusal limits its severity.

**Correction:** make the supported application workflow enforce both relevant queue and source preimages before mutation, including existing-pointer replacement. A bounded extension of the existing authoring command is one option; do not introduce a recurring checker. Document the actual safe application command. An alternative design is acceptable if it preserves owner changes and guarantees the advertised refusal. The manifest hash alone is not enforcement.

**Owner and closure:** candidate implementer supplies a refreshed frozen candidate. Close IR-639-1 when an independent focused recheck shows existing-source replacement refuses after question change, closure, pointer swap or source change without altering either owner file; an unchanged replacement must still succeed. Preserve the current fresh-card stale-patch positive coverage. Recheck this branch and its updated hashes, not the whole application. Owner-controlled published review/acceptance and installation remain separate afterward.

## Verified behavior and nonblocking limits

- /3 operational Notes changes preserve saved choice and operator conditions through actual fake-repository delivery and restore; the immutable snapshot keeps the old published row. Closing the current row later blocks current use while historical validation remains valid.
- The canonical prefix hold declaration (`**⛔ waits: reviewer**`) blocks; a marker merely quoted later in Notes does not. This matches the existing queue parser contract. A malformed extra options-pointer marker refuses.
- A HEAD-only pointer swap cannot be concealed by putting the old queue bytes back into the worktree.
- Publishing a new source first leaves the untouched queue on its previous plain /1 display; an unpublished pointer subsequently added to the queue refuses. It does not silently activate unpublished choices.
- Material natural-language restrictions added **only** to Notes are intentionally not bound or shown as new /3 decision terms. Independently confirmed with `New restriction: do not proceed until Friday`. This is documented design, not a new parser defect: the owner must author material restrictions in question/options/context/conditions. Matching chat confirmation remains important. Do not describe this as automatic semantic protection against arbitrary Notes prose.
- Source-authoring records remain explicitly chat-required. No code inspected or tested enabled app-only authority or changed acceptance. Installation must keep `app_only_enabled: false` and matching chat confirmation; notification proof is still separate.
- Integrated-receipt recommendation function creates no controls; received/no-receipt cards retain controls, and read-only received controls remain disabled. Tested the actual candidate JavaScript function in Node with a minimal DOM constructor. This is function-level verification, not a browser rendering claim.

## Executed checks and limits

1. Independent reconstruction/hash verification: passed.
2. Own seven counterexample tests: passed as observations, including the two tests proving the defect. `python3 /tmp/cato-wq639-independent-review/independent_tests.py`; final log `independent-tests-final.txt`. Fixture setup reused the existing fake-repository helper; assertions and counterexamples are independent. Initial discovery also ran ten imported author tests (17 total); preserved separately in `independent-tests.txt`.
3. Focused existing suite: `python3 -m unittest -q test_wq639 test_wq638 test_wq641 test_desk test_revision_delivery`. **130 test executions: 127 passed, three errors, no assertion failures.** All three errors are the same imported real-desk test, repeated by unittest discovery: it calls `Repo(reader.ROOT)` on the reconstructed archive, which intentionally has no `.git`. This is an execution limitation, not a candidate regression and not a full-suite pass. Log: `focused-suite.txt`. Imported fixture duplication means 127 is not a count of unique scenarios.
4. Actual JavaScript recommendation-controls function: four state checks passed (`node ui-controls.js`, `ui-controls.txt`).

No native Chrome/Windows browser run, live pilot rendering, live wake proof, owner integration or ordinary-use benefit is independently claimed. I did not reinterpret the author's 239 Python/18 browser results as my own evidence. The bounded review has enough evidence for the stated BLOCK; broadening to live browser/history would not close IR-639-1.

This unedited report and reproducer are delivered to the parent for preservation/publication. No acceptance or installation authority is conveyed by this report.
