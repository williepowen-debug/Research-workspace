# WQ-639 independent focused recheck — November 11, 2026

**Verdict: PASS / nonblocking for repair-1. IR-639-1 is closed for these exact candidate bytes.** The supported application command now refuses stale queue/source inputs before changing either file. No further implementation is required for this finding. Owner-controlled published acceptance and installation remain separate; this report does not activate the app.

## Scope, identity and frozen evidence

I did not implement the original candidate or this repair. This was the parent-requested independent closure recheck, following Will's explicit authorization to repair IR-639-1. Runtime remains the OpenAI Codex thread-local reviewer `/root/wq639_independent_review`; exact model identifier not separately exposed. Root/CATO instructions and owner contracts loaded during the original review continue to apply. No new delegation, PROME message, live file mutation, acceptance change, installation, commit or real answer occurred.

Copied the supplied repair-1 package into `/tmp/cato-wq639-independent-recheck/` and independently reconstructed `candidate.patch` against base `9cc3bfd7bf8f5a9898f206ca8f8e537ea97a8315`. Verified the patch digest, all nine manifest file hashes and all 27 runtime map entries. Compared to the original independent reconstruction: only `author_card.py`, `test_wq639.py` and `WQ639.md` changed. The other reviewed runtime/UI/binding files retain their prior exact hashes. Evidence: `hash-verification.txt`, `scope-verification.txt`, copied `manifest.json` and `build-hashes.json`.

Exact relevant hashes:

- Patch: `9a4c3aeb7f32e38da86b8700e860bae16cebbf940c30385901875f92d44ef01d`
- `author_card.py`: `90a4aa5c1c33d4539b653a482631f4a1e37de2138f2b6021ff0822ddebce9385`
- `test_wq639.py`: `9b34c38429ae96f53fc21ab33b03b86446e11ba9bbe6209bffc31f171af7edb2`
- `WQ639.md`: `e51e5a04909cf87c145289b0125c0f3f42516253f7d3f98ae7fd59395ab0f612`

These are the reviewed artifact bytes, not a claim about a later shared HEAD or installed acceptance. The original BLOCK report and reproducer remain unchanged under `/tmp/cato-wq639-independent-review/`.

## IR-639-1 closure evidence

Original defect: replacing a source with an unchanged queue pointer emitted no queue precondition. Plain `git apply` accepted the replacement after the question changed or closed. Runtime refusal prevented an approval bypass but left an unusable authored card.

Repair inspected: preparation records the patch digest and both complete owner-file preimages. The documented `--apply PREPARED_DIRECTORY` path validates patch bytes, queue/source preimages and Git applicability before applying captured patch bytes through stdin. It rechecks preimages before actual application. Replacement patches also retain a no-op target-row hunk. The guide explicitly identifies `--apply` as supported and says raw `git apply` cannot enforce complete manifest preimages.

My independently devised tests verify:

- Existing-source replacement refuses changed question, closed row, removed row and swapped source pointer.
- Source wording edits and appended owner qualifications refuse.
- Appended queue text and changes to a different queue row refuse, demonstrating full-file preimage checking rather than only nearby hunk context.
- A deleted source or newly created source-path collision refuses.
- Modified patch bytes refuse.
- Each refusal preserves every regular non-Git fixture file, the index tree, HEAD and origin/master exactly as they stood immediately before the attempt.
- Unchanged replacement succeeds, leaves queue bytes unchanged, writes the expected source, and preserves unrelated staged work, the index tree, HEAD and origin/master.
- Fresh-card application still refuses a stale Notes edit; restoring the original preimage allows successful application without staging.
- Actual CLI preparation followed by CLI `--apply` succeeds without index changes.
- As a supplementary defense, raw replacement `git apply` now refuses the original changed-question case without changing files. Raw application is still not the supported full-preimage workflow.

**Finding status: CLOSED.** No newly discovered blocking or nonblocking implementation defect within this repair perimeter. No broad re-audit or recurring checker is recommended.

## Executed verification and limits

- `python3 /tmp/cato-wq639-independent-recheck/recheck.py`: **10 independent tests passed**, including multiple closure cases within parameterized loops. Reproducer: `recheck.py`; log: `recheck-tests.txt`. Reused existing disposable fixture setup, but devised the cases/assertions independently.
- `python3 -m unittest -q test_wq639.CardTests`: **13 existing focused tests passed**. Log: `focused-author-tests.txt`. This independently reruns existing author tests; it is distinct from the new independent counterexamples and from the copied author's `author-tests.txt`.
- All execution completed without test errors or sandbox escalation. Only disposable Git repositories/local remotes and state were changed. All recheck artifacts and fixtures were under the assigned `/tmp/cato-wq639-independent-recheck/` area.

This workflow assumes the documented exclusive owner write custody during application. It does not lock out arbitrary concurrent writers; my result is not a cross-process atomicity claim. The manifest/patch integrity check is not authentication against a malicious same-account actor who changes both. Neither limitation is a new authority grant or an undisclosed release promise.

The unchanged /3 binding/UI/history evidence and limits from the original review remain applicable; no new browser, live pilot, live notification, deployment or ordinary-use claim is made. In particular, /3 operational Notes still require owner discipline: material restrictions belong in bound question/options/context/conditions. Installation must preserve `app_only_enabled: false`, matching chat confirmation, exact accepted hashes and a published review reference. The prior broad-suite archive errors were not rerun or reclassified; this focused suite avoids those unrelated real-repository assumptions.

Next owner action: preserve/publish this unedited review with the refreshed package, then perform the existing owner-controlled acceptance/installation step when authorized. The independent review's bounded stopping point is reached.
