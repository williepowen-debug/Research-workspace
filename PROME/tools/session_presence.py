#!/usr/bin/env python3
"""Read-only runtime evidence beside due rows. Never a global census or spawn grant."""
import argparse
import datetime as dt
import json
from pathlib import Path
import socket

import session_bridge
import spawn_list
import desk_activity
import session_identity

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


def _field(row, name, index):
    """Read one producer field by NAME, falling back to position. See spawn_list.Row."""
    value = getattr(row, name, None)
    if value is None:
        value = row[index]
    return str(value)


def report(rows, data, reference=None, host=None, activities=None, identities=None, desks=()):
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
    if activities is not None or identities is not None:
        print("Desk overview — file activity is independent evidence; quiet files do not mean an offline desk.")
        for owner in sorted(set(desks) | {_field(r, "owner", 3) for r in rows}):
            if owner in ("WILL", "?"):
                continue
            view = evidence(owner, data, reference) if error is None else {"current_presence": "UNKNOWN", "reason": error}
            view["spawn_authorized"] = False
            view["identity"] = (identities or {}).get(owner, {"current_presence": "UNKNOWN"})
            if activities and owner in activities.get("desks", {}):
                view["file_activity"] = desk_activity.public_view(activities, owner)
            else:
                view["file_activity"] = {"error": (activities or {}).get("error", "not collected")}
            print(owner + "\t" + json.dumps(view, ensure_ascii=True))
    print("key\tdue\towner\tgit_class\truntime_evidence")
    for row in rows:
        # ⛔ NEVER positionally unpack the producer's whole row (2026-09-19): spawn_list gained a
        # `cadence` field and the 7-field unpack here crashed the boot gate. Named access first,
        # index fallback for a plain tuple. Adding a field must never break this reader again.
        key, due = _field(row, "key", 0), _field(row, "due", 1)
        owner, git_class = _field(row, "owner", 3), _field(row, "cls", 4)
        view = evidence(owner, data, reference) if error is None else {
            "current_presence": "UNKNOWN", "reason": error, "spawn_authorized": False}
        print("\t".join((key, due, owner, git_class, json.dumps(view, ensure_ascii=False))))
    print("Full due-row view complete; source/coverage gaps remain UNKNOWN.")
    return 1 if error else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sessions-json")
    ap.add_argument("--desk", action="append", default=[], help="Include a desk even without a due row; repeatable")
    ap.add_argument("--activity-state", type=Path, help="Optional snapshot outside the repo for between-run comparisons")
    ap.add_argument("--codex-state-db", type=Path, help="Optional read-only stored identity metadata; never live status")
    args = ap.parse_args()
    try:
        for owner in args.desk:
            desk_activity.desk_path(owner)
    except ValueError as exc:
        ap.error(str(exc))
    try:
        data = json.loads(Path(args.sessions_json).read_text()) if args.sessions_json else session_bridge.inventory()
    except (OSError, ValueError) as exc:
        data = {"error": str(exc)}
    today = dt.date.today()
    rows = spawn_list.collect(spawn_list.read_text("PROME/DOCKET.tsv"),
        spawn_list.read_text("PROME/GATES.tsv"), today, 0, spawn_list.Liveness(None))
    owners = sorted(set(args.desk) | {r[3] for r in rows if r[3] not in ("WILL", "?")} | {"PROME"})
    try:
        for owner in owners:
            desk_activity.desk_path(owner)
        activities = desk_activity.observe(ROOT, owners, args.activity_state)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        activities = {"error": f"UNKNOWN activity: {exc}"}
    identities = session_identity.collect(ROOT, owners, args.codex_state_db)
    rc = report(rows, data, activities=activities, identities=identities, desks=owners)
    return 1 if activities.get("error") or any(not d["complete"] or not d.get("content_complete", False)
        for d in activities.get("desks", {}).values()) else rc


def guarded_main():
    """rc 2 = the CHECK DID NOT RUN (we did not look). rc 1 = it ran, evidence unavailable.
    ⛔ These must never render identically: on 2026-09-19 a crash and a stale snapshot both
    reached the boot summary as the same UNKNOWN. CHECK_STANDARD §9 rc convention."""
    try:
        return main()
    except Exception as exc:  # noqa: BLE001 — a reader crash is a DID-NOT-RUN, never a finding
        import traceback
        traceback.print_exc()
        print(f"\u274c CHECK DID NOT RUN \u2014 {type(exc).__name__}: {str(exc)[:160]}")
        print("\u26d4 rc=2 UNKNOWN EXECUTION. This establishes NOTHING about fleet presence, and is "
              "NOT the same state as 'ran, evidence unavailable' (rc=1). Do not read it as either.")
        return 2


if __name__ == "__main__":
    raise SystemExit(guarded_main())
