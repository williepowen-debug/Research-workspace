"""Pure validation and replay primitives for the fixture-only Kernel v1 slice."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from typing import Any, Iterable


SCHEMA_VERSION = "kernel.schema.1"
POLICY_VERSION = "kernel.policy.1"
WRITER_VERSION = "kernel.writer.1"
AUTHORITY_MODE = "SHADOW"

UUID7 = r"[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
ID_PATTERNS = {
    "command_id": re.compile(rf"^CMD-{UUID7}$"),
    "event_id": re.compile(rf"^EVT-{UUID7}$"),
    "question_id": re.compile(rf"^Q-{UUID7}$"),
    "forecast_id": re.compile(rf"^F-{UUID7}$"),
    "resolution_id": re.compile(rf"^R-{UUID7}$"),
}

COMMAND_FIELDS = {
    "schema_version",
    "policy_version",
    "command_id",
    "command_type",
    "actor_id",
    "submitted_at",
    "expected_version",
    "target_stream_id",
    "correlation_id",
    "caused_by",
    "depends_on",
    "payload",
    "native_refs",
}

EVENT_FIELDS = {
    "schema_version",
    "policy_version",
    "writer_version",
    "event_id",
    "event_type",
    "command_id",
    "command_hash",
    "command_result",
    "stream_id",
    "stream_version",
    "previous_event_id",
    "object_id",
    "object_type",
    "actor_id",
    "writer_id",
    "submitted_at",
    "recorded_at",
    "effective_at",
    "correlation_id",
    "caused_by",
    "authority_mode",
    "native_refs",
    "evidence_refs",
    "payload",
}

NATIVE_REF_FIELDS = {
    "repository",
    "source_commit",
    "path",
    "locator_type",
    "locator",
    "raw_record_sha256",
}

QUESTION_FIELDS = {
    "question_id",
    "owner_actor_id",
    "claim",
    "forecast_family",
    "opens_at",
    "closes_at",
    "resolver_anchor_type",
    "resolution_condition",
    "resolution_rule",
    "resolution_sources",
    "fallback_resolution_source",
    "ambiguity_rule",
    "annulment_rules",
    "resolver_actor_id",
    "independent_verifier_actor_id",
    "negative_search_procedure",
}

FORECAST_FIELDS = {
    "forecast_id",
    "question_id",
    "forecaster_actor_id",
    "forecast_version",
    "information_as_of",
    "probability",
    "rationale_ref",
    "evidence_refs",
    "intervention_stage",
    "decision_consequence",
}


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    location: str = "$"


@dataclass
class ValidationResult:
    findings: list[Finding] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return not self.findings

    def add(self, code: str, message: str, location: str = "$") -> None:
        self.findings.append(Finding(code, message, location))


@dataclass
class ReplayResult:
    streams: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    current: dict[str, dict[str, Any]] = field(default_factory=dict)
    conflicts: set[str] = field(default_factory=set)
    findings: list[Finding] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return not self.findings and not self.conflicts


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")


def sha256_hex(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def _exact_fields(result: ValidationResult, value: Any, allowed: set[str], location: str) -> bool:
    if not isinstance(value, dict):
        result.add("TYPE_INVALID", "must be an object", location)
        return False
    missing = sorted(allowed - value.keys())
    extra = sorted(value.keys() - allowed)
    if missing:
        result.add("REQUIRED_FIELD_MISSING", f"missing fields: {', '.join(missing)}", location)
    if extra:
        result.add("UNKNOWN_FIELD", f"unknown fields: {', '.join(extra)}", location)
    return not missing and not extra


def _timestamp(result: ValidationResult, value: Any, location: str, *, optional: bool = False) -> dt.datetime | None:
    if optional and value is None:
        return None
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z", value):
        result.add("INVALID_TIMESTAMP", "must be UTC RFC 3339 with six fractional digits and Z", location)
        return None
    try:
        return dt.datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        result.add("INVALID_TIMESTAMP", "timestamp is not a real date-time", location)
        return None


def _identifier(result: ValidationResult, field_name: str, value: Any, location: str) -> None:
    pattern = ID_PATTERNS[field_name]
    if not isinstance(value, str) or not pattern.fullmatch(value):
        result.add("IDENTIFIER_INVALID", f"invalid {field_name}", location)


def _native_ref(result: ValidationResult, value: Any, location: str) -> None:
    if not _exact_fields(result, value, NATIVE_REF_FIELDS, location):
        return
    if value["repository"] != "williepowen-debug/Research-workspace":
        result.add("NATIVE_REPOSITORY_INVALID", "repository is not the configured authority", f"{location}.repository")
    if not isinstance(value["source_commit"], str) or not re.fullmatch(r"[0-9a-f]{40}", value["source_commit"]):
        result.add("NATIVE_COMMIT_INVALID", "source_commit must be a full lowercase Git SHA", f"{location}.source_commit")
    path = value["path"]
    if not isinstance(path, str) or path.startswith("/") or ".." in path.split("/") or not path:
        result.add("NATIVE_PATH_INVALID", "path must be normalized and repository-relative", f"{location}.path")
    if value["locator_type"] not in {"TSV_RECORD_ID", "JSON_POINTER"}:
        result.add("NATIVE_LOCATOR_INVALID", "live-compatible locator must be TSV_RECORD_ID or JSON_POINTER", f"{location}.locator_type")
    if not isinstance(value["locator"], str) or not value["locator"]:
        result.add("NATIVE_LOCATOR_INVALID", "locator must be non-empty", f"{location}.locator")
    if not isinstance(value["raw_record_sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", value["raw_record_sha256"]):
        result.add("NATIVE_HASH_INVALID", "raw_record_sha256 must be lowercase SHA-256", f"{location}.raw_record_sha256")


def _question_payload(result: ValidationResult, value: Any, location: str) -> None:
    if not _exact_fields(result, value, QUESTION_FIELDS, location):
        return
    _identifier(result, "question_id", value["question_id"], f"{location}.question_id")
    if value["forecast_family"] != "BINARY_PROBABILITY":
        result.add("FAMILY_NOT_ENABLED", "only BINARY_PROBABILITY is enabled", f"{location}.forecast_family")
    opens = _timestamp(result, value["opens_at"], f"{location}.opens_at")
    closes = _timestamp(result, value["closes_at"], f"{location}.closes_at")
    if opens and closes and opens >= closes:
        result.add("QUESTION_WINDOW_INVALID", "opens_at must precede closes_at", location)
    if value["resolver_anchor_type"] not in {"FIXED_DEADLINE", "EXPECTED_EVENT", "DECISION_DATE"}:
        result.add("RESOLVER_ANCHOR_INVALID", "unknown resolver anchor type", f"{location}.resolver_anchor_type")
    for field_name in ("claim", "resolution_condition", "resolution_rule", "ambiguity_rule", "resolver_actor_id"):
        if not isinstance(value[field_name], str) or not value[field_name].strip():
            result.add("VALUE_REQUIRED", f"{field_name} must be non-empty", f"{location}.{field_name}")
    if not isinstance(value["resolution_sources"], list) or not value["resolution_sources"]:
        result.add("EVIDENCE_REQUIRED", "resolution_sources must be non-empty", f"{location}.resolution_sources")
    if not isinstance(value["annulment_rules"], list) or not value["annulment_rules"]:
        result.add("ANNULMENT_RULE_REQUIRED", "annulment_rules must be non-empty", f"{location}.annulment_rules")


def _forecast_payload(result: ValidationResult, value: Any, location: str, submitted_at: dt.datetime | None) -> None:
    if not _exact_fields(result, value, FORECAST_FIELDS, location):
        return
    _identifier(result, "forecast_id", value["forecast_id"], f"{location}.forecast_id")
    _identifier(result, "question_id", value["question_id"], f"{location}.question_id")
    if value["forecast_version"] != 1:
        result.add("FORECAST_VERSION_INVALID", "initial forecast_version must be 1", f"{location}.forecast_version")
    information_as_of = _timestamp(result, value["information_as_of"], f"{location}.information_as_of")
    if submitted_at and information_as_of and information_as_of > submitted_at:
        result.add("INVALID_INFORMATION_CUTOFF", "information_as_of cannot follow submitted_at", f"{location}.information_as_of")
    try:
        probability = Decimal(str(value["probability"]))
    except (InvalidOperation, ValueError):
        result.add("PROBABILITY_INVALID", "probability must be decimal", f"{location}.probability")
    else:
        if probability < 0 or probability > 1:
            result.add("PROBABILITY_INVALID", "probability must be between 0 and 1", f"{location}.probability")
    if value["intervention_stage"] not in {"INITIAL", "POST_CHALLENGE", "POST_SYNTHESIS", "FINAL_CUTOFF"}:
        result.add("INTERVENTION_STAGE_INVALID", "unknown intervention stage", f"{location}.intervention_stage")


def validate_command(command: Any) -> ValidationResult:
    result = ValidationResult()
    if not _exact_fields(result, command, COMMAND_FIELDS, "$"):
        return result
    if command["schema_version"] != SCHEMA_VERSION:
        result.add("SCHEMA_VERSION_UNSUPPORTED", "unsupported schema_version", "$.schema_version")
    if command["policy_version"] != POLICY_VERSION:
        result.add("POLICY_VERSION_UNSUPPORTED", "unsupported policy_version", "$.policy_version")
    _identifier(result, "command_id", command["command_id"], "$.command_id")
    submitted_at = _timestamp(result, command["submitted_at"], "$.submitted_at")
    if not isinstance(command["expected_version"], int) or isinstance(command["expected_version"], bool) or command["expected_version"] < 0:
        result.add("EXPECTED_VERSION_INVALID", "expected_version must be a non-negative integer", "$.expected_version")
    if not isinstance(command["depends_on"], list) or any(not ID_PATTERNS["command_id"].fullmatch(v) for v in command["depends_on"] if isinstance(v, str)) or any(not isinstance(v, str) for v in command["depends_on"]):
        result.add("DEPENDENCY_INVALID", "depends_on must contain command IDs", "$.depends_on")
    native_refs = command["native_refs"]
    if not isinstance(native_refs, list) or not native_refs:
        result.add("NATIVE_REFERENCE_REQUIRED", "native_refs must be non-empty", "$.native_refs")
    else:
        for index, native_ref in enumerate(native_refs):
            _native_ref(result, native_ref, f"$.native_refs[{index}]")
    command_type = command["command_type"]
    if command_type == "RegisterQuestion":
        _question_payload(result, command["payload"], "$.payload")
        expected_stream = f"QS-{command['payload'].get('question_id')}" if isinstance(command["payload"], dict) else None
    elif command_type == "SubmitForecast":
        _forecast_payload(result, command["payload"], "$.payload", submitted_at)
        expected_stream = f"FS-{command['payload'].get('forecast_id')}" if isinstance(command["payload"], dict) else None
    else:
        result.add("COMMAND_TYPE_UNSUPPORTED", "command type is outside the first fixture slice", "$.command_type")
        expected_stream = None
    if expected_stream and command["target_stream_id"] != expected_stream:
        result.add("TARGET_STREAM_MISMATCH", "target_stream_id does not match payload identity", "$.target_stream_id")
    return result


def validate_event(event: Any) -> ValidationResult:
    result = ValidationResult()
    if not _exact_fields(result, event, EVENT_FIELDS, "$"):
        return result
    for field_name, expected in (
        ("schema_version", SCHEMA_VERSION),
        ("policy_version", POLICY_VERSION),
        ("writer_version", WRITER_VERSION),
        ("command_result", "ACCEPTED"),
        ("authority_mode", AUTHORITY_MODE),
    ):
        if event[field_name] != expected:
            result.add("EVENT_ENVELOPE_INVALID", f"{field_name} must be {expected}", f"$.{field_name}")
    _identifier(result, "event_id", event["event_id"], "$.event_id")
    _identifier(result, "command_id", event["command_id"], "$.command_id")
    if not isinstance(event["command_hash"], str) or not re.fullmatch(r"[0-9a-f]{64}", event["command_hash"]):
        result.add("COMMAND_HASH_INVALID", "command_hash must be lowercase SHA-256", "$.command_hash")
    _timestamp(result, event["submitted_at"], "$.submitted_at")
    _timestamp(result, event["recorded_at"], "$.recorded_at")
    _timestamp(result, event["effective_at"], "$.effective_at", optional=True)
    version = event["stream_version"]
    if not isinstance(version, int) or isinstance(version, bool) or version < 1:
        result.add("STREAM_VERSION_INVALID", "stream_version must be a positive integer", "$.stream_version")
    if version == 1 and event["previous_event_id"] is not None:
        result.add("PREVIOUS_EVENT_INVALID", "stream version 1 must have no parent", "$.previous_event_id")
    if version != 1:
        _identifier(result, "event_id", event["previous_event_id"], "$.previous_event_id")
    refs = event["native_refs"]
    if not isinstance(refs, list) or not refs:
        result.add("NATIVE_REFERENCE_REQUIRED", "native_refs must be non-empty", "$.native_refs")
    else:
        for index, native_ref in enumerate(refs):
            _native_ref(result, native_ref, f"$.native_refs[{index}]")
    if event["event_type"] == "QuestionRegistered":
        _question_payload(result, event["payload"], "$.payload")
        if event["object_type"] != "QUESTION" or event["object_id"] != event["payload"].get("question_id"):
            result.add("OBJECT_MISMATCH", "question object identity does not match payload", "$")
    elif event["event_type"] == "ForecastSubmitted":
        submitted = _timestamp(ValidationResult(), event["submitted_at"], "$.submitted_at")
        _forecast_payload(result, event["payload"], "$.payload", submitted)
        if event["object_type"] != "FORECAST" or event["object_id"] != event["payload"].get("forecast_id"):
            result.add("OBJECT_MISMATCH", "forecast object identity does not match payload", "$")
    else:
        result.add("EVENT_TYPE_UNSUPPORTED", "event type is outside the first fixture slice", "$.event_type")
    return result


def replay(events: Iterable[dict[str, Any]]) -> ReplayResult:
    result = ReplayResult()
    valid_events: list[dict[str, Any]] = []
    event_ids: set[str] = set()
    for event in events:
        validation = validate_event(event)
        if not validation.valid:
            result.findings.extend(validation.findings)
            continue
        if event["event_id"] in event_ids:
            result.findings.append(Finding("DUPLICATE_EVENT_ID", event["event_id"]))
            continue
        event_ids.add(event["event_id"])
        valid_events.append(event)
        result.streams.setdefault(event["stream_id"], []).append(event)

    for stream_id, stream_events in result.streams.items():
        by_version: dict[int, list[dict[str, Any]]] = {}
        for event in stream_events:
            by_version.setdefault(event["stream_version"], []).append(event)
        if any(len(children) != 1 for children in by_version.values()):
            result.conflicts.add(stream_id)
            continue
        ordered = [by_version[version][0] for version in sorted(by_version)]
        expected_versions = list(range(1, len(ordered) + 1))
        if [event["stream_version"] for event in ordered] != expected_versions:
            result.findings.append(Finding("STREAM_VERSION_GAP", stream_id))
            continue
        for index, event in enumerate(ordered):
            expected_parent = None if index == 0 else ordered[index - 1]["event_id"]
            if event["previous_event_id"] != expected_parent:
                result.findings.append(Finding("STREAM_PARENT_MISMATCH", event["event_id"]))
        if not any(f.message == stream_id or f.message in {e["event_id"] for e in ordered} for f in result.findings):
            result.current[stream_id] = ordered[-1]
            result.streams[stream_id] = ordered
    return result
