#!/usr/bin/env python3
"""
SAM Boot Sequence — Master Orchestrator

Runs all SAM monitoring scripts in sequence and prints a consolidated boot
brief. Replaces the multi-step manual refresh in CLAUDE.md boot step 7 with
a single command.

Smart behavior:
  - Scripts are run in order of priority (threshold breaches first).
  - Each script's exit code is captured; failures are reported in the summary
    but do not stop the boot sequence.
  - FXY options runs weekly (skipped if FXY_OPTIONS.tsv already has today's date).
  - JGB auctions auto-probe the last few business days for recent results.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/boot.py
  .venv/bin/python3 AGENTS/SAM/scripts/boot.py --quick    # skip options + auction lookback
  .venv/bin/python3 AGENTS/SAM/scripts/boot.py --verbose  # don't collapse script output
"""

import subprocess
import re
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
SAM_DIR = SCRIPTS_DIR.parent
WORKSPACE = SAM_DIR.parent.parent  # Research-workspace/
WORKBOOK = SAM_DIR / "workbook"
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"

FXY_OPTIONS_TSV = WORKBOOK / "FXY_OPTIONS.tsv"


def _has_today_row(tsv_path):
    """Check if a TSV has a row for today's date in the first column."""
    if not tsv_path.exists():
        return False
    today = datetime.now().strftime("%Y-%m-%d")
    with open(tsv_path) as f:
        next(f, None)
        for line in f:
            parts = line.strip().split("\t")
            if parts and parts[0] == today:
                return True
    return False


# Boot sequence: (label, script_name, args, section_header, slow)
BOOT_SEQUENCE = [
    ("Market / Threshold Monitor", "thresholds.py",        [], "THRESHOLDS",   False),
    ("USDJPY History",             "usdjpy.py",            [], "USDJPY",       False),
    ("JGB Yields",                 "jgb_yields.py",        [], "JGB YIELDS",   False),
    ("JGB Auctions",               "jgb_auctions.py",      [], "JGB AUCTIONS", False),
    ("BOJ OIS (hike pricing)",     "boj_ois.py",           [], "BOJ OIS",      False),
    ("CFTC JPY Positioning",       "cftc_jpy.py",          [], "CFTC",         False),
    ("Rate Differential (SAM-41)", "rate_differential.py", [], "SAM-41",       False),
    ("MOF Weekly Flows",           "mof_flows.py",         [], "MOF FLOWS",    False),
    ("JPY xccy basis PROXY",       "xccy_basis.py",        [], "XCCY BASIS",   False),
    ("GPIF Portfolio / Flows",     "gpif_flows.py",        [], "GPIF",         False),
    ("Japan Trade Balance",        "trade_balance_japan.py", ["--boot"], "TRADE BALANCE", False),
    ("Japan CPI",                  "cpi_japan.py",         [], "CPI",          False),
    ("Catalyst Countdown",         "catalyst_countdown.py", [], "CATALYSTS",    False),
    ("FXY Options OI",             "fxy_options.py",       [], "FXY OPTIONS",  True),  # weekly
]


def run_script(name, script_path, args, timeout=60):
    """Run a script and capture output. Returns (success, output, elapsed_seconds)."""
    if not script_path.exists():
        return False, f"  SKIP: {script_path.name} not found", 0

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
        return result.returncode == 0, output, elapsed
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        return False, f"  TIMEOUT after {elapsed:.0f}s", elapsed
    except Exception as e:
        elapsed = time.time() - start
        return False, f"  ERROR: {e}", elapsed


# ---------------------------------------------------------------------------
# TOOL INVENTORY — generated from disk, never hand-maintained.
#
# WHY GENERATED (Will-directed 2026-08-04): a future SAM boot must be able to see what
# tooling EXISTS without reading the source or trusting a hand-written list. A static
# inventory in CLAUDE.md rots the moment someone adds a script — and the failure is
# SILENT: an unwired script never runs, never prints, and a later session rebuilds it
# or does its job by hand. (SAM did exactly that on 8/4, sourcing BOJ OIS pricing by
# ad-hoc web search.) So the list is derived from the scripts directory at run time and
# cross-checked against BOOT_SEQUENCE; the check cannot go stale because there is
# nothing to keep up to date.
# ---------------------------------------------------------------------------

def _one_line_purpose(path):
    """One-line purpose from the module docstring.

    Scripts here open with a title line ("SAM JGB Yield Monitor") that is sometimes the
    whole purpose and sometimes just a name. Rules, in order:
      1. title carries a separator ("SAM BOJ OIS Monitor - market-implied ...") -> take
         the part after it;
      2. otherwise take the next non-empty line (the usual "Fetches ..." summary);
      3. otherwise fall back to the title itself.
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "(unreadable)"
    m = re.search(r'"""(.*?)"""', text, re.S)
    if not m:
        return "(no docstring)"
    lines = [ln.strip() for ln in m.group(1).strip().split("\n")]
    lines = [ln for ln in lines if ln]
    if not lines:
        return "(empty docstring)"
    title = lines[0]
    for sep in ("\u2014", " - ", ": "):          # em dash, hyphen, colon
        if sep in title:
            tail = title.split(sep, 1)[1].strip()
            if tail:
                return tail[:78]
    if len(lines) > 1:
        return lines[1][:78]
    return title[:78]


def documented_manual():
    """Scripts CLAUDE.md declares deliberately manual-only, read from CLAUDE.md itself.

    Why parse the doc instead of hard-coding a list here: the drift check's whole value
    is that it has nothing to keep up to date. A second hand-maintained allowlist in this
    file would rot exactly like the inventory this function exists to replace — and it
    would rot SILENTLY, re-creating the defect one layer down. CLAUDE.md's MANUAL-ONLY row
    is already the record of record (the gate's own remedy text points there), so the
    allowlist IS that row. Delete a script from the row and the gate goes loud again.

    Fails OPEN (returns empty) if CLAUDE.md is unreadable or the row is absent: an
    unreadable doc must not silence a real drift warning.
    """
    doc = SCRIPTS_DIR.parent / "CLAUDE.md"
    try:
        text = doc.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return set()
    names = set()
    for line in text.split("\n"):
        if "MANUAL-ONLY" not in line:
            continue
        names.update(re.findall(r"`([A-Za-z0-9_]+\.py)`", line))
    return names


def tool_inventory():
    """Return (rows, orphans, missing, manual).
    rows    = [(script_name, wired?, purpose)] for everything on disk
    orphans = on disk, NOT wired, and NOT documented manual -> REAL drift, gate fires
    missing = in BOOT_SEQUENCE but NOT on disk  -> boot references a ghost
    manual  = on disk, not wired, but CLAUDE.md says why -> known-good, reported quietly

    The orphans/manual split is the fix for a DEAD GATE (DAEDALUS 8/17 item 6, PAT-074):
    this check fired 🔴 on the same 4 known-good scripts every single run, and a flag that
    fires every run for a known-good reason trains the reader to skip it — which is exactly
    what happened to grade_8_14_branch.py, flagged for days while SAM read past it. A gate
    that cannot go green cannot be trusted when it goes red.
    """
    wired = {name for _, name, _, _, _ in BOOT_SEQUENCE}
    declared = documented_manual()
    on_disk = sorted(p.name for p in SCRIPTS_DIR.glob("*.py") if p.name != "boot.py")
    rows = [(n, n in wired, _one_line_purpose(SCRIPTS_DIR / n)) for n in on_disk]
    unwired = [n for n in on_disk if n not in wired]
    manual = [n for n in unwired if n in declared]
    orphans = [n for n in unwired if n not in declared]
    missing = sorted(wired - set(on_disk))
    return rows, orphans, missing, manual


def print_tool_inventory(full=True):
    """Full table on demand; drift warnings ALWAYS (they are silent when clean)."""
    rows, orphans, missing, manual = tool_inventory()
    if full:
        print(f"\n{'='*72}")
        print("  SAM TOOL INVENTORY  (generated from scripts/ — not a maintained list)")
        print(f"{'='*72}\n")
        print(f"  {'Script':<26}{'Boot':<7}Purpose")
        print(f"  {'-'*68}")
        for name, is_wired, purpose in rows:
            flag = "✓" if is_wired else ("M" if name in manual else "—")
            print(f"  {name:<26}{flag:<7}{purpose}")
        print(f"\n  {len(rows)} tool(s); {sum(1 for r in rows if r[1])} boot-wired"
              f"{f'; {len(manual)} manual-only by design (M)' if manual else ''}.")
        print("  Run any of them directly: .venv/bin/python3 AGENTS/SAM/scripts/<name>")
        if manual:
            print(f"\n  ℹ️  {len(manual)} manual-only BY DESIGN, per CLAUDE.md — not drift:")
            for n in manual:
                print(f"       {n}")
            print( "     (allowlist is parsed from CLAUDE.md's MANUAL-ONLY row, so removing")
            print( "      a script from that row makes this gate go loud again.)")
    if orphans:
        print(f"\n  🔴 {len(orphans)} SCRIPT(S) ON DISK BUT NOT BOOT-WIRED — boot never runs")
        print( "     these, so a future session will not know they exist:")
        for n in orphans:
            print(f"       {n}")
        print( "     → add to BOOT_SEQUENCE, or record in CLAUDE.md why it is manual-only.")
    if missing:
        print(f"\n  🔴 {len(missing)} SCRIPT(S) IN BOOT_SEQUENCE BUT NOT ON DISK:")
        for n in missing:
            print(f"       {n}")
    return orphans, missing


def main():
    quick = "--quick" in sys.argv
    verbose = "--verbose" in sys.argv

    # Inventory-only mode: what tooling exists, no network, no writes.
    if "--tools" in sys.argv:
        orphans, missing = print_tool_inventory(full=True)
        print()
        return 1 if (orphans or missing) else 0

    start_time = time.time()
    now = datetime.now()

    print(f"\n{'#'*72}")
    print(f"#{'':^70}#")
    print(f"#{'SAM BOOT SEQUENCE':^70}#")
    print(f"#{'':^70}#")
    print(f"#  {now.strftime('%A, %B %d, %Y  %H:%M %Z'):^66}#")
    print(f"#{'':^70}#")
    print(f"{'#'*72}")

    results = []

    for label, script_name, args, section_header, is_slow in BOOT_SEQUENCE:
        # Smart skip: FXY options only if TSV doesn't already have today's data
        if script_name == "fxy_options.py":
            if _has_today_row(FXY_OPTIONS_TSV):
                print(f"\n  ⏩ Skipping {label} — TSV already has today's snapshot")
                results.append((label, "SKIP", 0))
                continue
            if quick:
                print(f"\n  ⏩ Skipping {label} (--quick)")
                results.append((label, "SKIP", 0))
                continue

        script_path = SCRIPTS_DIR / script_name

        print(f"\n  ⏳ {label}...", flush=True)
        success, output, elapsed = run_script(label, script_path, args)

        if verbose or not output:
            if output.strip():
                print(output)
        else:
            # Collapse: show only lines that contain key markers
            key_markers = (
                "🔴", "🟠", "🟡", "🟢", "⚠️",
                "BREACH", "CRISIS", "STRESS", "ELEVATED",
                "ALERT", "SHORT BUILD", "SHORT COVER",
                "BUYER STRIKE", "Quality problem",
                "IMMINENT", "HIGH PRIORITY",
                "Latest", "LATEST", "NEW:",
                "VOL PROXY", "ATM IV", "25d RR",  # surface the FXY vol read
                "🎯", "IN-WINDOW", "unpriced", "Data as of",  # surface the BOJ OIS read
            )
            lines = output.splitlines()
            shown = False
            # Always show the script's own section header line for context
            for line in lines:
                if any(marker in line for marker in key_markers):
                    print(f"    {line}")
                    shown = True
            if not shown:
                # Show a 1-line "ok" result
                print(f"    ✓ ran cleanly, no alerts")

        status = "OK" if success else "FAIL"
        results.append((label, status, elapsed))

    # Summary
    total_time = time.time() - start_time
    print(f"\n{'='*72}")
    print(f"  BOOT SUMMARY")
    print(f"{'='*72}")
    print(f"\n  {'Script':<30} {'Status':>8} {'Time':>8}")
    print(f"  {'-'*50}")
    for label, status, elapsed in results:
        icon = "✅" if status == "OK" else "⏩" if status == "SKIP" else "❌"
        print(f"  {icon} {label:<28} {status:>6} {elapsed:>6.1f}s")

    print(f"\n  Total boot time: {total_time:.1f}s")
    print(f"  Date: {now.strftime('%Y-%m-%d')} | Day: {now.strftime('%A')}")

    # Tooling visibility: one always-on line so a future boot knows the full toolset
    # exists and how to list it, plus loud drift warnings (silent when clean).
    inv_rows, _, _, inv_manual = tool_inventory()
    print(f"  Tools: {len(inv_rows)} in scripts/ "
          f"({sum(1 for r in inv_rows if r[1])} boot-wired"
          f"{f', {len(inv_manual)} manual-only by design' if inv_manual else ''}) — "
          f"full list: boot.py --tools")
    print_tool_inventory(full=False)

    failures = [r for r in results if r[1] == "FAIL"]
    if failures:
        print(f"\n  ⚠️  {len(failures)} script(s) failed — check output above (try --verbose).")
        return 1
    else:
        print(f"\n  ✅ All scripts completed successfully.")
        print(f"\n  Tip: run with --verbose to see full output for each script.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
