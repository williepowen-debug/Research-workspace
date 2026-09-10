# 🧊 FROZEN 2026-09-09 — Kernel v1 implementation CHRONOLOGY (moved verbatim from `KERNEL/IMPLEMENTATION_STATUS.md` lines 13–246 at `0ab1e8e51`; DOCKET L268)

**HISTORY, not status.** Build chronology dated 2026-08-25 → 2026-08-28, whose 2026-09-03 header called it "through 2026-08-26"; its present-tense lines were falsified by Sitting 1 (2026-08-27) and declared HISTORY on 2026-09-03; the live, records-derived status is `KERNEL/IMPLEMENTATION_STATUS.md`. **Block crc32 3472015315** = `PROME/tools/measure.py` (crc32-no-final-nl) over the exact moved bytes below, from the first `## Session entry` line to the closing fence of `## Verification record`. Verify by RECOMPUTING from the bytes between the markers, never from this banner. The 9/3 header (lines 1–11) was rewritten in place and is NOT in this block — `git show 0ab1e8e51:KERNEL/IMPLEMENTATION_STATUS.md` has it.

<!-- FROZEN BLOCK BEGIN -->
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

Expected baseline at this checkpoint: **207 tests pass**.

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
| Registered projection exclusions (CALIBRATION) — kernel.renderer.2 | COMPLETE (code + tests; first live render at Sitting 2) | 2026-08-28 | `KERNEL/policies/projection-exclusions.json` (schema `kernel.projection-exclusions.1`, one enumerated reason `OUTCOME_VOCABULARY_MISMATCH`, entry = MIDAS-06 `Q-019306a1-…006a`, Will-ruled 8/28); `render.validate_projection_exclusions` fail-closed; applied in every question state; joins the source-input digest; `live_shadow.render_live_views` reads it from the activation's `repository_root` (malformed ⇒ `PROJECTION_EXCLUSIONS_INVALID` LiveRefusal); `tests/test_projection_exclusions.py`. ⚠️ Committed `KERNEL/views/` still carry `kernel.renderer.1` — views are written only under a live grant; the first `--apply` at Sitting 2 re-renders them (runbook: views re-render by design) and `--check-views` then reproduces. Not a pinned-hash change: activations pin actors/grants/custody/commands, not the renderer. |
| Gate B checkpoint 3 — exact native-reference verification | COMPLETE / APPROVED | `65335142c` | Read-only injectable Git boundary; strict TSV/JSON selection; exact selected-byte hashes; material-term reconciliation; 35 tests passed; Will approved 2026-08-25 |
| Gate B checkpoint 4 — actor registry and deterministic permissions | COMPLETE | `55a6dd182` | Strict actor/capability registries; owned-path, half-open-window, identity, payload-ownership, and capability checks; 46 tests passed |
| Gate B checkpoint 5 — dependency planner and pending inventory | COMPLETE | `264a8ade6` | Explicit synthetic inventories; deterministic topological order; completed/ready/waiting/rejection classes; iterative cycle and missing-root analysis; 58 tests passed |
| Gate B checkpoint 6 — durable accepted/rejected result writer | COMPLETE | `63b72bac2` | Strict receipt contract; canonical atomic fixture publication; durable-result inventory; same-byte retry idempotency; collision and crash-boundary tests; 74 tests passed |
| Gate B checkpoint 7 — exclusive local acceptance lock | COMPLETE | `b62b59abb` | Repository-refusing `.rw/locks/command.lock`; locked inventory→plan→write pass; direct writer serialization; cross-process exclusion and release/authority-boundary tests; 80 tests passed |
| Gate B checkpoint 8 — remaining lifecycle events | COMPLETE | `865be30f5` | Strict close/annul, amend/withdraw, and propose/verify/dispute/correct contracts; replay state machines; replay-backed writer transitions; lifecycle views, native terms, permissions, and adversarial receipts; 99 tests passed |
| Gate B checkpoint 9 — additions-only and audit-gap verification | COMPLETE | `b37f560b5` | Repository-refusing synthetic Git-history boundary; additions-only protected paths; explicit durable-result reconciliation; perimeter-aware `PASS`/`EXCEPTION`/`UNKNOWN`; 117 tests passed |
| Gate B checkpoint 10 — disposable projection rebuild | COMPLETE | `94eb93602` | Root `.rw/` ignore boundary; atomic SQLite rebuild from explicit fixture events; strict read reconciliation; delete/rebuild semantic and view-byte identity; 136 tests passed |
| Gate B checkpoint 11 — fixture adversarial review | COMPLETE / BLOCKING FINDINGS | `720b8e2e9` reviewed baseline | Two readers agreed on all 22 expected outcomes and component-vs-complete-path qualifications; review proved the integrated acceptance path and uniform executable check disclosure are absent; `GATE_B_ADVERSARIAL_REVIEW.md` |
| Gate B checkpoint 12 — integrated fixture acceptance and check disclosure | COMPLETE / INDEPENDENT PASS | `e212bd26b` starting baseline | Ready-only integrated schema/permission/native/lifecycle/write path; durable dependency dispositions; retry re-verification; explicit `UNKNOWN` accounting; render disclosure; 155 tests; `CHECKPOINT_12_ACCEPTANCE_REMEDIATION.md` |
| Gate C live-interface remediation | BUILT + REHEARSED / INDEPENDENT REVIEW OWED | `f8560f2c0` | One explicit activation-gated live door (`live_shadow.py` + minted grant); no synthetic refusal weakened; refusal matrix tested; disposable C6 rehearsal repeated through the exact interface with a durable transcript; 207 tests; `GATE_C_LIVE_INTERFACE_REMEDIATION.md` |

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
- fixture result summaries fed back into the deterministic planner;
- an exclusive advisory lock at `<injected-workspace>/.rw/locks/command.lock` that refuses repository-related roots;
- lock-scoped durable-result inventory, dependency planning, and result writing;
- direct writer serialization across result lookup and atomic publication;
- release on ordinary completion and exceptional exit; and
- two-process proof that a waiter re-inventories after release and cannot publish a second result;
- strict payload schemas and command/event mappings for all ten approved fixture lifecycle families;
- deterministic Question states `OPEN`, `CLOSED`, `RESOLUTION_PROPOSED`, `DISPUTED`, and `FINAL`;
- deterministic Forecast states `ACTIVE`, `WITHDRAWN`, and derived `LOCKED`, with every immutable version retained;
- stale-version, forbidden-transition, evidence, registered-annulment, negative-search, and protected-verifier rejection paths;
- replay-backed lifecycle acceptance that infers the exact previous event from the durable stream head;
- Resolution proposal, dispute/re-proposal, verification, privileged correction, and annulment replay;
- exact synthetic native material-term reconciliation for lifecycle outcomes and evidence; and
- lifecycle-aware open-question, resolution-queue, and un-clipped corrected-outcome calibration views;
- exact full-SHA synthetic history comparison over injected Git repositories;
- additions-only enforcement for protected accepted-event and rejected-receipt paths, including modification, deletion, rename-away, and unknown-history blocking;
- explicit fixture submission/result reconciliation with global duplicate-result blocking;
- post-success `AUDIT_GAP` and pre-success `AUDIT_COMPLETENESS_UNKNOWN` distinction; and
- audit CLI perimeter disclosure with exactly one of `PASS`, `EXCEPTION`, or `UNKNOWN` and live-repository refusal;
- a root-only Git ignore boundary for disposable `.rw/` state;
- atomic, fsynced SQLite projection replacement beneath injected non-repository workspaces;
- canonical cached event copies, deterministic semantic snapshots, registered view bytes, and reconciled hashes;
- strict projection schema, metadata, SQLite integrity, source-event, semantic-state, and view-content verification;
- stale-input, corruption, schema-expansion, path-collision, symlink-escape, and live-boundary failures; and
- proof that deleting `.rw/` and replaying the same fixture events reproduces identical semantic state and registered view bytes;
- one lock-scoped integrated fixture path that enforces dependency order, permission, exact native verification, lifecycle legality, and exactly-one durable result;
- accepted-retry re-verification against the complete printed check perimeter;
- aggregate refusal on rejected results, collisions, `UNKNOWN`, and any selected command left unprocessed; and
- explicit perimeter, status, pass proof, and pass limitation output for integrated acceptance and view reproduction.

## Current limitations

The implementation does **not** yet:

- enforce configured trusted-history reachability beyond resolving the supplied full commit in the injected repository;
- support `TEXT_ANCHOR` (deliberately excluded from this live-compatible fixture slice);
- issue receipts for inputs lacking the minimum parseable transport identity needed by the approved receipt path;
- scan any submission directory — live input discovery is and remains an explicit operator-pinned inventory, never a filesystem or repository scan.

An executable live-shadow interface now exists (`tools/live_shadow.py`), but it
has not been independently reviewed and no activation document for the real
repository exists; no live command, result, view, or shadow operation has
occurred.

## Next action — independent adversarial review of the live interface

**The remediation is built and rehearsed. The next step belongs to a reviewer
who is not the builder, in a separate sitting: run the review brief in
`GATE_C_LIVE_INTERFACE_REMEDIATION.md`. Only after that review may a fresh C7
packet fix start and end timestamps and request an activation ruling. Do not
create live commands or results or activate custody before that ruling.**

Will closed Gate B on 2026-08-26 based on the technical exit evidence recorded in
`KERNEL/CHECKPOINT_12_ACCEPTANCE_REMEDIATION.md`. The ruling confirms only that
the approved fixture implementation is complete. It does not activate Gate C,
authorize real records, install the live Git carve-out, or switch authority.
The staged readiness and decision sequence is canonical in
`KERNEL/GATE_C_READINESS_PLAN.md`.

Approved C1–C2 records:

- `KERNEL/GATE_C_C1_PILOT_CONTRACT_DRAFT.md`
- `KERNEL/GATE_C_C2_GIT_CARVEOUT_DRAFT.md`

## Remaining Gate B sequence

| Order | Increment | State | Exit condition |
|---:|---|---|---|
| 1 | Exact native-reference verification | COMPLETE | Synthetic Git-backed references pass; malformed/mismatched references fail closed |
| 2 | Actor registry and deterministic permissions | COMPLETE | Actor/path/capability fixtures pass; custody grants no research authority |
| 3 | Dependency planner and pending-command inventory | COMPLETE | Explicit dependencies topologically order; missing dependencies remain visible; cycles reject deterministically |
| 4 | Durable accepted/rejected result writer | COMPLETE | Exactly one atomic fixture result per processed command; retry idempotency proven |
| 5 | Exclusive local acceptance lock | COMPLETE | Concurrent fixture processes cannot both accept the same command |
| 6 | Remaining lifecycle events | COMPLETE | Amendment, close, withdrawal, proposal, verification, dispute, correction, and annulment fixtures pass |
| 7 | Additions-only and audit-gap verification | COMPLETE | Modified/deleted accepted fixture files and missing/duplicate results are blocking failures |
| 8 | Disposable projection rebuild | COMPLETE | Delete `.rw/`; replay reproduces identical semantic state and committed-view bytes |
| 9 | Gate B adversarial review | COMPLETE / BLOCKING FINDINGS | Two readers agree on all 22 expected outcomes and component-vs-complete-path qualifications; integration and executable-disclosure gaps recorded |
| 10 | Integrated fixture acceptance and check disclosure | COMPLETE / INDEPENDENT PASS | Required checks cannot be skipped through the complete fixture interface; ready-only processing yields exactly one result; `UNKNOWN` blocks aggregate green; every check states perimeter and limits |

The sequence may be simplified when implementation evidence supports it, but any reordering or scope addition must be recorded here.

## Gate state

| Gate | State | Meaning |
|---|---|---|
| Gate A — specification approval | PASSED | Fixture implementation is authorized |
| Gate B — fixture implementation | PASSED / CLOSED 2026-08-26 | Will approved closure after checkpoint 12 remediated checkpoint 11 findings and passed independent review |
| Gate C — live shadow activation | C1–C6 COMPLETE / C7 REMEDIATION BUILT + REHEARSED / REVIEW OWED / NOT ACTIVE | The explicit live interface exists and the rehearsal repeated through it passed; independent adversarial review, then a fresh timestamped C7 packet and Will's ruling, are required before any live command |
| Gate D — authority switch | OUT OF SCOPE | Requires later operational evidence and explicit ruling |

## Verification record

Latest completed verification after the live-interface remediation:

```text
python3 -m unittest discover -s KERNEL/tests -p 'test*.py'
Ran 207 tests — OK

python3 -m compileall -q KERNEL/tools KERNEL/tests
PASS

KERNEL/tools/live_shadow.py --preflight / --apply / --check-views / --audit-additions
Disposable-clone rehearsal through the exact live interface: every step passed;
durable transcript = KERNEL/rehearsals/2026-08-26_live-interface-rehearsal-transcript.txt;
live repository verified untouched (0 files under live KERNEL/shadow + KERNEL/views).
```

Prior verification after checkpoint 12 remediation:

```text
python3 -m unittest discover -s KERNEL/tests -p 'test*.py' -v
Ran 155 tests — OK

python3 -m compileall -q KERNEL/tools KERNEL/tests

python3 KERNEL/tools/acceptance.py --inventory <temporary-explicit-path-and-command-inventory.json> --actors KERNEL/tests/fixtures/permissions/actors.json --capabilities KERNEL/tests/fixtures/permissions/capability-grants.json --repository <temporary-synthetic-git-repository> --store <temporary-fixture-workspace>/KERNEL --event-ids <temporary-command-to-event-id-map.json> --recorded-at 2026-08-26T12:00:00.000000Z
PASS: aggregate; every required fixture check printed its perimeter, pass claim, and limitation

python3 KERNEL/tools/render.py --events KERNEL/tests/fixtures/events/valid_binary.json --output <temporary-view-directory> --as-of 2026-08-26T00:00:00.000000Z --check
PASS: registered fixture views verified deterministically; perimeter and claim limits printed

python3 KERNEL/tools/verify_native.py <synthetic-command> --repository <temporary-synthetic-git-repository>
PASS: exact native bytes and material structured terms verified; research quality was not judged

python3 KERNEL/tools/audit.py additions-only --repository <temporary-synthetic-git-repository> --base <full-base-commit> --head <full-head-commit>
PASS: protected accepted-event and receipt paths contain additions only in the compared history

python3 KERNEL/tools/audit.py durable-results --submissions <temporary-explicit-submission-inventory.json> --results <temporary-explicit-result-inventory.json> --pass-reported-success
PASS: every explicit fixture submission has exactly one durable result

python3 KERNEL/tools/projection.py --workspace <temporary-fixture-workspace> --events KERNEL/tests/fixtures/events/valid_binary.json --as-of 2026-08-26T00:00:00.000000Z
PASS: disposable projection rebuilt; semantic state and registered view bytes reconcile with explicit fixture events; SQLite has no authority

python3 KERNEL/tools/projection.py --workspace <temporary-fixture-workspace> --events KERNEL/tests/fixtures/events/valid_binary.json --as-of 2026-08-26T00:00:00.000000Z --check
PASS: disposable projection verified; semantic state and registered view bytes reconcile with explicit fixture events; SQLite has no authority
```
<!-- FROZEN BLOCK END -->
