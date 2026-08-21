#!/usr/bin/env python3
"""
boot.py — VULCAN boot instrument. Ledger staleness + predictions-due, one verdict.

Built by DAEDALUS 2026-07-10 (VULCAN build). cwd-proof + self-locating: lives at
AGENTS/VULCAN/boot.py -> parents[2] == repo root; finds scripts/ledger_staleness.py
regardless of launch cwd.

Boot step 4 in CLAUDE.md. Four legs:
  1. ledger staleness — workbook/*.tsv AND TRADE.md vs STATUS mtime (shared script).
  2. predictions-due  — workbook/PREDICTIONS.tsv rows past resolve_date still OPEN.
  3. S2 series age    — workbook/S2_SERIES.tsv vintage, CONTENT-derived from the
     row's own asof_utc (never mtime — git sync restamps mtime and the check would
     fail false-negative). Advisory only: it prompts you to run tools/semi_watch.py,
     it does NOT fetch (boot stays fast and offline-safe).
  4. MAG7 series age  — workbook/MAG7_SERIES.tsv vintage, CONTENT-derived from the
     row's own holdings_asof. Added 2026-08-21 the same day the instrument was built,
     because building the tool that fixes six-week rot WITHOUT the alarm that reports
     rot leaves the same hole one level down. Cadence is deliberately SLOWER than S2's
     (index weights move slowly; SPY publishes daily but the number does not move
     daily) — see MAG7_MAX_AGE_DAYS.

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
MAG7_SERIES = HERE / "workbook" / "MAG7_SERIES.tsv"
# 21d, and the bound is set from the CADENCE of what it measures, not inherited:
# index weights drift slowly, so a daily bound would cry wolf. But it must be well
# inside the 6-WEEK rot that made this instrument necessary — 21d catches that class
# twice over. (`finding_inherited_default_threshold_is_a_silent_decision`)
MAG7_MAX_AGE_DAYS = 21


def run(cmd):
    try:
        return subprocess.run([sys.executable, *cmd], cwd=str(ROOT)).returncode
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2


def run_alert(cmd):
    """Run the shared ledger_staleness check. rc contract REVISED 2026-08-17
    (DAEDALUS shared-script fix, PROME-approved, CHECK_STANDARD §8 rule 3):
    0 clean · 1 stale FINDINGS · 2 CANNOT-CERTIFY (MISCONFIGURED /
    LEDGERS-OUTSIDE-GLOB / usage) — the old 'always 0' alert contract is
    retired; rc now AGREES with the ⚠️/🔴 markers instead of contradicting
    them. Verdict = rc 1 OR marker-present (§8 rule 5 keeps the marker channel
    authoritative; still never bare output-nonempty — the 8/11→8/16 scope-line
    false-REVIEW stays fixed; CHECKS.tsv ledger_staleness row = contract home).
    rc 2 → leg failure (enforcement silently absent = never assume quiet).
    Returns 0 quiet · 1 REVIEW · 2 failure/cannot-certify."""
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
    if p.returncode not in (0, 1):
        return 2
    return 1 if (p.returncode == 1 or "⚠️" in out or "🔴" in out) else 0


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


def mag7_series_age():
    """Leg 4 — S1 concentration series vintage, derived from CONTENT (holdings_asof).

    Returns (rc, message). rc 0 = fresh · 1 = stale/absent (REVIEW) · 2 = unreadable.
    Like leg 3 it does NOT fetch — it tells you to run tools/mag7.py.

    Why it exists: the Mag-7 weight sat aggregator-sourced and six weeks stale while
    serving as BOTH S1's banded threshold input AND thesis-kill leg 2's instrument.
    An instrument with no staleness alarm is the same failure one level down.
    """
    if not MAG7_SERIES.exists():
        return 1, ("  MAG7 series ABSENT — run: python3 AGENTS/VULCAN/tools/mag7.py\n"
                   "    (S1's band input and thesis-kill leg 2 both read this number.)")
    try:
        rows = list(csv.DictReader(MAG7_SERIES.open(encoding="utf-8"), delimiter="\t"))
        if not rows:
            return 1, "  MAG7 series is header-only — run tools/mag7.py"
        last = rows[-1]
        vintage = datetime.strptime(last.get("holdings_asof", ""), "%d-%b-%Y").date()
    except Exception as e:  # noqa: BLE001
        return 2, f"  MAG7 series UNREADABLE ({type(e).__name__}) — inspect workbook/MAG7_SERIES.tsv"

    age = (date.today() - vintage).days
    notes = []
    if str(last.get("validation", "")).startswith("ERR"):
        notes.append("⚠️ last row failed validation — do not read it as data")
    band = str(last.get("band", ""))
    if band and band != "below-yellow":
        notes.append(f"⚠️ BAND = {band}")
    # proximity warning: the whole point of the 8/21 pull was that 32.98% sat 0.019pp
    # under the line while the files said "comfortably below".
    try:
        pct = float(last.get("mag7_pct", "nan"))
        if 32.0 <= pct < 33.0:
            notes.append(f"⚠️ {pct:.2f}% is inside 1pp of the 33% yellow line — AT it, not below it")
    except (TypeError, ValueError):
        pass
    note = ("\n    " + " · ".join(notes)) if notes else ""

    if len(rows) < 2:
        note += "\n    ⚠️ n=1 — a LEVEL, not a trend (breadth IS measured; there is just no history of it yet)."
    if age > MAG7_MAX_AGE_DAYS:
        return 1, (f"  MAG7 series STALE {age}d (holdings as-of {vintage}, {len(rows)} rows) — "
                   f"run: python3 AGENTS/VULCAN/tools/mag7.py{note}")
    return 0, f"  \u2713 MAG7 series fresh ({age}d, {len(rows)} rows, holdings as-of {vintage}){note}"


def main():
    print("=" * 72)
    print("  VULCAN BOOT — ledger staleness · predictions-due · S2 + S1 series")
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

    print("\n--- 4. S1 Mag-7 concentration series (content-vintage) ---")
    m7_rc, m7_msg = mag7_series_age()
    print(m7_msg)
    rcs.append(m7_rc)

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
