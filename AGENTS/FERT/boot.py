#!/usr/bin/env python3
"""
boot.py — FERT boot instrument. Wall clock + ledger staleness + predictions-due
+ triggers-due, one verdict.

Built by DAEDALUS 2026-08-16 (re-charter build; pattern = WATT/VULCAN/MIDAS trio
incl. the 7/31 PAT-074 output-nonempty fix for the ledger_staleness alert
contract). cwd-proof + self-locating: lives at AGENTS/FERT/boot.py ->
parents[2] == repo root. Pure stdlib — no venv-only imports (PAT-103 n/a).

Legs:
  1. ledger staleness — workbook/*.tsv AND TRADE.md (shared script; flag is
     OUTPUT-NONEMPTY, never rc — the script exits 0 by documented contract).
  2. predictions-due  — workbook/PREDICTIONS.tsv rows past Resolve_By still OPEN.
  3. triggers-due     — workbook/TRIGGERS.tsv rows past Next_Check (the
     event-driven wake register; a due trigger is this session's work queue).

Combined exit: 0 = quiet · 1 = REVIEW (something due/stale) · 2 = a leg failed.
"""

import csv
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STALENESS = ROOT / "scripts" / "ledger_staleness.py"
PREDICTIONS = HERE / "workbook" / "PREDICTIONS.tsv"
TRIGGERS = HERE / "workbook" / "TRIGGERS.tsv"


def run_alert(cmd):
    """Runner for the shared ledger_staleness check. rc contract REVISED
    2026-08-17 (DAEDALUS shared-script fix, PROME-approved, CHECK_STANDARD §8
    rule 3): 0 clean · 1 stale FINDINGS · 2 CANNOT-CERTIFY (MISCONFIGURED /
    LEDGERS-OUTSIDE-GLOB / usage) — the old 'always 0' contract is retired;
    rc now AGREES with the ⚠️/🔴 markers. Verdict = rc 1 OR marker-present
    (§8 rule 5 keeps the marker channel authoritative; still never bare
    output-nonempty, which mis-reads the clean-run SCOPE statement
    ("trade perimeter: ...") as an alert — found 2026-08-16 building this file).
    rc 2 → leg failure (enforcement silently absent = never assume quiet).
    Returns 0 quiet · 1 REVIEW · 2 failure/cannot-certify."""
    try:
        p = subprocess.run([sys.executable, *cmd], cwd=str(ROOT),
                           capture_output=True, text=True)
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2
    out = (p.stdout or "").strip()
    err = (p.stderr or "").strip()
    if out:
        print(out)
    if err:
        print(err, file=sys.stderr)
    if p.returncode not in (0, 1):
        return 2
    return 1 if (p.returncode == 1 or "⚠️" in out or "🔴" in out) else 0


def _tsv_rows(path):
    """DictReader over a TSV, skipping leading '#' comment lines."""
    with path.open(encoding="utf-8") as f:
        lines = [ln for ln in f if not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t")), None


def dated_scan(path, date_col, label, status_col=None, live_statuses=None):
    """Generic due-scan: rows whose date_col <= today (optionally filtered to
    live statuses). Returns (rc, [lines]). rc 0 = none due · 1 = due · 2 = error.
    Null output states its scope (finding_verification_zero_is_ambiguous)."""
    if not path.exists():
        return 2, [f"  {label}: {path.name} MISSING — the register this leg certifies does not exist"]
    today = date.today()
    due = []
    try:
        rows, _ = _tsv_rows(path)
        for r in rows:
            if status_col and live_statuses is not None:
                if (r.get(status_col) or "").strip().upper().split(" ")[0] not in live_statuses:
                    continue
            raw = (r.get(date_col) or "").strip()
            try:
                when = datetime.strptime(raw[:10], "%Y-%m-%d").date()
            except ValueError:
                continue
            if when <= today:
                rid = (r.get("ID") or "?").strip()
                what = (r.get("Trigger") or r.get("Prediction") or "").strip()[:60]
                due.append(f"  DUE: {rid} [{raw}] {what}")
    except Exception as e:  # noqa: BLE001
        return 2, [f"  {label}: scan error {type(e).__name__}: {e}"]
    if not due:
        return 0, [f"  none due ({label}: {len(rows)} data row(s) scanned on {date_col})"]
    return 1, due


def main():
    print("=" * 72)
    print(f"  ⏰ WALL CLOCK: {datetime.now().strftime('%Y-%m-%d %H:%M %A')} — never hand-write a time; copy this line")
    print("  FERT BOOT — ledger staleness · predictions-due · triggers-due")
    print("=" * 72)
    rcs = []

    print("\n--- 1. ledger staleness (workbook + TRADE.md) ---")
    sw = run_alert([str(STALENESS), "FERT", "--quiet"])
    st = run_alert([str(STALENESS), "FERT", "--trade", "--quiet"])
    if sw == st == 0:
        print("  ✓ quiet (alert-contract: output only when stale/misconfigured)")
    rcs.append(2 if 2 in (sw, st) else (1 if 1 in (sw, st) else 0))

    print("\n--- 2. predictions-due (OPEN rows past Resolve_By) ---")
    rc, lines = dated_scan(PREDICTIONS, "Resolve_By", "predictions",
                           status_col="Status", live_statuses={"OPEN"})
    print("\n".join(lines))
    rcs.append(rc)

    print("\n--- 3. triggers-due (wake register past Next_Check) ---")
    rc, lines = dated_scan(TRIGGERS, "Next_Check", "triggers")
    print("\n".join(lines))
    rcs.append(rc)

    print("\n" + "=" * 72)
    if 2 in rcs:
        print("  FERT boot: a leg FAILED — check manually, do NOT assume quiet.")
        return 2
    if 1 in rcs:
        print("  FERT boot: REVIEW — work the flagged items before new research.")
        return 1
    print("  FERT boot: all quiet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
