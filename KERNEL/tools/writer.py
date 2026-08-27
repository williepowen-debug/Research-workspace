"""Fixture-only atomic result construction, publication, and idempotent lookup."""

from __future__ import annotations

import json
import os
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable, Iterator

from core import (
    AUTHORITY_MODE,
    COMMAND_EVENT_TYPES,
    POLICY_VERSION,
    REJECTION_REASONS,
    SCHEMA_VERSION,
    WRITER_VERSION,
    Finding,
    canonical_bytes,
    sha256_hex,
    validate_command,
    validate_event,
    validate_receipt,
    validate_transition,
)
from live_grant import LiveShadowGrant, require_live_grant
from locking import FixtureAcceptanceLock
from planner import DependencyPlan, plan_commands


LIVE_KERNEL_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = LIVE_KERNEL_ROOT.parent


class ResultConstructionError(ValueError):
    def __init__(self, findings: list[Finding]):
        super().__init__("; ".join(f"{finding.code}: {finding.message}" for finding in findings))
        self.findings = findings


@dataclass(frozen=True)
class StoredResult:
    path: Path
    document: dict[str, Any]


@dataclass
class StoreInventory:
    results: dict[str, StoredResult] = field(default_factory=dict)
    findings: list[Finding] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return not self.findings

    def planner_summaries(self) -> list[dict[str, Any]]:
        if not self.valid:
            raise ResultConstructionError(self.findings)
        return [
            {
                "command_id": command_id,
                "command_result": stored.document["command_result"],
                "reason_code": stored.document.get("reason_code"),
            }
            for command_id, stored in sorted(self.results.items())
        ]


@dataclass(frozen=True)
class WriteOutcome:
    state: str
    document: dict[str, Any] | None = None
    path: Path | None = None
    finding: Finding | None = None


@dataclass
class FixtureAcceptancePass:
    """One inventory→plan→write session protected by the local fixture lock."""

    writer: "FixtureResultWriter"
    plan: DependencyPlan
    submissions: tuple[dict[str, Any], ...]
    _active: bool = True

    def accept(
        self,
        command: dict[str, Any],
        *,
        event_id: str,
        recorded_at: str,
        previous_event_id: str | None = None,
    ) -> WriteOutcome:
        self._require_active()
        next_ready = self.plan.ready[0]["command_id"] if self.plan.ready else None
        if command.get("command_id") != next_ready:
            raise RuntimeError("fixture command is not next in the current dependency plan")
        return self.writer._accept_locked(
            command,
            event_id=event_id,
            recorded_at=recorded_at,
            previous_event_id=previous_event_id,
        )

    def reject(
        self,
        command: dict[str, Any],
        *,
        recorded_at: str,
        reason_code: str,
        reason_detail: str,
    ) -> WriteOutcome:
        self._require_active()
        return self.writer._reject_locked(
            command,
            recorded_at=recorded_at,
            reason_code=reason_code,
            reason_detail=reason_detail,
        )

    def prior(self, command: dict[str, Any]) -> WriteOutcome | None:
        """Return the matching prior result or an idempotency failure under lock."""

        self._require_active()
        return self.writer._prior_outcome(command)

    def refresh(self) -> DependencyPlan:
        """Re-inventory and re-plan while the same acceptance lock remains held."""

        self._require_active()
        inventory = self.writer.store.inventory()
        if not inventory.valid:
            raise ResultConstructionError(inventory.findings)
        self.plan = plan_commands(self.submissions, inventory.planner_summaries())
        return self.plan

    def _require_active(self) -> None:
        if not self._active:
            raise RuntimeError("fixture acceptance pass is no longer lock-protected")


def build_accepted_event(
    command: dict[str, Any],
    *,
    event_id: str,
    recorded_at: str,
    writer_id: str,
    previous_event_id: str | None = None,
) -> dict[str, Any]:
    validation = validate_command(command)
    if not validation.valid:
        raise ResultConstructionError(
            [Finding("COMMAND_SCHEMA_INVALID", _finding_codes(validation.findings))]
        )

    command_type = command["command_type"]
    payload = command["payload"]
    event_type = COMMAND_EVENT_TYPES.get(command_type)
    if event_type is None:  # validate_command already fails closed; retained as a defensive boundary.
        raise ResultConstructionError([Finding("COMMAND_SCHEMA_INVALID", "unsupported command type")])
    if command_type in {"RegisterQuestion", "CloseQuestion", "AnnulQuestion"}:
        object_type = "QUESTION"
        object_id = payload["question_id"]
    elif command_type in {"SubmitForecast", "AmendForecast", "WithdrawForecast"}:
        object_type = "FORECAST"
        object_id = payload["forecast_id"]
    else:
        object_type = "RESOLUTION"
        object_id = payload["resolution_id"]

    event = {
        "schema_version": SCHEMA_VERSION,
        "policy_version": POLICY_VERSION,
        "writer_version": WRITER_VERSION,
        "event_id": event_id,
        "event_type": event_type,
        "command_id": command["command_id"],
        "command_hash": _command_hash(command),
        "command_result": "ACCEPTED",
        "stream_id": command["target_stream_id"],
        "stream_version": command["expected_version"] + 1,
        "previous_event_id": previous_event_id,
        "object_id": object_id,
        "object_type": object_type,
        "actor_id": command["actor_id"],
        "writer_id": writer_id,
        "submitted_at": command["submitted_at"],
        "recorded_at": recorded_at,
        "effective_at": payload.get("closed_at") if command_type == "CloseQuestion" else None,
        "correlation_id": command["correlation_id"],
        "caused_by": command["caused_by"],
        "authority_mode": AUTHORITY_MODE,
        "native_refs": command["native_refs"],
        "evidence_refs": _event_evidence_refs(command_type, payload),
        "payload": payload,
    }
    event_validation = validate_event(event)
    if not event_validation.valid:
        raise ResultConstructionError(event_validation.findings)
    return event


def build_rejected_receipt(
    command: dict[str, Any],
    *,
    recorded_at: str,
    writer_id: str,
    reason_code: str,
    reason_detail: str,
) -> dict[str, Any]:
    required_transport = {
        "command_id",
        "actor_id",
        "submitted_at",
        "target_stream_id",
        "expected_version",
    }
    missing = sorted(required_transport - command.keys())
    if missing:
        raise ResultConstructionError(
            [Finding("COMMAND_SCHEMA_INVALID", f"receipt transport fields missing: {', '.join(missing)}")]
        )
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "policy_version": POLICY_VERSION,
        "writer_version": WRITER_VERSION,
        "command_id": command["command_id"],
        "command_hash": _command_hash(command),
        "command_result": "REJECTED",
        "actor_id": command["actor_id"],
        "writer_id": writer_id,
        "submitted_at": command["submitted_at"],
        "recorded_at": recorded_at,
        "reason_code": reason_code,
        "reason_detail": reason_detail,
        "target_stream_id": command["target_stream_id"],
        "expected_version": command["expected_version"],
        "native_refs": command.get("native_refs", []),
    }
    receipt_validation = validate_receipt(receipt)
    if not receipt_validation.valid:
        raise ResultConstructionError(receipt_validation.findings)
    return receipt


class FixtureResultStore:
    """Atomic result storage rooted outside the repository's live KERNEL tree.

    Without a minted live grant the store refuses the live repository tree;
    with one it requires exactly the granted ``KERNEL`` root and nothing else.
    """

    def __init__(
        self,
        root: str | Path,
        *,
        before_publish: Callable[[Path, Path], None] | None = None,
        forbidden_repository_root: str | Path | None = None,
        live_grant: LiveShadowGrant | None = None,
    ):
        self.root = Path(root).resolve()
        if live_grant is not None:
            if forbidden_repository_root is not None:
                raise ValueError("live_grant and forbidden_repository_root are mutually exclusive")
            self.live_grant: LiveShadowGrant | None = require_live_grant(live_grant)
            self.forbidden_repository_root: Path | None = None
            if self.root != self.live_grant.kernel_root:
                raise ValueError("live result store must target exactly the granted KERNEL root")
        else:
            self.live_grant = None
            repository_root = Path(forbidden_repository_root or REPOSITORY_ROOT).resolve()
            self.forbidden_repository_root = repository_root
            if self.root == repository_root or repository_root in self.root.parents:
                raise ValueError("fixture result store cannot target the live repository tree")
        self.before_publish = before_publish

    def inventory(self) -> StoreInventory:
        inventory = StoreInventory()
        grouped: dict[str, list[StoredResult]] = {}
        paths = sorted(self.root.glob("shadow/events/**/*.json"))
        paths.extend(sorted(self.root.glob("audit/commands/**/*.json")))
        for path in paths:
            try:
                document = json.loads(
                    path.read_text(encoding="utf-8"),
                    object_pairs_hook=_unique_object,
                    parse_constant=_reject_constant,
                )
            except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
                inventory.findings.append(Finding("RESULT_INVENTORY_INVALID", str(exc), str(path)))
                continue
            validation = _validate_result_document(document)
            if not validation.valid:
                inventory.findings.append(
                    Finding(
                        "RESULT_INVENTORY_INVALID",
                        _finding_codes(validation.findings),
                        str(path),
                    )
                )
                continue
            command_id = document["command_id"]
            grouped.setdefault(command_id, []).append(StoredResult(path, document))

        for command_id in sorted(grouped):
            candidates = grouped[command_id]
            if len(candidates) != 1:
                inventory.findings.append(Finding("AUDIT_DUPLICATE_RESULT", command_id, str(self.root)))
                continue
            inventory.results[command_id] = candidates[0]
        inventory.findings.sort(key=lambda finding: (finding.code, finding.message, finding.location))
        return inventory

    def lookup(self, command_id: str) -> tuple[StoredResult | None, list[Finding]]:
        inventory = self.inventory()
        if not inventory.valid:
            return None, inventory.findings
        return inventory.results.get(command_id), []

    def accepted_events(self) -> list[dict[str, Any]]:
        inventory = self.inventory()
        if not inventory.valid:
            raise ResultConstructionError(inventory.findings)
        events = [
            stored.document
            for stored in inventory.results.values()
            if stored.document["command_result"] == "ACCEPTED"
        ]
        return sorted(events, key=lambda event: (event["stream_id"], event["stream_version"], event["event_id"]))

    def publish(self, document: dict[str, Any]) -> Path:
        if self.live_grant is not None and not self.live_grant.window_enforced:
            raise ValueError(
                "live grant was minted without window enforcement; durable writes refuse it"
            )
        validation = _validate_result_document(document)
        if not validation.valid:
            raise ResultConstructionError(validation.findings)
        destination = self._destination(document)
        if destination.exists():
            raise FileExistsError(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        payload = canonical_bytes(document) + b"\n"
        descriptor, temporary_name = tempfile.mkstemp(prefix=".tmp-", dir=destination.parent)
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            if self.before_publish is not None:
                self.before_publish(temporary, destination)
            if destination.exists():
                raise FileExistsError(destination)
            _fsync_directory(destination.parent)
            os.replace(temporary, destination)
            _fsync_directory(destination.parent)
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
        return destination

    def _destination(self, document: dict[str, Any]) -> Path:
        year = document["recorded_at"][:4]
        month = document["recorded_at"][5:7]
        if document["command_result"] == "ACCEPTED":
            return self.root / "shadow" / "events" / year / month / f"{document['event_id']}.json"
        return self.root / "audit" / "commands" / year / month / f"{document['command_id']}.json"


class FixtureResultWriter:
    """Fixture writer with local serialization and no policy authority."""

    def __init__(self, store: FixtureResultStore, *, writer_id: str):
        if not writer_id:
            raise ValueError("writer_id must be non-empty")
        self.store = store
        self.writer_id = writer_id

    @contextmanager
    def acceptance_pass(
        self,
        submissions: Iterable[dict[str, Any]],
    ) -> Iterator[FixtureAcceptancePass]:
        """Hold the lock across durable inventory, dependency planning, and writes."""

        supplied = tuple(submissions)
        with self._acceptance_lock():
            inventory = self.store.inventory()
            if not inventory.valid:
                raise ResultConstructionError(inventory.findings)
            plan = plan_commands(supplied, inventory.planner_summaries())
            acceptance_pass = FixtureAcceptancePass(self, plan, supplied)
            try:
                yield acceptance_pass
            finally:
                acceptance_pass._active = False

    def accept(
        self,
        command: dict[str, Any],
        *,
        event_id: str,
        recorded_at: str,
        previous_event_id: str | None = None,
    ) -> WriteOutcome:
        with self._acceptance_lock():
            return self._accept_locked(
                command,
                event_id=event_id,
                recorded_at=recorded_at,
                previous_event_id=previous_event_id,
            )

    def _accept_locked(
        self,
        command: dict[str, Any],
        *,
        event_id: str,
        recorded_at: str,
        previous_event_id: str | None = None,
    ) -> WriteOutcome:
        prior = self._prior_outcome(command)
        if prior is not None:
            return prior
        validation = validate_command(command)
        if not validation.valid:
            return self._reject_locked(
                command,
                recorded_at=recorded_at,
                reason_code=_rejection_reason(validation.findings, "COMMAND_SCHEMA_INVALID"),
                reason_detail=_finding_codes(validation.findings),
            )
        try:
            history = self.store.accepted_events()
        except ResultConstructionError as exc:
            return WriteOutcome("BLOCKED", finding=exc.findings[0])
        transition = validate_transition(command, history)
        if not transition.valid:
            return self._reject_locked(
                command,
                recorded_at=recorded_at,
                reason_code=_rejection_reason(transition.findings, "TRANSITION_FORBIDDEN"),
                reason_detail=_finding_codes(transition.findings),
            )
        target_history = [event for event in history if event["stream_id"] == command["target_stream_id"]]
        inferred_previous = target_history[-1]["event_id"] if target_history else None
        if previous_event_id is not None and previous_event_id != inferred_previous:
            return self._reject_locked(
                command,
                recorded_at=recorded_at,
                reason_code="STALE_EXPECTED_VERSION",
                reason_detail="previous_event_id does not match the replayed stream head",
            )
        try:
            event = build_accepted_event(
                command,
                event_id=event_id,
                recorded_at=recorded_at,
                writer_id=self.writer_id,
                previous_event_id=inferred_previous,
            )
            path = self.store.publish(event)
        except FileExistsError:
            return self._reject_locked(
                command,
                recorded_at=recorded_at,
                reason_code="IDENTIFIER_COLLISION",
                reason_detail=f"event destination already exists for {event_id}",
            )
        except ResultConstructionError as exc:
            return WriteOutcome("BLOCKED", finding=exc.findings[0])
        return WriteOutcome("WRITTEN", event, path)

    def reject(
        self,
        command: dict[str, Any],
        *,
        recorded_at: str,
        reason_code: str,
        reason_detail: str,
    ) -> WriteOutcome:
        with self._acceptance_lock():
            return self._reject_locked(
                command,
                recorded_at=recorded_at,
                reason_code=reason_code,
                reason_detail=reason_detail,
            )

    def _reject_locked(
        self,
        command: dict[str, Any],
        *,
        recorded_at: str,
        reason_code: str,
        reason_detail: str,
    ) -> WriteOutcome:
        prior = self._prior_outcome(command)
        if prior is not None:
            return prior
        try:
            receipt = build_rejected_receipt(
                command,
                recorded_at=recorded_at,
                writer_id=self.writer_id,
                reason_code=reason_code,
                reason_detail=reason_detail,
            )
            path = self.store.publish(receipt)
        except FileExistsError:
            return WriteOutcome(
                "BLOCKED",
                finding=Finding("IDENTIFIER_COLLISION", f"receipt destination exists for {command.get('command_id')}"),
            )
        except ResultConstructionError as exc:
            return WriteOutcome("BLOCKED", finding=exc.findings[0])
        return WriteOutcome("WRITTEN", receipt, path)

    def _prior_outcome(self, command: dict[str, Any]) -> WriteOutcome | None:
        try:
            command_hash = _command_hash(command)
        except ResultConstructionError as exc:
            return WriteOutcome("BLOCKED", finding=exc.findings[0])
        stored, findings = self.store.lookup(command.get("command_id", ""))
        if findings:
            return WriteOutcome("BLOCKED", finding=findings[0])
        if stored is None:
            return None
        if stored.document["command_hash"] == command_hash:
            return WriteOutcome("EXISTING", stored.document, stored.path)
        return WriteOutcome(
            "REJECTED",
            stored.document,
            stored.path,
            Finding("IDEMPOTENCY_KEY_REUSED", f"command_id {command.get('command_id')} has different bytes"),
        )

    def _acceptance_lock(self) -> FixtureAcceptanceLock:
        if self.store.live_grant is not None:
            return FixtureAcceptanceLock(
                self.store.root.parent,
                live_grant=self.store.live_grant,
            )
        return FixtureAcceptanceLock(
            self.store.root.parent,
            forbidden_repository_root=self.store.forbidden_repository_root,
        )


def _validate_result_document(document: Any):
    if isinstance(document, dict) and document.get("command_result") == "ACCEPTED":
        return validate_event(document)
    return validate_receipt(document)


def _command_hash(command: Any) -> str:
    try:
        return sha256_hex(command)
    except (TypeError, ValueError, UnicodeError) as exc:
        raise ResultConstructionError([Finding("COMMAND_SCHEMA_INVALID", str(exc))]) from exc


def _finding_codes(findings: list[Finding]) -> str:
    return ",".join(sorted({finding.code for finding in findings}))


def _rejection_reason(findings: list[Finding], fallback: str) -> str:
    preferred = (
        "EVIDENCE_REQUIRED",
        "PROTECTED_SELF_VERIFICATION",
        "PERMISSION_DENIED",
        "STALE_EXPECTED_VERSION",
        "QUESTION_NOT_OPEN",
        "TRANSITION_FORBIDDEN",
        "FAMILY_NOT_ENABLED",
        "INVALID_INFORMATION_CUTOFF",
        "INVALID_TIMESTAMP",
        "NATIVE_PATH_INVALID",
    )
    codes = {finding.code for finding in findings}
    for code in preferred:
        if code in codes and code in REJECTION_REASONS:
            return code
    return fallback


def _event_evidence_refs(command_type: str, payload: dict[str, Any]) -> list[Any]:
    field_by_command = {
        "SubmitForecast": "evidence_refs",
        "AmendForecast": "evidence_refs",
        "ProposeResolution": "resolution_evidence_refs",
        "VerifyResolution": "verification_evidence_refs",
        "DisputeResolution": "dispute_evidence_refs",
        "CorrectResolution": "correction_evidence_refs",
    }
    field_name = field_by_command.get(command_type)
    return list(payload[field_name]) if field_name is not None else []


def _fsync_directory(path: Path) -> None:
    directory_descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(directory_descriptor)
    finally:
        os.close(directory_descriptor)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON member: {key}")
        value[key] = item
    return value


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-standard JSON constant: {value}")
