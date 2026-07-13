# Direct Messaging v1 Implementation Plan

**Planning principle:** deploy useful capability in slices, but do not pause for a multi-week observation pilot. New direct messages transition network-wide once the minimum slice is ratified and tested.

## Phase 0 — Ratify the contract

Actions:

1. Will dispositions the recommended choices in the specification §16.
2. Record the decision in the canonical decision surface.
3. Reconcile root `CLAUDE.md` so the current “do not build” restriction points to the ratified v1 effort rather than blocking it.
4. Name PROME as operational owner of the shared direct-message contract; preserve WALTER ownership.

Exit condition: no conflict remains between the proposal and canonical repository instructions.

## Phase 1 — Build the minimum useful slice

Add under root `MESSAGING/`:

- Ratified specification and templates.
- Machine-readable constrained schemas.
- Agent-ID lookup sourced from `PROME/ROSTER.md` rather than a duplicated live roster.
- Sender CLI that allocates IDs, validates envelopes, and writes a preview.
- Validator for message and receipt files.
- Test fixtures for ACTION, INFO, multi-obligation, supersession, and invalid cases.

Safety properties:

- Preview by default.
- Explicit confirmation or `--write` required to deliver.
- Writes only to the addressed recipient's permitted inbox path.
- Never edits WALTER files.
- Never commits or pushes automatically in v1.
- Duplicate ID or path fails closed.

Exit condition: all fixtures pass and messages remain usable by an agent without running the tool.

## Phase 2 — Build recipient receipts

Add:

- Receipt initializer for a recipient's own obligation.
- Append-event command.
- Lifecycle transition validation.
- Required fields for BLOCKED, DEFERRED, INTEGRATED, and NO_CHANGE.
- Idempotent behavior when the same event request is repeated.

Exit condition: a complete ACTION can be routed, accepted, completed, and integrated with evidence without manually editing structured metadata.

## Phase 3 — Build compatibility adapters

Adapters:

1. New direct v1 messages and receipts.
2. Legacy direct packets with deterministic `LEGACY-...` IDs.
3. WALTER native signals, deliveries, and consumption evidence with `SIG-W` preserved.

Fixed regression cases from the baseline:

- 47 WALTER messages.
- 103 WALTER recipient obligations.
- 29 obligations in the historical seven-agent comparison cohort.
- Five invalid WALTER timestamps reported, not silently repaired.
- Five source items in the BRENT legacy packet represented without collapsing their independent outcomes; normalization may couple item 5 to item 1 but must preserve provenance.
- PROME's missing board log treated as an instrumentation gap, not non-consumption.

Exit condition: adapter outputs reproduce the baseline counts and caveats.

## Phase 4 — Generate views and diagnostics

Create rebuildable outputs such as:

- `OPEN_ACTIONS.tsv`
- `BLOCKED_AND_DEFERRED.tsv`
- `AWAITING_INTEGRATION.tsv`
- `RECENTLY_CLOSED.tsv`
- `MESSAGING_HEALTH.md`

Views must include source lane and evidence tier. They must never be manually maintained or treated as research canon.

Diagnostics initially report only. Suggested severity:

- HIGH: duplicate ID, wrong recipient path, invalid ownership, broken receipt reference.
- MEDIUM: overdue required disposition, invalid transition, integration claim without evidence.
- LOW: optional INFO unacknowledged, legacy ambiguity, noncanonical filename.

Exit condition: deleting generated views and rerunning produces equivalent results from source records.

## Phase 5 — Activate network-wide compatibility rollout

Cutover rules:

1. All newly created direct ACTION messages use v1.
2. New direct INFO uses v1 when practical; truly ephemeral session chatter remains ephemeral.
3. All active agents may send directly; PROME and WALTER are not mandatory relays.
4. Existing inbox files remain valid and are not rewritten.
5. WALTER continues unchanged.
6. ACTION recipients create recipient-owned receipts at their next normal processing session.
7. Generated exception views inform Will/PROME; no automatic reassignment or escalation.

The initial compatibility window should last long enough to catch normal agent boot cycles, but implementation proceeds immediately; the window is for refinement, not a go/no-go pilot.

Exit condition: current direct ACTION traffic is represented consistently and old traffic still processes normally.

## Phase 6 — Reconcile agent instructions

After tooling is verified, update each active agent's instructions mechanically and narrowly:

- How to create a direct ACTION or INFO message.
- How to process a v1 message.
- Where to write receipts.
- How to record BLOCKED, REJECTED, NO_CHANGE, and INTEGRATED.
- Explicit statement that WALTER signals continue under WALTER's own rules.

Avoid copying the entire specification into every agent. Agent instructions should link to the shared contract and contain only boot/closeout actions necessary for that agent.

Exit condition: no agent-local rule contradicts the shared contract.

## Acceptance-test matrix

| Test | Expected result |
|---|---|
| Valid ACTION | Unique IDs, correct inbox path, required receipt |
| Valid INFO | No requested action; optional receipt |
| Mixed packet | Separate obligation states |
| Multi-recipient copy | Same message ID, recipient-specific obligations |
| Duplicate delivery | No duplicate obligation or effect |
| Wrong recipient writes receipt | Rejected |
| ACTION lacks definition of done | Rejected |
| Invalid minute/timezone | Rejected |
| BLOCKED lacks next review | Rejected |
| INTEGRATED lacks target/effect | Rejected |
| NO_CHANGE with rationale | Valid terminal outcome |
| Supersession | Old obligation closes only through valid reference |
| WALTER ingestion | Preserves `SIG-W`; makes no WALTER writes |
| Legacy direct ingestion | Labeled inferred; silence remains unknown |

## Rollback

Rollback must be boring:

1. Stop sender/receipt hooks and generated-view jobs.
2. Return to ordinary readable inbox processing.
3. Leave already delivered messages and receipts in place as historical evidence.
4. Do not delete or rewrite WALTER, inbox, board, or research records.
5. Record why activation was paused and which compatibility issue triggered rollback.

Because v1 retains the inbox as transport, rollback does not strand the underlying message content.

## Recommended build sequence for the next implementation session

1. Ratify the §16 defaults.
2. Install the four design documents under root `MESSAGING/`.
3. Define schemas and fixtures.
4. Build validator before sender writes.
5. Build sender in preview-only mode.
6. Build receipt events.
7. Reproduce the baseline with adapters.
8. Add generated views.
9. Review one end-to-end dry run.
10. Activate new direct ACTION messages network-wide and reconcile agent instructions.

