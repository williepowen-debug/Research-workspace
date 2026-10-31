#!/usr/bin/env python3
"""PROME's explicit receipt preparation command. Does not rule, commit, push or notify."""
import argparse
from datetime import datetime, timezone
import json
import fcntl
import os
import subprocess
import tempfile
from pathlib import Path
import uuid

from delivery import validate, published_packet
from pilot_files import RECEIPTS, RESPONSES, Repo, encoded, identifier, read_receipts, strict_json
from queue_store import REPLIES, queue_chain, check_current_snapshot, validate_reply
from store import reader


def load_event(repo, event_id):
    identifier(event_id)
    candidates = [p for prefix in (RESPONSES, REPLIES) for p in repo.git("ls-tree", "-r", "--name-only", "origin/master", "--", prefix).splitlines()
                  if p == f"{prefix}/{event_id}.json"]
    if len(candidates) != 1:
        raise ValueError("Expected one committed response with this ID")
    event = strict_json(repo.read(candidates[0], "origin/master"))
    if repo.read(candidates[0], "origin/master") != encoded(event) + "\n":
        raise ValueError("Response is not published exactly")
    validate(repo, event)
    if event["id"] != event_id:
        raise ValueError("Response filename disagrees with its identity")
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


def inspect_event(repo, event):
    """Owner intake preflight; never interprets an answer as a ruling."""
    packet = published_packet(repo, event)
    if not packet:
        raise ValueError("Published response lacks its exact inbox packet; not delivered")
    receipts = read_receipts(repo, event, commit="origin/master")
    if receipts and receipts[-1]["state"] in {"integrated", "rejected_stale", "needs_clarification"}:
        return {"status": receipts[-1]["state"], "receipt": receipts[-1], "packet": packet}
    if event["kind"] == "decisions-queue-response/1":
        wq = event["display"]["record"]["wq_id"]
        events = []
        for path in repo.git("ls-tree", "-r", "--name-only", "origin/master", "--", REPLIES).splitlines():
            try:
                other = strict_json(repo.read(path, "origin/master", prefix=REPLIES))
            except (ValueError, subprocess.CalledProcessError):
                continue  # Report this quarantined artifact on its own intake row.
            if not isinstance(other, dict):
                continue
            if other.get("display", {}).get("record", {}).get("wq_id") != wq:
                continue
            validate_reply(repo, other, wq)
            if path != f"{REPLIES}/{other['id']}.json":
                raise ValueError("Published response filename disagrees with its identity")
            events.append(other)
        ordered = queue_chain(repo, events)
        if not ordered or ordered[-1]["id"] != event["id"]:
            return {"status": "superseded", "packet": packet, "reason": "A later published answer exists"}
        for other in ordered:
            if any(r["state"] == "integrated" for r in read_receipts(repo, other, commit="origin/master")):
                raise ValueError("An answer was already recorded for this item")
        check_current_snapshot(repo, event["display"])
    else:
        # The old supervised pilot has a different source contract.
        from pilot_files import assert_current
        assert_current(repo, event["display"])
    return {"status": "received" if receipts else "ready", "packet": packet,
            "receipt": receipts[-1] if receipts else None,
            "requires_chat_confirmation": True,
            "meaning": "Mechanical checks only; PROME must interpret, confirm and record the ruling."}


def receipt_path(repo, receipt):
    return repo.path(f"{RECEIPTS}/{receipt['response_id']}/{receipt['id']}.json", RECEIPTS)


def write_received(repo, event):
    # Deterministic identity makes a retry before the owner's commit idempotent.
    receipt = prepare(repo, event, "received")
    receipt["id"] = uuid.uuid5(uuid.NAMESPACE_URL, "decisions-received/1/" + event["sha256"]).hex
    path = receipt_path(repo, receipt)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Respect a receipt prepared by PROME but not committed yet, including the
    # older explicit prepare command's random ID. Never create a parallel root.
    pending = list(path.parent.glob("*.json"))
    if pending:
        if len(pending) != 1:
            raise ValueError("Multiple local receipts need owner reconciliation before intake writes")
        prior_path = repo.path(str(pending[0].relative_to(repo.root)), RECEIPTS)
        prior = strict_json(prior_path.read_text())
        from pilot_files import timestamp
        timestamp(prior.get("at")); identifier(prior.get("id"))
        if prior_path.stem != prior["id"] or ({k: v for k, v in prior.items() if k not in {"id", "at"}} !=
                                               {k: v for k, v in receipt.items() if k not in {"id", "at"}}):
            raise ValueError("Existing local receipt conflicts; preserve it for owner reconciliation")
        return str(prior_path.relative_to(repo.root))
    if not path.exists():
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".receipt-") as out:
            out.write((encoded(receipt) + "\n").encode()); out.flush(); os.fsync(out.fileno())
            try:
                os.link(out.name, path)
            except FileExistsError:
                pass
    existing = strict_json(path.read_text())
    from pilot_files import timestamp
    timestamp(existing.get("at"))
    if {k: v for k, v in existing.items() if k != "at"} != {k: v for k, v in receipt.items() if k != "at"}:
        raise ValueError("Existing received receipt conflicts; preserve it for reconciliation")
    return str(path.relative_to(repo.root))


def intake(repo, write=False, event_id=None):
    # origin is fetched by the CLI once; report the checked revision with each run.
    revision = repo.git("rev-parse", "origin/master").strip()
    if event_id:
        identifier(event_id)
        ids = {event_id}
    else:
        ids = set()
        for prefix in (RESPONSES, REPLIES):
            ids.update(Path(path).stem for path in repo.git("ls-tree", "-r", "--name-only", revision, "--", prefix).splitlines()
                       if path.endswith(".json"))
    results = []
    for eid in sorted(ids):
        row = {"id": eid}
        try:
            event = load_event(repo, eid)
            row.update({"unit": event["request"]["unit_id"], "request": event["request"],
                        "question": event["display"]["record"], "response_sha256": event["sha256"]})
            row.update(inspect_event(repo, event))
            if write and row["status"] == "ready":
                lock = repo.path("AGENTS/CATO/prototypes/decisions/mvp/local-state/intake.lock")
                lock.parent.mkdir(parents=True, exist_ok=True)
                with lock.open("a") as stream:
                    fcntl.flock(stream, fcntl.LOCK_EX)
                    # Detect new published state / working question before writing.
                    if repo.git("rev-parse", "origin/master").strip() != revision:
                        raise ValueError("Published state changed during intake; rerun")
                    row.update(inspect_event(repo, event))
                    if row["status"] == "ready":
                        row["receipt_path"] = write_received(repo, event)
                        row["status"] = "received"
        except (ValueError, KeyError, TypeError, AttributeError, OSError, subprocess.CalledProcessError) as error:
            row.update({"status": "needs_clarification", "reason": str(error)})
        results.append(row)
    return {"checked_revision": revision, "items": results,
            "scope": "Published answers only; private drafts are not observable. Received is not ruled or implemented.",
            "requires_chat_confirmation": True}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("pending", help="Read-only published intake report; one bad item does not stop the scan")
    i = sub.add_parser("intake", help="Check delivered answers; optionally write received receipts, never rulings")
    i.add_argument("--event-id")
    i.add_argument("--write", action="store_true", help="PROME only: write received receipts; no Git commit or ruling")
    r = sub.add_parser("prepare")
    r.add_argument("event_id")
    r.add_argument("state", choices=["received", "needs_clarification", "rejected_stale", "integrated"])
    r.add_argument("--ruling-path"); r.add_argument("--ruling-commit")
    r.add_argument("--confirmation-path"); r.add_argument("--confirmation-commit")
    r.add_argument("--write", action="store_true", help="PROME only: create one immutable receipt; no Git mutation")
    args = p.parse_args(); repo = Repo(reader.ROOT)
    if args.command in {"pending", "intake"}:
        repo.git("fetch", "origin")
        print(json.dumps(intake(repo, getattr(args, "write", False), getattr(args, "event_id", None)),
                         indent=2, ensure_ascii=False))
        return
    event = load_event(repo, args.event_id)
    ruling = {"path": args.ruling_path, "commit": args.ruling_commit} if args.ruling_path else None
    confirmation = {"path": args.confirmation_path, "commit": args.confirmation_commit} if args.confirmation_path else None
    receipt = prepare(repo, event, args.state, ruling, confirmation)
    if args.write:
        path = receipt_path(repo, receipt)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x") as out:
            out.write(encoded(receipt) + "\n")
        print(path)
    else:
        print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
