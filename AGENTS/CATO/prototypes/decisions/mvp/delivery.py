"""User-requested exact-file transport. Never writes a ruling or rebases a dirty checkout."""
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import re
import subprocess

from pilot_files import RESPONSES, encoded, identifier, validate_event
from queue_store import REPLIES, validate_reply


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


def deliver(repo, event, guard=None):
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
        if repo.path(processed).exists():
            packet = processed
        target = repo.path(packet, "PROME/inbox")
        if target.exists():
            if target.read_text() != text:
                raise ValueError("Existing delivery packet differs; owner reconciliation required")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("x") as out:
                out.write(text)
        paths = [path, packet]
        def exact_working_files():
            if repo.git("branch", "--show-current").strip() != "master":
                raise ValueError("Checkout changed during delivery")
            for name, expected in ((path, payload), (packet, text)):
                if repo.path(name).read_text() != expected:
                    raise ValueError("Delivery file changed during Send; preserved for reconciliation")
            if guard:
                guard()
        checks = ["PROME/DOCKET.tsv", "PROME/GATES.tsv", "PROME/WILL_QUEUE.md", packet]
        for name in checks:
            with repo.path(name).open("rb") as stream:
                stream.read(1)
        subprocess.run(["python3", "scripts/claim_check.py", "--check", "weekday", *checks],
                       cwd=repo.root, check=True, capture_output=True, text=True, timeout=30)
        subprocess.run(["bash", "scripts/orphan_check.sh", "CATO"], cwd=repo.root,
                       check=True, capture_output=True, text=True, timeout=30)
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
        return {"message": "Delivered to PROME's inbox. Awaiting its receipt and matching chat confirmation.",
                "commit": commit, "packet": packet,
                "receipt": output.stdout[-2500:]}
