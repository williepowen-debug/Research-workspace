#!/usr/bin/env python3
"""
TERRY Boot — read-only situational card for trade construction sessions.

Prints: repo state, Terry file health, open setups, and optional market snapshot.
No writes, no trade recommendations, no execution.
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
TERRY_DIR = SCRIPTS_DIR.parent
WORKSPACE = SCRIPTS_DIR.parents[2]

REQUIRED = [
    "CLAUDE.md", "README.md", "STATUS.md", "RISK_RULES.md", "TRADE_CARD_TEMPLATE.md",
    "POSITION_INTAKE.md", "CHART_OPTIONS_WORKFLOW.md", "TRADE_BOOK.md", "SETUPS.tsv", "POSTMORTEMS.md",
    "scripts/boot.py", "scripts/snapshot.py", "scripts/risk_calc.py", "scripts/chain_parse.py",
]


def sh(cmd):
    try:
        return subprocess.check_output(cmd, cwd=WORKSPACE, text=True, stderr=subprocess.STDOUT).strip()
    except subprocess.CalledProcessError as e:
        return f"ERR: {e.output.strip()}"


def file_health():
    rows = []
    for name in REQUIRED:
        p = TERRY_DIR / name
        rows.append((name, p.exists(), p.stat().st_size if p.exists() else 0))
    return rows


def setups():
    p = TERRY_DIR / "SETUPS.tsv"
    if not p.exists():
        return [], ["SETUPS.tsv missing"]
    errors = []
    with p.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    terminal = {"CLOSED", "EXPIRED", "SUPERSEDED", "CREATED", "N/A"}
    openish = [r for r in rows if (r.get("status") or "").upper() not in terminal and (r.get("instrument") or "") != "TERRY"]
    # validate stable column count crudely
    lines = p.read_text().splitlines()
    cols = len(lines[0].split("\t")) if lines else 0
    bad = [i for i, line in enumerate(lines[1:], 2) if line and len(line.split("\t")) != cols]
    if bad:
        errors.append(f"SETUPS.tsv bad column count on lines: {bad[:8]}")
    return openish, errors


def latest_status_head(lines=18):
    p = TERRY_DIR / "STATUS.md"
    if not p.exists():
        return ["STATUS.md missing"]
    return p.read_text().splitlines()[:lines]


def run(args):
    print("TERRY boot card")
    print("===============")
    print("Repo:")
    print("  status:", sh(["git", "status", "--branch", "--short"]).replace("\n", " | "))
    print("  ahead/behind:", sh(["git", "rev-list", "--left-right", "--count", "HEAD...origin/master"]))

    print("\nFile health:")
    missing = False
    for name, ok, size in file_health():
        marker = "✓" if ok and size > 0 else "✗"
        if marker == "✗":
            missing = True
        print(f"  {marker} {name:<28} {size:>6} bytes")

    openish, errors = setups()
    print("\nSetups:")
    print(f"  actionable/open rows: {len(openish)}")
    for r in openish[:8]:
        print(f"  - {r.get('setup_id')} {r.get('instrument')} {r.get('structure')} | {r.get('verdict')} | {r.get('status')} | {r.get('notes')}")
    for e in errors:
        print(f"  ⚠ {e}")

    print("\nSTATUS head:")
    for line in latest_status_head():
        print("  " + line)

    print("\nReminder:")
    print("  Terry proposes only. Will approves/rejects. No execution.")
    print("  Use POSITION_INTAKE.md for existing positions and TRADE_CARD_TEMPLATE.md for proposals.")

    if args.snapshot:
        cmd = [sys.executable, str(SCRIPTS_DIR / "snapshot.py"), *args.snapshot]
        if args.benchmark:
            cmd += ["--benchmark", args.benchmark]
        if args.days:
            cmd += ["--days", str(args.days)]
        if args.stress:
            cmd += ["--stress"]
        print("\n--- snapshot ---")
        print(sh(cmd))

    return 1 if missing or errors else 0


def selftest():
    missing = [name for name, ok, size in file_health() if not ok or size <= 0]
    if missing:
        print(f"SELFTEST FAIL missing/empty: {missing}")
        return 1
    _, errors = setups()
    if errors:
        print(f"SELFTEST FAIL: {errors}")
        return 1
    print("boot.py SELFTEST: PASS")
    return 0


def main():
    ap = argparse.ArgumentParser(description="TERRY read-only boot card")
    ap.add_argument("--snapshot", nargs="*", help="Optional tickers to pass to snapshot.py, e.g. --snapshot WAL KRE")
    ap.add_argument("--benchmark", help="Benchmark for optional snapshot")
    ap.add_argument("--days", type=int, default=30, help="Lookback days for optional snapshot")
    ap.add_argument("--stress", action="store_true", help="Include stress backdrop in optional snapshot")
    ap.add_argument("--selftest", action="store_true", help="Validate Terry files and SETUPS.tsv")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
