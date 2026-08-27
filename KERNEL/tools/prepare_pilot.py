#!/usr/bin/env python3
"""Prepare the approved SAM-33 commands inside a marked disposable clone only."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from core import canonical_bytes, validate_command
from native import SubprocessGitBoundary, verify_native_references


LIVE_REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
MARKER_DOCUMENT = {"authority": "NON_AUTHORITATIVE", "mode": "SYNTHETIC_MIRROR"}
COMPANION_PATH = "AGENTS/SAM/thesis/SAM-33_KERNEL_NATIVE_COMPANION.json"
TSV_PATH = "AGENTS/SAM/thesis/PREDICTIONS.tsv"
QUESTION_COMMAND_ID = "CMD-019305f8-ec00-7000-8000-000000000033"
FORECAST_COMMAND_ID = "CMD-019305f8-ec00-7000-8000-000000000034"
EVENT_IDS = {
    QUESTION_COMMAND_ID: "EVT-019305f8-ec00-7000-8000-000000000033",
    FORECAST_COMMAND_ID: "EVT-019305f8-ec00-7000-8000-000000000034",
}


def prepare(root: Path, source_commit: str, submitted_at: str) -> dict[str, object]:
    root = root.resolve()
    live = LIVE_REPOSITORY_ROOT.resolve()
    if root == live or live in root.parents or root in live.parents:
        raise ValueError("pilot preparation refuses the live repository tree")
    marker = json.loads((root / ".gate-c-synthetic-mirror.json").read_text(encoding="utf-8"))
    if marker != MARKER_DOCUMENT:
        raise ValueError("exact synthetic mirror marker is required")
    git = SubprocessGitBoundary(root)
    if git.resolve_commit(source_commit) != source_commit:
        raise ValueError("source_commit must resolve as one exact full commit")
    companion_blob = git.read_blob(source_commit, COMPANION_PATH)
    tsv_blob = git.read_blob(source_commit, TSV_PATH)
    if companion_blob is None or tsv_blob is None:
        raise ValueError("approved native records are absent at source_commit")
    companion = json.loads(companion_blob.decode("utf-8"))
    row = next((line for line in tsv_blob.splitlines(keepends=True) if line.startswith(b"SAM-33\t")), None)
    if row is None:
        raise ValueError("SAM-33 row is absent at source_commit")

    def native_ref(path: str, locator_type: str, locator: str, selected: bytes) -> dict[str, str]:
        return {
            "repository": "williepowen-debug/Research-workspace",
            "source_commit": source_commit,
            "path": path,
            "locator_type": locator_type,
            "locator": locator,
            "raw_record_sha256": hashlib.sha256(selected).hexdigest(),
        }

    tsv_ref = native_ref(TSV_PATH, "TSV_RECORD_ID", "Pred_ID=SAM-33", row)
    question_ref = native_ref(COMPANION_PATH, "JSON_POINTER", "/question", canonical_bytes(companion["question"]))
    forecast_ref = native_ref(COMPANION_PATH, "JSON_POINTER", "/forecast", canonical_bytes(companion["forecast"]))
    common = {
        "schema_version": "kernel.schema.1",
        "policy_version": "kernel.policy.1",
        "actor_id": "SAM",
        "submitted_at": submitted_at,
        "correlation_id": "gate-c-sam-33-pilot",
        "caused_by": None,
    }
    question = common | {
        "command_id": QUESTION_COMMAND_ID,
        "command_type": "RegisterQuestion",
        "expected_version": 0,
        "target_stream_id": f"QS-{companion['question']['question_id']}",
        "depends_on": [],
        "payload": companion["question"],
        "native_refs": [tsv_ref, question_ref],
    }
    forecast = common | {
        "command_id": FORECAST_COMMAND_ID,
        "command_type": "SubmitForecast",
        "expected_version": 0,
        "target_stream_id": f"FS-{companion['forecast']['forecast_id']}",
        "depends_on": [QUESTION_COMMAND_ID],
        "payload": companion["forecast"],
        "native_refs": [tsv_ref, forecast_ref],
    }
    for name, command in (("question", question), ("forecast", forecast)):
        contract = validate_command(command)
        native = verify_native_references(command, git)
        if not contract.valid or not native.valid:
            codes = sorted({finding.code for finding in contract.findings + native.findings})
            raise ValueError(f"{name} preparation failed: {','.join(codes)}")

    submission_root = root / "AGENTS" / "SAM" / "outbox" / "kernel" / "submissions"
    submission_root.mkdir(parents=True, exist_ok=True)
    paths: list[str] = []
    for command in (question, forecast):
        relative = f"AGENTS/SAM/outbox/kernel/submissions/{command['command_id']}.json"
        destination = root / relative
        with destination.open("xb") as handle:
            handle.write(canonical_bytes(command) + b"\n")
        paths.append(relative)
    rw = root / ".rw" / "rehearsal"
    rw.mkdir(parents=True, exist_ok=True)
    (rw / "inventory.json").write_bytes(canonical_bytes(paths) + b"\n")
    (rw / "event-ids.json").write_bytes(canonical_bytes(EVENT_IDS) + b"\n")
    return {
        "notice": "SHADOW — NON-AUTHORITATIVE",
        "source_commit": source_commit,
        "submissions": paths,
        "inventory": str(rw / "inventory.json"),
        "event_ids": str(rw / "event-ids.json"),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mirror", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--submitted-at", required=True)
    args = parser.parse_args(argv)
    try:
        report = prepare(args.mirror, args.source_commit, args.submitted_at)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print("notice: SHADOW — NON-AUTHORITATIVE")
        print("EXCEPTION: pilot-preparation")
        print(f"PILOT_PREPARATION_INVALID\t$input\t{exc}")
        return 1
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
