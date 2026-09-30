"""Fixture tests for the VX_HISTORY validator behind the n=12 counter (threshold_scan.validate_history) and
creed_selfcheck's history block, which calls the same function.

Built 2026-09-30 to finish CATO's CW5 residual. Cases C1-C13 are CATO's saved counterexamples, transcribed
from AGENTS/CATO/runs/2026-09-29_2310_creed-workbook-probe.py (whose results file shows the pre-fix failures).
Cases O1-O9 are CREED's ordinary boundary cases. Each case runs BOTH real scripts end to end, in an isolated
temp copy of the working tree, and checks the COUNTER LINE and the SELFCHECK HISTORY LINES, never the exit code
alone: the scan exits 1 on the live near-band row whatever the history says.

Run: python3 AGENTS/CREED/scripts/test_history_validation.py   (exit 0 = all pass; read-only on the repo)
"""
import csv
import io
import pathlib
import shutil
import subprocess
import sys
import tempfile

CREED = pathlib.Path(__file__).resolve().parents[1]
REPO = CREED.parents[1]
HEADER = ["Vector_ID", "Date", "Value", "Status", "Notes", "Role", "Basis"]
V = "VX-CREED-1.01"          # counted by CREED-T-01a
V2 = "VX-CREED-2.01"         # counted by CREED-T-01b
BASIS = "Trepp headline"


def rows(vid=V, months=range(1, 12), year=2025, basis=BASIS, role="CANONICAL", value="11.5"):
    return [[vid, f"{year}-{m:02}", value, "ORANGE", "fixture", role, basis] for m in months]


def encode(data, fields=HEADER):
    out = io.StringIO()
    w = csv.writer(out, delimiter="\t", lineterminator="\n")
    w.writerow(fields)
    w.writerows(data)
    return out.getvalue().encode()


def row(vid=V, per="2025-12", value="11.5", role="CANONICAL", basis=BASIS):
    return [vid, per, value, "ORANGE", "fixture", role, basis]


BASE = rows()
# expect: substring the counter line for `vid` must contain; sc = True if selfcheck must emit a [history] finding
CASES = [
    # ---- CATO's saved counterexamples (C1-C13) ----
    ("C1 live snapshot", None, "VX-CREED-1.01: n=8/12", False, V),
    ("C2 11 months", encode(BASE), "n=11/12", False, V),
    ("C3 11 + excluded duplicate", encode(BASE + [row(per="2025-01", role="DUPLICATE")]), "n=11/12", False, V),
    ("C4 12 months", encode(BASE + [row()]), "DUE", False, V),
    ("C5 11 + context provider", encode(BASE + [row(role="CONTEXT")]), "n=11/12", False, V),
    ("C6 missing Role with data", encode([r[:5] for r in BASE], HEADER[:5]), "FAIL-LOUD", True, None),
    ("C7 empty history", b"", "FAIL-LOUD", True, None),
    ("C8 header only without Role", encode([], HEADER[:5]), "FAIL-LOUD", True, None),
    ("C9 11 + same-month dated row", encode(BASE + [row(per="2025-11-30")]), "INVALID", True, V),
    ("C10 11 + different basis", encode(BASE + [row(basis="different denominator/provider")]), "INVALID", True, V),
    ("C11 11 + impossible month", encode(BASE + [row(per="2025-13")]), "INVALID", True, V),
    ("C12 11 + blank basis", encode(BASE + [row(basis="")]), "INVALID", True, V),
    ("C13 conflicting canonical duplicate", encode(BASE + [row(per="2025-01", value="99")]), "INVALID", True, V),
    # ---- CREED's ordinary boundary cases (O1-O9) ----
    ("O1 header with Role but no data rows", encode([]), "FAIL-LOUD", True, None),
    ("O2 header lacks Basis column", encode([r[:6] for r in BASE], HEADER[:6]), "FAIL-LOUD", True, None),
    ("O3 12 quarters, one cadence", encode([row(per=f"{y}-Q{q}") for y in (2023, 2024, 2025) for q in (1, 2, 3, 4)]),
     "DUE", False, V),
    ("O4 12 real days, one cadence", encode([row(per=f"2025-09-{d:02}") for d in range(1, 13)]), "DUE", False, V),
    ("O5 impossible day 2025-02-30", encode(BASE + [row(per="2025-02-30")]), "INVALID", True, V),
    ("O6 non-numeric CANONICAL value", encode(BASE + [row(value="n/a")]), "INVALID", True, V),
    ("O7 mistyped Role token", encode(BASE + [row(role="CANONCAL")]), "INVALID", True, V),
    ("O8 bad series does not suppress a good one",
     encode(BASE + [row(per="2025-13")] + rows(vid=V2, months=range(1, 13))), "INVALID", True, V),
    ("O8b ...the good series still counts",
     encode(BASE + [row(per="2025-13")] + rows(vid=V2, months=range(1, 13))), "🟠 DUE      CREED-T-01b  VX-CREED-2.01: n=12", True, V2),
    ("O9 identical duplicate is still a conflict", encode(BASE + [row(per="2025-01")]), "INVALID", True, V),
]


def main():
    fails = 0
    with tempfile.TemporaryDirectory(prefix="creed-hist-test-") as tmp:
        home = pathlib.Path(tmp) / "AGENTS/CREED"
        shutil.copytree(CREED, home, ignore=shutil.ignore_patterns("__pycache__"))
        hist = home / "workbook/VX_HISTORY.tsv"
        live = hist.read_bytes()
        for name, data, expect, sc_expected, vid in CASES:
            hist.write_bytes(live if data is None else data)
            env = {"PATH": "/usr/bin:/bin", "PYTHONDONTWRITEBYTECODE": "1"}
            scan = subprocess.run([sys.executable, str(home / "scripts/threshold_scan.py")],
                                  capture_output=True, text=True, env=env)
            chk = subprocess.run([sys.executable, str(home / "scripts/creed_selfcheck.py")],
                                 capture_output=True, text=True, env=env)
            out = scan.stdout
            if vid:
                lines = [l for l in out.splitlines() if vid in l and ("n=" in l or "INVALID" in l)]
            else:
                lines = [l for l in out.splitlines() if "FAIL-LOUD" in l]
            hist_findings = [l.strip() for l in chk.stdout.splitlines() if "[history]" in l]
            # "DUE" also appears inside the INVALID line's own text ("neither n nor DUE"), so the forbidden
            # verdict is the 🟠 DUE MARKER, never the bare word (the harness's own first run hit exactly this).
            ok_scan = any(expect in l for l in lines) and not ("DUE" not in expect and any("🟠 DUE" in l for l in lines))
            ok_sc = bool(hist_findings) == sc_expected
            ok_rc = chk.returncode == (1 if sc_expected else 0) and scan.returncode in (0, 1)
            ok = ok_scan and ok_sc and ok_rc and "Traceback" not in scan.stderr + chk.stderr
            fails += not ok
            print(f"{'PASS' if ok else 'FAIL'}  {name:45} counter={lines[0].strip()[:70] if lines else '-'!r}"
                  f"  selfcheck_history={len(hist_findings)} rc={chk.returncode}")
            if not ok:
                print("      scan stderr:", scan.stderr[-300:], "\n      selfcheck:", hist_findings[:3], chk.stderr[-300:])
    print(f"\n{len(CASES) - fails}/{len(CASES)} passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
