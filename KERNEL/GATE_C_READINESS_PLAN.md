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

## Checkpoint record

| Checkpoint | State | Evidence |
|---:|---|---|
| C1 | APPROVED 2026-08-26 | `GATE_C_C1_PILOT_CONTRACT_DRAFT.md` |
| C2 | APPROVED / INSTALLED / INACTIVE 2026-08-26 | Root `CLAUDE.md` carve-out ④, root `AGENTS.md` pointer, `tools/git_policy_check.py`, and six synthetic tests |
| C3 | COMPLETE / PRIMARY PASS 2026-08-26 | `tools/gate_c_boundary.py`, eleven synthetic-mirror tests, and `GATE_C_C3_SYNTHETIC_BOUNDARY.md` |
| C4 | COMPLETE 2026-08-26 | RED registered dormant in `policies/custody-policy.json`; custody mechanism, fifteen synthetic tests, and `GATE_C_C4_CUSTODY.md` |
| C5 | COMPLETE 2026-08-26 | SAM-33 approved; SAM-owned companion committed at `1d9400425`; strict command and exact native-reference preflight pass |
| C6 | COMPLETE / INDEPENDENT PASS 2026-08-26 | `GATE_C_C6_REHEARSAL.md`; disposable two-command rehearsal, abort/retry/rebuild, audits, and remediated adversarial review passed |
| C7 | COMPLETE 2026-08-27 | RED independent review PROCEED (CHG-RED-050 RESOLVED, both findings closed by mechanism + probe-verified); activation `LIVE-2026-0001` Will-ruled in-session; pilot ran [16:30Z, 18:00Z) — 2 SAM-33 events accepted, 4 views, kernel commit `01478b659`, all step-8 checks PASS |
| C8 | COMPLETE / RULED **CONTINUE** 2026-08-27 | `GATE_C_C8_CLOSEOUT_PACKET_2026-08-27.md` (5 discrepancies); RED review `AGENTS/RED/reports/2026-08-27_KERNEL_GATE_C_C8_REVIEW.md` (integrity checks independently re-run PASS; 6 further findings N1–N6); Will's ruling `GATE_C_C8_RULING_2026-08-27.md`; all six conditions applied same day (runbook amended, suite 212 green post-fixture-fix, root enumeration reconciled) |
| **Sitting 2** (Increment-2 book + MIDAS-06 first resolution) | COMPLETE 2026-09-02 [14:00:15Z–14:13:08Z] / reviewer rec CONTINUE (DAEDALUS `08564edac`) — **RULED CONTINUE 2026-09-02 10:57 ET** (`GATE_C_C8_RULING_2026-09-02.md`; F carrier confirmed; three-outcome projection vocabulary (a) registered as the next build) | `GATE_C_C8_CLOSEOUT_PACKET_2026-09-02.md` (5 discrepancies, none silent; 17 events, 6 activations LIVE-2026-0007…0012, 0 refusals, grants promoted `a1fec819…`, six affirmative closes `78d8b5b37`); DAEDALUS review `AGENTS/DAEDALUS/reports/2026-09-02_C8_SITTING2_CLOSEOUT_REVIEW.md` (13 claims re-derived, 6 doc/process findings R1–R6). Owed to Will: WQ-149 F-carrier confirm · scoring vocabulary (MIDAS §4) · WQ-150 root-④ key (second live refusal) |

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

The bounded live-interface remediation is built and the disposable rehearsal
was repeated through the exact new interface (Will-authorized 2026-08-26; see
`GATE_C_LIVE_INTERFACE_REMEDIATION.md`). What remains, in order: an independent
adversarial review by a reviewer who is not the builder, in a separate sitting
(review brief in the remediation record); then a fresh C7 packet fixing exact
start and end timestamps; then Will's activation ruling. Do not create live
commands or results, activate custody, or begin shadow operation before that
ruling.
