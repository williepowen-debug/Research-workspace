#!/usr/bin/env python3
"""sweeps_due.py — DAEDALUS recurring-maintenance cadence check.

Reads sweeps/REGISTRY.tsv and prints any ACTIVE sweep whose cadence has elapsed
(today - last_run >= cadence_days). Wired into the DAEDALUS SPAWN PROTOCOL so a
recurring sweep can't silently lapse. Detection only — it never runs a sweep or
touches a file. Exit code is always 0 (an alert, not a gate).

Usage (cwd-proof, self-locating via __file__ — run from anywhere):
    python3 "$(git rev-parse --show-toplevel)/AGENTS/DAEDALUS/scripts/sweeps_due.py"
"""
import csv
import datetime
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTRY = os.path.normpath(os.path.join(HERE, "..", "sweeps", "REGISTRY.tsv"))


def main():
    today = datetime.date.today()
    due, tracked = [], 0
    try:
        with open(REGISTRY, encoding="utf-8") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                task = (row.get("task") or "").strip()
                if not task or task.startswith("#"):
                    continue
                if (row.get("status") or "active").strip().lower() != "active":
                    continue
                try:
                    last = datetime.date.fromisoformat((row.get("last_run") or "").strip())
                    cad = int((row.get("cadence_days") or "").strip())
                except (ValueError, TypeError):
                    print(f"⚠️  sweeps_due: un-parseable row for '{task}' (check last_run/cadence_days)", file=sys.stderr)
                    continue
                tracked += 1
                age = (today - last).days
                if age >= cad:
                    due.append((task, age, cad, (row.get("playbook") or "").strip()))
    except OSError:
        print("sweeps_due: no sweeps/REGISTRY.tsv found", file=sys.stderr)
        return 0

    if not due:
        print(f"✅ sweeps: none due ({tracked} tracked)")
    else:
        for task, age, cad, pb in sorted(due, key=lambda r: r[1] - r[2], reverse=True):
            print(f"⏰ DUE: {task} — last run {age}d ago (cadence {cad}d, +{age - cad}d over) → {pb}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
