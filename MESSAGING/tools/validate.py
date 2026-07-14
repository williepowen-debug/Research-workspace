#!/usr/bin/env python3
"""Read-only validator for Direct Agent Messaging v1 Markdown records."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment failure
    raise SystemExit("PyYAML is required: python -m pip install -r MESSAGING/requirements.txt") from exc


MESSAGE_ID_RE = re.compile(r"^MSG-([A-Z][A-Z0-9_-]*)-(\d{8})-(\d{3})$")
AGENT_ID_RE = re.compile(r"^[A-Z][A-Z0-9_-]*$")
OBLIGATION_ID_RE = re.compile(r"^(MSG-[A-Z][A-Z0-9_-]*-\d{8}-\d{3})#([A-Z][A-Z0-9_-]*)-(\d{2})$")
INBOX_RE = re.compile(r"(?:^|/)AGENTS/([^/]+)/inbox(?:/|$)")
RECEIPT_PATH_RE = re.compile(r"(?:^|/)AGENTS/([^/]+)/messages/receipts(?:/|$)")

MESSAGE_FIELDS = {"schema", "message_id", "created_at", "from", "subject", "supersedes", "related", "obligations"}
OBLIGATION_FIELDS = {"obligation_id", "to", "role", "urgency", "requested_action", "definition_of_done", "due", "receipt_required", "expected_targets"}
RECEIPT_FIELDS = {"schema", "message_id", "recipient", "obligations"}
URGENCIES = {"URGENT", "NEXT_BOOT", "SCHEDULED", "ROUTINE"}
EVENTS = {"ACKNOWLEDGED", "ACCEPTED", "DEFERRED", "BLOCKED", "REJECTED", "NOTED", "COMPLETED", "INTEGRATED", "NO_CHANGE"}
TERMINAL = {"REJECTED", "NOTED", "INTEGRATED", "NO_CHANGE"}
EVIDENCE_TIERS = {"ASSERTED", "POINTED", "CORROBORATED", "COMMIT_LINKED"}
RECEIPT_HEADERS = ["event_at", "obligation_id", "event", "next_review_at", "target_path", "effect_or_reason", "commit", "evidence_tier"]


@dataclass
class Finding:
    severity: str
    path: str
    code: str
    message: str


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)
    messages: dict[str, dict[str, Any]] = field(default_factory=dict)
    obligations: dict[str, dict[str, Any]] = field(default_factory=dict)
    receipts: int = 0

    def add(self, severity: str, path: Path, code: str, message: str) -> None:
        self.findings.append(Finding(severity, str(path), code, message))

    @property
    def errors(self) -> int:
        return sum(f.severity == "ERROR" for f in self.findings)

    @property
    def warnings(self) -> int:
        return sum(f.severity == "WARNING" for f in self.findings)


def load_front_matter(path: Path) -> tuple[dict[str, Any] | None, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("front matter opens with --- but has no closing ---") from exc
    data = yaml.safe_load("\n".join(lines[1:end]))
    if not isinstance(data, dict):
        raise ValueError("front matter must decode to a mapping")
    return data, "\n".join(lines[end + 1 :])


def parse_timestamp(value: Any) -> dt.datetime | None:
    if isinstance(value, dt.datetime):
        parsed = value
    elif isinstance(value, str):
        candidate = value[:-1] + "+00:00" if value.endswith("Z") else value
        try:
            parsed = dt.datetime.fromisoformat(candidate)
        except ValueError:
            return None
    else:
        return None
    return parsed if parsed.tzinfo is not None else None


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_exact_fields(report: Report, path: Path, data: dict[str, Any], allowed: set[str], label: str) -> None:
    missing = sorted(allowed - data.keys())
    extra = sorted(data.keys() - allowed)
    if missing:
        report.add("ERROR", path, "missing_fields", f"{label} missing: {', '.join(missing)}")
    if extra:
        report.add("ERROR", path, "unknown_fields", f"{label} unknown fields: {', '.join(extra)}")


def valid_agent(report: Report, path: Path, value: Any, field_name: str, agents: set[str]) -> bool:
    if not isinstance(value, str) or not AGENT_ID_RE.fullmatch(value):
        report.add("ERROR", path, "invalid_agent_id", f"{field_name} is not a valid agent ID: {value!r}")
        return False
    if agents and value not in agents:
        report.add("ERROR", path, "unknown_agent", f"{field_name} is not present in the roster: {value}")
        return False
    return True


def validate_message(report: Report, path: Path, data: dict[str, Any], agents: set[str]) -> None:
    validate_exact_fields(report, path, data, MESSAGE_FIELDS, "message")
    if data.get("schema") != "direct-message/v1":
        report.add("ERROR", path, "schema", "schema must be direct-message/v1")

    message_id = data.get("message_id")
    match = MESSAGE_ID_RE.fullmatch(message_id or "") if isinstance(message_id, str) else None
    if not match:
        report.add("ERROR", path, "message_id", f"invalid message_id: {message_id!r}")
    elif message_id in report.messages:
        existing = {key: value for key, value in report.messages[message_id].items() if key != "source_path"}
        if existing != data:
            report.add("ERROR", path, "duplicate_message_conflict", f"message_id has conflicting payloads: {message_id}")

    sender = data.get("from")
    valid_agent(report, path, sender, "from", agents)
    created = parse_timestamp(data.get("created_at"))
    if not created:
        report.add("ERROR", path, "created_at", "created_at must be a valid ISO 8601 timestamp with timezone")
    if match and sender != match.group(1):
        report.add("ERROR", path, "sender_mismatch", "message_id sender does not match from")
    if match and created and created.astimezone(dt.timezone.utc).strftime("%Y%m%d") != match.group(2):
        report.add("ERROR", path, "date_mismatch", "message_id date must equal created_at UTC date")
    if not nonempty(data.get("subject")):
        report.add("ERROR", path, "subject", "subject must be non-empty")
    if data.get("supersedes") is not None and not MESSAGE_ID_RE.fullmatch(str(data.get("supersedes"))):
        report.add("ERROR", path, "supersedes", "supersedes must be null or a valid message ID")
    if not isinstance(data.get("related"), list) or any(not nonempty(v) for v in data.get("related", [])):
        report.add("ERROR", path, "related", "related must be a list of non-empty strings")

    obligations = data.get("obligations")
    if not isinstance(obligations, list) or not obligations:
        report.add("ERROR", path, "obligations", "obligations must be a non-empty list")
        obligations = []
    delivered_recipient = None
    inbox_match = INBOX_RE.search(path.as_posix())
    if inbox_match:
        delivered_recipient = inbox_match.group(1).upper()

    matching_delivery = False
    local_ids: set[str] = set()
    for index, obligation in enumerate(obligations, start=1):
        label = f"obligation[{index}]"
        if not isinstance(obligation, dict):
            report.add("ERROR", path, "obligation_type", f"{label} must be a mapping")
            continue
        validate_exact_fields(report, path, obligation, OBLIGATION_FIELDS, label)
        oid = obligation.get("obligation_id")
        omatch = OBLIGATION_ID_RE.fullmatch(oid or "") if isinstance(oid, str) else None
        if not omatch:
            report.add("ERROR", path, "obligation_id", f"{label} has invalid obligation_id: {oid!r}")
        elif message_id != omatch.group(1):
            report.add("ERROR", path, "obligation_message", f"{oid} does not belong to {message_id}")
        elif oid in local_ids:
            report.add("ERROR", path, "duplicate_obligation", f"duplicate obligation_id: {oid}")
        elif oid in report.obligations:
            existing = {key: value for key, value in report.obligations[oid].items() if key != "source_path"}
            if existing != obligation:
                report.add("ERROR", path, "duplicate_obligation_conflict", f"obligation_id has conflicting definitions: {oid}")
        local_ids.add(str(oid))

        recipient = obligation.get("to")
        valid_agent(report, path, recipient, f"{label}.to", agents)
        if omatch and recipient != omatch.group(2):
            report.add("ERROR", path, "obligation_recipient", f"{oid} recipient does not match to")
        if delivered_recipient and recipient == delivered_recipient:
            matching_delivery = True

        role = obligation.get("role")
        urgency = obligation.get("urgency")
        due = obligation.get("due")
        action = obligation.get("requested_action")
        done = obligation.get("definition_of_done")
        receipt_required = obligation.get("receipt_required")
        targets = obligation.get("expected_targets")
        if role not in {"ACTION", "INFO"}:
            report.add("ERROR", path, "role", f"{label}.role must be ACTION or INFO")
        if urgency not in URGENCIES:
            report.add("ERROR", path, "urgency", f"{label}.urgency is invalid: {urgency!r}")
        if not isinstance(receipt_required, bool):
            report.add("ERROR", path, "receipt_required", f"{label}.receipt_required must be boolean")
        if not isinstance(targets, list) or any(not nonempty(v) for v in targets):
            report.add("ERROR", path, "expected_targets", f"{label}.expected_targets must be a list of paths")

        if role == "ACTION":
            if not nonempty(action):
                report.add("ERROR", path, "requested_action", f"{label} ACTION requires requested_action")
            if not nonempty(done):
                report.add("ERROR", path, "definition_of_done", f"{label} ACTION requires definition_of_done")
            if receipt_required is not True:
                report.add("ERROR", path, "action_receipt", f"{label} ACTION requires receipt_required: true")
            if urgency != "ROUTINE" and due in (None, ""):
                report.add("ERROR", path, "due", f"{label} non-ROUTINE ACTION requires due")
        elif role == "INFO":
            if action not in (None, "") or done not in (None, ""):
                report.add("ERROR", path, "info_action", f"{label} INFO cannot contain requested action or definition of done")

        if urgency in {"URGENT", "SCHEDULED"} and not parse_timestamp(due):
            report.add("ERROR", path, "due_timestamp", f"{label} {urgency} requires an ISO 8601 due timestamp")
        if urgency == "NEXT_BOOT" and due != "next_boot":
            report.add("ERROR", path, "next_boot_due", f"{label} NEXT_BOOT requires due: next_boot")
        if oid and isinstance(obligation, dict):
            report.obligations.setdefault(str(oid), {**obligation, "source_path": str(path)})

    if delivered_recipient and not matching_delivery:
        report.add("ERROR", path, "delivery_recipient", f"no obligation addresses inbox owner {delivered_recipient}")
    if match:
        report.messages.setdefault(message_id, {**data, "source_path": str(path)})


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def receipt_rows(body: str) -> list[dict[str, str]]:
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if split_table_row(line) == RECEIPT_HEADERS:
            rows: list[dict[str, str]] = []
            for candidate in lines[index + 2 :]:
                if not candidate.strip().startswith("|"):
                    if rows:
                        break
                    continue
                cells = split_table_row(candidate)
                if len(cells) == len(RECEIPT_HEADERS):
                    rows.append(dict(zip(RECEIPT_HEADERS, cells)))
            return rows
    return []


def validate_receipt(report: Report, path: Path, data: dict[str, Any], body: str, agents: set[str]) -> None:
    validate_exact_fields(report, path, data, RECEIPT_FIELDS, "receipt")
    if data.get("schema") != "direct-receipt/v1":
        report.add("ERROR", path, "schema", "schema must be direct-receipt/v1")
    message_id = data.get("message_id")
    if not isinstance(message_id, str) or not MESSAGE_ID_RE.fullmatch(message_id):
        report.add("ERROR", path, "message_id", f"invalid receipt message_id: {message_id!r}")
    recipient = data.get("recipient")
    valid_agent(report, path, recipient, "recipient", agents)
    path_match = RECEIPT_PATH_RE.search(path.as_posix())
    if path_match and recipient != path_match.group(1).upper():
        report.add("ERROR", path, "receipt_owner", "receipt recipient does not match owning agent directory")

    obligation_ids = data.get("obligations")
    if not isinstance(obligation_ids, list) or not obligation_ids:
        report.add("ERROR", path, "obligations", "receipt obligations must be a non-empty list")
        obligation_ids = []
    for oid in obligation_ids:
        match = OBLIGATION_ID_RE.fullmatch(oid or "") if isinstance(oid, str) else None
        if not match or match.group(1) != message_id or match.group(2) != recipient:
            report.add("ERROR", path, "receipt_obligation", f"receipt does not own obligation: {oid!r}")
        elif report.obligations and oid not in report.obligations:
            report.add("WARNING", path, "unresolved_obligation", f"message obligation was not included in this validation run: {oid}")

    rows = receipt_rows(body)
    if not rows:
        report.add("ERROR", path, "receipt_events", "receipt must contain the v1 event table and at least one event")
    states: dict[str, str] = {}
    for row in rows:
        oid = row["obligation_id"]
        event = row["event"]
        if oid not in obligation_ids:
            report.add("ERROR", path, "event_obligation", f"event references unowned obligation: {oid}")
        if not parse_timestamp(row["event_at"]):
            report.add("ERROR", path, "event_at", f"invalid event timestamp for {oid}")
        if event not in EVENTS:
            report.add("ERROR", path, "event", f"invalid event for {oid}: {event}")
            continue
        if states.get(oid) in TERMINAL:
            report.add("ERROR", path, "terminal_transition", f"{oid} has an event after terminal {states[oid]}")
        if event in {"DEFERRED", "BLOCKED"} and not parse_timestamp(row["next_review_at"]):
            report.add("ERROR", path, "next_review", f"{event} requires next_review_at for {oid}")
        if event in {"REJECTED", "BLOCKED", "NO_CHANGE", "INTEGRATED"} and not nonempty(row["effect_or_reason"]):
            report.add("ERROR", path, "effect_or_reason", f"{event} requires effect_or_reason for {oid}")
        if event in {"INTEGRATED", "NO_CHANGE"} and not nonempty(row["target_path"]):
            report.add("ERROR", path, "target_path", f"{event} requires target_path for {oid}")
        if row["evidence_tier"] and row["evidence_tier"] not in EVIDENCE_TIERS:
            report.add("ERROR", path, "evidence_tier", f"invalid evidence tier for {oid}: {row['evidence_tier']}")
        states[oid] = event
    report.receipts += 1


def collect_paths(inputs: list[str]) -> list[Path]:
    paths: list[Path] = []
    for raw in inputs:
        path = Path(raw)
        if path.is_dir():
            paths.extend(sorted(path.rglob("*.md")))
        else:
            paths.append(path)
    return sorted(set(paths))


def load_agents(repo_root: Path | None, agents_file: Path | None) -> set[str]:
    agents = {"WILL", "PROME"}
    if agents_file:
        agents.update(line.strip().upper() for line in agents_file.read_text(encoding="utf-8").splitlines() if line.strip())
    roster = repo_root / "PROME/ROSTER.md" if repo_root else None
    if roster and roster.exists():
        for line in roster.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^\|\s*([A-Z][A-Z0-9_-]*)\s*\|", line)
            if match and match.group(1) != "AGENT":
                agents.add(match.group(1))
    return agents


def validate(paths: Iterable[Path], agents: set[str]) -> Report:
    report = Report()
    receipts: list[tuple[Path, dict[str, Any], str]] = []
    for path in paths:
        if not path.exists():
            report.add("ERROR", path, "missing_file", "path does not exist")
            continue
        try:
            data, body = load_front_matter(path)
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
            report.add("ERROR", path, "front_matter", str(exc))
            continue
        if data is None:
            report.add("WARNING", path, "no_front_matter", "not a v1 record; skipped")
        elif data.get("schema") == "direct-message/v1":
            validate_message(report, path, data, agents)
        elif data.get("schema") == "direct-receipt/v1":
            receipts.append((path, data, body))
        else:
            report.add("ERROR", path, "schema", f"unknown schema: {data.get('schema')!r}")
    for path, data, body in receipts:
        validate_receipt(report, path, data, body, agents)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Message/receipt Markdown files or directories")
    parser.add_argument("--repo-root", type=Path, help="Repository root used to read PROME/ROSTER.md")
    parser.add_argument("--agents-file", type=Path, help="Newline-delimited agent IDs for fixtures")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args(argv)
    report = validate(collect_paths(args.paths), load_agents(args.repo_root, args.agents_file))
    payload = {
        "messages": len(report.messages),
        "obligations": len(report.obligations),
        "receipts": report.receipts,
        "errors": report.errors,
        "warnings": report.warnings,
        "findings": [finding.__dict__ for finding in report.findings],
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for finding in report.findings:
            print(f"{finding.severity} {finding.code} {finding.path}: {finding.message}")
        print(f"validated messages={payload['messages']} obligations={payload['obligations']} receipts={payload['receipts']} errors={payload['errors']} warnings={payload['warnings']}")
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
