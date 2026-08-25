# Kernel v1 Implementation Status

**Owner:** PROME

**Updated:** 2026-08-25

**Current mode:** GATE B FIXTURE IMPLEMENTATION — NOT LIVE — NON-AUTHORITATIVE

**Canonical use:** This file is the live implementation plan and progress tracker. Update it whenever a build increment is completed, blocked, reordered, or newly authorized. The proposal preserves design and ruling history; the audit preserves findings and checkpoint evidence; neither replaces this current-status surface.

## Session entry

Future implementation sessions should read, in order:

1. `KERNEL/README.md` — authority boundary and verification entry point
2. `KERNEL/SPEC.md` — implemented-contract pointer and authorization boundary
3. this file — completed work, next increment, and remaining gates
4. `PROME/proposals/2026-08-25_kernel-v1-spec-DRAFT.md` — full approved contract when changing behavior

Before editing, verify a clean `master`, synchronize with `origin/master`, and run:

```bash
python3 -m unittest discover -s KERNEL/tests -p 'test*.py' -v
```

Expected baseline at this checkpoint: **20 tests pass**.

## Authorization boundary

### Authorized now

- Fixture-only schemas, policies, registries, validation, replay, rendering, and tests
- Synthetic binary-probability Question and Forecast records
- Adversarial fixture histories
- Read-only Git-backed native-reference verification against synthetic fixtures
- Later Gate B acceptance/receipt implementation using fixtures only

### Not authorized

- Importing any real agent or native prediction record
- Scanning or processing live agent submission directories
- Writing live shadow events or receipts
- Committing registered operator views derived from real records
- Installing the live-operation Git carve-out
- Activating shadow operation
- Any canonical authority or authority switch

## Completed increments

| Increment | Status | Commit | Evidence |
|---|---|---|---|
| Architecture rulings | COMPLETE | `abdb5f0ff` | All 22 decisions resolved, amended, or deferred; no authority activated |
| Gate A operational specification | COMPLETE / APPROVED | `9bbf9c041` | Hardened contract approved by Will after adversarial review |
| Gate B checkpoint 1 — contract and replay core | COMPLETE | `ee322ff5a` | Five strict JSON Schemas; pure validation/replay core; 9 tests passed |
| Gate B checkpoint 2 — deterministic fixture views | COMPLETE | `262cd0641` | Four registered view renderers; valid/adversarial file fixtures; 20 tests passed; render/check byte reproduction passed |

Implemented behavior now includes:

- strict command and accepted-event envelopes;
- binary Question and Forecast payload validation;
- fail-closed unknown fields and disabled forecast families;
- UUIDv7-form identifier validation;
- probability and information-cutoff validation;
- native-reference shape and path-traversal validation;
- deterministic per-stream replay independent of input order;
- duplicate event-ID, broken-chain, gap, conflict, and orphan-Forecast detection;
- conflict/orphan omission from ordinary current state;
- explicit `render_as_of` for time-relative views;
- order-independent complete input hashing;
- byte-identical rendering and hand-edit drift detection;
- synthetic `OPEN_QUESTIONS.md`, `RESOLUTION_QUEUE.md`, `EXCEPTIONS.md`, and `CALIBRATION.tsv` output.

## Current limitations

The implementation does **not** yet:

- verify that a cited Git commit, blob, TSV record, or JSON pointer exists;
- compare selected native bytes with `raw_record_sha256`;
- prove that every material structured term exists in cited native records;
- validate actor capabilities or submission-path ownership;
- sort and process command dependencies;
- write accepted events or rejected receipts;
- implement idempotent command-result lookup;
- acquire a filesystem acceptance lock;
- enforce additions-only Git history;
- implement Question close, Forecast amendment/withdrawal, Resolution proposal/verification/dispute/correction, or annulment;
- populate calibration with verified outcomes;
- rebuild from a disposable SQLite projection;
- scan real repository submissions or generate live views.

## Next increment — checkpoint 3

**Build exact native-reference verification against synthetic Git-backed fixtures.**

Required behavior:

1. Resolve a full commit SHA without consulting mutable working-tree contents.
2. Load the referenced blob through Git.
3. Enforce repository-relative path normalization.
4. Support `TSV_RECORD_ID` with comment/blank skipping, one detected header, exact row width, declared ID column, and exactly one matching row.
5. Support strict `JSON_POINTER` selection for native companion artifacts.
6. Hash the exact selected native bytes and compare `raw_record_sha256`.
7. Return stable fail-closed findings for missing commit, missing path, missing record, duplicate record, shifted row, invalid pointer, and hash mismatch.
8. Verify material-term coverage between the structured command and its cited ledger/companion records without interpreting research quality.
9. Use synthetic commits/fixtures only; do not cite or import a real agent ledger.

Checkpoint-3 exit evidence:

- file-backed happy-path TSV and JSON companion fixtures;
- adversarial fixtures for every failure class above;
- injected repository/Git boundary for hermetic tests;
- no network dependency;
- no write-capable acceptance path;
- all prior tests remain green.

## Remaining Gate B sequence

| Order | Increment | State | Exit condition |
|---:|---|---|---|
| 1 | Exact native-reference verification | NEXT | Synthetic Git-backed references pass; malformed/mismatched references fail closed |
| 2 | Actor registry and deterministic permissions | PENDING | Actor/path/capability fixtures pass; custody grants no research authority |
| 3 | Dependency planner and pending-command inventory | PENDING | Explicit dependencies topologically order; missing dependencies remain visible; cycles reject deterministically |
| 4 | Durable accepted/rejected result writer | PENDING | Exactly one atomic fixture result per processed command; retry idempotency proven |
| 5 | Exclusive local acceptance lock | PENDING | Concurrent fixture processes cannot both accept the same command |
| 6 | Remaining lifecycle events | PENDING | Amendment, close, withdrawal, proposal, verification, dispute, correction, and annulment fixtures pass |
| 7 | Additions-only and audit-gap verification | PENDING | Modified/deleted accepted fixture files and missing/duplicate results are blocking failures |
| 8 | Disposable projection rebuild | PENDING | Delete `.rw/`; replay reproduces identical semantic state and committed-view bytes |
| 9 | Gate B adversarial review | PENDING | Two independent readers agree on fixture outcomes; all checks state perimeter and limits |

The sequence may be simplified when implementation evidence supports it, but any reordering or scope addition must be recorded here.

## Gate state

| Gate | State | Meaning |
|---|---|---|
| Gate A — specification approval | PASSED | Fixture implementation is authorized |
| Gate B — fixture implementation | IN PROGRESS | Checkpoints 1–2 complete; checkpoint 3 next |
| Gate C — live shadow activation | NOT AUTHORIZED | Requires separate Will approval and all listed activation prerequisites |
| Gate D — authority switch | OUT OF SCOPE | Requires later operational evidence and explicit ruling |

## Verification record

Latest completed verification at commit `262cd0641`:

```text
python3 -m unittest discover -s KERNEL/tests -p 'test*.py' -v
Ran 20 tests — OK

python3 KERNEL/tools/render.py --events <valid fixture> --output <temp> --as-of 2026-08-26T00:00:00.000000Z
python3 KERNEL/tools/render.py --events <valid fixture> --output <temp> --as-of 2026-08-26T00:00:00.000000Z --check
Four registered files reproduced exactly.
```

## Stop conditions

Stop and return to Will before proceeding if an implementation step would require:

- a real native record;
- a new governed object or forecast family;
- substantive interpretation by PROME;
- a live agent-directory scan or write;
- a shared/root Git ownership change;
- a messaging, obligation, scheduling, or hosted-runtime feature;
- weakening fail-closed behavior to make a fixture pass.
