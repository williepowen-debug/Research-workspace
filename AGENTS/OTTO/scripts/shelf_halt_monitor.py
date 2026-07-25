#!/usr/bin/env python3
"""
OTTO — Subprime ABS shelf-activity monitor (OTTO-07 instrument)

REPLACES workbook/ABS_ISSUANCE.tsv + scripts/abs_issuance_tracker.py, which were
FROZEN 2026-07-25 after being found INVERTED: the stub emitted `total_deals_ytd 0 /
shelf_halts 0` for a period STATUS documents as robust issuance (EART 2026-3 upsized
to $1.2bn, priced ~2026-06-24). It emitted zeros because nobody ran it — and a reader
could not tell that from an observation of zero issuance.

    OTTO-07: "At least one subprime ABS shelf halts issuance" (resolve 2026-12-31)

A default-zero instrument CANNOT falsify a "something halts" claim. It can only ever
appear to confirm the null. That defect is why this file exists.

DESIGN REQUIREMENT — fail-loud semantics (DAEDALUS spec, 2026-07-25, PAT-060):
  Every emitted row carries a RUN STAMP (run timestamp + query + per-issuer hit counts).
  A zero is only meaningful when attached to a run that provably executed.

  status=OK       -> the run executed, positive control passed, counts are real data
  status=INVALID  -> the run executed but the POSITIVE CONTROL FAILED; counts are
                     meaningless and must not be read (endpoint/schema/query drift)
  status=ERROR    -> the run failed (network/HTTP/parse). NO counts are written.

  There is deliberately NO code path that writes a bare 0 without a run stamp.
  If this script never runs, the ledger simply gains no rows — absence of a row means
  "nobody looked," which is exactly the state the old stub disguised as "nothing happened."

POSITIVE CONTROL (per [[finding_discovery_tool_wrong_slice_false_zero]]):
  Before trusting any zero, the run queries a KNOWN-ACTIVE shelf. If that control
  returns 0 hits, the query/endpoint is broken, not the market — the whole run is
  marked INVALID rather than reporting a false quiet.

Method + the four EDGAR-FTS rules: see AGENTS/OTTO/EDGAR_8K_MONITOR.md (instrument registry).

Usage:
  .venv/bin/python3 AGENTS/OTTO/scripts/shelf_halt_monitor.py            # 90-day window
  .venv/bin/python3 AGENTS/OTTO/scripts/shelf_halt_monitor.py --days 180
  .venv/bin/python3 AGENTS/OTTO/scripts/shelf_halt_monitor.py --dry-run  # no ledger write
"""

import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

OTTO_DIR = Path(__file__).resolve().parent.parent
LEDGER = OTTO_DIR / "workbook" / "SHELF_ACTIVITY.tsv"

FTS = "https://efts.sec.gov/LATEST/search-index?"
UA = {"User-Agent": "OTTO Research willi.research@gmail.com"}

# Subprime / near-subprime auto ABS shelves OTTO tracks, by EXACT EDGAR trust-name stem.
# Issuance is probed by testing whether "<stem> <year>-<n>" exists as a filed entity —
# a deterministic existence check, NOT a relevance-ranked sample. (An earlier draft
# sampled relevance-sorted hits and manufactured a false zero for CPS: the shelf was
# fine, the sampling was wrong. Cf. [[finding_discovery_tool_wrong_slice_false_zero]].)
SHELVES = [
    ("Exeter",    "Exeter Automobile Receivables Trust"),
    ("Santander", "Santander Drive Auto Receivables Trust"),
    ("CPS",       "CPS Auto Receivables Trust"),        # LETTER vintages (2026-A/B), not numeric
    ("Westlake",  "Westlake Automobile Receivables Trust"),
    ("Lendbuzz",  "Lendbuzz Securitization Trust"),
    ("GLS",       "GLS Auto Receivables Issuer Trust"),
    ("ACA",       "American Credit Acceptance Receivables Trust"),
    ("Bridgecrest", "Bridgecrest Lending Auto Securitization Trust"),  # = Carvana/DriveTime shelf
    # NOTE: "Carvana Auto Receivables Trust" is NOT an EDGAR entity — the 2026-07-25 run
    # correctly flagged it INVALID rather than reporting Carvana as a halted shelf.
    # Carvana-originated paper securitizes through Bridgecrest (above).
]

# Some shelves vintage by NUMBER (Exeter 2026-3), others by LETTER (CPS 2026-A).
# Probing only one convention manufactures a false "quiet" — CPS was mis-flagged
# INVALID on the 2026-07-25 first run for exactly this reason.
SUFFIXES = [str(i) for i in range(1, 9)] + list("ABCDEFGH")

# RETIRED FROM THE PROBE SET — corporate action, NOT a shelf halt:
#   Flagship Credit Auto Trust — 4 deals 2022, 3 in 2023, 2 in 2024, ZERO 2025-2026.
#   Shape looked like a textbook OTTO-07 halt. Verification (required by this file's own
#   rule) found Flagship Credit Acceptance was ACQUIRED BY INTERVEST in Nov 2025 and
#   rebranded (~"Flagship Financial"), is revamping originations for 2026, and took a
#   $300M facility. The shelf stopped because the issuer was absorbed, not because
#   funding closed. Logged as a near-miss: the instrument surfaced it, the verification
#   rule killed it. Re-add if a successor shelf appears and then goes quiet.

MAX_VINTAGE = 8          # legacy bound; SUFFIXES governs the probe
CONTROL_YEAR_OFFSET = 1  # per-issuer control: the prior year must show >=1 vintage

COLUMNS = [
    "run_ts", "status", "probe_year", "control_year", "shelves_checked",
    "shelves_issuing", "shelves_quiet", "shelves_invalid",
    "per_issuer_vintages", "verdict", "notes",
]


REQUEST_DELAY = 0.15   # EDGAR fair-use pacing (<10 req/s)
MAX_RETRIES = 3


def phrase_exists(phrase, timeout=30):
    """True if EDGAR full-text search matches this exact phrase at all.

    Retries transient HTTP errors with backoff, then RAISES. It must never return False
    because of a network error — a False here would be indistinguishable from "this shelf
    did not issue," which is the exact defect this whole instrument exists to prevent.
    (The 2026-07-25 first run hit EDGAR rate-limiting on CPS/Flagship; the fail-loud path
    correctly reported them as errors rather than as quiet shelves.)"""
    url = FTS + urllib.parse.urlencode({"q": f'"{phrase}"'})
    last = None
    for attempt in range(MAX_RETRIES):
        try:
            time.sleep(REQUEST_DELAY)
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                payload = json.load(r)
            return int(payload["hits"]["total"]["value"]) > 0
        except Exception as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise last


NUMERIC = [str(i) for i in range(1, 7)]
LETTER = list("ABCDEF")


def detect_convention(stem, control_year):
    """Return 'numeric' | 'letter' | None for how this shelf vintages its trusts.

    Determined against the CONTROL year, so a shelf that simply hasn't issued yet this
    year still resolves its convention. None => the stem never matches => config error,
    which must be reported as INVALID rather than as a quiet shelf.
    """
    if phrase_exists(f"{stem} {control_year}-1"):
        return "numeric"
    if phrase_exists(f"{stem} {control_year}-A"):
        return "letter"
    return None


def probe_shelf(stem, year, convention):
    """List the vintages of `stem` that exist for `year`, using the known convention.
    Stops after two consecutive misses — vintages are issued in order."""
    suffixes = NUMERIC if convention == "numeric" else LETTER
    found, misses = [], 0
    for suf in suffixes:
        if phrase_exists(f"{stem} {year}-{suf}"):
            found.append(f"{year}-{suf}")
            misses = 0
        else:
            misses += 1
            if misses >= 2:
                break
    return found


def write_row(row, dry_run=False):
    if dry_run:
        print("\n  [--dry-run] ledger row NOT written:")
        print("  " + "\t".join(str(row[c]) for c in COLUMNS))
        return
    new = not LEDGER.exists()
    with LEDGER.open("a") as f:
        if new:
            f.write("\t".join(COLUMNS) + "\n")
        f.write("\t".join(str(row[c]) for c in COLUMNS) + "\n")


def main():
    dry_run = "--dry-run" in sys.argv
    year = datetime.now().year
    if "--year" in sys.argv:
        year = int(sys.argv[sys.argv.index("--year") + 1])
    control_year = year - CONTROL_YEAR_OFFSET
    run_ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    print(f"\n{'='*74}")
    print(f"  OTTO Shelf-Activity Monitor (OTTO-07 instrument) — {run_ts}")
    print(f"  Probing {year} vintages; per-issuer control year {control_year}")
    print(f"{'='*74}")
    print(f"\n  {'Shelf':<12} {'control':>8}  {year} vintages")
    print(f"  {'-'*56}")

    row = dict.fromkeys(COLUMNS, "")
    row.update(run_ts=run_ts, probe_year=year, control_year=control_year,
               shelves_checked=len(SHELVES))

    per, issuing, quiet, invalid, errors = {}, [], [], [], []
    for name, stem in SHELVES:
        try:
            convention = detect_convention(stem, control_year)
            ctrl = probe_shelf(stem, control_year, convention) if convention else []
            if not ctrl:
                # Name/convention doesn't resolve -> config error, NOT a halt.
                per[name] = "INVALID"
                invalid.append(name)
                print(f"  {name:<12} {'NONE':>8}  ⚠️ INVALID — no {control_year} vintage either; "
                      f"trust-name stem likely wrong. NOT counted as quiet.")
                continue
            cur = probe_shelf(stem, year, convention)
        except Exception as e:
            per[name] = "ERR"
            errors.append(f"{name}:{type(e).__name__}")
            print(f"  {name:<12} {'ERR':>8}  ⚠️ query failed — NOT counted as quiet")
            continue
        per[name] = ",".join(cur) if cur else "none"
        if cur:
            issuing.append(name)
            print(f"  {name:<12} {len(ctrl):>8}  ✓ {', '.join(cur)}")
        else:
            quiet.append(name)
            print(f"  {name:<12} {len(ctrl):>8}  🔴 QUIET — issued in {control_year}, nothing in {year}")

    row.update(status="OK" if not errors else "OK-PARTIAL",
               shelves_issuing=len(issuing), shelves_quiet=len(quiet),
               shelves_invalid=len(invalid),
               per_issuer_vintages=";".join(f"{k}={v}" for k, v in per.items()))

    if quiet:
        row["verdict"] = f"OTTO-07 CANDIDATE — quiet: {','.join(quiet)}"
        note = (f"{len(quiet)} shelf/shelves issued in {control_year} but show NO {year} vintage. "
                f"This is the OTTO-07 signal shape. VERIFY BEFORE RESOLVING: confirm the issuer was not "
                f"acquired, renamed, or simply slower than annual cadence — a shelf halt requires intent "
                f"or inability to issue, not merely a gap.")
    else:
        row["verdict"] = "NO HALT — every validated shelf issued this year"
        note = (f"All {len(issuing)} validated shelves show at least one {year} vintage. This is a REAL "
                f"observed zero-halts reading, attributable to a run that executed at {run_ts} with "
                f"per-issuer controls passing against {control_year}.")
    if invalid:
        note += (f" | {len(invalid)} shelf/shelves marked INVALID (no {control_year} vintage — "
                 f"name stem wrong, not quiet): {','.join(invalid)}. FIX THE STEM, do not read as a halt.")
    if errors:
        note += f" | PARTIAL: query errors on {','.join(errors)} — NOT counted as quiet."
    row["notes"] = note

    print(f"\n  VERDICT: {row['verdict']}")
    print(f"  {note}")
    write_row(row, dry_run)
    print(f"\n  {'(dry run — nothing written)' if dry_run else f'Appended to {LEDGER.name}'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
