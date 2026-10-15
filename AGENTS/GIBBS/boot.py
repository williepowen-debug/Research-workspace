#!/usr/bin/env python3
"""
boot.py — GIBBS boot instrument. Wall clock + ledger staleness + predictions-due
+ prints-due + perimeter re-cut, one verdict.

Built by DAEDALUS 2026-10-14 (GIBBS build, WQ-426; pattern = FLG boot.py 2026-08-20).
cwd-proof + self-locating: AGENTS/GIBBS/boot.py -> parents[2] == repo root. Pure stdlib.

Legs:
  1. ledger staleness — workbook/*.tsv AND TRADE.md (shared script; verdict = rc OR
     marker, never bare output-nonempty).
  2. predictions-due  — workbook/PREDICTIONS.tsv OPEN rows past Resolve_By.
  3. prints-due       — docket/CATALYSTS.tsv rows dated TODAY, within PRINT_WINDOW_DAYS,
     or past (past rows are the OWNER's to prune; listed by count, oldest first).
  4. perimeter        — workbook/PERIMETER.tsv: (a) the quarterly re-cut is due once the
     next quarter-end + RECUT_LAG_DAYS has passed the As_Of; (b) any blank CIK is an
     unverified identifier (REGINALD's VLY/CIK lesson) — a PROMPT, never a claim.

Combined exit (CHECK_STANDARD §9): 0 quiet · 1 REVIEW · 2 a leg FAILED / cannot certify.
Drill clock: GIBBS_BOOT_TODAY=YYYY-MM-DD overrides today for drills ONLY (the header
line says so when set) — never set it in a real boot.
"""

import csv
import os
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STALENESS = ROOT / "scripts" / "ledger_staleness.py"
PREDICTIONS = HERE / "workbook" / "PREDICTIONS.tsv"
CATALYSTS = HERE / "docket" / "CATALYSTS.tsv"
PERIMETER = HERE / "workbook" / "PERIMETER.tsv"

PRINT_WINDOW_DAYS = 2      # same horizon as PROME's summons check (SUMMONS_WINDOW_DAYS)
RECUT_LAG_DAYS = 45        # quarter-end + ~45d: Q3 prints done and Y-9C window open — a RULE anchor

_DRILL = os.environ.get("GIBBS_BOOT_TODAY")
TODAY = date.fromisoformat(_DRILL) if _DRILL else date.today()


def run_alert(cmd):
    """Shared ledger_staleness runner (CHECK_STANDARD §8/§9): 0 quiet · 1 REVIEW · 2 failure."""
    try:
        p = subprocess.run([sys.executable, *cmd], cwd=str(ROOT), capture_output=True, text=True)
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2
    out, err = (p.stdout or "").strip(), (p.stderr or "").strip()
    if out:
        print(out)
    if err:
        print(err, file=sys.stderr)
    if p.returncode not in (0, 1):
        return 2
    return 1 if (p.returncode == 1 or "⚠️" in out or "🔴" in out) else 0


def _rows(path, skip_comments=True):
    with path.open(encoding="utf-8") as f:
        lines = [ln for ln in f if not (skip_comments and ln.startswith("#"))]
    return list(csv.DictReader(lines, delimiter="\t"))


def _missing(label, path):
    try:
        shown = path.relative_to(HERE)
    except ValueError:          # a drill or a moved file: never let the failure path itself crash
        shown = path
    return 2, [f"  🔴 {label}: {shown} MISSING — the register this leg certifies does not "
               f"exist; enforcement is silently absent, do NOT read this as quiet"]


def predictions_due():
    if not PREDICTIONS.exists():
        return _missing("predictions", PREDICTIONS)
    try:
        rows = _rows(PREDICTIONS)
    except Exception as e:  # noqa: BLE001
        return 2, [f"  🔴 predictions: read error {type(e).__name__}: {e}"]
    due, unparsed, open_n = [], 0, 0
    for r in rows:
        if (r.get("Status") or "").strip().upper().split(" ")[0] != "OPEN":
            continue
        open_n += 1
        raw = (r.get("Resolve_By") or "").strip()
        try:
            when = datetime.strptime(raw[:10], "%Y-%m-%d").date()
        except ValueError:
            unparsed += 1
            continue
        if when <= TODAY:
            due.append(f"  ⚠️ DUE: {(r.get('ID') or '?').strip()} [{raw}] {(r.get('Prediction') or '').strip()[:70]}")
    tail = f" ({unparsed} OPEN row(s) with an unparsable Resolve_By — not scanned)" if unparsed else ""
    if unparsed:
        due.append(f"  ⚠️ {unparsed} OPEN row(s) with an unparsable Resolve_By — cannot tell if due; fix the date")
    if due:
        return 1, due + [f"  ({len(rows)} row(s), {open_n} OPEN scanned on Resolve_By{tail})"]
    return 0, [f"  ✓ none due — {len(rows)} row(s), {open_n} OPEN scanned on Resolve_By"]


def prints_due():
    if not CATALYSTS.exists():
        return _missing("prints", CATALYSTS)
    try:
        rows = _rows(CATALYSTS, skip_comments=False)   # PROME's summons reader takes line 1 as the header
    except Exception as e:  # noqa: BLE001
        return 2, [f"  🔴 prints: read error {type(e).__name__}: {e}"]
    if rows and "date" not in rows[0]:
        return 2, ["  🔴 prints: CATALYSTS.tsv line 1 is not the `date…` header — PROME's summons reader would misparse it"]
    horizon = TODAY + timedelta(days=PRINT_WINDOW_DAYS)
    window, past, unparsed, forward = [], [], 0, 0
    for r in rows:
        raw = (r.get("date") or "").strip()
        try:
            when = datetime.strptime(raw[:10], "%Y-%m-%d").date()
        except ValueError:
            unparsed += 1
            continue
        if when >= TODAY:
            forward += 1
        line = f"{raw} [{(r.get('priority') or '?').strip()}] {(r.get('event') or '').strip()[:60]}"
        if when < TODAY:
            past.append((when, line))
        elif when <= horizon:
            window.append(f"  ⚠️ {'TODAY' if when == TODAY else f'in {(when - TODAY).days}d'}: {line}")
    out = list(window)
    if past:
        past.sort()
        out.append(f"  ⚠️ {len(past)} past-dated row(s) (oldest {past[0][0]}) — owner prunes or re-dates: "
                   + " · ".join(l for _, l in past[:3]) + (" …" if len(past) > 3 else ""))
    if forward == 0:
        out.append("  ⚠️ EMPTY-FORWARD: no row dated today or later — nothing can summon this desk")
    if unparsed:
        out.append(f"  ⚠️ {unparsed} row(s) with no parseable date — not scanned")
    if out:
        return 1, out + [f"  ({len(rows)} row(s) scanned; window {PRINT_WINDOW_DAYS}d)"]
    return 0, [f"  ✓ none due — {len(rows)} row(s) scanned, {forward} forward, none inside {PRINT_WINDOW_DAYS}d"]


def _next_quarter_end(d):
    y, m = d.year, d.month + 3
    if m > 12:
        y, m = y + 1, m - 12
    ny, nm = (y, m + 1) if m < 12 else (y + 1, 1)
    return date(ny, nm, 1) - timedelta(days=1)


def perimeter():
    if not PERIMETER.exists():
        return _missing("perimeter", PERIMETER)
    try:
        rows = _rows(PERIMETER)
    except Exception as e:  # noqa: BLE001
        return 2, [f"  🔴 perimeter: read error {type(e).__name__}: {e}"]
    if not rows:
        return 2, ["  🔴 perimeter: 0 firms parsed — an empty perimeter certifies nothing (PAT-155)"]
    asofs = set()
    for r in rows:
        try:
            asofs.add(date.fromisoformat((r.get("As_Of") or "").strip()))
        except ValueError:
            return 2, [f"  🔴 perimeter: unparsable As_Of on {(r.get('Ticker') or '?')} — cannot certify the re-cut clock"]
    out = []
    oldest = min(asofs)
    due_at = _next_quarter_end(oldest) + timedelta(days=RECUT_LAG_DAYS)
    if TODAY >= due_at:
        out.append(f"  ⚠️ RE-CUT DUE: As_Of {oldest} — the next quarter-end + {RECUT_LAG_DAYS}d ({due_at}) has passed; "
                   f"re-cut PERIMETER.tsv (category moves, boundary firms). A re-cut is a registration event → PROME")
    blank = [(r.get("Ticker") or "?").strip() for r in rows if not (r.get("CIK") or "").strip()]
    if blank:
        out.append(f"  ⚠️ CIK UNVERIFIED: {len(blank)} of {len(rows)} firm(s) have no CIK ({' '.join(blank[:6])}{' …' if len(blank) > 6 else ''}) — "
                   f"fill from EDGAR and check each response names the issuer. A PROMPT, not a claim")
    if out:
        return 1, out + [f"  ({len(rows)} firm(s); As_Of {oldest}; re-cut due {due_at})"]
    return 0, [f"  ✓ quiet — {len(rows)} firm(s), every CIK filled; re-cut due {due_at}"]


def main():
    print("=" * 74)
    print(f"  ⏰ WALL CLOCK: {datetime.now().strftime('%Y-%m-%d %H:%M %A')} — never hand-write a time; copy this line")
    if _DRILL:
        print(f"  🧪 DRILL CLOCK: legs 2–4 evaluate as of {TODAY} (GIBBS_BOOT_TODAY) — NOT a real boot")
    print("  GIBBS BOOT — ledger staleness · predictions-due · prints-due · perimeter")
    print("=" * 74)
    rcs = []
    print("\n--- 1. ledger staleness (workbook + TRADE.md) ---")
    sw = run_alert([str(STALENESS), "GIBBS", "--quiet"])
    st = run_alert([str(STALENESS), "GIBBS", "--trade", "--quiet"])
    if sw == st == 0:
        print("  ✓ quiet (alert-contract: this check prints only when stale or misconfigured)")
    rcs.append(2 if 2 in (sw, st) else (1 if 1 in (sw, st) else 0))
    for title, fn in (("2. predictions-due (OPEN rows past Resolve_By)", predictions_due),
                      ("3. prints-due (docket/CATALYSTS.tsv: today · ≤2d · past)", prints_due),
                      ("4. perimeter (re-cut clock · CIK identifiers)", perimeter)):
        print(f"\n--- {title} ---")
        rc, lines = fn()
        print("\n".join(lines))
        rcs.append(rc)
    print("\n" + "=" * 74)
    if 2 in rcs:
        print("  GIBBS boot: a leg FAILED — check manually, do NOT assume quiet.")
        return 2
    if 1 in rcs:
        print("  GIBBS boot: REVIEW — work the flagged items before new research.")
        return 1
    print("  GIBBS boot: all quiet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
