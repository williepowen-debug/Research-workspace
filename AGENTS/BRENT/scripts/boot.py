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
    # Verifies that every registered gate/threshold/falsifier in workbook/REGISTRY.tsv has an
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
    # RE-WIRED 2026-08-17 (Will-approved). Retired from this boot on the explicit condition
    # "do not re-wire without a live unfrozen surface for it to inspect" -- that condition is
    # now MET (REGISTRY.tsv, board_log.tsv, docket/CATALYSTS.tsv and refinery_damage/
    # INCIDENTS.tsv are all live and unfrozen), so this is the retirement clause working as
    # written, not an override of it.
    #
    # WHAT IT BUYS: the two-clock PAT-044 header ("Last real data refresh:") had NO READER on
    # this desk after the retirement. A stamp nothing reads is a comment.
    #
    # ⛔⛔ CORRECTED 2026-08-21 (file audit, Will-directed). This comment previously claimed the
    # wiring was "the measured root cause of TRADE.md:3 carrying an 8/10 stamp over an 8/14 body
    # -- the THIRD instance of that class." THAT WAS FALSE WHEN WRITTEN. workbook/LEDGER_GLOB
    # deliberately scoped to TSV ledgers + board_log (Will-approved at the glob header), so
    # TRADE.md -- markdown -- was NEVER in the scanned set and this wiring never bought it a
    # reader. Measured cost: boot rendered "Ledger Staleness OK" at 09:41 on 8/21 while
    # TRADE.md:3 sat ELEVEN DAYS stale carrying USO $125.92 / Brent $87.85 against a live
    # $134.53 / $94.24.  [[finding_instrument_reports_clean_against_the_wrong_reference]]
    #
    # ★ AND THE REASON IT NEEDED A SEPARATE FIX HERE: the identical false sentence was corrected
    # in AGENTS/BRENT/CLAUDE.md at 11:07 today (commit 108c61b4c) and NOT here, four hours
    # earlier in the same file tree. A correction that lands on the doc and not on the code
    # leaves the code stating the retracted claim to every future reader.
    # [[finding_record_of_an_action_is_not_the_action]]
    #
    # ⚠️ PRECONDITION, and it mattered: the script's DEFAULT glob is workbook/*.tsv, which sees
    # 6 files here and MISSES board_log / CATALYSTS / INCIDENTS -- i.e. all three ledgers that
    # actually rot. Wiring it on the default would have produced a check that reports CLEAN
    # because it is not looking. workbook/LEDGER_GLOB now declares the real set (9 ledgers,
    # verified by running it, not by reading it).
    ("Ledger Staleness",      "scripts/ledger_staleness.py", ["BRENT", "--days", "7"], False),

    # ⚑ ADDED 2026-08-21 (file audit, Will-directed "fix all"). EXTENDS the age check above;
    # supersedes: none. Retirement ratchet satisfied -- this is a second READING of an already
    # wired script, not a second script.
    #
    # THE DEFECT IT FIXES: on 2026-08-21 boot rendered "Ledger Staleness OK" while INCIDENTS.tsv
    # was +7d and REGISTRY.tsv +3d behind STATUS. Both are real; neither surfaced. Cause is that
    # boot invokes the age check with NO --days, so it runs on the script's INHERITED default of
    # 30 -- a number with no BRENT base rate behind it.
    # [[finding_inherited_default_threshold_is_a_silent_decision]]
    #
    # ⛔⛔ SUPERSEDED 2026-09-07 (Will-approved in-session, housekeeping pass). This block used to
    # read "WHY THE FIX IS NOT 'SET --days TO SOMETHING'" and kept the inherited 30. The age row
    # above now passes --days 7. The old text is REPLACED, not annotated beside, because the code
    # now does the thing it said not to do and two live rules is the worse failure.
    # [[finding_correction_beside_an_instruction_leaves_two_live_instructions]]
    #
    # WHY THE 8/21 REASONING NO LONGER HOLDS -- it named its own discharge condition and that
    # condition is met. It deferred on exactly two grounds:
    #   (1) "picking a number without a base rate is the un-base-rated threshold L21/L22 forbid."
    #       ✅ DISCHARGED: the base rate was MEASURED 2026-09-07 before the number was chosen.
    #       Basis: 90d of git history, gap from each STATUS.md write-day back to the most recent
    #       prior write of each glob ledger (a COMMIT-DATE proxy for the content-vintage the
    #       script actually reads -- stated so the basis can be attacked). Pooled n=178 over 6
    #       live ledgers: median 0d, p90 8d, max 17d. Flag rates:
    #           --days  3 -> 26.4% of boot-days    --days 10 ->  5.6%
    #           --days  5 -> 19.1%                 --days 14 ->  3.4%
    #           --days  7 -> 11.2%                 --days 30 ->  0.0%
    #   (2) "per-glob-entry --days is queued into the Staleness #4 ~9/1 manifest design."
    #       ⛔ NOT SHIPPED. Verified 2026-09-07: ledger_staleness.py still exposes only a single
    #       global --days (argparse default=30) and LEDGER_GLOB parses globs only, no directives.
    #       17 days past its own ~9/1 date. A blanket --days on MY invocation is the only lever
    #       this desk owns -- the script is shared fleet code outside AGENTS/BRENT/, same
    #       consumer-side-mapping posture as the FINDINGS_MARKERS rc contract below.
    #
    # ★ THE NUMBER THAT DECIDES IT: --days 30 flags 0/178 boot-days across EVERY ledger over 90
    # days. The inherited default is not "conservative" -- it is provably incapable of firing on
    # this desk's real history. That is a check that certifies clean by construction, which is
    # the silent-fallback-green class this whole file exists to kill.
    #
    # WHY 7 AND NOT 10/14: 7 sits just under the pooled p90 (8d), i.e. it flags the top decile and
    # nothing else. 10 and 14 sit ABOVE p90 and start reproducing the inert problem -- at 14 the
    # only ledger that can still fire is INCIDENTS.tsv; TRADE.md, board_log.tsv and REGISTRY.tsv
    # become unflaggable, which is where the 8/21 defect came from in the first place.
    #
    # ⚠️ KNOWN AND ACCEPTED, not hidden: INCIDENTS.tsv supplies 8 of the 20 flags at --days 7 and
    # is ALSO reported by instrument_check's 60d per-ROW re-verify budget. That is genuine double
    # reporting. It is accepted because the two measure different things -- this is whole-FILE
    # vintage vs STATUS, that is per-row re-verification age -- and suppressing one to quiet the
    # other is [[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]].
    #
    # ⚠️ RE-MEASURE THE BASE RATE BEFORE MOVING THIS NUMBER AGAIN. It is a measured constant with
    # a dated basis, not a preference; if the desk's write cadence changes, 7 rots silently.
    #
    # ✅ WHY --nudge IS THE RIGHT SECOND READER: it is THRESHOLDLESS. It counts STATUS-writes a
    # ledger is behind, so it invents no constant and cannot rot. It already existed and was
    # wired ONLY at closeout -- i.e. it fired where the gap is DISCOVERED, never where a session
    # would still have time to act on it.
    #
    # ⚠️ FALSIFY, DON'T JUST RUN (standing rule): verified 2026-08-21 that the age row alone
    # renders OK on today's tree while --nudge reports "2 ledger(s) behind" -- so this line
    # changes boot's verdict TODAY, on real state, rather than being a no-op that looks prudent.
    ("Ledger Nudge",          "scripts/ledger_staleness.py", ["--nudge", "BRENT"], False),
]


# Output markers that promote an rc=0 run to FINDINGS.
#
# ⛔ ORIGIN (historical as of 2026-08-17 same-day): `scripts/ledger_staleness.py` returned 0
# EVEN WHEN IT FOUND STALE LEDGERS (verified 2026-08-17: --days 1 reported 2 stale, exited 0).
# Wired unmodified it would render ✅ OK whether or not ledgers rot -- the identical
# silent-fallback-green class killed in thresholds.py the same morning. The guard was built
# HERE because the shared script was not BRENT's to edit (flagged to PROME -- correct restraint).
#
# ✅ RESOLVED UPSTREAM 2026-08-17 (DAEDALUS shared-script fix off that flag, PROME-approved):
# the script's exit contract is now 0 clean · 1 stale FINDINGS · 2 CANNOT-CERTIFY
# (MISCONFIGURED / LEDGERS-OUTSIDE-GLOB / usage); FINDINGS_RCS below maps rc to the verdict.
# The marker promotion STAYS as defense-in-depth -- §8 rule 5 keeps marker-present the
# authoritative wrapper channel, and it only ever UPGRADES OK -> FINDINGS.
#
# ✅ CANON, not a local workaround: this is the marker-keyed verdict form of DAEDALUS's
# CHECK_STANDARD §8, RATIFIED by Will 2026-08-17 (verbatim "Ratify §8"; ruling record
# AGENTS/DAEDALUS/inbox/processed/2026-08-17_from-PROME_WILL-RULING-check-standard-s8-RATIFIED.md,
# committed 2efa4f2f0). Verified at that artifact, not adopted on the relay that reported it.
# ⚠️ This comment first read "(Will-gate pending)" and was stale within hours of being written
# — §8 was ratified the same morning. Kept visible as the dated-carry-item class it is: a note
# asserting an OPEN gate is a claim, and reading it never re-evaluates it.
# ⇒ Do NOT unwire this as a BRENT-local hack; the fleet standard now has this shape.
FINDINGS_MARKERS = {
    # ⚑ "behind" added 2026-08-21 for the --nudge reading wired above -- as DEFENSE-IN-DEPTH,
    # not as the load-bearing mechanism.
    #
    # ⛔ SELF-CORRECTION, SAME SESSION, WORTH KEEPING: this comment first asserted that --nudge
    # "exits 0 whether or not it finds ledgers behind", which is why the marker was needed.
    # THEN I RAN IT: --nudge returns rc=1 when ledgers are behind and rc=2 on a bad agent dir --
    # i.e. it already honours the revised 2026-08-17 exit contract, and FINDINGS_RCS below
    # ALREADY maps 1 and 2 to FINDINGS. The marker is redundant with the rc path, not load-bearing.
    # ★ I wrote a mechanism claim from the sibling invocation's known behaviour instead of from
    # this one's, in a comment whose whole subject is "verified by running it, not reading it",
    # during an audit of exactly that class. Kept visible rather than quietly reworded.
    # [[finding_test_the_guard_not_just_the_guarded]] · [[finding_verify_recommended_fix_not_just_finding]]
    #
    # The marker STAYS: it only ever upgrades OK -> FINDINGS, and it keeps the wrapper channel
    # authoritative if the shared script's rc contract is ever revised again (it has been once).
    "scripts/ledger_staleness.py": ("STALE", "MISCONFIGURED", "LEDGERS-OUTSIDE-GLOB", "behind"),
}

# rc values meaning "ran correctly, reported real problems" for scripts whose contract
# differs from the desk convention (0 OK / 2 FINDINGS / else FAIL). ledger_staleness
# (revised 2026-08-17): 1 = stale FINDINGS; 2 = cannot-certify, which the desk
# convention already renders FINDINGS.
FINDINGS_RCS = {
    "scripts/ledger_staleness.py": (1, 2),
}


# Per-script timeout overrides. `eia_weekly.py` legitimately takes ~50-62s against the EIA
# v2 API and was tripping the 60s default -- it showed ❌ FAIL in the boot summary on 8/4
# while exiting 0 with perfectly good data standalone. A wrapper timeout rendered
# identically to a real data outage, which is exactly the camouflage the tri-state status
# below exists to remove. Fixing the label without fixing the timeout would be cosmetic.
TIMEOUTS = {"eia_weekly.py": 150, "instrument_check.py": 120, "thresholds.py": 90}


def run_script(script_path, args, timeout=60, findings_markers=(), findings_rcs=()):
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
        status = "OK" if result.returncode == 0 else (
            "FINDINGS" if (result.returncode == 2 or result.returncode in findings_rcs) else "FAIL")
        # Marker-keyed promotion: a script that reports real problems on rc=0 would otherwise
        # render ✅ OK. Only ever UPGRADES OK -> FINDINGS; it can never downgrade a FAIL, and
        # it can never turn a genuine problem into a clean board. See FINDINGS_MARKERS.
        if status == "OK" and findings_markers:
            hay = (output or "") + (result.stderr or "")
            if any(m in hay for m in findings_markers):
                status = "FINDINGS"
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

        # A name containing "/" is repo-root-relative (shared fleet scripts under scripts/);
        # a bare name is one of BRENT's own in AGENTS/BRENT/scripts/.
        script_path = (WORKSPACE / script_name) if "/" in script_name else (SCRIPTS_DIR / script_name)

        print(f"\n  ⏳ {label}...", flush=True)
        success, output, elapsed = run_script(
            script_path, args,
            timeout=TIMEOUTS.get(script_name, 60),
            findings_markers=FINDINGS_MARKERS.get(script_name, ()),
            findings_rcs=FINDINGS_RCS.get(script_name, ()),
        )

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
