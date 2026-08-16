#!/usr/bin/env python3
"""
boot.py — WATT boot instrument. Runs three checks, one combined verdict.

Built by DAEDALUS 2026-07-10 (WATT spinout, Step-2). cwd-proof + self-locating:
lives at AGENTS/WATT/boot.py -> parents[2] == repo root; finds power_watch.py
(sibling) and scripts/ledger_staleness.py (root) regardless of launch cwd.

Boot step 4 in CLAUDE.md. Three legs:
  1. power_watch.py   — PJM emergency postings + EIA-930 demand + retail backdrop
                        (P1 stress->price live read). Its own rc: 0 quiet / 1
                        emergency-class posting / 2 fetch-fail.
  2. ledger staleness — workbook/*.tsv AND the TRADE.md surface vs STATUS mtime
                        (shared scripts/ledger_staleness.py, --quiet).
  3. predictions-due  — workbook/PREDICTIONS.tsv rows past their resolve date
                        still marked OPEN/ACTIVE.

Combined exit: 0 = all quiet · 1 = something needs REVIEW (emergency posting,
stale ledger, or a prediction due) · 2 = a leg failed to run (never assume quiet).
"""

import csv
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
POWER_WATCH = HERE / "power_watch.py"
STALENESS = ROOT / "scripts" / "ledger_staleness.py"
PREDICTIONS = HERE / "workbook" / "PREDICTIONS.tsv"

# power_watch leg-4 (EIA wholesale) needs openpyxl, which lives in the repo .venv,
# NOT necessarily in the system python that the canonical `python3 boot.py` uses.
# Route child processes through the .venv interpreter when present so leg-4 doesn't
# false-fetch-fail on a box whose system python lacks openpyxl (memory:
# finding_market_data_venv_invocation). Falls back to sys.executable if no .venv.
_VENV_PY = ROOT / ".venv" / "bin" / "python3"
PYTHON = str(_VENV_PY) if _VENV_PY.exists() else sys.executable


def run(cmd):
    """Run a subprocess, stream its output, return its rc (or 2 on launch failure)."""
    try:
        r = subprocess.run([PYTHON, *cmd], cwd=str(ROOT))
        return r.returncode
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2


def run_alert(cmd):
    """Run an ALERT-CONTRACT script (ledger_staleness: prints only when something
    needs attention, exit code ALWAYS 0 by documented contract). Relay its output;
    the flag is MARKER-PRESENT (a line carrying ⚠️/🔴), never rc and never bare
    output-nonempty — rc 1 is never emitted (dead-code fix 2026-07-31, PAT-074),
    and since 8/11 the script also prints an unmarked SCOPE line
    ('trade perimeter: ...') even when clean, so bare-nonempty false-REVIEWed
    every clean boot 8/11→8/16 (DAEDALUS marker fix 2026-08-16, Will-approved;
    CHECKS.tsv ledger_staleness row = contract home).
    Returns 0 quiet · 1 alert-marker printed (REVIEW) · 2 launch/usage failure.
    power_watch keeps run(): it has REAL rc semantics (0/1/2 by its own contract)."""
    try:
        p = subprocess.run([PYTHON, *cmd], cwd=str(ROOT),
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
    """Return (n_due, rows) for PREDICTIONS.tsv rows past resolve-date still OPEN.
    Tolerant of an empty/newborn ledger. Expects a 'resolve_date' (or 'resolves')
    ISO-date col and a 'status' col; skips rows it can't parse rather than crashing."""
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
                return 0, []  # schema not ready yet — newborn ledger
            for row in reader:
                status = (row.get(scol) or "").strip().upper()
                if status not in ("OPEN", "ACTIVE", "PENDING"):
                    continue
                raw = (row.get(dcol) or "").strip()
                try:
                    when = datetime.strptime(raw[:10], "%Y-%m-%d").date()
                except ValueError:
                    continue
                if when <= today:
                    pid = row.get(cols.get("id", "id"), "?")
                    due.append(f"{pid} due {raw} (status {status})")
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: predictions scan error: {e}", file=sys.stderr)
        return 2, []
    return len(due), due


def main():
    print("=" * 72)
    print("  WATT BOOT — power_watch · ledger staleness · predictions-due")
    print("=" * 72)
    rcs = []

    print("\n--- 1. power_watch (P1 stress->price live read) ---")
    rcs.append(("power_watch", run([str(POWER_WATCH)])))

    print("\n--- 2. ledger staleness (workbook + TRADE.md vs STATUS) ---")
    # --days 7, NOT the shared script's 30-day default. That default is tuned for
    # "rot, not mild drift" — correct for a slow reference ledger, WRONG for this
    # seat: VX.tsv carries the per-channel convergence SCORES and FLOW.tsv the
    # pathways, both of which change on a normal session. On 2026-08-04 both sat
    # 13 days / 3 half-sessions behind STATUS — carrying P1=3 against STATUS's
    # P1=2, P3=3 against P3=4, and a "PJM_API_KEY DARK" note the key's restoration
    # had already falsified — and this leg printed "✓ quiet" the whole time,
    # because 13 < 30. Threshold is measured RELATIVE TO STATUS.md, so a long gap
    # between sessions does not trip it (STATUS ages too); only genuine
    # write-back drift does. Found by Will asking whether the prior session
    # closed out properly (L-26).
    sw = run_alert([str(STALENESS), "WATT", "--days", "7", "--quiet"])
    st = run_alert([str(STALENESS), "WATT", "--trade", "--days", "7", "--quiet"])
    if sw == st == 0:
        print("  ✓ quiet (alert-contract: output only when stale/misconfigured)")
    rcs.append(("staleness", 2 if 2 in (sw, st) else (1 if 1 in (sw, st) else 0)))

    print("\n--- 3. predictions-due scan ---")
    n_due, due = predictions_due()
    if n_due == 0:
        print("  none due (or newborn ledger)")
        rcs.append(("predictions", 0))
    elif due:
        for d in due:
            print(f"  DUE: {d}")
        rcs.append(("predictions", 1))
    else:  # scan error returned (n_due==2 sentinel path)
        rcs.append(("predictions", 2))

    # --- combined verdict ---
    fail = [n for n, c in rcs if c == 2]
    review = [n for n, c in rcs if c == 1]
    print("\n" + "=" * 72)
    if fail:
        print(f"  WATT boot: {', '.join(fail)} FAILED — check manually, do NOT assume quiet.")
        return 2
    if review:
        print(f"  WATT boot: REVIEW — {', '.join(review)}")
        return 1
    print("  WATT boot: all quiet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
