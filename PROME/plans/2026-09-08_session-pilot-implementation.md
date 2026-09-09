# Session pilot implementation — September 8

Scope: implement and test the first bounded slice of the approved six-area plan, before any fleet-wide rollout. Work stays in PROME/tools, PROME/tests and dated PROME reports. Existing orchestration and messaging canon remains authoritative. No domain writer is launched by the tools in this slice.

## Proposed implementation

1. Read-only inventory: combine host process identity (PID plus start ticks, cwd, runtime), Claude agents JSON, explicit Codex app-server loaded threads, and an optional native-helper snapshot. Mark coverage gaps UNKNOWN. Persisted blocked records without a PID do not prove a running process. A process does not prove a turn is active. Enumerate pagination; do not read conversation content or credential values.
2. Small JSON-lines RPC client: connect to an explicitly supplied local Codex socket or owned stdio process, initialize, correlate replies, retain lifecycle events and reject unexpected server approval requests. Never grant an approval. Inventory uses read-only methods only. Pilot uses new isolated threads; no automatic resume of an existing owner. No daemon bootstrap/restart or global settings changes.
3. Coordination envelope: stable task/message IDs, sender explicitly PROME (peer coordination, not Will), intended session/cwd, artifact pointer and expected turn ID when steering. A transport receipt means accepted, never completed. Timeout after sending means UNKNOWN; do not retry automatically. Reject duplicate IDs and recipient mismatch before sending. No arbitrary remote endpoints. Durable content remains the existing packet lane.
4. Atomic capacity reservations in an explicitly named local SQLite database: caller-configured pilot limit, parent/helper linkage, unique owner-writer identity, live PID/start identity, no wall-time-only eviction. Dead processes release reservations; inaccessible processes remain UNKNOWN and occupy capacity. Reserving capacity grants no launch authority. Cooperative participants only; inventory explicitly exposes unregistered work. No claim that eight is a measured host limit.
5. Pilot lifecycle: lightweight invocation-specific hooks/event recording only for newly created test sessions, not changes to existing root/user hooks. Checkpoint and follow-up reuse the same test thread. Separate execution outcome from verification and Git durability. No polling LLM loops; completion comes from runtime events. Never interrupt a non-pilot session.
6. Worktree policy and recipe: use an isolated temporary Git fixture to prove separate indexes and explicit shared artifact routing. Do not make new production worktrees or alter research routing in this pilot. Operational adoption remains conditional on pilot evidence.

## Acceptance and failure cases

Exercise two isolated test sessions and one helper, with exact fixture cwd/session identity. Verify idle delivery, active steering, completion, unreachable recipient and recovery without duplicate owner. Test competing final-slot reservations, stale PID reuse, inaccessible liveness, duplicate IDs, changed payload under same ID, malformed responses and partial transport failure. Simulate direct operator reprioritization as a labeled FIXTURE, never as a real Will instruction. Approval requests fail closed. A failed or interrupted turn is not success. Inventory coverage is scoped to accessible runtimes; no missing provider can become a DARK assertion.

Claude-to-Claude native messaging and one-shot notices must be exercised if available. Codex-to-Claude socket payload shape is not yet established by the opened documentation; do not guess it or impersonate a Claude peer. Record a supported transport gap if a safe documented route cannot be demonstrated. Independent existing manual sessions are currently absent from the host process snapshot; test sessions cannot establish all manual-session recovery cases.

## Sources and invariants

Implementation interfaces: installed Codex 0.153.4 generated schema in /tmp/prome-app-schema; Claude 2.1.263 help; official App Server and cross-session messaging pages linked in the parent plan. The parent plan's claim that Claude agents JSON omits interactive sessions is superseded by current CLI help and official docs; verify in the pilot.

No trades, external sends, global permissions changes, credential output, owner grade, Gate C activation or canonical operating-rule amendment. Only explicitly created pilot processes may be stopped; no broad process kill. Keep evidence receipts and declared limitations. Tests must force failure behavior, not merely assert source strings.

Plan review, September 8: independent reader found no blocking contradiction. Declared advisory residue: reservation-to-child handoff/crash semantics require implementation evidence; deduplication and UNKNOWN must be checked across client restart; the final acceptance matrix must name deferred parent-plan cases, including manual-session recovery and measurements. A successful fixture run does not close these operational acceptance requirements.
