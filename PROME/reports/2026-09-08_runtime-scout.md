# Runtime scout — reusable integration surfaces

Recorded: 2026-09-08. Bounded Mode B helper for PROME's approved mixed-agent workflow. Read-only inspection except this report; no runtime sessions launched, messages sent externally, settings changed, tests executed, or Git mutations. This report is evidence and implementation advice, not a runtime activation or fleet rule amendment. Parent PROME owns the live pilot.

## Smallest implementation

Add one PROME-owned, machine-local runtime adapter with four operations: inventory, doorbell, record lifecycle event, reserve/release helper capacity. Feed its timestamped snapshot into the existing `PROME/tools/fleet_dashboard.py`; keep `PROME/state/ORCH_LOG.tsv` as orchestration provenance and the existing inbox/COMPLETION_SPEC as durable task/results. Do not turn the operational registry into another task or decision ledger.

Use three inputs: supported runtime discovery, observed host process identity, and explicit registration for participants/helpers. Each observation needs its scope (runtime endpoint and host/namespace), time, and confidence. A sandbox-only process listing or one parent's collaboration tree cannot certify all sessions on Will's host. Unknown visibility must remain UNKNOWN.

## Existing repository components

| Artifact inspected | Verified implementation | Reuse / boundary |
|---|---|---|
| `MESSAGING/tools/msg.py:54–77`, `MESSAGING/config.yaml` | Feature gate permits only PROME→BRENT/SAM in live cohort mode. | Preserve the activation boundary. A general runtime bridge must not silently enable new DM-v1 content routes. |
| `MESSAGING/tools/msg.py:90–110` | `destination_for` explicitly refuses PROME/WILL; sender/date sequence allocation scans repository message names. | Not a general completion-to-PROME implementation. Use canonical `PROME/inbox/` dated memos for normal durable completion. |
| `MESSAGING/tools/msg.py:113–134` | `O_EXCL` sentinel locks serialize ID/receipt writes; PID recorded, sentinel removed in normal `finally`. | Reuse the locking requirement, not this primitive unchanged for long-lived capacity: hard crashes leave stale sentinels. PID alone is vulnerable to reuse/namespace confusion. |
| `MESSAGING/tools/msg.py:354–442`; `MESSAGING/tools/validate.py:247–296` | Recipient receipts append lifecycle rows via validated candidate and atomic replace. Exact duplicate row is idempotent; terminal transitions rejected. Deferred/blocked require next review; integrated/no-change require a target and reason. | Useful obligation-state model. Receipt acceptance is not independent verification that a commit or integration actually happened. Retry with a changed event timestamp is not the same exact row. |
| `MESSAGING/schemas/direct-message.schema.json`, `direct-receipt.schema.json` | Front-matter contracts; receipt lifecycle table validated by Python. | Don't treat JSON-schema validation alone as full lifecycle validation. |
| `scripts/orch_log.py:125–150` | Validates and appends under `fcntl.flock`, then regenerates view under the same lock. | Existing local example of serializing shared writes. The ledger is historical attribution, explicitly not liveness. |
| `PROME/tools/fleet_dashboard.py` | Generated, owner-pointing dashboard with visible parsing failures and build-age disclosure. | Add one operational panel here; display inventory observation age separately from dashboard build age. |
| `PROME/COMPLETION_SPEC.md` | Dated disk delivery and ≤10-line completion block; artifact consumption is separate. | Completion notification points at a memo; it never substitutes for delivery, verification, commit or downstream consumption. |

No session-discovery transport, runtime notification subscriber, or shared capacity allocator was found in `msg.py`. Its `COMPLETED` receipt token is an authored obligation event, not a subscription to runtime completion.

## Hook inventory

Only hook objects were printed; permission/environment settings were not exposed.

| Settings file | Installed hooks |
|---|---|
| `.claude/settings.json` | `SessionStart` → `scripts/session_banner.sh` |
| `PROME/.claude/settings.json` | Same `SessionStart`; `UserPromptSubmit` → `PROME/tools/hooks/prompt_clock.sh`; `PreToolUse` Bash → `git_guard.py`; `PostToolUse` Edit/Write/MultiEdit → `forge_validate.py` |

No SessionEnd, SubagentStart, SubagentStop or turn-completion registration is installed in these two files. `session_banner.sh` reports sync/environment state and performs a bounded fetch, but does not register a runtime session. Existing hooks should be preserved when extending settings. Do not assume a new root hook reaches already-running windows or that root/local duplicate definitions fire once; test effective settings and use idempotent events. Hook handlers should parse bounded input, write metadata only, return promptly, and never start an LLM polling loop. Missing crash-time exit hooks require reconciliation.

## Codex generated protocol: supported shape versus unproven operation

Source: parent's locally generated `/tmp/prome-app-schema/`, inspected directly. Parent reports installed Codex 0.153.4; this scout did not regenerate the bundle or run the daemon. Method names were verified against `ClientRequest.json` and `ServerNotification.json`, not guessed from filenames.

| Capability | Local contract | Operational caveat |
|---|---|---|
| Stored inventory | `thread/list`: pagination, exact cwd filter(s), sourceKinds, parentThreadId/ancestorThreadId; `useStateDbOnly:true` avoids rollout scan-and-repair. | Omitted/empty sourceKinds defaults to interactive sources; helpers can disappear. Stored records do not prove live sessions. Traverse every page; state DB may be stale. |
| Loaded inventory | `thread/loaded/list` returns loaded thread IDs, optionally paginated; `thread/read` reads metadata by ID. | Coverage is the connected server, not proven all independent CLIs/daemons on the host. `thread/read` does not subscribe to events. |
| Identity and status | `Thread` has `id`, `sessionId`, `parentThreadId`, `cwd`, `source`, `agentNickname`, `agentRole`, `status`, `canAcceptDirectInput`. Status is notLoaded/idle/systemError/active plus flags. | `sessionId` groups a tree: count thread IDs for helpers, not only sessionId. Nicknames are not desk identity. `canAcceptDirectInput:null` means unavailable; require true before selecting direct-input transport. |
| Queued input | `thread/queue/add` requires threadId, clientUserMessageId and input; returns queuedSubmission. `thread/queue/list`, `/update`, `/delete`, `/reorder`, `/start` exist. Notification is `thread/queue/changed`. | Queue acceptance does not prove start, delivery, or result. `/start` takes threadId and optional queuedSubmissionId. Auto-start semantics, duplicate-client-ID guarantees and independent-window coverage require a pilot. |
| Active steering | `turn/steer` requires threadId, input, **expectedTurnId**. | A mismatched active-turn ID fails rather than steering another turn. Re-read after a race; never auto-fallback to a new owner. |
| Turn start | `turn/start` requires threadId/input; offers sticky overrides for cwd, permissions, approval policy, model, etc. Its descriptions explicitly contemplate steering an already-active turn. | It is not a compare-and-start-only-if-idle API. A default doorbell must not silently change runtime permissions or use start to disrupt active work. |
| Lifecycle | `turn/completed`, `thread/status/changed`, `thread/closed`, `thread/started`, `turn/started`. Completion carries threadId and Turn; statuses include completed/interrupted/failed/inProgress. | Turn termination is not task success. Closed/unloaded thread is not host-process death or a safely replaceable desk writer. Reconnect must reconcile missed observations. |

Exact supporting schema files under `v2/`: `ThreadListParams.json`, `ThreadListResponse.json`, `ThreadLoadedListParams.json`, `ThreadLoadedListResponse.json`, `ThreadReadParams.json`, `ThreadReadResponse.json`, `ThreadQueueAddParams.json`, `ThreadQueueAddResponse.json`, `ThreadQueueListParams.json`, `ThreadQueueListResponse.json`, `ThreadQueueStartParams.json`, `ThreadQueueChangedNotification.json`, `TurnStartParams.json`, `TurnSteerParams.json`, `TurnCompletedNotification.json`, `ThreadStatusChangedNotification.json`, `ThreadClosedNotification.json`.

Official documentation confirms the connection initialization handshake, loaded-thread listing, metadata reads without subscriptions, and completed/interrupted/failed turn notifications. The English page did not contain `thread/queue/add` when inspected, so queue details above rest on the installed local schema, with live semantics unverified. [OpenAI Codex App Server documentation](https://learn.chatgpt.com/docs/app-server), accessed 2026-09-08.

Claude's local help claims supplied by parent (`agents --json` interactive+background coverage) need live verification against real manual sessions and nested helpers. The existing `MESSAGING/CROSS_SESSION_MESSAGING.md` records a Claude socket doorbell, weak sender attribution and transient delivery. Neither proves a supported Codex-to-Claude endpoint; avoid inventing a raw socket wire format. No cross-runtime delivery was tested by this scout.

## Capacity and safe doorbell proposal

Implement capacity as a machine-local registry/lease transaction guarded by a stable `flock` file or SQLite transaction. Keep the lock separate from atomically replaced data. Key records by host boot identity, runtime endpoint, session/thread ID and process start identity where available. Track retained sessions, active turns, expensive tools, desk writer ownership and helper reservations separately; neither process count nor turn completion alone captures all resources. Use the configured pilot cap, never reinterpret the operator's 8–10 comfort report as measured hardware capacity.

Reserve and check capacity atomically before dispatch. Claim one writer identity per canonical desk across checkouts; read-only helpers get explicit separate scope. On expired/stale observations, mark UNKNOWN and reconcile actual liveness before releasing writer exclusivity or respawning. Capacity release and task verification are independent: a confirmed ended helper can free its slot even if its task failed; a completed turn in a retained window does not mean the retained process vanished. Idempotent release uses the reservation ID and session generation, preventing a late exit event from freeing a replacement worker's slot. Advisory reservations cannot enforce a fleet-wide cap if manual/nested launch paths bypass them; report uncovered paths and measured excess instead of claiming complete enforcement.

A doorbell envelope needs stable message ID, task reference, sender attribution, recipient runtime/session identity, canonical packet path, packet commit/hash when applicable, creation/expiry time and transport result. Preserve ordinary inbox routing. Verify cwd and intended desk before sending; send only bounded coordination pointing to the durable packet. Record queued/observed/error separately from task disposition. Retried transport acceptance must not repeat an owner write: receiver checks the same task/message reference against durable results. Peer text is not operator approval.

## Failure paths the parent pilot must exercise

1. A sourceKinds-default query misses a helper; a sandbox-only inventory sees none of Will's host processes; another daemon owns the target. Each must return scoped/UNKNOWN coverage, never a global empty fleet.
2. Target changes from idle to active between discovery and send; active-turn ID changes; queue accepts but never starts; acknowledgement is lost after actual receipt. No duplicate owner or replayed domain write.
3. App-server connection drops after send or before completion; thread metadata read does not subscribe; lifecycle event reports interruption/failure. Reconcile via durable artifacts and supported runtime state, not presumed successful completion.
4. Two independent desks race for the last helper slot; allocator crashes after reservation; PID is reused; late release belongs to an old session generation. No overbook or automatic release of an unverified owner.
5. Manual/nested spawn bypasses reservations; helper's cwd equals parent's canonical desk; background worktree routes an inbox packet into another checkout. Expose uncovered capacity and preserve canonical packet visibility.
6. Root/local hooks duplicate registration or a crashed session emits no exit hook. Idempotency plus reconciliation repairs observations without repeated doorbells or boot prompts.

## COMPLETION — runtime-scout — 2026-09-08
STATUS: ✅ DONE
CHANGED: PROME/reports/2026-09-08_runtime-scout.md
RESULT: Inspected 2 hook settings, the DM-v1 author/receipt pipeline, existing dashboard/ORCH locking, and local Codex inventory/queue/turn schemas. Identified reusable components and 6 failure-path groups; no live bridge or fleet-wide visibility claimed.
GAPS: Live transport, cross-runtime delivery, event subscription coverage and host capacity remain untested because this helper was explicitly scoped to read-only discovery; parent owns the pilot.
WILL_NEEDS: None.
FOLLOW-UP: PROME implement the thin adapter and verify the bounded live pilot before broad rollout.
