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

Expected baseline at this checkpoint: **35 tests pass**.

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
| Gate B checkpoint 3 — exact native-reference verification | COMPLETE | this checkpoint commit | Read-only injectable Git boundary; strict TSV/JSON selection; exact selected-byte hashes; material-term reconciliation; 35 tests passed |

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
- full-SHA commit resolution and blob reads through Git rather than the mutable checkout;
- strict normalized repository-relative native paths;
- `TSV_RECORD_ID` selection using a declared `column=value` locator, deliberate comment/blank skipping, one header, exact row widths, and exactly one match;
- strict RFC 6901 JSON Pointer selection, including duplicate-member and invalid-escape rejection;
- SHA-256 comparison over the exact selected TSV line bytes or canonical selected JSON value bytes;
- stable fail-closed findings for missing commits/paths/records, ambiguous selections, invalid rows/pointers, hash mismatch, and material-term mismatch;
- same-named material Question/Forecast field reconciliation across cited ledger and companion selections, without research-quality judgment;
- an injectable Git boundary and temporary synthetic Git repositories for hermetic, network-free tests and CLI exercise.

## Current limitations

The implementation does **not** yet:

- enforce configured trusted-history reachability beyond resolving the supplied full commit in the injected repository;
- support `TEXT_ANCHOR` (deliberately excluded from this live-compatible fixture slice);
- reconcile Resolution material terms because Resolution commands are not implemented yet;
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

## Next increment — checkpoint 4

**Build the actor registry and deterministic permission checks using fixtures only.**

The next increment should validate actor identity, submission-path ownership, active
windows, and command capabilities under the cited policy. It must preserve the
custody boundary: `command.accept` grants PROME no research, resolution, or
verification discretion. It must not scan a live submission directory or add a
write-capable acceptance path.

## Remaining Gate B sequence

| Order | Increment | State | Exit condition |
|---:|---|---|---|
| 1 | Exact native-reference verification | COMPLETE | Synthetic Git-backed references pass; malformed/mismatched references fail closed |
| 2 | Actor registry and deterministic permissions | NEXT | Actor/path/capability fixtures pass; custody grants no research authority |
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
| Gate B — fixture implementation | IN PROGRESS | Checkpoints 1–3 complete; checkpoint 4 next |
| Gate C — live shadow activation | NOT AUTHORIZED | Requires separate Will approval and all listed activation prerequisites |
| Gate D — authority switch | OUT OF SCOPE | Requires later operational evidence and explicit ruling |

## Verification record

Latest completed verification for checkpoint 3:

```text
python3 -m unittest discover -s KERNEL/tests -p 'test*.py' -v
Ran 35 tests — OK

python3 -m compileall -q KERNEL/tools KERNEL/tests

python3 KERNEL/tools/verify_native.py <synthetic-command> --repository <temporary-synthetic-git-repository>
PASS: exact native bytes and material structured terms verified; research quality was not judged
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
