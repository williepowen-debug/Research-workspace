# KERNEL

**Mode:** GATE C PLANNING — NOT LIVE — NON-AUTHORITATIVE

This directory contains the completed Gate B fixture implementation and the
planning workspace for the Kernel v1 operational shadow registry.

No real native record may be inspected or imported and no shadow operation is
active. Gate C planning is authorized, but live implementation, Git carve-out
installation, custody activation, real-record selection, and shadow activation
remain separately gated in [`GATE_C_READINESS_PLAN.md`](GATE_C_READINESS_PLAN.md).

## Authority

- Approved contract: [`SPEC.md`](SPEC.md)
- Live implementation plan and completed work: [`IMPLEMENTATION_STATUS.md`](IMPLEMENTATION_STATUS.md)
- Gate C staged readiness plan: [`GATE_C_READINESS_PLAN.md`](GATE_C_READINESS_PLAN.md)
- Design and ruling history: [`../PROME/proposals/2026-08-24_kernel-membrane-design-DRAFT.md`](../PROME/proposals/2026-08-24_kernel-membrane-design-DRAFT.md)
- Hardened Gate A specification: [`../PROME/proposals/2026-08-25_kernel-v1-spec-DRAFT.md`](../PROME/proposals/2026-08-25_kernel-v1-spec-DRAFT.md)

Native agent records remain authoritative. `KERNEL/` has no live authority.

## Current slice

The implemented slice is fixture-only and binary-question-only:

1. validate strict command and event envelopes;
2. validate binary Question, Forecast, and Resolution lifecycle payloads;
3. replay accepted fixture events and lifecycle states deterministically;
4. detect invalid chains and competing children;
5. render byte-stable empty or fixture-backed operator views;
6. verify exact synthetic native references against committed Git blobs; and
7. authorize fixture commands against injected actor and capability registries;
8. inventory explicit fixture commands/results and deterministically plan dependencies;
9. atomically publish canonical accepted events or rejected receipts beneath injected temporary roots;
10. serialize fixture inventory→plan→write passes with an exclusive local lock;
11. enforce Question close/annul, Forecast amend/withdraw, and Resolution propose/verify/dispute/correct transitions;
12. verify additions-only synthetic Git history and reconcile explicit fixture submissions with durable results; and
13. atomically rebuild and verify a disposable SQLite projection from explicit accepted fixture events; and
14. run schema, dependency, permission, native-reference, lifecycle, and durable-result checks through one fixture-only acceptance path.

There is no live acceptance pipeline, live submission scan, commit automation, or
push automation in this slice. `tools/acceptance.py` accepts only explicit injected
fixture inventories, registries, a synthetic Git repository, event identifiers,
and a result store outside the live repository.

Exact native-reference verification is read-only. TSV locators use the strict form
`<declared-id-column>=<record-id>`; JSON companions use RFC 6901 JSON Pointers.
The verifier reads committed Git objects through an injected repository boundary
and never treats mutable checkout contents as native authority.

Permission verification is also injected and read-only. It validates strict actor
and capability registries, half-open active windows, exact agent-owned submission
paths, payload ownership, referenced actor identity, and command capabilities. It
does not read the live roster or scan an agent submission directory. Lifecycle
capabilities remain separate from acceptance custody.

Lifecycle replay retains every Forecast version, derives ACTIVE, WITHDRAWN, and
LOCKED states, and derives OPEN, CLOSED, RESOLUTION_PROPOSED, DISPUTED, and FINAL
Question states. Resolution correction appends history and changes only the derived
current outcome. Registered views consume those replayed states; calibration uses
the final verified or corrected binary outcome without clipping probabilities.

Dependency planning accepts commands and minimal durable-result summaries supplied
directly by tests. It separates completed, ready, waiting, and dependency-rejection
classes; uses dependency order followed by `submitted_at` and `command_id`; and
writes nothing. Missing dependencies remain visible and unprocessed.

The fixture writer refuses every destination inside the live repository. Beneath an
injected temporary root it writes canonical JSON through a file-and-directory-fsynced
temporary file and atomic rename, returns an existing result for a same-byte retry,
never overwrites a different-byte command-ID result, and exposes stored summaries
back to the planner. Before constructing an accepted event it replays accepted
fixture history, checks the target stream version and legal lifecycle transition,
and infers the exact previous event from the replayed stream head.

The fixture acceptance lock also refuses the live repository. It uses an advisory
exclusive lock at `<injected-workspace>/.rw/locks/command.lock`; the locked pass
holds it across durable-result inventory, dependency planning, and result writes.
Direct writer calls hold the same lock across result lookup and publication. The
lock protects one shared local workspace only and grants no actor capability or
research authority.

The integrated fixture runner holds that lock while it repeatedly inventories and
re-plans. It processes only the next dependency-ready command, durably publishes
planned dependency rejections, runs permission and exact native-reference checks
before lifecycle acceptance, and re-plans after every result. A missing dependency
remains visible and unprocessed. Every instantiated check prints its exact
perimeter, `PASS`, `EXCEPTION`, or `UNKNOWN`, what a pass proves, and what it does
not prove. Any required `UNKNOWN` blocks aggregate green and leaves the affected
command unprocessed. The lower-level writer remains a fixture component used by
unit tests; it is not the complete acceptance interface.

The fixture audit reads only injected synthetic Git histories and explicit
submission/result inventories. It reports its exact perimeter and `PASS`,
`EXCEPTION`, or `UNKNOWN`; any non-pass blocks an aggregate green claim. Protected
accepted-event and receipt paths may only be added in the compared history.
Modification, deletion, rename-away, and other non-addition statuses fail closed.
Duplicate results are blocking, and a missing result becomes `AUDIT_GAP` only after
the caller reports a successful pass. The CLI refuses the live repository and
inventories stored inside it.

The local projection exists only at `<injected-workspace>/.rw/projection.sqlite`.
It caches canonical event copies, a deterministic semantic replay snapshot, and
the exact registered view bytes, all with reconciled hashes and strict schema
metadata. Rebuild uses a fully written and fsynced temporary database followed by
atomic replacement. Read and `--check` paths independently replay the cached
events and compare the snapshot and view bytes; explicit durable events are still
required to prove that the cache is current. Deleting `.rw/` loses no authority,
and rebuilding from the same durable events reproduces the same semantic state
and view bytes. The CLI refuses the live repository and live accepted-event paths.

The exact next increment and remaining Gate B sequence are canonical in `IMPLEMENTATION_STATUS.md`.

## Verification

```bash
python3 -m unittest discover -s KERNEL/tests -p 'test*.py' -v

python3 KERNEL/tools/git_policy_check.py \
  CLAUDE.md AGENTS.md KERNEL/README.md KERNEL/SPEC.md \
  KERNEL/IMPLEMENTATION_STATUS.md KERNEL/GATE_C_READINESS_PLAN.md \
  KERNEL/GATE_C_C1_PILOT_CONTRACT_DRAFT.md

python3 KERNEL/tools/gate_c_boundary.py \
  --mirror <marked-synthetic-git-mirror> \
  --live-repository-root <actual-live-repository-root> \
  --inventory <explicit-one-to-three-path-inventory.json> \
  --submission-commit <full-commit-sha> \
  --actors <synthetic-actor-registry.json> \
  --capabilities <synthetic-capability-registry.json> \
  --event-ids <synthetic-command-event-map.json> \
  --custody-policy KERNEL/policies/custody-policy.json \
  --recorded-at 2026-08-26T12:00:00.000000Z \
  --dry-run

python3 KERNEL/tools/acceptance.py \
  --inventory <temporary-explicit-path-and-command-inventory.json> \
  --actors KERNEL/tests/fixtures/permissions/actors.json \
  --capabilities KERNEL/tests/fixtures/permissions/capability-grants.json \
  --repository <temporary-synthetic-git-repository> \
  --store <temporary-fixture-workspace>/KERNEL \
  --event-ids <temporary-command-to-event-id-map.json> \
  --recorded-at 2026-08-26T12:00:00.000000Z

fixture_out="$(mktemp -d)"
python3 KERNEL/tools/render.py \
  --events KERNEL/tests/fixtures/events/valid_binary.json \
  --output "$fixture_out" \
  --as-of 2026-08-26T00:00:00.000000Z
python3 KERNEL/tools/render.py \
  --events KERNEL/tests/fixtures/events/valid_binary.json \
  --output "$fixture_out" \
  --as-of 2026-08-26T00:00:00.000000Z \
  --check

python3 KERNEL/tools/verify_native.py \
  <synthetic-command.json> \
  --repository <temporary-synthetic-git-repository>

python3 KERNEL/tools/audit.py additions-only \
  --repository <temporary-synthetic-git-repository> \
  --base <full-base-commit> \
  --head <full-head-commit>

python3 KERNEL/tools/audit.py durable-results \
  --submissions <temporary-explicit-submission-inventory.json> \
  --results <temporary-explicit-result-inventory.json> \
  --pass-reported-success

python3 KERNEL/tools/projection.py \
  --workspace <temporary-fixture-workspace> \
  --events KERNEL/tests/fixtures/events/valid_binary.json \
  --as-of 2026-08-26T00:00:00.000000Z
python3 KERNEL/tools/projection.py \
  --workspace <temporary-fixture-workspace> \
  --events KERNEL/tests/fixtures/events/valid_binary.json \
  --as-of 2026-08-26T00:00:00.000000Z \
  --check
```
