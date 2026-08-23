#!/usr/bin/env python3
"""
LABOR SPINE FRESHNESS GATE — BD-02, built 2026-08-23 after THREE misses.

Automates CLAUDE.md boot step B2a: compare the observation date STATUS.md carries
for the core claims spine against the newest observation FRED actually holds. If
FRED is newer, a print has LANDED UNNOTICED and the STATUS spine must be refreshed
BEFORE any analysis.

WHY THIS EXISTS (the misses it is paid for):
  2026-07-16  claims print (208K w/e 7/11) sat unnoticed while 7 live STATUS
              surfaces still presented w/e Jul-4 as current. Caught 4 days later
              by a seeded sweep, not by boot.
  2026-07-31  STATUS stamped 7/24 still presenting w/e Jul 18 as current while the
              7/30 print had landed with a frozen grading card waiting for it.
  2026-08-20  STATUS carried w/e Aug 1 while FRED carried TWO later prints
              (w/e 8/8 and 8/15). DAEDALUS's external sweep flagged it 8/17 —
              THREE DAYS BEFORE LABOR's own boot did.

DESIGN NOTES — each one is a defect this script is deliberately avoiding:

  1. ISO TOKENS ONLY. We parse `obs YYYY-MM-DD` and nothing else. STATUS also
     carries prose dates ("w/e Aug 15"), and parsing those is exactly the
     fragility that got BD-02 deferred three times. A prose-only STATUS reports
     CANNOT-VERIFY, never a false PASS.

  2. MAX, NOT FIRST. STATUS legitimately carries OLD obs dates in dated-historical
     rows (graded calendar rows, prior UPDATE blocks) — those are correct and must
     not trip the gate. The question is "does STATUS know about the newest print?",
     so the reducer is max() over all obs tokens for the series. Historical rows
     are therefore inert here by construction, not by exclusion rules that rot.

  3. THREE STATES, NEVER SILENT. STALE / FRESH / CANNOT-VERIFY are all printed,
     every run. A check whose reporting is gated on a state — where the normal
     case is the silent one — is the exact defect found in catalyst_countdown.py
     on 2026-08-23 (it collected past-due rows but printed them only when the
     upcoming list was empty, i.e. never on a normal boot). That failure is
     silent AND clean, which is the worst combination. Every line here carries a
     KEY_MARKER so boot.py's collapsed (non-verbose) view cannot filter it out.

  4. A FETCH FAILURE IS NOT A PASS. If FRED cannot be reached the series reports
     CANNOT-VERIFY and the exit code still signals. Never report a clean spine
     because the instrument was blind.

Usage:
  .venv/bin/python3 AGENTS/LABOR/scripts/spine_check.py
Exit: 0 = all fresh · 2 = stale or unverifiable (boot.py treats 2 as alert)
"""

import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
LABOR_DIR = SCRIPTS_DIR.parent
WORKSPACE = LABOR_DIR.parent.parent
STATUS = LABOR_DIR / "STATUS.md"
FETCH = WORKSPACE / "FORGE" / "tools" / "market-data" / "fetch.py"
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"
PYTHON = str(VENV_PYTHON) if VENV_PYTHON.exists() else sys.executable

OBS_RE = re.compile(r"obs\s+(\d{4}-\d{2}-\d{2})")

# series_id, human label, keywords that tie a STATUS line to this series.
# Matching is per-LINE: a line must carry an `obs` token AND one of these.
SPINE = [
    ("ICSA", "Initial claims",    ("icsa", "initial claims", "4-wk ma", "dol/fred")),
    ("CCSA", "Continuing claims", ("ccsa", "continuing claims")),
]


def status_obs_dates():
    """{series_id: (max_obs_date, n_lines_seen)} parsed from STATUS.md."""
    out = {sid: (None, 0) for sid, _, _ in SPINE}
    if not STATUS.exists():
        return out
    for line in STATUS.read_text(encoding="utf-8", errors="ignore").split("\n"):
        obs = OBS_RE.findall(line)
        if not obs:
            continue
        low = line.lower()
        for sid, _label, keys in SPINE:
            if any(k in low for k in keys):
                best, n = out[sid]
                newest = max(obs)
                out[sid] = (max(best, newest) if best else newest, n + 1)
    return out


def fred_newest(series_id):
    """(iso_date, value) newest observation, or (None, error_string)."""
    try:
        r = subprocess.run(
            [PYTHON, str(FETCH), "fred", series_id, "--periods", "2", "--json"],
            capture_output=True, text=True, timeout=45,
        )
        if r.returncode != 0:
            return None, f"fetch.py exit {r.returncode}"
        data = json.loads(r.stdout)
        obs = data.get("observations") or data.get("data") or []
        if not obs:
            return None, "no observations returned"
        first = obs[0]
        date = first.get("date") or first.get("obs_date")
        val = first.get("value")
        if not date:
            return None, "no date field in response"
        return date, val
    except subprocess.TimeoutExpired:
        return None, "fetch timed out"
    except Exception as e:                                    # noqa: BLE001
        return None, f"{type(e).__name__}: {str(e)[:60]}"


def main():
    print(f"\n{'='*72}")
    print(f"  LABOR Spine Freshness Gate (B2a / BD-02) — {datetime.now():%Y-%m-%d %H:%M}")
    print(f"  Compares STATUS.md `obs YYYY-MM-DD` tokens vs newest FRED observation")
    print(f"{'='*72}\n")

    parsed = status_obs_dates()
    stale, unverifiable = [], []

    for sid, label, _keys in SPINE:
        s_date, n_lines = parsed[sid]
        f_date, f_extra = fred_newest(sid)

        if f_date is None:
            print(f"  ⚠️  {label:<20} CANNOT VERIFY — FRED unreachable ({f_extra}). "
                  f"NOT a pass; re-run before trusting the spine.")
            unverifiable.append(label)
            continue

        if s_date is None:
            print(f"  ⚠️  {label:<20} CANNOT VERIFY — no `obs YYYY-MM-DD` token found in "
                  f"STATUS.md for this series (FRED newest {f_date}).")
            print(f"      ↳ Prose dates alone cannot be checked. Add an ISO `obs` token "
                  f"to the surface that carries this series.")
            unverifiable.append(label)
            continue

        if s_date < f_date:
            lag = (datetime.fromisoformat(f_date) - datetime.fromisoformat(s_date)).days
            print(f"  🔴 {label:<20} STATUS SPINE STALE — STATUS obs {s_date}, "
                  f"FRED obs {f_date} ({lag}d newer, value {f_extra})")
            print(f"      ↳ A print has LANDED UNNOTICED. Refresh the STATUS spine "
                  f"BEFORE any analysis (B2a), then sweep EVERY surface carrying it (C1).")
            stale.append(label)
        else:
            note = "" if s_date == f_date else "  (STATUS ahead — unreleased/manual entry)"
            print(f"  ✅ SPINE FRESH: {label:<12} STATUS obs {s_date} == FRED obs {f_date}"
                  f"{note}   [{n_lines} obs token(s) read]")

    print()
    if stale:
        print(f"  🔴 SPINE GATE FAILED — {len(stale)} series behind FRED: {', '.join(stale)}")
        print(f"      This is boot step B2a and it OUTRANKS the task you booted for.")
    if unverifiable:
        print(f"  ⚠️  SPINE GATE INCONCLUSIVE — {len(unverifiable)} series unverifiable: "
              f"{', '.join(unverifiable)}. Treat as NOT CHECKED, never as clean.")
    if not stale and not unverifiable:
        print(f"  ✅ SPINE GATE PASS — STATUS matches FRED on every core claims series.")
    print()
    return 2 if (stale or unverifiable) else 0


if __name__ == "__main__":
    sys.exit(main())
