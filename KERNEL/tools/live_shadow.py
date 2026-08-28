#!/usr/bin/env python3
"""The one explicit Gate C live-shadow interface, gated by an operator activation document.

This module is the only permitted path to live-shadow writes. It never weakens
the synthetic boundary: every other tool keeps its live-repository refusal, and
this tool writes nothing until a strict activation document — the operator's
exact half-open UTC window, command identities and exact file hashes, pinned
policy files, pinned event identifiers, and an exact repository-root binding —
validates completely against the real clock and the supplied root. Only then is
a live grant minted and the same acceptance path proven at Gate B / C6 runs.

Modes:
  --preflight        read-only full-perimeter dress check; writes nothing
  --apply            one operator-attended live-shadow acceptance pass
  --check-views      read-only reproduction check of the committed views
  --audit-additions  read-only additions-only history audit (window not required)

The tool never stages, commits, or pushes. After --apply it prints the exact
file paths an operator may stage explicitly.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from acceptance import AcceptanceRun, FixtureAcceptanceRunner, format_acceptance_run
from audit import verify_additions_only, verify_durable_results
from core import Finding, ID_PATTERNS, POLICY_VERSION, validate_command, validate_transition
from custody import TIMESTAMP_FORMAT, authorize_writer, load_custody, run_with_custody
from gate_c_boundary import SUBMISSION
from live_grant import LiveShadowGrant, _MINT_KEY  # noqa: F401  (mint key import is this module's exclusive door)
from native import FULL_SHA, SubprocessGitBoundary, normalized_repository_path, verify_native_references
from permissions import PermissionRegistry, authorize_command
from render import DEFAULT_EXCLUSIONS_RELPATH, load_projection_exclusions, render_views, write_views
from writer import FixtureResultStore


NOTICE = "SHADOW — NON-AUTHORITATIVE"
ACTIVATION_SCHEMA = "kernel.live-activation.1"
LIVE_MODE = "LIVE_SHADOW_PILOT"
REPOSITORY_IDENTITY = "williepowen-debug/Research-workspace"
SHA256_HEX = re.compile(r"^[0-9a-f]{64}$")
ACTIVATION_FIELDS = {
    "schema_version",
    "policy_version",
    "activation_id",
    "authorized_by",
    "authorization_ref",
    "mode",
    "repository_root",
    "repository",
    "source_commit",
    "window_start",
    "window_end",
    "revoked_at",
    "writer_id",
    "commands",
    "actors_path",
    "actors_sha256",
    "capabilities_path",
    "capabilities_sha256",
    "custody_policy_path",
    "custody_policy_sha256",
    "event_ids",
}
ACTIVATION_COMMAND_FIELDS = {"command_id", "path", "sha256"}


@dataclass(frozen=True)
class ActivationCommand:
    command_id: str
    path: str
    sha256: str


@dataclass(frozen=True)
class LiveActivation:
    activation_id: str
    authorization_ref: str
    repository_root: str
    source_commit: str
    window_start: dt.datetime
    window_end: dt.datetime
    revoked_at: dt.datetime | None
    writer_id: str
    commands: tuple[ActivationCommand, ...]
    actors_path: str
    actors_sha256: str
    capabilities_path: str
    capabilities_sha256: str
    custody_policy_path: str
    custody_policy_sha256: str
    event_ids: dict[str, str]


def _strict_timestamp(value: Any) -> dt.datetime:
    if not isinstance(value, str):
        raise TypeError("timestamp must be a string")
    parsed = dt.datetime.strptime(value, TIMESTAMP_FORMAT).replace(tzinfo=dt.timezone.utc)
    if parsed.strftime(TIMESTAMP_FORMAT) != value:
        raise ValueError("timestamp is not canonical")
    return parsed


def captured_utc_now() -> str:
    """One captured real-clock UTC instant; live modes never accept an injected time."""

    return dt.datetime.now(dt.timezone.utc).strftime(TIMESTAMP_FORMAT)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON member: {key}")
        value[key] = item
    return value


def _strict_json_bytes(data: bytes) -> Any:
    return json.loads(data.decode("utf-8"), object_pairs_hook=_unique_object)


def load_activation_document(document: Any) -> tuple[LiveActivation | None, list[Finding]]:
    findings: list[Finding] = []

    def invalid(message: str, location: str = "$activation") -> tuple[None, list[Finding]]:
        findings.append(Finding("LIVE_ACTIVATION_INVALID", message, location))
        return None, findings

    if not isinstance(document, dict) or set(document) != ACTIVATION_FIELDS:
        return invalid("activation fields are not exactly the registered set")
    if document["schema_version"] != ACTIVATION_SCHEMA:
        return invalid("unsupported activation schema_version", "$.schema_version")
    if document["policy_version"] != POLICY_VERSION:
        return invalid("unsupported activation policy_version", "$.policy_version")
    if document["authorized_by"] != "WILL":
        return invalid("activation must be authorized by WILL", "$.authorized_by")
    if document["mode"] != LIVE_MODE:
        return invalid("activation mode must be LIVE_SHADOW_PILOT", "$.mode")
    if document["repository"] != REPOSITORY_IDENTITY:
        return invalid("activation repository identity is not the approved repository", "$.repository")
    activation_id = document["activation_id"]
    if not isinstance(activation_id, str) or not activation_id.strip():
        return invalid("activation_id must be non-empty", "$.activation_id")
    authorization_ref = document["authorization_ref"]
    if not normalized_repository_path(authorization_ref):
        return invalid("authorization_ref must be a normalized repository-relative path", "$.authorization_ref")
    repository_root = document["repository_root"]
    if not isinstance(repository_root, str) or not Path(repository_root).is_absolute():
        return invalid("repository_root must be an absolute path string", "$.repository_root")
    source_commit = document["source_commit"]
    if not isinstance(source_commit, str) or not FULL_SHA.fullmatch(source_commit):
        return invalid("source_commit must be one full 40-hex commit SHA", "$.source_commit")
    writer_id = document["writer_id"]
    if not isinstance(writer_id, str) or not writer_id.strip():
        return invalid("writer_id must be non-empty", "$.writer_id")
    try:
        window_start = _strict_timestamp(document["window_start"])
        window_end = _strict_timestamp(document["window_end"])
        revoked_at = _strict_timestamp(document["revoked_at"]) if document["revoked_at"] is not None else None
    except (TypeError, ValueError):
        return invalid("window timestamps must be strict canonical UTC timestamps", "$.window_start")
    if window_start >= window_end:
        return invalid("window must be a non-empty half-open interval", "$.window_end")
    if revoked_at is not None and not (window_start <= revoked_at <= window_end):
        return invalid("revocation must fall within the activation window", "$.revoked_at")

    raw_commands = document["commands"]
    if not isinstance(raw_commands, list) or not 1 <= len(raw_commands) <= 3:
        return invalid("commands must name one to three exact submissions", "$.commands")
    commands: list[ActivationCommand] = []
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for index, entry in enumerate(raw_commands):
        location = f"$.commands[{index}]"
        if not isinstance(entry, dict) or set(entry) != ACTIVATION_COMMAND_FIELDS:
            return invalid("command entry fields are invalid", location)
        command_id = entry["command_id"]
        path = entry["path"]
        digest = entry["sha256"]
        if not isinstance(command_id, str) or not ID_PATTERNS["command_id"].fullmatch(command_id):
            return invalid("command_id is not a registered command identifier", f"{location}.command_id")
        if command_id in seen_ids:
            return invalid(f"duplicate command_id {command_id}", f"{location}.command_id")
        if not isinstance(path, str) or str(PurePosixPath(path)) != path or PurePosixPath(path).is_absolute():
            return invalid("path must be a canonical relative POSIX path", f"{location}.path")
        match = SUBMISSION.fullmatch(path)
        if match is None or match.group("command_id") != command_id:
            return invalid("path must be the exact owned submission path for its command_id", f"{location}.path")
        if path in seen_paths:
            return invalid(f"duplicate command path {path}", f"{location}.path")
        if not isinstance(digest, str) or not SHA256_HEX.fullmatch(digest):
            return invalid("sha256 must be 64 lowercase hex characters", f"{location}.sha256")
        seen_ids.add(command_id)
        seen_paths.add(path)
        commands.append(ActivationCommand(command_id, path, digest))

    for label in ("actors", "capabilities", "custody_policy"):
        path_value = document[f"{label}_path"]
        sha_value = document[f"{label}_sha256"]
        if not normalized_repository_path(path_value):
            return invalid(f"{label}_path must be a normalized repository-relative path", f"$.{label}_path")
        if not isinstance(sha_value, str) or not SHA256_HEX.fullmatch(sha_value):
            return invalid(f"{label}_sha256 must be 64 lowercase hex characters", f"$.{label}_sha256")

    event_ids = document["event_ids"]
    if not isinstance(event_ids, dict) or set(event_ids) != seen_ids:
        return invalid("event_ids must map exactly the activation command_ids", "$.event_ids")
    if any(
        not isinstance(value, str) or not ID_PATTERNS["event_id"].fullmatch(value)
        for value in event_ids.values()
    ) or len(set(event_ids.values())) != len(event_ids):
        return invalid("event_ids values must be unique registered event identifiers", "$.event_ids")

    activation = LiveActivation(
        activation_id=activation_id,
        authorization_ref=authorization_ref,
        repository_root=repository_root,
        source_commit=source_commit,
        window_start=window_start,
        window_end=window_end,
        revoked_at=revoked_at,
        writer_id=writer_id,
        commands=tuple(commands),
        actors_path=document["actors_path"],
        actors_sha256=document["actors_sha256"],
        capabilities_path=document["capabilities_path"],
        capabilities_sha256=document["capabilities_sha256"],
        custody_policy_path=document["custody_policy_path"],
        custody_policy_sha256=document["custody_policy_sha256"],
        event_ids=dict(event_ids),
    )
    return activation, findings


def authorize_live_activation(
    document: Any,
    *,
    live_repository_root: str | Path,
    now: str,
    require_window: bool = True,
) -> tuple[LiveShadowGrant | None, LiveActivation | None, list[Finding]]:
    """Validate the activation, the clock, and the root binding; mint the grant.

    Absence, expiry, mismatch, or ambiguity fails closed here — before any store,
    lock, or writer exists. Read-only modes may skip the window requirement; the
    minted grant records that choice as ``window_enforced``, and every durable
    write refuses a grant minted without window enforcement, so a caller that
    wrongly passes ``require_window=False`` on a write path is stopped by the
    store, not by this comment (adversarial review 2026-08-27, finding 1).
    """

    activation, findings = load_activation_document(document)
    if activation is None:
        return None, None, findings

    try:
        instant = _strict_timestamp(now)
    except (TypeError, ValueError):
        return None, None, [Finding("LIVE_WINDOW_REFUSED", "captured instant is not a canonical UTC timestamp", "$.now")]
    effective_end = activation.revoked_at if activation.revoked_at is not None else activation.window_end
    if require_window:
        if instant < activation.window_start:
            return None, None, [Finding(
                "LIVE_WINDOW_REFUSED",
                f"window has not started (now={now} start={activation.window_start.strftime(TIMESTAMP_FORMAT)})",
                "$.window_start",
            )]
        if instant >= effective_end:
            return None, None, [Finding(
                "LIVE_WINDOW_REFUSED",
                f"window is closed (now={now} end={effective_end.strftime(TIMESTAMP_FORMAT)})",
                "$.window_end",
            )]

    supplied = Path(live_repository_root).resolve()
    declared = Path(activation.repository_root).resolve()
    if supplied != declared:
        return None, activation, [Finding(
            "LIVE_BINDING_MISMATCH",
            f"supplied root {supplied} does not equal the activation repository_root {declared}",
            "$.repository_root",
        )]

    grant = LiveShadowGrant(
        _MINT_KEY,
        repository_root=supplied,
        activation_id=activation.activation_id,
        writer_id=activation.writer_id,
        recorded_at=now,
        window_enforced=require_window,
    )
    return grant, activation, []


def verify_pinned_file(root: Path, relative: str, expected_sha256: str) -> tuple[bytes | None, Finding | None]:
    target = (root / relative).resolve()
    if root != target and root not in target.parents:
        return None, Finding("LIVE_BINDING_MISMATCH", f"pinned path escapes the granted root: {relative}", relative)
    try:
        data = target.read_bytes()
    except OSError as exc:
        return None, Finding("LIVE_BINDING_MISMATCH", f"pinned file is unreadable: {exc}", relative)
    digest = hashlib.sha256(data).hexdigest()
    if digest != expected_sha256:
        return None, Finding(
            "LIVE_BINDING_MISMATCH",
            f"pinned file hash mismatch: expected {expected_sha256} observed {digest}",
            relative,
        )
    return data, None


def load_live_submissions(
    git: SubprocessGitBoundary,
    submission_commit: str,
    activation: LiveActivation,
) -> tuple[list[dict[str, Any]], dict[str, str], list[Finding]]:
    findings: list[Finding] = []
    if not isinstance(submission_commit, str) or not FULL_SHA.fullmatch(submission_commit) or git.resolve_commit(submission_commit) != submission_commit:
        return [], {}, [Finding("LIVE_BINDING_MISMATCH", "submission commit must be one existing full commit SHA", "$.submission_commit")]
    if git.resolve_commit(activation.source_commit) != activation.source_commit:
        return [], {}, [Finding("LIVE_BINDING_MISMATCH", "activation source_commit is absent from the bound repository", "$.source_commit")]
    commands: list[dict[str, Any]] = []
    paths: dict[str, str] = {}
    for pinned in activation.commands:
        blob = git.read_blob(submission_commit, pinned.path)
        if blob is None:
            findings.append(Finding("LIVE_BINDING_MISMATCH", f"submission is absent at the exact commit: {pinned.path}", pinned.path))
            continue
        digest = hashlib.sha256(blob).hexdigest()
        if digest != pinned.sha256:
            findings.append(Finding(
                "LIVE_BINDING_MISMATCH",
                f"submission bytes do not match the activation pin: expected {pinned.sha256} observed {digest}",
                pinned.path,
            ))
            continue
        try:
            command = _strict_json_bytes(blob)
        except (UnicodeError, ValueError) as exc:
            findings.append(Finding("LIVE_BINDING_MISMATCH", f"submission is not strict JSON: {exc}", pinned.path))
            continue
        if not isinstance(command, dict) or command.get("command_id") != pinned.command_id:
            findings.append(Finding("LIVE_BINDING_MISMATCH", "embedded command_id does not match the activation pin", pinned.path))
            continue
        match = SUBMISSION.fullmatch(pinned.path)
        if match is None or command.get("actor_id") != match.group("actor"):
            findings.append(Finding("LIVE_BINDING_MISMATCH", "submission path actor and actor_id do not agree", pinned.path))
            continue
        commands.append(command)
        paths[pinned.command_id] = pinned.path
    if findings:
        return [], {}, findings
    return commands, paths, []


class LiveGitHistoryBoundary:
    """Read the granted repository's history for the read-only additions audit."""

    def __init__(self, repository_root: Path):
        self.repository = Path(repository_root).resolve()

    def _run(self, *args: str) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            ["git", "-C", str(self.repository), *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )

    def resolve_commit(self, commit: str) -> str | None:
        if not isinstance(commit, str) or not FULL_SHA.fullmatch(commit):
            return None
        completed = self._run("rev-parse", "--verify", f"{commit}^{{commit}}")
        resolved = completed.stdout.strip().decode("ascii", errors="ignore")
        return resolved if completed.returncode == 0 and FULL_SHA.fullmatch(resolved) else None

    def is_ancestor(self, base: str, head: str) -> bool | None:
        completed = self._run("merge-base", "--is-ancestor", base, head)
        if completed.returncode == 0:
            return True
        if completed.returncode == 1:
            return False
        return None

    def commits_between(self, base: str, head: str) -> list[str] | None:
        completed = self._run("rev-list", "--reverse", "--topo-order", f"{base}..{head}")
        if completed.returncode != 0:
            return None
        commits = completed.stdout.decode("ascii", errors="ignore").splitlines()
        return commits if all(FULL_SHA.fullmatch(commit) for commit in commits) else None

    def commit_changes(self, commit: str) -> list[tuple[str, str]] | None:
        completed = self._run(
            "diff-tree", "--no-commit-id", "--name-status", "-z", "-r", "-m", "--no-renames", commit,
        )
        if completed.returncode != 0:
            return None
        fields = completed.stdout.split(b"\0")
        if fields and fields[-1] == b"":
            fields.pop()
        if len(fields) % 2:
            return None
        changes: list[tuple[str, str]] = []
        try:
            for index in range(0, len(fields), 2):
                changes.append((fields[index].decode("ascii"), fields[index + 1].decode("utf-8")))
        except UnicodeDecodeError:
            return None
        return changes


@dataclass
class LiveInputs:
    activation: LiveActivation
    grant: LiveShadowGrant
    git: SubprocessGitBoundary
    registry: PermissionRegistry
    custody_load: Any
    commands: list[dict[str, Any]]
    paths: dict[str, str]


class LiveRefusal(ValueError):
    def __init__(self, findings: list[Finding]):
        super().__init__("; ".join(f"{finding.code}: {finding.message}" for finding in findings))
        self.findings = findings


def prepare_live_inputs(
    *,
    activation_path: Path,
    live_repository_root: Path,
    submission_commit: str | None,
    custody_activation_path: Path | None,
    now: str,
    require_window: bool,
    load_submissions: bool,
) -> LiveInputs:
    try:
        document = _strict_json_bytes(Path(activation_path).read_bytes())
    except (OSError, UnicodeError, ValueError) as exc:
        raise LiveRefusal([Finding("LIVE_ACTIVATION_INVALID", f"activation document is unreadable: {exc}", str(activation_path))])
    grant, activation, findings = authorize_live_activation(
        document,
        live_repository_root=live_repository_root,
        now=now,
        require_window=require_window,
    )
    if grant is None or activation is None:
        raise LiveRefusal(findings)

    pinned: dict[str, bytes] = {}
    pin_findings: list[Finding] = []
    for label, relative, digest in (
        ("actors", activation.actors_path, activation.actors_sha256),
        ("capabilities", activation.capabilities_path, activation.capabilities_sha256),
        ("custody_policy", activation.custody_policy_path, activation.custody_policy_sha256),
    ):
        data, finding = verify_pinned_file(grant.repository_root, relative, digest)
        if finding is not None:
            pin_findings.append(finding)
        else:
            assert data is not None
            pinned[label] = data
    if pin_findings:
        raise LiveRefusal(pin_findings)

    try:
        actors_document = _strict_json_bytes(pinned["actors"])
        capabilities_document = _strict_json_bytes(pinned["capabilities"])
        custody_document = _strict_json_bytes(pinned["custody_policy"])
        custody_activation_document = (
            _strict_json_bytes(Path(custody_activation_path).read_bytes())
            if custody_activation_path is not None
            else None
        )
    except (OSError, UnicodeError, ValueError) as exc:
        raise LiveRefusal([Finding("LIVE_ACTIVATION_INVALID", f"pinned policy input is not strict JSON: {exc}", "$policies")])

    registry = PermissionRegistry.from_documents(actors_document, capabilities_document)
    if not registry.valid:
        raise LiveRefusal(list(registry.findings))
    custody_load = load_custody(custody_document, custody_activation_document)
    if not custody_load.valid:
        raise LiveRefusal(list(custody_load.findings))
    assert custody_load.policy is not None
    if activation.writer_id != custody_load.policy.primary_writer_id:
        raise LiveRefusal([Finding(
            "LIVE_BINDING_MISMATCH",
            "activation writer_id must be the custody policy primary writer",
            "$.writer_id",
        )])

    git = SubprocessGitBoundary(grant.repository_root)
    commands: list[dict[str, Any]] = []
    paths: dict[str, str] = {}
    if load_submissions:
        if submission_commit is None:
            raise LiveRefusal([Finding("LIVE_BINDING_MISMATCH", "submission commit is required for this mode", "$.submission_commit")])
        commands, paths, submission_findings = load_live_submissions(git, submission_commit, activation)
        if submission_findings:
            raise LiveRefusal(submission_findings)

    return LiveInputs(
        activation=activation,
        grant=grant,
        git=git,
        registry=registry,
        custody_load=custody_load,
        commands=commands,
        paths=paths,
    )


def run_live_apply(inputs: LiveInputs) -> tuple[AcceptanceRun, FixtureResultStore]:
    store = FixtureResultStore(inputs.grant.kernel_root, live_grant=inputs.grant)
    runner = FixtureAcceptanceRunner(
        store,
        writer_id=inputs.activation.writer_id,
        registry=inputs.registry,
        git=inputs.git,
        event_id_for=lambda command: inputs.activation.event_ids[command["command_id"]],
        recorded_at_for=lambda _command: inputs.grant.recorded_at,
    )
    run = run_with_custody(
        runner,
        inputs.custody_load,
        writer_id=inputs.activation.writer_id,
        recorded_at=inputs.grant.recorded_at,
        submissions=inputs.commands,
        submission_paths=inputs.paths,
    )
    return run, store


def _store_context(store: FixtureResultStore, commands: list[dict[str, Any]]):
    inventory = store.inventory()
    if not inventory.valid:
        raise LiveRefusal(list(inventory.findings))
    accepted = store.accepted_events()
    receipts = [
        stored.document
        for _command_id, stored in sorted(inventory.results.items())
        if stored.document["command_result"] == "REJECTED"
    ]
    unprocessed = [command for command in commands if command["command_id"] not in inventory.results]
    return accepted, receipts, unprocessed


def render_live_views(
    store: FixtureResultStore,
    grant: LiveShadowGrant,
    commands: list[dict[str, Any]],
    *,
    render_as_of: str,
    check: bool,
) -> tuple[dict[str, str], list[Finding]]:
    accepted, receipts, unprocessed = _store_context(store, commands)
    # Registered projection exclusions (2026-08-28): read from the activation's
    # declared repository root, validated fail-closed, joined to the digest.
    # Absent file = no exclusions; malformed file = LiveRefusal, never a render.
    exclusions_path = Path(grant.repository_root) / DEFAULT_EXCLUSIONS_RELPATH
    try:
        registry = load_projection_exclusions(exclusions_path)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise LiveRefusal([Finding("PROJECTION_EXCLUSIONS_INVALID", str(exc), str(exclusions_path))]) from exc
    views = render_views(accepted, render_as_of=render_as_of, context_inputs=receipts + unprocessed,
                         projection_exclusions=registry)
    findings = write_views(views, grant.views_root, check=check, live_grant=grant)
    return views, findings


def committed_render_as_of(views_root: Path) -> str:
    calibration = views_root / "CALIBRATION.tsv"
    try:
        for line in calibration.read_text(encoding="utf-8").splitlines():
            if line.startswith("# render_as_of: "):
                return line[len("# render_as_of: "):]
    except OSError as exc:
        raise LiveRefusal([Finding("LIVE_BINDING_MISMATCH", f"committed views are unreadable: {exc}", str(calibration))])
    raise LiveRefusal([Finding("LIVE_BINDING_MISMATCH", "committed CALIBRATION.tsv carries no render_as_of", str(calibration))])


def _print_refusal(mode: str, findings: list[Finding]) -> int:
    print(f"notice: {NOTICE}")
    print(f"mode: {mode}")
    print("EXCEPTION: live-shadow refusal — nothing was written")
    for finding in findings:
        print(f"{finding.code}\t{finding.location}\t{finding.message}")
    print("PASS proves: nothing; the requested live operation was refused before any write")
    print("PASS does not prove: live readiness, research truth, or authorization")
    return 1


def _print_banner(mode: str, inputs: LiveInputs, extra: str = "") -> None:
    activation = inputs.activation
    print(f"notice: {NOTICE}")
    print(f"mode: {mode}")
    print(
        "perimeter: "
        f"activation_id={activation.activation_id} authorized_by=WILL "
        f"authorization_ref={activation.authorization_ref} "
        f"repository_root={inputs.grant.repository_root} "
        f"window={activation.window_start.strftime(TIMESTAMP_FORMAT)}..{activation.window_end.strftime(TIMESTAMP_FORMAT)} "
        f"writer_id={activation.writer_id} commands={len(activation.commands)} "
        f"recorded_at={inputs.grant.recorded_at}{extra}"
    )


def _preflight(inputs: LiveInputs) -> int:
    _print_banner("LIVE_SHADOW_PREFLIGHT", inputs)
    store = FixtureResultStore(inputs.grant.kernel_root, live_grant=inputs.grant)
    inventory = store.inventory()
    if not inventory.valid:
        for finding in inventory.findings:
            print(f"EXCEPTION: store-inventory {finding.code}\t{finding.location}\t{finding.message}")
        return 1
    failed = False
    history = store.accepted_events()
    for command in inputs.commands:
        command_id = command["command_id"]
        path = inputs.paths[command_id]
        checks: list[tuple[str, Any]] = [
            ("custody", authorize_writer(inputs.custody_load, inputs.activation.writer_id, command_id, inputs.grant.recorded_at)),
            ("schema", validate_command(command)),
            ("permissions", authorize_command(command, path, inputs.registry)),
            ("native-reference", verify_native_references(command, inputs.git)),
        ]
        dependencies = command.get("depends_on", [])
        satisfied = all(dependency in inventory.results for dependency in dependencies)
        if satisfied:
            checks.append(("lifecycle", validate_transition(command, history)))
        else:
            print(f"perimeter: check=lifecycle command_id={command_id} preflight=deferred_pending_dependency")
        for name, result in checks:
            status = "PASS" if result.valid else "EXCEPTION"
            print(f"perimeter: check={name} command_id={command_id} preflight=read_only")
            print(f"{status}: {name}")
            for finding in result.findings:
                print(f"{finding.code}\t{finding.location}\t{finding.message}")
            if not result.valid:
                failed = True
    print("preflight-writes: 0 (read-only mode wrote nothing)")
    print("PASS proves: every read-only preflight check passed for the printed perimeter")
    print("PASS does not prove: acceptance, durable results, or state outside this perimeter")
    return 1 if failed else 0


def _apply(inputs: LiveInputs) -> int:
    _print_banner("LIVE_SHADOW_APPLY", inputs)
    run, store = run_live_apply(inputs)
    print(format_acceptance_run(run), end="")

    written: list[Path] = []
    for outcome in run.outcomes.values():
        if outcome.state == "WRITTEN" and outcome.path is not None:
            written.append(outcome.path)

    all_durable = not run.waiting and len(run.outcomes) == len(inputs.commands) and len(inputs.commands) > 0
    view_paths: list[Path] = []
    if all_durable:
        views, findings = render_live_views(
            store, inputs.grant, inputs.commands, render_as_of=inputs.grant.recorded_at, check=False,
        )
        for finding in findings:
            print(f"EXCEPTION: view {finding.code}\t{finding.location}\t{finding.message}")
        if not findings:
            for name in sorted(views):
                path = inputs.grant.views_root / name
                digest = hashlib.sha256(views[name].encode("utf-8")).hexdigest()
                print(f"view: {path} sha256={digest}")
                view_paths.append(path)
    else:
        print("views: not rendered — a selected command has no durable result")

    summaries = []
    inventory = store.inventory()
    if inventory.valid:
        summaries = [
            {
                "command_id": command_id,
                "command_result": stored.document["command_result"],
                "reason_code": stored.document.get("reason_code"),
            }
            for command_id, stored in sorted(inventory.results.items())
            if any(command["command_id"] == command_id for command in inputs.commands)
        ]
    durable = verify_durable_results(inputs.commands, summaries, pass_reported_success=all_durable)
    print(f"perimeter: check={durable.name} {durable.perimeter}")
    print(f"{durable.status}: durable-results")
    for finding in durable.findings + durable.unknowns:
        print(f"{finding.code}\t{finding.location}\t{finding.message}")

    if written or view_paths:
        print("operator-staging: this tool never runs git write commands; stage explicitly, path by path:")
        for path in written + view_paths:
            try:
                relative = path.resolve().relative_to(inputs.grant.repository_root)
            except ValueError:
                relative = path
            print(f"  git add {relative}")

    success = run.status == "PASS" and durable.status == "PASS" and all_durable
    return 0 if success else 1


def _check_views(inputs: LiveInputs) -> int:
    _print_banner("LIVE_SHADOW_CHECK_VIEWS", inputs)
    store = FixtureResultStore(inputs.grant.kernel_root, live_grant=inputs.grant)
    render_as_of = committed_render_as_of(inputs.grant.views_root)
    _views, findings = render_live_views(
        store, inputs.grant, inputs.commands, render_as_of=render_as_of, check=True,
    )
    print(
        f"perimeter: check=view-reproduction views_root={inputs.grant.views_root} "
        f"render_as_of={render_as_of} commands={len(inputs.commands)}"
    )
    for finding in findings:
        print(f"{finding.code}\t{finding.location}\t{finding.message}")
    status = "PASS" if not findings else "EXCEPTION"
    print(f"{status}: view-reproduction")
    print("PASS proves: committed registered views equal deterministic renderer output for the stored events")
    print("PASS does not prove: coverage of unregistered repository state or research truth")
    return 0 if not findings else 1


def _audit_additions(inputs: LiveInputs, base: str, head: str) -> int:
    _print_banner("LIVE_SHADOW_AUDIT_ADDITIONS", inputs, extra=f" history={base}..{head}")
    check = verify_additions_only(LiveGitHistoryBoundary(inputs.grant.repository_root), base, head)
    print(f"perimeter: check={check.name} repository={inputs.grant.repository_root} {check.perimeter}")
    print(f"{check.status}: additions-only")
    for finding in check.findings + check.unknowns:
        print(f"{finding.code}\t{finding.location}\t{finding.message}")
    print("PASS proves: protected accepted-event and receipt paths contain additions only in the compared history")
    print("PASS does not prove: protection outside the compared range or against the excluded threat model")
    return 0 if check.status == "PASS" else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--activation", type=Path, required=True)
    parser.add_argument("--live-repository-root", type=Path, required=True)
    parser.add_argument("--submission-commit")
    parser.add_argument("--custody-activation", type=Path)
    parser.add_argument("--base", help="additions audit base commit")
    parser.add_argument("--head", help="additions audit head commit")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check-views", action="store_true")
    mode.add_argument("--audit-additions", action="store_true")
    args = parser.parse_args(argv)

    mode_name = (
        "LIVE_SHADOW_PREFLIGHT" if args.preflight
        else "LIVE_SHADOW_APPLY" if args.apply
        else "LIVE_SHADOW_CHECK_VIEWS" if args.check_views
        else "LIVE_SHADOW_AUDIT_ADDITIONS"
    )
    write_capable = args.apply
    now = captured_utc_now()
    try:
        inputs = prepare_live_inputs(
            activation_path=args.activation,
            live_repository_root=args.live_repository_root,
            submission_commit=args.submission_commit,
            custody_activation_path=args.custody_activation,
            now=now,
            require_window=write_capable or args.preflight,
            load_submissions=True,
        )
        if args.preflight:
            return _preflight(inputs)
        if args.apply:
            return _apply(inputs)
        if args.check_views:
            return _check_views(inputs)
        if not args.base or not args.head:
            raise LiveRefusal([Finding("LIVE_BINDING_MISMATCH", "--audit-additions requires --base and --head", "$history")])
        return _audit_additions(inputs, args.base, args.head)
    except LiveRefusal as exc:
        return _print_refusal(mode_name, exc.findings)
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        return _print_refusal(mode_name, [Finding("LIVE_ACTIVATION_INVALID", str(exc), "$input")])


if __name__ == "__main__":
    raise SystemExit(main())
