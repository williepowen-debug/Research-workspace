#!/usr/bin/env python3
"""Observed repository activity, independent of runtime liveness. No background watcher."""
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import stat
import subprocess
import tempfile

MAX_PATHS = 500
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_DESK_BYTES = 16 * 1024 * 1024


def desk_path(owner):
    if not re.fullmatch(r"[A-Z][A-Z0-9-]{1,31}", owner):
        raise ValueError("Invalid desk name")
    return "PROME" if owner == "PROME" else f"AGENTS/{owner}"


def git(root, *args):
    result = subprocess.run(["git", "--literal-pathspecs", "-C", str(root), *args],
                            capture_output=True, timeout=30, env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"})
    if result.returncode:
        raise ValueError(f"Git {args[0]} failed (rc={result.returncode})")
    return result.stdout


def pending(root, scope):
    raw = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--", scope)
    fields, entries, index = raw.split(b"\0"), {}, 0
    while index < len(fields) and fields[index]:
        field = fields[index].decode("utf-8", "surrogateescape")
        if len(field) < 4 or field[2] != " ":
            raise ValueError("Malformed Git status")
        state, path = field[:2], field[3:]
        if not path.startswith(scope + "/") or ".." in Path(path).parts:
            raise ValueError("Git path outside requested desk")
        entries[path] = {"status": state}
        index += 1
        if "R" in state or "C" in state:
            if index >= len(fields) or not fields[index]:
                raise ValueError("Incomplete rename receipt")
            # NUL status emits destination first, then original path.
            entries[path]["original_path"] = fields[index].decode("utf-8", "surrogateescape")
            index += 1
    if len(entries) > MAX_PATHS:
        raise ValueError(f"Pending-path limit exceeded ({MAX_PATHS}); coverage UNKNOWN")
    return entries


def fingerprint(root, relative, budget):
    """Open through directory descriptors, never through symlinks or special files."""
    parts = Path(relative).parts
    if any(p.lower() in (".codex", ".claude", "sessions", "transcripts", "credentials") for p in parts) or \
            any(p.lower().startswith((".env", "auth.json")) or p.lower().endswith(
                (".key", ".pem", ".events.jsonl", ".input.txt")) for p in parts):
        return None, "excluded sensitive/runtime path", 0
    directory = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    file_fd = None
    try:
        for part in parts[:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=directory)
            os.close(directory)
            directory = child
        file_fd = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=directory)
        before = os.fstat(file_fd)
        if not stat.S_ISREG(before.st_mode) or before.st_size > min(MAX_FILE_BYTES, budget):
            return None, "special/large file or scan budget exhausted", 0
        raw = b""
        while len(raw) <= MAX_FILE_BYTES:
            chunk = os.read(file_fd, min(65536, MAX_FILE_BYTES + 1 - len(raw)))
            if not chunk:
                break
            raw += chunk
        after = os.fstat(file_fd)
        keys = ("st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")
        if len(raw) > min(MAX_FILE_BYTES, budget) or any(getattr(before, k) != getattr(after, k) for k in keys):
            return None, "file changed during read", len(raw)
        return hashlib.sha256(raw).hexdigest(), "content measured", len(raw)
    except FileNotFoundError:
        return "ABSENT", "path absent at observation", 0
    except OSError as exc:
        return None, f"unmeasured: {type(exc).__name__}", 0
    finally:
        if file_fd is not None:
            os.close(file_fd)
        os.close(directory)


def last_commit(root, owner):
    pattern = rf"^{re.escape(owner)}( ->|:)"
    raw = git(root, "log", "-n", "40", "--extended-regexp", f"--grep={pattern}",
              "--format=%H%x09%cI%x09%s").decode("utf-8", "replace")
    for line in raw.splitlines():
        fields = line.split("\t", 2)
        if len(fields) == 3 and re.match(pattern, fields[2]):
            return {"sha": fields[0], "committed_at": fields[1], "subject": fields[2],
                    "basis": "desk-named commit subject; not proof of current activity"}
    return None


def capture(root, owners, reference):
    root = Path(root).resolve()
    result = {"version": 1, "repository": str(root), "host": socket.gethostname(),
              "observed_at": reference.isoformat(), "desks": {}}
    before = git(root, "rev-parse", "HEAD").decode().strip()
    for owner in sorted(set(owners)):
        try:
            scope = desk_path(owner)
            if not (root / scope).is_dir():
                raise ValueError("Desk directory is missing")
            entries = pending(root, scope)
            budget = MAX_DESK_BYTES
            for path, item in entries.items():
                item["fingerprint"], item["measurement"], used = fingerprint(root, path, budget)
                budget -= used
            # A changing dirty set cannot be presented as one consistent capture.
            after = pending(root, scope)
            if {p: {k: v for k, v in item.items() if k in ("status", "original_path")}
                    for p, item in entries.items()} != after:
                raise ValueError("Pending paths changed during scan")
            result["desks"][owner] = {"pending": entries, "last_self_commit": last_commit(root, owner),
                "complete": True, "content_complete": all(item["fingerprint"] is not None for item in entries.values())}
        except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
            result["desks"][owner] = {"complete": False, "error": str(exc), "pending": {}}
    result["head"] = before
    if before != git(root, "rev-parse", "HEAD").decode().strip():
        raise ValueError("HEAD changed during scan; retry observation")
    return result


def compare(current, previous):
    for owner, desk in current["desks"].items():
        prior = previous["desks"][owner] if previous else None
        now_paths, old_paths = desk["pending"], prior["pending"] if prior else {}
        desk["comparison"] = {"baseline_observed_at": previous["observed_at"] if previous else None,
            "baseline_head": previous["head"] if previous else None,
            "meaning": "first observation; edit time unknown" if prior is None else "between saved observations; writer unknown",
            "changed": [p for p, item in now_paths.items() if prior is not None
                and item.get("fingerprint") is not None and (p not in old_paths or
                (old_paths[p].get("fingerprint") is not None and
                 (item["fingerprint"], item["status"]) != (old_paths[p]["fingerprint"], old_paths[p]["status"])))],
            "no_longer_pending": sorted(set(old_paths) - set(now_paths)) if desk["complete"] else [],
            "self_commit_changed": prior is not None and desk.get("last_self_commit") != prior.get("last_self_commit")}
        if not desk["complete"]:
            desk["comparison"].update(meaning="UNKNOWN: incomplete capture; baseline preserved",
                changed=None, no_longer_pending=None, self_commit_changed=None)
    return current


def observe(root, owners, state_path=None, reference=None):
    reference = reference or dt.datetime.now(dt.timezone.utc)
    if state_path is None:
        return compare(capture(root, owners, reference), None)
    path = Path(state_path).absolute()
    if path.is_symlink() or path.resolve().is_relative_to(Path(root).resolve()):
        raise ValueError("Comparison snapshot must be outside the repository and not a symlink")
    # The lock file persists; flock is released on process exit, including crashes.
    with path.with_suffix(path.suffix + ".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        previous = None
        if path.exists():
            previous = json.loads(path.read_text())
            if not isinstance(previous, dict) or any(previous.get(k) != v for k, v in
                    {"version": 1, "repository": str(Path(root).resolve()), "host": socket.gethostname()}.items()):
                raise ValueError("Comparison snapshot provenance mismatch")
            stamp = dt.datetime.fromisoformat(previous["observed_at"])
            if stamp.tzinfo is None or stamp > reference or set(previous["desks"]) != set(owners):
                raise ValueError("Comparison timestamp/desk set mismatch")
            if not isinstance(previous.get("head"), str) or any(not isinstance(d, dict) or
                    not isinstance(d.get("pending"), dict) or any(not isinstance(v, dict) or
                    not isinstance(v.get("status"), str) or not isinstance(v.get("fingerprint"), (str, type(None)))
                    for v in d["pending"].values()) for d in previous["desks"].values()):
                raise ValueError("Malformed comparison snapshot")
        current = compare(capture(root, owners, reference), previous)
        current["comparison_file"] = str(path)
        current["baseline_advanced"] = all(d["complete"] for d in current["desks"].values())
        if current["baseline_advanced"]:
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False, encoding="utf-8") as stream:
                    temporary = Path(stream.name)
                    json.dump(current, stream, ensure_ascii=True)
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary.replace(path)
            finally:
                if temporary and temporary.exists():
                    temporary.unlink()
        return current


def public_view(snapshot, owner):
    desk = snapshot["desks"][owner]
    return {"observed_at": snapshot["observed_at"], "coverage": "Git-visible desk files; ignored files excluded",
        "complete": desk["complete"], "error": desk.get("error"),
        "content_complete": desk.get("content_complete", False),
        "pending_files": [{"path": p, **{k: v for k, v in item.items() if k != "fingerprint"}}
                          for p, item in desk["pending"].items()],
        "last_self_commit": desk.get("last_self_commit"), "comparison": desk["comparison"],
        "baseline_advanced": snapshot.get("baseline_advanced", False),
        "current_session_state": "UNKNOWN"}
