"""User-requested exact-file transport. Never writes a ruling or rebases a dirty checkout."""
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

from pilot_files import RESPONSES, encoded, identifier, read_receipts, strict_json, validate_event
from queue_store import REPLIES, check_current_snapshot, queue_chain, validate_reply


def event_path(event):
    prefix = REPLIES if event["kind"] == "decisions-queue-response/1" else RESPONSES
    return f"{prefix}/{identifier(event['id'])}.json"


def packet_text(event):
    path = event_path(event)
    eid = identifier(event["id"])
    if 'confirmation' in (event['display'].get('options_source') or {}):
        from authorization import needs_chat
        policy = 'Matching chat confirmation is required.' if needs_chat(event['display']) else 'App-only eligible, subject to PROME reviewing conditions and any chat conflict.'
        return (f"# CATO → PROME: Decisions response {eid}\n\n"
                f"Response: `{path}`\n\nEvent SHA256: `{event['sha256']}`\n\n"
                f"Unit: `{event['request']['unit_id']}`; saved {event['saved_at']}.\n\n"
                f"ACTION: read the exact immutable event and displayed terms. {policy} "
                "Preserve conditions verbatim. Read each ruling back to Will the same day; conflicting answers await clarification. "
                "Write your own receipt/ruling through owner_receipt.py. Notification is not a read receipt or ruling. "
                "The app does not execute decisions or launch an agent.\n")
    return (f"# CATO → PROME: Decisions response {eid}\n\n"
            f"Response: `{path}`\n\nEvent SHA256: `{event['sha256']}`\n\n"
            f"Unit: `{event['request']['unit_id']}`; saved {event['saved_at']}.\n\n"
            "ACTION: read the exact immutable event and displayed terms, verify the matching operator confirmation "
            "under the adopted trust rule, and write your own receipt/ruling. This packet is transport, not that "
            "confirmation. Preserve conditions verbatim. A task report is not evidence that an owner verified completion. "
            "Never infer completion from a receipt. The app does not change the queue or launch an agent.\n")


def published_packet(repo, event, ref="origin/master"):
    expected = packet_text(event)
    for directory in ("PROME/inbox", "PROME/inbox/processed"):
        path = f"{directory}/decisions-{event['id']}-from-CATO.md"
        try:
            if repo.read(path, ref, prefix="PROME/inbox") == expected:
                return path
        except (ValueError, subprocess.CalledProcessError):
            pass
    return None


def delivery_state(repo, event):
    path = event_path(event)
    payload = encoded(event) + "\n"
    for ref, label in [("origin/master", "delivered"), ("HEAD", "committed")]:
        try:
            if repo.read(path, ref) == payload:
                return label if published_packet(repo, event, ref) else "published without inbox packet" if ref == "origin/master" else "committed without inbox packet"
        except (ValueError, subprocess.CalledProcessError):
            pass
    if published_packet(repo, event):
        return "published without response"
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
        result = subprocess.run(command, cwd=repo.root, capture_output=True, text=True, timeout=30,
                                env=publication_environment())
    except (OSError, subprocess.SubprocessError) as error:
        raise ValueError(f"Response saved; not delivered: {label} could not run ({type(error).__name__})") from error
    if result.returncode not in ({0, 1} if label == "Weekday check" else {0}):
        raise ValueError(f"Response saved; not delivered: {label} failed (exit {result.returncode}). "
                         + (result.stdout + result.stderr)[-1800:])
    return {"check": label, "exit": result.returncode, "output": result.stdout + result.stderr}


def ancestor(repo, older, newer):
    result = subprocess.run(["git", "--no-replace-objects", "merge-base", "--is-ancestor", older, newer],
                            cwd=repo.root, capture_output=True)
    if result.returncode not in (0, 1):
        raise ValueError("Git ancestry could not be checked")
    return result.returncode == 0


def delivery_base(repo):
    head = repo.git("rev-parse", "HEAD").strip()
    remote = repo.git("rev-parse", "origin/master").strip()
    if ancestor(repo, head, remote):
        return remote
    if ancestor(repo, remote, head):
        return head
    raise ValueError("Response saved; checkout histories diverge. Reconcile Git before Send; no reply committed.")


PINNED_HOOKS = {"commit-msg", "pre-commit", "pre-push"}
TRANSPORT_FILES = ("scripts/safe-push.sh", "scripts/install-git-hooks.sh", "scripts/account_guard.py",
                   "scripts/claim_check.py", "scripts/orphan_check.sh",
                   *("scripts/githooks/" + name for name in sorted(PINNED_HOOKS)))


def check_transport_files(repo):
    """Refuse unreviewed executable hooks before any hook-capable command."""
    folder = repo.path("scripts/githooks")
    if folder.exists():
        for path in folder.iterdir():
            if path.is_symlink() or (path.name not in PINNED_HOOKS and os.access(path, os.X_OK)):
                raise ValueError("Unreviewed publication hook refused: " + path.name)
    for name in TRANSPORT_FILES:
        target = repo.path(name)
        if not target.is_file() or target.read_bytes() != repo.read(name).encode("utf-8"):
            raise ValueError("Publication safeguard has uncommitted or missing changes: " + name)


def publication_environment():
    # Isolate Python's module search, including stdin Python in inherited hooks.
    env = os.environ.copy()
    for key in list(env):
        if key in {"PYTHONPATH", "PYTHONHOME", "PYTHONUSERBASE", "PYTHONSTARTUP", "GIT_CONFIG_PARAMETERS"} or key.startswith("GIT_CONFIG_KEY_") or key.startswith("GIT_CONFIG_VALUE_"):
            env.pop(key)
    env.update(PYTHONSAFEPATH="1", PYTHONNOUSERSITE="1", PYTHONDONTWRITEBYTECODE="1",
               GIT_NO_REPLACE_OBJECTS="1", GIT_CONFIG_COUNT="1",
               GIT_CONFIG_KEY_0="push.followTags", GIT_CONFIG_VALUE_0="false")
    return env


def remote_refs(repo):
    # One captured response per observation; no second lookup used to explain the first.
    result = {}
    for line in repo.git("ls-remote", "--refs", "origin").splitlines():
        sha, name = line.split("\t")
        if not re.fullmatch(r"[0-9a-f]{40}", sha) or not name.startswith("refs/") or name in result:
            raise ValueError("Remote reference inventory is ambiguous; publication cannot be verified")
        result[name] = sha
    if "refs/heads/master" not in result:
        raise ValueError("Remote master is unavailable; publication cannot be verified")
    return result


def shared_state(repo):
    return (repo.git("rev-parse", "HEAD").strip(), repo.git("write-tree").strip())


def check_private_checkout(work):
    if work.git("for-each-ref", "--format=%(refname)", "refs/replace/", "refs/tags/").strip():
        raise ValueError("Private publication contains replacement refs or tags; refused")
    allowed = set(TRANSPORT_FILES)
    for target in work.path("scripts").rglob("*"):
        name = target.relative_to(work.root).as_posix()
        if target.is_symlink() or (target.is_file() and name not in allowed):
            raise ValueError("Unpinned file in private publication scripts: " + name)
    check_transport_files(work)


def exact_pair_commit(work, base, commit, expected, check_worktree=True):
    """Verify real objects, never replace-ref views; shared post-fetch reads need no worktree files."""
    if work.git("rev-list", "--count", base + ".." + commit).strip() != "1":
        raise ValueError("Publication is not exactly one response commit; refused")
    if work.git("show", "-s", "--format=%P", commit).strip() != base:
        raise ValueError("Publication has unexpected ancestry; refused")
    changed = set(work.git("diff-tree", "--no-commit-id", "--name-only", "-r", "-z", commit).rstrip("\0").split("\0"))
    if changed != set(expected):
        raise ValueError("Publication must change exactly the two selected response/packet paths; refused")
    for name, content in expected.items():
        if work.read(name, commit) != content or (check_worktree and work.path(name).read_text() != content):
            raise ValueError("Publication artifacts changed; refused")


def publication_checkout(repo, directory, base, paths):
    # No shared index or branch writes. Failed commits die with this private clone.
    subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", "--no-tags", "--single-branch", "--template=", str(repo.root), str(directory)],
                   check=True, capture_output=True, env=publication_environment())
    work = type(repo)(directory)
    work.git_environment = publication_environment()
    work.git("config", "core.hooksPath", "/dev/null")
    # Only materialize the hook/push programs, repository marker and selected pair.
    # Git's complete tree/index still preserves every other committed path.
    work.git("sparse-checkout", "set", "--no-cone", *("/" + name for name in TRANSPORT_FILES), "/PROME/ROSTER.md",
             "/AGENTS/CATO/decisions/.gitignore", *("/" + name for name in paths))
    work.git("checkout", "-q", "-B", "master", base)
    def remote_url(push=False):
        args = ("remote", "get-url", "--push", "origin") if push else ("remote", "get-url", "origin")
        value = repo.git(*args).strip()
        if ":" not in value and not Path(value).is_absolute():
            value = str((repo.root / value).resolve())
        return value
    work.git("remote", "set-url", "origin", remote_url())
    work.git("remote", "set-url", "--push", "origin", remote_url(True))
    for key in ("user.name", "user.email"):
        work.git("config", key, repo.git("config", "--get", key).strip())
    # Validate the base's hook directory before enabling it or fetching with it.
    for row in work.git("ls-tree", "-r", "HEAD", "--", "scripts/githooks").splitlines():
        meta, name = row.split("\t", 1)
        if meta.split()[0] == "120000" or (meta.split()[0] == "100755" and name not in TRANSPORT_FILES):
            raise ValueError("Unreviewed publication hook refused: " + name)
    check_private_checkout(work)
    for name in TRANSPORT_FILES:
        if repo.path(name).read_bytes() != work.path(name).read_bytes():
            raise ValueError("Publication safeguard has uncommitted or newer changes: " + name)
    work.git("config", "core.hooksPath", "scripts/githooks")
    work.git("fetch", "origin")
    return work


def refresh_after_publication(repo):
    # Never stash, reset, rebase foreign work, or move a busy shared checkout.
    dirty = bool(repo.git("status", "--porcelain", "--untracked-files=no").strip())
    ahead, behind = map(int, repo.git("rev-list", "--left-right", "--count", "HEAD...origin/master").split())
    if not ahead and not behind:
        return " Shared checkout is up to date."
    if not dirty and not ahead:
        try:
            repo.git("merge", "--ff-only", "--no-overwrite-ignore", "origin/master")
            return " Shared checkout fast-forwarded to the published records."
        except subprocess.CalledProcessError:
            pass
    head = repo.git("rev-parse", "--short", "HEAD").strip()
    remote = repo.git("rev-parse", "--short", "origin/master").strip()
    ahead, behind = map(int, repo.git("rev-list", "--left-right", "--count", "HEAD...origin/master").split())
    next_step = ("After owners save their work, use the root Git recovery procedure for the diverged histories."
                 if ahead and behind else "After owners save their work, use Sync to load the published records.")
    return (f" Shared checkout preserved: {head}, {ahead} ahead / {behind} behind origin/master {remote}; "
            f"tracked work {'is' if dirty else 'is not'} pending. Other desks' pushes may wait for synchronization. " + next_step)


def deliver(repo, event, guard=None, local_events=None):
    """Explicit Send: create and push the exact pair in a disposable checkout."""
    validate(repo, event)
    path = event_path(event)
    payload = encoded(event) + "\n"
    eid = identifier(event["id"])
    packet = f"PROME/inbox/decisions-{eid}-from-CATO.md"
    text = packet_text(event)
    with locked(repo):
        def recheck():
            if guard:
                guard()
            check_transport_files(repo)
            check_queue_delivery(repo, event, local_events)
        recheck()
        try:
            repo.git("fetch", "origin")
        except subprocess.CalledProcessError as error:
            raise ValueError("Response saved; latest published terms could not be fetched. No reply committed.") from error
        recheck()
        if delivery_state(repo, event) == "delivered":
            return {"message": "Already delivered to PROME; awaiting its read and the applicable confirmation.",
                    "commit": repo.git("rev-parse", "origin/master").strip(),
                    "packet": published_packet(repo, event), "checks": [], "receipt": "Exact published pair verified."}
        if delivery_state(repo, event).startswith("published without"):
            raise ValueError("Incomplete earlier publication. Save a new response version before Send; the original words are preserved.")
        checks = ["PROME/DOCKET.tsv", "PROME/GATES.tsv", "PROME/WILL_QUEUE.md"]
        for name in checks:
            with repo.path(name).open("rb") as stream:
                stream.read(1)
        before_advisories = shared_state(repo)
        base = delivery_base(repo)
        refs_before = remote_refs(repo)
        if refs_before["refs/heads/master"] != repo.git("rev-parse", "origin/master").strip():
            raise ValueError("Remote changed before preparation; Sync and retry. No reply committed.")
        riders = repo.git("log", "--format=%h %s", refs_before["refs/heads/master"] + ".." + base).splitlines()
        with tempfile.TemporaryDirectory(prefix="decisions-send-") as temp:
            candidate = Path(temp) / Path(packet).name
            candidate.write_text(text)
            results = [run_advisory(repo, ["python3", "-I", "scripts/claim_check.py", "--check", "weekday",
                                           *checks, str(candidate)], "Weekday check"),
                       run_advisory(repo, ["bash", "scripts/orphan_check.sh", "CATO"], "Orphan advisory")]
            if shared_state(repo) != before_advisories:
                raise ValueError("Shared HEAD or index changed during advisory checks. Owner work preserved; retry after reconciliation. No reply committed.")
            recheck()
            legacy = repo.git("diff", "--name-only", "origin/master", base, "--", REPLIES, RESPONSES, "PROME/inbox").splitlines()
            if any(n.startswith((REPLIES + "/", RESPONSES + "/")) or re.search(r"/decisions-[0-9a-f]{32}-from-CATO\.md$", n) for n in legacy):
                raise ValueError("An earlier unpublished reply commit needs owner reconciliation; Send will not publish it implicitly")
            work = publication_checkout(repo, Path(temp) / "repo", base, [path, packet])
            if not ancestor(work, "origin/master", "HEAD"):
                raise ValueError("Response saved; origin changed during preparation. Sync and retry. No shared reply commit.")
            for name, expected in ((path, payload), (packet, text)):
                target = work.path(name)
                if target.exists() and target.read_text() != expected:
                    raise ValueError("Existing delivery artifact differs; reconcile " + name)
                target.parent.mkdir(parents=True, exist_ok=True)
                if not target.exists():
                    with target.open("x") as out:
                        out.write(expected)
            recheck()
            # Force applies only to these selected files; draft exports never enter this checkout.
            work.git("add", "-f", "--", path, packet)
            try:
                if work.git("diff", "--cached", "--name-only", "--", path, packet).strip():
                    work.git("commit", "-m", f"CATO -> PROME: deliver Decisions response {eid[:12]}",
                             "-m", "Implemented-by: CATO", "--", path, packet)
            except subprocess.CalledProcessError as error:
                raise ValueError("Response saved; publication commit refused. Shared index unchanged; no reply published. "
                                 + error.stderr.decode("utf-8", errors="replace")[-1600:]) from error
            commit = work.git("rev-parse", "HEAD").strip()
            expected = {path: payload, packet: text}
            exact_pair_commit(work, base, commit, expected)
            # Fetch after commit: a refusal leaves no reachable reply on shared master.
            repo.git("fetch", "origin")
            recheck()
            if not ancestor(work, repo.git("rev-parse", "origin/master").strip(), commit):
                raise ValueError("Response saved; origin changed during commit. Sync and retry. No shared reply commit.")
            exact_pair_commit(work, base, commit, expected)
            check_private_checkout(work)
            uncertain = False
            try:
                output = subprocess.run(["bash", "scripts/safe-push.sh"], cwd=work.root,
                                        capture_output=True, text=True, timeout=120, env=publication_environment())
                detail = (output.stderr + output.stdout)[-1800:]
                uncertain = output.returncode != 1
            except (OSError, subprocess.SubprocessError) as error:
                detail = type(error).__name__
                uncertain = True
            # A killed push may still land later. Absence now is not proof of failure.
            try:
                repo.git("fetch", "origin")
            except subprocess.CalledProcessError as error:
                raise ValueError("Response saved; publication status unknown. Sync before retrying or confirming in chat.") from error
            if delivery_state(repo, event) != "delivered":
                if uncertain:
                    raise ValueError("Response saved; publication status unknown. Sync before retrying or confirming in chat. " + detail)
                raise ValueError("Response saved; exact response and inbox packet are not published. "
                                 "No reply commit was left on shared master. Retry after reconciliation. " + detail)
            # The independent shared clone verifies fetched objects, not the private writer's view.
            exact_pair_commit(repo, base, commit, expected, check_worktree=False)
            refs_after = remote_refs(repo)
            if (refs_after["refs/heads/master"] != commit
                    or repo.git("rev-parse", "origin/master").strip() != commit
                    or {k: v for k, v in refs_after.items() if k != "refs/heads/master"}
                    != {k: v for k, v in refs_before.items() if k != "refs/heads/master"}):
                raise ValueError("Published pair is present, but remote references differ from the expected publication. Reconcile before confirming in chat; concurrent updates may be responsible.")
            tail = refresh_after_publication(repo)
            advice = "\n\n".join(r["check"] + ":\n" + r["output"] for r in results if r["exit"] == 1)
            return {"message": "Delivered to PROME's inbox. Awaiting its read and the applicable confirmation." + tail
                               + ("\nAdvisory findings (delivery completed):\n" + advice if advice else ""),
                    "commit": commit, "packet": published_packet(repo, event), "checks": results,
                    "receipt": "One response commit, exactly the two selected paths, and published pair verified after fetch."
                               + (" Also published previously committed work: " + "; ".join(riders) if riders else ""),
                    "riders": riders}
