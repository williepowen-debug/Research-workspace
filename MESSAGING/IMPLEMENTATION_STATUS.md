# Direct Messaging v1 — Implementation Status

**As of:** 2026-07-14  
**Branch:** `codex/messaging-design-rationale`  
**Activation:** FIRST COHORT — PROME → BRENT / SAM ONLY

## Completed on the design branch

- Ratified v1 defaults and authority boundary.
- Machine-readable message and receipt schemas.
- Read-only message/receipt validator.
- Preview-only single-obligation message composer.
- Sender/date stable ID allocation.
- Atomic allocator lock and collision failure.
- Temporary-repository delivery simulation.
- Recipient-owned receipt initialization.
- Append-only receipt events.
- Atomic receipt replacement and per-receipt lock.
- Idempotent duplicate delivery/event handling.
- Lifecycle, evidence, ownership, path, and provenance validation.
- End-to-end temporary-repository tests.
- Multi-obligation, multi-recipient composition with atomic fanout.
- Recipient-scoped live allowlist for PROME → BRENT and PROME → SAM.

## Safety boundary

The committed `MESSAGING/config.yaml` uses `write_mode: cohort`. It permits only PROME → BRENT and PROME → SAM. All other senders and recipients fail closed. Temporary repositories may use `write_mode: test`.

The tooling does not commit, push, alter agent instructions, reassign work, escalate automatically, or write to WALTER-owned files.

## Known pre-activation limitations

- PROME and WILL incoming destination rules remain intentionally unresolved; the CLI refuses to guess them.
- Legacy direct and WALTER adapters are not yet implemented.
- Generated open-work and health views are not yet implemented.
- Root and agent instructions have not been reconciled for activation.

## Next build gate

Before live activation:

1. Observe the two first-cohort messages through recipient disposition and closeout.
2. Resolve PROME's incoming-message destination contract.
3. Build read-only legacy/WALTER adapters.
4. Build generated open-work and health views.
5. Review the cohort before expanding the allowlist.
