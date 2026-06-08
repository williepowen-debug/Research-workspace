#!/usr/bin/env python3
"""
OTTO Predictions-Due Scanner
Automates boot step 4: scan workbook/PREDICTIONS.tsv and flag
  (a) OVERDUE — Status OPEN but Resolve_Date already passed (never leave OPEN-but-stale)
  (b) DUE SOON — Resolve_Date within the next N days (default 14)
  (c) the remaining OPEN ledger, sorted by resolve date.

This is the mechanical backstop for the "never leave a prediction OPEN-but-stale"
rule in CLAUDE.md — a passed Resolve_Date on an OPEN row is exactly how a
high-confidence call goes unresolved.

Usage:
  .venv/bin/python3 AGENTS/OTTO/scripts/predictions_due.py
  .venv/bin/python3 AGENTS/OTTO/scripts/predictions_due.py --soon 30
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

OTTO_DIR = Path(__file__).resolve().parent.parent
PRED_TSV = OTTO_DIR / "workbook" / "PREDICTIONS.tsv"

DEFAULT_SOON = 14  # days


def load_predictions():
    if not PRED_TSV.exists():
        return None
    rows = []
    with open(PRED_TSV) as f:
        header = f.readline().rstrip("\n").split("\t")
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            rows.append(dict(zip(header, parts + [""] * (len(header) - len(parts)))))
    return rows


def main():
    soon = DEFAULT_SOON
    if "--soon" in sys.argv:
        idx = sys.argv.index("--soon")
        if idx + 1 < len(sys.argv):
            soon = int(sys.argv[idx + 1])

    today = datetime.now().date()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"\n{'='*72}")
    print(f"  OTTO Predictions Due — {now}  (soon = next {soon} days)")
    print(f"{'='*72}")

    rows = load_predictions()
    if rows is None:
        print(f"\n  ERROR: {PRED_TSV} not found.")
        return 1

    open_rows = [r for r in rows if r.get("Status", "").strip().upper() == "OPEN"]

    overdue, due_soon, later = [], [], []
    for r in open_rows:
        rd = r.get("Resolve_Date", "").strip()
        try:
            d = datetime.strptime(rd, "%Y-%m-%d").date()
        except ValueError:
            later.append((None, r))  # unparseable date — surface anyway
            continue
        if d < today:
            overdue.append((d, r))
        elif d <= today + timedelta(days=soon):
            due_soon.append((d, r))
        else:
            later.append((d, r))

    def line(d, r, note):
        idp = r.get("ID", "?")
        conf = r.get("Confidence", "").strip()
        pred = r.get("Prediction", "")
        if len(pred) > 60:
            pred = pred[:57] + "..."
        dstr = d.strftime("%Y-%m-%d") if d else "(bad date)"
        print(f"  {idp:<8} {dstr}  {note:<10} {conf:>4}  {pred}")

    rc = 0
    if overdue:
        rc = 1
        overdue.sort(key=lambda x: x[0])
        print(f"\n  🔴 OVERDUE — OPEN past Resolve_Date (RESOLVE/RE-ARM/PUSH at closeout)")
        print(f"  {'-'*68}")
        for d, r in overdue:
            days_over = (today - d).days
            line(d, r, f"+{days_over}d over")

    if due_soon:
        due_soon.sort(key=lambda x: x[0])
        print(f"\n  🟠 DUE SOON (≤{soon} days)")
        print(f"  {'-'*68}")
        for d, r in due_soon:
            days_to = (d - today).days
            line(d, r, f"in {days_to}d")

    if later:
        later.sort(key=lambda x: (x[0] is None, x[0]))
        print(f"\n  📋 OPEN ledger (later)")
        print(f"  {'-'*68}")
        for d, r in later:
            line(d, r, "open")

    n_open = len(open_rows)
    print(f"\n  {n_open} OPEN | 🔴 {len(overdue)} overdue | 🟠 {len(due_soon)} due soon")
    if overdue:
        print(f"  ⚠️  {len(overdue)} prediction(s) OPEN-but-stale — must resolve/re-arm/push this session.")
    print()
    return rc


if __name__ == "__main__":
    sys.exit(main())
