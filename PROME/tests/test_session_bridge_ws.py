"""WebSocket transport checks for the session bridge (DOCKET L907).

Local fixture servers and temporary state only; no Codex daemon is contacted or started.
Acceptance: PROME/tools/tests/ACCEPTANCE_session_bridge_codex_websocket_2026-11-16.md.
Run with the repository venv (the fixture server needs `websockets`):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python3 -m unittest discover -s PROME/tests -p 'test_session*.py'
"""
import importlib.util
import json
import logging
import os
from pathlib import Path
import socket
import sys
import tempfile
import threading
import unittest
from unittest import mock


SPEC = importlib.util.spec_from_file_location(
    "session_bridge", Path(__file__).resolve().parents[1] / "tools/session_bridge.py")
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)

try:
    from websockets.sync.server import unix_serve
    HAVE_WS = True
    logging.getLogger("websockets.server").setLevel(logging.CRITICAL)  # fixture noise only
except ImportError:  # the system Python; A6 below still runs
    HAVE_WS = False

FIELDS = ("id", "sessionId", "parentThreadId", "cwd", "source", "status", "canAcceptDirectInput")


def thread(tid, cwd="/repo/AGENTS/CATO"):
    return {"id": tid, "sessionId": tid, "parentThreadId": None, "cwd": cwd, "source": "vscode",
            "status": {"type": "idle"}, "canAcceptDirectInput": True, "preview": "not copied"}


class WsFixture:
    """An app-server double speaking WebSocket over a Unix socket.

    `overrides` maps a method to callable(ws, message) that replaces the default reply.
    Everything received is recorded in order.
    """

    PAGES = {None: (["t1", "t2"], "c1"), "c1": (["t3"], None)}

    def __init__(self, test, overrides=None):
        self.overrides = overrides or {}
        self.received = []
        self.directory = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.directory.name, "control.sock")
        self.server = unix_serve(self.handle, path=self.path)
        self.worker = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.worker.start()
        test.addCleanup(self.stop)

    def stop(self):
        self.server.shutdown()
        self.worker.join(timeout=5)
        self.directory.cleanup()

    def methods(self):
        return [m.get("method", "<reply>") for m in self.received]

    def handle(self, ws):
        try:
            for raw in ws:
                message = json.loads(raw)
                self.received.append(message)
                method = message.get("method")
                if method in self.overrides:
                    self.overrides[method](ws, message)
                elif method == "initialize":
                    ws.send(json.dumps({"id": message["id"], "result": {"userAgent": "fixture"}}))
                elif method == "thread/loaded/list":
                    data, cursor = self.PAGES[message["params"].get("cursor")]
                    ws.send(json.dumps({"id": message["id"], "result": {"data": data, "nextCursor": cursor}}))
                elif method == "thread/read":
                    tid = message["params"]["threadId"]
                    ws.send(json.dumps({"id": message["id"], "result": {"thread": thread(tid)}}))
                elif method is not None and "id" in message:
                    ws.send(json.dumps({"id": message["id"], "error": {"code": -32601, "message": "no"}}))
        except Exception:  # noqa: BLE001 - a test that breaks the connection on purpose
            pass


def reply(result):
    return lambda ws, message: ws.send(json.dumps({"id": message["id"], "result": result}))


@unittest.skipUnless(HAVE_WS, "fixture server needs websockets; run with the repository .venv")
class WebSocketInventoryTests(unittest.TestCase):
    def observe(self, overrides=None):
        fixture = WsFixture(self, overrides)
        return fixture, bridge.codex_observation(fixture.path)

    def assert_unknown(self, observed):
        self.assertEqual(observed.get("state"), "UNKNOWN", observed)
        self.assertNotIn("threads", observed)

    # A1
    def test_paged_inventory_lists_every_loaded_thread_with_identity_fields_only(self):
        fixture, observed = self.observe()
        self.assertEqual([t["id"] for t in observed["threads"]], ["t1", "t2", "t3"])
        for row in observed["threads"]:
            self.assertEqual(tuple(row), FIELDS)
        self.assertEqual(observed["endpoint"], "unix+ws://" + fixture.path)
        self.assertEqual(observed["scope"], "loaded threads on this server only")  # A8
        self.assertIn("observed_at", observed)
        self.assertEqual(fixture.methods(), ["initialize", "initialized", "thread/loaded/list",
                                             "thread/read", "thread/read", "thread/loaded/list", "thread/read"])
        for message in fixture.received:
            if message.get("method") == "thread/read":
                self.assertIs(message["params"]["includeTurns"], False)

    def test_empty_loaded_list_is_an_empty_list_not_an_absence_claim(self):
        _, observed = self.observe({"thread/loaded/list": reply({"data": [], "nextCursor": None})})
        self.assertEqual(observed["threads"], [])
        self.assertEqual(observed["scope"], "loaded threads on this server only")

    # A3
    def test_server_initiated_approval_is_refused_and_does_not_displace_the_response(self):
        def read_with_approval(ws, message):
            ws.send(json.dumps({"id": "srv-1", "method": "item/commandExecution/requestApproval", "params": {}}))
            ws.send(json.dumps({"method": "thread/status/changed", "params": {"threadId": "t9"}}))
            ws.send(json.dumps({"id": message["id"], "result": {"thread": thread(message["params"]["threadId"])}}))
        fixture, observed = self.observe({"thread/read": read_with_approval})
        self.assertEqual([t["id"] for t in observed["threads"]], ["t1", "t2", "t3"])
        replies = [m for m in fixture.received if "method" not in m]
        self.assertEqual(len(replies), 3)
        for message in replies:
            self.assertEqual(message["id"], "srv-1")
            self.assertIn("error", message)
            self.assertNotIn("result", message)

    # A2
    def test_only_read_methods_can_be_sent(self):
        fixture = WsFixture(self)
        rpc = bridge.WsRpc.unix(fixture.path)
        self.addCleanup(rpc.close)
        rpc.initialize()
        for method in ("thread/queue/add", "turn/steer", "turn/start", "turn/interrupt", "thread/start",
                       "thread/archive", "thread/resume", "Thread/Read", "thread/read "):
            with self.assertRaises(bridge.BridgeError):
                rpc.call(method, {"threadId": "t1"})
        with self.assertRaises(bridge.BridgeError):
            rpc.send({"method": "turn/interrupt"})
        with self.assertRaises(bridge.BridgeError):
            rpc.send({"id": "srv-1", "result": {"decision": "approved"}})
        with self.assertRaises(bridge.BridgeError):
            rpc.send({"id": "srv-1", "result": {"decision": "approved"}, "error": {"code": 1}})
        with self.assertRaises(bridge.BridgeError):
            rpc.send({})
        rpc.call("thread/loaded/list", {"cursor": None, "limit": 100})  # drains the connection in order
        self.assertEqual(fixture.methods(), ["initialize", "initialized", "thread/loaded/list"])

    def test_doorbell_refuses_before_reading_the_recipient_or_writing_the_journal(self):
        fixture = WsFixture(self)
        rpc = bridge.WsRpc.unix(fixture.path)
        self.addCleanup(rpc.close)
        rpc.initialize()
        state = tempfile.TemporaryDirectory()
        self.addCleanup(state.cleanup)
        artifact = Path(state.name) / "packet.md"
        artifact.write_text("packet")
        journal = bridge.Journal(Path(state.name) / "journal.sqlite")
        for mode, extra in (("queue", {}), ("steer", {"expected_turn_id": "turn-1"})):
            envelope = dict(message_id="m-" + mode, task_id="task", sender="PROME", thread_id="t1",
                            cwd="/repo/AGENTS/CATO", artifact=str(artifact), mode=mode, **extra)
            with self.assertRaises(bridge.BridgeError):
                bridge.doorbell(rpc, journal, envelope)
        rpc.call("thread/loaded/list", {"cursor": None, "limit": 100})
        self.assertEqual(fixture.methods(), ["initialize", "initialized", "thread/loaded/list"])
        with journal.connect() as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM messages").fetchone()[0], 0)

    # A5
    def test_failures_read_unknown_never_a_partial_list(self):
        def close(ws, message):
            ws.close()
        cases = {
            "binary message": {"thread/loaded/list": lambda ws, m: ws.send(b"\x00\x01")},
            "malformed JSON": {"thread/loaded/list": lambda ws, m: ws.send("{nope")},
            "non-object": {"thread/loaded/list": lambda ws, m: ws.send("[1, 2]")},
            "oversized": {"thread/read": lambda ws, m: ws.send("x" * (bridge.MAX_FRAME + 10))},
            "disconnect after list": {"thread/loaded/list": close},
            "disconnect after second read": {"thread/read": lambda ws, m: close(ws, m) if m["params"]["threadId"] == "t2"
                                             else ws.send(json.dumps({"id": m["id"], "result": {"thread": thread("t1")}}))},
            "disconnect at initialize": {"initialize": close},
            "identity mismatch": {"thread/read": reply({"thread": thread("someone-else")})},
            "thread missing": {"thread/read": reply({})},
            "thread not an object": {"thread/read": reply({"thread": "t1"})},
            "malformed list": {"thread/loaded/list": reply({"data": [1], "nextCursor": None})},
            "list not an object": {"thread/loaded/list": reply(["t1"])},
            "repeated cursor": {"thread/loaded/list": reply({"data": ["t1"], "nextCursor": "c1"})},
            "server error": {"thread/loaded/list": lambda ws, m: ws.send(
                json.dumps({"id": m["id"], "error": {"code": -32600, "message": "experimental"}}))},
        }
        for name, overrides in cases.items():
            with self.subTest(name):
                _, observed = self.observe(overrides)
                self.assert_unknown(observed)

    def test_response_deadline_is_a_timeout_not_a_result(self):
        fixture = WsFixture(self, {"thread/read": lambda ws, m: None})
        rpc = bridge.WsRpc.unix(fixture.path)
        self.addCleanup(rpc.close)
        rpc.initialize()
        with self.assertRaises(TimeoutError):
            rpc.call("thread/read", {"threadId": "t1", "includeTurns": False}, timeout=0.3)

    def test_newline_json_peer_fails_the_handshake_to_unknown(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = os.path.join(directory.name, "plain.sock")
        listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        listener.bind(path)
        listener.listen(1)
        self.addCleanup(listener.close)

        def serve():
            try:
                peer, _ = listener.accept()
                peer.recv(65536)
                peer.sendall(b'{"id":1,"result":{}}\n')
                peer.close()
            except OSError:
                pass
        threading.Thread(target=serve, daemon=True).start()
        self.assert_unknown(bridge.codex_observation(path))

    # A7 beside A1: the caller chooses the transport; neither is guessed
    def test_newline_transport_against_a_websocket_server_is_unknown(self):
        fixture = WsFixture(self)
        self.assert_unknown(bridge.codex_observation(fixture.path, "jsonl"))
        self.assertEqual(fixture.received, [])

    def test_newline_transport_still_reads_a_newline_server(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = os.path.join(directory.name, "plain.sock")
        listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        listener.bind(path)
        listener.listen(1)
        self.addCleanup(listener.close)

        def serve():
            try:
                peer, _ = listener.accept()
                stream = peer.makefile("rwb")
                for line in stream:
                    message = json.loads(line)
                    if "id" not in message:
                        continue
                    result = {"initialize": {}, "thread/loaded/list": {"data": ["t1"], "nextCursor": None},
                              "thread/read": {"thread": thread("t1")}}[message["method"]]
                    stream.write(json.dumps({"id": message["id"], "result": result}).encode() + b"\n")
                    stream.flush()
            except (OSError, ValueError):
                pass
        threading.Thread(target=serve, daemon=True).start()
        observed = bridge.codex_observation(path, "jsonl")
        self.assertEqual([t["id"] for t in observed["threads"]], ["t1"])
        self.assertEqual(observed["endpoint"], "unix://" + path)


class NoDaemonAndNoPackageTests(unittest.TestCase):
    """These need no fixture server and run under any Python."""

    # A4
    def test_absent_endpoints_are_unknown_and_nothing_is_started(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        missing = os.path.join(directory.name, "missing.sock")
        dangling = os.path.join(directory.name, "dangling.sock")
        os.symlink(os.path.join(directory.name, "gone"), dangling)
        dead = os.path.join(directory.name, "dead.sock")
        listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        listener.bind(dead)
        listener.close()  # the file stays, nothing listens
        with mock.patch.object(bridge.subprocess, "Popen") as popen, \
                mock.patch.object(bridge.subprocess, "run") as run:
            for path in (missing, dangling, dead, "relative.sock"):
                for transport in ("websocket", "jsonl"):
                    with self.subTest(path=os.path.basename(path), transport=transport):
                        observed = bridge.codex_observation(path, transport)
                        self.assertEqual(observed.get("state"), "UNKNOWN", observed)
                        self.assertNotIn("threads", observed)
            popen.assert_not_called()
            run.assert_not_called()

    # A6
    def test_missing_websocket_package_is_unknown_and_names_the_remedy(self):
        with mock.patch.dict(sys.modules, {"websockets.sync.client": None}):
            observed = bridge.codex_observation("/nonexistent/control.sock")
        self.assertEqual(observed["state"], "UNKNOWN")
        self.assertEqual(observed["error"], "BridgeUnavailable")
        self.assertIn(".venv", observed["reason"])
        self.assertNotIn("threads", observed)

    def test_reason_is_printed_only_for_the_bridges_own_unavailable_message(self):
        class Refusing:
            @classmethod
            def unix(cls, path):
                raise bridge.BridgeError('{"message": "server-supplied text"}')
        with mock.patch.object(bridge, "WsRpc", Refusing):
            observed = bridge.codex_observation("/nonexistent/control.sock")
        self.assertEqual(observed, {"state": "UNKNOWN", "error": "BridgeError"})


if __name__ == "__main__":
    unittest.main()
