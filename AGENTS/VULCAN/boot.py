#!/usr/bin/env python3
"""
boot.py — VULCAN boot instrument. Ledger staleness + predictions-due, one verdict.

Built by DAEDALUS 2026-07-10 (VULCAN build). cwd-proof + self-locating: lives at
AGENTS/VULCAN/boot.py -> parents[2] == repo root; finds scripts/ledger_staleness.py
regardless of launch cwd. (No bespoke fetch instrument yet — a semi/memory scraper
is a later increment; VULCAN's channels are earnings/policy-cadence, not per-boot.)

Boot step 4 in CLAUDE.md. Two legs:
  1. ledger staleness — workbook/*.tsv AND TRADE.md vs STATUS mtime (shared script).
  2. predictions-due  — workbook/PREDICTIONS.tsv rows past resolve_date still OPEN.

Combined exit: 0 = quiet · 1 = REVIEW (stale ledger or prediction due) · 2 = a leg failed.
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


def run(cmd):
    try:
        return subprocess.run([sys.executable, *cmd], cwd=str(ROOT)).returncode
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2


def run_alert(cmd):
    """Run an ALERT-CONTRACT script (ledger_staleness: prints only when something
    needs attention, exit code ALWAYS 0 by documented contract). Relay its output;
    the flag is OUTPUT-NONEMPTY, never rc — the old leg branched on rc 1, which
    the script never emits, so staleness could never trip the REVIEW exit (dead
    code since build 7/10; DAEDALUS fix 2026-07-31, Will-approved, PAT-074).
    Returns 0 quiet · 1 printed-something (REVIEW) · 2 launch/usage failure."""
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
    if p.returncode != 0:
        return 2
    return 1 if out else 0


def predictions_due():
    """(n_due, rows) for PREDICTIONS.tsv rows past resolve_date still OPEN/ACTIVE.
    Tolerant of a newborn/empty ledger."""
    if not PREDICTIONS.exists():
        return 0, []
    today = date.today()
    due = []
    try:
        with PREDICTIONS.open(encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter="\t")
            cols = {c.lower(): c for c in (reader.fieldnames or [])}
            dcol = cols.get("resolve_date") or cols.get("resolves") or cols.get("resolve")
            scol = cols.get("status")
            if not dcol or not scol:
                return 0, []
            for r in reader:
                if (r.get(scol) or "").strip().upper() not in ("OPEN", "ACTIVE", "PENDING"):
                    continue
                raw = (r.get(dcol) or "").strip()
                try:
                    when = datetime.strptime(raw[:10], "%Y-%m-%d").date()
                except ValueError:
                    continue
                if when <= today:
                    due.append(f"{r.get(cols.get('id', 'id'), '?')} due {raw}")
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: predictions scan error: {e}", file=sys.stderr)
        return 2, []
    return len(due), due


def main():
    print("=" * 72)
    print("  VULCAN BOOT — ledger staleness · predictions-due")
    print("=" * 72)
    rcs = []

    print("\n--- 1. ledger staleness (workbook + TRADE.md vs STATUS) ---")
    sw = run_alert([str(STALENESS), "VULCAN", "--quiet"])
    st = run_alert([str(STALENESS), "VULCAN", "--trade", "--quiet"])
    if sw == st == 0:
        print("  ✓ quiet (alert-contract: output only when stale/misconfigured)")
    rcs.append(2 if 2 in (sw, st) else (1 if 1 in (sw, st) else 0))

    print("\n--- 2. predictions-due scan ---")
    n_due, due = predictions_due()
    if due:
        for d in due:
            print(f"  DUE: {d}")
        rcs.append(1)
    elif n_due == 0:
        print("  none due (or newborn ledger)")
        rcs.append(0)
    else:
        rcs.append(2)

    print("\n" + "=" * 72)
    if 2 in rcs:
        print("  VULCAN boot: a leg FAILED — check manually, do NOT assume quiet.")
        return 2
    if 1 in rcs:
        print("  VULCAN boot: REVIEW — stale ledger or prediction due.")
        return 1
    print("  VULCAN boot: all quiet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
