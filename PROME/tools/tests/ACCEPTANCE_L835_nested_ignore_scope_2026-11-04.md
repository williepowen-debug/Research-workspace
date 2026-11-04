# ACCEPTANCE CONDITIONS — L835 nested ignore-file scope

**Written before edits, 2026-11-04.** Scope: `argus_contract.never_advisory()`, its tests, and the two existing procedure descriptions. No live-fleet rule, threshold, route, spawning behavior or operational authority changes.

1. **Root is unconditional.** Root `.gitignore` / `.gitattributes` remain guarded regardless of any unrelated EXCLUDED dotfile row.
2. **Guard every nested ignore file whose subtree can contain a non-EXCLUDED arrival under the pinned rules.** A segment-wise pattern walk must handle `*`, `?` and `**`, use the pinned first-match classification, and never rely on a single synthetic direct-child probe. Missing rules remain strict.
3. **Named covers:** `.claude/.gitignore` above OWNED agents/skills; `AGENTS/.gitignore` and `AGENTS/BROCK/.gitignore` above SHARED/PROME-evidenced inbox arrivals; `scripts/.gitignore` with registered SHARED files below it. Each is never advisory.
4. **Common exclusions stay advisory:** a nested ignore file under `AGENTS/BROCK/research/` and under the explicitly EXCLUDED `PROME/inbox/` subtree. A broad later OWNED rule must not override an earlier EXCLUDED subtree row.
5. **Committed route closes too.** The read-3 `.claude` case and read-2 CE-N2 committed-under-a-desk-subject case are ported as tests; `attributed_by_commit`, working-tree and `--ref`/`--snapshot` consumers all remain strict for those ignore files.
6. **No weakening elsewhere.** Existing `test_argus_contract.py`, `test_argus_scope.py`, `test_argus_scope_evidence.py`, and `test_argus_r100_consumed_move_WQ289.py` pass. Production behavior changes only in nested ignore-file classification and its consumers, not in spawn or owner logic.
7. **Procedure truth:** CLOSEOUT and ARGUS_CONTRACT describe the actual pinned-subtree scope, without claiming that every nested research ignore file blocks. The known `.git/info/exclude` blind spot and any live-fleet policy question remain declared, not silently repaired.
8. **Independent acceptance:** one reviewer who did not write the fix devises and runs at least one counterexample. Author tests alone do not close L835.

## Neighbours considered

- **Ordinary:** existing root and owned-lane guards remain strict.
- **Overlap:** committed+pending and committed-only nested ignore changes are covered, including the --ref form.
- **Wrong owner:** a desk-root ignore file above a PROME packet cannot hide behind desk authorship.
- **Missing information:** no pinned rules means guarded; an unreachable pattern cannot silently disable the root guard.
- **Concurrent activity:** all tests use disposable repositories; no live tree writes or shared-index mutations outside fixtures.

## Completion note

IMPLEMENTED + TESTED; STILL UNRESOLVED — independent acceptance is missing. The earlier PENDING text described acceptance-writing time only.

Crash recovery 2026-11-04: three completed Kimi reviews returned NOT ACCEPTED (selective witness exclusion; first-match ordering; deeper UNATTRIBUTED descendants). The code contains corrections and regression tests for all three. The fourth attempted review stopped at provider quota, with partial output explicitly unverified; its safety-sweep text is not an ACCEPT verdict. There is no recovered named exception to the three-read ceiling. Preserve the original responses in `PROME/reports/2026-11-04_kimi-maintenance-recovery/`.

Codex reran the existing suites: 69 contract tests and 71 neighbouring tests pass. This is recovery validation, not another independent acceptance round. No production-code change was made by Codex. Operational acceptance and delivery of this patch remain WITHHELD pending the bounded further-review decision WQ-597; the known baseline defect is not claimed fixed. No live-fleet policy change is approved.

## WQ-597 further acceptance — 2026-11-04

NOT ACCEPTED by independent Codex gpt-6.1-sol `/root/l835_acceptance`. Existing 140 tests pass, but embedded `**` in `root/a**/target` matches the OWNED descendant `root/a/b/target` while the witness walker falsely proves the parent wholly EXCLUDED. The nested ignore file becomes advisory. Repair STOPPED on this blocker; no further correction or review authorized by WQ-597. Saved dirty implementation remains uncommitted and WITHHELD; do not rely on its claimed scope. Prior history preserved. Full evidence and explicit reviewer closeout receipt: `PROME/reports/2026-11-04_approved-maintenance-reviews.md`.

## One bounded correction authorized — 2026-11-04

Will, verbatim: "accept the four completed repairs, leave L835 explicitly open, and authorize one carefully bounded correction—not another general maintenance sweep." WQ-594–596 and L910 accepted by Will; L835 remains OPEN. This authorizes one correction of the embedded-double-star exclusion proof, not another review round or broad sweep.

Acceptance before correction: the reported OWNED descendant and prefix/suffix embedded-double-star variants must keep the parent ignore/attributes file guarded. An earlier complete EXCLUDED subtree remains advisory under first-match rules. Existing common research/inbox exclusions and all recovered counterexamples must retain their tests. Conservative guard on an unsupported earlier non-EXCLUDED pattern is permitted as uncertainty, never claimed exact reachability. No matcher API, perimeter, policy, manual or owner changes. Test in a disposable overlay; preserve live dirty patch; save candidate as non-operational evidence until independently accepted. Ordinary/overlap/wrong-owner/missing/concurrent categories remain covered by existing suites; the new tests target matcher-language uncertainty and rule ordering.

Verification result: 71 contract + 34 scope + 37 consumed-move tests = 142 PASS in disposable overlay. Original failure reproduced before correction (6 failing subtests). IMPLEMENTED IN CANDIDATE / TESTED; NOT INDEPENDENTLY VERIFIED; L835 OPEN and operational patch WITHHELD. Live dirty implementation/tests/contract left unchanged. No further review round.

## Named saved-candidate acceptance review — authorized 2026-11-04

Will authorizes exactly one independent acceptance review of the saved candidate, requiring embedded-** before/after reproduction, all prior counterexamples, overlapping wildcard/first-match false-negative checks, genuinely excluded-directory closeout behavior, and a disposable repository with the actual consumer. Stop on a blocking finding; no automatic repair cycle. On PASS return an installation recommendation only. On FAIL pause incremental correction and reconsider the approach; no redesign or installation authorized. Reviewer: Codex gpt-6.1-sol `/root/l835_saved_acceptance`, read-only. Earlier review history and NOT ACCEPTED verdict remain intact.

Saved-candidate review verdict: NOT ACCEPTED. Latest false negative eliminated and five targeted regressions pass; unrelated `other/a**/target` before `root/** EXCLUDED` wrongly guards `root/.gitignore`, and actual `verify_review()` changes rc 0 to rc 1 solely on that arrival. Requirement 4 fails. STOP honored; incremental corrections PAUSED, L835 OPEN, candidate NOT INSTALLED. Further tests unperformed under stop rule; full result and explicit closeout receipt: `PROME/reports/2026-11-04_L835-saved-candidate-acceptance.md`. No further repair or reviewer.
