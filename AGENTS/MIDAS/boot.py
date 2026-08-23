#!/usr/bin/env python3
"""
boot.py — MIDAS boot instrument. Metals spot/yield + ledger staleness + predictions-due, one verdict.

Built by DAEDALUS 2026-07-11 (MIDAS build); metals_watch.py wired in 2026-07-12
(MIDAS first real session, PAT-041 — cadence wired same session as the build).
cwd-proof + self-locating: lives at AGENTS/MIDAS/boot.py -> parents[2] == repo
root; finds scripts/ledger_staleness.py and metals_watch.py regardless of
launch cwd.

Boot step 4 in CLAUDE.md. Three legs:
  0. metals_watch.py — real yield (FRED DFII10) + gold/silver/copper/Pt/Pd
     spot (futures + ETF proxy) + GSR + M1 divergence classifier.
  1. ledger staleness — workbook/*.tsv AND TRADE.md vs STATUS mtime (shared script).
  2. predictions-due  — workbook/PREDICTIONS.tsv rows past resolve_date still OPEN.

Combined exit: 0 = quiet · 1 = REVIEW (metals leg flagged, stale ledger, or
prediction due) · 2 = a leg failed. The verdict line NAMES the leg(s) that
flagged — legs are carried as (label, rc) pairs, not bare ints, so the footer
cannot describe a cause that did not occur (fixed 2026-08-23: the footer named
only the ledger and predictions legs on an rc=1 raised by the METALS leg alone,
sending a reader hunting for two conditions that were both clean).
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
METALS_WATCH = HERE / "metals_watch.py"

# Prefer the repo venv interpreter for child scripts: metals_watch needs
# yfinance, which lives in .venv/ (not system python). Without this, launching
# boot.py with system `python3` makes leg 0 die with "No module named
# 'yfinance'". Falls back to the launching interpreter if .venv is absent.
# (MIDAS 2026-07-23 hygiene fix; the venv wall was documented in SOURCES.md L13.)
_VENV_PY = ROOT / ".venv" / "bin" / "python"
PYTHON = str(_VENV_PY) if _VENV_PY.exists() else sys.executable


def run_marked(cmd):
    """Run a leg and apply the SAME verdict contract run_alert uses for the
    staleness legs: rc 1 OR a ⚠️/🔴 marker in stdout ⇒ REVIEW (CHECK_STANDARD §8
    rule 5, marker channel authoritative). DAEDALUS SFG sweep 2026-08-17 ACTION 2
    — the metals leg was rc-ONLY, so a metals_watch warning printed at rc 0 could
    not reach the verdict line. Built 2026-08-23.

    ⚠️ MEASURED AT BUILD TIME, AND SAY SO: `metals_watch.py` currently emits ZERO
    ⚠️/🔴 markers — it encodes every state in its rc — so this marker test is
    INERT TODAY. It is installed as a CONTRACT, not as a behaviour fix: if the
    metals leg ever gains a warn-at-rc-0 state, the verdict picks it up without
    anyone remembering to rewire boot. Do not record this as having changed what
    boot reports. A ported guard whose triggering condition does not exist in the
    recipient is inert, however correct the donor was
    (`finding_guard_correctness_and_wiring_are_independent`)."""
    sys.stdout.flush()
    try:
        pr = subprocess.run([PYTHON, *cmd], cwd=str(ROOT),
                            capture_output=True, text=True)
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2
    out = pr.stdout or ""
    if out:
        print(out, end="")
    if pr.stderr:
        print(pr.stderr, file=sys.stderr, end="")
    if pr.returncode not in (0, 1):
        return 2
    return 1 if (pr.returncode == 1 or "⚠️" in out or "🔴" in out) else 0


def run(cmd):
    sys.stdout.flush()  # avoid interleaving with the child's unbuffered stdout
    try:
        return subprocess.run([PYTHON, *cmd], cwd=str(ROOT)).returncode
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


def main():
    print("=" * 72)
    print("  MIDAS BOOT — metals watch · ledger staleness · predictions-due")
    print("=" * 72)
    legs = []  # (label, rc) — labelled so the verdict can name the cause

    print("\n--- 0. metals_watch (real yield + spot + GSR + M1 divergence) ---")
    if METALS_WATCH.exists():
        mw = run_marked([str(METALS_WATCH)])
        legs.append(("metals watch", mw))
    else:
        # Fail LOUD. An absent instrument is NOT a quiet one — same contract the
        # run_alert docstring states for ledger_staleness ("enforcement silently
        # absent = never assume quiet"). Pre-2026-08-23 this printed one line and
        # contributed nothing, so a deleted metals_watch.py returned "all quiet".
        print("  🔴 metals_watch.py NOT FOUND — leg cannot certify, verdict is NOT quiet")
        legs.append(("metals watch", 2))

    print("\n--- 1. ledger staleness (workbook + TRADE.md vs STATUS) ---")
    sw = run_alert([str(STALENESS), "MIDAS", "--quiet"])
    st = run_alert([str(STALENESS), "MIDAS", "--trade", "--quiet"])
    if sw == st == 0:
        print("  ✓ quiet (alert-contract: output only when stale/misconfigured)")
    legs.append(("ledger staleness", 2 if 2 in (sw, st) else (1 if 1 in (sw, st) else 0)))

    print("\n--- 2. predictions-due scan ---")
    n_due, due = predictions_due()
    if due:
        for d in due:
            print(f"  DUE: {d}")
        legs.append(("predictions due", 1))
    elif n_due == 0:
        print("  none due (or newborn ledger)")
        legs.append(("predictions due", 0))
    else:
        legs.append(("predictions due", 2))

    print("\n" + "=" * 72)
    failed = [name for name, rc in legs if rc == 2]
    flagged = [name for name, rc in legs if rc == 1]
    if failed:
        print(f"  MIDAS boot: leg FAILED — {', '.join(failed)}. "
              "Check manually, do NOT assume quiet.")
        return 2
    if flagged:
        print(f"  MIDAS boot: REVIEW — {', '.join(flagged)}.")
        return 1
    print("  MIDAS boot: all quiet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
