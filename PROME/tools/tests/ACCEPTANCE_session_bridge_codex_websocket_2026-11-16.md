# Session bridge: read loaded Codex threads over the socket form the Codex app server actually speaks

Written before the edit, 2026-11-16 11:52 ET (session prome-6f). DOCKET line 907, "SESSION BRIDGE CANNOT TALK TO CODEX SESSIONS". `reads: 0`.

The defect, in its own terms: `PROME/tools/session_bridge.py` `Rpc.unix` writes newline-terminated JSON straight onto the Unix socket. The installed Codex app-server control socket speaks WebSocket over that Unix socket (an HTTP Upgrade, then one JSON-RPC object per text message). So `--codex-socket` never completes `initialize` and the inventory reads UNKNOWN even when Codex threads are loaded. Owner evidence: WALTER, 2026-10-31, `AGENTS/WALTER/research/2026-10-31_boot-repair/codex-inventory.json` (8 loaded threads read with the repo venv's `websockets` 16.0 `unix_connect`, metadata only). Scope: the existing adapter's transport and its read-only inventory. No new checker, no new dependency, no broader messaging.

Acceptance:
- A1. Against a server that speaks WebSocket over a Unix socket and answers `initialize`, `thread/loaded/list` and `thread/read`, the CLI with `--codex-socket <path>` prints a `codex` object carrying every loaded thread's id, sessionId, parentThreadId, cwd, source, status and canAcceptDirectInput, the endpoint and an observation time. Paged lists (`nextCursor`) are followed to the end.
- A2. Read-only by construction. Over the WebSocket transport the only requests that can be sent are `initialize`, `thread/loaded/list` and `thread/read`, and the only notification is `initialized`. Any other method is refused locally before a byte is sent. `doorbell()` given this transport refuses before it reads the recipient or writes the journal.
- A3. A request the server initiates (an approval, a credential or an input request) is answered with the existing refusal error, never affirmatively, and does not displace the response being waited for.
- A4. Never starts a daemon. A missing socket path, a dangling symlink or a refused connection yields `codex.state` UNKNOWN with the error class; no subprocess is created.
- A5. Fails to UNKNOWN, never to a partial list presented as complete: a peer that does not complete the WebSocket handshake (for example a newline-JSON server), a binary message, malformed JSON, a non-object message, a message over the existing 4,000,000-byte cap, a response deadline, a disconnect after a request, a thread whose read returns a different id, a malformed list, a repeated cursor.
- A6. The module still imports, and every existing caller still runs, under a Python without the `websockets` package (`session_presence.py` and DAEDALUS's `fleet_view.py` import it). Without the package the WebSocket path raises the bridge's own error and the CLI prints UNKNOWN naming the remedy (run with the repository's `.venv`).
- A7. Unchanged: `Rpc.unix` (newline JSON), `Rpc.stdio`, `doorbell` over those transports, the journal and the capacity reservations. The existing 35 tests pass unmodified.
- A8. The output keeps saying what it does not establish: loaded threads on this one server only. An empty thread list, or UNKNOWN, is never an absent-desk verdict and authorizes no launch (the Desk-spawn preflight in `PROME/CLAUDE.md` owns that).
- A9. Live leg: against the installed Codex control socket with at least one loaded thread, the CLI lists it. PENDING · UNVERIFIED unless a Codex app server is running when the test is made; PROME does not start one for the test.

Neighbours:
- Ordinary: A1.
- Overlap: A7 with A1 (two transports in one module; the newline form still works and the caller chooses explicitly, no guessing between them); a list that changes between `thread/loaded/list` and `thread/read` (A5, identity mismatch).
- Wrong owner: A2 and A3 (the transport must not be able to write into someone else's session, and must not approve on anyone's behalf). The endpoint is identified only by its path, as before; this repair adds no identity check of the server and says so.
- Missing information: A4, A6, and a thread record lacking fields (rendered as null, as before).
- Concurrent activity: the server closing mid-inventory (A5). One RPC object, one caller, as before; no shared state is added.

Required result: tests for A1 to A7 against a local fixture server in `PROME/tests/test_session_bridge.py`; the existing tests unmodified and passing; `PROME/tools/SESSION_PILOT.md`'s sentence calling `--codex-socket` an unverified recipe replaced by what is now true and what is not; an independent reader devising its own counterexample before the repair is called fixed (a preflight instrument).

## Result

(written after the edit)
