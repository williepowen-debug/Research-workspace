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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tsvutil import read_tsv, col, cell  # noqa: E402

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


# A row whose Status carries one of these is deliberately not maintained — its age
# is DESIGNED, not rot, so it must not inflate the stale count (and its Last Updated
# is intentionally left at the original data vintage, never restamped by the freeze:
# restamping would destroy the vintage signal — finding_hygiene_commit_rearms_the_staleness_lie).
# Tokens per AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md class 1.
DEAD_TOKENS = ("FROZEN", "SUPERSEDED", "RETIRED", "ARCHIVED", "NOT MAINTAINED")
# Statuses that get CITED. A stale row in one of these is the dangerous kind.
LOADED_STATUSES = ("BREACHED", "CRITICAL")


def check_vx(today, max_days):
    """Stale-row check, triaged by STATUS rather than by age alone.

    ⚠️ Why the triage exists (session 18, 2026-07-25): a flat '42/57 vectors >60d'
    count was printed at boot, read as housekeeping, and filed — and that same
    session two stale rows were cited and were wrong in OPPOSITE directions
    (FL-01 said hospitality wages 11% BELOW national when they were above; 3.01
    carried a '4.5x national' insurance figure that would not reproduce). A stale
    NORMAL row is harmless. A stale BREACHED/CRITICAL row is the loaded gun,
    because BREACHED is exactly what gets quoted into a thesis. One aggregate
    number hid both. So: separate alert, ranked first, never folded into the total.
    """
    if not VX_TSV.exists():
        return ["  ❌ workbook/VX.tsv not found"]

    # Banner-tolerant read (PAT-044 two-clock header). The two naive skips both
    # fail SILENTLY on a bannered file — `readline()` makes the banner the header
    # so every column lookup misses, and `next(f)` counts the real header row as a
    # vector, inflating the denominator by one. See scripts/tsvutil.py.
    header, data = read_tsv(VX_TSV)
    lu_idx = col(header, "Last Updated")
    st_idx = col(header, "Status")
    if lu_idx == -1 or st_idx == -1:
        # Fail LOUD. The old code fell back to "last column" here, which is exactly
        # how a mis-read header turns into a confident wrong answer instead of an error.
        return [f"  ❌ workbook/VX.tsv — expected columns not found "
                f"(Last Updated={lu_idx}, Status={st_idx}); header parsed as "
                f"{header[:3]}... — check for a malformed banner before trusting any VX count"]

    stale, loaded, scheduled, dead = [], [], [], 0
    total = 0
    for parts in data:
        if len(parts) < 2:
            continue
        total += 1
        status = cell(parts, st_idx).strip()
        if any(status.upper().startswith(t) for t in DEAD_TOKENS):
            dead += 1
            continue                       # deliberately not maintained — age is by design
        d = parse_iso(cell(parts, lu_idx))
        if d is None:
            continue
        age = (today - d).days
        if age > max_days:
            value = cell(parts, col(header, "Current Value"))
            rec = (age, parts[0], parts[1] if len(parts) > 1 else "", d, status)
            stale.append(rec)
            # A row on a declared cadence (annual Census/CBO) or with no live
            # instrument is stale BY DESIGN — surfacing it every boot beside real
            # rot is what turns the alert into noise, and an ignored alert is how
            # session 18 happened. It stays in the total; it leaves the 🔴 list.
            by_design = ("STALE BY DESIGN" in value.upper()
                         or "NO PRIMARY" in value.upper())
            if by_design:
                scheduled.append(rec)
            elif any(status.upper().startswith(s) for s in LOADED_STATUSES):
                loaded.append(rec)

    out = []
    if loaded:
        out.append(f"  🔴 VX.tsv — {len(loaded)} STALE **{'/'.join(LOADED_STATUSES)}** row(s) "
                   f">{max_days}d — these are the ones that get cited:")
        for age, vid, name, d, status in sorted(loaded, reverse=True):
            out.append(f"    🔴 {vid:<18} {age:>3}d  {status:<10} {name[:32]}")
        out.append("    (refresh, or mark FROZEN/RETIRED per STATE_VOCABULARY if the area is dead)")
        out.append("")
    other = [r for r in stale if r not in loaded and r not in scheduled]
    out.append(f"  VX.tsv — {len(stale)}/{total} vectors >{max_days}d  "
               f"[🔴 {len(loaded)} loaded-status · {len(scheduled)} stale-by-design "
               f"(awaiting scheduled print / no primary) · {len(other)} other · "
               f"{dead} excluded FROZEN/RETIRED]")
    for age, vid, name, d, status in sorted(other, reverse=True)[:8]:
        out.append(f"    🟠 {vid:<18} {age:>3}d  ({d})  {status:<10} {name[:30]}")
    if len(other) > 8:
        out.append(f"    · …and {len(other)-8} more")
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
