#!/usr/bin/env python3
"""Opt-in local session pilot. No launch authority or fleet-wide enforcement.

Metadata-only inventory; explicit local RPC; durable no-auto-retry doorbells;
cooperative capacity reservations. CLI inventory never starts a Codex daemon.

The Codex app-server control socket speaks WebSocket over a Unix socket; WsRpc
reads it, read-only, and needs the repository .venv (websockets). Rpc.unix keeps
the newline-JSON form. Loaded threads on one server are never an absent-desk verdict.
"""
from __future__ import annotations

import argparse
from collections import deque
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import selectors
import socket
import sqlite3
import subprocess
import time
import uuid
from datetime import datetime, timezone


def now():
    return datetime.now(timezone.utc).isoformat()


class BridgeError(RuntimeError):
    pass


class BridgeUnavailable(BridgeError):
    """A local prerequisite is missing; the message is ours and safe to print."""


MAX_FRAME = 4_000_000
# The only traffic the WebSocket transport may originate (DOCKET L907: read-only).
READ_ONLY_METHODS = frozenset({"initialize", "thread/loaded/list", "thread/read"})
READ_ONLY_NOTIFICATIONS = frozenset({"initialized"})


class Rpc:
    """One connection, one caller. Never answers an approval affirmatively."""

    def __init__(self, reader, writer, endpoint, process=None):
        self.reader, self.writer, self.endpoint = reader, writer, endpoint
        self.process = process
        self.selector = selectors.DefaultSelector()
        self.selector.register(reader, selectors.EVENT_READ)
        self.buffer = b""
        self.events = deque()
        self.responses = {}
        self.serial = 0

    @classmethod
    def unix(cls, path):
        path = Path(path)
        if not path.is_absolute():
            raise BridgeError("An explicit absolute local socket path is required")
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.settimeout(10)
        try:
            sock.connect(str(path))
        except BaseException:
            sock.close()
            raise
        return cls(sock, sock, "unix://" + str(path))

    @classmethod
    def stdio(cls, command, cwd, stderr):
        proc = subprocess.Popen(command, cwd=cwd, stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, stderr=stderr, bufsize=0)
        return cls(proc.stdout, proc.stdin, "owned-stdio", proc)

    def send(self, value):
        raw = (json.dumps(value, separators=(",", ":")) + "\n").encode()
        if isinstance(self.writer, socket.socket):
            self.writer.sendall(raw)
        else:
            view = memoryview(raw)
            while view:
                n = os.write(self.writer.fileno(), view)
                view = view[n:]

    def receive(self, timeout=30):
        end = time.monotonic() + timeout
        while b"\n" not in self.buffer:
            if len(self.buffer) > MAX_FRAME:
                raise BridgeError("Oversized RPC frame")
            left = end - time.monotonic()
            if left <= 0 or not self.selector.select(left):
                raise TimeoutError("RPC response deadline; sent request outcome UNKNOWN")
            chunk = os.read(self.reader.fileno(), 65536)
            if not chunk:
                raise BridgeError("RPC disconnected; sent request outcome UNKNOWN")
            self.buffer += chunk
        line, self.buffer = self.buffer.split(b"\n", 1)
        try:
            value = json.loads(line)
        except (ValueError, UnicodeDecodeError) as exc:
            raise BridgeError("Malformed RPC frame") from exc
        if not isinstance(value, dict):
            raise BridgeError("RPC frame is not an object")
        return value

    def route(self, value):
        if "method" in value and "id" in value:
            # Includes approvals, credentials and interactive input requests.
            self.send({"id": value["id"], "error": {
                "code": -32601, "message": "PROME pilot cannot authorize or answer this request"}})
            self.events.append({"method": "pilot/requestRejected",
                                "params": {"method": value["method"]}})
        elif "id" in value:
            self.responses[value["id"]] = value
        else:
            self.events.append(value)

    def call(self, method, params=None, timeout=30):
        self.serial += 1
        request_id = self.serial
        self.send({"id": request_id, "method": method, "params": params or {}})
        end = time.monotonic() + timeout
        while request_id not in self.responses:
            self.route(self.receive(max(0, end - time.monotonic())))
        value = self.responses.pop(request_id)
        if "error" in value:
            raise BridgeError(json.dumps(value["error"]))
        if "result" not in value:
            raise BridgeError("RPC response lacks result/error")
        return value["result"]

    def initialize(self):
        result = self.call("initialize", {
            "clientInfo": {"name": "prome_session_pilot", "version": "0.1"},
            "capabilities": {"experimentalApi": True}})
        self.send({"method": "initialized"})
        return result

    def wait_event(self, method, predicate=lambda p: True, timeout=30):
        end = time.monotonic() + timeout
        while True:
            for event in tuple(self.events):
                if event.get("method") == method and predicate(event.get("params", {})):
                    self.events.remove(event)
                    return event["params"]
            self.route(self.receive(max(0, end - time.monotonic())))

    def close(self):
        self.selector.close()
        if isinstance(self.reader, socket.socket):
            self.reader.close()
        else:
            self.writer.close()
            self.reader.close()
        if self.process:
            # Only the exact child created by this object, never an existing daemon.
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()


class WsRpc(Rpc):
    """WebSocket over a Unix socket (the Codex control socket). Read-only by construction.

    Sends only READ_ONLY_METHODS, the `initialized` notification and error replies to
    requests the server initiates. Never starts a daemon; never delivers input.
    """

    read_only = True

    def __init__(self, connection, endpoint):
        self.connection, self.endpoint = connection, endpoint
        self.process = None
        self.events = deque()
        self.responses = {}
        self.serial = 0

    @classmethod
    def unix(cls, path):
        path = Path(path)
        if not path.is_absolute():
            raise BridgeError("An explicit absolute local socket path is required")
        try:
            from websockets.sync.client import unix_connect
        except ImportError as exc:
            raise BridgeUnavailable(
                "WebSocket client unavailable in this Python; run with the repository "
                ".venv/bin/python3 (websockets). Codex coverage UNKNOWN") from exc
        connection = unix_connect(path=str(path), open_timeout=10, max_size=MAX_FRAME,
                                  ping_interval=None, close_timeout=2)
        return cls(connection, "unix+ws://" + str(path))

    def send(self, value):
        if "method" in value and "id" in value:
            allowed = value["method"] in READ_ONLY_METHODS
        elif "method" in value:
            allowed = value["method"] in READ_ONLY_NOTIFICATIONS
        else:  # a reply to a server-initiated request: a refusal only, never a result
            allowed = "id" in value and "error" in value and "result" not in value
        if not allowed:
            raise BridgeError("Read-only transport refuses to send this message")
        self.connection.send(json.dumps(value, separators=(",", ":")))

    def receive(self, timeout=30):
        from websockets.exceptions import ConnectionClosed
        try:
            message = self.connection.recv(timeout=max(0, timeout))
        except TimeoutError:
            raise TimeoutError("RPC response deadline; sent request outcome UNKNOWN") from None
        except ConnectionClosed as exc:
            raise BridgeError("RPC disconnected; sent request outcome UNKNOWN") from exc
        if not isinstance(message, str):
            raise BridgeError("Binary RPC frame")
        if len(message) > MAX_FRAME:
            raise BridgeError("Oversized RPC frame")
        try:
            value = json.loads(message)
        except ValueError as exc:
            raise BridgeError("Malformed RPC frame") from exc
        if not isinstance(value, dict):
            raise BridgeError("RPC frame is not an object")
        return value

    def close(self):
        try:
            self.connection.close()
        except Exception:  # noqa: BLE001 - closing an already-broken connection changes nothing
            pass


def local_context(proc_root=Path("/proc")):
    try:
        return {"boot_id": (proc_root / "sys/kernel/random/boot_id").read_text().strip(),
                "pid_namespace": os.readlink(proc_root / "self/ns/pid")}
    except OSError as exc:
        raise BridgeError("Observer context UNKNOWN") from exc


def process_identity(pid, proc_root=Path("/proc")):
    """Missing process is DEAD; inability to inspect it is UNKNOWN."""
    try:
        stat = (proc_root / str(pid) / "stat").read_text()
    except FileNotFoundError:
        return None
    except OSError as exc:
        raise BridgeError("Process identity UNKNOWN") from exc
    try:
        tail = stat[stat.rfind(")") + 2:].split()
        return {"pid": int(pid), "start_ticks": tail[19], "state": tail[0],
                **local_context(proc_root)}
    except (OSError, ValueError, IndexError) as exc:
        raise BridgeError("Process identity UNKNOWN") from exc


def liveness(identity):
    try:
        context = local_context()
        if any(context[k] != identity[k] for k in context):
            return "UNKNOWN"
        current = process_identity(identity["pid"])
    except BridgeError:
        return "UNKNOWN"
    if current is None:
        return "DEAD"
    if current["boot_id"] != identity["boot_id"] or current["pid_namespace"] != identity["pid_namespace"]:
        return "UNKNOWN"  # Wrong host/namespace can never prove this holder died.
    if current["start_ticks"] != identity["start_ticks"] or current["state"] == "Z":
        return "DEAD"
    return "LIVE"


class Journal:
    """Local operational state only. Survives client restart; never auto-retries."""

    def __init__(self, path):
        self.path = str(path)
        with self.connect() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS messages (
                  id TEXT PRIMARY KEY, digest TEXT NOT NULL, status TEXT NOT NULL,
                  result TEXT, updated TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS reservations (
                  id TEXT PRIMARY KEY, owner TEXT, parent TEXT, identity TEXT NOT NULL,
                  active INTEGER NOT NULL, created TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS policy (
                  name TEXT PRIMARY KEY, value INTEGER NOT NULL);
            """)

    def connect(self):
        return sqlite3.connect(self.path, timeout=10, isolation_level=None)

    @contextmanager
    def transaction(self):
        db = self.connect()
        try:
            db.execute("BEGIN IMMEDIATE")
            yield db
            db.commit()
        except BaseException:
            db.rollback()
            raise
        finally:
            db.close()

    def begin_message(self, envelope):
        digest = hashlib.sha256(json.dumps(envelope, sort_keys=True).encode()).hexdigest()
        with self.transaction() as db:
            prior = db.execute("SELECT digest,status,result FROM messages WHERE id=?",
                               (envelope["message_id"],)).fetchone()
            if prior:
                if prior[0] != digest:
                    raise BridgeError("Message ID reused with different payload")
                return {"status": prior[1], "result": prior[2], "duplicate": True}
            db.execute("INSERT INTO messages VALUES (?,?,?,NULL,?)",
                       (envelope["message_id"], digest, "ATTEMPTED", now()))
        return None

    def finish_message(self, message_id, status, result):
        with self.transaction() as db:
            db.execute("UPDATE messages SET status=?,result=?,updated=? WHERE id=?",
                       (status, json.dumps(result), now(), message_id))

    def reserve(self, limit, identity, owner=None, parent=None, check=liveness):
        if limit < 1 or check(identity) != "LIVE":
            raise BridgeError("Reservation requires positive limit and verified live holder")
        with self.transaction() as db:
            policy = db.execute("SELECT value FROM policy WHERE name='capacity'").fetchone()
            if policy and policy[0] != limit:
                raise BridgeError("Pilot capacity limit disagrees with shared policy")
            if not policy:
                db.execute("INSERT INTO policy VALUES ('capacity',?)", (limit,))
            rows = db.execute("SELECT id,owner,identity FROM reservations WHERE active=1").fetchall()
            survivors = []
            for rid, row_owner, raw in rows:
                if check(json.loads(raw)) == "DEAD":
                    db.execute("UPDATE reservations SET active=0 WHERE id=?", (rid,))
                else:
                    survivors.append((rid, row_owner))
            if parent and parent not in {r[0] for r in survivors}:
                raise BridgeError("Parent reservation is not active")
            if owner and any(row_owner == owner for _, row_owner in survivors):
                raise BridgeError("Owner writer already reserved")
            if len(survivors) >= limit:
                raise BridgeError("Pilot capacity exhausted (UNKNOWN holders count)")
            rid = str(uuid.uuid4())
            db.execute("INSERT INTO reservations VALUES (?,?,?,?,1,?)",
                       (rid, owner, parent, json.dumps(identity), now()))
            return rid

    def release(self, rid, identity):
        with self.transaction() as db:
            row = db.execute("SELECT identity FROM reservations WHERE id=? AND active=1", (rid,)).fetchone()
            if not row:
                return False
            if json.loads(row[0]) != identity:
                raise BridgeError("Holder generation mismatch")
            db.execute("UPDATE reservations SET active=0 WHERE id=?", (rid,))
            return True


def doorbell(rpc, journal, envelope):
    if getattr(rpc, "read_only", False):
        raise BridgeError("Read-only transport cannot deliver a doorbell")
    required = ("message_id", "task_id", "sender", "thread_id", "cwd", "artifact", "mode")
    if any(not envelope.get(k) for k in required) or envelope["sender"] != "PROME":
        raise BridgeError("Explicit PROME peer envelope required")
    if envelope["mode"] not in ("queue", "steer"):
        raise BridgeError("Unsupported delivery mode")
    if envelope["mode"] == "steer" and not envelope.get("expected_turn_id"):
        raise BridgeError("Active steering requires expected turn ID")
    artifact = Path(envelope["artifact"])
    if not artifact.is_absolute() or not artifact.is_file():
        raise BridgeError("Existing absolute artifact path required")
    # Hash is part of the durable message identity, including across restarts.
    envelope = dict(envelope, artifact_sha256=hashlib.sha256(artifact.read_bytes()).hexdigest(),
                    endpoint=rpc.endpoint)
    read = rpc.call("thread/read", {"threadId": envelope["thread_id"], "includeTurns": False})
    target = read.get("thread") if isinstance(read, dict) else None
    if not isinstance(target, dict) or target.get("id") != envelope["thread_id"]:
        raise BridgeError("Recipient session identity mismatch or UNKNOWN")
    if Path(target["cwd"]).resolve() != Path(envelope["cwd"]).resolve():
        raise BridgeError("Recipient cwd mismatch")
    if target.get("canAcceptDirectInput") is not True or target.get("status", {}).get("type") not in ("idle", "active"):
        raise BridgeError("Recipient direct-input/liveness capability UNKNOWN or unavailable")
    if envelope["mode"] == "queue" and target.get("ephemeral") is True:
        raise BridgeError("Ephemeral threads do not support queued submissions")
    prior = journal.begin_message(envelope)
    if prior:
        return prior
    text = (f"Peer coordination from PROME, not an operator approval. "
            f"Task {envelope['task_id']}; message {envelope['message_id']}. "
            f"Read {artifact}. SHA256 {envelope['artifact_sha256']}. "
            "Verify the artifact and your task scope before acting; preserve permission checks. "
            "Deduplicate this message/task against prior work. Report any priority conflict.")
    params = {"threadId": envelope["thread_id"], "input": [{"type": "text", "text": text}]}
    if envelope["mode"] == "steer":
        method = "turn/steer"
        params["expectedTurnId"] = envelope["expected_turn_id"]
    else:
        method = "thread/queue/add"
        params["clientUserMessageId"] = envelope["message_id"]
    try:
        result = rpc.call(method, params)
        if envelope["mode"] == "queue":
            queued = result.get("queuedSubmission") if isinstance(result, dict) else None
            if (not isinstance(queued, dict) or not isinstance(queued.get("id"), str)
                    or not queued["id"] or queued.get("clientUserMessageId") != envelope["message_id"]):
                raise BridgeError("Malformed queue acknowledgement; outcome UNKNOWN")
        elif not isinstance(result, dict) or result.get("turnId") != envelope["expected_turn_id"]:
            raise BridgeError("Steer acknowledgement identity mismatch; outcome UNKNOWN")
    except Exception as exc:
        journal.finish_message(envelope["message_id"], "UNKNOWN", {"error": type(exc).__name__})
        raise
    journal.finish_message(envelope["message_id"], "ACCEPTED", result)
    return {"status": "ACCEPTED", "result": result, "duplicate": False}


def codex_inventory(rpc):
    threads, cursor, seen = [], None, set()
    while True:
        result = rpc.call("thread/loaded/list", {"cursor": cursor, "limit": 100})
        if (not isinstance(result, dict) or not isinstance(result.get("data"), list)
                or any(not isinstance(tid, str) or not tid for tid in result["data"])):
            raise BridgeError("Malformed loaded-thread inventory; coverage UNKNOWN")
        for tid in result["data"]:
            thread = rpc.call("thread/read", {"threadId": tid, "includeTurns": False})["thread"]
            if not isinstance(thread, dict) or thread.get("id") != tid:
                raise BridgeError("Inventory thread identity mismatch; coverage UNKNOWN")
            threads.append({k: thread.get(k) for k in (
                "id", "sessionId", "parentThreadId", "cwd", "source", "status", "canAcceptDirectInput")})
        cursor = result.get("nextCursor")
        if not cursor:
            break
        if cursor in seen:
            raise BridgeError("Repeated inventory cursor; coverage incomplete")
        seen.add(cursor)
    return {"endpoint": rpc.endpoint, "scope": "loaded threads on this server only",
            "observed_at": now(), "threads": threads}


def inventory():
    result = {"observed_at": now(), "host": socket.gethostname(), "processes": [],
              "coverage": "Visible PID namespace only; turn activity and native helpers UNKNOWN",
              "codex": {"state": "UNKNOWN", "reason": "No explicit app-server endpoint supplied"}}
    try:
        result["pid1"] = Path("/proc/1/comm").read_text().strip()
        for p in Path("/proc").iterdir():
            if not p.name.isdigit():
                continue
            try:
                comm = (p / "comm").read_text().strip()
                if comm not in ("codex", "claude", "claude-code"):
                    continue
                result["processes"].append({"runtime": comm, "identity": process_identity(int(p.name)),
                    "cwd": os.readlink(p / "cwd"), "turn_status": "UNKNOWN"})
            except (OSError, BridgeError):
                result.setdefault("gaps", []).append({"pid": p.name, "state": "UNKNOWN"})
        mem = {}
        for line in Path("/proc/meminfo").read_text().splitlines():
            key, _, value = line.partition(":")
            if key in ("MemTotal", "MemAvailable", "SwapTotal", "SwapFree"):
                mem[key] = value.strip()
        result["visible_memory"] = mem
        run = subprocess.run(["claude", "agents", "--json"], capture_output=True, text=True, timeout=15)
        if run.returncode:
            raise BridgeError("Claude inventory failed")
        rows = json.loads(run.stdout)
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            raise BridgeError("Claude inventory is not an array of objects")
        result["claude"] = [{k: row.get(k) for k in (
            "id", "sessionId", "parentThreadId", "cwd", "kind", "pid", "state", "status", "waitingFor")} for row in rows]
    except (OSError, ValueError, BridgeError, subprocess.TimeoutExpired) as exc:
        result["error"] = type(exc).__name__
    return result


def codex_observation(socket_path, transport="websocket"):
    """Read-only loaded-thread inventory of one existing app server, or UNKNOWN. Never raises."""
    rpc = None
    try:
        rpc = (WsRpc if transport == "websocket" else Rpc).unix(socket_path)
        rpc.initialize()
        return codex_inventory(rpc)
    except BridgeUnavailable as exc:
        return {"state": "UNKNOWN", "error": type(exc).__name__, "reason": str(exc)}
    except Exception as exc:  # noqa: BLE001 - every failure is UNKNOWN, never a partial list
        return {"state": "UNKNOWN", "error": type(exc).__name__}
    finally:
        if rpc:
            rpc.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-socket", help="Optional explicit existing local socket; never starts a daemon")
    parser.add_argument("--codex-transport", choices=("websocket", "jsonl"), default="websocket",
                        help="websocket: the Codex control socket (read-only; needs the repository .venv). "
                             "jsonl: the earlier newline-JSON form")
    args = parser.parse_args()
    result = inventory()
    if args.codex_socket:
        result["codex"] = codex_observation(args.codex_socket, args.codex_transport)
    else:
        result["codex"] = {"state": "UNKNOWN", "reason": "No explicit app-server endpoint supplied"}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
