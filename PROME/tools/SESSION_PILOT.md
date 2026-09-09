# Opt-in session pilot

Status: tested first slice, not fleet-wide activation. Evidence and rollout limits: [September 8 capability report](../reports/2026-09-08_session-pilot-results.md). Existing roster, orchestration, completion and messaging rules remain authoritative.

From the repository root, capture metadata with:

```bash
python3 PROME/tools/session_bridge.py > /tmp/prome-sessions.json
python3 PROME/tools/fleet_dashboard.py --sessions-json /tmp/prome-sessions.json -o /tmp/fleet_dashboard.html
```

The dashboard command also updates its existing local change-feed baseline. Inventory sees only its accessible PID namespace. A sandbox snapshot cannot establish host absence. Inspect `coverage`, `pid1`, timestamps and gaps. Process presence does not establish an active turn, and a persisted Claude blocked record without a PID does not establish a live process. No supplied Codex endpoint means UNKNOWN. The optional `--codex-socket` path is experimental: the Unix initialization pilot disconnected; it is not a verified connection recipe. The proven RPC transport is an explicitly owned stdio app-server process.

`session_bridge.py` is a library plus read-only inventory CLI. It does not launch desks, reserve capacity automatically, install hooks, resume owner sessions or dispatch messages from its CLI. `Rpc.stdio` explicitly creates an owned subprocess when a caller invokes it; closing that object stops that child. Never substitute a production session for a fixture without current roster and live-owner preflight. One RPC object supports one caller.

For an already authorized caller, `doorbell(rpc, journal, envelope)` requires `message_id`, `task_id`, `sender="PROME"`, `thread_id`, exact `cwd`, absolute existing `artifact`, and `mode="queue"` or `"steer"`. Steering also requires `expected_turn_id`. Artifacts retain the existing task and completion format; the envelope is only delivery metadata. Peer input grants no operator approval. The recipient must verify the artifact hash and its own authority before acting. Persistent idle queues can start immediately; there is no guaranteed staging period. Ephemeral queues are refused.

Use one explicitly selected local SQLite `Journal` for cooperating callers. A message ID binds the complete envelope, artifact content hash and endpoint. ACCEPTED means a matching runtime acknowledgment; it is not execution, verification, commit or consumption. ATTEMPTED/UNKNOWN after interruption must be reconciled against the recipient before any new message ID is considered. Restarting the client never automatically resends the old ID. Do not delete the journal to make a pending outcome disappear.

`reserve(limit, identity, owner, parent)` atomically enforces the first configured limit in that database. Unknown holders occupy slots; only verified dead generations are reclaimed. Use a canonical owner name. Keep and reuse the original returned `process_identity` token for `release`: transient process state is part of the current token comparison. Reservation does not authorize launch. There is no atomic reservation-to-child binding yet, and unregistered manual sessions/helpers are outside enforcement. Do not use this pilot to claim global spare capacity or set an eight-to-ten-session host limit.

Validation:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s PROME/tests -p 'test_session*.py' -v
```

Socket and multiprocessing cases require an environment that permits local sockets and semaphores. No model calls, accounts or market writes are needed for these tests.
