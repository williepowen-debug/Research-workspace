#!/usr/bin/env python3
"""
boot.py — VULCAN boot instrument. Ledger staleness + predictions-due, one verdict.

Built by DAEDALUS 2026-07-10 (VULCAN build). cwd-proof + self-locating: lives at
AGENTS/VULCAN/boot.py -> parents[2] == repo root; finds scripts/ledger_staleness.py
regardless of launch cwd.

Boot step 4 in CLAUDE.md. Three legs:
  1. ledger staleness — workbook/*.tsv AND TRADE.md vs STATUS mtime (shared script).
  2. predictions-due  — workbook/PREDICTIONS.tsv rows past resolve_date still OPEN.
  3. S2 series age    — workbook/S2_SERIES.tsv vintage, CONTENT-derived from the
     row's own asof_utc (never mtime — git sync restamps mtime and the check would
     fail false-negative). Advisory only: it prompts you to run tools/semi_watch.py,
     it does NOT fetch (boot stays fast and offline-safe).

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
S2_SERIES = HERE / "workbook" / "S2_SERIES.tsv"
S2_MAX_AGE_DAYS = 7  # S2 is a score-3 channel; a week-old series is a stale channel


def run(cmd):
    try:
        return subprocess.run([sys.executable, *cmd], cwd=str(ROOT)).returncode
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2


def run_alert(cmd):
    """Run an ALERT-CONTRACT script (ledger_staleness: exit code ALWAYS 0 by
    documented contract). Relay its output; the flag is MARKER-PRESENT (a line
    carrying ⚠️/🔴), never rc and never bare output-nonempty — rc 1 is never
    emitted (dead-code fix 2026-07-31, PAT-074), and since 8/11 the script also
    prints an unmarked SCOPE line ('trade perimeter: ...') even when clean, so
    bare-nonempty false-REVIEWed every clean boot 8/11→8/16 (DAEDALUS marker
    fix 2026-08-16, Will-approved; CHECKS.tsv ledger_staleness row = contract home).
    Returns 0 quiet · 1 alert-marker printed (REVIEW) · 2 launch/usage failure."""
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
    return 1 if ("⚠️" in out or "🔴" in out) else 0


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



def s2_series_age():
    """Leg 3 — S2 memory-cycle series vintage, derived from CONTENT (asof_utc).

    Returns (rc, message). rc 0 = fresh · 1 = stale/absent (REVIEW) · 2 = unreadable.
    Deliberately does NOT fetch: boot must stay fast and work offline. It tells you
    to run tools/semi_watch.py; running it is the session's job.
    """
    if not S2_SERIES.exists():
        return 1, ("  S2 series ABSENT — run: python3 AGENTS/VULCAN/tools/semi_watch.py\n"
                   "    (S2 is at score 3 with no retained history; the live read is a point, not a trend.)")
    try:
        rows = list(csv.DictReader(S2_SERIES.open(encoding="utf-8"), delimiter="\t"))
        if not rows:
            return 1, "  S2 series is header-only — run tools/semi_watch.py"
        stamp = rows[-1].get("asof_utc", "")
        vintage = datetime.strptime(stamp[:10], "%Y-%m-%d").date()
    except Exception as e:  # noqa: BLE001
        return 2, f"  S2 series UNREADABLE ({type(e).__name__}) — inspect workbook/S2_SERIES.tsv"

    age = (date.today() - vintage).days
    n_err = sum(1 for k, v in rows[-1].items() if str(v).startswith("ERR:"))
    err_note = f"  ⚠️ last row has {n_err} ERR field(s) — do not read them as data." if n_err else ""
    if age > S2_MAX_AGE_DAYS:
        return 1, (f"  S2 series STALE {age}d (last {vintage}, {len(rows)} rows) — "
                   f"run: python3 AGENTS/VULCAN/tools/semi_watch.py{err_note}")
    return (1 if n_err else 0), f"  \u2713 S2 series fresh ({age}d, {len(rows)} rows, last {vintage}){err_note}"


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

    print("\n--- 3. S2 memory-cycle series (content-vintage) ---")
    s2_rc, s2_msg = s2_series_age()
    print(s2_msg)
    rcs.append(s2_rc)

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
