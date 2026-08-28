#!/usr/bin/env python3
"""
LABOR Boot Sequence — Master Orchestrator

Runs LABOR's boot scripts in sequence and prints a consolidated brief, so a
fresh spawn refreshes domain data BEFORE analysis (parity with SAM/BRENT
boot.py). Replaces manual data-refresh + calendar-walk with one command.

Sequence:
  1. labor_data.py        — live FRED sweep (claims, NFP, U-3/6, JOLTS, temp) + threshold flags
  2. spine_check.py       — B2a gate: STATUS `obs` dates vs newest FRED obs (BD-02)
  3. catalyst_countdown.py — docket/CATALYSTS.tsv countdown (imminent ≤5 trd) + PAST-DUE rows
  4. predictions_due.py   — flag OPEN predictions past/near due-by

Smart behavior:
  - Each script's exit code captured; failures reported but don't stop the run
  - Collapsed output by default (alert-worthy lines only); --verbose shows full output
  - Aggregate exit: 2 if any sub-script signalled a RED/overdue condition

Usage:
  .venv/bin/python3 AGENTS/LABOR/scripts/boot.py
  .venv/bin/python3 AGENTS/LABOR/scripts/boot.py --verbose
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
LABOR_DIR = SCRIPTS_DIR.parent
WORKSPACE = LABOR_DIR.parent.parent  # Research-workspace/
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"
PYTHON = str(VENV_PYTHON) if VENV_PYTHON.exists() else sys.executable  # fall back to system python in no-.venv envs

# label, script, args
BOOT_SEQUENCE = [
    ("Domain Data Sweep",  "labor_data.py",         []),
    # B2a immediately after B2, mirroring the documented boot order: the sweep prints
    # what FRED holds, then the gate says whether STATUS knows about it. BD-02, built
    # 2026-08-23 after THREE misses (7/16, 7/31, 8/20) — the 8/20 gap was found by
    # DAEDALUS's external sweep 3 days before LABOR's own boot found it.
    ("Spine Freshness Gate (B2a)", "spine_check.py", []),
    ("Catalyst Countdown", "catalyst_countdown.py", []),
    ("Predictions Due",    "predictions_due.py",    []),
]

# lines worth surfacing in collapsed mode
KEY_MARKERS = (
    "🔴", "🟠", "⚠️", "RED", "OVERDUE", "DUE SOON",
    "IMMINENT", "HIGH PRIORITY", "threshold flag",
    "No RED", "No OPEN", "Report refreshed",
    # SPINE: all THREE states (STALE / FRESH / CANNOT-VERIFY) must survive the
    # collapsed view. A check whose PASS line is filtered out teaches the reader
    # that silence means clean — and silence is also what a filtered-out failure
    # looks like. Found the hard way in catalyst_countdown.py on 2026-08-23, which
    # printed past-due rows only when there were no upcoming ones (i.e. never).
    "SPINE",
)


def run_script(script_path, args, timeout=90):
    if not script_path.exists():
        return None, f"  SKIP: {script_path.name} not found", 0
    start = time.time()
    try:
        result = subprocess.run(
            [PYTHON, str(script_path)] + args,
            capture_output=True, text=True, timeout=timeout, cwd=str(WORKSPACE),
        )
        out = result.stdout
        # CHECK_STANDARD.md §8 (RATIFIED 2026-08-17, Will verbatim) — relay stderr
        # UNCONDITIONALLY. The old guard was `returncode not in (0, 2) and result.stderr`,
        # which deleted stderr on rc==0 AND on this repo's own rc==2 alert convention, so a
        # producer warning emitted at rc 0/2 was unrescuable by KEY_MARKERS downstream.
        # Fixed 2026-08-20 per DAEDALUS packet (donor pattern: WATT/VULCAN/MIDAS/FERT run_alert()).
        if result.stderr:
            out += f"\n  STDERR: {result.stderr[:500]}"
        return result.returncode, out, time.time() - start
    except subprocess.TimeoutExpired:
        return None, f"  TIMEOUT after {time.time()-start:.0f}s", time.time() - start
    except Exception as e:  # noqa: BLE001
        return None, f"  ERROR: {e}", time.time() - start


def main():
    verbose = "--verbose" in sys.argv
    start_time = time.time()
    now = datetime.now()

    print(f"\n{'#'*72}")
    print(f"#{'':^70}#")
    print(f"#{'LABOR BOOT SEQUENCE':^70}#")
    print(f"#{now.strftime('%A, %B %d, %Y  %H:%M'):^70}#")
    print(f"#{'':^70}#")
    print(f"{'#'*72}")

    # --- Live ledger staleness check (frozen ledgers excluded; VX/FLOW are archived) ---
    # KB.tsv REVIVED to LIVE 2026-07-10 (Will-approved) — state (b) per fleet Data Hygiene
    # doctrine requires this boot-time mtime alert so it can't silently rot again (the L-04 trap).
    # KB is event-cadence (logs on major prints/events, ~monthly) → 21d threshold, not 14d.
    LIVE_LEDGERS = [
        (LABOR_DIR / "workbook" / "PREDICTIONS.tsv", 14, "PREDICTIONS.tsv"),
        (LABOR_DIR / "docket" / "CATALYSTS.tsv", 14, "CATALYSTS.tsv"),
        (LABOR_DIR / "workbook" / "KB.tsv", 21, "KB.tsv"),
        # WARN_COHORT.tsv (created 7/10): rolling filing->effective->claims tracker for the
        # WARN->claims framework. Event-cadence (new material filings) → 30d threshold.
        (LABOR_DIR / "docket" / "WARN_COHORT.tsv", 30, "WARN_COHORT.tsv"),
    ]
    # BD-22 DISCHARGED 2026-08-28 (DAEDALUS wiring-sweep flag 16, accepted at the artifact).
    # The mtime leg below was FALSE-NEGATIVE by construction: git sync restamps st_mtime on the
    # receiving box, so after every pull this read every ledger as fresh. Root Data-Hygiene (b)
    # requires a CONTENT-DERIVED vintage; `ledger_staleness.py` implements the correct chain
    # (content-vintage -> git-commit -> mtime last-resort) and prints its basis.
    # `finding_mtime_is_corrupted_by_git_sync` — n+4 on 2026-08-28 (CORAL, CREED, LABOR, OZK).
    # ⚠️ GLOB IS DELIBERATE, do not "simplify" it to the tool default. DAEDALUS prescribed the
    # bare `ledger_staleness.py LABOR --quiet`, whose default perimeter is workbook/*.tsv — that
    # scans 2 of my 4 live ledgers and DROPS docket/CATALYSTS.tsv + docket/WARN_COHORT.tsv, both
    # of which the mtime loop covered. Accepting the fix as written would have narrowed coverage
    # while reporting success (`finding_a_fix_can_relocate_a_constraint_and_report_it_removed`).
    # `**/*.tsv` covers all 7, and correctly reports the two FROZEN ledgers as FROZEN, not stale.
    try:
        rc_ls, out_ls, _ = run_script(
            Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                capture_output=True, text=True, check=True).stdout.strip())
            / "scripts" / "ledger_staleness.py",
            ["LABOR", "--quiet", "--glob", "**/*.tsv"],  # NOT the default workbook/*.tsv — see note
        )
        if out_ls and out_ls.strip():
            print(out_ls.rstrip())
    except Exception as exc:  # fail LOUD, never silently "fresh"
        print(f"  ⚠️  LEDGER STALENESS CANNOT-VERIFY: {exc} — treat ledgers as UNKNOWN, not fresh")

    results = []
    alert = False

    for label, script_name, args in BOOT_SEQUENCE:
        script_path = SCRIPTS_DIR / script_name
        print(f"\n  ⏳ {label}...", flush=True)
        rc, output, elapsed = run_script(script_path, args)

        if verbose:
            if output.strip():
                print(output)
        else:
            shown = False
            for line in output.splitlines():
                if any(m in line for m in KEY_MARKERS):
                    print(f"    {line.strip()}")
                    shown = True
            if not shown:
                print(f"    ✓ ran cleanly")

        # §8 rule 5 — derive the verdict from MARKER-PRESENT alongside rc, not rc alone.
        # A producer can warn on stderr at rc 0/2; keying the summary on rc would report OK.
        stderr_warned = "STDERR:" in output
        if rc == 2:
            alert = True
        if stderr_warned:
            alert = True
        if rc not in (0, 2):
            status = "FAIL"
        elif stderr_warned:
            status = "WARN"
        else:
            status = "OK"
        results.append((label, status, elapsed))

    print(f"\n{'='*72}")
    print(f"  BOOT SUMMARY")
    print(f"{'='*72}")
    print(f"\n  {'Script':<24} {'Status':>8} {'Time':>8}")
    print(f"  {'-'*42}")
    for label, status, elapsed in results:
        icon = "✅" if status == "OK" else "❌"
        print(f"  {icon} {label:<22} {status:>6} {elapsed:>6.1f}s")

    print(f"\n  Total boot time: {time.time()-start_time:.1f}s | {now.strftime('%Y-%m-%d %A')}")
    if alert:
        print(f"\n  🔴 Alert condition(s) flagged above — review before analysis.")
    print(f"\n  Tip: --verbose for full per-script output.\n")

    failures = [r for r in results if r[1] == "FAIL"]
    if failures:
        print(f"  ⚠️  {len(failures)} script(s) failed.\n")
        return 1
    return 2 if alert else 0


if __name__ == "__main__":
    sys.exit(main())
