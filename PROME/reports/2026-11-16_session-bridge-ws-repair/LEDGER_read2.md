# Independent read 2: the fix diff only (commit 39f306de67)

Reader: the same blind reviewer as read 1, 2026-11-16. Scope: only what 39f306de67 changed in `PROME/tools/session_bridge.py`, `PROME/tests/test_session_bridge_ws.py`, the changed SESSION_PILOT.md sentence and the amended acceptance conditions and Result section. Residue items 5, 6, 7, 8, 10 and 11 were not re-raised; none was made worse by the fix. Fixtures were under `mktemp -d` (/tmp/tmp.HPo7y6QRKI). No Codex process was started or contacted. The repository tree was clean before and after my runs (`git status --short` empty).

Totals: **0 BLOCKING, 3 NON-BLOCKING (⚠️).** Read 1's blocking findings 1, 2 and 3 are all **CLOSED**.

## Read 1's blocking findings

| # | Verdict | What I ran | Observed |
|---|---|---|---|
| 1 (endless fresh cursor; no overall deadline) | **CLOSED** | My original `endless_cursor` fixture; a new `slow_default` fixture (fresh cursor and one thread per page, each `thread/read` answered after 4 s, **default** budget, through `codex_observation`); `legit_large` (200 threads over 2 pages); `small_pages` (60 one-thread pages) | Endless cursor: UNKNOWN `BridgeError` after 0.02 s (it previously hung). Slow server: UNKNOWN `TimeoutError` at **60.0 s** wall time from start, matching the 60 s bound. 200 threads listed in 0.07 s. 60 one-thread pages: UNKNOWN (the 50-page limit fails closed; see ⚠️ 3). |
| 2 (manual's "only three requests"; guard admitted replies and crafted shapes) | **CLOSED** | My original `guard_bypass`, `server_request_at_init` and `crafted_ids` fixtures; read the new sentence against `WsRpc.send`/`WsRpc.route` | All four of my original bypass messages are now refused locally; the server received only `initialize` and `initialized`. A server request during `initialize`, and a forged request reusing our pending id with a `result`, both give UNKNOWN, and **no reply of any kind** is sent (the server's received list has no method-less message). The new sentence (three requests, bare `initialized`, never answers a server request, UNKNOWN) is true of the code. |
| 3 (stale acceptance record) | **CLOSED** | `grep -c "def test_"` on both test files; `git show 39f306de67 --stat`; the author's suite under both Pythons | 26 cases in `test_session_bridge.py`, which neither commit touches. A7 now says 26, and Required result names the new file. The Result section is written and keeps the four states apart. Its TESTED row is true: 42 run, OK under `.venv`; 42 run, 13 skipped, OK under system `python3`. |

## New findings on the fix

| # | Sev | Claim tested | Artifact | Command run | Observed | Proposed change |
|---|---|---|---|---|---|---|
| 1 | ⚠️ RUN | Amended A3's reason ("on a shared control socket a reply could settle another session's pending approval") is applied wherever the CLI reads a control socket | `codex_observation` with `transport="jsonl"` → `Rpc.route` (unchanged) | `ce.py jsonl`: a newline-JSON fixture sends `{"id":"srv","method":"approval"}` before the `thread/read` response | The jsonl transport still lists the thread, so the request was answered with the `-32601` refusal. `--codex-transport jsonl` is a CLI option, so the same reply that A3 now forbids can still go out over a shared socket through that option. This was true before the fix and the fix did not make it worse; the amended A3 is scoped "over this transport", so it is not a false claim. | Give the jsonl path in `codex_observation` the same no-reply rule, for example a read-only flag on `Rpc` that makes `route` raise. Otherwise add one line to the manual: "the jsonl form still refuses server requests by replying; do not point it at a shared control socket". |
| 2 | ⚠️ RUN + INFERRED | The 60 s bound also bounds memory | `Rpc.route` events deque (`self.events.append`), reached from `WsRpc.route` → `super().route` | `ce.py batchflood` (per-call `timeout=1`) and `batchflood_inv` (`codex_inventory(budget=2)`): the server floods 5,000-notification batches without stopping | **RUN:** the deadlines hold under a flood. The per-call timeout fired at 1.0 s and the inventory at 2.0 s, with no outrun. But 29,627 and 59,573 notifications were queued in `events`, which is never read on the inventory path. **INFERRED:** at the 60 s default that is roughly 1.8 million queued dicts, hundreds of MB, before UNKNOWN. | Cap `events` (a `deque(maxlen=…)`), or let `WsRpc` drop notifications during an inventory. Low priority: it needs a hostile or broken server. |
| 3 | ⚠️ RUN (wording) | The manual's "(identity fields, never turn content)" and "50 pages" | SESSION_PILOT.md changed sentence; `codex_inventory` | `small_pages` fixture; read the author's own fixture `thread()` | (a) `includeTurns: false` keeps turns out of the request, but the thread object the server returns may still carry user text: the author's own fixture includes a `preview` field. That text crosses the socket and is dropped only by the 7-field projection. "never turn content" is true of the output, not of what is read. (b) "50 pages" is a page count, not a thread count. A server that pages in small pages (60 pages of 1 thread here) gives UNKNOWN for a legitimate inventory. It fails closed, so this is not a false "complete". | Reword to "requests no turns; prints identity fields only". Optionally note that the page limit is 50 pages of up to 100 threads. |

## Can the new and rewritten tests fail? (mutations on a temp copy of the tool; the test file was run unchanged)

| Mutation | Result |
|---|---|
| M5: remove the page limit | FAILED (endless-cursor test) ✅ |
| M6: remove the overall deadline, per-call timeout back to 30 | FAILED (slow-server test) ✅ |
| M8: `WsRpc.route` silently drops a server request instead of raising | FAILED ×2 ✅ |
| M9: `includeTurns` unchecked · M10: id type unchecked · M11: parameter names unchecked · M12: `initialized` allowed with extra keys | each FAILED ×3 ✅ |
| M7: `WsRpc.route` falls through to `super().route` (replies again) | **suite OK.** Expected, not a defect: the reply is still refused by `WsRpc.send`, so no byte goes out and the read is UNKNOWN. The no-reply property has two independent layers and the tests cannot tell which one held. Noted only. |

The other caller, `PROME/tests/test_boot_hardening.py` (`codex_inventory(rpc)` with a `mock.Mock`), still passes: I ran `python -m unittest PROME.tests.test_boot_hardening` under `.venv`, OK, and the tree stayed clean. The newline transport still reads a newline server through the new `codex_inventory` signature (`ce.py jsonl`, RUN).

## Manual and Result bounds checked

- "10 seconds to connect": `open_timeout=10`. Read 1 RUN: a trickled handshake gave UNKNOWN at 10.0 s. True.
- "30 to initialize": `initialize` uses `Rpc.call`'s default 30 s. Read, not timed. True by reading.
- "60 seconds and 50 pages for the inventory": RUN, UNKNOWN at 60.0 s and at the 51st page. True. Not mentioned: `close_timeout=2` adds up to 2 s, and the CLI's separate `claude agents` subprocess has its own 15 s.
- "It never answers a request the server starts … the result is UNKNOWN": RUN. True for the WebSocket transport (see ⚠️ 1 for jsonl).
- Result row STILL UNRESOLVED (A9 PENDING; Codex's routing of approvals UNKNOWN): consistent with what I observed. The control-socket symlink target was missing when I `stat`ed it in read 1. I did not verify the author's own run against the real path.

## Run vs inferred

RUN: closure of 1, 2 and 3; ⚠️ 1; ⚠️ 2 (deadline behaviour and queued counts); ⚠️ 3 (small pages); every mutation; both suites; boot_hardening. INFERRED: ⚠️ 2's memory extrapolation to 60 s. Read only: the "30 to initialize" bound, and the `preview` field crossing the socket (read in the author's fixture, not observed from Codex).
