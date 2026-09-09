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
  - FXY options checked daily (skipped if today has all four expiry rows).
  - JGB auctions auto-probe the last few business days for recent results.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/boot.py
  .venv/bin/python3 AGENTS/SAM/scripts/boot.py --quick    # skip options only
  .venv/bin/python3 AGENTS/SAM/scripts/boot.py --verbose  # don't collapse script output
"""

import argparse
import csv
import json
import uuid
import subprocess
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Explicit context modes must not create __pycache__ during their local import.
sys.dont_write_bytecode = True

SCRIPTS_DIR = Path(__file__).resolve().parent
SAM_DIR = SCRIPTS_DIR.parent
WORKSPACE = SAM_DIR.parent.parent  # Research-workspace/
WORKBOOK = SAM_DIR / "workbook"
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"

FXY_OPTIONS_TSV = WORKBOOK / "FXY_OPTIONS.tsv"


def _has_today_row(tsv_path):
    """Four unique future expiries are required; a partial snapshot cannot skip."""
    if not tsv_path.exists():
        return False
    today = datetime.now().strftime('%Y-%m-%d')
    try:
        with tsv_path.open() as f:
            reader = csv.DictReader(f, delimiter='\t')
            if not {'Date', 'Expiry'}.issubset(reader.fieldnames or []):
                return False
            expiries = {datetime.strptime(r['Expiry'], '%Y-%m-%d').date().isoformat()
                        for r in reader if r['Date'] == today and r['Expiry'] >= today}
        return len(expiries) >= 4
    except (OSError, csv.Error, KeyError, TypeError, ValueError):
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
    """Preserve both output streams, exit code and partial timeout output."""
    start = time.monotonic()
    result = dict(label=name, script=script_path.name, exit_code=None, stdout='', stderr='',
                  elapsed=0.0, success=False, reason='')
    if not script_path.exists():
        result['reason'] = f'Missing script: {script_path}'
        return result
    try:
        child = subprocess.run([str(VENV_PYTHON), str(script_path)] + args,
                               capture_output=True, text=True, timeout=timeout, cwd=str(WORKSPACE))
        result.update(exit_code=child.returncode, stdout=child.stdout, stderr=child.stderr,
                      success=child.returncode == 0,
                      reason='' if child.returncode == 0 else f'Child exited {child.returncode}')
    except subprocess.TimeoutExpired as exc:
        def decoded(value):
            return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else value or ''
        result.update(stdout=decoded(exc.stdout), stderr=decoded(exc.stderr), reason=f'Timeout after {timeout}s')
    except OSError as exc:
        result['reason'] = str(exc)
    result['elapsed'] = time.monotonic()-start
    return result


# Helpers imported/executed directly by the orchestrator are also boot wiring.
CONTEXT_MODULE = SCRIPTS_DIR / 'lib/boot_context.py'
LEDGERS = {
    'usdjpy.py': 'USDJPY.tsv', 'jgb_yields.py': 'JGB_YIELDS.tsv',
    'jgb_auctions.py': 'JGB_AUCTIONS.tsv', 'boj_ois.py': 'BOJ_MEETING_OIS.tsv',
    'cftc_jpy.py': 'CFTC_JPY.tsv', 'rate_differential.py': 'RATE_DIFFERENTIAL.tsv',
    'mof_flows.py': 'MOF_FLOWS.tsv', 'xccy_basis.py': 'XCCY_BASIS.tsv',
    'gpif_flows.py': 'GPIF_FLOWS.tsv', 'trade_balance_japan.py': 'TRADE_BALANCE.tsv',
    'cpi_japan.py': 'CPI.tsv', 'fxy_options.py': 'FXY_OPTIONS.tsv',
}


def stored_vintage(script):
    name = LEDGERS.get(script)
    if not name:
        return 'Freshness unverified here; consult explicit source clocks in child output.'
    try:
        with (WORKBOOK/name).open() as f:
            reader = csv.DictReader(f, delimiter='\t')
            column = next((c for c in ('quote_as_of', 'Date', 'date') if c in (reader.fieldnames or [])), None)
            if column is None:
                return f'{name}: no recognized observation-date column; freshness unverified.'
            stamps = [r[column] for r in reader if r.get(column)]
        if not stamps:
            return f'{name}: no dated rows; freshness unverified.'
        return f'{name}: latest stored {column}={max(stamps)}; execution success does not certify source freshness.'
    except (OSError, csv.Error, KeyError, TypeError):
        return f'{name}: cannot read observation dates; freshness unverified.'


def display_result(result, verbose=False):
    output = result['stdout'] + ('\nSTDERR:\n'+result['stderr'] if result['stderr'] else '')
    if not result['success']:
        print('FAIL: '+result['reason'])
        # A failure never travels through the success/no-matched-lines branch.
        if output.strip():
            lines = output.strip().splitlines()
            diagnostic = [line for line in lines if any(k in line.upper() for k in ('ERROR','ALERT','UNAVAILABLE','FAIL'))]
            print(output if verbose else '\n'.join((diagnostic or lines[-5:])[:8]))
        else:
            print('No child diagnostic output; see exit/reason and raw report.')
    elif verbose:
        print(output)
    else:
        markers = ('BREACH', 'WARNING', 'UNAVAILABLE', 'ALERT', 'ERROR', 'SHORT COVER',
                   'Latest', 'LATEST', 'As of:', 'Data as of', 'IMMINENT', 'VOL PROXY',
                   'source quote', 'as_of=', 'NOT EVALUATED', 'UNKNOWN', '⚠️', '🔴', '🟠')
        lines = [line for line in output.splitlines() if any(k in line for k in markers)]
        print('\n'.join(lines) if lines else 'Completed; see detailed output. Freshness unverified here.')
    print(result.get('stored_vintage', 'Freshness unverified here.'))


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
    # Regression tests are not operational tools and must not run during boot.
    on_disk = sorted(p.name for p in SCRIPTS_DIR.glob("*.py")
                     if p.name != "boot.py" and not p.name.startswith("test_"))
    rows = [(n, n in wired, _one_line_purpose(SCRIPTS_DIR / n)) for n in on_disk]
    unwired = [n for n in on_disk if n not in wired]
    manual = [n for n in unwired if n in declared]
    orphans = [n for n in unwired if n not in declared]
    missing = sorted(wired - set(on_disk))
    if not CONTEXT_MODULE.is_file():
        missing.append('lib/boot_context.py')
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
        print("  Context helper: lib/boot_context.py (imported by boot; missing file is drift).")
        print("  Read-only modes: boot.py --orient [--part N], --predictions, --tools.")
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


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--tools', action='store_true')
    mode.add_argument('--orient', action='store_true', help='Read-only orientation index; use --part N to read every part')
    mode.add_argument('--predictions', action='store_true', help='Read-only OPEN prediction reminders')
    parser.add_argument('--part', type=int, help='Orientation part number; requires --orient')
    parser.add_argument('--quick', action='store_true', help='Monitoring: skip options only')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--report', type=Path, help='New raw JSONL report file for monitoring')
    args = parser.parse_args(argv)
    if args.part is not None and not args.orient:
        parser.error('--part requires --orient')
    if (args.orient or args.predictions or args.tools) and (args.quick or args.report):
        parser.error('Read-only modes cannot use --quick or --report')
    if args.tools:
        orphans, missing = print_tool_inventory(full=True)
        return int(bool(orphans or missing))
    # No network/script execution or writes on either context path.
    try:
        from lib.boot_context import ContextError, emit_orientation, prediction_report
    except ImportError as exc:
        print(f'ERROR: missing context reader: {exc}')
        return 1
    if args.orient or args.predictions:
        try:
            if args.orient:
                return emit_orientation(SAM_DIR, args.part)
            report, issues = prediction_report(SAM_DIR)
            print(report)
            return int(bool(issues))
        except (ContextError, OSError, ValueError) as exc:
            print(f'ERROR: context reader could not evaluate: {exc}')
            return 1
    now = datetime.now(timezone.utc)
    started = time.monotonic()
    path = args.report or SAM_DIR/'reports/boot-runs'/(now.strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8]+'.jsonl')
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        log = path.open('x', encoding='utf-8')
    except OSError as exc:
        print(f'ERROR: cannot create raw boot report {path}: {exc}; no monitoring started')
        return 1
    print(f'SAM monitoring started {now.isoformat()} | raw report: {path.resolve()}')
    results=[]
    with log:
        log.write(json.dumps({'started_at': now.isoformat(), 'mode': 'quick' if args.quick else 'monitor'})+'\n')
        for label, script_name, child_args, section_header, is_slow in BOOT_SEQUENCE:
            if script_name == 'fxy_options.py' and (args.quick or _has_today_row(FXY_OPTIONS_TSV)):
                reason='--quick' if args.quick else 'four unique future expiry rows already stored today'
                print(f'SKIP {label}: {reason}; snapshot quality not recertified.')
                log.write(json.dumps(dict(label=label, skipped=True, reason=reason))+'\n');log.flush()
                continue
            print(f'\nRunning {label}...', flush=True)
            result=run_script(label,SCRIPTS_DIR/script_name,child_args)
            result['stored_vintage']=stored_vintage(script_name)
            results.append(result)
            log.write(json.dumps(result,ensure_ascii=False)+'\n');log.flush()
            display_result(result,args.verbose)
        try:
            report,issues=prediction_report(SAM_DIR)
        except (ContextError,OSError,ValueError) as exc:
            report=f'ERROR: prediction reader could not evaluate: {exc}';issues=[report]
        print('\n'+report)
        log.write(json.dumps(dict(prediction_report=report,issues=issues),ensure_ascii=False)+'\n')
        orphans,missing=print_tool_inventory(full=False)
        failed=sum(not r['success'] for r in results)
        print(f'\nBOOT SUMMARY: {len(results)-failed}/{len(results)} executed scripts completed; {failed} failed.')
        print(f'Prediction reader: {"FAIL" if issues else "OK"}; inventory: {"FAIL" if orphans or missing else "OK"}.')
        print(f'Elapsed {time.monotonic()-started:.1f}s | Raw stdout/stderr and diagnostics: {path.resolve()}')
        print('Completion counts measure execution, not market freshness or analytical approval.')
        code=int(bool(failed or issues or orphans or missing))
        log.write(json.dumps(dict(exit_code=code,failed_scripts=failed,orphans=orphans,missing=missing))+'\n')
    return code


if __name__ == '__main__':
    sys.exit(main())
