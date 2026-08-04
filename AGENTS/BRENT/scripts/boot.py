#!/usr/bin/env python3
"""
BRENT Boot Sequence — Master Orchestrator

Runs all BRENT monitoring scripts in sequence and prints a consolidated boot
brief. Replaces manual web-search refresh with a single command.

Smart behavior:
  - Scripts run in order of priority (threshold breaches first)
  - Each script's exit code captured; failures reported but don't stop sequence
  - Collapsed output by default; --verbose shows full script output

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/boot.py
  .venv/bin/python3 AGENTS/BRENT/scripts/boot.py --quick    # skip slow
  .venv/bin/python3 AGENTS/BRENT/scripts/boot.py --verbose  # full output
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
BRENT_DIR = SCRIPTS_DIR.parent
WORKSPACE = BRENT_DIR.parent.parent  # Research-workspace/
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"


# Boot sequence: (label, script_name, args, slow)
BOOT_SEQUENCE = [
    ("Threshold Monitor",    "thresholds.py",         [], False),
    ("EIA Weekly Monitor",   "eia_weekly.py",         [], False),
    ("Catalyst Countdown",   "catalyst_countdown.py", [], False),
    ("Predictions-Due Scan", "predictions_due.py",    [], False),
    # Wired 2026-07-30 (Will-directed). Reports UNRESOLVED contradictions between BRENT's own
    # LESSONS. Lives IN boot, not in a CLAUDE.md instruction, because a documented command is
    # still a remembered ritual -- and the whole defect class this fixes came from lessons
    # nobody re-read before drafting a spec. See finding_mechanize_the_cap_not_the_ritual.
    ("Lesson-Conflict Check", "lessons_check.py",      [], False),
    # Wired 2026-08-04, the session DEPLOY GATE v2 turned out to be UNFILLABLE BY CONSTRUCTION.
    # Verifies that every registered gate/threshold/falsifier in workbook/INSTRUMENTS.tsv has an
    # instrument that (1) exists, (2) is reachable, (3) is fresh enough for its own staleness
    # budget, and (4) still PRINTS while the market it must be acted on in is open.
    #
    # (4) is invisible to every other check in this kit and is what cost a ratified gate: ^OVX
    # prints to 16:00 and USO options close 16:00, so leg (a) became knowable at exactly the
    # moment leg (b) became ungradeable. Five days ratified, undetected, and my own 8/2 premise
    # audit cleared the gate without ever asking whether it could be EXECUTED.
    #
    # In boot rather than in a CLAUDE.md line for the same reason as the lesson check above:
    # a documented command is a remembered ritual (finding_mechanize_the_cap_not_the_ritual),
    # and this whole defect class survives precisely because nobody re-probes a spec they wrote.
    ("Instrument Check",      "instrument_check.py",   [], False),
]


# Per-script timeout overrides. `eia_weekly.py` legitimately takes ~50-62s against the EIA
# v2 API and was tripping the 60s default -- it showed ❌ FAIL in the boot summary on 8/4
# while exiting 0 with perfectly good data standalone. A wrapper timeout rendered
# identically to a real data outage, which is exactly the camouflage the tri-state status
# below exists to remove. Fixing the label without fixing the timeout would be cosmetic.
TIMEOUTS = {"eia_weekly.py": 150, "instrument_check.py": 120, "thresholds.py": 90}


def run_script(script_path, args, timeout=60):
    """Run a script and capture output.

    Returns (status, output, elapsed) where status is one of:
      "OK"       — exit 0
      "FINDINGS" — exit 2: the script RAN CORRECTLY and reported real problems
      "FAIL"     — any other non-zero, a timeout, or a crash: the SCRIPT is broken

    ⚠️ FINDINGS and FAIL must never be collapsed. A check whose findings look identical
    to its own failure is a check that gets ignored -- and then a genuine breakage hides
    inside the noise of "that one always says FAIL".
    """
    if not script_path.exists():
        return "FAIL", f"  SKIP: {script_path.name} not found", 0

    start = time.time()
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), str(script_path)] + args,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(WORKSPACE),
        )
        elapsed = time.time() - start
        output = result.stdout
        if result.returncode != 0 and result.stderr:
            output += f"\n  STDERR: {result.stderr[:500]}"
        status = "OK" if result.returncode == 0 else ("FINDINGS" if result.returncode == 2 else "FAIL")
        return status, output, elapsed
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        return "FAIL", f"  TIMEOUT after {elapsed:.0f}s", elapsed
    except Exception as e:
        elapsed = time.time() - start
        return "FAIL", f"  ERROR: {e}", elapsed


def main():
    quick = "--quick" in sys.argv
    verbose = "--verbose" in sys.argv

    start_time = time.time()
    now = datetime.now()

    print(f"\n{'#'*72}")
    print(f"#{'':^70}#")
    print(f"#{'BRENT BOOT SEQUENCE':^70}#")
    print(f"#{'':^70}#")
    print(f"#  {now.strftime('%A, %B %d, %Y  %H:%M'):^66}#")
    print(f"#{'':^70}#")
    print(f"{'#'*72}")

    results = []

    for label, script_name, args, is_slow in BOOT_SEQUENCE:
        if is_slow and quick:
            print(f"\n  ⏩ Skipping {label} (--quick)")
            results.append((label, "SKIP", 0))
            continue

        script_path = SCRIPTS_DIR / script_name

        print(f"\n  ⏳ {label}...", flush=True)
        success, output, elapsed = run_script(script_path, args, timeout=TIMEOUTS.get(script_name, 60))

        if verbose:
            if output.strip():
                print(output)
        else:
            # Collapsed: show only alert-worthy lines
            key_markers = (
                "🔴", "🟠", "⚠️",
                "BREACHED", "BREACH", "CRISIS", "STRESS",
                "IMMINENT", "HIGH PRIORITY",
                "FIRED", "TRIGGER",
                "Source:", "Week ending", "Released",
                "Cushing:", "Gas demand YoY", "Refinery util",
                "Commercial crude",
                "CRUDE & FUTURES", "POSITIONS", "Brent futures", "WTI futures",
                "THESIS CONFIRMING",
            )
            lines = output.splitlines()
            shown = False
            for line in lines:
                if any(marker in line for marker in key_markers):
                    print(f"    {line}")
                    shown = True
            if not shown:
                print(f"    ✓ ran cleanly, no alerts")

        status = success  # run_script now returns the tri-state directly
        results.append((label, status, elapsed))

    # Summary
    total_time = time.time() - start_time
    print(f"\n{'='*72}")
    print(f"  BOOT SUMMARY")
    print(f"{'='*72}")
    print(f"\n  {'Script':<30} {'Status':>8} {'Time':>8}")
    print(f"  {'-'*50}")
    for label, status, elapsed in results:
        icon = {"OK": "✅", "FINDINGS": "🔴", "SKIP": "⏩"}.get(status, "❌")
        print(f"  {icon} {label:<28} {status:>6} {elapsed:>6.1f}s")

    print(f"\n  Total boot time: {total_time:.1f}s")
    print(f"  Date: {now.strftime('%Y-%m-%d')} | Day: {now.strftime('%A')}")

    findings = [r for r in results if r[1] == "FINDINGS"]
    failures = [r for r in results if r[1] == "FAIL"]
    if findings:
        print(f"\n  🔴 {len(findings)} check(s) reported BLOCKING FINDINGS (script ran fine — the SPEC is the problem):")
        for label, _, _ in findings:
            print(f"     • {label}")
    if failures:
        print(f"\n  ⚠️  {len(failures)} script(s) failed — check output (try --verbose).")
        return 1
    else:
        # "All scripts completed successfully" is TRUE about the scripts and MISLEADING
        # about the state of the world when a check just reported blocking findings.
        if findings:
            print(f"\n  ✅ All scripts RAN successfully — but see the blocking findings above.")
        else:
            print(f"\n  ✅ All scripts completed successfully.")
        print(f"\n  Tip: run with --verbose to see full output for each script.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
