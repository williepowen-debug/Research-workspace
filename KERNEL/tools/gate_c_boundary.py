#!/usr/bin/env python3
"""Gate C live-compatible acceptance boundary for marked synthetic mirrors only."""

from __future__ import annotations

import argparse
import json
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from acceptance import AcceptanceRun, FixtureAcceptanceRunner, format_acceptance_run
from custody import load_custody, run_with_custody
from native import FULL_SHA, SubprocessGitBoundary
from permissions import PermissionRegistry
from writer import FixtureResultStore


LIVE_REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
MARKER = ".gate-c-synthetic-mirror.json"
SUBMISSION = re.compile(
    r"AGENTS/(?P<actor>[A-Z][A-Z0-9_-]*)/outbox/kernel/submissions/"
    r"(?P<command_id>CMD-[0-9a-f-]+)\.json"
)
NOTICE = "SHADOW — NON-AUTHORITATIVE"


@dataclass(frozen=True)
class ExplicitSubmission:
    path: str
    command: dict[str, Any]


class GateCBoundaryError(ValueError):
    pass


class SyntheticMirrorBoundary:
    """Resolve only explicit canonical inputs inside a marked non-live mirror."""

    def __init__(self, root: str | Path, *, live_repository_root: str | Path | None = None):
        self.root = Path(root).resolve()
        live = Path(live_repository_root or LIVE_REPOSITORY_ROOT).resolve()
        self.live_repository_root = live
        if self.root == live or live in self.root.parents or self.root in live.parents:
            raise GateCBoundaryError("Gate C synthetic boundary refuses the live repository tree")
        marker_path = self.root / MARKER
        try:
            marker = json.loads(marker_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise GateCBoundaryError(f"valid synthetic mirror marker required: {exc}") from exc
        if marker != {"authority": "NON_AUTHORITATIVE", "mode": "SYNTHETIC_MIRROR"}:
            raise GateCBoundaryError("synthetic mirror marker has unregistered content")

    def load_inventory(
        self,
        inventory_path: str | Path,
        submission_commit: str,
    ) -> tuple[ExplicitSubmission, ...]:
        git = SubprocessGitBoundary(self.root)
        if not FULL_SHA.fullmatch(submission_commit) or git.resolve_commit(submission_commit) != submission_commit:
            raise GateCBoundaryError("submission commit must be one existing full commit SHA")
        try:
            inventory = json.loads(Path(inventory_path).read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise GateCBoundaryError(f"explicit inventory is invalid: {exc}") from exc
        if not isinstance(inventory, list) or not inventory or len(inventory) > 3:
            raise GateCBoundaryError("explicit inventory must contain 1 to 3 submission paths")
        loaded: list[ExplicitSubmission] = []
        seen_paths: set[str] = set()
        seen_ids: set[str] = set()
        for entry in inventory:
            if not isinstance(entry, str):
                raise GateCBoundaryError("inventory entries must be canonical relative path strings")
            pure = PurePosixPath(entry)
            if pure.is_absolute() or ".." in pure.parts or str(pure) != entry:
                raise GateCBoundaryError(f"non-canonical submission path: {entry}")
            match = SUBMISSION.fullmatch(entry)
            if match is None:
                raise GateCBoundaryError(f"submission path is outside the Gate C allowlist: {entry}")
            if entry in seen_paths:
                raise GateCBoundaryError(f"duplicate explicit submission path: {entry}")
            try:
                blob = git.read_blob(submission_commit, entry)
                if blob is None:
                    raise GateCBoundaryError(f"submission is absent at the exact commit: {entry}")
                command = json.loads(blob.decode("utf-8"))
            except (UnicodeError, json.JSONDecodeError) as exc:
                raise GateCBoundaryError(f"submission cannot be read exactly: {entry}: {exc}") from exc
            command_id = command.get("command_id") if isinstance(command, dict) else None
            actor_id = command.get("actor_id") if isinstance(command, dict) else None
            if command_id != match.group("command_id") or actor_id != match.group("actor"):
                raise GateCBoundaryError(f"path, actor_id, and command_id do not agree: {entry}")
            if command_id in seen_ids:
                raise GateCBoundaryError(f"duplicate command identity in explicit inventory: {command_id}")
            seen_paths.add(entry)
            seen_ids.add(command_id)
            loaded.append(ExplicitSubmission(entry, command))
        return tuple(loaded)


def run_synthetic(
    boundary: SyntheticMirrorBoundary,
    submissions: tuple[ExplicitSubmission, ...],
    *,
    actors: Path,
    capabilities: Path,
    event_ids: Path,
    custody_policy: Path,
    recorded_at: str,
    dry_run: bool,
) -> tuple[AcceptanceRun, Path]:
    registry = PermissionRegistry.from_files(actors, capabilities)
    custody_document = json.loads(custody_policy.read_text(encoding="utf-8"))
    custody = load_custody(custody_document)
    mapping = json.loads(event_ids.read_text(encoding="utf-8"))
    if not isinstance(mapping, dict):
        raise GateCBoundaryError("event ID map must be an object")
    temporary: tempfile.TemporaryDirectory[str] | None = None
    if dry_run:
        temporary = tempfile.TemporaryDirectory(prefix="kernel-gate-c-dry-run-")
        result_root = Path(temporary.name) / "KERNEL"
    else:
        result_root = boundary.root / "KERNEL"
    try:
        runner = FixtureAcceptanceRunner(
            FixtureResultStore(
                result_root,
                forbidden_repository_root=boundary.live_repository_root,
            ),
            writer_id="PROME",
            registry=registry,
            git=SubprocessGitBoundary(boundary.root),
            event_id_for=lambda command: mapping[command["command_id"]],
            recorded_at_for=lambda _command: recorded_at,
        )
        commands = [item.command for item in submissions]
        paths = {item.command["command_id"]: item.path for item in submissions}
        run = run_with_custody(
            runner,
            custody,
            writer_id="PROME",
            recorded_at=recorded_at,
            submissions=commands,
            submission_paths=paths,
        )
        return run, result_root
    finally:
        # The run object contains the evidence; dry-run durable files are deliberately ephemeral.
        if temporary is not None:
            temporary.cleanup()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mirror", type=Path, required=True)
    parser.add_argument("--live-repository-root", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True, help="JSON array of 1-3 exact submission paths")
    parser.add_argument("--submission-commit", required=True, help="full commit containing every explicit submission")
    parser.add_argument("--actors", type=Path, required=True)
    parser.add_argument("--capabilities", type=Path, required=True)
    parser.add_argument("--event-ids", type=Path, required=True)
    parser.add_argument("--custody-policy", type=Path, required=True)
    parser.add_argument("--recorded-at", required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply-synthetic", action="store_true")
    args = parser.parse_args(argv)
    try:
        boundary = SyntheticMirrorBoundary(args.mirror, live_repository_root=args.live_repository_root)
        submissions = boundary.load_inventory(args.inventory, args.submission_commit)
        run, result_root = run_synthetic(
            boundary,
            submissions,
            actors=args.actors,
            capabilities=args.capabilities,
            event_ids=args.event_ids,
            custody_policy=args.custody_policy,
            recorded_at=args.recorded_at,
            dry_run=args.dry_run,
        )
        print(f"notice: {NOTICE}")
        print(f"mode: {'DRY_RUN_EPHEMERAL' if args.dry_run else 'SYNTHETIC_MIRROR_APPLY'}")
        print(f"perimeter: mirror={boundary.root} submission_commit={args.submission_commit} explicit_submissions={len(submissions)} result_root={result_root}")
        print(format_acceptance_run(run), end="")
        return 0 if run.status == "PASS" else 1
    except (GateCBoundaryError, OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"notice: {NOTICE}")
        print("mode: BOUNDARY_REFUSAL")
        print(f"perimeter: mirror={args.mirror} inventory={args.inventory}")
        print("EXCEPTION: gate-c-boundary")
        print(f"GATE_C_BOUNDARY_INVALID\t$input\t{exc}")
        print("PASS proves: nothing; the requested boundary was refused")
        print("PASS does not prove: live readiness, research truth, or authorization")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
