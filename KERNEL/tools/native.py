"""Exact, read-only native-reference verification for fixture-only Kernel v1."""

from __future__ import annotations

import hashlib
import json
import posixpath
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

from core import Finding, canonical_bytes


FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
MATERIAL_FIELDS = {
    "RegisterQuestion": {
        "owner_actor_id", "claim", "forecast_family", "opens_at", "closes_at",
        "resolver_anchor_type", "resolution_condition", "resolution_rule",
        "resolution_sources", "fallback_resolution_source", "ambiguity_rule",
        "annulment_rules", "resolver_actor_id", "independent_verifier_actor_id",
        "negative_search_procedure",
    },
    "SubmitForecast": {
        "question_id", "forecaster_actor_id", "information_as_of", "probability",
        "rationale_ref", "evidence_refs", "intervention_stage", "decision_consequence",
    },
}


class GitBoundary(Protocol):
    def resolve_commit(self, source_commit: str) -> str | None: ...
    def read_blob(self, source_commit: str, path: str) -> bytes | None: ...


class SubprocessGitBoundary:
    """Read committed objects without consulting files in the working tree."""

    def __init__(self, repository: str | Path):
        self.repository = Path(repository)

    def _run(self, *args: str) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            ["git", "-C", str(self.repository), *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )

    def resolve_commit(self, source_commit: str) -> str | None:
        if not FULL_SHA.fullmatch(source_commit):
            return None
        result = self._run("rev-parse", "--verify", f"{source_commit}^{{commit}}")
        resolved = result.stdout.strip().decode("ascii", errors="ignore")
        return resolved if result.returncode == 0 and FULL_SHA.fullmatch(resolved) else None

    def read_blob(self, source_commit: str, path: str) -> bytes | None:
        result = self._run("cat-file", "blob", f"{source_commit}:{path}")
        return result.stdout if result.returncode == 0 else None


@dataclass
class NativeVerificationResult:
    findings: list[Finding] = field(default_factory=list)
    selected_bytes: list[bytes] = field(default_factory=list)
    selected_values: list[Any] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return not self.findings


def normalized_repository_path(path: Any) -> bool:
    if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
        return False
    if path.endswith("/") or "//" in path or any(part in {"", ".", ".."} for part in path.split("/")):
        return False
    return posixpath.normpath(path) == path


def _tsv_select(blob: bytes, locator: str) -> tuple[bytes | None, Any | None, Finding | None]:
    if "=" not in locator:
        return None, None, Finding("NATIVE_LOCATOR_INVALID", "TSV locator must be column=value")
    id_column, record_id = locator.split("=", 1)
    if not id_column or not record_id or "\t" in locator or "\n" in locator:
        return None, None, Finding("NATIVE_LOCATOR_INVALID", "TSV locator must be column=value")

    lines = blob.splitlines(keepends=True)
    candidates = [(line.rstrip(b"\r\n"), line) for line in lines if line.strip() and not line.lstrip().startswith(b"#")]
    if not candidates:
        return None, None, Finding("NATIVE_RECORD_INVALID", "TSV has no header")
    try:
        header = candidates[0][0].decode("utf-8").split("\t")
    except UnicodeDecodeError:
        return None, None, Finding("NATIVE_RECORD_INVALID", "TSV is not UTF-8")
    if len(header) != len(set(header)) or any(not value for value in header):
        return None, None, Finding("NATIVE_RECORD_INVALID", "TSV header is empty or duplicated")
    if id_column not in header:
        return None, None, Finding("NATIVE_RECORD_INVALID", f"declared ID column is absent: {id_column}")
    id_index = header.index(id_column)
    matches: list[tuple[bytes, dict[str, str]]] = []
    for raw_without_eol, raw_line in candidates[1:]:
        try:
            cells = raw_without_eol.decode("utf-8").split("\t")
        except UnicodeDecodeError:
            return None, None, Finding("NATIVE_RECORD_INVALID", "TSV row is not UTF-8")
        if len(cells) != len(header):
            return None, None, Finding("NATIVE_RECORD_INVALID", "TSV row width does not match header")
        if cells == header:
            return None, None, Finding("NATIVE_RECORD_INVALID", "TSV contains more than one header")
        if cells[id_index] == record_id:
            matches.append((raw_line, dict(zip(header, cells))))
    if not matches:
        return None, None, Finding("NATIVE_RECORD_MISSING", f"record not found: {record_id}")
    if len(matches) != 1:
        return None, None, Finding("NATIVE_RECORD_AMBIGUOUS", f"record is not unique: {record_id}")
    return matches[0][0], matches[0][1], None


def _json_pointer_select(blob: bytes, pointer: str) -> tuple[bytes | None, Any | None, Finding | None]:
    class DuplicateJsonMember(ValueError):
        pass

    def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise DuplicateJsonMember(f"duplicate JSON member: {key}")
            result[key] = value
        return result

    def reject_constant(value: str) -> None:
        raise ValueError(f"non-standard JSON constant: {value}")

    try:
        value = json.loads(blob.decode("utf-8"), object_pairs_hook=strict_object, parse_constant=reject_constant)
    except DuplicateJsonMember:
        return None, None, Finding("NATIVE_RECORD_AMBIGUOUS", "companion artifact contains duplicate JSON members")
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError):
        return None, None, Finding("NATIVE_RECORD_INVALID", "companion artifact is not strict JSON")
    if pointer == "":
        selected = value
    elif not pointer.startswith("/"):
        return None, None, Finding("NATIVE_JSON_POINTER_INVALID", "JSON Pointer must be empty or begin with /")
    else:
        selected = value
        for raw_token in pointer[1:].split("/"):
            if re.search(r"~(?![01])", raw_token):
                return None, None, Finding("NATIVE_JSON_POINTER_INVALID", "JSON Pointer has invalid escape")
            token = raw_token.replace("~1", "/").replace("~0", "~")
            if isinstance(selected, dict):
                if token not in selected:
                    return None, None, Finding("NATIVE_RECORD_MISSING", f"JSON Pointer member not found: {token}")
                selected = selected[token]
            elif isinstance(selected, list):
                if token == "-" or not re.fullmatch(r"0|[1-9][0-9]*", token):
                    return None, None, Finding("NATIVE_JSON_POINTER_INVALID", "JSON Pointer array index is invalid")
                index = int(token)
                if index >= len(selected):
                    return None, None, Finding("NATIVE_RECORD_MISSING", f"JSON Pointer index not found: {token}")
                selected = selected[index]
            else:
                return None, None, Finding("NATIVE_RECORD_MISSING", "JSON Pointer traverses a scalar")
    return canonical_bytes(selected), selected, None


def _native_field_map(values: list[Any]) -> dict[str, list[Any]]:
    fields: dict[str, list[Any]] = {}
    def visit(value: Any) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                fields.setdefault(key, []).append(child)
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    for value in values:
        visit(value)
    return fields


def _equivalent(native: Any, expected: Any) -> bool:
    if native == expected:
        return True
    if isinstance(native, str):
        if native == json.dumps(expected, sort_keys=True, separators=(",", ":"), ensure_ascii=False):
            return True
        if expected is None and native.lower() in {"", "null", "none"}:
            return True
        if isinstance(expected, (int, float)) and not isinstance(expected, bool):
            return native == str(expected)
    return False


def verify_native_references(command: dict[str, Any], git: GitBoundary) -> NativeVerificationResult:
    result = NativeVerificationResult()
    for index, ref in enumerate(command.get("native_refs", [])):
        location = f"$.native_refs[{index}]"
        source_commit = ref.get("source_commit")
        path = ref.get("path")
        if not FULL_SHA.fullmatch(source_commit or "") or git.resolve_commit(source_commit) != source_commit:
            result.findings.append(Finding("NATIVE_COMMIT_MISSING", "full source commit does not exist", f"{location}.source_commit"))
            continue
        if not normalized_repository_path(path):
            result.findings.append(Finding("NATIVE_PATH_INVALID", "path is not normalized repository-relative", f"{location}.path"))
            continue
        blob = git.read_blob(source_commit, path)
        if blob is None:
            result.findings.append(Finding("NATIVE_PATH_MISSING", "path does not exist at source commit", f"{location}.path"))
            continue
        locator_type = ref.get("locator_type")
        if locator_type == "TSV_RECORD_ID":
            selected_bytes, selected_value, finding = _tsv_select(blob, ref.get("locator", ""))
        elif locator_type == "JSON_POINTER":
            selected_bytes, selected_value, finding = _json_pointer_select(blob, ref.get("locator", ""))
        else:
            selected_bytes, selected_value, finding = None, None, Finding("NATIVE_LOCATOR_INVALID", "unsupported locator type")
        if finding:
            result.findings.append(Finding(finding.code, finding.message, f"{location}.locator"))
            continue
        assert selected_bytes is not None
        if hashlib.sha256(selected_bytes).hexdigest() != ref.get("raw_record_sha256"):
            result.findings.append(Finding("NATIVE_BLOB_MISMATCH", "selected native bytes do not match raw_record_sha256", f"{location}.raw_record_sha256"))
            continue
        result.selected_bytes.append(selected_bytes)
        result.selected_values.append(selected_value)

    if result.findings:
        return result
    material = MATERIAL_FIELDS.get(command.get("command_type"), set())
    payload = command.get("payload", {})
    native_fields = _native_field_map(result.selected_values)
    for field_name in sorted(material):
        expected = payload.get(field_name)
        if not any(_equivalent(candidate, expected) for candidate in native_fields.get(field_name, [])):
            result.findings.append(Finding(
                "NATIVE_RECORD_MISMATCH",
                f"material field is absent or differs in cited native records: {field_name}",
                f"$.payload.{field_name}",
            ))
    return result
