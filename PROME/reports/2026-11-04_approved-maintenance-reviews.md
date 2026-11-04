# Approved maintenance — independent review receipts, 2026-11-04

Authorization: WQ-594–597; `PROME/proposals/2026-11-04_wq594-597-RULED.md`. All four helpers explicitly selected `gpt-6.1-sol` using Codex collaboration, read-only, no desk launches. Earlier Kimi history remains in `2026-11-04_kimi-maintenance-recovery/`; no prior verdict or missing lifecycle receipt is overwritten.

## L835 — further acceptance review, /root/l835_acceptance

**NOT ACCEPTED.** All 140 required tests passed (69 contract, 34 scope, 37 consumed-move), including the three recovered counterexample regressions. The independent reviewer executed a new blocker and stopped further investigation under WQ-597.

HIGH: `argus_contract.py` witness walker recognizes crossing wildcards only when `segment == '**'`, while `argus_scope._match()` recognizes `**` anywhere and emits `.*`. Embedded double-star therefore crosses directory separators in actual classification but not the witness walk. `_wholly_excluded()` incorrectly treats failure to construct a witness as proof of exclusion.

Executed counterexample:

```python
rules = [('root/a**/target', 'OWNED', 'cross-segment double-star'),
         ('root/**', 'EXCLUDED', 'fallback'),
         ('PROME/**', 'OWNED', 'delivery')]
parent = 'root/a/b'
# sc.classify('root/a/b/target', rules) == ('OWNED', 'cross-segment double-star')
# ac._ignore_witness(sc, rules[0][0], parent) is None
# ac._wholly_excluded(sc, parent, rules) is True
# ac.never_advisory(sc, 'root/a/b/.gitignore', rules) is False
```

A `target` ignore entry could hide the OWNED arrival without the intended guard. This violates acceptance condition 2 and reaches consumers in condition 5. Direct guard failure was executed; no further disposable-repository integration after the blocker. Resolution shape: witness reachability must respect the exact matcher language; missing witness cannot prove non-reachability. No repair or additional review was attempted.

Commands: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s PROME/tools/tests -p test_argus_contract.py`; equivalent patterns `test_argus_scope*.py` and `test_argus_r100_consumed_move_WQ289.py`. All pass. Counterexample imported `argus_scope` and `argus_contract` from `PROME/tools` and evaluated the four expressions above.

Reader inspected charter, root rules, completion/runtime mechanics, recovery README, all four recovered L835 reviewer texts, current dirty code/tests, acceptance history and both procedure descriptions. Incomplete `agent-ibdrgnnz` output remains unverified. Procedure drift: ARGUS_CONTRACT and live-fleet paragraph promise a broader guard than implementation provides; the older delivery paragraph also retains blanket pending-ignore/desk-commit wording inconsistent with the conditional subtree description. This is preserved L835 residue, not cured by L910's verbatim move.

Root consumed the NOT ACCEPTED verdict and requested closeout via `followup_task`: “Review consumed; NOT ACCEPTED and stop honored. Please close out now: confirm read-only work complete, no edits or outstanding processes, no further review. Return explicit closeout receipt.” Actual response: “Closeout receipt: read-only L835 review complete; NOT ACCEPTED delivered. No files edited, no Git writes, and no outstanding processes. No further review performed or planned.”

## L910 — further plan review, /root/l910_plan

**ACCEPTED** exact saved candidate pair for installation and the separately authorized result/execution review; not installed-file acceptance. No blockers.

Reader inspected charter, root instructions, runtime mechanics, recovery README/manifest, all three recovered L910 reports, plan/correction history and WQ-240 acceptance. Live source hash matches manifest; all 11 paragraphs match hashes, occur exactly once verbatim in cold candidate, and are absent verbatim from hot candidate. `measure.py` verified strict target; 51 overlay tests passed with expected-failure disabled only inside temporary test process. New sections have explicit hot pointers to actual cold headings; five old inventory entries survive. Commands, anchors, numbered order, commit → verify → push, wrapper --push prohibition, exact push receipt, L835 and L488 limitations survive.

Independent scenarios: intra-day Standard recovers steps 1–7, freeze, deferred audit, light gate and unreviewed wrapper path without falsely marking reviewed; an ARGUS correction to a DOCKET date recovers mandatory changed-portion review, regeneration/four checks, re-freeze, full gate rc=0, verify before push and baseline recording. rc=2 blocks progression. Existing pointer test covers only five old sections, so new headings/pointers were independently inspected. Earlier projection is explicitly superseded; no new duty/authority or semantic drift established. No edits or Git writes.

Root requested closeout via `followup_task` after consumption and installation. Actual response: “Closeout receipt: L910 plan review completed and delivered. Read-only throughout; no file or Git edits. No outstanding processes or remaining work in this review.”

## WQ-594–596 — pre-edit review, /root/docs_plan

**ACCEPTED**, no blocking or severity findings. Five-field assertions: (1) exact minus rows equal live source, 12 cells each, only column 10 changes INSTRUMENT → JUDGEMENT; (2) CARL non-MF household spillover and SHADE insurance routes match CREED Route Matrix; (3) separate pension edges remain unchanged and info-only in diagram and summary; (4) registration/handoff supply ID/date/owner/source to existing channel and PROME reconciles one docket home; (5) prospective date, next authorized owner session and explicit no-sweep/no-checker/no-launch limits match approval. No current prediction/docket row altered by the proposed diff. Future compliance not established by wording. Residue: installed four-file comparison required. WQ-597 outside this read.

Root requested closeout via `followup_task` after applying the exact proposal. Actual response: “Closeout receipt: read-only review complete. No edits or Git writes performed. No outstanding processes or further work.”

## Result/execution review

PENDING: `/root/maintenance_result`, one combined review counted once for L910 and once for each documentation episode. No additional L835 review.

## Final result/execution verdict — /root/maintenance_result

ACCEPTED separately for L910, WQ-594, WQ-595 and WQ-596. Installed manuals are byte-identical to saved candidates; 11 paragraph hashes/whitespace/newlines match; strict size target satisfied; marker removed; 23+28 live tests and table check pass. All four documentation files equal approved after-images, including only scannable cells on physical rows 16/20. All new and old heading pointers, command forms, freeze/review distinction and verify-before-push sequence recovered.

Rotated-content exercise recovered legacy consumed-move re-declaration at every freeze and separate-commit limitation until independently verified. Intra-day Standard recovers freeze, deferred audit, light gate and no false REVIEWED mark. Execution-order exercise recovered rendering before freeze, rc=2 stop, and obligation-date correction through regeneration, changed-portion review, full gate, verify, push and baseline. New counterexample: Light readers might skip content under the Standard/Heavy heading; hot every-actual-closeout and root-check pointers plus cold ANY-tier/EVERY-closeout text reject that shortcut. These were read-only document assertions, not an actual full fleet closeout.

L835 implementation was neither reviewed nor repaired in this result read; its known wording moved verbatim and acceptance was explicitly excluded. No semantic drift found in approved changes. Reviewer noted this receipt file absent at inspection; it was created during the concurrent receipt-writing leg and is now present, not a missing navigation target at delivery. No files/Git state written by reader.

Root requested explicit closeout through followup_task. Actual response: “Closeout receipt: read-only review complete. No edits or Git writes, no outstanding processes, and no further review performed. All four ACCEPTED verdicts stand; L835 remains NOT ACCEPTED and stopped.”

## Disposition and limits

IMPLEMENTED / TESTED / INDEPENDENTLY VERIFIED: WQ-594, WQ-595, WQ-596 and L910. STILL UNRESOLVED: L835, all unrelated desk registrations/grades/packets, and previous Kimi lifecycle receipt gaps. Code, contract and tests of the rejected L835 saved patch stay dirty and are excluded from delivery. The existing dirty CLOSEOUT L835 paragraph is preserved verbatim in the approved L910 rotation and is not newly accepted.

Root's first SOL-L835 spawn note mistakenly contained an unsupported exact launch timestamp; that field is withdrawn as UNKNOWN. Other initial helper rows lacked structured timestamps. Explicit asks/receipts above establish actual closeout, but the orchestration checker cannot retroactively certify missing original timestamps; these automated evidence gaps are disclosed, never fabricated. Related pre-existing Kimi ORCH rows are retained as original review history, with no inferred closure.
