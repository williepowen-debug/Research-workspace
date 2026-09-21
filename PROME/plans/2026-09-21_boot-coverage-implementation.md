# Boot coverage implementation — bounded batch

Owner: PROME · 2026-09-21. Authorized by Will: “Lets implementy it now. We can break this into phases if the context is large”. Implements the revised proposal `77e2a9a28`, incorporating CATO `94fa87e5e`.

## Acceptance conditions written before implementation

1. Generated calendar freshness and handwritten prose coverage have separate results. A changed deadline or an ET-date advance with unchanged files invalidates the old generated block. Evaluation date/options come from the caller, never the old block.
2. Missing, duplicated, reversed or malformed markers, malformed/unreadable source, and inconsistent source/destination observations cannot pass. Checks are read-only. Snapshot identity and evaluation date are reported; a concurrent change detected before verdict yields cannot-certify.
3. Empty handwritten scope is identified as empty; unmatched dated prose is identified as not assessed. Neither result certifies generated content. Preserve the existing prose-check exit contract, surveying consumers before any change.
4. HANDOFF manual and declaration both say whole-file before budget integration. Existing byte findings remain; no rotation, relabeling or budget increase.
5. Read-cap output is consumed through its structured result. Invoke `--agent PROME --require-manifest` (no heuristic fallback); require a single valid agent/PROME result, process/result rc agreement, rc 0/1/2, assessed 0/1, and nonnegative required counts. Missing/malformed/mismatched output is UNKNOWN. Preserve size versus manifest findings and inability to assess. Rotation-tier findings remain advisory, and memory uses its own cap.
6. Capability disclosure is a manual/skill ordering change using the actual session tool inventory and existing states. Shell credential presence never establishes callable private tools or authentication. No new capability framework or launch authority.
7. No production boot rerun: its one-shot receipt already exists. Test integration in fixtures; production spot-checks invoke only independently read-only checks. No change to trading logic, BOARD semantics or other desks' files.

## Intended implementation

- `scripts/docket_view.py`: add `--check-generated` using the same renderer/options as `--write`, strict marker extraction, input identity checks before verdict, and explicit caller date (CLI default ET). Reuse docket parsing via an in-memory snapshot so the renderer cannot combine source revisions. Add a structured generated result and a prose coverage footer; retain prose rc semantics with truthful coverage wording.
- `scripts/read_cap_check.py`: additive agent-result fields for rotation-tier count and ACTIVE_DECISIONS budget trigger, derived from already-assessed rows and existing constants. Do not change existing rc or field meanings.
- `PROME/tools/prome_gate.py`: separate advisory generated and prose checks on boot and closeout. Add a narrowly scoped optional summary parser to the existing subprocess wrapper for these checks and structured read-cap reporting. Replace the fixed document budget list with the declared read-cap result; retain a separate memory-cap check. Preserve advisory/blocking classes and existing rc=2 meanings; do not equate cannot-certify with did-not-run.
- BOOT + both boot skill copies: whole-file HANDOFF scope and early actual-runtime capability disclosure. Update manifest provenance for that row without changing its mode. Add this batch's read-only reporting inputs to the existing read manifest if a genuinely new input is introduced.
- Tests: throwaway files/repositories; copied or imported code may be the candidate, but all state inputs and writes are fixtures. Focused regression cases and existing adjacent suites. Independent result reviewer must devise a counterexample.

## Proposed instruction text for plan review

BOOT step 1 replacement:

> Read `PROME/HANDOFF.md` in full using the bounded reader. The declared read mode is `whole`; the retention target does not limit read scope. Preserve any read-budget finding until the file is brought within its existing budget or a separately reviewed scoped read is adopted.

BOOT step 0 addition, before repository checks:

> At the opening report, disclose whether this actual session exposes private Artifact ruling access and native fleet `ListAgents`/`SendMessage`, using the existing AVAILABLE / UNAVAILABLE / UNKNOWN capability states. Cite the session's tool evidence; a shell probe cannot establish connector availability. Record missing capabilities and dependent skipped steps in the boot receipt. Recheck at point of use. Missing tools withhold dependent work only; thread-local collaboration tools do not establish fleet presence. Credential presence remains distinct from authentication.

Both boot skills' step 0 points to this added BOOT step rather than restating its rule. BOOT's header records this amendment. The READS HANDOFF note records that Will authorized whole-file scope in this batch and points to this plan; no broader attestation or read scope changes.

## Neighbour cases and review boundary

| Category | Cases |
|---|---|
| Ordinary | Fresh matching render; matching prose claim; read-cap assessed/clean; memory below trigger. |
| Overlap | Generated block plus prose on the same page; size and manifest findings together; rc=2 with assessed information still visible. |
| Wrong owner | Wrong-desk structured result refused; content outside calendar markers excluded from generated comparison but retained for prose coverage. |
| Missing information | Missing source/markers/result, duplicate keys/results, absent cap, unassessed counts, invalid date. |
| Concurrent activity | Source or destination changes during generated comparison; read-only checker never writes; parser rejects contradictory process/result receipts. |

No category is dismissed. A general concurrency framework or global shared-check contract rewrite is outside scope.

## Review and completion record

- Plan review: read-only `boot_plan_review` completed. B1 accepted: require the manifest explicitly and test absence; A1 accepted: dated citations to undated rows remain unassessed. Exact instruction amendments accepted. Reviewer confirmed no edits, no live checks and no outstanding work.
- IMPLEMENTED: separate generated freshness and handwritten coverage checks in boot and closeout; snapshot identity checks; strict markers and numeric date validation; structured read-cap summary requiring the manifest; separate auto-memory cap; whole-file HANDOFF scope; early capability disclosure through existing instructions. Added READS itself as a summary input. No live boot rerun or calendar regeneration.
- TESTED: `python3 -B -W error::ResourceWarning -m unittest PROME/tools/tests/test_boot_coverage.py PROME/tools/tests/test_prome_gate_gates.py PROME/tools/tests/test_capability_class_WQ239.py` passed 60 tests, including the independent review's counterexamples. Calendar selftest passed 24/24; read-cap selftest passed 86/86; validate_all selftest passed 38/38. Candidate files overlaid into disposable `gate_fixture.build()` repositories: boot and closeout both returned rc=0 and retained all four coverage rows. These fixture results are not a new production boot receipt.
- INDEPENDENTLY VERIFIED: `boot_result_review` independently inspected the implementation and ran the acceptance suite, plus its own malformed-date and identical-content atomic-replacement counterexamples. Replacement was correctly refused. One blocking gap was found: dotted, Unicode-dash and compact numeric dates became undated rows and passed freshness. Corrected by refusing non-ISO numeric-leading spans; reviewer cases plus a symbolic session-key positive control now pass. The final correction was retested by the implementer; it did not change instruction meaning and did not receive a third cold read. Both helpers delivered explicit closeout receipts, recorded in ORCH_LOG.
- STILL UNRESOLVED / declared residue (2026-09-21): HANDOFF remains over its existing budget. The separate `reads_check.py --agent PROME` reports the older manifest attestation as UNKNOWN because boot instructions have changed; this batch updates its own input declaration but does not renew a global completeness attestation. The read-cap result measures declared rows, not proof that the current declaration is complete. Private Artifact and native fleet tools remain unavailable in this Codex session; capability disclosure adds no tools or launch authority. Structural cleanup, shorter-log reads and incremental boot remain deferred. Snapshot checks certify the observations they compared, not a lock against changes after those observations. Existing unrelated gate findings are outside this batch.

## Read-only workspace observations and reproducibility

Called only `check_calendar_views()` and `check_byte_budgets()` with logs under `/tmp/prome-coverage-spotchecks-20260921`; neither advances BOARD or creates a boot receipt. Generated calendar was FRESH at the supplied ET date; handwritten dated scope was explicitly EMPTY with generated content excluded. Declared read-cap reported assessed rows and the HANDOFF budget finding; auto-memory was below its rotation trigger. These are dated observations, not a persistent health claim.

Integration experiment: export committed state with `PROME/tools/tests/gate_fixture.py::build`, overlay this batch's calendar/checker/gate/manual/manifest/skill candidate files, call `run_gate(fixture, mode)` for boot and closeout, assert all four new coverage rows and no traceback, then destroy only the allocated fixture. Logs: `/tmp/boot-coverage-fixture-boot.log` and `/tmp/boot-coverage-fixture-closeout.log`. Existing production BOARD cursor and foreign ARGUS baseline were not modified. The strict ResourceWarning run also exposed an unclosed manifest read in the exercised producer; its file handle now uses a context manager.
