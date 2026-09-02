#!/usr/bin/env python3
"""
RED schema conformance check — does SCHEMA.tsv still describe the files it claims to?

    (cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/RED/scripts/schema_check.py)

Read-only. exit 0 = all conform, exit 1 = a declared contract has drifted from its file.

WHY THIS EXISTS (audit R8, 2026-08-12 / S30): SCHEMA.tsv is a CO-SIGNED contract — WALTER
reads the registry against it — and it had silently drifted for three months. It documented
8 registry columns while the file carried 12, and CATALYSTS.tsv (65 rows) and WATCHLINES.tsv
had no coverage at all. Nothing detected it because nothing was looking. A contract that
nobody checks is documentation, not a contract.

WHAT IT CHECKS (structure only, deliberately):
  * every file SCHEMA declares exists and is readable
  * declared column names == actual header, SAME ORDER
  * no undeclared file in the workbook/docket set

WHAT IT DOES NOT CHECK, and why: value-domain conformance. The allowed_values cells are
honest prose about a vocabulary that is legitimately richer than any enum (ML.tsv
Thesis_Impact carries 104 distinct values on 167 rows and that IS the content). Grading
values mechanically would either force a flattening that destroys information or produce
noise nobody reads. Structure is mechanically decidable; vocabulary is a judgment call.
Saying so beats shipping a check that certifies its own scope.

⚠️ Do NOT parse these TSVs with the csv module. Several carry literal '"' characters in
prose cells (ML.tsv had 36 on 2026-08-12), and csv.reader consumes them as field quoting —
a read/modify/write round-trip then persists the mangled parse. One such round-trip silently
rewrote a PREDICTIONS.tsv cell from '"' to 'W' the same session. Split on '\t'. (ML-RED-168)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # AGENTS/RED
WB = ROOT / "workbook"

# file -> header line index (FLOW.tsv line 0 is its FROZEN banner, not the header)
FILES = {
    "KB.tsv": (WB / "KB.tsv", 0),
    # VX.tsv line 0 is its two-clock LIVE banner (added S30/T7) — same shape as FLOW.tsv's
    # freeze banner. The banner is what makes ledger_staleness.py read a CONTENT vintage
    # instead of git time, which is the whole point; the cost is this skip.
    "VX.tsv": (WB / "VX.tsv", 1),
    "ML.tsv": (WB / "ML.tsv", 0),
    "CHALLENGES.tsv": (WB / "CHALLENGES.tsv", 0),
    "PREDICTIONS.tsv": (WB / "PREDICTIONS.tsv", 0),
    "FLOW.tsv": (WB / "FLOW.tsv", 1),
    "VX_HISTORY.tsv": (WB / "VX_HISTORY.tsv", 0),
    "FALSIFICATION_TRIGGERS.tsv": (ROOT / "registry" / "FALSIFICATION_TRIGGERS.tsv", 0),
    # Generated SCAN view (S39 2026-09-02, WALTER proposal): line 0 is the generator banner
    # carrying the canon sha256 — skip it. Content drift vs canon is gen_trigger_scan.py --check's job.
    "FALSIFICATION_TRIGGERS_SCAN.tsv": (ROOT / "registry" / "FALSIFICATION_TRIGGERS_SCAN.tsv", 1),
    # Outcome axis pair (added 2026-08-27 S36d, CHG-051 deliverable 2): the pre-committed
    # per-trigger spec and the per-fire grade ledger. Registry-adjacent, so they live in
    # registry/ beside the surface they grade.
    "OUTCOME_SPEC.tsv": (ROOT / "registry" / "OUTCOME_SPEC.tsv", 0),
    "TRIGGER_OUTCOMES.tsv": (ROOT / "registry" / "TRIGGER_OUTCOMES.tsv", 0),
    "../docket/CATALYSTS.tsv": (ROOT / "docket" / "CATALYSTS.tsv", 0),
    "../docket/WATCHLINES.tsv": (ROOT / "docket" / "WATCHLINES.tsv", 0),
}


def rows(path):
    return [l.split("\t") for l in path.read_text(encoding="utf-8").rstrip("\n").split("\n")]


def main():
    schema = WB / "SCHEMA.tsv"
    if not schema.exists():
        print("FAIL: SCHEMA.tsv missing")
        return 1

    declared = {}
    for r in rows(schema)[1:]:
        if len(r) >= 2:
            declared.setdefault(r[0], []).append(r[1])

    bad = 0
    print(f"{'file':<34}{'schema':>7}{'file':>6}   verdict")
    for name, (path, skip) in FILES.items():
        if not path.exists():
            print(f"{name:<34}{'-':>7}{'-':>6}   FAIL: file not found ({path})")
            bad += 1
            continue
        actual = rows(path)[skip]
        dec = declared.get(name, [])
        if not dec:
            print(f"{name:<34}{0:>7}{len(actual):>6}   FAIL: no SCHEMA coverage")
            bad += 1
        elif dec != actual:
            miss = [c for c in actual if c not in dec]
            extra = [c for c in dec if c not in actual]
            order = miss == [] and extra == []
            why = "column ORDER differs" if order else f"missing_from_schema={miss} not_in_file={extra}"
            print(f"{name:<34}{len(dec):>7}{len(actual):>6}   FAIL: {why}")
            bad += 1
        else:
            print(f"{name:<34}{len(dec):>7}{len(actual):>6}   ok")

    undeclared = set(declared) - set(FILES)
    for u in sorted(undeclared):
        print(f"{u:<34}{'-':>7}{'-':>6}   WARN: declared in SCHEMA but not in this check's file map")

    print("\n✅ ALL CONFORM" if not bad else f"\n❌ {bad} file(s) drifted from SCHEMA.tsv")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
