#!/usr/bin/env python3
"""
boot.py — FLG boot instrument. Wall clock + ledger staleness + predictions-due
+ triggers-due + quarter-due, one verdict.

Built by DAEDALUS 2026-08-20 (FLG greenfield build; pattern = FERT boot.py, which
inherits the WATT/VULCAN/MIDAS trio incl. the marker-contract fix for
ledger_staleness). cwd-proof + self-locating: lives at AGENTS/FLG/boot.py ->
parents[2] == repo root. Pure stdlib — no venv-only imports (PAT-103 n/a).

Legs:
  1. ledger staleness — workbook/*.tsv AND TRADE.md (shared script; verdict is
     rc OR marker, never bare output-nonempty — the clean run prints a SCOPE
     line that a nonempty test misreads as an alert).
  2. predictions-due  — workbook/PREDICTIONS.tsv rows past Resolve_By still OPEN.
  3. triggers-due     — workbook/TRIGGERS.tsv rows past Next_Check.
  4. quarter-due      — FLG-SPECIFIC. The desk's clock is the FFIEC Call Report
     (~quarter-end + 45d). If a quarter has closed and its filing window has
     passed with no matching row in MI3_FLG.tsv, that is an un-ingested filing.
     It is a PROMPT TO LOOK, never a claim the filing exists — the flag text
     says so, because a check that overstates what it knows trains skipping.

Combined exit (CHECK_STANDARD §9): 0 = quiet · 1 = REVIEW (something due/stale)
· 2 = a leg FAILED / cannot certify. rc 2 is never "quiet" — an absent register
means enforcement is silently absent (PAT-074: audit a check by what its PASS
means, not by what its failure means).
"""

import csv
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STALENESS = ROOT / "scripts" / "ledger_staleness.py"
PREDICTIONS = HERE / "workbook" / "PREDICTIONS.tsv"
TRIGGERS = HERE / "workbook" / "TRIGGERS.tsv"
MI3 = HERE / "workbook" / "MI3_FLG.tsv"

# Call Report filing lag. 45d is the FFIEC convention this desk's clock uses;
# it is a RULE anchor, not an announced date (charter WAKE TRIGGERS).
CALL_REPORT_LAG_DAYS = 45


def run_alert(cmd):
    """Runner for the shared ledger_staleness check. rc contract (CHECK_STANDARD
    §8 rule 3 / §9): 0 clean · 1 stale FINDINGS · 2 CANNOT-CERTIFY (MISCONFIGURED
    / LEDGERS-OUTSIDE-GLOB / usage). Verdict = rc 1 OR marker-present (§8 rule 5
    keeps the marker channel authoritative); never bare output-nonempty, which
    mis-reads the clean-run scope statement ("trade perimeter: ...") as an alert.
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


def _tsv_rows(path):
    """DictReader over a TSV, skipping leading '#' comment lines."""
    with path.open(encoding="utf-8") as f:
        lines = [ln for ln in f if not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def dated_scan(path, date_col, label, status_col=None, live_statuses=None):
    """Generic due-scan: rows whose date_col <= today (optionally filtered to
    live statuses). Returns (rc, [lines]). rc 0 = none due · 1 = due · 2 = error.
    Null output states its SCOPE, never a bare benign line
    (STRICT_TEXT rule 9 / finding_verification_zero_is_ambiguous)."""
    if not path.exists():
        return 2, [f"  🔴 {label}: {path.name} MISSING — the register this leg certifies does not exist; "
                   f"enforcement is silently absent, do NOT read this as quiet"]
    today = date.today()
    due, unparsed = [], 0
    try:
        rows = _tsv_rows(path)
        for r in rows:
            if status_col and live_statuses is not None:
                if (r.get(status_col) or "").strip().upper().split(" ")[0] not in live_statuses:
                    continue
            raw = (r.get(date_col) or "").strip()
            try:
                when = datetime.strptime(raw[:10], "%Y-%m-%d").date()
            except ValueError:
                if raw:
                    unparsed += 1
                continue
            if when <= today:
                rid = (r.get("ID") or "?").strip()
                what = (r.get("Trigger") or r.get("Prediction") or "").strip()[:70]
                due.append(f"  ⚠️ DUE: {rid} [{raw}] {what}")
    except Exception as e:  # noqa: BLE001
        return 2, [f"  🔴 {label}: scan error {type(e).__name__}: {e}"]
    tail = f" ({unparsed} row(s) had an unparsable {date_col} — not scanned)" if unparsed else ""
    if not due:
        return 0, [f"  ✓ none due — {label}: {len(rows)} data row(s) scanned on {date_col}{tail}"]
    return 1, due + [f"  ({len(rows)} row(s) scanned on {date_col}{tail})"]


def _quarter_end(qstr):
    """Parse the MI3 'quarter' cell (M/D/YYYY) into a date. Returns None if
    unparsable — the caller counts those rather than silently dropping them."""
    try:
        return datetime.strptime(qstr.strip(), "%m/%d/%Y").date()
    except ValueError:
        return None


def quarter_due():
    """FLG-specific: has a Call Report quarter closed and passed its filing
    window with no row in MI3_FLG.tsv? Returns (rc, [lines])."""
    if not MI3.exists():
        return 2, [f"  🔴 quarter-due: {MI3.name} MISSING — the Call Report series this desk "
                   f"is built on does not exist; enforcement silently absent"]
    try:
        rows = _tsv_rows(MI3)
        quarters = [q for q in (_quarter_end(r.get("quarter") or "") for r in rows) if q]
    except Exception as e:  # noqa: BLE001
        return 2, [f"  🔴 quarter-due: scan error {type(e).__name__}: {e}"]
    if not quarters:
        return 2, ["  🔴 quarter-due: 0 parsable 'quarter' cells in MI3_FLG.tsv — "
                   "cannot certify the filing clock (format may have changed)"]
    newest = max(quarters)
    today = date.today()
    # Walk forward one quarter at a time from the newest ingested quarter-end.
    missing = []
    probe = newest
    while True:
        y, m = probe.year, probe.month + 3
        if m > 12:
            y, m = y + 1, m - 12
        # last day of that month = first of next month minus a day
        ny, nm = (y, m + 1) if m < 12 else (y + 1, 1)
        probe = date(ny, nm, 1) - timedelta(days=1)
        if probe >= today:
            break
        if probe + timedelta(days=CALL_REPORT_LAG_DAYS) <= today:
            missing.append(probe)
        else:
            break
    if not missing:
        return 0, [f"  ✓ none due — newest ingested quarter {newest.isoformat()}; "
                   f"no closed quarter is past its ~{CALL_REPORT_LAG_DAYS}d filing window"]
    lines = [f"  ⚠️ DUE: {len(missing)} quarter(s) past the ~{CALL_REPORT_LAG_DAYS}d filing window "
             f"with no MI3_FLG.tsv row: {', '.join(q.isoformat() for q in missing)}",
             f"     (newest ingested: {newest.isoformat()}. This is a PROMPT TO LOOK at FFIEC CDR "
             f"RSSD 694904 — NOT a claim the filing exists. Filings slip.)"]
    return 1, lines


def main():
    print("=" * 74)
    print(f"  ⏰ WALL CLOCK: {datetime.now().strftime('%Y-%m-%d %H:%M %A')} — never hand-write a time; copy this line")
    print("  FLG BOOT — ledger staleness · predictions-due · triggers-due · quarter-due")
    print("=" * 74)
    rcs = []

    print("\n--- 1. ledger staleness (workbook + TRADE.md) ---")
    sw = run_alert([str(STALENESS), "FLG", "--quiet"])
    st = run_alert([str(STALENESS), "FLG", "--trade", "--quiet"])
    if sw == st == 0:
        print("  ✓ quiet (alert-contract: this check prints only when stale or misconfigured)")
    rcs.append(2 if 2 in (sw, st) else (1 if 1 in (sw, st) else 0))

    print("\n--- 2. predictions-due (OPEN rows past Resolve_By) ---")
    rc, lines = dated_scan(PREDICTIONS, "Resolve_By", "predictions",
                           status_col="Status", live_statuses={"OPEN"})
    print("\n".join(lines))
    rcs.append(rc)

    print("\n--- 3. triggers-due (wake register past Next_Check) ---")
    rc, lines = dated_scan(TRIGGERS, "Next_Check", "triggers")
    print("\n".join(lines))
    rcs.append(rc)

    print("\n--- 4. quarter-due (Call Report clock, RSSD 694904) ---")
    rc, lines = quarter_due()
    print("\n".join(lines))
    rcs.append(rc)

    print("\n" + "=" * 74)
    if 2 in rcs:
        print("  FLG boot: a leg FAILED — check manually, do NOT assume quiet.")
        return 2
    if 1 in rcs:
        print("  FLG boot: REVIEW — work the flagged items before new research.")
        return 1
    print("  FLG boot: all quiet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
