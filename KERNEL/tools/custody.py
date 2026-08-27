"""Deterministic Gate C primary/substitute custody policy for synthetic testing."""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field
from typing import Any, Iterable

from core import Finding, ValidationResult, sha256_hex


TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
POLICY_FIELDS = {"schema_version", "policy_version", "primary_writer_id", "substitutes"}
SUBSTITUTE_FIELDS = {"writer_id", "command_accept_default", "registered_by"}
ACTIVATION_FIELDS = {
    "schema_version", "policy_version", "activation_id", "authorized_by",
    "substitute_writer_id", "window_start", "window_end", "command_ids", "revoked_at",
}
REVIEW_FIELDS = {
    "schema_version", "policy_version", "activation_id", "reviewed_by",
    "reviewed_at", "result_hashes",
}


@dataclass(frozen=True)
class CustodyPolicy:
    schema_version: str
    policy_version: str
    primary_writer_id: str
    dormant_substitutes: frozenset[str]


@dataclass(frozen=True)
class SubstituteActivation:
    schema_version: str
    policy_version: str
    activation_id: str
    substitute_writer_id: str
    window_start: dt.datetime
    window_end: dt.datetime
    command_ids: frozenset[str]
    revoked_at: dt.datetime | None

    def active_at(self, instant: dt.datetime) -> bool:
        end = self.revoked_at if self.revoked_at is not None else self.window_end
        return self.window_start <= instant < end


@dataclass
class CustodyLoad:
    policy: CustodyPolicy | None = None
    activation: SubstituteActivation | None = None
    findings: list[Finding] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return not self.findings and self.policy is not None


def load_custody(policy_document: Any, activation_document: Any | None = None) -> CustodyLoad:
    findings: list[Finding] = []
    policy: CustodyPolicy | None = None
    activation: SubstituteActivation | None = None
    if not isinstance(policy_document, dict) or set(policy_document) != POLICY_FIELDS:
        findings.append(Finding("CUSTODY_POLICY_INVALID", "custody policy fields are invalid", "$policy"))
    else:
        schema = policy_document["schema_version"]
        version = policy_document["policy_version"]
        primary = policy_document["primary_writer_id"]
        substitutes = policy_document["substitutes"]
        if schema != "kernel.custody.1" or version != "kernel.policy.1":
            findings.append(Finding("CUSTODY_POLICY_INVALID", "unsupported custody schema or policy version", "$policy"))
        if not isinstance(primary, str) or not primary:
            findings.append(Finding("CUSTODY_POLICY_INVALID", "primary_writer_id must be non-empty", "$.primary_writer_id"))
        dormant: set[str] = set()
        if not isinstance(substitutes, list) or not substitutes:
            findings.append(Finding("CUSTODY_POLICY_INVALID", "at least one dormant substitute is required", "$.substitutes"))
        else:
            for index, item in enumerate(substitutes):
                location = f"$.substitutes[{index}]"
                if not isinstance(item, dict) or set(item) != SUBSTITUTE_FIELDS:
                    findings.append(Finding("CUSTODY_POLICY_INVALID", "substitute fields are invalid", location))
                    continue
                writer = item["writer_id"]
                if not isinstance(writer, str) or not writer or writer == primary or writer in dormant:
                    findings.append(Finding("CUSTODY_POLICY_INVALID", "substitute writer_id is invalid or duplicate", location))
                elif item["command_accept_default"] is not False:
                    findings.append(Finding("CUSTODY_POLICY_INVALID", "substitute must be disabled by default", location))
                elif item["registered_by"] != "WILL":
                    findings.append(Finding("CUSTODY_POLICY_INVALID", "substitute must be registered by WILL", location))
                else:
                    dormant.add(writer)
        if not findings:
            policy = CustodyPolicy(schema, version, primary, frozenset(dormant))

    if activation_document is not None:
        activation = _load_activation(activation_document, policy, findings)
    return CustodyLoad(policy, activation, findings)


def _load_activation(document: Any, policy: CustodyPolicy | None, findings: list[Finding]) -> SubstituteActivation | None:
    if not isinstance(document, dict) or set(document) != ACTIVATION_FIELDS:
        findings.append(Finding("CUSTODY_ACTIVATION_INVALID", "activation fields are invalid", "$activation"))
        return None
    if policy is None or document["schema_version"] != policy.schema_version or document["policy_version"] != policy.policy_version:
        findings.append(Finding("CUSTODY_ACTIVATION_INVALID", "activation versions do not match custody policy", "$activation"))
        return None
    writer = document["substitute_writer_id"]
    if writer not in policy.dormant_substitutes or document["authorized_by"] != "WILL":
        findings.append(Finding("CUSTODY_ACTIVATION_INVALID", "activation must name a registered substitute and WILL", "$activation"))
        return None
    try:
        start = _timestamp(document["window_start"])
        end = _timestamp(document["window_end"])
        revoked = _timestamp(document["revoked_at"]) if document["revoked_at"] is not None else None
    except (TypeError, ValueError):
        findings.append(Finding("CUSTODY_ACTIVATION_INVALID", "activation timestamps must be strict UTC timestamps", "$activation"))
        return None
    commands = document["command_ids"]
    if start >= end or not isinstance(commands, list) or not 1 <= len(commands) <= 3 or any(not isinstance(v, str) or not v for v in commands) or len(set(commands)) != len(commands):
        findings.append(Finding("CUSTODY_ACTIVATION_INVALID", "window or one-to-three command perimeter is invalid", "$activation"))
        return None
    if revoked is not None and not (start <= revoked <= end):
        findings.append(Finding("CUSTODY_ACTIVATION_INVALID", "revocation must fall within the activation window", "$.revoked_at"))
        return None
    activation_id = document["activation_id"]
    if not isinstance(activation_id, str) or not activation_id:
        findings.append(Finding("CUSTODY_ACTIVATION_INVALID", "activation_id must be non-empty", "$.activation_id"))
        return None
    return SubstituteActivation(policy.schema_version, policy.policy_version, activation_id, writer, start, end, frozenset(commands), revoked)


def authorize_writer(load: CustodyLoad, writer_id: str, command_id: str, recorded_at: str) -> ValidationResult:
    result = ValidationResult()
    if not load.valid:
        result.add("CUSTODY_UNKNOWN", "custody policy or activation is invalid")
        return result
    try:
        instant = _timestamp(recorded_at)
    except (TypeError, ValueError):
        result.add("CUSTODY_UNKNOWN", "recorded_at is not a strict UTC timestamp", "$.recorded_at")
        return result
    assert load.policy is not None
    activation = load.activation
    active_substitute = activation is not None and activation.active_at(instant)
    if writer_id == load.policy.primary_writer_id:
        if active_substitute:
            result.add("CUSTODY_DENIED", "primary custody is suspended during the substitute window", "$.writer_id")
        return result
    if writer_id not in load.policy.dormant_substitutes:
        result.add("CUSTODY_DENIED", "writer is not registered for custody", "$.writer_id")
    elif not active_substitute or activation is None or writer_id != activation.substitute_writer_id:
        result.add("CUSTODY_DENIED", "substitute custody is dormant or outside its window", "$.writer_id")
    elif command_id not in activation.command_ids:
        result.add("CUSTODY_DENIED", "command is outside the substitute activation perimeter", "$.command_id")
    return result


def run_with_custody(
    runner: Any,
    load: CustodyLoad,
    *,
    writer_id: str,
    recorded_at: str,
    submissions: Iterable[dict[str, Any]],
    submission_paths: dict[str, str],
) -> Any:
    """Authorize custody before entering the integrated acceptance lock or writer."""

    from acceptance import AcceptanceCheck, AcceptanceRun, CLAIMS

    supplied = tuple(submissions)
    checks: list[AcceptanceCheck] = []
    blocked = False
    unknown = False
    for command in supplied:
        command_id = command.get("command_id", "") if isinstance(command, dict) else ""
        decision = authorize_writer(load, writer_id, command_id, recorded_at)
        if decision.valid:
            status = "PASS"
        elif any(finding.code in {"CUSTODY_UNKNOWN", "CUSTODY_AUDIT_UNKNOWN"} for finding in decision.findings):
            status = "UNKNOWN"
            unknown = True
            blocked = True
        else:
            status = "EXCEPTION"
            blocked = True
        checks.append(AcceptanceCheck(
            "custody",
            status,
            f"writer_id={writer_id} command_id={command_id} recorded_at={recorded_at}",
            "the named writer holds custody for this command at the injected instant",
            "research authority, command validity, or permission to process any other command",
            tuple(decision.findings),
        ))
    if blocked:
        status = "UNKNOWN" if unknown else "EXCEPTION"
        proves, does_not = CLAIMS["aggregate"]
        checks.append(AcceptanceCheck(
            "aggregate",
            status,
            f"custody_preflight=true explicit_submissions={len(supplied)} durable_outcomes=0",
            proves,
            does_not,
        ))
        return AcceptanceRun(checks=checks)
    run = runner.run(supplied, submission_paths)
    run.checks[0:0] = checks
    return run


def audit_return(load: CustodyLoad, results: Iterable[dict[str, Any]], review: Any) -> ValidationResult:
    result = ValidationResult()
    if not load.valid or load.activation is None:
        result.add("CUSTODY_AUDIT_UNKNOWN", "valid substitute activation is required")
        return result
    activation = load.activation
    if not isinstance(review, dict) or set(review) != REVIEW_FIELDS:
        result.add("CUSTODY_AUDIT_INVALID", "return review fields are invalid", "$review")
        return result
    if review["schema_version"] != activation.schema_version or review["policy_version"] != activation.policy_version or review["activation_id"] != activation.activation_id:
        result.add("CUSTODY_AUDIT_INVALID", "review does not identify the active policy and activation", "$review")
    assert load.policy is not None
    if review["reviewed_by"] != load.policy.primary_writer_id:
        result.add("CUSTODY_AUDIT_INVALID", "primary custodian must perform the return review", "$.reviewed_by")
    try:
        reviewed_at = _timestamp(review["reviewed_at"])
        closed_at = activation.revoked_at if activation.revoked_at is not None else activation.window_end
        if reviewed_at < closed_at:
            result.add("CUSTODY_AUDIT_INVALID", "return review cannot predate window closure", "$.reviewed_at")
    except (TypeError, ValueError):
        result.add("CUSTODY_AUDIT_INVALID", "reviewed_at is not a strict UTC timestamp", "$.reviewed_at")
    hashes = review["result_hashes"]
    if not isinstance(hashes, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in hashes.items()):
        result.add("CUSTODY_AUDIT_INVALID", "result_hashes must be a string map", "$.result_hashes")
        return result
    supplied: dict[str, dict[str, Any]] = {}
    for document in results:
        command_id = document.get("command_id") if isinstance(document, dict) else None
        if not isinstance(command_id, str) or command_id in supplied:
            result.add("CUSTODY_AUDIT_INVALID", "results contain invalid or duplicate command identity", "$results")
            continue
        supplied[command_id] = document
        if document.get("writer_id") != activation.substitute_writer_id:
            result.add("CUSTODY_AUDIT_INVALID", "result writer does not match activated substitute", f"$results.{command_id}")
        recorded_at = document.get("recorded_at")
        try:
            if not activation.active_at(_timestamp(recorded_at)):
                result.add("CUSTODY_AUDIT_INVALID", "result falls outside the activation window", f"$results.{command_id}.recorded_at")
        except (TypeError, ValueError):
            result.add("CUSTODY_AUDIT_INVALID", "result recorded_at is invalid", f"$results.{command_id}.recorded_at")
    if set(supplied) != set(activation.command_ids) or set(hashes) != set(activation.command_ids):
        result.add("CUSTODY_AUDIT_GAP", "activation, results, and reviewed hashes must name the same commands", "$results")
    for command_id in set(supplied) & set(hashes):
        if hashes[command_id] != sha256_hex(supplied[command_id]):
            result.add("CUSTODY_AUDIT_INVALID", "reviewed result hash does not match exact result bytes", f"$.result_hashes.{command_id}")
    return result


def _timestamp(value: Any) -> dt.datetime:
    if not isinstance(value, str):
        raise TypeError("timestamp must be a string")
    parsed = dt.datetime.strptime(value, TIMESTAMP_FORMAT).replace(tzinfo=dt.timezone.utc)
    if parsed.strftime(TIMESTAMP_FORMAT) != value:
        raise ValueError("timestamp is not canonical")
    return parsed
