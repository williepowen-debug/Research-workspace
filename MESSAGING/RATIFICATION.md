# Direct Messaging v1 Ratification Record

**Decision-maker:** Will  
**Decision date:** 2026-07-13  
**Decision:** Approved the recommended defaults in `DIRECT_MESSAGING_V1_SPEC.md` §16.  
**Scope authorized:** Design-branch implementation, schemas, fixtures, read-only validation, adapters, and generated-view development.  
**Not yet authorized by this record:** Live agent-instruction cutover, automatic inbox writes, automatic commits/pushes, automatic escalation/reassignment, or changes to WALTER-owned behavior.

## Ratified defaults

- Root `MESSAGING/` shared location.
- Network-wide compatibility rollout for new direct messages after activation; no long pilot.
- Readable Markdown plus constrained YAML front matter.
- `MSG-<SENDER>-<YYYYMMDD>-<NNN>` message IDs.
- One lifecycle state per message × recipient × independently decidable obligation.
- Required receipts for ACTION; optional receipts for INFO unless requested.
- Recipient-owned receipt storage.
- Exact target path plus effect required to claim integration.
- Native, read-only WALTER adapter with no duplicate IDs or receipts.
- Baseline/on-demand historical backfill only.
- PROME as proposed operational owner, subject to canonical root-rule reconciliation at activation.
- No automatic escalation in v1.
- ISO 8601 explicit deadlines plus `next_boot` as a first-class due value.

## Activation gate

Before v1 changes live agent behavior:

1. Validator and fixtures pass.
2. WALTER compatibility is demonstrated without WALTER writes.
3. Root and agent instructions are reconciled in one reviewed activation change.
4. Rollback is demonstrated.

