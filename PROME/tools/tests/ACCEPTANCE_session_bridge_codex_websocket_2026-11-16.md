# Session bridge: read loaded Codex threads over the socket form the Codex app server actually speaks

Written before the edit, 2026-11-16 11:52 ET (session prome-6f). DOCKET line 907, "SESSION BRIDGE CANNOT TALK TO CODEX SESSIONS". `reads: 2` (read 1 delivered 12:00 ET, read 2 of the fix diff delivered 12:07 ET; both by one independent reader; history under Result). No code, test or manual text changed after read 2.

The defect, in its own terms: `PROME/tools/session_bridge.py` `Rpc.unix` writes newline-terminated JSON straight onto the Unix socket. The installed Codex app-server control socket speaks WebSocket over that Unix socket (an HTTP Upgrade, then one JSON-RPC object per text message). So `--codex-socket` never completes `initialize` and the inventory reads UNKNOWN even when Codex threads are loaded. Owner evidence: WALTER, 2026-10-31, `AGENTS/WALTER/research/2026-10-31_boot-repair/codex-inventory.json` (8 loaded threads read with the repo venv's `websockets` 16.0 `unix_connect`, metadata only). Scope: the existing adapter's transport and its read-only inventory. No new checker, no new dependency, no broader messaging.

Acceptance:
- A1. Against a server that speaks WebSocket over a Unix socket and answers `initialize`, `thread/loaded/list` and `thread/read`, the CLI with `--codex-socket <path>` prints a `codex` object carrying every loaded thread's id, sessionId, parentThreadId, cwd, source, status and canAcceptDirectInput, the endpoint and an observation time. Paged lists (`nextCursor`) are followed to the end.
- A2. Read-only by construction. Over the WebSocket transport the only requests that can be sent are `initialize`, `thread/loaded/list` and `thread/read`, and the only notification is `initialized`. Any other method is refused locally before a byte is sent. (Tightened after read 1, finding 2: the message must have exactly the request shape, an integer id, only that method's parameter names, and `includeTurns` false on `thread/read`; no reply of any kind can be sent.) `doorbell()` given this transport refuses before it reads the recipient or writes the journal.
- A3 (AMENDED after independent read 1, finding 4; the first text said such a request "is answered with the existing refusal error"). A request the server initiates (an approval, a credential or an input request) is NEVER answered over this transport, not even with a refusal: on a shared control socket a reply could settle another session's pending request. It stops the read, and the result is UNKNOWN. Server notifications do not stop the read.
- A4. Never starts a daemon. A missing socket path, a dangling symlink or a refused connection yields `codex.state` UNKNOWN with the error class; no subprocess is created.
- A5. Fails to UNKNOWN, never to a partial list presented as complete: a peer that does not complete the WebSocket handshake (for example a newline-JSON server), a binary message, malformed JSON, a non-object message, a message over the existing 4,000,000-byte cap, a response deadline, a disconnect after a request, a thread whose read returns a different id, a malformed list, a repeated cursor. (Added after read 1, finding 1:) a server that returns a fresh cursor on every page, or answers slowly without end: one inventory is bounded by an overall deadline of 60 seconds and 50 pages, and exceeding either is UNKNOWN.
- A6. The module still imports, and every existing caller still runs, under a Python without the `websockets` package (`session_presence.py` and DAEDALUS's `fleet_view.py` import it). Without the package the WebSocket path raises the bridge's own error and the CLI prints UNKNOWN naming the remedy (run with the repository's `.venv`).
- A7. Unchanged: `Rpc.unix` (newline JSON), `Rpc.stdio`, `doorbell` over those transports, the journal and the capacity reservations. The 26 existing cases in `PROME/tests/test_session_bridge.py` pass unmodified (the first text said 35, which is the wider `test_session*.py` pattern: 26 bridge cases and 9 panel cases).
- A8. The output keeps saying what it does not establish: loaded threads on this one server only. An empty thread list, or UNKNOWN, is never an absent-desk verdict and authorizes no launch (the Desk-spawn preflight in `PROME/CLAUDE.md` owns that).
- A9. Live leg: against the installed Codex control socket with at least one loaded thread, the CLI lists it. PENDING · UNVERIFIED unless a Codex app server is running when the test is made; PROME does not start one for the test.

Neighbours:
- Ordinary: A1.
- Overlap: A7 with A1 (two transports in one module; the newline form still works and the caller chooses explicitly, no guessing between them); a list that changes between `thread/loaded/list` and `thread/read` (A5, identity mismatch).
- Wrong owner: A2 and A3 (the transport must not be able to write into someone else's session, and must not approve on anyone's behalf). The endpoint is identified only by its path, as before; this repair adds no identity check of the server and says so.
- Missing information: A4, A6, and a thread record lacking fields (rendered as null, as before).
- Concurrent activity: the server closing mid-inventory (A5). One RPC object, one caller, as before; no shared state is added.

Required result: tests for A1 to A7 against a local fixture server, in the new file `PROME/tests/test_session_bridge_ws.py` so the existing file stays byte-unmodified (the first text named the existing file); the existing tests unmodified and passing; `PROME/tools/SESSION_PILOT.md`'s sentence calling `--codex-socket` an unverified recipe replaced by what is now true and what is not; an independent reader devising its own counterexample before the repair is called fixed (a preflight instrument).

## Result

Recorded 2026-11-16 12:02 ET by PROME prome-6f. The four states, kept apart:

| State | What holds |
|---|---|
| IMPLEMENTED | bb4970ca69 (the transport, the CLI option, the manual paragraph) and the fix commit that carries this section (read 1's three blocking findings). |
| TESTED | The author's suite, counted by `grep -c 'def test_'`: 26 existing bridge cases unmodified, and the cases in `test_session_bridge_ws.py`; all pass under the repository venv; under the system Python the fixture-server cases are skipped and the rest pass. Against a local stand-in server only. |
| INDEPENDENTLY VERIFIED | YES, against a local stand-in server only, recorded 2026-11-16 12:07 ET. Read 2 (same reader, bounded to the fix commit 39f306de67, its own new counterexamples and eight mutations; ledger `PROME/reports/2026-11-16_session-bridge-ws-repair/LEDGER_read2.md`): 0 blocking, 3 non-blocking; read 1's findings 1, 2 and 3 each CLOSED by re-running its reproductions. Nothing was changed after read 2, so no fix is unreviewed. This does not cover the live leg. History: Read 1 (Agent-tool reader `bridge-ws-reader`, Opus, read-only, own fixtures and counterexamples; ledger `PROME/reports/2026-11-16_session-bridge-ws-repair/LEDGER_read1.md`) found 3 blocking and 8 non-blocking. The fixes below were made after read 1 and reviewed by read 2. |
| STILL UNRESOLVED | A9, the live leg: PENDING · UNVERIFIED. No Codex app server was running (the control-socket symlink's target was missing at 11:54 ET) and PROME did not start one. Against the real path the CLI printed `codex: UNKNOWN, FileNotFoundError`, which is A4 on the real path and nothing more. How a real Codex app server routes approval requests among connected clients is UNKNOWN (read 1, finding 4, inferred); the amended A3 fails closed either way. Whether such requests are common enough to make the read UNKNOWN in ordinary use is also UNKNOWN until the live leg. |

Read 1's blocking findings and what changed:

| # | Finding | Change |
|---|---|---|
| 1 | The inventory loop never ended against a server minting a fresh cursor on every page, and had no overall deadline (the loop predates this repair; this repair made it reachable). | `codex_inventory` takes one overall deadline (60 s) and a page limit (50); exceeding either raises and reads UNKNOWN. Two tests. |
| 2 | The manual said the transport can send only three requests; it also sent `initialized` and an error reply to any server request, and the guard checked only method names and top-level keys (it sent a `thread/read` carrying a `result`). | `WsRpc.send` now admits only the exact request shape (integer id, that method's parameter names, `includeTurns` false) and the bare `initialized`; `WsRpc.route` never replies (amended A3, which also takes up finding 4). The manual sentence states exactly that. The reader's four bypasses are tests. |
| 3 | This record was stale: 35 for 26, the wrong test file named, an empty Result. | Corrected above; this section. |

Declared residue (read 1's non-blocking findings NOT fixed, 2026-11-16 12:02 ET; each is the reader's, with its ledger number):
- 5: a successful read prints the `scope` string only. It carries no `state` token and no sentence that an empty list is not absence; that sentence is in `PROME/tools/SESSION_PILOT.md` and in the Desk-spawn preflight, not in the output. A reader of the raw JSON must not take `"threads": []` as "no Codex desk is live".
- 6: a thread id repeated within or across pages is listed as given, not refused.
- 7: the binary-message and oversize cases pass even with the tool's own two checks removed (the library rejects first; the length check after it is unreachable).
- 8: a relative socket path prints UNKNOWN without the bridge's own reason text.
- 10: `read_only` is an instance-settable attribute; switching it off re-opens `doorbell`'s first read and a journal row, though the send rule still refuses delivery.
- 11: a library caller passing an unknown transport name gets the newline form; the CLI's choices prevent it there.
Read 2's three non-blocking findings, also NOT fixed (declared 2026-11-16 12:07 ET):
- R2-1: `--codex-transport jsonl` still answers a server-initiated request with a refusal, the reply the amended A3 forbids over the WebSocket transport. Do NOT point the jsonl form at a shared control socket; the installed Codex socket does not speak it anyway.
- R2-2: the deadlines hold under a flood of server notifications, but the notifications queue in memory until the deadline (about 60,000 in 2 seconds, run; hundreds of MB by 60 seconds, the reader's estimate). Needs a hostile or broken server.
- R2-3: two loose wordings in the manual sentence. "never turn content" is true of what is printed; the thread record the server returns can carry user text (a preview field) across the socket, and the seven-field projection drops it. And the page limit is 50 pages of up to 100 threads: a server paging in small pages reads UNKNOWN for a legitimate inventory (it fails closed).
- Noted by the reader, not a defect: the no-reply property is held by two layers (`route` raises; `send` would refuse the reply), and the tests cannot tell which one held.
Fixed although non-blocking: 9 (one token: the test file's own run instruction named the wider pattern that rewrites a tracked file) and 4 (taken up by the fix for 2).

## A9, the live leg: OBSERVED 2026-11-16 15:47 ET (recorded 2026-11-16 15:47 ET by PROME prome-6f)

A sourced receipt; no code, test or manual text changed. With Will's CATO session open on this desktop (a `codex --model gpt-6-astra --cd …/AGENTS/CATO` process and its app-server daemon, running about 2.4 hours), PROME ran `.venv/bin/python3 PROME/tools/session_bridge.py --codex-socket /home/willi/.codex/app-server-control/app-server-control.sock` once. Result: a `codex` object with endpoint `unix+ws://…/app-server-control.sock`, scope "loaded threads on this server only", observed_at 2026-11-16T20:47:22Z, and ONE thread: cwd `/home/willi/Research-workspace/AGENTS/CATO`, status idle, source vscode, canAcceptDirectInput true. The process scan in the same output showed three `codex` processes with that working directory.

What this establishes: against the installed Codex app server the handshake, `initialize`, `thread/loaded/list` and `thread/read` complete and a live Codex desk's thread is listed. What it does not: more than one loaded thread or a paged list on the real server; a server-initiated request arriving mid-read (the amended A3 path was not exercised, and how Codex routes approval requests is still UNKNOWN); a Codex desk started another way. CATO reported the same day, through Will, that its own live check had already found this session; PROME's run is independent of that report. A9 moves from PENDING to OBSERVED, once.

