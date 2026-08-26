# Gate C Live-Shadow Readiness Plan

**Date:** 2026-08-26

**Authorization:** Will authorized Gate C planning on 2026-08-26.

**Current state:** PLANNING ONLY — LIVE SHADOW NOT AUTHORIZED

## Objective

Prepare a bounded activation packet for one real, binary-question shadow pilot.
Native research remains authoritative. No planning checkpoint may import a real
record, scan a live submission directory, write a live event or receipt, install
the root Git carve-out, or activate a custodian without the approval stated for
that checkpoint.

## Pilot boundary

- One operator-selected native Question record and its exact committed resolver
  path.
- Binary Question/Forecast/Resolution family only; no threshold, conditional,
  interval, or `TEXT_ANCHOR` support.
- One shared worktree and one acceptance writer at a time.
- Manual invocation only; no watcher, scheduler, CI writer, automatic commit, or
  automatic push.
- Every generated output visibly states `SHADOW — NON-AUTHORITATIVE`.
- Native records remain authoritative and are never rewritten by the Kernel.
- Gate D and any authority switch remain out of scope.

## Readiness checkpoints

| Checkpoint | Work | Required evidence | Operator decision |
|---:|---|---|---|
| C1 | Freeze the pilot contract and threat boundary | Exact paths, roles, commands, exclusions, stop conditions, and proof/limitation table | Approve the bounded pilot contract |
| C2 | Draft the root Git carve-out | Exact root-canon wording; path ownership; explicit staging; additions-only event/receipt protection; no auto-commit/push | Approve and authorize installation of the carve-out |
| C3 | Build the live-compatible boundary without using real records | Explicit-inventory adapter, repository-safe locking, live-path guards, dry-run mode, labeling, and tests using synthetic mirrors | Approve technical readiness to select a record |
| C4 | Register custody | Active PROME custodian, named dormant substitute, `command.accept` disabled for substitute, bounded activation/revocation procedure, audit-after-return test | Approve custody policy and named substitute |
| C5 | Select one native pilot record | Operator supplies or explicitly approves one committed record, exact resolver, actor, family, and material-term mapping; read-only preflight reports no `UNKNOWN` | Approve that record for the activation packet |
| C6 | Rehearse the complete pilot | Disposable clone/worktree rehearsal from explicit inputs; deterministic replay/views; additions-only audit; recovery and abort drill; two-reader review | Accept readiness evidence or order remediation |
| C7 | Activation ruling | Signed checklist fixing record, commit, paths, writer, time window, command count, and stop conditions | Separately authorize one bounded live-shadow pilot |
| C8 | Pilot closeout | Results, receipts, discrepancies, burden, audit completeness, rollback/stop disposition | Continue, pause, remediate, or end Gate C |

Checkpoint C7 is the first point at which processing a real record may be
authorized. Completing C1–C6 does not activate shadow operation.

## Required implementation properties

1. Live input discovery is explicit and bounded. The operator-approved submission
   inventory is the perimeter; recursive repository scanning is prohibited.
2. Acceptance preserves the Gate B order: schema, dependency readiness,
   permission, exact native reference, lifecycle legality, and exactly one durable
   result under one lock.
3. The live writer uses the approved repository paths and refuses every path not
   named by the installed carve-out.
4. Accepted events and rejected receipts are immutable and additions-only.
5. A retry re-runs the full printed verification perimeter before returning a
   prior result.
6. Any required `UNKNOWN`, collision, conflict, missing result, audit gap, dirty
   unrelated worktree state, or custody ambiguity blocks aggregate green.
7. Rendering is deterministic and includes rejected receipts and unprocessed
   approved submissions in the declared source perimeter.
8. `.rw/` remains disposable; deletion and rebuild cannot lose authority.
9. Tools stage only explicit paths and never commit or push automatically.
10. The pilot can be stopped without modifying or deleting any durable result.

## Stop conditions

The pilot stops before the next command if any of the following occurs:

- a required check returns `EXCEPTION` or `UNKNOWN`;
- the selected native bytes or material terms do not reconcile;
- a duplicate, modified, deleted, or conflicting durable result is detected;
- the acceptance lock or single-writer assumption cannot be proven;
- an unapproved actor, path, family, policy version, or custodian appears;
- output lacks the shadow/non-authoritative notice;
- deterministic replay, view reproduction, projection rebuild, or additions-only
  verification fails;
- repository state would require staging unrelated paths; or
- Will pauses or revokes the pilot.

A stop preserves all existing evidence, produces no authority switch, and
requires an explicit disposition before resumption.

## Activation packet

Before requesting C7, the packet must contain:

- the approved root Git carve-out and installed commit;
- the exact native source commit, path, locator, and selected-byte hash;
- enabled family and policy versions;
- active and dormant-custodian registrations plus activation/revocation steps;
- the explicit submission/result/view path inventory;
- rehearsal commands and outputs, including all `PASS`/`EXCEPTION`/`UNKNOWN`
  perimeters and limitations;
- independent review reconciliation;
- pilot time window and maximum command count;
- stop, recovery, and closeout procedures; and
- a clear operator ruling line that authorizes only the described pilot.

## Immediate next action

Draft checkpoint C1's bounded pilot contract and checkpoint C2's proposed Git
carve-out for review. These are documents only. Do not install the carve-out,
inspect a real native record, or implement a live adapter until separately
approved.
