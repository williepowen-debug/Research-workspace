# Gate C Checkpoint C3 — Synthetic Live-Compatible Boundary

**Date:** 2026-08-26

**Authorization:** Will approved C3 after C1 approval and C2 installation.

**Status:** COMPLETE — PRIMARY VERIFICATION PASS — NOT LIVE

## Scope

C3 implements the repository-compatible boundary only against explicitly marked
synthetic Git mirrors. No real record, live submission directory, live result
path, active custodian, or Gate C activation was inspected or exercised.

## Implementation

`KERNEL/tools/gate_c_boundary.py`:

- hard-refuses the real Research-workspace repository and related parent/child
  boundaries;
- requires an exact synthetic marker with `NON_AUTHORITATIVE` authority;
- accepts only an explicit JSON array of one to three canonical submission paths;
- permits only
  `AGENTS/<ACTOR>/outbox/kernel/submissions/<command_id>.json`;
- reads every submission blob from one exact full Git commit rather than the
  mutable checkout;
- reconciles path actor, embedded `actor_id`, filename, and `command_id`;
- reuses the complete Gate B schema, planning, permission, native-reference,
  lifecycle, lock, writer, and durability path;
- supports an ephemeral `--dry-run` that leaves no result in the mirror;
- supports `--apply-synthetic` only inside the marked non-live mirror, writing
  canonical event or receipt paths through the existing atomic writer; and
- prints `SHADOW — NON-AUTHORITATIVE`, mode, explicit perimeter, status, proof,
  and limitations.

No scanning, watcher, scheduler, automatic commit, or automatic push exists.

## Adversarial coverage

Eleven C3 tests prove:

1. an exact committed canonical submission loads;
2. embedded command objects are refused in the path-only inventory;
3. traversal and non-allowlisted paths are refused;
4. more than three selected paths are refused;
5. path, actor, filename, and command identity mismatch is refused;
6. an unmarked mirror is refused;
7. the live repository is refused before marker use;
8. missing and abbreviated submission commits are refused;
9. mutable-checkout submission changes are ignored;
10. dry-run results are ephemeral and do not alter the mirror; and
11. synthetic apply writes exactly one canonical result path.

The full discoverable baseline is **172 tests passing**.

## What this pass proves

- The live-compatible adapter can preserve the C1 explicit path and command-count
  perimeter in a synthetic Git mirror.
- Submission authority comes from exact committed bytes, not a mutable worktree.
- The existing complete acceptance path can operate with repository-shaped paths
  and lock/result locations outside the live repository.
- Dry-run and synthetic-apply modes are distinguishable and visibly
  non-authoritative.

## What this pass does not prove

- Readiness to inspect or process a real record.
- Correctness of a future active custody registry or substitute procedure.
- Safe installation of live registries, result directories, or view generation.
- Operational behavior with multiple machines, writers, or more than three
  commands.
- Gate C activation or any Gate D authority.

## Disposition

- C3: **COMPLETE**.
- C2 carve-out: **INSTALLED BUT INACTIVE**.
- Next checkpoint: **C4 custody policy and operational test; separately
  authorized**.
- C5 real-record selection and C7 activation: **NOT AUTHORIZED**.
