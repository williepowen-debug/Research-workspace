# Direct Messaging v1 — Implementation Status

**As of:** 2026-07-14  
**Branch:** `codex/messaging-design-rationale`  
**Activation:** LOCKED

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

## Safety boundary

The committed `MESSAGING/config.yaml` uses `write_mode: disabled`. The CLI implementation accepts writes only when a temporary test repository explicitly sets `write_mode: test`. It has no live-write mode.

The tooling does not commit, push, alter agent instructions, reassign work, escalate automatically, or write to WALTER-owned files.

## Known pre-activation limitations

- Composer currently creates one recipient obligation per invocation. Multi-obligation authoring remains to be added before broad activation.
- PROME and WILL incoming destination rules remain intentionally unresolved; the CLI refuses to guess them.
- Legacy direct and WALTER adapters are not yet implemented.
- Generated open-work and health views are not yet implemented.
- Root and agent instructions have not been reconciled for activation.

## Next build gate

Before live activation:

1. Add multi-obligation and multi-recipient composition while preserving recipient-specific state.
2. Resolve PROME's incoming-message destination contract.
3. Build read-only legacy/WALTER adapters.
4. Build generated open-work and health views.
5. Run a full dry run against a disposable copy of repository structure.
6. Reconcile canonical root and agent instructions in one reviewed activation change.

