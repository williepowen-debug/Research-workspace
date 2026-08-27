# Gate C Checkpoint C2 — Root Git Carve-Out (Draft)

**Date:** 2026-08-26

**Status:** APPROVED AND INSTALLED 2026-08-26 — INACTIVE UNTIL C7

**Installed at:** root `CLAUDE.md` § Git Protocol, as carve-out ④ plus the PROME
scope note stated below; short fleet pointer in root `AGENTS.md`.

## Design constraints

- Preserve the existing default: each domain agent commits only its own directory.
- Grant agents only the submission path they already own.
- Give PROME custody of explicit Kernel result/view/policy paths without giving
  research authority.
- Require explicit file pathspecs; never authorize directory-wide staging.
- Make event and receipt history additions-only.
- Keep commits and pushes manual and subject to the existing Git protocol.
- Fail closed on shared-index ambiguity, unrelated dirty files, non-fast-forward
  state, modification/deletion, or multiple writers.

## Proposed root-canon wording

The following approved text was installed after carve-out ③ in root `CLAUDE.md`
§ Git Protocol.

> **④ Gate C Kernel shadow paths (inactive until a separate Gate C activation
> ruling):** after Will approves and activates a bounded Gate C pilot, a domain
> agent may create and commit only a canonical immutable command it authored at
> `AGENTS/<NAME>/outbox/kernel/submissions/<command_id>.json`. The path name,
> embedded `actor_id`, and command filename must agree; the agent must stage and
> commit the single explicit file path and may never edit or delete it after
> submission. This grant conveys submission only—never `command.accept`, Kernel
> custody, permission to edit `KERNEL/`, or research authority over another
> agent's record.
>
> PROME is the sole active Gate C acceptance custodian. Under an operator-approved
> activation packet, PROME may explicitly stage and commit only: approved Kernel
> schemas and policy/registry versions; new accepted events at
> `KERNEL/shadow/events/YYYY/MM/<event_id>.json`; new rejected receipts at
> `KERNEL/audit/commands/YYYY/MM/<command_id>.json`; and the four registered
> generated views under `KERNEL/views/`. Accepted events and rejected receipts are
> additions-only: modification, deletion, rename, overwrite, replacement, or
> history rewrite is a blocking integrity failure. View files are generated
> replaceable projections, not authority, and may change only through the
> registered deterministic renderer over the declared input perimeter.
>
> Every stage and commit uses exact file pathspecs. Never stage a submission,
> result, month directory, `KERNEL/`, `AGENTS/<NAME>/`, or `.rw/` as a directory;
> never use `git add .`, `git add -A`, a computed path list, or `git commit -a`.
> Kernel tools never commit or push automatically. Before a Kernel commit, prove
> one active writer, inspect the exact staged paths, run the registered
> additions-only and durable-result checks, and stop on unrelated staged changes,
> an unapproved path, `EXCEPTION`, or `UNKNOWN`. Existing non-fast-forward,
> no-force, no-amend, and shared-index rules remain unchanged.
>
> A substitute custodian receives no standing Git grant. Will must activate a
> pre-registered substitute for a named time window and command perimeter; the
> substitute uses the identical PROME path limits and acceptance binary, records
> its own `writer_id`, and loses the grant at the window's end. CI never becomes
> an acceptance writer. No timeout transfers custody.

## Proposed PROME scope-note amendment

The existing `CLAUDE.md` scope note now adds:

> During an explicitly activated Gate C pilot, PROME also owns the approved
> Kernel custody paths named in carve-out ④. This is mechanical shadow custody,
> not ownership of native research, a grant to edit agent submissions, or an
> authority switch. Outside an active packet, PROME may maintain Kernel code and
> planning documents under its approved workstream but may not process real
> records or write live results.

## Installation record

1. C1 was approved and the tree was clean and synchronized before installation.
2. The exact approved wording was inserted without changing carve-outs ①–③.
3. Root `AGENTS.md` received only a short pointer; root `CLAUDE.md` remains
   canonical.
4. `KERNEL/tools/git_policy_check.py` checks explicit instruction perimeters for
   directory-wide Kernel staging, automatic Kernel commit/push instructions, and
   agent grants to shared `KERNEL/` paths.
5. `KERNEL/tests/test_git_policy_check.py` covers safe explicit submission paths,
   each prohibited class, and negated prohibitions.
6. The installed instruction perimeter passes the new check.

No installation step may create submission, event, receipt, registry, or view
data for a real record.

## C2 exit criteria

- Will approves the exact root wording or supplies amendments.
- The installed wording has a dedicated commit and passes canon checks.
- No existing carve-out or agent ownership rule is weakened unintentionally.
- Root and pointer surfaces agree about activation, paths, custody, staging, and
  additions-only protection.
- Installation evidence states that live shadow remains inactive.

C2 installation is not C3 implementation approval and is never C7 activation
approval.
