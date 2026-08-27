# Gate C Checkpoint C1 — Bounded Pilot Contract (Draft)

**Date:** 2026-08-26

**Status:** APPROVED BY WILL 2026-08-26 — NOT LIVE

**Depends on:** Gate B closed; `GATE_C_READINESS_PLAN.md`

## Operator ruling

Will approved this contract as the fixed boundary for preparing one Gate C
activation packet. The ruling authorizes later checkpoints only when each is
separately approved. It does not authorize real-record inspection or processing,
live writes, substitute activation, or the C7 pilot.

## Purpose

Test whether the completed Gate B fixture implementation can operate safely in a
real repository workflow while remaining a non-authoritative shadow. The pilot
tests custody, traceability, deterministic processing, recovery, and operator
burden. It does not test whether the Kernel should replace native research.

## Fixed scope

| Dimension | Pilot limit |
|---|---|
| Native input | One exact, operator-selected committed Question record |
| Family | Binary Question/Forecast/Resolution only |
| Locator | `TSV_RECORD_ID` or `JSON_POINTER`; never `TEXT_ANCHOR` |
| Submissions | Maximum 3 commands: register Question, submit one Forecast, then either close or withdraw if separately prepared |
| Actors | One native research actor; PROME as sole active acceptance custodian |
| Custody fallback | One Will-named dormant substitute, disabled by default |
| Execution | Manual, one shared worktree, one acceptance writer |
| Duration | One bounded operator-approved window; no standing watcher or schedule |
| Outputs | Durable event/receipt plus the four registered views |
| Authority | `SHADOW — NON-AUTHORITATIVE`; native record remains authoritative |

The activation packet may reduce the command count or duration. Increasing either
requires a new operator ruling.

## Exact path perimeter

- Submission:
  `AGENTS/<CANONICAL_NAME>/outbox/kernel/submissions/<command_id>.json`
- Accepted event:
  `KERNEL/shadow/events/YYYY/MM/<event_id>.json`
- Rejected receipt:
  `KERNEL/audit/commands/YYYY/MM/<command_id>.json`
- Registered views:
  `KERNEL/views/OPEN_QUESTIONS.md`,
  `KERNEL/views/RESOLUTION_QUEUE.md`,
  `KERNEL/views/EXCEPTIONS.md`, and
  `KERNEL/views/CALIBRATION.tsv`
- Disposable local state: `.rw/` only
- Policy/registry inputs: exact files and versions must be named in the C7 packet;
  no directory-wide policy discovery is permitted.

No other path is writable by the pilot.

## Roles

### Native research actor

- Authors and explicitly commits only its immutable command file under its own
  submission path.
- Supplies structured terms already present in exact cited committed native bytes.
- Cannot accept, reject, verify its own protected resolution, alter a result, or
  edit a registered view.

### PROME acceptance custodian

- Runs the identical registered acceptance interface mechanically.
- May validate, accept, reject, render, audit, stage explicit Kernel result/view
  paths, and report exceptions.
- Cannot invent research terms, improve evidence, resolve ambiguity, change native
  records, waive a failed check, or switch authority.

### Dormant substitute custodian

- Is named in C4 and has `command.accept` disabled by default.
- May act only after a separate bounded Will activation with start/end conditions.
- Runs the same interface with no additional discretion.
- Triggers a mandatory PROME audit on return.

### Will

- Approves the carve-out, custody policy, selected native record, rehearsal
  evidence, and C7 activation separately.
- May pause or revoke the pilot at any time.

## Required processing sequence

For each explicitly inventoried command, under one acceptance lock:

1. reconcile the repository and custody perimeter;
2. validate schema and immutable command identity;
3. determine dependency readiness;
4. validate actor, path, policy version, activity window, and capabilities;
5. resolve the full native commit and exact selected bytes;
6. reconcile every material structured term;
7. validate stream version and lifecycle legality;
8. write exactly one accepted event or rejected receipt atomically;
9. re-inventory and re-plan;
10. rebuild the disposable projection and registered views;
11. run durable-result, additions-only, replay, and view-reproduction checks; and
12. print the exact perimeter, status, proof, and limitation of every check.

Any required `UNKNOWN` blocks aggregate green.

## What a successful pilot proves

- The named commands in the printed perimeter received exactly one durable result.
- Exact cited native bytes existed at the named commits and material structured
  terms reconciled mechanically.
- Registered permissions and lifecycle rules were enforced.
- Replay, projection rebuild, and views were deterministic for the named inputs.
- Protected result paths remained additions-only in the compared history.
- The named custody and recovery procedures worked during the bounded window.

## What it does not prove

- Research truth, evidence persuasiveness, forecast quality, or actor competence.
- That every native research action was submitted.
- Coverage outside the one selected record and explicit command inventory.
- Safety with multiple machines, multiple writers, automation, or higher volume.
- Readiness for Gate D or any authority switch.

## Prohibited behavior

- Recursive scanning of live agent or repository directories.
- Mutable drafts entering the durable submission path.
- Automatic acceptance, commit, push, watcher, cron, or CI writing.
- Processing a path, actor, record, command, family, or policy not named in the
  activation packet.
- Editing or deleting accepted events or rejected receipts.
- Treating `.rw/`, registered views, or Kernel events as native authority.
- Hiding `EXCEPTION`, `UNKNOWN`, unprocessed commands, conflicts, or audit gaps.
- Continuing after any stop condition without an explicit disposition.

## Stop and recovery contract

The stop conditions in `GATE_C_READINESS_PLAN.md` are mandatory. On stop:

1. process no next command;
2. preserve every durable file and diagnostic;
3. do not modify or delete a result to repair the failure;
4. report the exact completed, rejected, waiting, and unprocessed inventory;
5. rebuild from durable inputs when safe to determine whether state reproduces;
6. present Will with continue, remediate, or end options; and
7. require a new ruling before resuming if the approved perimeter changes.

## C1 exit criteria

C1 is complete only when Will explicitly approves or amends:

- the one-record, maximum-three-command boundary;
- the exact writable paths;
- roles and custody separation;
- proof and non-proof claims;
- prohibited behavior; and
- stop/recovery behavior.

Approval of C1 is not approval of C2 installation or C7 activation.
