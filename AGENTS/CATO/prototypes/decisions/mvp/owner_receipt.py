#!/usr/bin/env python3
"""PROME's explicit receipt preparation command. Does not rule, commit, push or notify."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import uuid

from delivery import validate
from pilot_files import RECEIPTS, RESPONSES, Repo, encoded, identifier, read_receipts, strict_json
from queue_store import REPLIES
from store import reader


def load_event(repo, event_id):
    identifier(event_id)
    candidates = [p for prefix in (RESPONSES, REPLIES) for p in repo.files(prefix)
                  if p == f"{prefix}/{event_id}.json"]
    if len(candidates) != 1:
        raise ValueError("Expected one committed response with this ID")
    event = strict_json(repo.read(candidates[0], clean=True))
    if repo.read(candidates[0], "origin/master") != encoded(event) + "\n":
        raise ValueError("Response is not published exactly")
    validate(repo, event)
    return event


def prepare(repo, event, state, ruling=None, confirmation=None):
    validate(repo, event)
    old = read_receipts(repo, event)
    if old and (old[-1]["state"] != "received" or state == "received"):
        raise ValueError("Receipt already terminal or duplicate received state; preserve history")
    if state not in {"received", "needs_clarification", "rejected_stale", "integrated"}:
        raise ValueError("Unsupported receipt state")
    if state == "integrated":
        for ref in (ruling, confirmation):
            if not isinstance(ref, dict) or set(ref) != {"path", "commit"}:
                raise ValueError("Integration requires published ruling and matching-confirmation references")
            repo.git("merge-base", "--is-ancestor", ref["commit"], "origin/master")
            repo.read(ref["path"], ref["commit"], prefix="PROME/proposals")
        if not ruling["path"].endswith("-RULED.md"):
            raise ValueError("Ruling reference must name a -RULED.md record")
    elif ruling or confirmation:
        raise ValueError("Only integration carries ruling/confirmation references")
    return {"schema_version": "decisions-receipt/1", "id": uuid.uuid4().hex,
            "response_id": event["id"], "response_sha256": event["sha256"], "state": state,
            "at": datetime.now(timezone.utc).isoformat(), "previous_receipt_id": old[-1]["id"] if old else None,
            "canonical_ruling": ruling, "chat_confirmation": confirmation,
            "confirmed_response_sha256": event["sha256"] if state == "integrated" else None}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("pending")
    r = sub.add_parser("prepare")
    r.add_argument("event_id")
    r.add_argument("state", choices=["received", "needs_clarification", "rejected_stale", "integrated"])
    r.add_argument("--ruling-path"); r.add_argument("--ruling-commit")
    r.add_argument("--confirmation-path"); r.add_argument("--confirmation-commit")
    r.add_argument("--write", action="store_true", help="PROME only: create one immutable receipt; no Git mutation")
    args = p.parse_args(); repo = Repo(reader.ROOT)
    if args.command == "pending":
        result = []
        for prefix in (RESPONSES, REPLIES):
            for path in repo.files(prefix):
                event = load_event(repo, Path(path).stem)
                receipts = read_receipts(repo, event)
                if not receipts or receipts[-1]["state"] == "received":
                    result.append({"id": event["id"], "unit": event["request"]["unit_id"],
                                   "request": event["request"], "state": receipts[-1]["state"] if receipts else "unacknowledged"})
        print(json.dumps(result, indent=2, ensure_ascii=False)); return
    event = load_event(repo, args.event_id)
    ruling = {"path": args.ruling_path, "commit": args.ruling_commit} if args.ruling_path else None
    confirmation = {"path": args.confirmation_path, "commit": args.confirmation_commit} if args.confirmation_path else None
    receipt = prepare(repo, event, args.state, ruling, confirmation)
    if args.write:
        path = repo.path(f"{RECEIPTS}/{event['id']}/{receipt['id']}.json", RECEIPTS)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x") as out:
            out.write(encoded(receipt) + "\n")
        print(path)
    else:
        print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
