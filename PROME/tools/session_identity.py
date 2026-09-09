#!/usr/bin/env python3
"""Optional stored Codex identity metadata. Stored records never establish liveness."""
import os
from pathlib import Path
import sqlite3
import json

from desk_activity import desk_path


def collect(root, owners, database=None, caller_cwd=None, caller_id=None):
    caller_id = caller_id if caller_id is not None else os.environ.get("CODEX_THREAD_ID")
    caller_cwd = Path(caller_cwd or Path.cwd()).resolve()
    root = Path(root).resolve()
    result = {owner: {"caller_session": None, "stored_candidates": [],
        "stored_coverage": "UNKNOWN: no metadata store supplied", "current_presence": "UNKNOWN"} for owner in owners}
    # Caller association is explicit environment + exact caller cwd, never inferred from a process name.
    for owner in owners:
        if caller_id and caller_cwd == root / desk_path(owner):
            result[owner]["caller_session"] = {"id": caller_id, "basis": "CODEX_THREAD_ID + exact caller cwd",
                "metadata_corroborated": False}
    if database is None:
        return result
    connection = None
    try:
        path = Path(database).resolve()
        connection = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True, timeout=2)
        connection.row_factory = sqlite3.Row
        # Explicit allowlist; no first_user_message, preview, title or rollout contents.
        for owner in owners:
            rows = connection.execute("SELECT id,cwd,source,archived,updated_at FROM threads WHERE cwd=? "
                "ORDER BY updated_at DESC LIMIT 101", (str(root / desk_path(owner)),)).fetchall()
            candidates = []
            for row in rows[:100]:
                parent, kind = None, "UNKNOWN"
                if row["source"] in ("cli", "vscode", "exec", "appServer"):
                    kind = "interactive/source-declared"
                else:
                    try:
                        source = json.loads(row["source"])
                        parent = source.get("subagent", {}).get("thread_spawn", {}).get("parent_thread_id")
                        kind = "helper" if parent else "UNKNOWN"
                    except (ValueError, TypeError, AttributeError):
                        pass
                candidates.append({"id": row["id"], "cwd": row["cwd"], "archived": row["archived"],
                    "stored_updated_at": row["updated_at"], "parent_id": parent, "kind": kind,
                    "liveness": "UNKNOWN"})
            result[owner]["stored_candidates"] = candidates
            result[owner]["stored_coverage"] = "PARTIAL: more than 100 candidates" if len(rows) > 100 else "exact-cwd stored records only"
            result[owner]["database"] = str(path)
            if caller_id and any(c["id"] == caller_id for c in candidates):
                result[owner]["caller_session"] = {"id": caller_id,
                    "basis": "CODEX_THREAD_ID + exact stored cwd", "metadata_corroborated": True}
            caller = result[owner]["caller_session"]
            if caller:
                caller["metadata_corroborated"] = any(c["id"] == caller["id"] for c in candidates)
    except (OSError, ValueError, sqlite3.Error) as exc:
        for value in result.values():
            value["stored_candidates"] = []
            value["stored_coverage"] = f"UNKNOWN: {type(exc).__name__}"
            if value["caller_session"]:
                value["caller_session"]["metadata_corroborated"] = False
    finally:
        if connection is not None:
            connection.close()
    return result
