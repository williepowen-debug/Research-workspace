#!/usr/bin/env python3
"""
MARCO Boot Sequence — Master Orchestrator

One command for the MARCO boot situational-awareness sweep. Replaces the manual
"surface predictions-due + eyeball KEY DATES" steps with an automated pass.

Two layers:
  1. READ-ONLY AWARENESS (always run, fast, offline-safe) —
       catalyst_countdown.py   what's due / passed-but-still-listed
       predictions_due.py      OPEN predictions + expected-signals past/near window
       staleness.py            STATUS / VX dashboard drift
       ledger_staleness.py     every workbook ledger vs the two-state rule (shared)
  2. DATA FETCHERS (run when their output is stale; skip when current) —
       banxico_reverse.py · h2a_pull.py · slaughter_pull.py
     Each is wrapped defensively (SAM pattern): per-fetcher timeout, non-fatal on
     failure, and a CADENCE-SKIP keyed on the output file's mtime — so a monthly
     series isn't re-pulled every boot, only when a new print is actually due.
     Running them at boot also keeps them exercised — breakage shows as ❌ FAIL
     instead of rotting unnoticed.

Usage:
  .venv/bin/python3 AGENTS/MARCO/scripts/boot.py
  .venv/bin/python3 AGENTS/MARCO/scripts/boot.py --quick     # awareness only, skip all fetchers
  .venv/bin/python3 AGENTS/MARCO/scripts/boot.py --refresh   # force fetchers, ignore cadence-skip
  .venv/bin/python3 AGENTS/MARCO/scripts/boot.py --verbose   # full output for every step
"""

import re
import subprocess
import sys
import time
from datetime import datetime, date, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
MARCO_DIR = SCRIPTS_DIR.parent
WORKSPACE = MARCO_DIR.parent.parent
VENV_PY = WORKSPACE / ".venv" / "bin" / "python3"
BASELINES = MARCO_DIR / "baselines"
TOOLS = MARCO_DIR / "tools"

# Read-only awareness scripts — always run, shown in full (they ARE the brief).
# (label, path, extra_args)
AWARENESS = [
    ("Catalyst Countdown",   SCRIPTS_DIR / "catalyst_countdown.py", []),
    ("Predictions Due Scan", SCRIPTS_DIR / "predictions_due.py", []),
    ("Staleness Check",      SCRIPTS_DIR / "staleness.py", []),
    # staleness.py covers STATUS + VX only. The shared fleet checker covers every
    # workbook ledger (FLOW/ML/KB/MIGRATION_PROXIES) against the two-state rule.
    # Wired 2026-08-11 after DAEDALUS measured FLOW+ML at +59d three times
    # (7/25 sweep, 8/4 WATT, 8/7 production review) with zero references to it
    # anywhere under AGENTS/MARCO/ — detection existed, invocation never did.
    ("Ledger Staleness",     WORKSPACE / "scripts" / "ledger_staleness.py", ["MARCO"]),
    # Built 2026-08-12 after session 21 produced FOUR instances of "the fix cleared the
    # region, not the file" — a brief section stale 11 days past its own test's resolution,
    # a git mv half-committed, duplicated stamp residue surviving a rewrite of its own line,
    # and (not machine-checkable) an analytical overclaim. Detection was never the gap;
    # invocation was — same lesson as the memory-index check.
    ("Version / Residue Drift", SCRIPTS_DIR / "version_drift_check.py", []),
    # Built 2026-08-21 (s23). Every check above reads a TSV through tsvutil, so a
    # defect INSIDE tsvutil makes all of them confidently wrong at once — and the
    # 8/21 quote-doubling incident proved that class is invisible to row counts,
    # field counts and staleness output alike. The specific trigger: read_tsv was
    # repaired to be csv-aware and read_tsv_numbered, forty lines below it, was not.
    # The one-time round-trip assertion written up as the fix could not see that,
    # because a one-time assertion tests the reader you were thinking about.
    ("TSV Reader Invariants", SCRIPTS_DIR / "tsvutil_selftest.py", []),
]

# Data fetchers: (label, script, output_file, cadence_days, timeout_s, vintage_fn)
# cadence_days = skip the fetch if the output file was refreshed within this window.
# vintage_fn (optional) = content-derived freshness test, overriding the mtime
#   cadence. Returns (should_fetch: bool, reason: str). PAT-044 / root CLAUDE.md:
#   mtime is restamped by git sync, so it fails FALSE-NEGATIVE — derive vintage
#   from file CONTENT wherever the content carries one.
FETCHERS = [
    ("Banxico remittances", TOOLS / "banxico_reverse.py",
     BASELINES / "banxico_destination_states.tsv", 85, 120, None),
    ("H-2A disclosure",     TOOLS / "h2a_pull.py",
     BASELINES / "h2a_latest.tsv",                 85, 180, lambda p: h2a_vintage(p)),
    ("Slaughter weekly",    TOOLS / "slaughter_pull.py",
     BASELINES / "slaughter_weekly.tsv",            6, 90, None),
]


def expected_h2a_quarter(today=None):
    """Newest FY quarter DOL should have published by `today`.

    OFLC fiscal quarters are Oct-start (Q1 = Oct-Dec). The disclosure file lands
    roughly a month after quarter end — FY26 Q3 closed Jun 30, docket expects it
    Aug 1 — so a quarter counts as 'available' 32 days after it ends.
    """
    today = today or date.today()
    ends = {1: (12, 31), 2: (3, 31), 3: (6, 30), 4: (9, 30)}
    best = None
    for fy in (today.year, today.year + 1):
        for q, (m, d) in ends.items():
            # FY2026 Q1 ends Dec 2025; Q2-Q4 end in calendar 2026.
            cal_year = fy - 1 if q == 1 else fy
            if date(cal_year, m, d) + timedelta(days=32) <= today:
                if best is None or (fy, q) > best:
                    best = (fy, q)
    return best


def h2a_vintage(path):
    """Fetch only when DOL should have a NEWER fiscal quarter than the file holds.

    Why not mtime: a successful pull would otherwise arm an 85-day skip, and doing
    that today (2026-07-31) would blind MARCO to the FY26 Q3 file publishing
    TOMORROW — straight through the window MAR-11 resolves in.
    """
    if not path.exists():
        return True, "output missing"
    try:
        head = path.read_text(errors="replace").split("\n", 1)[0]
        fy = int(re.search(r"\bfy=(\d{4})", head).group(1))
        q = int(re.search(r"\bthrough_q=(\d)", head).group(1))
    except Exception:
        return True, "no content vintage in header (pre-2026-07-31 format)"
    exp = expected_h2a_quarter()
    if exp and (fy, q) < exp:
        return True, f"holds FY{fy} Q{q}, DOL should have FY{exp[0]} Q{exp[1]}"
    # Rate-limit re-attempts when DOL is simply late, so a delayed publication
    # doesn't re-download 16MB on every boot of the day.
    age = file_age_days(path)
    if exp and (fy, q) == exp:
        return False, f"holds FY{fy} Q{q} = newest published"
    if age is not None and age < 1:
        return False, f"FY{fy} Q{q}, re-checked <1d ago"
    return True, f"holds FY{fy} Q{q}, re-checking"


def file_age_days(path):
    if not path.exists():
        return None
    return (time.time() - path.stat().st_mtime) / 86400.0


def run_script(path, timeout, args=(), findings_rc=()):
    # findings_rc: rc values meaning "ran correctly, reported real problems" (FINDINGS,
    # never FAIL). ledger_staleness rc contract REVISED 2026-08-17 (DAEDALUS shared-script
    # fix, CHECK_STANDARD §8 rule 3): 0 clean · 1 stale FINDINGS · 2 cannot-certify.
    if not path.exists():
        return "MISSING", f"  SKIP: {path.name} not found", 0.0
    start = time.time()
    try:
        r = subprocess.run([str(VENV_PY), str(path), *args], capture_output=True,
                           text=True, timeout=timeout, cwd=str(WORKSPACE))
        out = r.stdout
        # §8 rule 5 (DAEDALUS 2026-08-17): relay stderr UNCONDITIONALLY. The old
        # form gated on `returncode != 0`, so a script that exited 0 while warning
        # on stderr had that warning silently discarded — the same silent-green
        # class as the 101-day H-2A failure, one channel over.
        if r.stderr and r.stderr.strip():
            out += f"\n  STDERR: {r.stderr.strip()[-400:]}"
        status = "OK" if r.returncode == 0 else ("FINDINGS" if r.returncode in findings_rc else "FAIL")
        return status, out, time.time() - start
    except subprocess.TimeoutExpired:
        return "FAIL", f"  TIMEOUT after {timeout}s", time.time() - start
    except Exception as e:
        return "FAIL", f"  ERROR: {e}", time.time() - start


def collapse(output, status="OK"):
    """Show only alert/marker lines from a fetcher's output.

    NEVER prints the all-clear for a step that did not exit 0. A marker-matching
    filter cannot be trusted to surface arbitrary failure text (a bare Python
    traceback contains none of these tokens), so a failed step that happened to
    print nothing matchable used to render as '✓ ran cleanly' beside a FAIL in
    the summary — the two lines contradicting each other. That is how the H-2A
    fetcher sat dead for 101 days: boot said 'ran cleanly' every time.
    """
    # ALERT markers carry the finding; INFO markers are routine progress chatter.
    # Split because the cap must never evict an alert (DAEDALUS §8, 2026-08-17).
    ALERT = ("🔴", "🟠", "⚠️", "❌", "FAIL", "ERROR", "TIMEOUT", "Traceback")
    INFO = ("wrote", "Wrote", "Source:", "Total", "range:")
    src = output.splitlines()
    if status != "OK":
        # Show the RAW tail, not the marker-filtered lines: a traceback's marker
        # token is its first line but its cause is its last.
        tail = [ln for ln in src if ln.strip()][-3:]
        return [f"❌ exited {status} — output tail:"] + (tail or ["(no output captured)"])

    alerts = [ln for ln in src if any(m in ln for m in ALERT)]
    infos = [ln for ln in src if any(m in ln for m in INFO)
             and not any(m in ln for m in ALERT)]
    if not alerts and not infos:
        return ["    ✓ ran cleanly"]

    # EVERY alert line survives, oldest first — the earliest ⚠️ is usually the
    # root cause, and `lines[-4:]` used to drop it with no announcement at all
    # (a truncation that does not announce itself, CHECK_STANDARD §4).
    CAP = 4
    out = list(alerts)
    room = max(0, CAP - len(out))
    kept_info = infos[-room:] if room else []
    out += kept_info
    dropped = len(infos) - len(kept_info)
    if dropped > 0:
        out.append(f"    (+{dropped} earlier info line(s) suppressed — --verbose for all)")
    return out


def main():
    quick = "--quick" in sys.argv
    refresh = "--refresh" in sys.argv
    verbose = "--verbose" in sys.argv
    now = datetime.now()

    print(f"\n{'#'*72}")
    print(f"#{'MARCO BOOT SEQUENCE':^70}#")
    print(f"#{now.strftime('%A, %B %d, %Y  %H:%M'):^70}#")
    print(f"{'#'*72}")

    t0 = time.time()
    results = []

    # ---- Layer 1: read-only awareness ----
    # ledger_staleness emits 1 = stale FINDINGS under its revised 2026-08-17 rc contract
    # (2 = cannot-certify: MISCONFIGURED/OUTSIDE-GLOB — also findings, not script breakage).
    findings_rcs = {"Ledger Staleness": (1, 2)}
    for label, path, extra in AWARENESS:
        print(f"\n  ⏳ {label}…", flush=True)
        status, out, el = run_script(path, 60, extra, findings_rc=findings_rcs.get(label, ()))
        if out.strip():
            print(out if (verbose or True) else "")  # awareness always shown full
        results.append((label, status, el))

    # ---- Layer 2: data fetchers ----
    if quick:
        print(f"\n  ⏩ Fetchers skipped (--quick)")
    else:
        print(f"\n{'='*72}\n  DATA FETCHERS (content-vintage where available, else mtime)\n{'='*72}")
        for label, script, out_file, cadence, timeout, vintage_fn in FETCHERS:
            age = file_age_days(out_file)
            if vintage_fn is not None:
                should, why = vintage_fn(out_file)
                if not refresh and not should:
                    print(f"\n  ⏩ {label} — current ({why}), skip")
                    results.append((label, "SKIP", 0.0))
                    continue
                age_str = why
            else:
                if not refresh and age is not None and age < cadence:
                    print(f"\n  ⏩ {label} — current ({age:.0f}d < {cadence}d cadence), skip")
                    results.append((label, "SKIP", 0.0))
                    continue
                age_str = "missing" if age is None else f"{age:.0f}d old ≥ {cadence}d"
            print(f"\n  ⏳ {label} — {age_str}, fetching (timeout {timeout}s)…", flush=True)
            status, out, el = run_script(script, timeout)
            for ln in (out.splitlines() if verbose else collapse(out, status)):
                print(f"    {ln}" if not ln.startswith("    ") else ln)
            results.append((label, status, el))

    # ---- Summary ----
    print(f"\n{'='*72}\n  BOOT SUMMARY\n{'='*72}")
    print(f"\n  {'Step':<26}{'Status':>8}{'Time':>8}")
    print(f"  {'-'*42}")
    for label, status, el in results:
        icon = {"OK": "✅", "SKIP": "⏩", "MISSING": "❓", "FINDINGS": "⚠️"}.get(status, "❌")
        print(f"  {icon} {label:<24}{status:>6}{el:>7.1f}s")
    print(f"\n  Total boot: {time.time()-t0:.1f}s  |  {now:%Y-%m-%d}")

    fails = [r for r in results if r[1] == "FAIL"]
    if fails:
        print(f"\n  ⚠️  {len(fails)} step(s) failed — rerun with --verbose for detail.")
        return 1
    print(f"\n  ✅ Boot sweep complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
