#!/usr/bin/env python3
"""Collect existing WALTER closeout checks and draft a dated receipt.

No source edits, fetch, staging, commit, push, scheduling or completion judgment.
Run after the applicable owner updates. Manual outcomes remain in LAST_COMPLETION;
this evidence bundle is not an obligation registry. rc 0/1/2 grades selected checks
only (PASS/REVIEW/UNKNOWN), never the entire procedure.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
DESK = Path("AGENTS/WALTER")
COMMON_DUTIES = {
    "11": "Account for authored signals, handoffs and batches; preserve delivery/consumption limits.",
    "Tier1": "Refresh affected/stale live state or record unavailable evidence; preserve dated observations.",
    "15": "Review carried duties and owner evidence; retain unresolved work in LAST_COMPLETION.",
    "root.retirement": "Assess research/source retirement under root Data Hygiene; record scope and disposition.",
    "16": "Exact-path commit and authorized publication or explicit deferral; reconcile after publication.",
}
FULL_DUTIES = {
    "13": "Refresh REGISTRY before regenerating NETWORK AWARENESS.",
    "12(a,b)": "Refresh STATUS facts and derived network summary from canonical sources.",
    "12(c)": "Review FILTER POSTURE and standing flags; change only when warranted.",
    "12(d,e)": "Write session entry and current BOTTOM LINE; account for earlier full-deferred breadcrumbs.",
    "14": "Refresh/prune MEMORY and assess promotion without losing unresolved duties.",
}


def plan(root, tier, *, spec_changed=False, status_changed=False,
         memory_slugs=(), superseded=()):
    py = sys.executable
    def python(name, path, *args):
        return (name, [py, path, *args], "standard")
    checks = [
        python("receipt", str(DESK / "tools/closeout_check.py")),
        python("read-cap", "scripts/read_cap_check.py", "--agent", "WALTER"),
        python("archives", str(DESK / "tools/archive_pair_check.py")),
        ("orphans", ["bash", "scripts/orphan_check.sh", "WALTER"], "advisory"),
    ]
    weekdays = ["PROME/DOCKET.tsv", "PROME/GATES.tsv", "PROME/WILL_QUEUE.md",
                str(DESK / "STATUS.md")]
    weekdays += [str(DESK / p) for p in ("workbook/CATALYSTS.tsv", "CALENDAR.md")
                 if (root / DESK / p).exists()]
    checks.append(python("weekdays", "scripts/claim_check.py", "--check", "weekday", *weekdays))
    if status_changed or tier == "full":
        checks.append(python("ledger-nudge", "scripts/ledger_staleness.py", "--nudge", "WALTER"))
    if tier == "full":
        checks += [python("basis", str(DESK / "tools/boot_basis_check.py")),
                   python("reads", "PROME/tools/reads_check.py", "--agent", "WALTER"),
                   ("doctor", [py, str(DESK / "tools/walter_doctor.py")], "doctor")]
    if tier == "full" or spec_changed:
        checks.append(python("versions", str(DESK / "tools/version_drift_check.py")))
    if memory_slugs:
        args = [arg for slug in memory_slugs for arg in ("--slug", slug)]
        checks += [python("memory-index", "scripts/memory_index_check.py", "--strict", *args),
                   ("memory-length", ["bash", "scripts/check_memory_length.sh"], "standard")]
    for i, (old, new) in enumerate(superseded, 1):
        for scope in ("peer", "self"):
            flags = ["--self"] if scope == "self" else []
            checks.append(python(f"consumer-{i}-{scope}", "scripts/consumer_check.py",
                                 "--agent", "WALTER", *flags, "--old", old, "--new", new))
    return checks


def execute(argv, root):
    return subprocess.run(argv, cwd=root, capture_output=True, text=True, timeout=60)


def classify(code, kind, output):
    if "Traceback (most recent call last):" in output:
        return "UNKNOWN"
    if kind == "doctor":
        if "check raised " in output or code < 0:
            return "UNKNOWN"
        return "REVIEW" if code else "PASS"
    if kind == "advisory":
        return "ADVISORY" if code == 0 else "UNKNOWN"
    return "PASS" if code == 0 else "REVIEW" if code == 1 else "UNKNOWN"


def run(root, tier, output_dir, *, executor=execute, **options):
    root, output_dir = root.resolve(), output_dir.resolve()
    allowed = (root / DESK / "research").resolve()
    if not output_dir.is_relative_to(allowed):
        raise ValueError("output must be inside AGENTS/WALTER/research/")
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for name, argv, kind in plan(root, tier, **options):
        if name == "weekdays" and any(not (root / p).is_file() for p in argv[4:]):
            code, text = 2, "Required weekday input missing; cannot certify.\n"
        else:
            try:
                completed = executor(argv, root)
                code, text = completed.returncode, completed.stdout + completed.stderr
            except (OSError, subprocess.TimeoutExpired) as exc:
                code, text = 2, f"Check did not finish: {type(exc).__name__}: {exc}\n"
        artifact = output_dir / (name + ".txt")
        artifact.write_text(text)
        rows.append({"check": name, "state": classify(code, kind, text), "rc": code,
                     "command": argv, "output": str(artifact.relative_to(root))})
    if tier == "full":
        try:
            count = len((root / DESK / "MEMORY.md").read_text().splitlines())
            row = {"check": "local-memory-lines", "state": "PASS" if count <= 100 else "REVIEW",
                   "lines": count, "limit": 100}
        except OSError as exc:
            row = {"check": "local-memory-lines", "state": "UNKNOWN", "reason": str(exc)}
        rows.append(row)
    duties = dict(COMMON_DUTIES)
    duties["Tier1.breadcrumb"] = "Record the light-closeout breadcrumb; full narrative regeneration is deferred."
    if tier == "full":
        duties.pop("Tier1.breadcrumb")
        duties.update(FULL_DUTIES)
    state = ("UNKNOWN" if any(r["state"] == "UNKNOWN" for r in rows) else
             "REVIEW" if any(r["state"] == "REVIEW" for r in rows) else "PASS")
    report = {"as_of": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "tier": tier, "selected_check_state": state,
              "procedure_completion": "UNVERIFIED — owner must account for manual duties",
              "checks": rows, "manual_duties": [{"step": k, "state": "UNVERIFIED", "duty": v}
                                                for k, v in duties.items()],
              "conditional_selection": options,
              "limits": "No fetch or source writes. Local origin can be stale. Advisory findings and manual judgments require review. Conditional flags must match actual work; unselected checks are not passes."}
    # Reuse the existing receipt check's facts; do not reconstruct a second ledger.
    try:
        current = json.loads((output_dir / "receipt.txt").read_text())
        report["receipt_observation"] = {k: current[k] for k in
            ("as_of", "origin_ref", "delivery_scope", "delivered", "total", "limits") if k in current}
        report["receipt_observation"]["note"] = "Existing receipt observation; this runner did not fetch. Not consumption or fresh publication proof."
    except (ValueError, OSError):
        pass
    (output_dir / "checks.json").write_text(json.dumps(report, indent=2) + "\n")
    draft = [f"# WALTER {tier} closeout check draft — {report['as_of']}", "",
             f"Selected checks: {state}. Procedure completion: UNVERIFIED.", "",
             "Record owner outcomes/evidence or unresolved dispositions in the existing LAST_COMPLETION receipt.", "",
             "| Check | Result |", "|---|---|"]
    draft += [f"| {r['check']} | {r['state']} |" for r in rows]
    draft += ["", "Manual duties — none is certified by command success:", ""]
    draft += [f"- {k}: UNVERIFIED — {v}" for k, v in duties.items()]
    draft += ["", report["limits"], ""]
    (output_dir / "draft.md").write_text("\n".join(draft))
    return report, {"PASS": 0, "REVIEW": 1, "UNKNOWN": 2}[state]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tier", choices=("light", "full"), required=True)
    ap.add_argument("--output", type=Path, required=True, help="dated directory under WALTER/research")
    ap.add_argument("--status-changed", action="store_true")
    ap.add_argument("--spec-changed", action="store_true")
    ap.add_argument("--auto-memory", action="append", default=[])
    ap.add_argument("--superseded", nargs=2, action="append", default=[], metavar=("OLD", "NEW"))
    a = ap.parse_args()
    try:
        output = a.output if a.output.is_absolute() else ROOT / a.output
        report, rc = run(ROOT, a.tier, output, status_changed=a.status_changed,
                         spec_changed=a.spec_changed, memory_slugs=a.auto_memory,
                         superseded=a.superseded)
    except (ValueError, OSError) as exc:
        print("UNKNOWN: " + str(exc)); return 2
    print(f"Selected checks: {report['selected_check_state']}; procedure completion: UNVERIFIED.")
    print(f"Evidence and owner-review draft: {a.output}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
