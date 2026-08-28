"""Byte-deterministic registered-view rendering for Kernel v1 fixtures."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from decimal import Decimal
from pathlib import Path
from typing import Any, Iterable

from core import AUTHORITY_MODE, POLICY_VERSION, SCHEMA_VERSION, Finding, canonical_bytes, replay


RENDERER_VERSION = "kernel.renderer.2"   # .2 (2026-08-28): registered projection exclusions in CALIBRATION.tsv
EXCLUSIONS_SCHEMA_VERSION = "kernel.projection-exclusions.1"
EXCLUSION_REASONS = frozenset({"OUTCOME_VOCABULARY_MISMATCH"})
DEFAULT_EXCLUSIONS_RELPATH = Path("KERNEL/policies/projection-exclusions.json")
NOTICE = "GENERATED — DO NOT EDIT — NON-AUTHORITATIVE"
VIEW_NAMES = ("OPEN_QUESTIONS.md", "RESOLUTION_QUEUE.md", "EXCEPTIONS.md", "CALIBRATION.tsv")


def _source_digest(inputs: Iterable[dict[str, Any]]) -> tuple[int, str]:
    identities: list[tuple[str, str, str]] = []
    for value in inputs:
        kind = "event" if "event_id" in value else ("registry" if "registry_id" in value else "input")
        identity = str(value.get("event_id") or value.get("command_id") or value.get("receipt_id")
                       or value.get("registry_id") or "UNIDENTIFIED")
        digest = hashlib.sha256(canonical_bytes(value)).hexdigest()
        identities.append((kind, identity, digest))
    identities.sort()
    return len(identities), hashlib.sha256(canonical_bytes(identities)).hexdigest()


def _metadata(render_as_of: str, inputs: list[dict[str, Any]]) -> list[tuple[str, str]]:
    count, digest = _source_digest(inputs)
    return [
        ("authority_mode", AUTHORITY_MODE),
        ("render_as_of", render_as_of),
        ("source_input_count", str(count)),
        ("source_input_set_sha256", digest),
        ("schema_versions", SCHEMA_VERSION),
        ("policy_versions", POLICY_VERSION),
        ("renderer_version", RENDERER_VERSION),
        ("notice", NOTICE),
    ]


def _markdown_header(title: str, metadata: list[tuple[str, str]]) -> list[str]:
    lines = [f"# {title}", ""]
    lines.extend(f"**{key}:** {value}" for key, value in metadata)
    lines.extend(["", f"> {NOTICE}", ""])
    return lines


def _escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def validate_projection_exclusions(value: Any) -> dict[str, dict[str, Any]]:
    """Validate a projection-exclusions registry; return {question_id: entry}.

    Fail-closed on any malformation (ValueError) — an unreadable registry must
    never degrade to "no exclusions", because the failure mode this guards is a
    score that looks correct. Bounded by construction: enumerated reasons, one
    entry per question_id, every entry names who ruled it and where the ruling
    lives. Registered 2026-08-28 (Will "go ahead approved"; Codex audit H2 +
    follow-up: documentation alone did not implement the fence).
    """
    if not isinstance(value, dict):
        raise ValueError("projection exclusions must be a JSON object")
    if value.get("schema_version") != EXCLUSIONS_SCHEMA_VERSION:
        raise ValueError(f"projection exclusions schema_version must be {EXCLUSIONS_SCHEMA_VERSION}")
    if value.get("registry_id") != "projection-exclusions":
        raise ValueError("projection exclusions registry_id must be 'projection-exclusions'")
    entries = value.get("exclusions")
    if not isinstance(entries, list):
        raise ValueError("projection exclusions must carry an 'exclusions' array")
    required = {"question_id", "exclusion_reason", "ruled_by", "ruled_at", "ruling_record"}
    out: dict[str, dict[str, Any]] = {}
    for index, entry in enumerate(entries):
        location = f"$.exclusions[{index}]"
        if not isinstance(entry, dict) or not required.issubset(entry):
            raise ValueError(f"{location} must carry {sorted(required)}")
        for key in required:
            if not isinstance(entry[key], str) or not entry[key].strip():
                raise ValueError(f"{location}.{key} must be a non-empty string")
        if entry["exclusion_reason"] not in EXCLUSION_REASONS:
            raise ValueError(f"{location}.exclusion_reason is not a registered reason")
        if entry["question_id"] in out:
            raise ValueError(f"{location}.question_id duplicates an earlier entry")
        out[entry["question_id"]] = entry
    return out


def load_projection_exclusions(path: Path) -> dict[str, Any] | None:
    """Read + validate the registry file; None when the file is absent (no
    exclusions registered is a legitimate state — a malformed file is not)."""
    if not path.exists():
        return None
    value = json.loads(path.read_text(encoding="utf-8"))
    validate_projection_exclusions(value)
    return value


def _question_and_forecasts(replay_result: Any) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    questions = sorted(replay_result.question_states.values(), key=lambda item: item["question_id"])
    forecasts: dict[str, list[dict[str, Any]]] = {}
    for state in replay_result.forecast_states.values():
        if state["state"] == "ACTIVE":
            forecasts.setdefault(state["question_id"], []).append(state)
    for items in forecasts.values():
        items.sort(key=lambda item: item["forecast_id"])
    return questions, forecasts


def _open_questions(metadata: list[tuple[str, str]], replay_result: Any) -> str:
    lines = _markdown_header("OPEN QUESTIONS — SHADOW", metadata)
    lines.extend(["| Question | Owner | Closes | Claim | Forecasts |", "|---|---|---|---|---|"])
    questions, forecasts = _question_and_forecasts(replay_result)
    questions = [question for question in questions if question["state"] == "OPEN"]
    for question in questions:
        payload = question["registration"]
        attached = forecasts.get(payload["question_id"], [])
        forecast_text = ", ".join(
            f"{item['forecaster_actor_id']}={item['versions'][-1]['probability']}" for item in attached
        ) or "—"
        lines.append(
            f"| {_escape(payload['question_id'])} | {_escape(payload['owner_actor_id'])} | "
            f"{_escape(payload['closes_at'])} | {_escape(payload['claim'])} | {_escape(forecast_text)} |"
        )
    if not questions:
        lines.append("| — | — | — | No replay-valid open fixture questions. | — |")
    return "\n".join(lines) + "\n"


def _resolution_queue(metadata: list[tuple[str, str]], replay_result: Any, render_as_of: str) -> str:
    lines = _markdown_header("RESOLUTION QUEUE — SHADOW", metadata)
    lines.extend(["| Question | State | Resolver | Close time |", "|---|---|---|---|"])
    questions, _ = _question_and_forecasts(replay_result)
    questions = [question for question in questions if question["state"] != "FINAL"]
    for question in questions:
        payload = question["registration"]
        state = question["state"]
        if state == "OPEN":
            state = "OVERDUE" if payload["closes_at"] <= render_as_of else "NOT_DUE"
        lines.append(
            f"| {_escape(payload['question_id'])} | {state} | {_escape(payload['resolver_actor_id'])} | "
            f"{_escape(payload['closes_at'])} |"
        )
    if not questions:
        lines.append("| — | EMPTY | — | — |")
    return "\n".join(lines) + "\n"


def _exceptions(metadata: list[tuple[str, str]], replay_result: Any) -> str:
    lines = _markdown_header("EXCEPTIONS — SHADOW", metadata)
    lines.extend(["| State | Code | Subject | Detail |", "|---|---|---|---|"])
    rows: list[tuple[str, str, str, str]] = []
    for finding in replay_result.findings:
        rows.append(("EXCEPTION", finding.code, finding.location, finding.message))
    for stream_id in replay_result.conflicts:
        rows.append(("EXCEPTION", "STREAM_CONFLICT", stream_id, "Competing events claim one stream version."))
    for state, code, subject, detail in sorted(rows):
        lines.append(f"| {state} | {_escape(code)} | {_escape(subject)} | {_escape(detail)} |")
    if not rows:
        lines.append("| PASS | NONE | declared fixture perimeter | No replay or conflict exceptions. |")
    return "\n".join(lines) + "\n"


def _calibration(metadata: list[tuple[str, str]], replay_result: Any,
                 exclusions: dict[str, dict[str, Any]] | None = None) -> str:
    lines = [f"# {key}: {value}" for key, value in metadata]
    lines.append("question_id\tforecast_id\tforecast_version\tprobability\toutcome\tbrier_score\texclusion_reason")
    rows: list[tuple[str, str, int, Any, str, str, str]] = []
    for forecast in replay_result.forecast_states.values():
        question = replay_result.question_states.get(forecast["question_id"])
        outcome = question["outcome"] if question is not None and question["state"] == "FINAL" else None
        registered = (exclusions or {}).get(forecast["question_id"])
        for version in forecast["versions"]:
            score = ""
            exclusion = "QUESTION_NOT_FINAL"
            if registered is not None:
                # Registered exclusion wins in EVERY state — before finality, and on
                # YES/NO/AMBIGUOUS alike. A binary score on a question whose native
                # forecast carries non-binary mass is a number that looks right.
                exclusion = registered["exclusion_reason"]
            elif outcome in {"YES", "NO"}:
                target = Decimal(1 if outcome == "YES" else 0)
                probability = Decimal(str(version["probability"]))
                score = format(((probability - target) ** 2).normalize(), "f")
                exclusion = ""
            elif outcome is not None:
                exclusion = f"OUTCOME_{outcome}"
            rows.append(
                (
                    forecast["question_id"],
                    forecast["forecast_id"],
                    version["forecast_version"],
                    version["probability"],
                    outcome or "",
                    score,
                    exclusion,
                )
            )
    for row in sorted(rows):
        lines.append("\t".join(str(value) for value in row))
    return "\n".join(lines) + "\n"


def render_views(
    events: Iterable[dict[str, Any]],
    *,
    render_as_of: str,
    context_inputs: Iterable[dict[str, Any]] = (),
    projection_exclusions: dict[str, Any] | None = None,
) -> dict[str, str]:
    """Render the registered views from accepted events.

    ``context_inputs`` (rejected receipts, unprocessed approved submissions)
    join the declared source-input digest but never enter replay — they carry
    provenance for the render perimeter, not lifecycle state.

    ``projection_exclusions`` (the validated registry document, or None) joins
    the digest the same way and is applied by the CALIBRATION view only.
    """

    inputs = list(events)
    context = list(context_inputs)
    exclusions: dict[str, dict[str, Any]] | None = None
    if projection_exclusions is not None:
        exclusions = validate_projection_exclusions(projection_exclusions)
        context.append(projection_exclusions)
    if not isinstance(render_as_of, str):
        raise ValueError("render_as_of must be a UTC RFC 3339 timestamp with six fractional digits")
    try:
        parsed_as_of = dt.datetime.strptime(render_as_of, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError as exc:
        raise ValueError("render_as_of must be a UTC RFC 3339 timestamp with six fractional digits") from exc
    if parsed_as_of.strftime("%Y-%m-%dT%H:%M:%S.%fZ") != render_as_of:
        raise ValueError("render_as_of must use exactly six fractional digits")
    replay_result = replay(inputs)
    metadata = _metadata(render_as_of, inputs + context)
    return {
        "OPEN_QUESTIONS.md": _open_questions(metadata, replay_result),
        "RESOLUTION_QUEUE.md": _resolution_queue(metadata, replay_result, render_as_of),
        "EXCEPTIONS.md": _exceptions(metadata, replay_result),
        "CALIBRATION.tsv": _calibration(metadata, replay_result, exclusions),
    }


def write_views(
    views: dict[str, str],
    output_dir: Path,
    *,
    check: bool = False,
    live_grant: object | None = None,
) -> list[Finding]:
    if live_grant is not None:
        from live_grant import require_live_grant

        grant = require_live_grant(live_grant)
        # Durable view writes under a live grant require the operator window to
        # have been checked at mint (adversarial review 2026-08-27, finding 1
        # residual: the views path must not be read-only by call path alone).
        # check=True is the read/compare mode and stays permitted.
        if not check and not grant.window_enforced:
            raise ValueError(
                "live grant was minted without window enforcement; durable view writes refuse it"
            )
    findings: list[Finding] = []
    if set(views) != set(VIEW_NAMES):
        return [Finding("VIEW_SET_INVALID", "renderer must produce exactly the registered view set")]
    if not check:
        output_dir.mkdir(parents=True, exist_ok=True)
    for name in VIEW_NAMES:
        path = output_dir / name
        expected = views[name]
        if check:
            if not path.exists():
                findings.append(Finding("VIEW_MISSING", name, str(path)))
            elif path.read_text(encoding="utf-8") != expected:
                findings.append(Finding("VIEW_DRIFT", name, str(path)))
        else:
            path.write_text(expected, encoding="utf-8", newline="\n")
    return findings


def _load_events(path: Path) -> list[dict[str, Any]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise ValueError("fixture event input must be a JSON array of objects")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render fixture-only Kernel v1 views")
    parser.add_argument("--events", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--as-of", required=True)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--exclusions", type=Path, default=None,
                        help="projection-exclusions registry (validated; joins the digest; CALIBRATION only)")
    args = parser.parse_args(argv)
    print(
        f"perimeter: check=view-reproduction mode={'check' if args.check else 'render'} "
        f"events={args.events.resolve()} output={args.output.resolve()} render_as_of={args.as_of} "
        f"exclusions={args.exclusions.resolve() if args.exclusions else 'NONE'}"
    )
    try:
        registry = load_projection_exclusions(args.exclusions) if args.exclusions else None
        if args.exclusions and registry is None:
            raise ValueError(f"exclusions registry not found: {args.exclusions}")
        views = render_views(_load_events(args.events), render_as_of=args.as_of, projection_exclusions=registry)
        findings = write_views(views, args.output, check=args.check)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"EXCEPTION: view-reproduction input failed: {exc}")
        print("PASS proves: registered view bytes equal deterministic renderer output for the printed fixture perimeter")
        print("PASS does not prove: coverage of unregistered repository state or undisclosed inputs")
        return 1
    for finding in findings:
        print(f"EXCEPTION {finding.code}: {finding.message} ({finding.location})")
    if findings:
        print("EXCEPTION: view-reproduction verification did not pass")
    else:
        action = "verified" if args.check else "rendered"
        print(f"PASS: registered fixture views {action} deterministically")
    print("PASS proves: registered view bytes equal deterministic renderer output for the printed fixture perimeter")
    print("PASS does not prove: coverage of unregistered repository state or undisclosed inputs")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
