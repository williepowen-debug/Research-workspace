#!/usr/bin/env python3
"""
MARCO Staleness Check
Lightweight hygiene scan: flags state files whose self-reported "last updated"
date has drifted, so the boot brief can nudge a refresh before the dashboard
quietly goes stale.

Checks:
  STATUS.md       — the "**Last Updated:** YYYY-MM-DD" header (warn if > --status-days, default 7)
  workbook/VX.tsv — per-row "Last Updated" column (list rows older than --vx-days, default 60)

Usage:
  .venv/bin/python3 AGENTS/MARCO/scripts/staleness.py
  .venv/bin/python3 AGENTS/MARCO/scripts/staleness.py --status-days 5 --vx-days 45
"""

import re
import sys
from datetime import datetime, date
from pathlib import Path

MARCO_DIR = Path(__file__).resolve().parent.parent
STATUS_MD = MARCO_DIR / "STATUS.md"
VX_TSV = MARCO_DIR / "workbook" / "VX.tsv"

DEFAULT_STATUS_DAYS = 7
DEFAULT_VX_DAYS = 60

DATE_RE = re.compile(r"(20\d{2})-(\d{2})-(\d{2})")


def _arg(flag, default):
    if flag in sys.argv:
        i = sys.argv.index(flag)
        if i + 1 < len(sys.argv):
            return int(sys.argv[i + 1])
    return default


def parse_iso(s):
    m = DATE_RE.search(s or "")
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def check_status(today, max_days):
    if not STATUS_MD.exists():
        return f"  ❌ STATUS.md not found"
    head = "".join(STATUS_MD.open().readlines()[:5])
    m = re.search(r"Last Updated[:*\s]*"+DATE_RE.pattern, head)
    d = parse_iso(m.group(0)) if m else None
    if d is None:
        return "  ⚠️  STATUS.md — could not find a 'Last Updated' date in the header"
    age = (today - d).days
    icon = "🟠" if age > max_days else "✓"
    flag = f"  {icon} STATUS.md last updated {d} ({age}d ago)"
    if age > max_days:
        flag += f"  — exceeds {max_days}d, consider refresh"
    return flag


def check_vx(today, max_days):
    if not VX_TSV.exists():
        return ["  ❌ workbook/VX.tsv not found"]
    with open(VX_TSV) as f:
        header = f.readline().rstrip("\n").split("\t")
    try:
        lu_idx = header.index("Last Updated")
    except ValueError:
        lu_idx = -1  # last column fallback
    stale = []
    total = 0
    with open(VX_TSV) as f:
        next(f)
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2 or not parts[0].strip():
                continue
            total += 1
            cell = parts[lu_idx] if -len(parts) <= lu_idx < len(parts) else ""
            d = parse_iso(cell)
            if d is None:
                continue
            age = (today - d).days
            if age > max_days:
                stale.append((age, parts[0], parts[1] if len(parts) > 1 else "", d))
    out = [f"  VX.tsv — {len(stale)}/{total} vectors older than {max_days}d"]
    for age, vid, name, d in sorted(stale, reverse=True)[:8]:
        out.append(f"    🟠 {vid:<18} {age:>3}d  ({d})  {name[:34]}")
    if len(stale) > 8:
        out.append(f"    · …and {len(stale)-8} more")
    return out


def main():
    today = date.today()
    print(f"\n{'='*72}")
    print(f"  MARCO Staleness Check — {datetime.now():%Y-%m-%d %H:%M}")
    print(f"{'='*72}\n")
    print(check_status(today, _arg("--status-days", DEFAULT_STATUS_DAYS)))
    print()
    for line in check_vx(today, _arg("--vx-days", DEFAULT_VX_DAYS)):
        print(line)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
