"""Fixture-only actor registry and deterministic Kernel permission checks."""

from __future__ import annotations

import datetime as dt
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from core import POLICY_VERSION, SCHEMA_VERSION, Finding, ValidationResult, validate_command


ACTOR_REGISTRY_FIELDS = {"schema_version", "actors"}
ACTOR_FIELDS = {
    "actor_id",
    "actor_type",
    "canonical_name",
    "source_ref",
    "active_from",
    "active_until",
}
CAPABILITY_REGISTRY_FIELDS = {"policy_version", "grants"}
GRANT_FIELDS = {"actor_id", "capabilities"}

CAPABILITIES = {
    "question.register",
    "question.close_own",
    "forecast.submit_own",
    "forecast.amend_own",
    "resolution.propose",
    "resolution.verify",
    "resolution.dispute",
    "resolution.correct",
    "question.annul_own",
    "forecast.withdraw_own",
    "command.accept",
    "policy.override",
}

COMMAND_PERMISSIONS = {
    "RegisterQuestion": ("question.register", "owner_actor_id"),
    "SubmitForecast": ("forecast.submit_own", "forecaster_actor_id"),
}

COMMAND_ACTOR_REFERENCES = {
    "RegisterQuestion": (
        "owner_actor_id",
        "resolver_actor_id",
        "independent_verifier_actor_id",
    ),
    "SubmitForecast": ("forecaster_actor_id",),
}

TIMESTAMP_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z")


@dataclass(frozen=True)
class ActorRecord:
    actor_id: str
    actor_type: str
    canonical_name: str
    source_ref: str
    active_from: dt.datetime
    active_until: dt.datetime | None


@dataclass
class PermissionRegistry:
    actors: dict[str, ActorRecord] = field(default_factory=dict)
    capabilities: dict[str, frozenset[str]] = field(default_factory=dict)
    findings: list[Finding] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return not self.findings

    @classmethod
    def from_documents(cls, actor_document: Any, capability_document: Any) -> "PermissionRegistry":
        findings: list[Finding] = []
        actors: dict[str, ActorRecord] = {}
        canonical_names: set[str] = set()

        if not _has_exact_fields(actor_document, ACTOR_REGISTRY_FIELDS):
            findings.append(Finding("ACTOR_REGISTRY_INVALID", "actor registry envelope is invalid"))
        elif actor_document["schema_version"] != SCHEMA_VERSION:
            findings.append(Finding("ACTOR_REGISTRY_INVALID", "unsupported actor registry schema_version", "$.schema_version"))
        elif not isinstance(actor_document["actors"], list):
            findings.append(Finding("ACTOR_REGISTRY_INVALID", "actors must be an array", "$.actors"))
        else:
            for index, value in enumerate(actor_document["actors"]):
                location = f"$.actors[{index}]"
                record = _actor_record(value, location, findings)
                if record is None:
                    continue
                if record.actor_id in actors:
                    findings.append(Finding("ACTOR_REGISTRY_INVALID", f"duplicate actor_id {record.actor_id}", location))
                    continue
                if record.canonical_name in canonical_names:
                    findings.append(
                        Finding("ACTOR_REGISTRY_INVALID", f"duplicate canonical_name {record.canonical_name}", location)
                    )
                    continue
                actors[record.actor_id] = record
                canonical_names.add(record.canonical_name)

        capabilities: dict[str, frozenset[str]] = {}
        if not _has_exact_fields(capability_document, CAPABILITY_REGISTRY_FIELDS):
            findings.append(Finding("CAPABILITY_REGISTRY_INVALID", "capability registry envelope is invalid"))
        elif capability_document["policy_version"] != POLICY_VERSION:
            findings.append(
                Finding("CAPABILITY_REGISTRY_INVALID", "unsupported capability policy_version", "$.policy_version")
            )
        elif not isinstance(capability_document["grants"], list):
            findings.append(Finding("CAPABILITY_REGISTRY_INVALID", "grants must be an array", "$.grants"))
        else:
            for index, value in enumerate(capability_document["grants"]):
                location = f"$.grants[{index}]"
                grant = _capability_grant(value, location, findings)
                if grant is None:
                    continue
                actor_id, actor_capabilities = grant
                if actor_id in capabilities:
                    findings.append(Finding("CAPABILITY_REGISTRY_INVALID", f"duplicate grant for {actor_id}", location))
                    continue
                if actor_id not in actors:
                    findings.append(Finding("CAPABILITY_REGISTRY_INVALID", f"unknown actor_id {actor_id}", location))
                    continue
                capabilities[actor_id] = frozenset(actor_capabilities)

        return cls(actors=actors, capabilities=capabilities, findings=findings)

    @classmethod
    def from_files(cls, actor_path: str | Path, capability_path: str | Path) -> "PermissionRegistry":
        findings: list[Finding] = []
        documents: list[Any] = []
        for label, path in (("actor", actor_path), ("capability", capability_path)):
            try:
                documents.append(json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=_unique_object))
            except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
                findings.append(Finding(f"{label.upper()}_REGISTRY_INVALID", str(exc), str(path)))
                documents.append({})
        if findings:
            return cls(findings=findings)
        return cls.from_documents(documents[0], documents[1])


def authorize_command(command: Any, submission_path: str, registry: PermissionRegistry) -> ValidationResult:
    """Authorize one already-submitted command without reading or writing repository state."""

    result = ValidationResult()
    command_validation = validate_command(command)
    if not command_validation.valid:
        result.add("COMMAND_SCHEMA_INVALID", "command must pass contract validation before authorization")
        return result
    if not registry.valid:
        result.add("PERMISSION_DENIED", "permission registry is invalid")
        return result

    actor_id = command["actor_id"]
    actor = registry.actors.get(actor_id)
    if actor is None:
        result.add("PERMISSION_DENIED", f"actor_id {actor_id} is not registered", "$.actor_id")
        return result

    submitted_at = _parse_timestamp(command["submitted_at"])
    if submitted_at < actor.active_from or (actor.active_until is not None and submitted_at >= actor.active_until):
        result.add("PERMISSION_DENIED", f"actor_id {actor_id} is inactive at submitted_at", "$.submitted_at")

    expected_path = (
        f"AGENTS/{actor.canonical_name}/outbox/kernel/submissions/"
        f"{command['command_id']}.json"
    )
    if submission_path != expected_path:
        result.add(
            "ACTOR_PATH_MISMATCH",
            f"submission path must be {expected_path}",
            "$submission_path",
        )

    required_capability, ownership_field = COMMAND_PERMISSIONS[command["command_type"]]
    if required_capability not in registry.capabilities.get(actor_id, frozenset()):
        result.add(
            "PERMISSION_DENIED",
            f"actor_id {actor_id} lacks {required_capability}",
            "$.actor_id",
        )

    payload = command["payload"]
    if payload[ownership_field] != actor_id:
        result.add(
            "PERMISSION_DENIED",
            f"{ownership_field} must match the command actor",
            f"$.payload.{ownership_field}",
        )

    for field_name in COMMAND_ACTOR_REFERENCES[command["command_type"]]:
        referenced_actor = payload[field_name]
        if referenced_actor is not None and (
            not isinstance(referenced_actor, str) or referenced_actor not in registry.actors
        ):
            result.add(
                "PERMISSION_DENIED",
                f"referenced actor_id {referenced_actor} is not registered",
                f"$.payload.{field_name}",
            )
    return result


def _has_exact_fields(value: Any, fields: set[str]) -> bool:
    return isinstance(value, dict) and set(value) == fields


def _actor_record(value: Any, location: str, findings: list[Finding]) -> ActorRecord | None:
    if not _has_exact_fields(value, ACTOR_FIELDS):
        findings.append(Finding("ACTOR_REGISTRY_INVALID", "actor record fields are invalid", location))
        return None
    actor_id = value["actor_id"]
    canonical_name = value["canonical_name"]
    source_ref = value["source_ref"]
    if not isinstance(actor_id, str) or not actor_id.strip():
        findings.append(Finding("ACTOR_REGISTRY_INVALID", "actor_id must be non-empty", f"{location}.actor_id"))
        return None
    if (
        not isinstance(canonical_name, str)
        or not canonical_name.strip()
        or canonical_name in {".", ".."}
        or "/" in canonical_name
        or "\\" in canonical_name
    ):
        findings.append(
            Finding("ACTOR_REGISTRY_INVALID", "canonical_name must be one safe path component", f"{location}.canonical_name")
        )
        return None
    if (
        not isinstance(source_ref, str)
        or not source_ref
        or source_ref.startswith("/")
        or ".." in source_ref.split("/")
    ):
        findings.append(
            Finding("ACTOR_REGISTRY_INVALID", "source_ref must be normalized and repository-relative", f"{location}.source_ref")
        )
        return None
    if value["actor_type"] not in {"HUMAN", "AGENT", "SERVICE"}:
        findings.append(Finding("ACTOR_REGISTRY_INVALID", "actor_type is invalid", f"{location}.actor_type"))
        return None
    active_from = _registry_timestamp(value["active_from"], f"{location}.active_from", findings)
    active_until = None
    if value["active_until"] is not None:
        active_until = _registry_timestamp(value["active_until"], f"{location}.active_until", findings)
    if active_from is None or (value["active_until"] is not None and active_until is None):
        return None
    if active_until is not None and active_from >= active_until:
        findings.append(
            Finding("ACTOR_REGISTRY_INVALID", "active window must be non-empty", location)
        )
        return None
    return ActorRecord(
        actor_id=actor_id,
        actor_type=value["actor_type"],
        canonical_name=canonical_name,
        source_ref=source_ref,
        active_from=active_from,
        active_until=active_until,
    )


def _capability_grant(value: Any, location: str, findings: list[Finding]) -> tuple[str, list[str]] | None:
    if not _has_exact_fields(value, GRANT_FIELDS):
        findings.append(Finding("CAPABILITY_REGISTRY_INVALID", "grant fields are invalid", location))
        return None
    actor_id = value["actor_id"]
    actor_capabilities = value["capabilities"]
    if not isinstance(actor_id, str) or not actor_id:
        findings.append(Finding("CAPABILITY_REGISTRY_INVALID", "actor_id must be non-empty", f"{location}.actor_id"))
        return None
    if not isinstance(actor_capabilities, list) or any(not isinstance(item, str) for item in actor_capabilities):
        findings.append(
            Finding("CAPABILITY_REGISTRY_INVALID", "capabilities must be a string array", f"{location}.capabilities")
        )
        return None
    if len(set(actor_capabilities)) != len(actor_capabilities):
        findings.append(
            Finding("CAPABILITY_REGISTRY_INVALID", "capabilities must be unique", f"{location}.capabilities")
        )
        return None
    unknown = sorted(set(actor_capabilities) - CAPABILITIES)
    if unknown:
        findings.append(
            Finding("CAPABILITY_REGISTRY_INVALID", f"unknown capabilities: {', '.join(unknown)}", f"{location}.capabilities")
        )
        return None
    return actor_id, actor_capabilities


def _registry_timestamp(value: Any, location: str, findings: list[Finding]) -> dt.datetime | None:
    try:
        return _parse_timestamp(value)
    except (TypeError, ValueError):
        findings.append(
            Finding("ACTOR_REGISTRY_INVALID", "timestamp must be UTC RFC 3339 with six fractional digits and Z", location)
        )
        return None


def _parse_timestamp(value: Any) -> dt.datetime:
    if not isinstance(value, str) or not TIMESTAMP_PATTERN.fullmatch(value):
        raise TypeError("invalid timestamp")
    return dt.datetime.fromisoformat(value[:-1] + "+00:00")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON member: {key}")
        value[key] = item
    return value
