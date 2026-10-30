# Decisions MVP — storage, receipt and pilot plan

October 30, 2026. Will's direction to proceed survives the context handoff. CATO owns the app; PROME owns source adoption, interpretation of responses and canonical rulings. This plan makes the next implementation concrete; it does not activate live intake.

## First delivery and stopping point

One suitable real decision must travel from the displayed proposal through an unchanged saved answer/conditions, PROME's explicit acknowledgment and visible owner follow-through. Verify the path on desktop and laptop. The current implementation starts with a durable, fictional rehearsal using the existing draft record and pinned comparison reader. No new financial research or migration is needed to build that component.

## Storage and delivery

Use one immutable JSON file per response, containing its unique ID, complete displayed record, record hash, selected unit and full selected choice, unmodified note, deferral return condition, timestamp and previous-response reference. Store an immutable display snapshot before accepting its answer. A refresh must compare the actual record content, not just the author's revision number. Keep original responses when answers change. An identical retry returns the original event; reuse of an ID for different content fails.

For the rehearsal, SQLite transactions provide atomic saves, uniqueness and restart recovery in a local store; export produces self-contained JSON event files for transport. The database is machine-local and is never the file synchronized through Git. Test copies and synthetic acknowledgment events live only in that rehearsal. Proposed production paths: `AGENTS/CATO/decisions/responses/<event_id>.json`, with CATO committing exact exported event paths; `PROME/decisions/receipts/<event_id>/<receipt_id>.json`, with PROME committing its own receipt events. PROME keeps authored records in its existing proposal documents with a registered `wq-record` block and supplies the bounded live dialect/allowlist. These concrete paths and custody choices need owner adoption before creation or live use. No automatic app pull, stash, commit or push.

Distinguish local save, exported file, fresh-fetch-confirmed repository delivery, PROME acknowledgment, canonical interpretation and owner completion. Export alone proves neither delivery nor receipt. A lost HTTP reply is retried with the same event ID. A storage failure leaves the draft visible and reports failure. Source failure disables submission; it cannot become an empty queue. A stale display requires redisplay and review. Conflicting answers remain evidence, not last-write-wins authority.

## Identity and acknowledgment

Serve only on loopback; require the expected Host, same-origin mutation requests and a per-process browser capability. Do not put tokens in logs or permanent URLs. These controls prevent ordinary foreign web pages from submitting responses; they do not distinguish Will from another process running as the same OS user. Label rehearsal events synthetic. Before a real pilot, PROME and Will must explicitly adopt the supervised local-user trust boundary or choose stronger authentication. Never claim cryptographic proof of Will's identity from local file permissions or a Git commit.

PROME's eventual receipt references event ID and event hash, with one of received, needs clarification, rejected/stale or integrated. Receipt is distinct from canonical interpretation. Integration references the canonical ruling and exact conditions; completed implementation requires separate owner evidence. Re-delivery must not create a second ruling. Rehearsal receipts are explicitly synthetic and cannot enter production intake. The browser never manufactures a PROME acknowledgment.

## Source transition and existing conditions

Reuse the draft schema and three-copy reader. The current dialect permits design copies only; a live dialect and registered source perimeter are owner adoption work. Existing WQ records stay authoritative until that bounded transition is adopted. Preserve uncertain historical display provenance (WQ-C1); future snapshots bind the full shown record to each response without reinterpreting historic approvals. PROME selects one task identity for WQ-31/495 (M-495-3). Reuse the existing deferred return instruction and establish its read path. Before any generated queue replacement, compare with the last generated baseline and stop on direct edits; PROME reconciles those edits into the adopted source. Keep prior source/export for rollback and name the single active writer. No general queue writer is part of this first component.

## Pilot and acceptance before live enablement

PROME selects one new, low-consequence non-trade decision with explicit choices and a visible condition, and one personal-task or deferral case only if needed to exercise the other path. Do not reuse a settled historical ruling as new approval. CATO supplies the app/event contract and tests; PROME supplies source/receipt adapters and meaning acceptance. Independent review must be obtained before live integration under applicable owner rules. No owner send or launch is implied by this plan.

Acceptance cases: normal answer survives restart with exact words; a response concerns only the selected unit; retries and process interruption cannot yield partial or duplicate acceptance; changed terms or a new ruling block the stale display; two overlapping replies cannot silently override each other; unknown/malformed records and receipts fail visibly; nonexistent or wrong-event receipt is rejected; receipt without completion cannot display completion; export/import preserves hashes; both computers show the same delivered event and acknowledgment through the actual handoff. Missing owner evidence stays unknown. Demonstrated usefulness is one real completed path, not passing fixtures.

Remaining live dependencies: PROME source/directory/trust/receipt adoption and the named source conditions; independent acceptance; launcher entry; actual desktop/laptop handoff; real pilot. These are explicit work items, not claims of completion by this rehearsal.
