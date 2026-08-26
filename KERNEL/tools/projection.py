#!/usr/bin/env python3
"""Disposable fixture-only SQLite projection rebuilt from accepted events."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from core import (
    AUTHORITY_MODE,
    POLICY_VERSION,
    SCHEMA_VERSION,
    Finding,
    canonical_bytes,
    replay,
    validate_event,
)
from render import NOTICE, RENDERER_VERSION, VIEW_NAMES, render_views


PROJECTION_VERSION = "kernel.projection.1"
LIVE_KERNEL_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = LIVE_KERNEL_ROOT.parent
LIVE_EVENT_ROOT = LIVE_KERNEL_ROOT / "shadow" / "events"
TABLES = {
    "metadata",
    "registered_views",
    "semantic_snapshot",
    "source_events",
}
METADATA_KEYS = {
    "authority_mode",
    "notice",
    "policy_version",
    "projection_version",
    "render_as_of",
    "renderer_version",
    "schema_version",
    "semantic_sha256",
    "source_event_count",
    "source_input_sha256",
}


class ProjectionError(ValueError):
    def __init__(self, findings: list[Finding]):
        super().__init__("; ".join(f"{finding.code}: {finding.message}" for finding in findings))
        self.findings = findings


@dataclass(frozen=True)
class ProjectionSnapshot:
    path: Path
    metadata: dict[str, str]
    semantic_state: dict[str, Any]
    views: dict[str, str]


def rebuild_projection(
    workspace_root: str | Path,
    events: Iterable[dict[str, Any]],
    *,
    render_as_of: str,
) -> ProjectionSnapshot:
    """Atomically replace the disposable projection from explicit durable events."""

    workspace = _fixture_workspace(workspace_root)
    source_events, metadata, semantic_state, views = _expected_projection(events, render_as_of)
    rw_root = workspace / ".rw"
    projection_path = rw_root / "projection.sqlite"
    try:
        rw_root.mkdir(parents=True, exist_ok=True)
        _guard_resolved_path(rw_root, "projection .rw directory")
        _guard_resolved_path(projection_path, "projection database")
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=".tmp-projection-",
            suffix=".sqlite",
            dir=rw_root,
        )
    except ProjectionError:
        raise
    except OSError as exc:
        raise ProjectionError(
            [Finding("PROJECTION_REBUILD_FAILED", str(exc), str(projection_path))]
        ) from exc
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        _write_database(temporary, source_events, metadata, semantic_state, views)
        _fsync_file(temporary)
        _fsync_directory(rw_root)
        os.replace(temporary, projection_path)
        _fsync_directory(rw_root)
    except (OSError, sqlite3.Error) as exc:
        _remove_sqlite_temporary(temporary)
        raise ProjectionError([Finding("PROJECTION_REBUILD_FAILED", str(exc), str(projection_path))]) from exc
    return load_projection(workspace)


def load_projection(workspace_root: str | Path) -> ProjectionSnapshot:
    """Read and fully reconcile a projection without creating or mutating it."""

    workspace = _fixture_workspace(workspace_root)
    projection_path = workspace / ".rw" / "projection.sqlite"
    _guard_resolved_path(projection_path, "projection database")
    if not projection_path.is_file():
        raise ProjectionError([Finding("PROJECTION_MISSING", "projection.sqlite does not exist", str(projection_path))])
    try:
        connection = sqlite3.connect(f"{projection_path.as_uri()}?mode=ro", uri=True)
        connection.execute("PRAGMA query_only = ON")
        try:
            snapshot = _read_and_verify_database(connection, projection_path)
        finally:
            connection.close()
    except ProjectionError:
        raise
    except (OSError, sqlite3.Error, TypeError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        raise ProjectionError(
            [Finding("PROJECTION_INVALID", str(exc), str(projection_path))]
        ) from exc
    return snapshot


def verify_projection(
    workspace_root: str | Path,
    events: Iterable[dict[str, Any]],
    *,
    render_as_of: str,
) -> ProjectionSnapshot:
    """Prove the stored projection equals the supplied durable-event replay."""

    stored = load_projection(workspace_root)
    _, metadata, semantic_state, views = _expected_projection(events, render_as_of)
    findings: list[Finding] = []
    if stored.metadata != metadata:
        findings.append(Finding("PROJECTION_METADATA_MISMATCH", "stored metadata differs from durable inputs"))
    if stored.semantic_state != semantic_state:
        findings.append(Finding("PROJECTION_SEMANTIC_MISMATCH", "stored semantic state differs from replay"))
    if stored.views != views:
        findings.append(Finding("PROJECTION_VIEW_MISMATCH", "stored view bytes differ from replay"))
    if findings:
        raise ProjectionError(findings)
    return stored


def _expected_projection(
    events: Iterable[dict[str, Any]],
    render_as_of: str,
) -> tuple[list[dict[str, Any]], dict[str, str], dict[str, Any], dict[str, str]]:
    values = list(events)
    findings: list[Finding] = []
    for index, event in enumerate(values):
        validation = validate_event(event)
        if not validation.valid:
            codes = ",".join(sorted({finding.code for finding in validation.findings}))
            findings.append(
                Finding("PROJECTION_EVENT_INVALID", codes, f"$events[{index}]")
            )
    if findings:
        raise ProjectionError(findings)
    try:
        digests = {
            index: hashlib.sha256(canonical_bytes(event)).hexdigest()
            for index, event in enumerate(values)
        }
        source_events = [
            event
            for _, event in sorted(
                enumerate(values),
                key=lambda item: (
                    item[1]["stream_id"],
                    item[1]["stream_version"],
                    item[1]["event_id"],
                    digests[item[0]],
                ),
            )
        ]
    except (TypeError, ValueError, UnicodeError) as exc:
        raise ProjectionError(
            [Finding("PROJECTION_EVENT_INVALID", str(exc), "$events")]
        ) from exc
    replayed = replay(source_events)
    semantic_state = _semantic_document(replayed)
    semantic_sha256 = hashlib.sha256(canonical_bytes(semantic_state)).hexdigest()
    source_items = [
        (event["event_id"], hashlib.sha256(canonical_bytes(event)).hexdigest())
        for event in source_events
    ]
    source_input_sha256 = hashlib.sha256(canonical_bytes(source_items)).hexdigest()
    try:
        views = render_views(source_events, render_as_of=render_as_of)
    except ValueError as exc:
        raise ProjectionError([Finding("PROJECTION_RENDER_AS_OF_INVALID", str(exc), "$render_as_of")]) from exc
    metadata = {
        "authority_mode": AUTHORITY_MODE,
        "notice": NOTICE,
        "policy_version": POLICY_VERSION,
        "projection_version": PROJECTION_VERSION,
        "render_as_of": render_as_of,
        "renderer_version": RENDERER_VERSION,
        "schema_version": SCHEMA_VERSION,
        "semantic_sha256": semantic_sha256,
        "source_event_count": str(len(source_events)),
        "source_input_sha256": source_input_sha256,
    }
    return source_events, metadata, semantic_state, views


def _semantic_document(replayed: Any) -> dict[str, Any]:
    return {
        "conflicts": sorted(replayed.conflicts),
        "current": {key: replayed.current[key] for key in sorted(replayed.current)},
        "findings": [
            {
                "code": finding.code,
                "location": finding.location,
                "message": finding.message,
            }
            for finding in sorted(
                replayed.findings,
                key=lambda item: (item.code, item.location, item.message),
            )
        ],
        "forecast_states": {
            key: replayed.forecast_states[key] for key in sorted(replayed.forecast_states)
        },
        "question_states": {
            key: replayed.question_states[key] for key in sorted(replayed.question_states)
        },
        "streams": {key: replayed.streams[key] for key in sorted(replayed.streams)},
    }


def _write_database(
    path: Path,
    events: list[dict[str, Any]],
    metadata: dict[str, str],
    semantic_state: dict[str, Any],
    views: dict[str, str],
) -> None:
    connection = sqlite3.connect(path)
    try:
        connection.execute("PRAGMA journal_mode = DELETE")
        connection.execute("PRAGMA synchronous = FULL")
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA user_version = 1")
        connection.executescript(
            """
            CREATE TABLE metadata (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            ) WITHOUT ROWID;
            CREATE TABLE source_events (
                position INTEGER PRIMARY KEY,
                event_id TEXT NOT NULL,
                stream_id TEXT NOT NULL,
                stream_version INTEGER NOT NULL,
                event_sha256 TEXT NOT NULL,
                event_json TEXT NOT NULL
            );
            CREATE TABLE semantic_snapshot (
                singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
                semantic_sha256 TEXT NOT NULL,
                semantic_json TEXT NOT NULL
            );
            CREATE TABLE registered_views (
                name TEXT PRIMARY KEY,
                content_sha256 TEXT NOT NULL,
                content BLOB NOT NULL
            ) WITHOUT ROWID;
            """
        )
        with connection:
            connection.executemany(
                "INSERT INTO metadata(key, value) VALUES (?, ?)",
                sorted(metadata.items()),
            )
            for position, event in enumerate(events):
                event_bytes = canonical_bytes(event)
                connection.execute(
                    """
                    INSERT INTO source_events(
                        position, event_id, stream_id, stream_version, event_sha256, event_json
                    ) VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        position,
                        event["event_id"],
                        event["stream_id"],
                        event["stream_version"],
                        hashlib.sha256(event_bytes).hexdigest(),
                        event_bytes.decode("utf-8"),
                    ),
                )
            semantic_bytes = canonical_bytes(semantic_state)
            connection.execute(
                "INSERT INTO semantic_snapshot(singleton, semantic_sha256, semantic_json) VALUES (1, ?, ?)",
                (hashlib.sha256(semantic_bytes).hexdigest(), semantic_bytes.decode("utf-8")),
            )
            for name in VIEW_NAMES:
                content = views[name].encode("utf-8")
                connection.execute(
                    "INSERT INTO registered_views(name, content_sha256, content) VALUES (?, ?, ?)",
                    (name, hashlib.sha256(content).hexdigest(), content),
                )
    finally:
        connection.close()


def _read_and_verify_database(
    connection: sqlite3.Connection,
    projection_path: Path,
) -> ProjectionSnapshot:
    integrity = connection.execute("PRAGMA integrity_check").fetchone()
    if integrity != ("ok",):
        raise ProjectionError([Finding("PROJECTION_INVALID", "SQLite integrity check failed", str(projection_path))])
    user_version = connection.execute("PRAGMA user_version").fetchone()
    if user_version != (1,):
        raise ProjectionError([Finding("PROJECTION_VERSION_UNSUPPORTED", str(user_version), str(projection_path))])
    tables = {
        row[0]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%'"
        )
    }
    if tables != TABLES:
        raise ProjectionError(
            [Finding("PROJECTION_SCHEMA_INVALID", f"tables={sorted(tables)}", str(projection_path))]
        )
    metadata = dict(connection.execute("SELECT key, value FROM metadata ORDER BY key"))
    if set(metadata) != METADATA_KEYS:
        raise ProjectionError(
            [Finding("PROJECTION_METADATA_INVALID", f"keys={sorted(metadata)}", str(projection_path))]
        )
    if metadata["projection_version"] != PROJECTION_VERSION:
        raise ProjectionError(
            [Finding("PROJECTION_VERSION_UNSUPPORTED", metadata["projection_version"], str(projection_path))]
        )
    rows = list(
        connection.execute(
            """
            SELECT position, event_id, stream_id, stream_version, event_sha256, event_json
            FROM source_events ORDER BY position
            """
        )
    )
    if [row[0] for row in rows] != list(range(len(rows))):
        raise ProjectionError(
            [Finding("PROJECTION_SOURCE_INVALID", "source event positions are not contiguous", str(projection_path))]
        )
    events: list[dict[str, Any]] = []
    for position, event_id, stream_id, stream_version, event_sha256, event_json in rows:
        event = _strict_json(event_json)
        if not isinstance(event, dict) or canonical_bytes(event).decode("utf-8") != event_json:
            raise ProjectionError(
                [Finding("PROJECTION_SOURCE_INVALID", "source event JSON is not canonical", f"$events[{position}]")]
            )
        event_bytes = canonical_bytes(event)
        if (
            hashlib.sha256(event_bytes).hexdigest() != event_sha256
            or event.get("event_id") != event_id
            or event.get("stream_id") != stream_id
            or event.get("stream_version") != stream_version
        ):
            raise ProjectionError(
                [Finding("PROJECTION_SOURCE_INVALID", "source event columns do not reconcile", f"$events[{position}]")]
            )
        events.append(event)
    _, expected_metadata, semantic_state, expected_views = _expected_projection(
        events,
        metadata["render_as_of"],
    )
    if metadata != expected_metadata:
        raise ProjectionError(
            [Finding("PROJECTION_METADATA_MISMATCH", "metadata does not reconcile with source events", str(projection_path))]
        )
    semantic_rows = list(
        connection.execute(
            "SELECT singleton, semantic_sha256, semantic_json FROM semantic_snapshot"
        )
    )
    if len(semantic_rows) != 1 or semantic_rows[0][0] != 1:
        raise ProjectionError(
            [Finding("PROJECTION_SEMANTIC_INVALID", "semantic snapshot singleton is invalid", str(projection_path))]
        )
    _, semantic_sha256, semantic_json = semantic_rows[0]
    stored_semantic = _strict_json(semantic_json)
    if (
        not isinstance(stored_semantic, dict)
        or canonical_bytes(stored_semantic).decode("utf-8") != semantic_json
        or hashlib.sha256(semantic_json.encode("utf-8")).hexdigest() != semantic_sha256
        or stored_semantic != semantic_state
    ):
        raise ProjectionError(
            [Finding("PROJECTION_SEMANTIC_MISMATCH", "semantic snapshot does not reconcile", str(projection_path))]
        )
    view_rows = list(
        connection.execute(
            "SELECT name, content_sha256, content FROM registered_views ORDER BY name"
        )
    )
    if {row[0] for row in view_rows} != set(VIEW_NAMES) or len(view_rows) != len(VIEW_NAMES):
        raise ProjectionError(
            [Finding("PROJECTION_VIEW_SET_INVALID", "registered view set is incomplete", str(projection_path))]
        )
    stored_views: dict[str, str] = {}
    for name, content_sha256, content in view_rows:
        if not isinstance(content, bytes) or hashlib.sha256(content).hexdigest() != content_sha256:
            raise ProjectionError(
                [Finding("PROJECTION_VIEW_MISMATCH", f"view hash mismatch: {name}", str(projection_path))]
            )
        value = content.decode("utf-8")
        if value != expected_views[name]:
            raise ProjectionError(
                [Finding("PROJECTION_VIEW_MISMATCH", f"view content mismatch: {name}", str(projection_path))]
            )
        stored_views[name] = value
    return ProjectionSnapshot(projection_path, metadata, stored_semantic, stored_views)


def _strict_json(value: str) -> Any:
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, item in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON member: {key}")
            result[key] = item
        return result

    def reject_constant(item: str) -> None:
        raise ValueError(f"non-standard JSON constant: {item}")

    return json.loads(value, object_pairs_hook=unique_object, parse_constant=reject_constant)


def _fixture_workspace(workspace_root: str | Path) -> Path:
    workspace = Path(workspace_root).resolve()
    repository_root = REPOSITORY_ROOT.resolve()
    if (
        workspace == repository_root
        or repository_root in workspace.parents
        or workspace in repository_root.parents
    ):
        raise ProjectionError(
            [Finding("PROJECTION_BOUNDARY_REFUSED", "projection cannot target the live repository tree", str(workspace))]
        )
    return workspace


def _guard_resolved_path(path: Path, label: str) -> None:
    resolved = path.resolve()
    repository_root = REPOSITORY_ROOT.resolve()
    if resolved == repository_root or repository_root in resolved.parents:
        raise ProjectionError(
            [Finding("PROJECTION_BOUNDARY_REFUSED", f"{label} resolves into the live repository", str(path))]
        )


def _fsync_file(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _remove_sqlite_temporary(path: Path) -> None:
    for candidate in (path, Path(f"{path}-journal"), Path(f"{path}-wal"), Path(f"{path}-shm")):
        candidate.unlink(missing_ok=True)


def _load_fixture_events(path: Path) -> list[dict[str, Any]]:
    resolved = path.resolve()
    live_event_root = LIVE_EVENT_ROOT.resolve()
    if resolved == live_event_root or live_event_root in resolved.parents:
        raise ProjectionError(
            [Finding("PROJECTION_BOUNDARY_REFUSED", "live accepted-event paths are not authorized", str(path))]
        )
    value = _strict_json(path.read_text(encoding="utf-8"))
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise ProjectionError(
            [Finding("PROJECTION_EVENT_INVALID", "fixture input must be a JSON array of events", str(path))]
        )
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild or verify a fixture-only disposable projection")
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--events", type=Path, required=True)
    parser.add_argument("--as-of", required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        events = _load_fixture_events(args.events)
        if args.check:
            snapshot = verify_projection(args.workspace, events, render_as_of=args.as_of)
            action = "verified"
        else:
            snapshot = rebuild_projection(args.workspace, events, render_as_of=args.as_of)
            action = "rebuilt"
    except (OSError, TypeError, UnicodeError, ValueError, json.JSONDecodeError, ProjectionError) as exc:
        print(
            f"perimeter: workspace={args.workspace.resolve()} events={args.events.resolve()} render_as_of={args.as_of}"
        )
        print(f"EXCEPTION: disposable projection {('check' if args.check else 'rebuild')} failed")
        findings = exc.findings if isinstance(exc, ProjectionError) else [Finding("PROJECTION_INVALID", str(exc))]
        for finding in findings:
            print(f"{finding.code}\t{finding.location}\t{finding.message}")
        return 1
    print(
        f"perimeter: workspace={args.workspace.resolve()} events={args.events.resolve()} "
        f"event_count={snapshot.metadata['source_event_count']} render_as_of={args.as_of}"
    )
    print(
        f"PASS: disposable projection {action}; semantic state and registered view bytes reconcile "
        "with explicit fixture events; SQLite has no authority"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
