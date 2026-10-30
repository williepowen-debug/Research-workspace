# Bounded pilot adapter contract — candidate for owner acceptance

October 30, 2026. Will selected **A** for WQ-555 in CATO's session after the explanation of the supervised test. The approval applies to one non-trade decision, with matching confirmation in PROME chat before integration. It does not answer the eventual L884 question, adopt a general source-authority switch or waive independent review.

PROME's owner disposition is `93d611559`, `AGENTS/CATO/inbox/2026-10-30_from-PROME_decisions-mvp-owner-disposition.md`. The paths and receipt states below follow that disposition. The candidate adapters do not create pilot response/receipt directories in the real workspace. Source and receipt fixtures stay in temporary repositories. Actual enablement awaits PROME's bounded pilot source contract and independent Opus acceptance.

## Acceptance properties before edits

- Read one explicitly selected, committed PROME proposal with one `wq-record` block; reject ambiguous blocks, unsafe paths, uncommitted edits, mismatched WQ/unit identity and a non-pilot dialect. The record includes complete choices, recommendations, conditions and original references. Preserve the real producer's fields; no truncation or inferred options.
- Freeze the exact displayed record and original source content in each response. Changes to either the proposal or its live queue row invalidate a pending answer. A new ruling or source failure cannot silently accept the old display. No queue write or authority transfer occurs.
- Export an existing saved event once under its own ID. Identical retries are harmless; changed bytes, symlink paths or a reused ID fail. No partial destination file is visible. Failed export does not destroy the saved local answer.
- Restore only committed response events into the other machine's store. Verify hashes, IDs, full selected option and prior-response chain. A foreign pilot, synthetic response, malformed event, missing predecessor, branched replies or local conflict fails visibly without partial import. Repeated import preserves the original timestamp and terms.
- Read PROME's committed receipt files without writing them. Match exact event ID/hash. States are `received`, `needs_clarification`, `rejected_stale`, `integrated`. A received event can advance to a final interpretation; conflicting final receipts fail. Integration must reference a canonical ruling and PROME's evidence that the separate chat confirmation matches the app response. This checks the owner's recorded assertion, not human identity or the truth of the chat independently.
- Distinguish saved, exported, committed locally and present in the last-fetched remote ref. None proves recipient acknowledgment or completed implementation. Read-only Git inspection does not fetch, commit or push. Missing remote evidence is unknown. Integrated receipts never imply completed work.
- Preserve existing fictional rehearsal behavior. Tests use temporary Git repositories and fictional response data. Production activation, authentication redesign, automatic Git, queue generation and an owner completion parser are outside this adapter batch.

## Candidate pilot source

PROME supplies the real WQ number and source path when the app is ready. The bounded pilot uses the existing record shape with `schema_version: wq-record/0.1-pilot`, `mode: supervised-pilot`, one independently answerable non-trade decision unit, and explicit A/B choices. This proposed dialect is for that pilot only; it is not adoption of the later general structured-record authority. PROME must accept the distinction before any real source is used.

The caller supplies the expected WQ/unit IDs. The source is a committed Markdown file under `PROME/proposals/` with exactly one `wq-record` JSON fence. A live queue row with the same WQ ID must exist exactly once and match its committed version. The queue remains authoritative. The adapter pins the full proposal bytes, record, queue-row bytes and source commit. It refuses locally edited source/queue terms. Existing evidence references must resolve at their pinned commits.

## Events and receipts

`decisions-response/1` contains `synthetic: false`, ID, saved timestamp, exact request and display snapshot, the full selected choice (or null for deferral/question), and the local-user identity limitation. `sha256` covers every field except itself. The snapshot carries the pilot's source path/commit, full original source and queue row, record and presentation hash. Only the app's explicit review/save creates a response; this contract file is no response.

The immutable event file is `AGENTS/CATO/decisions/responses/<event_id>.json`. CATO commits exact event paths under the adopted custody. PROME's separate receipt file is `PROME/decisions/receipts/<event_id>/<receipt_id>.json` with fields: `schema_version: decisions-receipt/1`, `id`, `response_id`, `response_sha256`, `state`, timezone-aware `at`, `previous_receipt_id` (null for the first), `canonical_ruling` (pinned path/commit or null), `chat_confirmation` (pinned path/commit or null), and `confirmed_response_sha256` (hash or null). An integrated receipt requires all three confirmation/ruling fields and the matching response hash. The referenced documents must be committed PROME proposal/ruling records. PROME records the actual matching confirmation; CATO never synthesizes it.

Receipt chains retain original events and reject forks. No receipt has a `completed` state. Actual owner follow-through remains a distinct source and a later visible integration step. An exported JSON event is not a receipt, and a receipt for one response cannot approve another.

## Owner handoff and remaining work

Record WQ-555 A with Will's exact word and the explained conditions. Resolve the bounded source contract above without activating the general source switch. Provide the L884 source/registered WQ when ready. PROME supplies actual receipts and arranges the required independent Opus counterexample review after CATO's adapter delivery. CATO then enables the accepted adapters through a reviewed launch path and launcher entry, observes the actual desktop/laptop path, and completes one real pilot. No new owner launch or live activation follows merely from fixture checks.
