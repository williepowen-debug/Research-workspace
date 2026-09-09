# Mixed-agent workflow: first implementation and pilot

September 8, 2026, laptop WilliePOwen. Will approved checking the remaining market obligations and then starting implementation. The [six-area plan](../plans/2026-09-08_mixed-agent-workflow.md) remains the full workstream; this report closes the [bounded pilot](../plans/2026-09-08_session-pilot-implementation.md), not fleet rollout. [Market pickup](2026-09-08_evening-market-checks.md) includes the later published SKEW reset.

## What is implemented

`PROME/tools/session_bridge.py` provides metadata inventory, a tested owned-stdio RPC client, persistent message deduplication, explicit target/turn checks and cooperative atomic reservations. The optional Fleet Ops panel renders a supplied snapshot with its own age and coverage. [Usage and constraints](../tools/SESSION_PILOT.md). No root settings, domain instructions or fleet launch routing changed.

## Capability and acceptance matrix

| Area | Observed result | Remaining acceptance |
|---|---|---|
| Codex delivery and completion | Two isolated persistent threads discovered by exact cwd; idle queue accepted and auto-started; completion event received; reopened journal suppressed duplicate delivery. | Independent Unix client disconnected during initialize. No live production endpoint discovery/attachment proven. |
| Active steering and direct operator priority | Expected-turn steering acknowledged; recipient verified the artifact and preserved its original higher-priority marker when peer instructions conflicted. Inactive steering refused. | Delivery and conflict handling passed; successful reprioritization was not demonstrated. No real operator approval was simulated as authority. |
| Claude native messaging | Two explicitly created CLI test sessions appeared in `claude agents --json` as interactive; ListAgents, SendMessage, receiver reply and one-shot idle notice verified in runtime receipts/transcripts. | No arbitrary existing manual desk recovery or documented raw socket bridge implemented. |
| Cross-runtime coordination | Codex controlled the supported Claude CLI streams and observed native Claude peer delivery/reply. | CLI-mediated fixture only; direct native Codex-to-Claude / Claude-to-Codex peer bridge remains unimplemented. |
| Inventory and shared capacity | Host metadata snapshot, endpoint-scoped Codex inventory and escaped optional dashboard panel; competing processes could not both reserve the final slot. PID reuse, foreign observer context and unknown holders tested. | Full manual/nested-helper census, registration, atomic reservation-to-child handoff and hook enforcement remain. Current database enforcement is cooperative only. Host memory is an observation, not a validated session limit. |
| Lifecycle and recovery | Runtime completion/idle events consumed; after stopping an owned Codex server, the same persisted test thread resumed with both prior context markers. UNKNOWN outcomes survive journal restart without resend. | Clean unload/resume only: crash/interruption recovery and production hooks not proven or installed. |
| Compact task/completion handoff | Stable message/task IDs, canonical artifact pointer/hash and explicit peer attribution; acceptance kept separate from execution. Existing completion canon retained. | No new fleet-wide completion format or automatic committed/consumed reconciler installed. |
| Context and independent review | Same-thread follow-up and resume recalled markers. Separate plan/result readers reviewed implementation and regression repairs. | No cost/context benchmark or fleet-wide reuse policy activation. |
| Selective worktrees | Temporary Git fixture proved separate indexes and explicit absolute shared-artifact routing. | No production worktree/merge, conflict recovery or shared Git lock integration. Research remains in its canonical tree. |

## Receipts and verification

- [Codex session pilot](2026-09-08_codex-session-pilot.json), [same-thread recovery](2026-09-08_codex-recovery-pilot.json), [Unix disconnect](2026-09-08_codex-unix-disconnect.json).
- [Ephemeral queue rejection](2026-09-08_codex-pilot-ephemeral-rejection.json) and [auto-start discovery](2026-09-08_codex-pilot-autostart-observation.json) are retained failed attempts, not success receipts.
- [Claude CLI/native pilot](2026-09-08_claude-session-pilot.json) and [receiver/idle transcript receipts](2026-09-08_claude-receiver-receipts.json). Actual pilot model resolved to claude-opus-5; Codex fixtures used gpt-6-astra. Tool uses were Read, ListAgents and SendMessage. Existing user configuration advertised additional connectors; none was invoked.
- [Host inventory](2026-09-08_session-inventory.json), [worktree fixture](2026-09-08_worktree-fixture.json), [runtime interface research](2026-09-08_runtime-scout.md).

All 26 bridge tests and nine panel tests passed. Tests cover partial/coalesced RPC frames, notification routing, approval-request rejection, disconnect/timeout, malformed results, exact recipient identity, mutation acknowledgment identity, restart deduplication, unknown capability, stale PID and atomic capacity contention. The four independent RESULT blockers were repaired and independently rechecked: observer context before PID absence; immutable database capacity; matching thread identity; validated mutation receipt. Panel review found no blocker. Tests were updated for the corrected response contract and rerun after that review's fixture warning.

Declared advisory residue: reservation release compares transient process state, so callers must retain the original identity token; using a fresh S/R-state sample can reject an otherwise rightful release. This fails closed. Unix framing/initialization remains undiagnosed. The independent-client failure is not evidence of an unavailable product capability. Every launched runtime was a bounded test process, stopped by exact owned-process handle; no production daemon restart or domain writer launch occurred.

## Next implementation checkpoint

Continue with one real manual session plus one nested helper, preserving both Will's direct conversation and PROME's peer coordination. First establish the documented shared endpoint/transport and complete inventory coverage, then bind cooperative reservations to child lifecycle and recovery. Require explicit target identity, no duplicate owner, observable completion and restart reconciliation before enabling automation. Subsequent slices cover completion consumption, context measurement and production worktree/Git integration. Eight-to-ten-session comfort remains an operator preference, not measured capacity.

Other desks wrote their own files concurrently during this run. Those files remain outside this implementation's staging and ownership. Missing FFIEC laptop credentials remain a boot limitation; this pilot and the completed market checks did not require them.
