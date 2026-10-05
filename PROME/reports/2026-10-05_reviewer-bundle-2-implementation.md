# Reviewer bundle 2 — v4 implementation

Authority: Will's “okay go ahead and impement” after the v4 PASS assessment. Scope is the exact reviewed 13-file v4 bundle; no fleet launch, numerical cap selection, rule-row migration or laptop installation.

## Acceptance conditions, recorded before application

- Installed files match the reviewed v4 candidate exactly.
- Ordinary: bare boot does not advance BOARD; one-shot boot explicitly requests advancement. Valid orange candidates remain advisory, own red findings block, failed producer results cannot pass as candidate-only success.
- Overlap: changed-row cap handles edits and appends, grandfathered shrink, staged versus working-tree differences; parser preserves plus-bearing filenames while splitting recognized joined paths.
- Wrong owner: fleet findings remain advisory; no other desk's files are edited.
- Missing information: undeclared closeout inputs and missing consumer verdicts fail appropriately; unset cap stays visibly dormant at pre-commit/closeout, silent at save.
- Concurrent activity: index-aware hook tests cover alternate indexes/path-scoped commits; live concurrency exercise N/A because this task launches no agents and uses exact reviewed paths without Git index mutation.
- Run the seven bundle/regression suites on the installed code, verify hook executability and current hooksPath, and check whitespace/parity. Existing independent review is the v4 assessment; do not commission another review round.

## Implementation and validation receipt

- **IMPLEMENTED:** applied the exact consolidated v4 patch to the shared working tree. All 13 resulting files match the reviewed disposable v4 candidate byte-for-byte. No additional product changes.
- **TESTED:** all seven suites pass on the installed code with ResourceWarning treated as error: cap 19, declarations 16, locks 14, repeat boot 33, boot coverage 21, orchestration closeout 17, closeout simplification 23 — total 143. `git diff --check` passes; both closeout skill copies are identical.
- **INDEPENDENTLY VERIFIED:** prior v4 assessment records PROME's review of the external reviewer's implementation, including independently devised failed-exit probes through the real wrapper. Installation matches those reviewed bytes; no new independent read or stronger whole-system certification is claimed.
- **STILL UNRESOLVED / separate scope:** numerical cap choice, undated rule-row classification, laptop installation, candidate verification receipts and DAEDALUS C2 follow-up remain separate work. None blocks this authorized bundle installation.

Desktop `core.hooksPath` was already `scripts/githooks`. The updated installer succeeds without a configuration change; pre-commit, commit-msg and pre-push are executable. The new pre-commit hook is therefore discoverable at the next commit. A live `docket_row_cap.py --quiet` invocation returns rc 0 and the explicit not-configured notice; `scripts/harness_caps.env` was not changed. No real commit was used as a test.

Delivery state for this implementation turn: working-tree implementation complete; not committed or pushed, no hosted publication. This is not a full session closeout. No fleet spawned and no other desk files changed.
