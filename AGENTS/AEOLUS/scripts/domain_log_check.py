#!/usr/bin/env python3
"""
domain_log_check.py — closeout guard for the AEOLUS domain-folder architecture.

THE FAILURE THIS CATCHES (observed 2026-08-13, L-28):
  water/ gained five bodies of work in one day. The ONE done by a spawned worker landed in
  water/workbook/LOG.tsv. The other four were done by AEOLUS directly, went straight to the
  central workbook/KB.tsv, and never touched the domain log at all. A reader opening
  water/workbook/LOG.tsv would have concluded the day was Rhine-and-Powell only.

  The cause is structural, not carelessness: AGENT.md disciplines WORKERS into writing the
  observation layer. When the orchestrator does the work itself, nothing disciplines it.

WHAT IT CHECKS, per domain folder:
  A. Folder was TOUCHED today (commits since midnight, or an uncommitted change) but its
     event log gained NO row dated today.  -> the L-28 shape exactly.
  B. Central KB.tsv gained rows today tagged with a channel this folder owns, but the
     folder's event log gained none. -> findings recorded centrally, domain layer silent.

Advisory. Exit 0 always — never block a closeout on it (fleet convention, per orphan_check.sh).
The output is designed to be impossible to skim past; that is the whole control.

Usage:  python3 AGENTS/AEOLUS/scripts/domain_log_check.py [--date YYYY-MM-DD]
"""
import argparse
import datetime
import os
import subprocess
import sys

AGENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                      text=True, cwd=AGENT_DIR).stdout.strip()

# domain folder -> (event-log filename, channels it owns in KB's Vectors column)
DOMAINS = {
    "regime":    ("LOG.tsv",    {"ENSO"}),
    "water":     ("LOG.tsv",    {"C6", "C5"}),
    "hurricane": ("LOG.tsv",    {"C1"}),
    "wildfire":  ("LOG.tsv",    {"C4"}),
    "seismic":   ("EVENTS.tsv", set()),   # event-triggered: quiet is CORRECT, never flag on A
}
# seismic is exempt from check A by design — an empty dossier there is the expected state.
EXEMPT_FROM_TOUCH_CHECK = {"seismic"}


def sh(*args):
    return subprocess.run(args, capture_output=True, text=True, cwd=REPO).stdout


def touched_today(folder, date):
    """Committed since midnight, or dirty in the working tree."""
    rel = f"AGENTS/AEOLUS/{folder}/"
    committed = sh("git", "log", f"--since={date} 00:00", "--format=%H", "--", rel).split()
    dirty = sh("git", "status", "--porcelain", "--", rel).strip()
    return bool(committed) or bool(dirty)


def log_rows_today(folder, logname, date):
    p = os.path.join(AGENT_DIR, folder, "workbook", logname)
    if not os.path.isfile(p):
        return None  # no log file at all
    n = 0
    with open(p, newline="", encoding="utf-8", errors="replace") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            if line.split("\t")[0].strip() == date:
                n += 1
    return n


def kb_rows_today(date, channels):
    """Central KB rows dated `date` whose Vectors column names a channel this domain owns."""
    p = os.path.join(AGENT_DIR, "workbook", "KB.tsv")
    if not os.path.isfile(p) or not channels:
        return []
    hits = []
    with open(p, newline="", encoding="utf-8", errors="replace") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            c = line.split("\t")
            if len(c) < 12 or c[1].strip() != date:
                continue
            vec = {v.strip() for v in c[11].split(",")}
            if vec & channels:
                hits.append(c[0].strip())
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    date = a.date

    print("\n" + "=" * 68)
    print("  DOMAIN LOG CHECK  ·  did each domain layer record what its domain did?")
    print("=" * 68)
    print(f"  date: {date}\n")

    flags = []
    for folder, (logname, channels) in sorted(DOMAINS.items()):
        if not os.path.isdir(os.path.join(AGENT_DIR, folder)):
            continue
        rows = log_rows_today(folder, logname, date)
        if rows is None:
            print(f"  ⚠️  {folder+'/':<12} no {logname} at all")
            continue
        touched = touched_today(folder, date)
        kb = kb_rows_today(date, channels)

        # A — folder moved, log silent
        if touched and rows == 0 and folder not in EXEMPT_FROM_TOUCH_CHECK:
            flags.append((folder, "A", f"folder changed today but {logname} gained 0 rows"))
        # B — findings landed centrally, domain layer silent
        if kb and rows == 0:
            flags.append((folder, "B", f"KB gained {len(kb)} row(s) for this domain "
                                       f"({', '.join(kb[:4])}{'…' if len(kb) > 4 else ''}) "
                                       f"but {logname} gained 0"))
        # B-partial — heuristic, deliberately loud only on a wide gap
        elif kb and rows and len(kb) >= 3 * rows:
            flags.append((folder, "B?", f"KB gained {len(kb)} row(s) vs {rows} log row(s) "
                                        f"— check nothing was recorded centrally only"))

        mark = "·" if touched else " "
        print(f"  {mark} {folder+'/':<12} log rows today: {rows:<3}  KB rows: {len(kb):<3}"
              f"  {'(touched)' if touched else ''}")

    print()
    if not flags:
        print("  ✓ clean — every touched domain recorded at least one event in its own log.")
    else:
        print(f"  🔴 {len(flags)} DOMAIN LOG GAP(S):\n")
        for folder, kind, msg in flags:
            print(f"     [{kind}] {folder}/ — {msg}")
        print("\n  This is the L-28 shape: work done by the ORCHESTRATOR bypasses the")
        print("  observation layer, because AGENT.md only disciplines spawned WORKERS.")
        print("  The contract binds whoever did the work, not whoever was spawned.")
        print("\n  Fix: append the day's events to the domain log, as a worker would have.")
    print("=" * 68 + "\n")
    return 0  # advisory — never blocks a closeout


if __name__ == "__main__":
    sys.exit(main())
