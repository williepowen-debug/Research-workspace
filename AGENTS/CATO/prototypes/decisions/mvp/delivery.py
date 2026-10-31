"""User-requested exact-file transport. Never writes a ruling or rebases a dirty checkout."""
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import re
import subprocess
import tempfile

from pilot_files import RESPONSES, encoded, identifier, read_receipts, strict_json, validate_event
from queue_store import REPLIES, check_current_snapshot, queue_chain, validate_reply


def event_path(event):
    prefix = REPLIES if event["kind"] == "decisions-queue-response/1" else RESPONSES
    return f"{prefix}/{identifier(event['id'])}.json"


def delivery_state(repo, event):
    path = event_path(event)
    payload = encoded(event) + "\n"
    for ref, label in [("origin/master", "delivered"), ("HEAD", "committed")]:
        try:
            if repo.read(path, ref) == payload:
                return label
        except (ValueError, subprocess.CalledProcessError):
            pass
    return "saved"


def validate(repo, event):
    if event["kind"] == "decisions-queue-response/1":
        validate_reply(repo, event, event["display"]["record"]["wq_id"])
    else:
        validate_event(repo, event, event["display"]["record"]["wq_id"], event["request"]["unit_id"],
                       event["display"]["source_path"])


def locked(repo):
    if repo.git("branch", "--show-current").strip() != "master":
        raise ValueError("Decisions transport requires the shared master checkout")
    path = repo.path("AGENTS/CATO/prototypes/decisions/mvp/local-state/transport.lock")
    path.parent.mkdir(parents=True, exist_ok=True)
    stream = path.open("a")
    try:
        fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        stream.close()
        raise ValueError("Another Decisions window is synchronizing; try again shortly")
    return stream


def sync(repo):
    with locked(repo):
        repo.git("fetch", "origin")
        ahead, behind = map(int, repo.git("rev-list", "--left-right", "--count", "HEAD...origin/master").split())
        message = "Up to date."
        if behind:
            if ahead or repo.git("status", "--porcelain", "--untracked-files=no").strip():
                message = "Remote updates fetched. Local work must be reconciled before they can be applied."
            else:
                repo.git("pull", "--rebase")
                message = "Latest records loaded."
        return {"message": message, "fetched_at": datetime.now(timezone.utc).isoformat(),
                "origin": repo.git("rev-parse", "origin/master").strip()}


def check_queue_delivery(repo, event, local_events=None):
    if event["kind"] != "decisions-queue-response/1":
        return
    wq = event["display"]["record"]["wq_id"]
    events = {event["id"]: event}
    # Read anew at every guard; another app window can save a newer revision
    # while the advisory checks run. Local versions remain local-only files.
    for saved in local_events() if local_events else ():
        if saved.get("display", {}).get("record", {}).get("wq_id") != wq:
            raise ValueError("Local history names another queue item")
        validate_reply(repo, saved, wq)
        if saved["id"] in events and events[saved["id"]] != saved:
            raise ValueError("Conflicting immutable response; delivery refused")
        events[saved["id"]] = saved
    for ref in ("HEAD", "origin/master"):
        for path in repo.git("ls-tree", "-r", "--name-only", ref, "--", REPLIES).splitlines():
            saved = strict_json(repo.read(path, ref, prefix=REPLIES))
            if saved.get("display", {}).get("record", {}).get("wq_id") != wq:
                continue
            validate_reply(repo, saved, wq)
            if saved["id"] in events and events[saved["id"]] != saved:
                raise ValueError("Conflicting immutable response; delivery refused")
            events[saved["id"]] = saved
    for saved in events.values():
        for ref in ("HEAD", "origin/master"):
            if any(r["state"] == "integrated" for r in read_receipts(repo, saved, commit=ref)):
                raise ValueError("PROME already recorded an answer to this item; no further answer can be delivered")
    ordered = queue_chain(repo, list(events.values()))
    if ordered[-1]["id"] != event["id"]:
        raise ValueError("Only the latest saved response can be delivered; review its replacement")
    check_current_snapshot(repo, event["display"])


def run_advisory(repo, command, label):
    try:
        result = subprocess.run(command, cwd=repo.root, capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError) as error:
        raise ValueError(f"Response saved; not delivered: {label} could not run ({type(error).__name__})") from error
    if result.returncode not in ({0, 1} if label == "Weekday check" else {0}):
        raise ValueError(f"Response saved; not delivered: {label} failed (exit {result.returncode}). "
                         + (result.stdout + result.stderr)[-1800:])
    return {"check": label, "exit": result.returncode, "output": result.stdout + result.stderr}


def deliver(repo, event, guard=None, local_events=None):
    """Explicit button only, after acceptance. Exact immutable response plus one inbox pointer."""
    validate(repo, event)
    path = event_path(event)
    payload = encoded(event) + "\n"
    if repo.path(path).read_text() != payload:
        raise ValueError("Export changed or is absent; response was not delivered")
    eid = identifier(event["id"])
    # Stable filename makes an unchanged retry idempotent.
    packet = f"PROME/inbox/decisions-{eid}-from-CATO.md"
    processed = f"PROME/inbox/processed/decisions-{eid}-from-CATO.md"
    text = (f"# CATO → PROME: Decisions response {eid}\n\n"
            f"Response: `{path}`\n\nEvent SHA256: `{event['sha256']}`\n\n"
            f"Unit: `{event['request']['unit_id']}`; saved {event['saved_at']}.\n\n"
            "ACTION: read the exact immutable event and displayed terms, verify the matching operator confirmation "
            "under the adopted trust rule, and write your own receipt/ruling. This packet is transport, not that "
            "confirmation. Preserve conditions verbatim. A task report is not evidence that an owner verified completion. "
            "Never infer completion from a receipt. The app does not change the queue or launch an agent.\n")
    with locked(repo):
        if guard:
            guard()
        try:
            repo.git("fetch", "origin")
        except subprocess.CalledProcessError as error:
            raise ValueError("Response saved; not delivered: latest published terms could not be fetched") from error
        check_queue_delivery(repo, event, local_events)
        if repo.path(processed).exists():
            packet = processed
        target = repo.path(packet, "PROME/inbox")
        if target.exists():
            if target.read_text() != text:
                raise ValueError("Existing delivery packet differs; owner reconciliation required")
        paths = [path, packet]
        def exact_working_files():
            if repo.git("branch", "--show-current").strip() != "master":
                raise ValueError("Checkout changed during delivery")
            for name, expected in ((path, payload), (packet, text)):
                if repo.path(name).read_text() != expected:
                    raise ValueError("Delivery file changed during Send; preserved for reconciliation")
            if guard:
                guard()
            check_queue_delivery(repo, event, local_events)
        checks = ["PROME/DOCKET.tsv", "PROME/GATES.tsv", "PROME/WILL_QUEUE.md"]
        for name in checks:
            with repo.path(name).open("rb") as stream:
                stream.read(1)
        # Check the exact candidate before creating an inbox artifact. rc 1 is
        # advisory; rc 2 or failure to execute is unassessed, never a pass.
        with tempfile.TemporaryDirectory(prefix="decisions-packet-") as temp:
            candidate = Path(temp) / Path(packet).name
            candidate.write_text(text)
            results = [run_advisory(repo, ["python3", "scripts/claim_check.py", "--check", "weekday",
                                          *checks, str(candidate)], "Weekday check"),
                       run_advisory(repo, ["bash", "scripts/orphan_check.sh", "CATO"], "Orphan advisory")]
        check_queue_delivery(repo, event, local_events)
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("x") as out:
                out.write(text)
        # A pathspec commit preserves unrelated staged work. No directory staging.
        exact_working_files()
        repo.git("add", "--", *paths)
        changed = repo.git("diff", "--cached", "--name-only", "--", *paths).strip()
        if changed:
            repo.git("commit", "-m", f"CATO -> PROME: deliver Decisions response {eid[:12]}",
                     "-m", "Implemented-by: CATO", "--", *paths)
        commit = repo.git("rev-parse", "HEAD").strip()
        exact_working_files()
        if repo.read(path, commit) != payload or repo.read(packet, commit) != text:
            raise ValueError("Committed delivery differs; publication stopped for reconciliation")
        output = subprocess.run(["bash", "scripts/safe-push.sh"], cwd=repo.root,
                                capture_output=True, text=True, timeout=120)
        if output.returncode:
            raise ValueError("Saved and committed locally; publication not confirmed. CATO must reconcile Git. "
                             + (output.stderr + output.stdout)[-1800:])
        repo.git("fetch", "origin")
        repo.git("merge-base", "--is-ancestor", commit, "origin/master")
        if repo.read(path, "origin/master") != payload or repo.read(packet, "origin/master") != text:
            raise ValueError("Published response does not match; delivery unconfirmed")
        advice = "\n\n".join(r["check"] + ":\n" + r["output"] for r in results if r["exit"] == 1)
        return {"message": "Delivered to PROME's inbox. Awaiting its receipt and matching chat confirmation."
                           + ("\nAdvisory findings (delivery completed):\n" + advice if advice else ""),
                "commit": commit, "packet": packet,
                "checks": results,
                "receipt": output.stdout[-2500:]}
