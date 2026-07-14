#!/usr/bin/env python3
"""Feature-gated authoring and receipt CLI for Direct Agent Messaging v1."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

import yaml

from validate import (
    EVENTS,
    RECEIPT_HEADERS,
    Report,
    load_agents,
    load_front_matter,
    validate,
    validate_message,
)


ID_SCAN_RE = re.compile(r"^MSG-([A-Z][A-Z0-9_-]*)-(\d{8})-(\d{3})(?:__.*)?\.md$")
SAFE_SLUG_RE = re.compile(r"[^a-z0-9]+")


class MessagingError(RuntimeError):
    pass


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def parse_cli_timestamp(value: str | None, label: str) -> dt.datetime | None:
    if value is None:
        return None
    candidate = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = dt.datetime.fromisoformat(candidate)
    except ValueError as exc:
        raise MessagingError(f"{label} must be an ISO 8601 timestamp with timezone") from exc
    if parsed.tzinfo is None:
        raise MessagingError(f"{label} must include a timezone")
    return parsed


def load_config(repo_root: Path) -> dict[str, Any]:
    path = repo_root / "MESSAGING/config.yaml"
    if not path.exists():
        return {"schema": "direct-messaging-config/v1", "write_mode": "disabled", "reason": "config missing"}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema") != "direct-messaging-config/v1":
        raise MessagingError(f"invalid messaging config: {path}")
    return data


def require_write(repo_root: Path, sender: str, recipient: str) -> None:
    config = load_config(repo_root)
    mode = config.get("write_mode")
    if mode == "test":
        return
    if mode == "cohort":
        allowed_senders = set(config.get("allowed_senders") or [])
        allowed_recipients = set(config.get("allowed_recipients") or [])
        if sender in allowed_senders and recipient in allowed_recipients:
            return
        raise MessagingError(f"live cohort does not allow {sender} -> {recipient}")
    reason = config.get("reason", "live activation has not been approved")
    raise MessagingError(f"writes are locked (write_mode={mode!r}): {reason}")


def slugify(value: str) -> str:
    slug = SAFE_SLUG_RE.sub("-", value.lower()).strip("-")
    if not slug:
        raise MessagingError("subject must produce a non-empty filename slug")
    return slug[:64]


def format_timestamp(value: dt.datetime) -> str:
    return value.isoformat(timespec="seconds")


def destination_for(repo_root: Path, recipient: str, message_id: str, role: str, subject: str) -> Path:
    if recipient in {"PROME", "WILL"}:
        raise MessagingError(f"v1 destination for {recipient} is intentionally unresolved; use the current canonical path")
    agent_root = repo_root / "AGENTS" / recipient
    if not agent_root.is_dir():
        raise MessagingError(f"recipient directory does not exist: {agent_root}")
    filename = f"{message_id}__{role}__{slugify(subject)}.md"
    return agent_root / "inbox" / filename


def next_sequence(repo_root: Path, sender: str, date_key: str) -> int:
    maximum = 0
    for path in repo_root.rglob(f"MSG-{sender}-{date_key}-*.md"):
        match = ID_SCAN_RE.fullmatch(path.name)
        if match and match.group(1) == sender and match.group(2) == date_key:
            maximum = max(maximum, int(match.group(3)))
    sequence = maximum + 1
    if sequence > 999:
        raise MessagingError(f"daily sequence exhausted for {sender} on {date_key}")
    return sequence


@contextmanager
def exclusive_lock(repo_root: Path, name: str) -> Iterator[None]:
    runtime = repo_root / "MESSAGING/runtime"
    runtime.mkdir(parents=True, exist_ok=True)
    lock = runtime / f"{name}.lock"
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise MessagingError(f"ID allocator is busy: {lock}") from exc
    try:
        os.write(descriptor, f"pid={os.getpid()}\n".encode())
        os.close(descriptor)
        yield
    finally:
        lock.unlink(missing_ok=True)


def allocation_lock(repo_root: Path, sender: str, date_key: str) -> Iterator[None]:
    return exclusive_lock(repo_root, f"allocate-{sender}-{date_key}")


def receipt_lock(repo_root: Path, recipient: str, message_id: str) -> Iterator[None]:
    return exclusive_lock(repo_root, f"receipt-{recipient}-{message_id}")


def build_message_data(args: argparse.Namespace, message_id: str, created: dt.datetime) -> dict[str, Any]:
    obligation_id = f"{message_id}#{args.recipient}-01"
    due: str | None = args.due
    if args.urgency == "NEXT_BOOT" and due is None:
        due = "next_boot"
    if args.role == "INFO":
        requested_action = None
        definition_of_done = None
    else:
        requested_action = args.requested_action
        definition_of_done = args.definition_of_done
    return {
        "schema": "direct-message/v1",
        "message_id": message_id,
        "created_at": format_timestamp(created),
        "from": args.sender,
        "subject": args.subject,
        "supersedes": args.supersedes,
        "related": args.related or [],
        "obligations": [
            {
                "obligation_id": obligation_id,
                "to": args.recipient,
                "role": args.role,
                "urgency": args.urgency,
                "requested_action": requested_action,
                "definition_of_done": definition_of_done,
                "due": due,
                "receipt_required": args.role == "ACTION" or args.receipt_required,
                "expected_targets": args.expected_target or [],
            }
        ],
    }


def render_message(data: dict[str, Any], body: str | None) -> str:
    sections = [f"# {data['subject']}"]
    if body:
        sections.extend(["", body.strip()])
    if len(data["obligations"]) == 1 and data["obligations"][0]["role"] == "ACTION":
        obligation = data["obligations"][0]
        sections.extend(
            [
                "",
                "## Requested action",
                "",
                obligation["requested_action"],
                "",
                "## Definition of done",
                "",
                obligation["definition_of_done"],
            ]
        )
    elif len(data["obligations"]) == 1:
        sections.extend(["", "**No action is requested.**"])
    else:
        sections.extend(["", "## Recipient obligations"])
        for obligation in data["obligations"]:
            sections.extend(["", f"### {obligation['obligation_id']} — {obligation['role']}"])
            if obligation["role"] == "ACTION":
                sections.extend(
                    [
                        "",
                        f"**Requested action:** {obligation['requested_action']}",
                        "",
                        f"**Definition of done:** {obligation['definition_of_done']}",
                    ]
                )
            else:
                sections.extend(["", "**No action is requested from this recipient.**"])
    front = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{front}\n---\n\n" + "\n".join(sections).rstrip() + "\n"


def validate_message_data(data: dict[str, Any], agents: set[str]) -> None:
    report = Report()
    validate_message(report, Path("preview.md"), data, agents)
    if report.errors:
        details = "; ".join(f"{finding.code}: {finding.message}" for finding in report.findings if finding.severity == "ERROR")
        raise MessagingError(f"message validation failed: {details}")


def compose(args: argparse.Namespace) -> tuple[str, Path]:
    repo_root = args.repo_root.resolve()
    agents = load_agents(repo_root, None)
    if args.sender not in agents or args.recipient not in agents:
        raise MessagingError("sender and recipient must exist in PROME/ROSTER.md")
    created = parse_cli_timestamp(args.created_at, "created_at") or utc_now()
    date_key = created.astimezone(dt.timezone.utc).strftime("%Y%m%d")

    def generate() -> tuple[str, Path]:
        sequence = next_sequence(repo_root, args.sender, date_key)
        message_id = f"MSG-{args.sender}-{date_key}-{sequence:03d}"
        data = build_message_data(args, message_id, created)
        validate_message_data(data, agents)
        destination = destination_for(repo_root, args.recipient, message_id, args.role, args.subject)
        body = args.body
        if args.body_file:
            body = args.body_file.read_text(encoding="utf-8")
        return render_message(data, body), destination

    if not args.write:
        return generate()
    require_write(repo_root, args.sender, args.recipient)
    with allocation_lock(repo_root, args.sender, date_key):
        text, destination = generate()
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            with destination.open("x", encoding="utf-8") as handle:
                handle.write(text)
        except FileExistsError as exc:
            raise MessagingError(f"destination already exists: {destination}") from exc
        return text, destination


def build_batch_data(draft: dict[str, Any], message_id: str, created: dt.datetime) -> dict[str, Any]:
    raw_obligations = draft.get("obligations")
    if not isinstance(raw_obligations, list) or not raw_obligations:
        raise MessagingError("compose-file obligations must be a non-empty list")
    counters: dict[str, int] = {}
    obligations: list[dict[str, Any]] = []
    for raw in raw_obligations:
        if not isinstance(raw, dict):
            raise MessagingError("each compose-file obligation must be a mapping")
        recipient = str(raw.get("to", "")).upper()
        counters[recipient] = counters.get(recipient, 0) + 1
        role = str(raw.get("role", "")).upper()
        urgency = str(raw.get("urgency", "")).upper()
        due = raw.get("due")
        if urgency == "NEXT_BOOT" and due is None:
            due = "next_boot"
        obligations.append(
            {
                "obligation_id": f"{message_id}#{recipient}-{counters[recipient]:02d}",
                "to": recipient,
                "role": role,
                "urgency": urgency,
                "requested_action": raw.get("requested_action") if role == "ACTION" else None,
                "definition_of_done": raw.get("definition_of_done") if role == "ACTION" else None,
                "due": due,
                "receipt_required": True if role == "ACTION" else bool(raw.get("receipt_required", False)),
                "expected_targets": raw.get("expected_targets") or [],
            }
        )
    return {
        "schema": "direct-message/v1",
        "message_id": message_id,
        "created_at": format_timestamp(created),
        "from": str(draft.get("sender", "")).upper(),
        "subject": draft.get("subject"),
        "supersedes": draft.get("supersedes"),
        "related": draft.get("related") or [],
        "obligations": obligations,
    }


def batch_destinations(repo_root: Path, data: dict[str, Any]) -> list[Path]:
    recipients = sorted({item["to"] for item in data["obligations"]})
    paths: list[Path] = []
    for recipient in recipients:
        roles = {item["role"] for item in data["obligations"] if item["to"] == recipient}
        filename_role = next(iter(roles)) if len(roles) == 1 else "MIXED"
        paths.append(destination_for(repo_root, recipient, data["message_id"], filename_role, data["subject"]))
    return paths


def write_batch(paths: list[Path], text: str) -> None:
    existing = [path for path in paths if path.exists()]
    if existing:
        raise MessagingError(f"batch destination already exists: {existing[0]}")
    created: list[Path] = []
    try:
        for path in paths:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8") as handle:
                handle.write(text)
            created.append(path)
    except Exception:
        for path in created:
            path.unlink(missing_ok=True)
        raise


def compose_file(args: argparse.Namespace) -> tuple[str, list[Path]]:
    repo_root = args.repo_root.resolve()
    draft = yaml.safe_load(args.spec.read_text(encoding="utf-8"))
    if not isinstance(draft, dict):
        raise MessagingError("compose-file spec must decode to a mapping")
    sender = str(draft.get("sender", "")).upper()
    created = parse_cli_timestamp(draft.get("created_at"), "created_at") or utc_now()
    date_key = created.astimezone(dt.timezone.utc).strftime("%Y%m%d")
    agents = load_agents(repo_root, None)
    recipients = {str(item.get("to", "")).upper() for item in draft.get("obligations", []) if isinstance(item, dict)}
    if sender not in agents or not recipients or not recipients.issubset(agents):
        raise MessagingError("compose-file sender and recipients must exist in PROME/ROSTER.md")

    def generate() -> tuple[str, list[Path]]:
        sequence = next_sequence(repo_root, sender, date_key)
        message_id = f"MSG-{sender}-{date_key}-{sequence:03d}"
        data = build_batch_data(draft, message_id, created)
        validate_message_data(data, agents)
        return render_message(data, draft.get("body")), batch_destinations(repo_root, data)

    if not args.write:
        return generate()
    for recipient in recipients:
        require_write(repo_root, sender, recipient)
    with allocation_lock(repo_root, sender, date_key):
        text, destinations = generate()
        write_batch(destinations, text)
        return text, destinations


def escape_table(value: str | None) -> str:
    return (value or "").replace("|", "¦").replace("\n", " ").strip()


def receipt_path(repo_root: Path, recipient: str, message_id: str) -> Path:
    return repo_root / "AGENTS" / recipient / "messages" / "receipts" / f"{message_id}__{recipient}.md"


def initial_receipt(message_id: str, recipient: str, obligation_ids: list[str]) -> str:
    data = {
        "schema": "direct-receipt/v1",
        "message_id": message_id,
        "recipient": recipient,
        "obligations": obligation_ids,
    }
    front = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).strip()
    header = "| " + " | ".join(RECEIPT_HEADERS) + " |"
    divider = "|" + "|".join("---" for _ in RECEIPT_HEADERS) + "|"
    return f"---\n{front}\n---\n\n# Receipt — {message_id} — {recipient}\n\n{header}\n{divider}\n"


def event_row(args: argparse.Namespace, event_at: dt.datetime) -> str:
    values = [
        format_timestamp(event_at),
        args.obligation_id,
        args.event,
        args.next_review_at or "",
        args.target_path or "",
        args.effect_or_reason or "",
        args.commit or "",
        args.evidence_tier or "",
    ]
    return "| " + " | ".join(escape_table(value) for value in values) + " |"


def validate_candidate(message_path: Path, receipt_path_value: Path, text: str, repo_root: Path) -> None:
    receipt_path_value.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp_name = tempfile.mkstemp(prefix=".receipt-", suffix=".md", dir=receipt_path_value.parent)
    os.close(descriptor)
    temp = Path(temp_name)
    try:
        temp.write_text(text, encoding="utf-8")
        report = validate([message_path, temp], load_agents(repo_root, None))
        if report.errors:
            details = "; ".join(f"{finding.code}: {finding.message}" for finding in report.findings if finding.severity == "ERROR")
            raise MessagingError(f"receipt validation failed: {details}")
    finally:
        temp.unlink(missing_ok=True)


def record_receipt(args: argparse.Namespace) -> tuple[str, Path, bool]:
    repo_root = args.repo_root.resolve()
    message_path = args.message.resolve()
    try:
        relative_message = message_path.relative_to(repo_root)
    except ValueError as exc:
        raise MessagingError("--message must be inside --repo-root") from exc
    expected_inbox = Path("AGENTS") / args.recipient / "inbox"
    if not relative_message.is_relative_to(expected_inbox):
        raise MessagingError(f"--message must be delivered under {expected_inbox}")
    data, _ = load_front_matter(message_path)
    if not data or data.get("schema") != "direct-message/v1":
        raise MessagingError("--message must be a Direct Messaging v1 file")
    require_write(repo_root, data.get("from", ""), args.recipient)
    matching = [item for item in data["obligations"] if item.get("to") == args.recipient]
    if not matching:
        raise MessagingError(f"{args.recipient} owns no obligation in {data['message_id']}")
    obligation_ids = [item["obligation_id"] for item in matching]
    if args.obligation_id not in obligation_ids:
        raise MessagingError(f"receipt cannot disposition another recipient's obligation: {args.obligation_id}")
    if args.event not in EVENTS:
        raise MessagingError(f"unsupported event: {args.event}")
    event_at = parse_cli_timestamp(args.event_at, "event_at") or utc_now()
    if args.next_review_at:
        parse_cli_timestamp(args.next_review_at, "next_review_at")
    target = receipt_path(repo_root, args.recipient, data["message_id"])
    with receipt_lock(repo_root, args.recipient, data["message_id"]):
        existing = target.read_text(encoding="utf-8") if target.exists() else initial_receipt(data["message_id"], args.recipient, obligation_ids)
        row = event_row(args, event_at)
        if row in existing.splitlines():
            return existing, target, False
        candidate = existing.rstrip() + "\n" + row + "\n"
        validate_candidate(message_path, target, candidate, repo_root)
        descriptor, temp_name = tempfile.mkstemp(prefix=".receipt-write-", suffix=".md", dir=target.parent)
        os.close(descriptor)
        temp = Path(temp_name)
        try:
            temp.write_text(candidate, encoding="utf-8")
            os.replace(temp, target)
        finally:
            temp.unlink(missing_ok=True)
        return candidate, target, True


def add_common_repo(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)

    compose_parser = commands.add_parser("compose", help="Preview or test-write one direct message")
    add_common_repo(compose_parser)
    compose_parser.add_argument("--sender", required=True, type=str.upper)
    compose_parser.add_argument("--recipient", required=True, type=str.upper)
    compose_parser.add_argument("--role", required=True, choices=["ACTION", "INFO"])
    compose_parser.add_argument("--urgency", required=True, choices=["URGENT", "NEXT_BOOT", "SCHEDULED", "ROUTINE"])
    compose_parser.add_argument("--subject", required=True)
    compose_parser.add_argument("--requested-action")
    compose_parser.add_argument("--definition-of-done")
    compose_parser.add_argument("--due")
    compose_parser.add_argument("--receipt-required", action="store_true")
    compose_parser.add_argument("--expected-target", action="append")
    compose_parser.add_argument("--related", action="append")
    compose_parser.add_argument("--supersedes")
    compose_parser.add_argument("--created-at")
    compose_parser.add_argument("--body")
    compose_parser.add_argument("--body-file", type=Path)
    compose_parser.add_argument("--write", action="store_true", help="Requires test mode or an allowed live-cohort route")

    file_parser = commands.add_parser("compose-file", help="Preview or write a multi-obligation YAML draft")
    add_common_repo(file_parser)
    file_parser.add_argument("--spec", required=True, type=Path)
    file_parser.add_argument("--write", action="store_true", help="Requires test mode or allowed routes for every recipient")

    receipt_parser = commands.add_parser("receipt", help="Append one recipient-owned event in test mode")
    add_common_repo(receipt_parser)
    receipt_parser.add_argument("--message", required=True, type=Path)
    receipt_parser.add_argument("--recipient", required=True, type=str.upper)
    receipt_parser.add_argument("--obligation-id", required=True)
    receipt_parser.add_argument("--event", required=True, choices=sorted(EVENTS))
    receipt_parser.add_argument("--event-at")
    receipt_parser.add_argument("--next-review-at")
    receipt_parser.add_argument("--target-path")
    receipt_parser.add_argument("--effect-or-reason")
    receipt_parser.add_argument("--commit")
    receipt_parser.add_argument("--evidence-tier", choices=["ASSERTED", "POINTED", "CORROBORATED", "COMMIT_LINKED"])
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "compose":
            text, destination = compose(args)
            print(f"destination: {destination}")
            print("mode: TEST-WRITE" if args.write else "mode: PREVIEW")
            print(text)
        elif args.command == "compose-file":
            text, destinations = compose_file(args)
            for destination in destinations:
                print(f"destination: {destination}")
            print("mode: COHORT/TEST-WRITE" if args.write else "mode: PREVIEW")
            print(text)
        elif args.command == "receipt":
            _, target, changed = record_receipt(args)
            print(f"receipt: {target}")
            print("result: appended" if changed else "result: idempotent-noop")
        return 0
    except (MessagingError, OSError, yaml.YAMLError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
