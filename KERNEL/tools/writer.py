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
    POLICY_VERSION,
    SCHEMA_VERSION,
    WRITER_VERSION,
    Finding,
    canonical_bytes,
    sha256_hex,
    validate_command,
    validate_event,
    validate_receipt,
)
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

    if command["command_type"] == "RegisterQuestion":
        event_type = "QuestionRegistered"
        object_type = "QUESTION"
        object_id = command["payload"]["question_id"]
    elif command["command_type"] == "SubmitForecast":
        event_type = "ForecastSubmitted"
        object_type = "FORECAST"
        object_id = command["payload"]["forecast_id"]
    else:  # validate_command already fails closed; retained as a defensive boundary.
        raise ResultConstructionError([Finding("COMMAND_SCHEMA_INVALID", "unsupported command type")])

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
        "effective_at": None,
        "correlation_id": command["correlation_id"],
        "caused_by": command["caused_by"],
        "authority_mode": AUTHORITY_MODE,
        "native_refs": command["native_refs"],
        "evidence_refs": command["payload"].get("evidence_refs", []),
        "payload": command["payload"],
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
    """Atomic result storage rooted outside the repository's live KERNEL tree."""

    def __init__(
        self,
        root: str | Path,
        *,
        before_publish: Callable[[Path, Path], None] | None = None,
    ):
        self.root = Path(root).resolve()
        repository_root = REPOSITORY_ROOT.resolve()
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

    def publish(self, document: dict[str, Any]) -> Path:
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

        with self._acceptance_lock():
            inventory = self.store.inventory()
            if not inventory.valid:
                raise ResultConstructionError(inventory.findings)
            plan = plan_commands(submissions, inventory.planner_summaries())
            acceptance_pass = FixtureAcceptancePass(self, plan)
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
                reason_code="COMMAND_SCHEMA_INVALID",
                reason_detail=_finding_codes(validation.findings),
            )
        try:
            event = build_accepted_event(
                command,
                event_id=event_id,
                recorded_at=recorded_at,
                writer_id=self.writer_id,
                previous_event_id=previous_event_id,
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
        return FixtureAcceptanceLock(self.store.root.parent)


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
