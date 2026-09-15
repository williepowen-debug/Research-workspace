# PROME second-eyes review — September 15, 2026

Initial review boundary: `3c6f9759d4f69b83528bac139d53782eae4ba745`. Working tree initially clean. Review is scoped to continuity and selected assurance tools, not market facts or the entire fleet.

## Acceptance conditions for the test-fixture repair (before editing)

The ARGUS scope suite must run Git discovery and content reads against each temporary repository, including its nested subject-invariance repositories. Its ROOT override must be restored after each test. Preserve production repository anchoring and all existing behavioral assertions. The suite must pass with ResourceWarning treated as an error; repository operational state must remain untouched.

Neighbour cases: ordinary = existing scope scenarios; overlap and wrong owner = existing fixture assertions; missing information = corrupt/missing/orphaned baseline cases; concurrency = no parallel threads in this suite, but nested repository selection and cleanup must remain correct. No production control or review authority changes.

## Findings and results

Additional acceptance condition, recorded before the gate-test entrypoint edit: direct execution and unittest discovery must run the same existing tests. Move only the entrypoint, preserving all assertions. Ordinary = both invocation styles; overlap = classes defined before/after the former entrypoint; wrong owner/missing data/concurrency = N/A for an entrypoint move in pure fixture tests.

### 1. P2 — ARGUS regression suite broke when production Git reads were correctly anchored

**VERIFIED; test-only repair implemented and tested.** `PROME/tools/argus_scope.py:43–53` uses `cwd=ROOT`, introduced by `7a9e1cfd7` to fix a real cross-checkout defect. The existing test fixture changed only process cwd. Its nested subject-invariance fixture had the same omission. Consequently the test's temporary commit IDs were looked up in the live repository.

Verification command: `PYTHONDONTWRITEBYTECODE=1 python3 -W error::ResourceWarning PROME/tools/tests/test_argus_scope.py`.

Observed before repair: 28 tests, 2 failures and 27 errors (subtests account for the additional errors). Observed after repair: 28 tests pass. The repair patches the imported module's ROOT to each temporary repository, restores it with unittest cleanup, and also handles the nested repository case. Production anchoring is unchanged. An additional in-process run of the nested-repository and committed-plus-pending cases asserted ROOT and process cwd were restored afterward: PASS.

Consequence: the prior passing-suite receipts no longer establish that this suite runs successfully against current code. This finding does not establish a production ARGUS failure. The original run performed erroneous live Git reads, but git status confirmed no operational writes.

### 2. P2 — Direct gate-suite execution silently omitted aged-wait tests

**VERIFIED; test-only repair implemented and tested.** In `PROME/tools/tests/test_prome_gate_gates.py`, `unittest.main()` ran before `AgedWaitsTests` was defined. Direct execution returned success after four tests; module discovery returned success after seven. The omitted cases cover dark-owner aging, dated-deliverable exclusion, and unknown liveness.

Commands, both with `PYTHONDONTWRITEBYTECODE=1` and `-W error::ResourceWarning`:

```text
python3 PROME/tools/tests/test_prome_gate_gates.py
python3 -m unittest PROME/tools/tests/test_prome_gate_gates.py
```

Moved the entrypoint below all classes. Both invocations now run seven passing tests. All original assertions are unchanged. The documented module invocation already ran the full set; this finding is specifically about direct invocation, not evidence the omitted behaviors are broken.

### 3. P2 — A completed specification correction still appears as owed on the boot path

**VERIFIED at repository artifacts; corrected on Will's subsequent approval.** At the initial review boundary, `PROME/STATUS.md:28` said F4 was NOT closed because the specification listed four refuse tokens. `PROME/DOCKET.tsv:247` explicitly closes F4 on September 14 while retaining F3/F8 and RED's F1 review as outstanding. `KERNEL/OUTCOME_VECTOR_PROJECTION_SPEC_DRAFT.md` section 9 enumerates the seven refuse tokens, including both previously omitted tokens. The old STATUS statement was demonstrably stale, not merely a difference in wording.

Verification: read the exact STATUS row, physical docket row 247, and the specification's section 4/section 9 token lists. Commands: `sed -n '28p' PROME/STATUS.md`, `sed -n '247p' PROME/DOCKET.tsv`, and `rg -n 'F4|VECTOR_LABEL_UNMAPPED|VECTOR_RULED_BYTES_MISMATCH' KERNEL/OUTCOME_VECTOR_PROJECTION_SPEC_DRAFT.md`.

Consequence: a fresh session can recommission a completed correction. Proposed replacement for the STATUS row:

> L247 remaining specification/review work — see DOCKET L247 for current disposition. F4 is closed; F3/F8 and RED's F1 recheck remain owed. No code before the required review passes.

On Will's approval to complete steps 1–2 and prepare step 3, STATUS was reconciled to that disposition and its maintenance stamp scoped to this correction. F3 source_masses/normalization, F8 carrier reconciliation, RED's F1 v0.3 recheck and the no-code-before-review restriction remain explicit. No docket or Kernel change was needed.

### 4. Bloat assessment — existing ownership rules are not holding in practice

**VERIFIED document mismatch; INFERRED operational cost.** `PROME/CLOSEOUT.md` assigns current operational state to STATUS and explicitly excludes session accounts, market narrative and history. Yet `PROME/STATUS.md:21` contains an extended market-analysis/retraction history, and line 24 explicitly calls its account of the session's errors the record. CLOSEOUT also assigns concise navigation to HANDOFF; its September 14 entries contain extended recaps and repeated error narratives.

This is not a finding that every guard can be deleted. The verified problem is that the designated document roles are not consistently followed; the inferred cost is repeated reading and reconciliation of historical claims on the startup path. Adding another rule saying the same thing would not resolve that mismatch.

Recommendation for discussion: a bounded STATUS/HANDOFF simplification using the already-approved roles. Preserve live guards at the point where the decision is made; keep session accounts in the existing daily log; replace duplicated task dispositions with source pointers. Review a concrete before/after sample before broad changes. No restructuring performed in this pass.

## What held up, and review limits

- The current WQ-ledger regression suite passes 24 tests: `PYTHONDONTWRITEBYTECODE=1 python3 -W error::ResourceWarning PROME/tools/tests/test_wq_ledger_L336.py`. Its intentional duplicate-rejection diagnostic is expected fixture output, not a live ledger failure.
- September 14 L335/L394 completion reports distinguish implemented scope from calibration, historical hosted-data and publication limits. Those reports were read; this pass does not independently recertify L394 or hosted delivery.
- The production ARGUS cwd fix is worth retaining. The repaired tests now exercise that anchored implementation instead of accidentally depending on the previous cwd behavior.
- Full operational boot/closeout was not run; these commands include stateful work outside this review. No market data, live desk coverage or hosted artifact was certified.
- Initial review changed only the two test files and this report. Approved follow-through adds the bounded STATUS correction and [proposed continuity sample](2026-09-15_prome_continuity_sample.md). No agent packets, Kernel artifacts, trade decisions or hosted pages were changed. Commit/delivery evidence is in Git history and the session's final receipt.

## Completion states

**IMPLEMENTED:** two bounded test repairs and the approved L247 continuity correction. **TESTED:** ARGUS 28 passing, gate tests seven via both entrypoints, ledger 24 passing, plus ROOT/cwd restoration checks; STATUS compared against the docket and spec, with only its target row and maintenance header changed. **INDEPENDENTLY VERIFIED:** original defects were reproduced as an external reviewer; my repairs have not received a second independent review. **STILL UNRESOLVED:** broader continuity simplification; the before/after sample is proposed only. No new operating rule, blocking gate or recurring audit was added.
