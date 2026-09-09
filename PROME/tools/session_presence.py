#!/usr/bin/env python3
"""Read-only runtime evidence beside due rows. Never a global census or spawn grant."""
import argparse
import datetime as dt
import json
from pathlib import Path
import socket

import session_bridge
import spawn_list

ROOT = Path(__file__).resolve().parents[2]
MAX_AGE_SECONDS = 60


def fresh(stamp, reference):
    try:
        observed = dt.datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        return observed.tzinfo is not None and 0 <= (reference - observed).total_seconds() <= MAX_AGE_SECONDS
    except (ValueError, TypeError, AttributeError):
        return False


def validate_snapshot(data, reference, host):
    if not isinstance(data, dict):
        raise ValueError("snapshot must be an object")
    if data.get("host") != host or not fresh(data.get("observed_at"), reference):
        raise ValueError("snapshot is stale, future, undated or from another host")
    for key in ("processes", "claude"):
        rows = data.get(key, [])
        if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
            raise ValueError(f"malformed {key} inventory")
    codex = data.get("codex", {})
    if not isinstance(codex, dict):
        raise ValueError("malformed Codex inventory")
    rows = codex.get("threads", [])
    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        raise ValueError("malformed Codex thread inventory")


def evidence(owner, data, reference):
    """Positive sightings only. Preserve provider identity/status; never infer absence."""
    cwd = str(ROOT / ("PROME" if owner == "PROME" else f"AGENTS/{owner}"))
    observed, processes = [], []
    for row in data.get("claude", []):
        if row.get("cwd") == cwd and (row.get("id") or row.get("sessionId")):
            observed.append({"runtime": "claude", **{k: row.get(k) for k in
                ("id", "sessionId", "parentThreadId", "kind", "state", "status", "waitingFor")}})
    codex = data.get("codex", {})
    if fresh(codex.get("observed_at"), reference) and codex.get("endpoint"):
        for row in codex.get("threads", []):
            if row.get("cwd") == cwd and isinstance(row.get("id"), str) and row["id"]:
                observed.append({"runtime": "codex", "endpoint": codex["endpoint"],
                    **{k: row.get(k) for k in ("id", "sessionId", "parentThreadId", "status")}})
    for row in data.get("processes", []):
        if row.get("cwd") == cwd:
            processes.append({"runtime": row.get("runtime"), "identity": row.get("identity"),
                              "turn_status": "UNKNOWN"})
    return {"sessions_observed": observed, "processes_observed": processes,
            "current_presence": "UNKNOWN", "spawn_authorized": False}


def report(rows, data, reference=None, host=None):
    reference = reference or dt.datetime.now(dt.timezone.utc)
    host = host or socket.gethostname()
    error = None
    try:
        validate_snapshot(data, reference, host)
    except ValueError as exc:
        error = str(exc)
    print("Session evidence beside due obligations — metadata snapshot; current fleet presence UNKNOWN.")
    print("Missing sightings NEVER prove absence. Native ListAgents in the same minute remains required.")
    print("Git DARK/ACTIVE describes self-commit history; loaded sessions and processes do not prove active turns.")
    print("snapshot:", json.dumps({k: data.get(k) for k in
        ("observed_at", "host", "coverage", "gaps", "error")} if isinstance(data, dict) else {}, ensure_ascii=False))
    print("Codex coverage:", json.dumps(data.get("codex", {}) if isinstance(data, dict) else {}, ensure_ascii=False))
    if error:
        print(f"⚠️ UNKNOWN: {error}")
    print("key\tdue\towner\tgit_class\truntime_evidence")
    for key, due, delta, owner, git_class, basis, catalyst in rows:
        view = evidence(owner, data, reference) if error is None else {
            "current_presence": "UNKNOWN", "reason": error, "spawn_authorized": False}
        print("\t".join((key, due, owner, git_class, json.dumps(view, ensure_ascii=False))))
    print("Full due-row view complete; source/coverage gaps remain UNKNOWN.")
    return 1 if error else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sessions-json")
    args = ap.parse_args()
    try:
        data = json.loads(Path(args.sessions_json).read_text()) if args.sessions_json else session_bridge.inventory()
    except (OSError, ValueError) as exc:
        data = {"error": str(exc)}
    today = dt.date.today()
    rows = spawn_list.collect(spawn_list.read_text("PROME/DOCKET.tsv"),
        spawn_list.read_text("PROME/GATES.tsv"), today, 0, spawn_list.Liveness(None))
    return report(rows, data)


if __name__ == "__main__":
    raise SystemExit(main())
