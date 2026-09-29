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

  2. THE LIVE ROW, NOT THE FILE (rewritten 2026-09-29; was "MAX, NOT FIRST").
     The old reducer took max() over every obs token on any keyword line, so a
     stale live row plus an unrelated later-dated note read FRESH, and a date
     AHEAD of FRED read FRESH too. Now each series is read from its one live
     KEY THRESHOLDS row; missing / duplicated / multi-date rows are CANNOT-VERIFY,
     and AHEAD-of-FRED is CANNOT-VERIFY. Historical rows are inert because they
     are never read. Regression suite: tests/test_spine_check.py.

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

# series_id, human label, regex for the ONE live KEY THRESHOLDS row that carries it.
# ROW-ANCHORED since 2026-09-29 (reviewer-found false passes, reproduced before fixing):
# the old matcher took max() over ANY line carrying a keyword + an `obs` token, so a
# stale live row plus an unrelated later-dated note certified FRESH, and a date AHEAD
# of FRED also printed FRESH. Now: the live row, exactly one of it, exactly one obs.
SPINE = [
    ("ICSA",   "Initial claims",    r"^\|\s*Initial claims \(MA basis\)\s*\|"),
    ("CCSA",   "Continuing claims", r"^\|\s*Continuing claims\s*\|"),
    # Added 2026-09-29 (L-26 n=2): JOLTS Aug printed 9/29 while labor_data.py had
    # already FETCHED it at boot — nothing compared its obs date to STATUS. FL UR
    # sat two prints stale the same way.
    ("JTSHIL", "JOLTS hires",       r"^\|\s*JOLTS hires\b"),
    ("FLUR",   "FL UR",             r"^\|\s*FL UR\s*\|"),
]


def parse_spine(text):
    """{series_id: (obs_date | None, reason)} from the series' LIVE row only.

    None + reason when the row is missing, duplicated, carries no obs token, or
    carries more than one distinct obs date — every one of those is CANNOT-VERIFY,
    never a pass. Dates elsewhere in the file are ignored by construction."""
    out = {}
    lines = text.split("\n")
    for sid, _label, row_rx in SPINE:
        rows = [l for l in lines if re.search(row_rx, l)]
        if not rows:
            out[sid] = (None, "live row not found")
            continue
        if len(rows) > 1:
            out[sid] = (None, f"{len(rows)} rows match the live-row anchor — ambiguous")
            continue
        dates = sorted(set(OBS_RE.findall(rows[0])))
        if not dates:
            out[sid] = (None, "live row carries no `obs YYYY-MM-DD` token")
        elif len(dates) > 1:
            out[sid] = (None, f"live row carries {len(dates)} different obs dates {dates}")
        else:
            out[sid] = (dates[0], "live row")
    return out


def verdict(s_date, f_date):
    """FRESH only on exact equality. STATUS behind FRED = STALE. STATUS AHEAD of
    FRED = AHEAD: an observation FRED does not hold is unverified, never fresh."""
    if s_date == f_date:
        return "FRESH"
    return "STALE" if s_date < f_date else "AHEAD"


def status_obs_dates():
    if not STATUS.exists():
        return {sid: (None, "STATUS.md missing") for sid, _, _ in SPINE}
    return parse_spine(STATUS.read_text(encoding="utf-8", errors="ignore"))


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
        s_date, why = parsed[sid]
        f_date, f_extra = fred_newest(sid)

        if f_date is None:
            print(f"  ⚠️  {label:<20} CANNOT VERIFY — FRED unreachable ({f_extra}). "
                  f"NOT a pass; re-run before trusting the spine.")
            unverifiable.append(label)
            continue

        if s_date is None:
            print(f"  ⚠️  {label:<20} CANNOT VERIFY — {why} (FRED newest {f_date}).")
            print(f"      ↳ The gate reads ONLY the series' live KEY THRESHOLDS row; give it "
                  f"exactly one ISO `obs` token there.")
            unverifiable.append(label)
            continue

        v = verdict(s_date, f_date)
        if v == "STALE":
            lag = (datetime.fromisoformat(f_date) - datetime.fromisoformat(s_date)).days
            print(f"  🔴 {label:<20} STATUS SPINE STALE — STATUS obs {s_date}, "
                  f"FRED obs {f_date} ({lag}d newer, value {f_extra})")
            print(f"      ↳ A print has LANDED UNNOTICED. Refresh the STATUS spine "
                  f"BEFORE any analysis (B2a), then sweep EVERY surface carrying it (C1).")
            stale.append(label)
        elif v == "AHEAD":
            print(f"  ⚠️  {label:<20} CANNOT VERIFY — STATUS obs {s_date} is AHEAD of FRED "
                  f"obs {f_date}: an observation FRED does not hold is unverified, not fresh.")
            unverifiable.append(label)
        else:
            print(f"  ✅ SPINE FRESH: {label:<12} STATUS obs {s_date} == FRED obs {f_date}"
                  f"   [live row]")

    print()
    if stale:
        print(f"  🔴 SPINE GATE FAILED — {len(stale)} series behind FRED: {', '.join(stale)}")
        print(f"      This is boot step B2a and it OUTRANKS the task you booted for.")
    if unverifiable:
        print(f"  ⚠️  SPINE GATE INCONCLUSIVE — {len(unverifiable)} series unverifiable: "
              f"{', '.join(unverifiable)}. Treat as NOT CHECKED, never as clean.")
    if not stale and not unverifiable:
        print(f"  ✅ SPINE GATE PASS — STATUS matches FRED on every spine series (claims · JOLTS · FL UR).")
    print()
    return 2 if (stale or unverifiable) else 0


if __name__ == "__main__":
    sys.exit(main())
