# WQ-638 author checks — frozen candidate, not independent verification

The candidate is based on `219752ac53a3c094fe37d541e94e6106e3163d06`. Apply `candidate.patch` at that revision in an isolated checkout; live mvp was not edited. `candidate-sha256.txt` identifies the executable candidate and owner contract.

- Existing desk, revision-delivery, intake-shape and brief suites: 44 tests passed. Initial attempt lacked the sparse-checkout decisions directory; those errors were missing test inputs, repaired by including the tracked directory and rerunning.
- New Option A tests: 10 passed (the first module invocation also discovered 27 imported DeskTests; 37 total passed). Two additional recovery/database-failure tests passed.
- Native Chrome fixture: eligible policy, recommended A with exact multiline conditions, no chat repeat notice, disapproval without selecting B, viewport fit all passed. First result extractor expected a hidden marker; Chrome itself reported all true; corrected fixture marker and reran successfully. No live responses were sent.
- Batch suite + Option A run: 30 passed, one old batch assertion errors because it expects the removed global `requires_chat_confirmation` key. The contract now reports eligibility per answer; this test needs updating. An additional loader error used nonexistent `test_pilot` module; correct legacy suite `test_pilot_files` passed 31 tests separately. These errors are disclosed, not counted as passes.
- Native Claude probe is combined with the one authorized Opus review. The isolated hook returned exit 2; model receipt of its reminder is for the reviewer to establish. No live PROME connection or idle wake is claimed from that exit code alone.

Tests are author-written unless the independent report says otherwise. Fixtures run only against disposable repositories. Same-login identity is not authenticated; scope/conflict/readback fields attest owner judgment, not transcript verification. WQ-639 source backfill/authoring changes are separate and unassigned.
