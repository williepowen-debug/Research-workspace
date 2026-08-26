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

RECEIPT_FIELDS = {
    "schema_version",
    "policy_version",
    "writer_version",
    "command_id",
    "command_hash",
    "command_result",
    "actor_id",
    "writer_id",
    "submitted_at",
    "recorded_at",
    "reason_code",
    "reason_detail",
    "target_stream_id",
    "expected_version",
    "native_refs",
}

REJECTION_REASONS = {
    "ACTOR_PATH_MISMATCH",
    "AUDIT_DUPLICATE_RESULT",
    "COMMAND_SCHEMA_INVALID",
    "DEPENDENCY_CYCLE",
    "DEPENDENCY_REJECTED",
    "DUPLICATE_COMMAND",
    "EVIDENCE_REQUIRED",
    "FAMILY_NOT_ENABLED",
    "IDENTIFIER_COLLISION",
    "IDEMPOTENCY_KEY_REUSED",
    "INVALID_INFORMATION_CUTOFF",
    "INVALID_TIMESTAMP",
    "NATIVE_BLOB_MISMATCH",
    "NATIVE_PATH_INVALID",
    "NATIVE_RECORD_AMBIGUOUS",
    "NATIVE_RECORD_INVALID",
    "NATIVE_RECORD_MISSING",
    "NATIVE_RECORD_MISMATCH",
    "PERMISSION_DENIED",
    "POLICY_VERSION_UNSUPPORTED",
    "PROTECTED_SELF_VERIFICATION",
    "QUESTION_NOT_OPEN",
    "SCHEMA_VERSION_UNSUPPORTED",
    "STALE_EXPECTED_VERSION",
    "TRANSITION_FORBIDDEN",
    "UNSUPPORTED_HISTORICAL_VERSION",
}

MAX_REASON_DETAIL_BYTES = 512

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

COMMAND_EVENT_TYPES = {
    "RegisterQuestion": "QuestionRegistered",
    "CloseQuestion": "QuestionClosed",
    "AnnulQuestion": "QuestionAnnulled",
    "SubmitForecast": "ForecastSubmitted",
    "AmendForecast": "ForecastAmended",
    "WithdrawForecast": "ForecastWithdrawn",
    "ProposeResolution": "ResolutionProposed",
    "VerifyResolution": "ResolutionVerified",
    "DisputeResolution": "ResolutionDisputed",
    "CorrectResolution": "ResolutionCorrected",
}

EVENT_COMMAND_TYPES = {event_type: command_type for command_type, event_type in COMMAND_EVENT_TYPES.items()}

CLOSE_QUESTION_FIELDS = {"question_id", "closed_by", "closed_at"}
WITHDRAW_FORECAST_FIELDS = {"forecast_id", "question_id", "forecaster_actor_id"}
PROPOSE_RESOLUTION_FIELDS = {
    "resolution_id",
    "question_id",
    "outcome_value",
    "proposed_by",
    "resolution_evidence_refs",
    "negative_search_attempt",
    "annulment_reason",
}
VERIFY_RESOLUTION_FIELDS = {
    "resolution_id",
    "question_id",
    "verified_outcome_value",
    "verified_by",
    "verification_evidence_refs",
    "disposition",
}
DISPUTE_RESOLUTION_FIELDS = {
    "resolution_id",
    "question_id",
    "disputed_by",
    "dispute_evidence_refs",
}
CORRECT_RESOLUTION_FIELDS = {
    "resolution_id",
    "question_id",
    "corrected_outcome_value",
    "corrected_by",
    "correction_evidence_refs",
    "will_authorization_ref",
}
ANNUL_QUESTION_FIELDS = {
    "question_id",
    "annulled_by",
    "annulment_reason",
    "independent_approval_ref",
}

OUTCOME_VALUES = {"YES", "NO", "AMBIGUOUS", "ANNULLED"}


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
    question_states: dict[str, dict[str, Any]] = field(default_factory=dict)
    forecast_states: dict[str, dict[str, Any]] = field(default_factory=dict)
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
    for field_name in (
        "owner_actor_id",
        "claim",
        "resolution_condition",
        "resolution_rule",
        "ambiguity_rule",
        "resolver_actor_id",
    ):
        _required_string(result, value[field_name], f"{location}.{field_name}", field_name)
    _string_array(result, value["resolution_sources"], f"{location}.resolution_sources")
    if (
        not isinstance(value["annulment_rules"], list)
        or not value["annulment_rules"]
        or any(not isinstance(item, str) or not item.strip() for item in value["annulment_rules"])
    ):
        result.add("ANNULMENT_RULE_REQUIRED", "annulment_rules must be non-empty strings", f"{location}.annulment_rules")
    for field_name in ("fallback_resolution_source", "independent_verifier_actor_id", "negative_search_procedure"):
        if value[field_name] is not None:
            _required_string(result, value[field_name], f"{location}.{field_name}", field_name)


def _forecast_payload(
    result: ValidationResult,
    value: Any,
    location: str,
    submitted_at: dt.datetime | None,
    *,
    initial: bool,
) -> None:
    if not _exact_fields(result, value, FORECAST_FIELDS, location):
        return
    _identifier(result, "forecast_id", value["forecast_id"], f"{location}.forecast_id")
    _identifier(result, "question_id", value["question_id"], f"{location}.question_id")
    required_version = 1 if initial else 2
    if (
        not isinstance(value["forecast_version"], int)
        or isinstance(value["forecast_version"], bool)
        or value["forecast_version"] < required_version
        or (initial and value["forecast_version"] != 1)
    ):
        message = "initial forecast_version must be 1" if initial else "amended forecast_version must be at least 2"
        result.add("FORECAST_VERSION_INVALID", message, f"{location}.forecast_version")
    information_as_of = _timestamp(result, value["information_as_of"], f"{location}.information_as_of")
    if submitted_at and information_as_of and information_as_of > submitted_at:
        result.add("INVALID_INFORMATION_CUTOFF", "information_as_of cannot follow submitted_at", f"{location}.information_as_of")
    try:
        probability = Decimal(str(value["probability"]))
    except (InvalidOperation, ValueError):
        result.add("PROBABILITY_INVALID", "probability must be decimal", f"{location}.probability")
    else:
        if not probability.is_finite() or probability < 0 or probability > 1:
            result.add("PROBABILITY_INVALID", "probability must be between 0 and 1", f"{location}.probability")
    if value["intervention_stage"] not in {"INITIAL", "POST_CHALLENGE", "POST_SYNTHESIS", "FINAL_CUTOFF"}:
        result.add("INTERVENTION_STAGE_INVALID", "unknown intervention stage", f"{location}.intervention_stage")
    for field_name in ("forecaster_actor_id", "rationale_ref"):
        _required_string(result, value[field_name], f"{location}.{field_name}", field_name)
    _string_array(result, value["evidence_refs"], f"{location}.evidence_refs", allow_empty=True)


def _close_question_payload(result: ValidationResult, value: Any, location: str) -> None:
    if not _exact_fields(result, value, CLOSE_QUESTION_FIELDS, location):
        return
    _identifier(result, "question_id", value["question_id"], f"{location}.question_id")
    _required_string(result, value["closed_by"], f"{location}.closed_by", "closed_by")
    _timestamp(result, value["closed_at"], f"{location}.closed_at")


def _withdraw_forecast_payload(result: ValidationResult, value: Any, location: str) -> None:
    if not _exact_fields(result, value, WITHDRAW_FORECAST_FIELDS, location):
        return
    _identifier(result, "forecast_id", value["forecast_id"], f"{location}.forecast_id")
    _identifier(result, "question_id", value["question_id"], f"{location}.question_id")
    _required_string(result, value["forecaster_actor_id"], f"{location}.forecaster_actor_id", "forecaster_actor_id")


def _propose_resolution_payload(result: ValidationResult, value: Any, location: str) -> None:
    if not _exact_fields(result, value, PROPOSE_RESOLUTION_FIELDS, location):
        return
    _resolution_identity(result, value, location)
    if value["outcome_value"] not in OUTCOME_VALUES:
        result.add("OUTCOME_INVALID", "outcome_value is not registered", f"{location}.outcome_value")
    _required_string(result, value["proposed_by"], f"{location}.proposed_by", "proposed_by")
    evidence = value["resolution_evidence_refs"]
    _string_array(
        result,
        evidence,
        f"{location}.resolution_evidence_refs",
        allow_empty=value["outcome_value"] == "ANNULLED",
    )
    if value["outcome_value"] == "ANNULLED":
        _required_string(result, value["annulment_reason"], f"{location}.annulment_reason", "annulment_reason")
    elif value["annulment_reason"] is not None:
        result.add("VALUE_FORBIDDEN", "annulment_reason is only valid for ANNULLED", f"{location}.annulment_reason")
    if value["negative_search_attempt"] is not None:
        _required_string(
            result,
            value["negative_search_attempt"],
            f"{location}.negative_search_attempt",
            "negative_search_attempt",
        )


def _verify_resolution_payload(result: ValidationResult, value: Any, location: str) -> None:
    if not _exact_fields(result, value, VERIFY_RESOLUTION_FIELDS, location):
        return
    _resolution_identity(result, value, location)
    if value["verified_outcome_value"] not in OUTCOME_VALUES:
        result.add("OUTCOME_INVALID", "verified_outcome_value is not registered", f"{location}.verified_outcome_value")
    _required_string(result, value["verified_by"], f"{location}.verified_by", "verified_by")
    _string_array(result, value["verification_evidence_refs"], f"{location}.verification_evidence_refs")
    if value["disposition"] != "VERIFY":
        result.add("DISPOSITION_INVALID", "disposition must be VERIFY", f"{location}.disposition")


def _dispute_resolution_payload(result: ValidationResult, value: Any, location: str) -> None:
    if not _exact_fields(result, value, DISPUTE_RESOLUTION_FIELDS, location):
        return
    _resolution_identity(result, value, location)
    _required_string(result, value["disputed_by"], f"{location}.disputed_by", "disputed_by")
    _string_array(result, value["dispute_evidence_refs"], f"{location}.dispute_evidence_refs")


def _correct_resolution_payload(result: ValidationResult, value: Any, location: str) -> None:
    if not _exact_fields(result, value, CORRECT_RESOLUTION_FIELDS, location):
        return
    _resolution_identity(result, value, location)
    if value["corrected_outcome_value"] not in OUTCOME_VALUES - {"ANNULLED"}:
        result.add("OUTCOME_INVALID", "corrected_outcome_value is not registered", f"{location}.corrected_outcome_value")
    _required_string(result, value["corrected_by"], f"{location}.corrected_by", "corrected_by")
    _string_array(result, value["correction_evidence_refs"], f"{location}.correction_evidence_refs")
    _required_string(
        result,
        value["will_authorization_ref"],
        f"{location}.will_authorization_ref",
        "will_authorization_ref",
    )


def _annul_question_payload(result: ValidationResult, value: Any, location: str) -> None:
    if not _exact_fields(result, value, ANNUL_QUESTION_FIELDS, location):
        return
    _identifier(result, "question_id", value["question_id"], f"{location}.question_id")
    _required_string(result, value["annulled_by"], f"{location}.annulled_by", "annulled_by")
    _required_string(result, value["annulment_reason"], f"{location}.annulment_reason", "annulment_reason")
    if value["independent_approval_ref"] is not None:
        _required_string(
            result,
            value["independent_approval_ref"],
            f"{location}.independent_approval_ref",
            "independent_approval_ref",
        )


def _resolution_identity(result: ValidationResult, value: dict[str, Any], location: str) -> None:
    _identifier(result, "resolution_id", value["resolution_id"], f"{location}.resolution_id")
    _identifier(result, "question_id", value["question_id"], f"{location}.question_id")


def _required_string(result: ValidationResult, value: Any, location: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        result.add("VALUE_REQUIRED", f"{field_name} must be non-empty", location)


def _string_array(
    result: ValidationResult,
    value: Any,
    location: str,
    *,
    allow_empty: bool = False,
) -> None:
    if (
        not isinstance(value, list)
        or (not value and not allow_empty)
        or any(not isinstance(item, str) or not item.strip() for item in value)
    ):
        result.add("EVIDENCE_REQUIRED", "must be an array of non-empty references", location)


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
    if (
        not isinstance(command["depends_on"], list)
        or any(not isinstance(value, str) for value in command["depends_on"])
        or any(
            not ID_PATTERNS["command_id"].fullmatch(value)
            for value in command["depends_on"]
            if isinstance(value, str)
        )
        or (
            all(isinstance(value, str) for value in command["depends_on"])
            and len(set(command["depends_on"])) != len(command["depends_on"])
        )
    ):
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
    elif command_type == "CloseQuestion":
        _close_question_payload(result, command["payload"], "$.payload")
        expected_stream = f"QS-{command['payload'].get('question_id')}" if isinstance(command["payload"], dict) else None
    elif command_type == "AnnulQuestion":
        _annul_question_payload(result, command["payload"], "$.payload")
        expected_stream = f"QS-{command['payload'].get('question_id')}" if isinstance(command["payload"], dict) else None
    elif command_type == "SubmitForecast":
        _forecast_payload(result, command["payload"], "$.payload", submitted_at, initial=True)
        expected_stream = f"FS-{command['payload'].get('forecast_id')}" if isinstance(command["payload"], dict) else None
    elif command_type == "AmendForecast":
        _forecast_payload(result, command["payload"], "$.payload", submitted_at, initial=False)
        expected_stream = f"FS-{command['payload'].get('forecast_id')}" if isinstance(command["payload"], dict) else None
    elif command_type == "WithdrawForecast":
        _withdraw_forecast_payload(result, command["payload"], "$.payload")
        expected_stream = f"FS-{command['payload'].get('forecast_id')}" if isinstance(command["payload"], dict) else None
    elif command_type == "ProposeResolution":
        _propose_resolution_payload(result, command["payload"], "$.payload")
        expected_stream = f"QS-{command['payload'].get('question_id')}" if isinstance(command["payload"], dict) else None
    elif command_type == "VerifyResolution":
        _verify_resolution_payload(result, command["payload"], "$.payload")
        expected_stream = f"QS-{command['payload'].get('question_id')}" if isinstance(command["payload"], dict) else None
    elif command_type == "DisputeResolution":
        _dispute_resolution_payload(result, command["payload"], "$.payload")
        expected_stream = f"QS-{command['payload'].get('question_id')}" if isinstance(command["payload"], dict) else None
    elif command_type == "CorrectResolution":
        _correct_resolution_payload(result, command["payload"], "$.payload")
        expected_stream = f"QS-{command['payload'].get('question_id')}" if isinstance(command["payload"], dict) else None
    else:
        result.add("COMMAND_TYPE_UNSUPPORTED", "command type is outside the fixture lifecycle slice", "$.command_type")
        expected_stream = None
    if command_type in {"RegisterQuestion", "SubmitForecast"} and command["expected_version"] != 0:
        result.add("EXPECTED_VERSION_INVALID", "creation commands require expected_version 0", "$.expected_version")
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
    if not isinstance(event["evidence_refs"], list):
        result.add("TYPE_INVALID", "evidence_refs must be an array", "$.evidence_refs")
    event_type = event["event_type"]
    if event_type == "QuestionRegistered":
        _question_payload(result, event["payload"], "$.payload")
        expected_object_type = "QUESTION"
        identity_field = "question_id"
    elif event_type == "QuestionClosed":
        _close_question_payload(result, event["payload"], "$.payload")
        expected_object_type = "QUESTION"
        identity_field = "question_id"
    elif event_type == "QuestionAnnulled":
        _annul_question_payload(result, event["payload"], "$.payload")
        expected_object_type = "QUESTION"
        identity_field = "question_id"
    elif event_type in {"ForecastSubmitted", "ForecastAmended"}:
        submitted = _timestamp(ValidationResult(), event["submitted_at"], "$.submitted_at")
        _forecast_payload(
            result,
            event["payload"],
            "$.payload",
            submitted,
            initial=event_type == "ForecastSubmitted",
        )
        expected_object_type = "FORECAST"
        identity_field = "forecast_id"
    elif event_type == "ForecastWithdrawn":
        _withdraw_forecast_payload(result, event["payload"], "$.payload")
        expected_object_type = "FORECAST"
        identity_field = "forecast_id"
    elif event_type == "ResolutionProposed":
        _propose_resolution_payload(result, event["payload"], "$.payload")
        expected_object_type = "RESOLUTION"
        identity_field = "resolution_id"
    elif event_type == "ResolutionVerified":
        _verify_resolution_payload(result, event["payload"], "$.payload")
        expected_object_type = "RESOLUTION"
        identity_field = "resolution_id"
    elif event_type == "ResolutionDisputed":
        _dispute_resolution_payload(result, event["payload"], "$.payload")
        expected_object_type = "RESOLUTION"
        identity_field = "resolution_id"
    elif event_type == "ResolutionCorrected":
        _correct_resolution_payload(result, event["payload"], "$.payload")
        expected_object_type = "RESOLUTION"
        identity_field = "resolution_id"
    else:
        result.add("EVENT_TYPE_UNSUPPORTED", "event type is outside the fixture lifecycle slice", "$.event_type")
        expected_object_type = None
        identity_field = None
    if expected_object_type is not None and (
        event["object_type"] != expected_object_type
        or not isinstance(event["payload"], dict)
        or event["object_id"] != event["payload"].get(identity_field)
    ):
        result.add("OBJECT_MISMATCH", "object identity does not match payload", "$")
    if isinstance(event["payload"], dict):
        question_id = event["payload"].get("question_id")
        forecast_id = event["payload"].get("forecast_id")
        expected_stream = f"FS-{forecast_id}" if expected_object_type == "FORECAST" else f"QS-{question_id}"
        if event["stream_id"] != expected_stream:
            result.add("TARGET_STREAM_MISMATCH", "stream_id does not match payload identity", "$.stream_id")
    if event_type in {"QuestionRegistered", "ForecastSubmitted"} and version != 1:
        result.add("STREAM_VERSION_INVALID", "creation events require stream_version 1", "$.stream_version")
    if event_type not in {"QuestionRegistered", "ForecastSubmitted"} and isinstance(version, int) and version < 2:
        result.add("STREAM_VERSION_INVALID", "lifecycle events require stream_version at least 2", "$.stream_version")
    return result


def validate_receipt(receipt: Any) -> ValidationResult:
    result = ValidationResult()
    if not _exact_fields(result, receipt, RECEIPT_FIELDS, "$"):
        return result
    for field_name, expected in (
        ("schema_version", SCHEMA_VERSION),
        ("policy_version", POLICY_VERSION),
        ("writer_version", WRITER_VERSION),
        ("command_result", "REJECTED"),
    ):
        if receipt[field_name] != expected:
            result.add("RECEIPT_ENVELOPE_INVALID", f"{field_name} must be {expected}", f"$.{field_name}")
    _identifier(result, "command_id", receipt["command_id"], "$.command_id")
    if not isinstance(receipt["command_hash"], str) or not re.fullmatch(r"[0-9a-f]{64}", receipt["command_hash"]):
        result.add("COMMAND_HASH_INVALID", "command_hash must be lowercase SHA-256", "$.command_hash")
    for field_name in ("actor_id", "writer_id", "target_stream_id"):
        if not isinstance(receipt[field_name], str) or not receipt[field_name]:
            result.add("VALUE_REQUIRED", f"{field_name} must be non-empty", f"$.{field_name}")
    _timestamp(result, receipt["submitted_at"], "$.submitted_at")
    _timestamp(result, receipt["recorded_at"], "$.recorded_at")
    if not isinstance(receipt["reason_code"], str) or receipt["reason_code"] not in REJECTION_REASONS:
        result.add("REJECTION_REASON_INVALID", "reason_code is not registered", "$.reason_code")
    detail = receipt["reason_detail"]
    try:
        detail_size = len(detail.encode("utf-8")) if isinstance(detail, str) else 0
    except UnicodeEncodeError:
        detail_size = MAX_REASON_DETAIL_BYTES + 1
    if not isinstance(detail, str) or not detail or detail_size > MAX_REASON_DETAIL_BYTES:
        result.add(
            "REASON_DETAIL_INVALID",
            f"reason_detail must contain 1 through {MAX_REASON_DETAIL_BYTES} UTF-8 bytes",
            "$.reason_detail",
        )
    expected_version = receipt["expected_version"]
    if not isinstance(expected_version, int) or isinstance(expected_version, bool) or expected_version < 0:
        result.add("EXPECTED_VERSION_INVALID", "expected_version must be a non-negative integer", "$.expected_version")
    if not isinstance(receipt["native_refs"], list):
        result.add("TYPE_INVALID", "native_refs must be an array", "$.native_refs")
    return result


def replay(events: Iterable[dict[str, Any]]) -> ReplayResult:
    result = ReplayResult()
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
        result.streams.setdefault(event["stream_id"], []).append(event)

    for stream_id, stream_events in list(result.streams.items()):
        by_version: dict[int, list[dict[str, Any]]] = {}
        for event in stream_events:
            by_version.setdefault(event["stream_version"], []).append(event)
        if any(len(children) != 1 for children in by_version.values()):
            result.conflicts.add(stream_id)
            continue
        ordered = [by_version[version][0] for version in sorted(by_version)]
        if [event["stream_version"] for event in ordered] != list(range(1, len(ordered) + 1)):
            result.findings.append(Finding("STREAM_VERSION_GAP", stream_id))
            continue
        parent_valid = True
        for index, event in enumerate(ordered):
            expected_parent = None if index == 0 else ordered[index - 1]["event_id"]
            if event["previous_event_id"] != expected_parent:
                result.findings.append(Finding("STREAM_PARENT_MISMATCH", event["event_id"], stream_id))
                parent_valid = False
        if not parent_valid:
            continue
        if stream_id.startswith("QS-"):
            semantic_valid = _reduce_question_stream(result, stream_id, ordered)
        elif stream_id.startswith("FS-"):
            semantic_valid = _reduce_forecast_stream(result, stream_id, ordered)
        else:
            result.findings.append(Finding("STREAM_TRANSITION_INVALID", "unknown stream type", stream_id))
            semantic_valid = False
        if semantic_valid:
            result.current[stream_id] = ordered[-1]
            result.streams[stream_id] = ordered

    for forecast_id, state in list(result.forecast_states.items()):
        question = result.question_states.get(state["question_id"])
        stream_id = f"FS-{forecast_id}"
        if question is None:
            result.findings.append(Finding("ORPHAN_FORECAST", forecast_id, stream_id))
            result.current.pop(stream_id, None)
            continue
        if state["state"] == "ACTIVE" and question["state"] != "OPEN":
            state["state"] = "LOCKED"
    return result


def validate_transition(command: Any, events: Iterable[dict[str, Any]]) -> ValidationResult:
    """Validate one command against deterministic state replayed from accepted events."""

    structural = validate_command(command)
    if not structural.valid:
        return structural
    result = ValidationResult()
    replayed = replay(events)
    if not replayed.valid:
        result.add("TRANSITION_FORBIDDEN", "accepted history is not replay-valid")
        return result

    stream = replayed.streams.get(command["target_stream_id"], [])
    current_version = stream[-1]["stream_version"] if stream else 0
    if command["expected_version"] != current_version:
        result.add(
            "STALE_EXPECTED_VERSION",
            f"expected_version {command['expected_version']} does not match current version {current_version}",
            "$.expected_version",
        )
        return result

    command_type = command["command_type"]
    payload = command["payload"]
    if command_type == "RegisterQuestion":
        return result
    if command_type == "SubmitForecast":
        question = replayed.question_states.get(payload["question_id"])
        if question is None or question["state"] != "OPEN":
            result.add("QUESTION_NOT_OPEN", "forecast question is not replay-valid and OPEN")
        elif command["submitted_at"] > question["registration"]["closes_at"]:
            result.add("QUESTION_NOT_OPEN", "forecast was submitted after closes_at")
        return result

    if not stream:
        result.add("TRANSITION_FORBIDDEN", "lifecycle command requires an existing target stream")
        return result

    if command_type in {"AmendForecast", "WithdrawForecast"}:
        forecast = replayed.forecast_states.get(payload["forecast_id"])
        if forecast is None or forecast["state"] != "ACTIVE":
            result.add("TRANSITION_FORBIDDEN", "forecast is not ACTIVE")
            return result
        if payload["question_id"] != forecast["question_id"] or payload["forecaster_actor_id"] != forecast["forecaster_actor_id"]:
            result.add("TRANSITION_FORBIDDEN", "forecast series identity cannot change")
            return result
        if command_type == "AmendForecast":
            question = replayed.question_states.get(forecast["question_id"])
            if (
                question is None
                or question["state"] != "OPEN"
                or command["submitted_at"] > question["registration"]["closes_at"]
            ):
                result.add("TRANSITION_FORBIDDEN", "forecast amendment requires an OPEN question before closes_at")
                return result
            expected_forecast_version = forecast["versions"][-1]["forecast_version"] + 1
            if payload["forecast_version"] != expected_forecast_version:
                result.add("TRANSITION_FORBIDDEN", "forecast_version must increment by exactly one")
        return result

    question = replayed.question_states.get(payload["question_id"])
    if question is None:
        result.add("TRANSITION_FORBIDDEN", "question stream is not replay-valid")
        return result
    state = question["state"]
    if command_type == "CloseQuestion":
        if state != "OPEN":
            result.add("TRANSITION_FORBIDDEN", "only an OPEN question may close")
        elif payload["closed_by"] != question["registration"]["owner_actor_id"]:
            result.add("PERMISSION_DENIED", "question.close_own is limited to the registered owner")
        elif payload["closed_at"] > command["submitted_at"]:
            result.add("TRANSITION_FORBIDDEN", "closed_at cannot follow submitted_at")
    elif command_type == "AnnulQuestion":
        if state == "FINAL":
            result.add("TRANSITION_FORBIDDEN", "a FINAL question cannot be annulled")
        elif payload["annulled_by"] != question["registration"]["owner_actor_id"]:
            result.add("PERMISSION_DENIED", "question.annul_own is limited to the registered owner")
        elif payload["annulment_reason"] not in question["registration"]["annulment_rules"]:
            result.add("TRANSITION_FORBIDDEN", "annulment_reason is not registered on the question")
        elif (
            question["registration"]["independent_verifier_actor_id"] is not None
            and not payload["independent_approval_ref"]
        ):
            result.add("EVIDENCE_REQUIRED", "protected question annulment requires independent approval")
    elif command_type == "ProposeResolution":
        if state not in {"CLOSED", "DISPUTED"}:
            result.add("TRANSITION_FORBIDDEN", "resolution may be proposed only from CLOSED or DISPUTED")
        elif payload["proposed_by"] != question["registration"]["resolver_actor_id"]:
            result.add("PERMISSION_DENIED", "resolution proposal requires the registered resolver")
        elif payload["outcome_value"] == "NO" and question["registration"]["negative_search_procedure"]:
            if not payload["negative_search_attempt"]:
                result.add("EVIDENCE_REQUIRED", "absence-based NO requires a negative search attempt")
        elif payload["outcome_value"] == "ANNULLED" and payload["annulment_reason"] not in question["registration"]["annulment_rules"]:
            result.add("TRANSITION_FORBIDDEN", "annulment_reason is not registered on the question")
    elif command_type == "VerifyResolution":
        proposal = question["resolution"]
        if state != "RESOLUTION_PROPOSED" or proposal is None:
            result.add("TRANSITION_FORBIDDEN", "verification requires a proposed resolution")
        elif payload["resolution_id"] != proposal["resolution_id"]:
            result.add("TRANSITION_FORBIDDEN", "verification resolution_id does not match the proposal")
        elif payload["verified_outcome_value"] != proposal["outcome_value"]:
            result.add("TRANSITION_FORBIDDEN", "disagreement must use DisputeResolution")
        else:
            _protected_verification(result, command, question, replayed)
    elif command_type == "DisputeResolution":
        proposal = question["resolution"]
        if state != "RESOLUTION_PROPOSED" or proposal is None:
            result.add("TRANSITION_FORBIDDEN", "dispute requires a proposed resolution")
        elif payload["resolution_id"] != proposal["resolution_id"]:
            result.add("TRANSITION_FORBIDDEN", "dispute resolution_id does not match the proposal")
    elif command_type == "CorrectResolution":
        proposal = question["resolution"]
        if state != "FINAL" or proposal is None or question["outcome"] == "ANNULLED":
            result.add("TRANSITION_FORBIDDEN", "correction requires a verified FINAL resolution")
        elif payload["resolution_id"] != proposal["resolution_id"]:
            result.add("TRANSITION_FORBIDDEN", "correction resolution_id does not match FINAL resolution")
    return result


def _reduce_question_stream(
    result: ReplayResult,
    stream_id: str,
    ordered: list[dict[str, Any]],
) -> bool:
    first = ordered[0]
    if first["event_type"] != "QuestionRegistered":
        result.findings.append(Finding("STREAM_TRANSITION_INVALID", "question stream must begin with QuestionRegistered", stream_id))
        return False
    question_id = first["payload"]["question_id"]
    state: dict[str, Any] = {
        "question_id": question_id,
        "state": "OPEN",
        "registration": first["payload"],
        "resolution": None,
        "outcome": None,
        "latest_event": first,
    }
    for event in ordered[1:]:
        event_type = event["event_type"]
        payload = event["payload"]
        valid = True
        if payload.get("question_id") != question_id:
            valid = False
        elif event_type == "QuestionClosed" and state["state"] == "OPEN":
            state["state"] = "CLOSED"
        elif event_type == "QuestionAnnulled" and state["state"] != "FINAL":
            state["state"] = "FINAL"
            state["outcome"] = "ANNULLED"
        elif event_type == "ResolutionProposed" and state["state"] in {"CLOSED", "DISPUTED"}:
            state["state"] = "RESOLUTION_PROPOSED"
            state["resolution"] = payload
        elif (
            event_type == "ResolutionVerified"
            and state["state"] == "RESOLUTION_PROPOSED"
            and state["resolution"] is not None
            and payload["resolution_id"] == state["resolution"]["resolution_id"]
            and payload["verified_outcome_value"] == state["resolution"]["outcome_value"]
        ):
            state["state"] = "FINAL"
            state["outcome"] = payload["verified_outcome_value"]
        elif (
            event_type == "ResolutionDisputed"
            and state["state"] == "RESOLUTION_PROPOSED"
            and state["resolution"] is not None
            and payload["resolution_id"] == state["resolution"]["resolution_id"]
        ):
            state["state"] = "DISPUTED"
        elif (
            event_type == "ResolutionCorrected"
            and state["state"] == "FINAL"
            and state["outcome"] != "ANNULLED"
            and state["resolution"] is not None
            and payload["resolution_id"] == state["resolution"]["resolution_id"]
        ):
            state["outcome"] = payload["corrected_outcome_value"]
        else:
            valid = False
        if not valid:
            result.findings.append(Finding("STREAM_TRANSITION_INVALID", event["event_id"], stream_id))
            return False
        state["latest_event"] = event
    result.question_states[question_id] = state
    return True


def _reduce_forecast_stream(
    result: ReplayResult,
    stream_id: str,
    ordered: list[dict[str, Any]],
) -> bool:
    first = ordered[0]
    if first["event_type"] != "ForecastSubmitted":
        result.findings.append(Finding("STREAM_TRANSITION_INVALID", "forecast stream must begin with ForecastSubmitted", stream_id))
        return False
    payload = first["payload"]
    forecast_id = payload["forecast_id"]
    state: dict[str, Any] = {
        "forecast_id": forecast_id,
        "question_id": payload["question_id"],
        "forecaster_actor_id": payload["forecaster_actor_id"],
        "state": "ACTIVE",
        "versions": [payload],
        "latest_event": first,
    }
    for event in ordered[1:]:
        event_payload = event["payload"]
        valid_identity = (
            event_payload.get("forecast_id") == forecast_id
            and event_payload.get("question_id") == state["question_id"]
            and event_payload.get("forecaster_actor_id") == state["forecaster_actor_id"]
        )
        if (
            event["event_type"] == "ForecastAmended"
            and state["state"] == "ACTIVE"
            and valid_identity
            and event_payload["forecast_version"] == state["versions"][-1]["forecast_version"] + 1
        ):
            state["versions"].append(event_payload)
        elif event["event_type"] == "ForecastWithdrawn" and state["state"] == "ACTIVE" and valid_identity:
            state["state"] = "WITHDRAWN"
        else:
            result.findings.append(Finding("STREAM_TRANSITION_INVALID", event["event_id"], stream_id))
            return False
        state["latest_event"] = event
    result.forecast_states[forecast_id] = state
    return True


def _protected_verification(
    result: ValidationResult,
    command: dict[str, Any],
    question: dict[str, Any],
    replayed: ReplayResult,
) -> None:
    designated = question["registration"]["independent_verifier_actor_id"]
    if designated is None:
        return
    verifier = command["payload"]["verified_by"]
    forecast_owners = {
        state["forecaster_actor_id"]
        for state in replayed.forecast_states.values()
        if state["question_id"] == question["question_id"]
    }
    proposer = question["resolution"]["proposed_by"]
    if verifier != designated or verifier in forecast_owners or verifier in {proposer, "PROME"}:
        result.add(
            "PROTECTED_SELF_VERIFICATION",
            "protected outcome requires the designated independent verifier with no prohibited role overlap",
        )
