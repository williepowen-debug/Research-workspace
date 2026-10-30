#!/usr/bin/env python3
"""Durable synthetic response rehearsal. No live intake, sync or owner writes."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sqlite3
import uuid

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("comparison", HERE.parent / "comparison/render.py")
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)
DEMO_PATH = "AGENTS/CATO/prototypes/decisions/record-draft/example.json"


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(encoded(value).encode("utf-8")).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def identifier(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{32}", value):
        raise ValueError("Expected a generated event ID")
    return value


def demo_record():
    record = json.loads(reader.source_text(reader.SCHEMA_REV, DEMO_PATH))
    # Resolve fictional working-copy source only in this rehearsal's in-memory copy.
    for source in record["sources"]:
        source["commit"] = reader.SCHEMA_REV
    return record


class Store:
    event_kind = "synthetic-response/1"
    synthetic = True
    identity = "local rehearsal session; not authenticated Will authority"

    def __init__(self, path, loader=demo_record):
        self.path = Path(path)
        self.loader = loader
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connection() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS snapshots (hash TEXT PRIMARY KEY, body TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS responses (
                    id TEXT PRIMARY KEY, unit TEXT NOT NULL, request TEXT NOT NULL,
                    body TEXT NOT NULL, previous TEXT UNIQUE);
                CREATE TABLE IF NOT EXISTS heads (unit TEXT PRIMARY KEY, id TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS receipts (
                    sequence INTEGER PRIMARY KEY, response TEXT NOT NULL, body TEXT NOT NULL);
            """)
            for row in db.execute("SELECT body FROM responses"):
                if json.loads(row[0]).get("kind") != self.event_kind:
                    raise ValueError("This database belongs to another response mode")

    @contextmanager
    def connection(self):
        db = sqlite3.connect(self.path, timeout=10, isolation_level=None)
        db.execute("PRAGMA synchronous=FULL")
        try:
            yield db
        finally:
            if db.in_transaction:
                db.rollback()
            db.close()

    def current(self):
        record = self.loader()
        if record["wq_id"] != "DEMO-900":
            raise ValueError("Rehearsal accepts only the fictional DEMO-900 source")
        schema = json.loads(reader.source_text(reader.SCHEMA_REV, reader.SCHEMA_PATH))
        reader.validate_record(record, schema)
        return record

    def make_snapshot(self, record):
        return {"kind": "synthetic-display/1", "record": record,
                "presentation_sha256": hashlib.sha256((HERE / "index.html").read_bytes()).hexdigest()}

    def validate_display(self, snapshot, current):
        template = hashlib.sha256((HERE / "index.html").read_bytes()).hexdigest()
        if snapshot["record"] != current or snapshot["presentation_sha256"] != template:
            raise ValueError("Displayed terms changed; keep your note, reload and review")

    def display(self):
        record = self.current()
        snapshot = self.make_snapshot(record)
        key = digest(snapshot)
        with self.connection() as db:
            db.execute("INSERT OR IGNORE INTO snapshots VALUES (?, ?)", (key, encoded(snapshot)))
        return {"hash": key, "snapshot": snapshot, "responses": self.responses(),
                "groups": reader.project([record])["groups"]}

    def responses(self):
        with self.connection() as db:
            events = [json.loads(r[0]) for r in db.execute("SELECT body FROM responses ORDER BY rowid")]
            history = [json.loads(r[0]) for r in db.execute("SELECT body FROM receipts ORDER BY sequence")]
            receipts = {r["response_id"]: r for r in history}
            heads = dict(db.execute("SELECT unit, id FROM heads"))
        return {"events": events, "receipts": receipts, "receipt_history": history, "heads": heads}

    def save(self, request):
        fields = {"id", "display_hash", "unit_id", "action", "choice_id", "note", "revisit", "supersedes"}
        if not isinstance(request, dict) or set(request) != fields:
            raise ValueError("Response fields do not match the event contract")
        event_id = identifier(request["id"])
        for field in ("display_hash", "unit_id", "action", "note", "revisit"):
            if not isinstance(request[field], str):
                raise ValueError(f"{field} must be text")
        if len(request["note"]) > 100000 or len(request["revisit"]) > 10000:
            raise ValueError("Response exceeds the local size limit; nothing was saved")
        if request["supersedes"] is not None:
            identifier(request["supersedes"])
        if request["choice_id"] is not None and not isinstance(request["choice_id"], str):
            raise ValueError("Choice must be an option ID or null")
        request_body = encoded(request)
        with self.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            existing = db.execute("SELECT request, body FROM responses WHERE id=?", (event_id,)).fetchone()
            if existing:
                if existing[0] != request_body:
                    raise ValueError("This response ID already belongs to different content")
                db.commit()
                return json.loads(existing[1])
            row = db.execute("SELECT body FROM snapshots WHERE hash=?", (request["display_hash"],)).fetchone()
            if not row:
                raise ValueError("Display snapshot is missing; reload and review")
            snapshot = json.loads(row[0])
            current = self.current()
            self.validate_display(snapshot, current)
            unit = next((u for u in current["units"] if u["id"] == request["unit_id"]), None)
            if unit is None or unit["disposition"]["state"] not in {"awaiting_answer", "outstanding"}:
                raise ValueError("This unit is unavailable for a rehearsal response")
            action = request["action"]
            allowed = {"choose", "defer", "request_changes"} if unit["kind"] == "decision" else {"report_done", "defer", "request_changes"}
            if action not in allowed:
                raise ValueError("Action does not belong to this unit")
            choices = {c["id"]: c for c in unit["proposal"]["choices"]}
            choice = choices.get(request["choice_id"])
            if (action == "choose" and choice is None) or (action != "choose" and request["choice_id"] is not None):
                raise ValueError("Selected choice and response action disagree")
            if action == "request_changes" and not request["note"].strip():
                raise ValueError("A question or change request needs your words")
            if action != "defer" and request["revisit"]:
                raise ValueError("Return condition belongs to a deferral")
            head = db.execute("SELECT id FROM heads WHERE unit=?", (unit["id"],)).fetchone()
            if request["supersedes"] != (head[0] if head else None):
                raise ValueError("Another response exists; review it before replacing it")
            event = {"kind": self.event_kind, "synthetic": self.synthetic, "id": event_id,
                     "saved_at": now(), "request": request, "display": snapshot,
                     "selected_choice": choice,
                     "identity": self.identity}
            event["sha256"] = digest(event)
            db.execute("INSERT INTO responses VALUES (?, ?, ?, ?, ?)",
                       (event_id, unit["id"], request_body, encoded(event), request["supersedes"]))
            db.execute("INSERT OR REPLACE INTO heads VALUES (?, ?)", (unit["id"], event_id))
            db.commit()
            return event

    def acknowledge(self, event_id, event_hash, state, reference):
        """CLI-only synthetic receiver; never represents an actual PROME receipt."""
        identifier(event_id)
        if state not in {"received", "needs_clarification", "rejected", "integrated"}:
            raise ValueError("Unsupported receipt state")
        if not isinstance(reference, str) or not reference.strip():
            raise ValueError("Receipt requires a synthetic evidence reference")
        with self.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT body FROM responses WHERE id=?", (event_id,)).fetchone()
            if not row or json.loads(row[0])["sha256"] != event_hash:
                raise ValueError("Receipt does not match an existing response and hash")
            old = [json.loads(r[0]) for r in db.execute(
                "SELECT body FROM receipts WHERE response=? ORDER BY sequence", (event_id,))]
            for receipt in old:
                if (receipt["state"], receipt["reference"]) == (state, reference):
                    db.commit()
                    return receipt
            if old and (old[-1]["state"] != "received" or state == "received"):
                raise ValueError("Conflicting receiver result; preserve the earlier receipt")
            receipt = {"kind": "synthetic-receipt/1", "synthetic": True, "response_id": event_id,
                       "response_sha256": event_hash, "state": state, "reference": reference, "at": now()}
            db.execute("INSERT INTO receipts (response, body) VALUES (?, ?)", (event_id, encoded(receipt)))
            db.commit()
            return receipt

    def export(self, event_id):
        identifier(event_id)
        state = self.responses()
        event = next((e for e in state["events"] if e["id"] == event_id), None)
        if event is None:
            raise ValueError("Unknown response")
        return {"kind": "synthetic-transfer/1", "event": event,
                "receipt_history": [r for r in state["receipt_history"] if r["response_id"] == event_id],
                "delivery": "Export only; no Git delivery, recipient read or completion established"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--store", type=Path, required=True)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    export = sub.add_parser("export")
    export.add_argument("id")
    ack = sub.add_parser("simulate-receipt")
    ack.add_argument("id")
    ack.add_argument("sha256")
    ack.add_argument("state", choices=["received", "needs_clarification", "rejected", "integrated"])
    ack.add_argument("reference")
    args = parser.parse_args()
    store = Store(args.store)
    if args.command == "list":
        result = store.responses()
    elif args.command == "export":
        result = store.export(args.id)
    else:
        result = store.acknowledge(args.id, args.sha256, args.state, args.reference)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
