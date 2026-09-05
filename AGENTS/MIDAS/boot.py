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
  3. COT vintage freshness — is CFTC serving a gold COT vintage this desk has not
     consumed? (wired 2026-09-05, closing DAEDALUS F-2.)

⛔ WHY ONLY ONE OF THE FOUR COT/SETTLE TOOLS IS WIRED, stated here so the next
reader does not "fix" the other three in (DAEDALUS F-2, 2026-09-05 — three
graders shipped and boot called none of them):

  WIRED — cot_gold.py. It is a PULLER with a STANDING WEEKLY CADENCE, and STATUS
    carries a live COT net/OI figure that silently rots between releases. That is
    exactly the shape a boot check is for, and the gap was live on 2026-09-05:
    STATUS said 56.86% [as-of 8/25] while the 9/1 vintage had been public since
    Fri 9/4 15:30 ET, with nothing on this desk saying so. Imported as a MODULE
    (extract_gold(fetch())) — not shelled out and stdout-parsed — so the code-keyed
    extraction and the totals reconciliation are the SAME code path the grades use,
    and cot_gold.py itself is unmodified. stdlib only, so leg 3 does not need .venv.

  NOT WIRED — grade_cot3.py, grade_midas07.py, settle_check.py. Each is a ONE-SHOT
    instrument bound to a question that is CLOSED: grade_cot3.py pre-registers a
    boundary for the 2026-08-25 vintage (graded 8/28), grade_midas07.py transcribes
    MIDAS-07's frozen branches (graded 8/14, INDETERMINATE), settle_check.py labels a
    13:30 ET COMEX settle window with PGM betas hardcoded from a consumed report.
    Running any of them every boot would RE-GRADE a consumed letter on new data —
    which is not a freshness check, it is re-opening a frozen question with a script.
    ⇒ Their correct cadence is ON DEMAND, at the moment their question is live, and
    the boot leg that matters is the one that TELLS YOU the moment has arrived. That
    is leg 3. A tool being unwired is not automatically a defect; a tool whose
    triggering moment nothing announces is.

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
COT_VINTAGES = HERE / "sources" / "cot_vintages_consumed.tsv"

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



def cot_vintage_leg():
    """Leg 3 — is CFTC serving a gold COT vintage this desk has NOT consumed?

    Returns (rc, lines). rc 0 quiet · 1 REVIEW (new vintage unconsumed) · 2
    cannot-certify (ledger missing/unreadable, pull or reconciliation failed, or
    the source serving OLDER than the ledger).

    ⛔ NO RELEASE-CALENDAR ARITHMETIC. The leg asks the SOURCE what the newest
    vintage is and compares it to what this desk has written down. A computed
    "expected Tuesday" would have to model holiday-shifted releases (Labor Day
    2026-09-07 is the next one) and would fail in whichever direction the model
    was wrong — silently all-clear being the dangerous one.

    ⛔ CANNOT-CERTIFY IS rc 2, DELIBERATELY, matching run_alert's contract
    ("enforcement silently absent = never assume quiet"). On an offline box leg 0
    already fails, so this adds no new false-alarm channel: an offline boot SHOULD
    be loud. It is NOT downgraded to keep laptop boots green — that is
    finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction.
    """
    out = []
    if not COT_VINTAGES.exists():
        return 2, [f"  🔴 CANNOT CERTIFY — consumed-vintage ledger missing: {COT_VINTAGES}"]
    try:
        rows = []
        with COT_VINTAGES.open(encoding="utf-8") as f:
            for line in f:
                if line.startswith("#") or not line.strip():
                    continue
                parts = line.rstrip("\n").split("\t")
                if parts[0] == "report_date":
                    continue
                rows.append(parts)
        if not rows:
            return 2, ["  🔴 CANNOT CERTIFY — consumed-vintage ledger has no rows"]
        last = max(rows, key=lambda r: r[0])
        last_date, last_ratio = last[0], float(last[5])
    except Exception as e:  # noqa: BLE001
        return 2, [f"  🔴 CANNOT CERTIFY — consumed-vintage ledger unreadable: {e}"]

    try:
        sys.path.insert(0, str(HERE))
        import cot_gold  # stdlib-only; same extraction + reconciliation as the graders
        d = cot_gold.extract_gold(cot_gold.fetch())
    except Exception as e:  # noqa: BLE001
        return 2, [f"  🔴 CANNOT CERTIFY — CFTC pull/parse/reconcile failed: {e}"]

    live_date, live_ratio = d["report_date"], d["net_over_oi"]
    out.append(f"  last consumed: {last_date}  net/OI {last_ratio:.4f}%  "
               f"[{COT_VINTAGES.name}]")
    out.append(f"  live at CFTC : {live_date}  net/OI {live_ratio:.4f}%  "
               f"(code 088691, reconciled)")
    if live_date < last_date:
        out.append("  🔴 SOURCE IS OLDER THAN THE LEDGER — a stale file served as a clean 200 "
                   "(finding_partitioned_source_returns_stale_window_at_200). Do NOT grade it.")
        return 2, out
    if live_date == last_date:
        out.append("  ✓ current vintage already consumed")
        return 0, out
    out.append(f"  ⚠️  NEW COT VINTAGE UNCONSUMED — {live_date} is public and this desk has not "
               f"read it. Δ net/OI vs last consumed: {live_ratio - last_ratio:+.4f}pp")
    out.append(f"      grade it:  python3 AGENTS/MIDAS/cot_gold.py --expect {live_date}")
    out.append(f"      then append a row to sources/{COT_VINTAGES.name} — the row is what "
               "clears this flag, and it means READ, not merely published.")
    return 1, out


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

    print("\n--- 3. COT vintage freshness (CFTC gold, code 088691) ---")
    cot_rc, cot_lines = cot_vintage_leg()
    for line in cot_lines:
        print(line)
    legs.append(("COT vintage", cot_rc))

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
