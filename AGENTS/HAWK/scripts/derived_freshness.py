#!/usr/bin/env python3
"""HAWK live aggregate dependency check; independent of the frozen boot suite.

Reader: HAWK CLAUDE boot 6a-3 and closeout 13b. No network, mtime, or grades.
Scope: both HAWK aggregates IN; explicitly enumerated owner inputs below.
Prior art: finding_mtime_is_corrupted_by_git_sync and
finding_derived_surface_fold_is_the_last_writeback (bodies read 2026-09-08).
Bias: any changed input needs review, including an owner's uncommitted edit.
rc 0 = fingerprints agree; 1 = drift; 2 = missing/invalid evidence.
This does not certify semantic consumption or the freshness of external data.
Production acceptance: audits/2026-09-08_derived-acceptance.json names the real
prior/current FALCON STRIKES blobs and actual aggregate clean/defective cases.
Baseline: two aggregates, eleven dependency edges; historical archives excluded.

Workflow: --capture /tmp/hawk-inputs.json BEFORE reading inputs; reconcile both
aggregates, then --record /tmp/hawk-inputs.json. A source change during review
refuses recording. Recording attests only to the reviewed bytes, never to truth.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OWN = "AGENTS/HAWK/"
BRIEFS = [f"AGENTS/{owner}/NEXUS_BRIEF.md" for owner in ("OSPREY", "FALCON")]
DEPENDENCIES = {
    OWN + "domain/energy-strikes/CROSS_WAR_SUMMARY.md": [
        "AGENTS/OSPREY/domain/energy-strikes/STRIKES.tsv",
        "AGENTS/FALCON/domain/energy-strikes/STRIKES.tsv",
        "AGENTS/OSPREY/domain/energy-strikes/ANALYSIS_2026-09-08.md",
        "AGENTS/FALCON/domain/energy-strikes/ANALYSIS_2026-09-08.md",
        "AGENTS/FALCON/domain/vessel-incidents/VESSELS.tsv",
        *BRIEFS,
    ],
    OWN + "domain/war-risk/CROSS_THEATER_WAR_RISK.md": [
        "AGENTS/OSPREY/workbook/WARRISK.tsv",
        "AGENTS/FALCON/workbook/WARRISK.tsv",
        *BRIEFS,
    ],
}
RECEIPT = OWN + "registry/derived_inputs.json"


def digest(path):
    data = path.read_bytes()
    if not data.strip():
        raise ValueError(f"empty input: {path}")
    return hashlib.sha256(data).hexdigest()


def capture(root):
    return {p: digest(root / p) for p in sorted({p for v in DEPENDENCIES.values() for p in v})}


def inspect(root, receipt):
    if not isinstance(receipt, dict):
        raise ValueError("receipt must be an object")
    if receipt.get("version") != 1 or set(receipt.get("products", {})) != set(DEPENDENCIES):
        raise ValueError("receipt must cover both declared aggregates")
    changed = []
    for output, inputs in DEPENDENCIES.items():
        item = receipt["products"][output]
        if set(item["inputs"]) != set(inputs):
            raise ValueError(f"dependency scope differs: {output}")
        for path, expected in {output: item["sha256"], **item["inputs"]}.items():
            if (not isinstance(expected, str) or len(expected) != 64
                    or any(c not in "0123456789abcdef" for c in expected)):
                raise ValueError(f"invalid digest: {path}")
            if digest(root / path) != expected:
                changed.append((output, path))
    return changed


def record(root, reviewed):
    if reviewed != capture(root):
        raise ValueError("sources changed after capture; HAWK must capture and review the changed inputs")
    return {"version": 1, "recorded_at": datetime.now(timezone.utc).isoformat(),
            "products": {output: {"sha256": digest(root / output),
                                   "inputs": {p: reviewed[p] for p in inputs}}
                         for output, inputs in DEPENDENCIES.items()}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--capture", type=Path)
    group.add_argument("--record", type=Path)
    args = parser.parse_args()
    print("Scope: 2 HAWK aggregates; 11 owner dependency edges; own outputs IN.")
    print("NOTE: No external data-age, premium, event, grade, or semantic-consumption certification.")
    try:
        if args.capture:
            args.capture.write_text(json.dumps(capture(ROOT), indent=2) + "\n")
            print(f"CAPTURED: {args.capture}. HAWK must read these source bytes before recording.")
            return 0
        if args.record:
            receipt = record(ROOT, json.loads(args.record.read_text()))
            (ROOT / RECEIPT).write_text(json.dumps(receipt, indent=2) + "\n")
            print("RECORDED: aggregate and source fingerprints. Run the default check before commit.")
            return 0
        changed = inspect(ROOT, json.loads((ROOT / RECEIPT).read_text()))
        for output, path in changed:
            print(f"REVIEW: {output}; changed {path}. HAWK must read and reconcile, then record.")
        if changed:
            print(f"REVIEW: {len(changed)} changed dependency/output edges; baseline 0 after reconciliation.")
            return 1
        print("PASS: both outputs match the reviewed inputs; this does not establish current external facts.")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"CANNOT-CERTIFY: {exc}. HAWK must restore the source or repair the receipt and recheck.")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
