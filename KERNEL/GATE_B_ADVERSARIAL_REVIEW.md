# Gate B Adversarial Review

**Checkpoint:** 11

**Date:** 2026-08-26

**Reviewed baseline:** `720b8e2e9`

**Scope:** Fixture-only. No live records, live submission paths, Gate C activation,
Git carve-out, or authority switch were inspected or exercised.

**Result:** REVIEW COMPLETE — BLOCKING FINDINGS — GATE B REMAINS IN PROGRESS

## Verification

Two independent readers inspected the approved contract, implementation, schemas,
tools, fixtures, and tests. Both independently ran:

```text
python3 -m unittest discover -s KERNEL/tests -p 'test*.py' -v
Ran 136 tests — OK

python3 -m compileall -q KERNEL/tools KERNEL/tests
PASS
```

The registered test inventory is machine-checkable with:

```text
rg -n '^    def test_' KERNEL/tests/test_*.py
```

Counts by module are: audit 18, core 11, lifecycle 18, locking 6, native 16,
permissions 11, planner 12, projection 19, render 9, schemas 1, and writer 15.
No tracked or top-level `EVALUATION/` subsystem exists.

## Approved fixture matrix reconciliation

`Component result` records what the current tests prove in isolation. `Complete
path` asks whether the expected result is produced by one acceptance path that
cannot omit a required check.

| # | Approved fixture and expected result | Principal test evidence | Component result | Complete path |
|---:|---|---|---|---|
| 1 | Valid native Question -> `QuestionRegistered`, question stream v1 | `test_file_backed_tsv_happy_path_ignores_mutable_checkout`; `test_valid_command_writes_canonical_accepted_event` | PASS | NOT PROVEN — native verification and writing are separate |
| 2 | Valid native binary Forecast -> `ForecastSubmitted`, forecast stream v1 | `test_file_backed_tsv_happy_path_ignores_mutable_checkout`; `test_valid_question_and_forecast_commands`; `test_valid_fixture_events_replay` | PASS | NOT PROVEN — native verification and writing are separate |
| 3 | Same command and bytes retried -> prior result, no event | `test_same_command_same_bytes_retry_returns_existing_result`; `test_same_rejected_command_retry_returns_existing_receipt` | PASS | NOT PROVEN as part of a complete acceptance path |
| 4 | Same command ID, different bytes -> `IDEMPOTENCY_KEY_REUSED` | `test_same_command_id_different_bytes_never_overwrites_prior_result` | PASS | NOT PROVEN as part of a complete acceptance path |
| 5 | Missing native commit/path/record -> durable native rejection | `test_missing_commit_fails_closed`; `test_missing_path_fails_closed`; `test_missing_record_fails_closed`; `test_rejected_receipt_retains_invalid_native_reference` | FAIL for the exact combined outcome — detection and caller-directed receipt writing are separate | NOT PROVEN |
| 6 | Shifted TSV row -> `NATIVE_RECORD_INVALID` | `test_shifted_row_is_invalid` | PASS for verifier | NOT PROVEN — no integrated durable rejection |
| 7 | Material term only in command -> `NATIVE_RECORD_MISMATCH` | `test_material_term_absent_from_native_records_fails_closed` | PASS for verifier | NOT PROVEN — no integrated durable rejection |
| 8 | Forecast and Question in one batch -> Question accepted first | `test_file_backed_forecast_follows_question_despite_input_order` | PASS for planner | NOT PROVEN — planner order is not enforced by acceptance |
| 9 | Missing dependency -> visible and unprocessed | `test_missing_dependency_remains_visible_and_unprocessed`; `test_missing_root_propagates_through_pending_chain` | PASS for planner | NOT PROVEN — `FixtureAcceptancePass.accept()` does not enforce readiness |
| 10 | Dependency cycle -> `DEPENDENCY_CYCLE` receipts | `test_cycle_members_and_downstream_command_have_distinct_reasons`; `test_planned_cycle_rejections_become_one_receipt_each` | PASS through caller-directed steps | NOT PROVEN as one acceptance path |
| 11 | Probability outside `[0,1]` -> `COMMAND_SCHEMA_INVALID` receipt | `test_probability_out_of_range_is_rejected`; generic durable invalid-command coverage in `test_invalid_command_is_durably_rejected_without_event` | PASS across components | NOT PROVEN by one targeted end-to-end fixture |
| 12 | Forecast on non-open Question -> `QUESTION_NOT_OPEN` | transition validation in `core.py`; lifecycle/writer state-mutation guards | PASS at component level | NOT PROVEN by one named end-to-end fixture |
| 13 | Stale expected version -> `STALE_EXPECTED_VERSION` | `test_stale_version_is_durably_rejected_without_state_mutation` | PASS | NOT PROVEN as part of a complete acceptance path |
| 14 | Unauthorized actor -> `PERMISSION_DENIED` | `test_unknown_actor_is_denied`; permission and custody-separation tests | PASS for permissions | NOT PROVEN — writer never invokes authorization |
| 15 | Threshold family -> `FAMILY_NOT_ENABLED` | `test_disabled_family_is_rejected` | PASS for validation | NOT PROVEN as part of a complete acceptance path |
| 16 | Amendment before close -> immutable new version, original retained | `test_full_resolution_path_and_correction_replay_deterministically` | PASS | NOT PROVEN as part of a complete acceptance path |
| 17 | Amendment after close -> `TRANSITION_FORBIDDEN` | `test_forecast_amendment_after_close_is_rejected`; deadline variant | PASS | NOT PROVEN as part of a complete acceptance path |
| 18 | Resolution without evidence -> `EVIDENCE_REQUIRED` | `test_resolution_without_evidence_is_durably_rejected` | PASS | NOT PROVEN as part of a complete acceptance path |
| 19 | Protected self-verification -> `PROTECTED_SELF_VERIFICATION` | `test_protected_self_verification_is_durably_rejected` | PASS | NOT PROVEN as part of a complete acceptance path |
| 20 | Competing children -> `CONFLICT`, omitted from ordinary views | `test_competing_children_quarantine_stream`; `test_conflict_is_visible_and_stream_is_omitted` | PASS | NOT PROVEN as part of a complete acceptance path |
| 21 | Delete `.rw/`, replay, render -> identical state and view bytes | `test_delete_rw_and_rebuild_reproduces_semantics_and_view_bytes` | PASS | NOT PROVEN as part of a complete acceptance path |
| 22 | Event modified/deleted -> blocking additions-only failure | `test_modified_event_is_blocking`; `test_deleted_receipt_is_blocking`; rename-away test | PASS | NOT PROVEN as part of a complete acceptance path |

After an explicit recount and correction round, both readers agree on all 22 rows
and every `NOT PROVEN` qualification above. Row 5's literal combined outcome is a
component-level failure: detection and durable rejection each exist, but nothing
connects them. Row 12 has component coverage for non-open lifecycle rejection, but
needs an exact fresh-`SubmitForecast`-against-closed-Question runner fixture. No
individual test assertion produced an unexpected result.

## Blocking finding: the checks are not an acceptance path

`FixtureAcceptancePass.accept()` delegates directly to
`FixtureResultWriter._accept_locked()`. That writer performs idempotency lookup,
command validation, lifecycle validation, event construction, and publication. It
does not call `authorize_command()` or `verify_native_references()`, and the pass
does not enforce membership in `plan.ready`.

Consequently, a schema-valid command can be durably accepted with an unauthorized
actor, an invalid native reference, or a waiting dependency if a caller invokes
the writer directly. Existing writer fixtures intentionally contain placeholder
native SHAs and hashes, yet produce accepted events because native verification is
outside the writer. The 136-test green result therefore proves the registered
components, not the approved end-to-end acceptance statement.

This is a hidden-check problem rather than an observed audit `UNKNOWN`: the audit
tests correctly prove that explicit `UNKNOWN` blocks. The absent runner means some
required checks are never instantiated, so they cannot report any status at all.

## Check perimeters and claim limits

| Check | Current perimeter | PASS proves | PASS does not prove | Failure/`UNKNOWN` behavior |
|---|---|---|---|---|
| Schema | Explicit supplied command/event/receipt | Registered syntax and strict fields | Truth, authorization, native fidelity, lifecycle legality | Findings fail closed; no aggregate CLI status |
| Permissions | Explicit command/path and injected registries | Actor, path, ownership, activity, and capabilities under cited policy | Competence or substantive independence beyond policy | Invalid inputs fail closed; no uniform CLI `UNKNOWN` |
| Native reference | Explicit command and injected synthetic Git repository | Exact selected bytes, hashes, and implemented material-term reconciliation | Research quality or trusted-history reachability | CLI prints perimeter and `PASS`/`EXCEPTION`; no `UNKNOWN` class |
| Planning | Explicit submission/result arrays | Deterministic completed/ready/waiting/rejection classification | That ready-only execution occurred | Missing dependency remains visible; no aggregate status |
| Replay/lifecycle | Explicit accepted events and command/history | Deterministic valid unconflicted state and legal transition result | Missing commands or permission/native validity | Findings fail closed; no aggregate status |
| Writer | Explicit command and injected fixture store | Atomic publication, exactly-one lookup, retries, writer-owned lifecycle checks | Permission, native verification, or planner readiness | Inventory defects block; no aggregate status |
| Locking | One injected local fixture workspace | Mutual exclusion in that workspace | Cross-clone serialization, authorization, or enclosed-work correctness | Boundary failures fail closed |
| Durable-result audit | Explicit submission/result inventories plus success claim | Exactly one result per supplied submission | Every native action was submitted or inventories are globally complete | Pre-success missing result is blocking `UNKNOWN`; post-success is `AUDIT_GAP` |
| Additions-only audit | Exact full-SHA synthetic history range and protected prefixes | No non-addition protected-path change in that range | Protection outside the range or threat model | Unresolved/unreadable history is blocking `UNKNOWN` |
| View reproduction | Explicit events and `render_as_of` | Four bytesets match renderer output for those events | Coverage of undisclosed repository state | Drift/input errors are exceptions; successful `--check` currently prints no perimeter or `PASS` |
| Projection | Explicit durable events, injected workspace, render time | Cache reconciles with replay, semantic state, and view bytes | Cache authority or freshness against undisclosed events | CLI prints perimeter and `PASS`/`EXCEPTION` |
| Test suite | 136 registered test methods | Every registered example behaved as asserted | That every required check ran for one command | Cannot represent skipped runtime checks as `UNKNOWN` |

The approved specification's generic claim-limit table remains correct. The
review found that executable disclosure is incomplete: audit, native verification,
and projection print perimeters/statuses, while successful `render --check` is
silent and the absent aggregate runner cannot print every required check and
refuse aggregate green on `UNKNOWN`.

## Required remediation before Gate B may close

Implement a fixture-only integrated acceptance runner that, under the existing
exclusive lock:

1. inventories explicit submissions and durable results;
2. plans dependencies and leaves waiting commands visible;
3. durably emits planned cycle/dependency rejections;
4. processes only `plan.ready`;
5. runs schema, permission, native-reference, and lifecycle checks;
6. converts registered failures into exactly one durable receipt;
7. publishes an event only after every required check passes;
8. prints every check's perimeter, status, and claim limits;
9. refuses aggregate `PASS` if a required check is `UNKNOWN`; and
10. renders only after every selected command has a durable result.

Minimum adversarial proof must show that invalid native references, unauthorized
actors, and waiting commands cannot reach accepted events; permission/native
failures produce one durable receipt; an injected `UNKNOWN` prevents aggregate
green; and a valid Question-plus-Forecast batch completes in dependency order.

Successful `render --check` must also disclose its perimeter, `PASS`, and claim
limit rather than exiting silently.

Trusted-history reachability beyond resolving the supplied full commit remains a
declared limitation and a Gate C concern. It was not hidden or expanded here.

## Gate decision

- Two-reader agreement on all 22 expected fixture outcomes: **PASS**, including
  the documented component-versus-complete-path qualifications.
- Complete registered fixture perimeter exercised: **PASS**.
- Review states check perimeters and limits: **PASS**.
- Executable checks uniformly state perimeters and limits: **FAIL**.
- No required check can be skipped beneath aggregate green: **FAIL**.
- Integrated acceptance-runner limitation explicitly dispositioned: **BLOCKING**.
- Checkpoint 11 review: **COMPLETE WITH BLOCKING FINDINGS**.
- Gate B: **IN PROGRESS**.
- Gate C: **NOT AUTHORIZED**.
