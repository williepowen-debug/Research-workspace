"""Exact-row replies to the existing queue. No queue/ruling writes or inferred options."""
from copy import deepcopy
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

from pilot_files import Repo, chain, fields, read_receipts, strict_json
from store import HERE, Store, digest, encoded, identifier, reader

QUEUE = "PROME/WILL_QUEUE.md"
REPLIES = "AGENTS/CATO/decisions/queue-responses"
RECEIPTS = "PROME/decisions/receipts"
IDENTITY = "local user response; PROME confirmation and interpretation required"
spec = importlib.util.spec_from_file_location("willq_reader", reader.ROOT / "PROME/tools/willq_view.py")
willq = importlib.util.module_from_spec(spec)
spec.loader.exec_module(willq)


def open_rows(text):
    try:
        metadata = willq.parse_open(text)
    except willq.WillqError as error:
        if str(error) != "OPEN table parsed to zero rows — refusing to write an empty block":
            raise ValueError(str(error)) from error
        metadata = []
    section = text.split("## OPEN", 1)[1].split("\n## ", 1)[0]
    found = {}
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = willq.split_cells(line)
        if len(cells) != 7 or not re.fullmatch(r"[1-9][0-9]*[a-z]?", cells[0]):
            continue
        if cells[0] in found:
            raise ValueError("Duplicate queue identity: " + cells[0])
        found[cells[0]] = {"cells": cells, "row": line}
    return {m["n"]: {**found[m["n"]], **m} for m in metadata}


def unit_for(row):
    c = row["cells"]
    return {"id": c[0] + ".queue", "kind": "hands" if row["kind"] == "HANDS" else "decision",
            "proposal": {"question": c[1], "context": c[6], "choices": [],
                         "recommendation": {"reason": c[5], "option_id": None}, "caveats": []},
            "timing": {"needed_by": row["due"], "meaning": c[3], "revisit_condition": None},
            "disposition": {"state": "outstanding" if row["kind"] == "HANDS" else "awaiting_answer"},
            "queue_kind": row["kind"], "blocked": row["blocked"]}


def validate_reply(repo, event, wq):
    fields(event, {"kind", "synthetic", "id", "saved_at", "request", "display", "selected_choice", "identity", "sha256"}, "Queue response")
    identifier(event["id"])
    if event["kind"] != "decisions-queue-response/1" or event["synthetic"] is not False or event["identity"] != IDENTITY:
        raise ValueError("Not a queue response")
    if digest({k: v for k, v in event.items() if k != "sha256"}) != event["sha256"]:
        raise ValueError("Queue response hash mismatch")
    d, r = event["display"], event["request"]
    fields(d, {"kind", "record", "source_path", "source_commit", "queue_row", "presentation_sha256"}, "Queue snapshot")
    fields(r, {"id", "display_hash", "unit_id", "action", "choice_id", "note", "revisit", "supersedes"}, "Queue request")
    if d["kind"] != "decisions-queue-display/1" or d["source_path"] != QUEUE:
        raise ValueError("Wrong queue source")
    row = open_rows(repo.read(QUEUE, d["source_commit"])).get(wq)
    if row is None or row["row"] != d["queue_row"] or d["record"] != {"wq_id": wq, "units": [unit_for(row)]}:
        raise ValueError("Saved queue terms differ from published source")
    if row["blocked"] or r["unit_id"] != wq + ".queue" or r["id"] != event["id"] or r["display_hash"] != digest(d):
        raise ValueError("Wrong or blocked queue response identity")
    allowed = {"reply", "request_changes", "defer"}
    if row["kind"] == "HANDS":
        allowed.add("report_done")
    if r["action"] not in allowed or r["choice_id"] is not None or event["selected_choice"] is not None:
        raise ValueError("Queue reply cannot infer or select an option")
    if not isinstance(r["note"], str) or not isinstance(r["revisit"], str):
        raise ValueError("Reply must preserve text")
    if r["action"] in {"reply", "request_changes"} and not r["note"].strip():
        raise ValueError("A reply needs your words")
    if r["action"] != "defer" and r["revisit"]:
        raise ValueError("Only deferral has a return condition")
    if r["supersedes"] is not None:
        identifier(r["supersedes"])
    from pilot_files import timestamp, sha
    timestamp(event["saved_at"])
    sha(d["presentation_sha256"])


def immutable_export(repo, event):
    path = repo.path(f"{REPLIES}/{identifier(event['id'])}.json", REPLIES)
    payload = (encoded(event) + "\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != payload:
            raise ValueError("Immutable response changed")
        return path
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".response-") as tmp:
        tmp.write(payload); tmp.flush(); os.fsync(tmp.fileno())
        try:
            os.link(tmp.name, path)
        except FileExistsError:
            if path.read_bytes() != payload:
                raise ValueError("Conflicting response export")
    return path


class QueueStore(Store):
    event_kind = "decisions-queue-response/1"
    synthetic = False
    identity = IDENTITY
    reply_allowed = True

    def __init__(self, path, repo, wq, enabled=False):
        if not re.fullmatch(r"[1-9][0-9]*[a-z]?", wq):
            raise ValueError("Invalid queue identity")
        self.repo, self.wq, self.enabled = repo, wq, enabled
        super().__init__(path)

    def source(self):
        commit = self.repo.git("rev-parse", "origin/master").strip()
        published = open_rows(self.repo.read(QUEUE, commit)).get(self.wq)
        current = open_rows(self.repo.path(QUEUE).read_text()).get(self.wq)
        head = open_rows(self.repo.read(QUEUE)).get(self.wq)
        if not published or not current or not head:
            raise ValueError("Published/current queue item unavailable or changed; sync after PROME finishes its update")
        if not (published["row"] == current["row"] == head["row"]):
            raise ValueError("Queue terms changed or are not yet published; refresh after PROME finishes")
        import hashlib
        return {"kind": "decisions-queue-display/1", "record": {"wq_id": self.wq, "units": [unit_for(current)]},
                "source_path": QUEUE, "source_commit": commit, "queue_row": current["row"],
                "presentation_sha256": hashlib.sha256((HERE / "desk.html").read_bytes()).hexdigest()}

    def current(self):
        return self.source()["record"]

    def make_snapshot(self, record):
        d = self.source()
        if d["record"] != record:
            raise ValueError("Queue changed while reading")
        return d

    def validate_display(self, snapshot, current):
        d = self.source()
        if any(snapshot[k] != d[k] for k in ("record", "queue_row", "presentation_sha256")):
            raise ValueError("Terms changed; refresh and review your answer again")
        if d["record"]["units"][0]["blocked"]:
            raise ValueError("PROME marked this item waiting on someone else")

    def restore(self):
        events = {e["id"]: e for e in self.responses()["events"]}
        for path in self.repo.files(REPLIES):
            if not re.fullmatch(re.escape(REPLIES) + r"/[0-9a-f]{32}\.json", path):
                raise ValueError("Unexpected queue response path")
            event = strict_json(self.repo.read(path, clean=True, prefix=REPLIES))
            if event.get("display", {}).get("record", {}).get("wq_id") != self.wq:
                continue
            validate_reply(self.repo, event, self.wq)
            if Path(path).stem != event["id"] or (event["id"] in events and event != events[event["id"]]):
                raise ValueError("Queue response conflicts with local history")
            events[event["id"]] = event
        for e in events.values():
            validate_reply(self.repo, e, self.wq)
        ordered = chain(list(events.values()), "id", lambda e: e["request"]["supersedes"])
        with self.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            for e in ordered:
                r = e["request"]
                db.execute("INSERT OR IGNORE INTO snapshots VALUES (?, ?)", (r["display_hash"], encoded(e["display"])))
                db.execute("INSERT OR IGNORE INTO responses VALUES (?, ?, ?, ?, ?)",
                           (e["id"], r["unit_id"], encoded(r), encoded(e), r["supersedes"]))
            if ordered:
                db.execute("INSERT OR REPLACE INTO heads VALUES (?, ?)", (self.wq + ".queue", ordered[-1]["id"]))
            db.commit()
        return ordered

    def display(self):
        errors = []
        events = self.restore()
        receipts, integration = {}, None
        for e in events:
            try:
                found = read_receipts(self.repo, e)
                if found:
                    receipts[e["id"]] = found[-1]
                    if found[-1]["state"] == "integrated":
                        integration = found[-1]
            except (ValueError, OSError, subprocess.CalledProcessError) as error:
                errors.append(str(error))
        historical = False
        if integration:
            d = next(e["display"] for e in events if e["id"] == integration["response_id"])
            historical = True
        else:
            try:
                d = self.source()
            except (ValueError, OSError, subprocess.CalledProcessError) as error:
                if not events:
                    raise
                d = events[-1]["display"]
                historical = True
                errors.append(str(error))
        key = digest(d)
        with self.connection() as db:
            db.execute("INSERT OR IGNORE INTO snapshots VALUES (?, ?)", (key, encoded(d)))
        unit = d["record"]["units"][0]
        last = events[-1] if events else None
        group = "History" if integration else ("Follow-through" if last or unit["queue_kind"] not in {"HANDS", "DECISION"}
                                               else ("Tasks for me" if unit["kind"] == "hands" else "Decisions"))
        return {"wq_id": self.wq, "unit": unit, "snapshot": d, "hash": key, "group": group,
                "events": events, "last": last, "receipt": integration or (receipts.get(last["id"]) if last else None),
                "errors": errors, "can_respond": self.enabled and not historical and not errors and not unit["blocked"],
                "response_type": "queue", "requires_confirmation": True}

    def save(self, request):
        if not self.enabled:
            raise ValueError("Daily responses await final acceptance; this view is read-only")
        state = self.display()
        existing = next((e for e in state["events"] if e["id"] == request.get("id")), None)
        if not state["can_respond"] and existing is None:
            raise ValueError("This item is closed or needs reconciliation; no new answer can be saved")
        event = super().save(request)
        validate_reply(self.repo, event, self.wq)
        try:
            immutable_export(self.repo, event)
        except (ValueError, OSError) as error:
            raise ValueError("Saved locally; delivery file pending. Retry the same response: " + str(error)) from error
        return event

    def acknowledge(self, *args, **kwargs):
        raise ValueError("Only PROME writes owner receipts")
