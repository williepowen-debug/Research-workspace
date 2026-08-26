# Kernel v1 Implementation Status

**Owner:** PROME

**Updated:** 2026-08-25

**Latest operator ruling:** Gate B checkpoint 3 approved by Will on 2026-08-25. Checkpoints 4–6 were subsequently implemented at `55a6dd182`, `264a8ade6`, and `63b72bac2`; they remain fixture-only and do not complete Gate B or authorize live operation.

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

Expected baseline at this checkpoint: **74 tests pass**.

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
| Gate B checkpoint 3 — exact native-reference verification | COMPLETE / APPROVED | `65335142c` | Read-only injectable Git boundary; strict TSV/JSON selection; exact selected-byte hashes; material-term reconciliation; 35 tests passed; Will approved 2026-08-25 |
| Gate B checkpoint 4 — actor registry and deterministic permissions | COMPLETE | `55a6dd182` | Strict actor/capability registries; owned-path, half-open-window, identity, payload-ownership, and capability checks; 46 tests passed |
| Gate B checkpoint 5 — dependency planner and pending inventory | COMPLETE | `264a8ade6` | Explicit synthetic inventories; deterministic topological order; completed/ready/waiting/rejection classes; iterative cycle and missing-root analysis; 58 tests passed |
| Gate B checkpoint 6 — durable accepted/rejected result writer | COMPLETE | `63b72bac2` | Strict receipt contract; canonical atomic fixture publication; durable-result inventory; same-byte retry idempotency; collision and crash-boundary tests; 74 tests passed |

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
- an injectable Git boundary and temporary synthetic Git repositories for hermetic, network-free tests and CLI exercise;
- strict injected actor and policy-versioned capability registries with duplicate and unknown-capability rejection;
- exact agent-owned submission-path and command-filename verification without directory scanning;
- half-open actor activity-window checks using the command's `submitted_at`;
- payload-owner and referenced-actor identity checks for the enabled commands; and
- deterministic capability enforcement proving that `command.accept` conveys custody only;
- explicit injected command and minimal durable-result inventory without filesystem enumeration;
- deterministic topological planning with `submitted_at` and `command_id` tie-breaks;
- separate completed, ready, waiting, planned-cycle-rejection, and planned-dependency-rejection classes;
- transitive missing-root visibility without prematurely rejecting a waiting command; and
- iterative graph traversal verified against a 1,200-command adversarial chain;
- strict rejected-receipt envelopes with registered reasons and bounded administrative detail;
- canonical JSON result files with one trailing newline under injected non-repository roots;
- file and directory fsync around temporary-file atomic publication;
- exactly-one-result lookup across accepted events and rejected receipts;
- same-command/same-byte retry return, different-byte ID-reuse rejection without overwrite, and duplicate-result blocking;
- durable conversion of planned dependency rejections and schema-invalid fixture commands;
- injected crash-before-publish recovery and event-identifier collision handling; and
- fixture result summaries fed back into the deterministic planner.

## Current limitations

The implementation does **not** yet:

- enforce configured trusted-history reachability beyond resolving the supplied full commit in the injected repository;
- support `TEXT_ANCHOR` (deliberately excluded from this live-compatible fixture slice);
- reconcile Resolution material terms because Resolution commands are not implemented yet;
- execute a planned acceptance pass against replayed stream state;
- acquire a filesystem acceptance lock;
- orchestrate permissions, native verification, lifecycle validation, planning, and result writing as one acceptance pass;
- issue receipts for inputs lacking the minimum parseable transport identity needed by the approved receipt path;
- enforce additions-only Git history;
- implement Question close, Forecast amendment/withdrawal, Resolution proposal/verification/dispute/correction, or annulment;
- populate calibration with verified outcomes;
- rebuild from a disposable SQLite projection;
- scan real repository submissions or generate live views.

## Next increment — checkpoint 7

**Build the exclusive local acceptance lock using fixtures only.**

The next increment should serialize the inventory→plan→write critical section with
an exclusive local lock beneath an injected temporary `.rw/locks/` root. It must
prove that two fixture processes cannot both publish a result for the same command,
that lock release occurs after success and failure, and that waiting for the lock
does not confer any policy authority. It must not target the live repository or add
a live submission scan.

## Remaining Gate B sequence

| Order | Increment | State | Exit condition |
|---:|---|---|---|
| 1 | Exact native-reference verification | COMPLETE | Synthetic Git-backed references pass; malformed/mismatched references fail closed |
| 2 | Actor registry and deterministic permissions | COMPLETE | Actor/path/capability fixtures pass; custody grants no research authority |
| 3 | Dependency planner and pending-command inventory | COMPLETE | Explicit dependencies topologically order; missing dependencies remain visible; cycles reject deterministically |
| 4 | Durable accepted/rejected result writer | COMPLETE | Exactly one atomic fixture result per processed command; retry idempotency proven |
| 5 | Exclusive local acceptance lock | NEXT | Concurrent fixture processes cannot both accept the same command |
| 6 | Remaining lifecycle events | PENDING | Amendment, close, withdrawal, proposal, verification, dispute, correction, and annulment fixtures pass |
| 7 | Additions-only and audit-gap verification | PENDING | Modified/deleted accepted fixture files and missing/duplicate results are blocking failures |
| 8 | Disposable projection rebuild | PENDING | Delete `.rw/`; replay reproduces identical semantic state and committed-view bytes |
| 9 | Gate B adversarial review | PENDING | Two independent readers agree on fixture outcomes; all checks state perimeter and limits |

The sequence may be simplified when implementation evidence supports it, but any reordering or scope addition must be recorded here.

## Gate state

| Gate | State | Meaning |
|---|---|---|
| Gate A — specification approval | PASSED | Fixture implementation is authorized |
| Gate B — fixture implementation | IN PROGRESS | Checkpoints 1–6 complete; checkpoint 7 next |
| Gate C — live shadow activation | NOT AUTHORIZED | Requires separate Will approval and all listed activation prerequisites |
| Gate D — authority switch | OUT OF SCOPE | Requires later operational evidence and explicit ruling |

## Verification record

Latest completed verification at commit `63b72bac2`:

```text
python3 -m unittest discover -s KERNEL/tests -p 'test*.py' -v
Ran 74 tests — OK

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
