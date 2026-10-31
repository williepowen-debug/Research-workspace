#!/usr/bin/env python3
"""Candidate file adapters. No live activation, owner writes, Git mutation or sends."""
from __future__ import annotations

from datetime import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile

from store import HERE, Store, digest, encoded, identifier, reader

RESPONSES = "AGENTS/CATO/decisions/responses"
RECEIPTS = "PROME/decisions/receipts"
IDENTITY = "supervised local user; PROME chat confirmation required before integration"
REQUEST_FIELDS = {"id", "display_hash", "unit_id", "action", "choice_id", "note", "revisit", "supersedes"}
SNAPSHOT_FIELDS = {"kind", "record", "source_path", "source_commit", "source_text", "queue_row", "fingerprint", "presentation_sha256"}


def strict_json(text):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError(f"Duplicate JSON field: {key}")
            out[key] = value
        return out
    return json.loads(text, object_pairs_hook=pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError("Nonfinite JSON number")))


def fields(value, expected, label):
    if not isinstance(value, dict) or set(value) != set(expected):
        raise ValueError(f"{label} fields do not match the pilot contract")


def sha(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
        raise ValueError("Expected a SHA-256 digest")
    return value


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError("Timestamp must be text")
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("Timestamp requires a timezone")
    return parsed


class Repo:
    def __init__(self, root):
        self.root = Path(root).resolve(strict=True)
        actual = Path(self.git("rev-parse", "--show-toplevel").strip()).resolve()
        if actual != self.root:
            raise ValueError("Expected the Git repository root")

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root,
                                       stderr=subprocess.PIPE).decode("utf-8")

    def path(self, name, prefix=None):
        if not isinstance(name, str) or any(c in name for c in ("\\", ":", "\x00", "\n")):
            raise ValueError("Invalid repository path")
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or str(path) != name or name in {"", "."}:
            raise ValueError("Out-of-workspace path")
        if prefix and not name.startswith(prefix + "/"):
            raise ValueError("Wrong owner path")
        candidate = self.root
        for component in path.parts:
            candidate /= component
            if candidate.is_symlink():
                raise ValueError("Symlink paths are not pilot artifacts")
        if not candidate.resolve().is_relative_to(self.root):
            raise ValueError("Path escapes repository")
        return candidate

    def read(self, path, commit="HEAD", clean=False, prefix=None):
        target = self.path(path, prefix)
        if commit not in {"HEAD", "origin/master"} and not re.fullmatch(r"[0-9a-f]{40}", commit):
            raise ValueError("Expected a pinned commit")
        row = self.git("ls-tree", commit, "--", path).split("\t", 1)
        if len(row) != 2 or row[0].split()[0] not in {"100644", "100755"}:
            raise ValueError(f"Committed regular file missing: {path}")
        content = self.git("show", f"{commit}:{path}")
        if len(content.encode("utf-8")) > 8_000_000:
            raise ValueError("Pilot artifact exceeds read limit")
        if clean and target.read_bytes() != content.encode("utf-8"):
            raise ValueError(f"Uncommitted artifact change: {path}")
        return content

    def files(self, prefix):
        self.path(prefix)
        return self.git("ls-tree", "-r", "--name-only", "HEAD", "--", prefix).splitlines()


def record_block(text, label="wq-record"):
    # Recognize CommonMark backtick/tilde fences, including up to three spaces.
    # Scan all fences so a nested example cannot masquerade as a record.
    blocks, fence, body, is_record = [], None, [], False
    for line in text.splitlines():
        # The adopted dialect forbids container fences and invalid backtick info.
        # Reject rather than pretending this small scanner is a Markdown parser.
        if re.match(r"\s*(?:>\s*|[-+*]\s+|\d+[.)]\s+)+(?:.*?)(?:`{3,}|~{3,})", line):
            raise ValueError(f"Expected exactly one top-level {label} block; container fences are unsupported")
        if fence is None:
            opening = re.fullmatch(r" {0,3}(`{3,}|~{3,})([^\r\n]*)", line)
            if opening:
                fence, info = opening.groups()
                if fence[0] == "`" and "`" in info:
                    raise ValueError("Invalid backtick fence info; ambiguous record source")
                is_record = info.strip().split(None, 1)[:1] == [label]
                body = []
        elif re.fullmatch(r" {0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}[ \t]*", line):
            if is_record:
                blocks.append("\n".join(body))
            fence = None
        else:
            body.append(line)
    if fence is not None and is_record:
        raise ValueError(f"Unclosed {label} block")
    if len(blocks) != 1:
        raise ValueError(f"Expected exactly one {label} block")
    return strict_json(blocks[0])


def validate_record(repo, record):
    # Keep the existing shape, with a distinct dialect that cannot launder design copies.
    schema = strict_json(reader.source_text(reader.SCHEMA_REV, reader.SCHEMA_PATH))
    schema["properties"]["schema_version"] = {"const": "wq-record/0.1-pilot"}
    schema["properties"]["mode"] = {"const": "supervised-pilot"}
    reader.Draft202012Validator(schema, format_checker=reader.FormatChecker()).validate(record)
    sources = record["sources"]
    reader.unique([s["id"] for s in sources], "source ID")
    reader.unique([u["id"] for u in record["units"]], "unit ID")
    source_ids = {s["id"] for s in sources}
    unit_ids = {u["id"] for u in record["units"]}
    for source in sources:
        if not isinstance(source["commit"], str) or not re.fullmatch(r"[0-9a-f]{40}", source["commit"]):
            raise ValueError("Pilot evidence must have a pinned commit")
        repo.read(source["path"], source["commit"])
    for unit in record["units"]:
        if not unit["id"].startswith(record["wq_id"] + "."):
            raise ValueError("Unit belongs to another WQ")
        choices = unit["proposal"]["choices"]
        reader.unique([c["id"] for c in choices], "choice ID")
        choice_ids = {c["id"] for c in choices}
        recommended = unit["proposal"]["recommendation"]["option_id"]
        if recommended is not None and recommended not in choice_ids:
            raise ValueError("Unknown recommended choice")
        refs = unit["proposal"]["source_ids"] + unit["disposition"]["source_ids"]
        refs += [f["source_id"] for f in unit["follow_through"]]
        ruling = unit["disposition"]["ruling"]
        if ruling:
            refs += [ruling["source_id"], *ruling["proposal_source_ids"]]
            if (ruling["answered_proposal_revision"] == unit["proposal"]["revision"]
                    and ruling["selected_option_id"] is not None and ruling["selected_option_id"] not in choice_ids):
                raise ValueError("Ruling choice missing from answered revision")
        if not set(refs) <= source_ids:
            raise ValueError("Unknown evidence reference")
    for correction in record["corrections"]:
        if correction["source_id"] not in source_ids or not set(correction["affected_unit_ids"]) <= unit_ids:
            raise ValueError("Unknown correction reference")


def queue_row(text, wq_id):
    rows = [line for line in text.splitlines() if line.lstrip().startswith("|") and line.split("|")[1].strip() == wq_id]
    if len(rows) != 1:
        raise ValueError("Pilot WQ row is missing or ambiguous; no permission inferred")
    return rows[0]


def snapshot(repo, source_path, wq_id, unit_id, presentation_sha256):
    if not re.fullmatch(r"[1-9][0-9]*[a-z]?", wq_id) or not unit_id.startswith(wq_id + "."):
        raise ValueError("Pilot requires its registered WQ and unit identity")
    sha(presentation_sha256)
    head = repo.git("rev-parse", "HEAD").strip()
    source = repo.read(source_path, head, clean=True, prefix="PROME/proposals")
    if not source_path.endswith(".md"):
        raise ValueError("Pilot source must be a PROME Markdown proposal")
    record = record_block(source)
    validate_record(repo, record)
    if record["wq_id"] != wq_id or len(record["units"]) != 1 or record["units"][0]["id"] != unit_id:
        raise ValueError("Source does not match the single registered pilot unit")
    unit = record["units"][0]
    if unit["kind"] != "decision":
        raise ValueError("Pilot is not a decision")
    committed_queue = repo.read("PROME/WILL_QUEUE.md", head)
    row = queue_row(committed_queue, wq_id)
    working_row = queue_row(repo.path("PROME/WILL_QUEUE.md").read_text(), wq_id)
    if row != working_row:
        raise ValueError("Direct queue edit requires owner reconciliation")
    # Only published history survives the normal rebase of local commits. Bind
    # BOTH source and selected queue row to the same already-published commit.
    published = repo.git("rev-parse", "origin/master").strip()
    if (repo.read(source_path, published) != source
            or queue_row(repo.read("PROME/WILL_QUEUE.md", published), wq_id) != row):
        raise ValueError("Pilot source and queue row must be published before display or answer")
    content = {"record": record, "source_path": source_path, "source_text": source, "queue_row": row}
    return {"kind": "decisions-display/1", **content, "source_commit": published,
            "fingerprint": digest(content), "presentation_sha256": presentation_sha256}


def assert_current(repo, displayed):
    record = displayed["record"]
    current = snapshot(repo, displayed["source_path"], record["wq_id"], record["units"][0]["id"],
                       displayed["presentation_sha256"])
    if current["fingerprint"] != displayed["fingerprint"]:
        raise ValueError("Pilot terms or queue row changed; redisplay and review")
    return current


def validate_event(repo, event, wq_id, unit_id, source_path=None):
    fields(event, {"kind", "synthetic", "id", "saved_at", "request", "display", "selected_choice", "identity", "sha256"}, "Response")
    if event["kind"] != "decisions-response/1" or event["synthetic"] is not False or event["identity"] != IDENTITY:
        raise ValueError("Not a supervised pilot response")
    identifier(event["id"])
    timestamp(event["saved_at"])
    if sha(event["sha256"]) != digest({k: v for k, v in event.items() if k != "sha256"}):
        raise ValueError("Response hash mismatch")
    display = event["display"]
    fields(display, SNAPSHOT_FIELDS, "Display")
    if display["kind"] != "decisions-display/1":
        raise ValueError("Wrong display kind")
    if source_path is not None and display["source_path"] != source_path:
        raise ValueError("Response belongs to another source path")
    sha(display["presentation_sha256"])
    content = {key: display[key] for key in ("record", "source_path", "source_text", "queue_row")}
    if sha(display["fingerprint"]) != digest(content):
        raise ValueError("Display fingerprint mismatch")
    original = repo.read(display["source_path"], display["source_commit"], prefix="PROME/proposals")
    if original != display["source_text"] or record_block(original) != display["record"]:
        raise ValueError("Displayed terms disagree with their original source")
    record = display["record"]
    validate_record(repo, record)
    if record["wq_id"] != wq_id or len(record["units"]) != 1 or record["units"][0]["id"] != unit_id:
        raise ValueError("Response belongs to another pilot")
    if queue_row(repo.read("PROME/WILL_QUEUE.md", display["source_commit"]), wq_id) != display["queue_row"]:
        raise ValueError("Original queue-row binding mismatch")
    unit = record["units"][0]
    if (unit["kind"] != "decision" or unit["disposition"]["state"] != "awaiting_answer"
            or unit["proposal"]["submission_block_reason"] is not None):
        raise ValueError("Original pilot terms did not permit an answer")
    request = event["request"]
    fields(request, REQUEST_FIELDS, "Request")
    if request["id"] != event["id"] or request["unit_id"] != unit_id or request["display_hash"] != digest(display):
        raise ValueError("Response identity/display mismatch")
    if request["supersedes"] is not None:
        identifier(request["supersedes"])
    if not isinstance(request["note"], str) or not isinstance(request["revisit"], str):
        raise ValueError("Conditions must be preserved text")
    choices = {c["id"]: c for c in unit["proposal"]["choices"]}
    action = request["action"]
    if action not in {"choose", "defer", "request_changes"}:
        raise ValueError("Wrong pilot action")
    if action == "choose":
        if request["choice_id"] not in choices or event["selected_choice"] != choices[request["choice_id"]]:
            raise ValueError("Selected option does not preserve the shown meaning")
    elif request["choice_id"] is not None or event["selected_choice"] is not None:
        raise ValueError("A deferral/question cannot select an approval")
    if action == "request_changes" and not request["note"].strip():
        raise ValueError("A question needs the operator's words")
    if action != "defer" and request["revisit"]:
        raise ValueError("Only deferral has a return condition")


def chain(items, id_key, previous_key):
    by_id = {item[id_key]: item for item in items}
    if len(by_id) != len(items):
        raise ValueError("Duplicate chain ID")
    if not items:
        return []
    children = {}
    for item in items:
        previous = previous_key(item)
        if previous is not None and previous not in by_id:
            raise ValueError("Missing predecessor")
        if previous in children:
            raise ValueError("Conflicting branches; owner reconciliation required")
        children[previous] = item
    ordered, current = [], children.get(None)
    while current:
        if current in ordered:
            raise ValueError("Cyclic history")
        ordered.append(current)
        current = children.get(current[id_key])
    if len(ordered) != len(items):
        raise ValueError("History has a disconnected cycle")
    return ordered


def export_event(repo, event, wq_id, unit_id):
    validate_event(repo, event, wq_id, unit_id)
    path = repo.path(f"{RESPONSES}/{event['id']}.json", RESPONSES)
    payload = (encoded(event) + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != payload:
            raise ValueError("Immutable response path already contains different bytes")
        return path
    # Publish a complete file without overwriting any simultaneous winner.
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".response-", delete=True) as temporary:
        temporary.write(payload)
        temporary.flush()
        os.fsync(temporary.fileno())
        try:
            os.link(temporary.name, path)
        except FileExistsError:
            if path.read_bytes() != payload:
                raise ValueError("Concurrent export conflicts with the existing response")
    directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)
    return path


def import_responses(repo, store, wq_id, unit_id):
    if store.event_kind != "decisions-response/1":
        raise ValueError("Pilot import cannot use the rehearsal database")
    incoming, errors = [], []
    store.import_errors = errors
    for path in repo.files(RESPONSES):
        if not re.fullmatch(re.escape(RESPONSES) + r"/[0-9a-f]{32}\.json", path):
            raise ValueError("Unexpected response file in the adopted path")
        event = strict_json(repo.read(path, clean=True, prefix=RESPONSES))
        try:
            validate_event(repo, event, wq_id, unit_id, store.source_path)
        except subprocess.CalledProcessError:
            errors.append({"path": path, "reason": "Pinned Git evidence unavailable; response quarantined"})
            continue
        if Path(path).stem != event["id"]:
            raise ValueError("Response filename/ID mismatch")
        incoming.append(event)
    with store.connection() as db:
        db.execute("BEGIN IMMEDIATE")
        existing = {json.loads(row[0])["id"]: json.loads(row[0]) for row in db.execute("SELECT body FROM responses")}
        combined = dict(existing)
        for event in existing.values():
            try:
                validate_event(repo, event, wq_id, unit_id, store.source_path)
            except subprocess.CalledProcessError:
                errors.append({"path": f"local response {event['id']}", "reason": "Pinned Git evidence unavailable; response quarantined"})
                combined.pop(event["id"])
        for event in incoming:
            if event["id"] in combined and combined[event["id"]] != event:
                raise ValueError("Imported response conflicts with local history")
            combined[event["id"]] = event
        # Preserve the usable prefix while quarantining descendants of a lost
        # event. Never promote a later reply across a missing predecessor.
        if errors:
            while True:
                missing = [e for e in combined.values() if e["request"]["supersedes"] is not None
                           and e["request"]["supersedes"] not in combined]
                if not missing:
                    break
                for event in missing:
                    errors.append({"path": f"response {event['id']}", "reason": "Predecessor unavailable; response quarantined"})
                    combined.pop(event["id"])
        ordered = chain(list(combined.values()), "id", lambda e: e["request"]["supersedes"])
        for event in ordered:
            if event["id"] in existing:
                continue
            request = event["request"]
            db.execute("INSERT OR IGNORE INTO snapshots VALUES (?, ?)", (request["display_hash"], encoded(event["display"])))
            saved = db.execute("SELECT body FROM snapshots WHERE hash=?", (request["display_hash"],)).fetchone()
            if saved[0] != encoded(event["display"]):
                raise ValueError("Local display snapshot conflicts with imported content")
            db.execute("INSERT INTO responses VALUES (?, ?, ?, ?, ?)",
                       (event["id"], unit_id, encoded(request), encoded(event), request["supersedes"]))
        if ordered:
            db.execute("INSERT OR REPLACE INTO heads VALUES (?, ?)", (unit_id, ordered[-1]["id"]))
        db.commit()
    store.visible_response_ids = set(combined)
    committed_responses = set(repo.files(RESPONSES))
    queue_responses = set(repo.files("AGENTS/CATO/decisions/queue-responses"))
    # A retired event must not erase the fact that its owner issued a receipt.
    for path in repo.files(RECEIPTS):
        match = re.fullmatch(re.escape(RECEIPTS) + r"/([0-9a-f]{32})/[0-9a-f]{32}\.json", path)
        if not match:
            raise ValueError("Unexpected owner receipt path")
        event_path = f"{RESPONSES}/{match[1]}.json"
        if event_path not in committed_responses:
            queue_path = f"AGENTS/CATO/decisions/queue-responses/{match[1]}.json"
            if queue_path in queue_responses:
                # The daily desk's separate dialect has its own validator. It
                # must not mask a retired response belonging to this pilot.
                from queue_store import validate_reply
                other = strict_json(repo.read(queue_path, clean=True))
                if other.get("display", {}).get("record", {}).get("wq_id") != wq_id:
                    validate_reply(repo, other, other["display"]["record"]["wq_id"])
                    continue
            errors.append({"path": path, "reason": "Owner receipt has no committed response; reconciliation required"})
    return len(combined) - len(existing)


def read_receipts(repo, event, commit="HEAD"):
    event_id = identifier(event["id"])
    prefix = f"{RECEIPTS}/{event_id}"
    receipts = []
    expected = {"schema_version", "id", "response_id", "response_sha256", "state", "at", "previous_receipt_id",
                "canonical_ruling", "chat_confirmation", "confirmed_response_sha256"}
    for path in repo.git("ls-tree", "-r", "--name-only", commit, "--", prefix).splitlines():
        if not re.fullmatch(re.escape(prefix) + r"/[0-9a-f]{32}\.json", path):
            raise ValueError("Unexpected owner receipt path")
        receipt = strict_json(repo.read(path, commit, clean=commit == "HEAD", prefix=prefix))
        fields(receipt, expected, "Receipt")
        identifier(receipt["id"])
        if Path(path).stem != receipt["id"] or receipt["schema_version"] != "decisions-receipt/1":
            raise ValueError("Receipt filename/schema mismatch")
        if receipt["response_id"] != event_id or receipt["response_sha256"] != event["sha256"]:
            raise ValueError("Receipt names another response/hash")
        timestamp(receipt["at"])
        if receipt["previous_receipt_id"] is not None:
            identifier(receipt["previous_receipt_id"])
        if receipt["state"] not in {"received", "needs_clarification", "rejected_stale", "integrated"}:
            raise ValueError("Unknown receipt state; no completed-work inference")
        if receipt["state"] == "integrated":
            if receipt["confirmed_response_sha256"] != event["sha256"]:
                raise ValueError("Integration lacks the matching chat-confirmation assertion")
            for key in ("canonical_ruling", "chat_confirmation"):
                ref = receipt[key]
                fields(ref, {"path", "commit"}, key)
                if not re.fullmatch(r"[0-9a-f]{40}", ref["commit"]):
                    raise ValueError("Receipt evidence must be pinned")
                try:
                    repo.git("merge-base", "--is-ancestor", ref["commit"], "origin/master")
                except subprocess.CalledProcessError as error:
                    raise ValueError("Receipt evidence is missing or unpublished; reconciliation required") from error
                repo.read(ref["path"], ref["commit"], prefix="PROME/proposals")
            if not receipt["canonical_ruling"]["path"].endswith("-RULED.md"):
                raise ValueError("Canonical integration requires a ruling record")
        elif any(receipt[key] is not None for key in ("canonical_ruling", "chat_confirmation", "confirmed_response_sha256")):
            raise ValueError("Non-integrated receipt contains ambiguous ruling fields")
        receipts.append(receipt)
    ordered = chain(receipts, "id", lambda r: r["previous_receipt_id"])
    for earlier, later in zip(ordered, ordered[1:]):
        if earlier["state"] != "received" or later["state"] == "received" or timestamp(later["at"]) < timestamp(earlier["at"]):
            raise ValueError("Invalid or conflicting receipt progression")
    return ordered


def delivery_status(repo, event):
    path = f"{RESPONSES}/{identifier(event['id'])}.json"
    expected = encoded(event) + "\n"
    target = repo.path(path, RESPONSES)
    if not target.exists():
        return "saved locally; no export present"
    if target.read_text() != expected:
        raise ValueError("Export differs from saved response")
    try:
        committed = repo.read(path)
    except (ValueError, subprocess.CalledProcessError):
        return "exported locally; not committed"
    if committed != expected:
        raise ValueError("Committed event differs from saved response")
    try:
        remote = repo.read(path, "origin/master")
    except (ValueError, subprocess.CalledProcessError):
        return "committed locally; remote delivery unverified"
    if remote != expected:
        raise ValueError("Last-fetched remote event conflicts with local response")
    return "present in last-fetched origin/master; fresh delivery and acknowledgment not established"


class PilotStore(Store):
    """Candidate backend; no public live launch option is installed.

    enable_submissions is false by default. The caller may enable it only after
    owner source acceptance and independent review. Tests enable isolated repos.
    """
    event_kind = "decisions-response/1"
    synthetic = False
    identity = IDENTITY

    def __init__(self, path, repo, source_path, wq_id, unit_id, *, enable_submissions=False):
        self.repo, self.source_path, self.wq_id, self.unit_id = repo, source_path, wq_id, unit_id
        self.enable_submissions = enable_submissions
        super().__init__(path)

    def source(self):
        return snapshot(self.repo, self.source_path, self.wq_id, self.unit_id,
                        hashlib.sha256((HERE / "index.html").read_bytes()).hexdigest())

    def current(self):
        return self.source()["record"]

    def make_snapshot(self, record):
        displayed = self.source()
        if displayed["record"] != record:
            raise ValueError("Source changed during display; retry the read")
        return displayed

    def validate_display(self, displayed, current):
        super().validate_display(displayed, current)
        assert_current(self.repo, displayed)
        unit = current["units"][0]
        if unit["proposal"]["submission_block_reason"] is not None or not unit["proposal"]["choices"]:
            raise ValueError("Owner withheld pilot submission or choices")

    def display(self):
        try:
            import_responses(self.repo, self, self.wq_id, self.unit_id)
        except (ValueError, subprocess.CalledProcessError) as error:
            # A bad history must not hide the proposal or create permission.
            self.import_errors = [{"path": RESPONSES, "reason": str(error)}]
            self.visible_response_ids = set()
        responses = self.responses()
        responses["events"] = [e for e in responses["events"] if e["id"] in self.visible_response_ids]
        responses["heads"] = ({self.unit_id: chain(responses["events"], "id", lambda e: e["request"]["supersedes"])[-1]["id"]}
                              if responses["events"] else {})
        responses["integrated"] = {}
        responses["receipt_history"], responses["receipts"], responses["delivery"] = [], {}, {}
        for event in responses["events"]:
            try:
                receipts = read_receipts(self.repo, event)
            except (ValueError, OSError, subprocess.CalledProcessError) as error:
                self.import_errors.append({"path": f"{RECEIPTS}/{event['id']}", "reason": str(error)})
                receipts = []
            responses["receipt_history"].extend(receipts)
            if receipts:
                responses["receipts"][event["id"]] = receipts[-1]
                if receipts[-1]["state"] == "integrated":
                    responses["integrated"][self.unit_id] = receipts[-1]
            responses["delivery"][event["id"]] = delivery_status(self.repo, event)
        integrated = responses["integrated"].get(self.unit_id)
        historical = False
        if integrated:
            # A ruling consumes the live queue row. Its exact saved terms remain
            # the display authority for this historical answer, never for a save.
            displayed = next(e["display"] for e in responses["events"]
                             if e["id"] == integrated["response_id"])
            historical = True
        else:
            try:
                displayed = self.source()
            except (ValueError, OSError, subprocess.CalledProcessError) as error:
                if not responses["events"]:
                    raise
                displayed = responses["events"][-1]["display"]
                historical = True
                self.import_errors.append({"path": self.source_path,
                                           "reason": "Saved terms only; current source unavailable: " + str(error)})
        record = displayed["record"]
        key = digest(displayed)
        with self.connection() as db:
            db.execute("INSERT OR IGNORE INTO snapshots VALUES (?, ?)", (key, encoded(displayed)))
        groups = {name: [] for name in reader.GROUPS}
        unit = record["units"][0]
        group = "History" if integrated else ("Decisions" if unit["disposition"]["state"] == "awaiting_answer" else "Follow-through")
        groups[group].append({"wq_id": self.wq_id, "title": record["title"], "unit": unit,
                              "sources": record["sources"], "observations": [], "corrections": record["corrections"]})
        return {"hash": key, "snapshot": displayed, "responses": responses, "groups": groups,
                "mode": "supervised-pilot", "submissions_enabled": self.enable_submissions and not self.import_errors and not historical and not integrated,
                "import_errors": self.import_errors,
                "notice": "Decision recorded by PROME." if integrated else "Saved answers keep their exact terms. PROME records the ruling after matching chat confirmation."}

    def save(self, request):
        if not self.enable_submissions:
            raise ValueError("Pilot submissions remain disabled pending owner contract and independent acceptance")
        import_responses(self.repo, self, self.wq_id, self.unit_id)
        if self.import_errors:
            raise ValueError("Response history needs owner reconciliation; submissions disabled")
        state = self.responses()
        if isinstance(request, dict) and not any(e["id"] == request.get("id") for e in state["events"]):
            for previous in state["events"]:
                receipts = read_receipts(self.repo, previous)
                if receipts and receipts[-1]["state"] == "integrated":
                    raise ValueError("This answer is already integrated; PROME must supply a new question before another response")
        event = super().save(request)
        try:
            export_event(self.repo, event, self.wq_id, self.unit_id)
        except (OSError, ValueError) as error:
            raise ValueError(f"Saved locally; export pending: {error}. Retry the unchanged response.") from error
        return event

    def acknowledge(self, *args, **kwargs):
        raise ValueError("Only PROME writes pilot receipts; synthetic acknowledgment is unavailable")

    def export(self, event_id):
        if not self.enable_submissions:
            raise ValueError("Pilot exports remain disabled with submissions")
        event = next((e for e in self.responses()["events"] if e["id"] == identifier(event_id)), None)
        if event is None:
            raise ValueError("Unknown pilot response")
        return str(export_event(self.repo, event, self.wq_id, self.unit_id))
