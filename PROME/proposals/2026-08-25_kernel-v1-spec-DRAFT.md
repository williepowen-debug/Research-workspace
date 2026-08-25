# Kernel v1 Operational Shadow Specification

**Date:** 2026-08-25

**Status:** DRAFT — specification review only; no `KERNEL/` creation, shadow activation, or authority switch authorized

**Design authority:** `PROME/proposals/2026-08-24_kernel-membrane-design-DRAFT.md`

**Operator and policy authority:** Will

**Version 1 acceptance custodian:** PROME, exercising deterministic custody only

---

## 1. Purpose

Version 1 is a small operational shadow registry for prospective `Question`, `Forecast`, and `Resolution` records. Actor identity and Evidence provenance support those objects. Native prediction ledgers remain authoritative throughout shadow operation.

The first implementation increment proves one binary-probability path from an exact native record through command submission, deterministic acceptance or rejection, immutable shadow history, replay, and registered operator views.

The kernel validates administrative facts. It does not judge research quality, alter submitted judgments, infer missing analytical terms, execute trades, own messaging, or establish forecasting superiority.

## 2. Authority and non-goals

### 2.1 Shadow authority

- Every accepted v1 event has `authority_mode: SHADOW`.
- Every accepted Question, Forecast, and Resolution event cites an exact `native_ref` unless the active command definition explicitly represents kernel administration rather than a native research fact.
- Native state wins whenever native and shadow state disagree.
- A discrepancy is rendered as an exception; it is never silently repaired.
- Shadow events are never promoted or copied into canonical history. A later authority ruling must name the first canonical records and effective time.

### 2.2 Custody boundary

PROME may:

- process pending commands in deterministic order;
- accept a command that satisfies the active schema and policy;
- reject a command using a registered reason code;
- write accepted events, rejected receipts, and registered views;
- report and route exceptions.

PROME may not:

- edit a submitted payload;
- supply missing research terms;
- change a forecast value;
- choose or reinterpret an outcome;
- verify a protected outcome solely because it is custodian;
- waive policy without a Will-authorized override;
- rewrite or delete accepted history.

### 2.3 Explicit non-goals

The first slice excludes:

- `TrialManifest`, cohorts, arms, baselines, sample targets, and stopping rules;
- generalized historical conversion or fleet-wide adapters;
- messaging transport or a messaging bridge;
- durable obligations, jobs, scheduling, or retries across time;
- evidence graphs, claim ontologies, or source-quality judgments;
- hosted services, workflow engines, or cryptographic signing;
- agent-status generation, dashboards, or broad repository canon generation;
- canonical forecast authority.

## 3. First executable boundary

The first increment enables only `BINARY_PROBABILITY`. `THRESHOLD_CROSSING` and `CONDITIONAL` are registered v1 family names but remain disabled until their payload, activation, and scoring contracts have separately approved fixtures and tests. Attempts to use them return `FAMILY_NOT_ENABLED`.

The first increment implements:

1. `RegisterQuestion` → `QuestionRegistered`
2. `SubmitForecast` → `ForecastSubmitted`
3. duplicate-command idempotency
4. durable rejection receipts
5. per-stream chaining and conflict detection
6. deterministic replay
7. all four registered shadow views

Before live shadow activation, the implementation must also support:

1. `AmendForecast` → `ForecastAmended`
2. `CloseQuestion` → `QuestionClosed`
3. `ProposeResolution` → `ResolutionProposed`
4. `VerifyResolution` → `ResolutionVerified`
5. `DisputeResolution` → `ResolutionDisputed`
6. `CorrectResolution` → `ResolutionCorrected`
7. stale-version rejection and competing-child quarantine
8. prospective schema and policy upgrades

## 4. Identifiers and time

### 4.1 Identifier forms

All identifiers are uppercase ASCII and globally unique within their namespace.

| Entity | Form |
|---|---|
| Command | `CMD-<ACTOR>-<YYYYMMDDTHHMMSSffffffZ>-<12HEX>` |
| Event | `EVT-<YYYYMMDDTHHMMSSffffffZ>-<16HEX>` |
| Question | `Q-<OWNER>-<YYYYMMDD>-<12HEX>` |
| Forecast series | `F-<FORECASTER>-<QUESTION_12HEX>-<12HEX>` |
| Resolution | `R-<QUESTION_12HEX>-<12HEX>` |
| Evidence | `E-<12HEX>` |
| Question stream | `QS-<question_id>` |
| Forecast stream | `FS-<forecast_id>` |

`<12HEX>` and `<16HEX>` are uppercase hexadecimal prefixes of SHA-256 over the canonical input described below. IDs do not depend on Git commit order or filenames.

- `command_id`: actor-supplied and derived from the canonical command body excluding `command_id` and `submitted_at`, plus a caller-supplied nonce. Reusing an ID with different content is `IDEMPOTENCY_KEY_REUSED`.
- `question_id`, `forecast_id`, and `resolution_id`: allocated during command preparation and validated by the acceptor. The canonical preimage includes object type, actor, native reference, and a caller nonce.
- `event_id`: custodian-assigned from the canonical accepted command hash, recorded timestamp, stream ID, and stream version.
- An existing identifier with different canonical content is `IDENTIFIER_COLLISION` and fails closed.

The implementation may use a library ULID internally only if the serialized public identifier forms and deterministic collision behavior above remain unchanged. No random-only identifier is accepted without collision checking.

### 4.2 Time contract

- All serialized timestamps use UTC RFC 3339 with six fractional digits and `Z`.
- `submitted_at` is actor-supplied.
- `recorded_at` is assigned by the acceptance clock.
- `effective_at` is optional actor-supplied domain time and never establishes stream order.
- Tests inject a clock; production uses a single captured UTC instant per processed command.
- Event semantic order is `stream_version`, never timestamp, filename, or Git order.
- The acceptor rejects an invalid timestamp as `INVALID_TIMESTAMP` and a future `information_as_of` later than `submitted_at` as `INVALID_INFORMATION_CUTOFF`.

## 5. Canonical serialization and hashing

Canonical JSON is UTF-8, object keys sorted lexicographically, no insignificant whitespace, no NaN or Infinity, and one trailing newline in files. Hashes use SHA-256 over the canonical bytes without the trailing newline.

Schemas use `additionalProperties: false`. Unknown fields fail closed. Free-form analytical prose belongs in a cited native artifact, not an event payload.

## 6. Version contract

Version identifiers are immutable strings:

```text
schema_version: kernel.schema.1
policy_version: kernel.policy.1
writer_version: kernel.writer.1
renderer_version: kernel.renderer.1
```

Rules:

1. Every command declares the schema and policy versions against which it was prepared.
2. Every receipt records the versions used to evaluate it.
3. Every accepted event records schema, policy, writer, and authority versions.
4. A schema or policy change receives a new immutable identifier and applies prospectively.
5. Replay dispatches using each historical event's recorded schema and policy semantics.
6. A replay adapter may translate an old serialized shape into an internal representation only if tests prove that it preserves the original meaning. It may not rewrite the event file.
7. An unavailable historical version is `UNSUPPORTED_HISTORICAL_VERSION` and makes the affected stream an exception, never a guessed state.
8. Policy rollback creates a new forward version; identifiers are never reused.

## 7. Actor registry and permissions

Actor records contain only:

```text
actor_id
actor_type                 # HUMAN | AGENT | SERVICE
canonical_name
source_ref                 # pointer to existing roster/authority canon
active_from
active_until               # optional
```

The kernel does not mirror activity class, domain ownership, or the fleet roster.

Initial capabilities:

```text
question.register
question.close_own
forecast.submit_own
forecast.amend_own
resolution.propose
resolution.verify
resolution.dispute
command.accept
policy.override
```

Will owns `policy.override`. PROME holds `command.accept`. Acceptance custody grants no research, resolution, or verification capability.

## 8. Command contract

Every command file contains:

```text
schema_version
policy_version
command_id
command_type
actor_id
submitted_at
expected_version
target_stream_id
correlation_id             # optional
caused_by                  # optional command or event ID
payload
native_ref
```

`expected_version` is a non-negative integer. A creation command uses `0`. The next accepted event receives `stream_version = expected_version + 1`.

Commands are immutable after submission. A correction is a new command ID. The command filename is `<command_id>.json` and must equal the embedded ID.

### 8.1 Submission path

Ordinary agents submit only under their owned path:

```text
AGENTS/<CANONICAL_NAME>/outbox/kernel/pending/<command_id>.json
```

The path actor and `actor_id` must map to the same canonical agent unless policy explicitly permits a service submission. A mismatch is `ACTOR_PATH_MISMATCH`.

The acceptor never edits or deletes a submitted file. Processed state is derived from the durable accepted event or rejected receipt matching its `command_id`.

### 8.2 Acceptance order

One acceptance pass:

1. acquires `.rw/locks/command.lock` exclusively;
2. inventories pending commands;
3. sorts by canonical `submitted_at`, then `command_id`;
4. processes each command against state replayed from accepted events;
5. atomically writes exactly one event or one rejected receipt;
6. fsyncs and renames from a temporary file in the destination directory;
7. releases the lock;
8. renders views only after all selected commands have durable results.

A crash before atomic rename leaves no result. A retry safely processes the still-pending request. A crash after rename returns the existing matching result.

## 9. Event and receipt contract

### 9.1 Accepted event envelope

```text
schema_version
policy_version
writer_version
event_id
event_type
command_id
command_hash
command_result             # ACCEPTED
stream_id
stream_version
previous_event_id          # null only at version 1
object_id
object_type                # QUESTION | FORECAST | RESOLUTION
actor_id
writer_id
submitted_at
recorded_at
effective_at               # optional
correlation_id             # optional
caused_by                  # optional
authority_mode             # SHADOW
native_ref
evidence_refs
payload
```

Accepted event path:

```text
KERNEL/shadow/events/YYYY/MM/<event_id>.json
```

The date partition comes from `recorded_at` and has no semantic authority.

### 9.2 Rejected receipt

```text
schema_version
policy_version
writer_version
command_id
command_hash
command_result             # REJECTED
actor_id
writer_id
submitted_at
recorded_at
reason_code
reason_detail              # bounded administrative detail; no invented judgment
target_stream_id
expected_version
native_ref                 # retained when supplied
```

Rejected receipt path:

```text
KERNEL/audit/commands/YYYY/MM/<command_id>.json
```

A rejection never advances a stream version and never emits a domain event.

### 9.3 Durable-result invariant

For every processed `command_id`, exactly one durable result exists:

- one accepted event; or
- one rejected receipt.

Both is `AUDIT_DUPLICATE_RESULT`; neither after a reported successful acceptance pass is `AUDIT_GAP`.

## 10. Native-reference contract

Every native research reference contains:

```text
repository                 # fixed value: williepowen-debug/Research-workspace
source_commit              # full 40-character commit SHA
path                       # repository-relative, normalized, no traversal
locator_type               # TSV_RECORD_ID | JSON_POINTER | TEXT_ANCHOR
locator
content_sha256
raw_record_sha256
```

Rules:

1. `source_commit` must exist and be reachable from the configured trusted history.
2. `path` must exist at that commit.
3. The importer reads the blob from Git at `source_commit`, not the mutable working tree.
4. `TSV_RECORD_ID` identifies exactly one non-comment data row by the detected header's declared ID column and preserves the raw line bytes.
5. `JSON_POINTER` must select exactly one JSON value.
6. `TEXT_ANCHOR` is allowed only for fixture development until its uniqueness and normalization rules are separately approved; live shadow activation does not permit it.
7. `content_sha256` hashes the complete source blob. `raw_record_sha256` hashes the exact selected record bytes.
8. Missing, duplicate, shifted, width-invalid, ambiguous, or hash-mismatched records fail closed.
9. The shadow payload must be a faithful structured interpretation of the cited record. Fields absent from the native record must be supplied as explicit command metadata and identified as such by schema; they may not be presented as native facts.

The first real native example must be chosen only after fixture validation. No cohort selection is required; one record is sufficient for the activation demonstration.

## 11. Object contracts

### 11.1 Question

`RegisterQuestion.payload` requires:

```text
question_id
owner_actor_id
claim
forecast_family            # BINARY_PROBABILITY in first increment
opens_at
closes_at                  # exact time in first increment
resolver_anchor_type       # FIXED_DEADLINE | EXPECTED_EVENT | DECISION_DATE
resolution_condition
resolution_rule
resolution_sources         # non-empty evidence-source descriptors
fallback_resolution_source # optional
ambiguity_rule
annulment_rules            # enumerated reason codes
resolver_actor_id
independent_verifier_actor_id  # required when policy marks protected
negative_search_procedure      # required when NO may depend on absence
```

The first increment permits exact `closes_at`; condition-only close support may follow before activation if required by the selected real record.

Question stream: `QS-<question_id>`. Question and Resolution events share this stream.

### 11.2 Forecast

`SubmitForecast.payload` requires:

```text
forecast_id
question_id
forecaster_actor_id
forecast_version           # 1 on submission
information_as_of
probability                # decimal number, 0 through 1 inclusive
rationale_ref
evidence_refs
intervention_stage         # INITIAL | POST_CHALLENGE | POST_SYNTHESIS | FINAL_CUTOFF
decision_consequence       # optional reference or bounded administrative label
```

The question must be `OPEN`. The forecaster and command actor must match unless policy explicitly grants proxy submission. `information_as_of <= submitted_at <= closes_at`.

Forecast stream: `FS-<forecast_id>`. One forecast series belongs to one actor and one question. An amendment increments `forecast_version` by exactly one and preserves every earlier value.

### 11.3 Resolution

`ProposeResolution.payload` requires:

```text
resolution_id
question_id
outcome_value              # YES | NO | AMBIGUOUS | ANNULLED
proposed_by
resolution_evidence_refs   # non-empty except registered ANNULLED cases
negative_search_attempt    # required for an absence-based NO
annulment_reason           # required only for ANNULLED
```

`VerifyResolution.payload` requires:

```text
resolution_id
question_id
verified_outcome_value
verified_by
verification_evidence_refs
disposition                # VERIFY | REJECT
```

A protected outcome cannot be verified by the forecast owner, resolution proposer, or acceptance custodian unless policy explicitly names a permitted role combination and Will approves it prospectively.

## 12. Lifecycle and stream rules

### 12.1 Question states

```text
OPEN -> CLOSED -> RESOLUTION_PROPOSED -> FINAL
                         |-> DISPUTED -> RESOLUTION_PROPOSED
OPEN|CLOSED|RESOLUTION_PROPOSED|DISPUTED -> FINAL(ANNULLED)
```

`STUCK` and `CONFLICT` are exception conditions, not successful lifecycle states.

Binding rules:

1. Question terms may be amended only while `OPEN` and before the first forecast.
2. After a forecast exists, a material question change requires a new question with `supersedes_question_id`.
3. Forecast-value and question-definition changes are distinct events.
4. Binary outcomes are never retrospectively labeled `PARTIAL`.
5. Conditional questions use their registered activation rule; no automatic miss is inferred when a prerequisite does not fire.
6. `ANNULLED` requires a registered reason.
7. `FINAL` is never reopened. A correction retains the earlier verified resolution and appends a privileged correction.

### 12.2 Forecast states

```text
ACTIVE -> SUPERSEDED + new ACTIVE version
ACTIVE -> WITHDRAWN
ACTIVE -> LOCKED when question closes
```

Withdrawal and supersession never erase a submitted value.

### 12.3 Chain rules

- Version 1 has `previous_event_id: null`.
- Version N requires the unique accepted event at version N-1 as parent.
- A command whose `expected_version` differs from current stream version is rejected `STALE_EXPECTED_VERSION`.
- If stored history contains two children claiming the same parent/version, the stream is `CONFLICT`.
- Replay never chooses a winner using time or filename order.
- Conflicted streams are omitted from ordinary current-state and calibration rows and appear in `EXCEPTIONS.md`.

## 13. Initial rejection reason registry

The first implementation registers at least:

```text
ACTOR_PATH_MISMATCH
AUDIT_DUPLICATE_RESULT
COMMAND_SCHEMA_INVALID
DUPLICATE_COMMAND
EVIDENCE_REQUIRED
FAMILY_NOT_ENABLED
IDENTIFIER_COLLISION
IDEMPOTENCY_KEY_REUSED
INVALID_INFORMATION_CUTOFF
INVALID_TIMESTAMP
NATIVE_BLOB_MISMATCH
NATIVE_PATH_INVALID
NATIVE_RECORD_AMBIGUOUS
NATIVE_RECORD_INVALID
NATIVE_RECORD_MISSING
NATIVE_RECORD_MISMATCH
PERMISSION_DENIED
POLICY_VERSION_UNSUPPORTED
PROTECTED_SELF_VERIFICATION
QUESTION_NOT_OPEN
SCHEMA_VERSION_UNSUPPORTED
STALE_EXPECTED_VERSION
TRANSITION_FORBIDDEN
UNSUPPORTED_HISTORICAL_VERSION
```

Reason meanings are versioned policy. Free-text detail may identify offending fields or references but may not replace the stable reason code.

## 14. Registered views

Only these cross-session views are committed initially:

```text
KERNEL/views/OPEN_QUESTIONS.md
KERNEL/views/RESOLUTION_QUEUE.md
KERNEL/views/EXCEPTIONS.md
KERNEL/views/CALIBRATION.tsv
```

Every view contains or, for TSV, is paired with machine-readable metadata specifying:

```text
authority_mode: SHADOW
generated_at
source_event_count
source_event_set_sha256
schema_versions
policy_versions
renderer_version
notice: GENERATED — DO NOT EDIT — NON-AUTHORITATIVE
```

Deterministic rows sort by stable semantic keys, never filesystem enumeration order. `generated_at` is injected; reproduction checks hold it fixed or exclude it from the reproducible content digest.

### 14.1 View meanings

- `OPEN_QUESTIONS.md`: replay-valid open questions and attached current forecast versions.
- `RESOLUTION_QUEUE.md`: closed, due, overdue, proposed, disputed, and verification-pending questions.
- `EXCEPTIONS.md`: conflicts, audit gaps, invalid history, native-shadow discrepancies, unsupported versions, and declared `UNKNOWN` checks.
- `CALIBRATION.tsv`: verified, mechanically eligible forecast versions and outcomes. No subjective recoding; explicit exclusion reason otherwise.

An empty view is valid and must still carry its metadata and shadow notice.

## 15. Local projection and locking

`.rw/` is gitignored, disposable, and never authoritative. It may contain:

```text
.rw/projection.sqlite
.rw/locks/command.lock
.rw/logs/
```

Deleting `.rw/` and replaying the same accepted events must reproduce the same semantic state and registered view content. No accepted command or event exists only in SQLite.

The local lock protects the current shared-worktree operating model only. Independent clones require one acceptance writer before they may submit live commands.

## 16. PROME unavailability and substitute custody

The substitute path is procedural, not automatic delegation:

1. Pending commands remain durable and unaccepted while PROME is unavailable.
2. Will may name a temporary substitute custodian for a bounded acceptance window.
3. The substitute must already have an explicit `command.accept` grant in the active policy version, or Will authorizes a prospective policy-version change before processing.
4. The substitute runs the identical acceptance binary and may exercise no additional discretion.
5. Events record the substitute's `writer_id` and unchanged research `actor_id`.
6. The first subsequent PROME check verifies the acceptance window, results, and audit completeness.

No timeout silently transfers custody. CI never becomes the acceptance writer.

## 17. Git ownership and additions-only boundary

Implementation requires a narrow, explicit repository Git carve-out before live shadow activation:

- agents may commit only their own immutable submission files under their existing owned directories;
- PROME may commit kernel schemas, policies, registry changes approved within its authority, accepted events, rejected receipts, and registered views;
- staging is always explicit and path-scoped;
- accepted event and receipt paths are additions-only;
- modification or deletion of an accepted file is a blocking integrity failure;
- no tool commits or pushes automatically.

The exact root-canon Git wording must be approved and installed before a real shadow command is accepted. Fixture-only development may proceed on an implementation branch without implying live authority.

## 18. Verification claims

Each check prints its perimeter and one of `PASS`, `EXCEPTION`, or `UNKNOWN`.

| Check | A pass proves | A pass does not prove |
|---|---|---|
| Schema | Files in the printed perimeter match registered syntax | Research truth or evidence persuasiveness |
| Permissions | Recorded actors have required capabilities under cited policy | Actor competence or substantive independence beyond policy |
| Native reference | Exact cited bytes exist at the cited commit | Structured interpretation is analytically correct unless separately reconciled |
| Replay | Valid, unconflicted events deterministically reconstruct state | Missing commands never submitted |
| Audit | Every processed command in perimeter has exactly one result | Every native action was submitted |
| View reproduction | Registered views equal deterministic renderer output | Views cover unregistered repository state |
| Additions-only | Accepted paths were not modified or deleted in compared history | Protection against a malicious direct writer outside the threat model |

No aggregate green status is permitted when any required check is `UNKNOWN`.

## 19. Fixture acceptance matrix

The specification is ready for implementation only when fixtures encode these outcomes unambiguously:

| Fixture | Expected result |
|---|---|
| Valid native question | `QuestionRegistered`, question stream v1 |
| Valid native binary forecast | `ForecastSubmitted`, forecast stream v1 |
| Same command and same bytes retried | Return prior durable result; no new event |
| Same command ID with different bytes | Reject `IDEMPOTENCY_KEY_REUSED` |
| Missing native commit/path/record | Durable native-reference rejection |
| Shifted TSV row | Reject `NATIVE_RECORD_INVALID` |
| Probability outside `[0,1]` | Reject `COMMAND_SCHEMA_INVALID` |
| Forecast on non-open question | Reject `QUESTION_NOT_OPEN` |
| Stale expected version | Reject `STALE_EXPECTED_VERSION` |
| Unauthorized actor | Reject `PERMISSION_DENIED` |
| Threshold forecast in first increment | Reject `FAMILY_NOT_ENABLED` |
| Forecast amendment before close | New immutable version; original retained |
| Forecast amendment after close | Reject `TRANSITION_FORBIDDEN` |
| Resolution without evidence | Reject `EVIDENCE_REQUIRED` |
| Protected self-verification | Reject `PROTECTED_SELF_VERIFICATION` |
| Competing stored children | Stream `CONFLICT`; exclude from ordinary views |
| Delete `.rw/`, replay, render | Same semantic state and reproducible view digest |
| Event file modified or deleted | Blocking additions-only failure |

Two independent readers must agree on every expected result before live shadow activation.

## 20. Implementation and activation gates

### Gate A — specification approval

Will approves this contract or its successor. Approval authorizes creation of the fixture-backed implementation skeleton; it does not activate live shadow operation.

### Gate B — fixture implementation

Required:

- all fixture tests pass;
- accepted and rejected results are durable;
- replay is deterministic from an empty `.rw/`;
- all four views reproduce;
- no `EVALUATION/` subsystem exists;
- checks state their perimeter and limits.

### Gate C — live shadow activation

Separately requires:

- the root Git carve-out is approved and installed;
- one exact native record and resolver path are selected;
- its family contract is enabled;
- PROME and substitute custody are operationally tested;
- all output is visibly `SHADOW — NON-AUTHORITATIVE`;
- Will explicitly authorizes activation.

### Gate D — authority switch

Out of scope. It requires a later ruling satisfying the architecture packet's deterministic replay, additions-only, zero-integrity-defect, discrepancy, audit, burden, coverage, and stable-window requirements.

## 21. Deferred implementation decisions

These do not block the first binary fixture slice:

- exact threshold-crossing value model;
- conditional prerequisite activation and scoring rules;
- numerical interval support;
- generalized adapters for legacy ledger families;
- operational latency, queue-age, burden, coverage, and stable-window thresholds;
- formal evaluation design;
- scheduling or durable obligations;
- user-interface improvements beyond the CLI and registered views.

## 22. Approval checklist

- [ ] The first increment is binary-only and shadow-only.
- [ ] Native records remain authoritative.
- [ ] IDs, timestamps, hashes, paths, and versions are sufficiently exact.
- [ ] PROME's custody is deterministic and non-substantive.
- [ ] The substitute path preserves the same custody boundary.
- [ ] Accepted and rejected commands both have one durable result.
- [ ] Native-reference validation fails closed.
- [ ] Stream conflicts quarantine rather than auto-resolve.
- [ ] The four committed views are registered and visibly non-authoritative.
- [ ] Fixtures prove the contract before any real record is imported.
- [ ] `KERNEL/` creation and live shadow activation remain separate approvals.

---

## Bottom line

The first build is not a platform. It is one deterministic proof:

> A committed native binary forecast can be represented as an immutable, exactly referenced, visibly non-authoritative shadow history; invalid commands fail closed; every processed command leaves one durable result; and replay reproduces the same state and operator views.

Anything not necessary to prove that statement remains outside the first increment.
