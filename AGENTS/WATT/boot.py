#!/usr/bin/env python3
"""
boot.py — WATT boot instrument. Runs three checks, one combined verdict.

Built by DAEDALUS 2026-07-10 (WATT spinout, Step-2). cwd-proof + self-locating:
lives at AGENTS/WATT/boot.py -> parents[2] == repo root; finds power_watch.py
(sibling) and scripts/ledger_staleness.py (root) regardless of launch cwd.

Boot step 4 in CLAUDE.md. Three legs:
  1. power_watch.py   — PJM emergency postings + EIA-930 demand + retail backdrop
                        (P1 stress->price live read). Its own rc: 0 quiet / 1
                        emergency-class posting / 2 fetch-fail.
  2. ledger staleness — workbook/*.tsv AND the TRADE.md surface vs STATUS mtime
                        (shared scripts/ledger_staleness.py, --quiet).
  3. predictions-due  — workbook/PREDICTIONS.tsv rows past their resolve date
                        still marked OPEN/ACTIVE.

Combined exit: 0 = all quiet · 1 = something needs REVIEW (emergency posting,
stale ledger, or a prediction due) · 2 = a leg failed to run (never assume quiet).
"""

import csv
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
POWER_WATCH = HERE / "power_watch.py"
STALENESS = ROOT / "scripts" / "ledger_staleness.py"
PREDICTIONS = HERE / "workbook" / "PREDICTIONS.tsv"


def run(cmd):
    """Run a subprocess, stream its output, return its rc (or 2 on launch failure)."""
    try:
        r = subprocess.run([sys.executable, *cmd], cwd=str(ROOT))
        return r.returncode
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2


def predictions_due():
    """Return (n_due, rows) for PREDICTIONS.tsv rows past resolve-date still OPEN.
    Tolerant of an empty/newborn ledger. Expects a 'resolve_date' (or 'resolves')
    ISO-date col and a 'status' col; skips rows it can't parse rather than crashing."""
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
                return 0, []  # schema not ready yet — newborn ledger
            for row in reader:
                status = (row.get(scol) or "").strip().upper()
                if status not in ("OPEN", "ACTIVE", "PENDING"):
                    continue
                raw = (row.get(dcol) or "").strip()
                try:
                    when = datetime.strptime(raw[:10], "%Y-%m-%d").date()
                except ValueError:
                    continue
                if when <= today:
                    pid = row.get(cols.get("id", "id"), "?")
                    due.append(f"{pid} due {raw} (status {status})")
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: predictions scan error: {e}", file=sys.stderr)
        return 2, []
    return len(due), due


def main():
    print("=" * 72)
    print("  WATT BOOT — power_watch · ledger staleness · predictions-due")
    print("=" * 72)
    rcs = []

    print("\n--- 1. power_watch (P1 stress->price live read) ---")
    rcs.append(("power_watch", run([str(POWER_WATCH)])))

    print("\n--- 2. ledger staleness (workbook + TRADE.md vs STATUS) ---")
    sw = run([str(STALENESS), "WATT", "--quiet"])
    st = run([str(STALENESS), "WATT", "--trade", "--quiet"])
    rcs.append(("staleness", 1 if (sw == 1 or st == 1) else max(sw, st) if 2 in (sw, st) else 0))

    print("\n--- 3. predictions-due scan ---")
    n_due, due = predictions_due()
    if n_due == 0:
        print("  none due (or newborn ledger)")
        rcs.append(("predictions", 0))
    elif due:
        for d in due:
            print(f"  DUE: {d}")
        rcs.append(("predictions", 1))
    else:  # scan error returned (n_due==2 sentinel path)
        rcs.append(("predictions", 2))

    # --- combined verdict ---
    fail = [n for n, c in rcs if c == 2]
    review = [n for n, c in rcs if c == 1]
    print("\n" + "=" * 72)
    if fail:
        print(f"  WATT boot: {', '.join(fail)} FAILED — check manually, do NOT assume quiet.")
        return 2
    if review:
        print(f"  WATT boot: REVIEW — {', '.join(review)}")
        return 1
    print("  WATT boot: all quiet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
