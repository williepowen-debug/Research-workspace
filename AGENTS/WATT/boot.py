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


def run_rc_and_marker(cmd):
    """Run a script that has REAL rc semantics AND may print alert markers, and
    flag on EITHER. Returns max(rc-verdict, marker-verdict).

    Why this exists (DAEDALUS SFG sweep 2026-08-17, §8 rule 5): power_watch used
    plain run(), so its verdict was rc-ONLY. Its rc contract covers the cases it
    knows to score (emergency-class posting, Orange-band LMP, negative spark,
    fetch failure) — but any ⚠️ it prints for a case OUTSIDE that contract
    (a vintage-mismatch refusal, a cache-provenance caveat, a future warning
    added by a later edit) rendered at rc 0 and did NOT flip the boot verdict.
    That is the silent-fallback-green class: a warning that prints green.

    Unlike run_alert(), rc is NOT ignored here — power_watch's rc is meaningful
    and authoritative for what it scores. This is strictly ADDITIVE: it can only
    escalate a verdict, never suppress one. Output is captured and re-printed so
    the marker test can see it; ordering is preserved (stdout then stderr).
    """
    try:
        p = subprocess.run([PYTHON, *cmd], cwd=str(ROOT),
                           capture_output=True, text=True)
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2
    out = (p.stdout or "").rstrip()
    err = (p.stderr or "").rstrip()
    if out:
        print(out)
    if err:
        print(err, file=sys.stderr)
    rc = p.returncode if p.returncode in (0, 1, 2) else 2
    # markers on EITHER stream — power_watch prints its fetch failures to stderr
    marker = 1 if any(m in s for s in (out, err) for m in ("⚠️", "🔴")) else 0
    if marker and rc == 0:
        print("  boot.py: power_watch printed an alert MARKER at rc 0 "
              "— escalating to REVIEW (SFG guard, 2026-08-17).")
    return max(rc, marker)


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


# --- STATUS byte budget (fleet BYTE TIER convention, Will-ratified 2026-08-17) -----
# The line cap alone measures the one dimension that stops moving (PAT-086). Every
# STATUS cap carries a byte budget beside it; at >=75% the owner rotates the oldest
# history blocks VERBATIM into a dated archive until <70%. Rotation, never deletion.
#
# WATT's budget is 64,000 B — NOT the ~128 B/line x 250 = 32,000 default — set from
# measurement, per the convention's "owner sets it" clause:
#   measured 2026-08-17: STATUS = 105 lines / 41,190 bytes = 392 B/line.
# That is 3.1x the 128 B/line the default assumes. On the default budget this file
# would sit at 129% while using only 42% of its LINE cap, forcing rotation of LIVE
# state on day one — the opposite of the convention's intent. 64,000 B = 256 B/line
# across the 250-line cap, still BINDING WELL BEFORE the line cap (~163 lines at
# measured density), which is correct: for a dense file the byte budget should bind
# first. Trigger 48,000 · rotate to <44,800.
STATUS_BYTE_BUDGET = 64_000
STATUS_ARCHIVE_DIR = HERE / "status_archive"


def status_byte_budget():
    """Byte-tier check on STATUS.md. Returns 0 quiet / 1 rotate-now / 2 unreadable.
    ADVISORY BY DESIGN: it prints a marker and asks for a rotation decision; it never
    rotates anything itself. Choosing WHAT is superseded is a judgment call, and an
    auto-rotator would eventually move live state to hit a number — the exact
    corruption the two-state pilot spec warns about."""
    p = HERE / "STATUS.md"
    try:
        b = p.stat().st_size
        lines = sum(1 for _ in p.open())
    except Exception as e:  # noqa: BLE001
        print(f"  STATUS byte budget: UNREADABLE ({e})", file=sys.stderr)
        return 2
    pct = b / STATUS_BYTE_BUDGET * 100
    dens = b / lines if lines else 0
    if pct >= 75.0:
        target = int(STATUS_BYTE_BUDGET * 0.70)
        print(f"  \u26a0\ufe0f STATUS {b:,} B = {pct:.0f}% of the {STATUS_BYTE_BUDGET:,} B budget "
              f"({lines} lines, {dens:.0f} B/line) — ROTATE oldest history blocks "
              f"verbatim into {STATUS_ARCHIVE_DIR.name}/ until < {target:,} B. "
              f"Rotation, never deletion; never trim live state to hit the number.")
        return 1
    print(f"  \u2713 STATUS {b:,} B = {pct:.0f}% of {STATUS_BYTE_BUDGET:,} B budget "
          f"({lines} lines = {lines/250*100:.0f}% of the 250-line cap, {dens:.0f} B/line)")
    return 0


def main():
    print("=" * 72)
    print("  WATT BOOT — power_watch · ledger staleness · predictions-due")
    print("=" * 72)
    rcs = []

    print("\n--- 1. power_watch (P1 stress->price live read) ---")
    # rc AND marker (was rc-only until 2026-08-17). power_watch's rc scores the
    # cases it knows about; the marker test catches anything it warns about
    # outside that contract. DAEDALUS SFG sweep §8 rule 5.
    rcs.append(("power_watch", run_rc_and_marker([str(POWER_WATCH)])))

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

    print("\n--- 3. STATUS byte budget (byte-tier convention) ---")
    rcs.append(("status_bytes", status_byte_budget()))

    print("\n--- 4. predictions-due scan ---")
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
