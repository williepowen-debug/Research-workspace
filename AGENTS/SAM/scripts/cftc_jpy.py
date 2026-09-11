#!/usr/bin/env python3
"""
SAM CFTC JPY Positioning Monitor
Fetches CFTC Commitments of Traders (futures-only short report) for JPY.

Source: https://www.cftc.gov/dea/newcot/deafut.txt
Release: Fridays ~3:30pm ET, reflects positions through the prior Tuesday.

Extracts JPY non-commercial (speculative) long, short, and net position.
Compares vs:
  - Prior week (delta from CFTC's built-in change columns)
  - Ratified historical reference: -188,077 contracts (2007-06-26; reviewed August 2026)
Alerts:
  Shorts declining >10% WoW, measured against prior shorts
  Net below -150,000: descriptive position-size watch, no automatic rearm

Appends to workbook/CFTC_JPY.tsv.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/cftc_jpy.py
"""

import csv
import io
import sys
import urllib.request
from datetime import datetime, date
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
CFTC_TSV = WORKBOOK / "CFTC_JPY.tsv"

CFTC_URL = "https://www.cftc.gov/dea/newcot/deafut.txt"
HEADERS = {"User-Agent": "Mozilla/5.0 (SAM-Research)"}

JPY_NAME = "JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE"

# Historical reference points
# ⚠️ BASIS NOTE (2026-08-14) — THIS CONSTANT IS ON A RETIRED BASIS AND IS LEFT
# DELIBERATELY UNCHANGED. The forum-4 falsifier pass (2026-08-11) corrected SAM's
# reference extremum THREE times and settled on the publisher's FULL record:
#     R = -188,077 [2007-06-26], OI 352,299, n = 1,354 back to 2000-08-29
# superseding -184,223 (an epoch AND an undisclosed 2018+ window) and -180,000
# (a rounding). Corrected labels: 8/4 = 24.2% (not 25.3%) · 7/28 = 86.9% (not
# 90.8%) · the 7/10 fire = 82.5%, i.e. 2.5pp BELOW the 85% its own label invoked.
#
# WHY THE CONSTANT STAYS -180000 ANYWAY: the `Pct_of_Jul24_Peak` column is a
# DISPLAY BASIS, not a gate — "ALL CONTRACT GATES UNAFFECTED" (forum-4 §1.2).
# Re-basing it here would silently change the meaning of one column across ~100
# historical rows and leave the series half-converted, which is the
# partial-record-written-as-final failure class. The corrected percentage is
# computed at grade time in scripts/grade_8_14_branch.py, which carries R.
#
# ⛔ NEVER cite this column's output as "% of peak" in prose. It is legacy-basis.
JUL_2024_PEAK_NET = -180000   # RETIRED BASIS — see BASIS NOTE above; true R = -188,077
REFERENCE_NET = -188077  # display only; do not rebase the legacy TSV column
WARN_NET = -150000            # SAM alert level

TSV_HEADER = "Date\tOI\tNoncomm_Long\tNoncomm_Short\tNoncomm_Net\tChange_Long\tChange_Short\tChange_Net\tPct_of_Jul24_Peak\n"

# ---------------------------------------------------------------------------
# MULTI-PRINT DRIFT CHECK — successor to the single-week deadband (KB-SAM-231)
#
# THE DEFECT IT FIXES: the registered single-print rule grades any |WoW| inside
# +/-12,160 as B0 NO-VERDICT. That is calibrated to ONE-WEEK moves and is
# structurally blind to a persistent SAME-SIGN drift: the resolver can print B0
# four weeks running while the net walks a long way. Measured instance
# (KB-SAM-231, 2026-09-02): 2026-08-18 (-10,808) + 2026-08-25 (-10,405)
# = -21,213 with BOTH prints inside the deadband and both graded B0.
#
# THE RULE: when two CONSECUTIVE prints are both inside the deadband, test their
# AGGREGATE against DRIFT_BAR. Breach => the pair is flagged for a read; it is
# NOT a grade, NOT an entry condition, and re-arms nothing (the convexity frame
# retired 2026-08-07 and the -153K/85% flip-condition is void, not unfired).
#
# ⛔ BOTH CONSTANTS ARE FROZEN AT REGISTRATION AND MUST NOT FLOAT.
# Recomputing the median each run would make the bar a moving target — i.e. a
# retune of a LIVE rule, which is exactly what the registration discipline
# forbids. The live median is printed as ADVISORY ONLY so a future session can
# see sample drift; nothing grades on it.
#
# PROVENANCE OF THE BAR: 1.5 x median|WoW| was named in KB-SAM-231 on 2026-09-02,
# BEFORE this backtest was run — it was not fitted here. median|WoW| = 12,325
# over n=22 weekly prints, 2026-04-07..2026-09-01; 1.5x = 18,488, frozen
# 2026-09-11 ahead of the Sep-8-vintage print.
# ⚠️ HONEST LIMIT ON THE EVIDENCE: over that sample the rule fires on 2 of 6
# consecutive-B0 pairs (2026-04-21+04-28 = -18,851; 2026-08-18+08-25 = -21,213)
# and stays silent on the 4 sign-alternating pairs — so it discriminates rather
# than firing on everything. But the 1.5x figure was itself derived from the
# Aug-18/25 episode, so that firing is IN-SAMPLE; only the April pair is an
# independent confirmation. n=22, one regime. This is a REGISTERED DECISION
# RULE, not a calibrated base rate.
DRIFT_DEADBAND = 12160        # FROZEN — the registered single-print B0 deadband
DRIFT_BAR = 18488             # FROZEN — 1.5 x median|WoW| (12,325), n=22, Apr-Sep 2026
DRIFT_BAR_BASIS = "1.5 x median|WoW| 12,325 over n=22 (2026-04-07..2026-09-01), frozen 2026-09-11"


def _read_drift_rows():
    """Return [(date, change_net)] for rows with a usable Change_Net, oldest first."""
    if not CFTC_TSV.exists():
        return []
    out = []
    with open(CFTC_TSV) as f:
        reader = csv.DictReader(f, delimiter="\t")
        if not {"Date", "Change_Net"}.issubset(reader.fieldnames or []):
            raise ValueError("CFTC ledger lacks Date/Change_Net columns")
        for row in reader:
            stamp = date.fromisoformat(row["Date"])
            # Do not drop malformed observations and bridge the resulting hole.
            out.append((stamp.isoformat(), int(row["Change_Net"])))
    out.sort()
    if len({d for d, _ in out}) != len(out):
        raise ValueError("duplicate CFTC observation dates")
    return out


def multi_print_drift_check():
    """Print the two-print aggregate drift check. Read-only; never grades or writes."""
    try:
        rows = _read_drift_rows()
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"\n  MULTI-PRINT DRIFT CHECK: UNKNOWN — {exc}; check NOT EVALUATED.")
        return False
    print("\n  MULTI-PRINT DRIFT CHECK (KB-SAM-231 successor; frozen bars)")
    print(f"  {'-'*60}")
    if len(rows) < 2:
        print("  INSUFFICIENT HISTORY: fewer than 2 usable prints; check NOT EVALUATED.")
        return False
    (d_prev, c_prev), (d_last, c_last) = rows[-2], rows[-1]
    print(f"  Deadband +/-{DRIFT_DEADBAND:,} | drift bar {DRIFT_BAR:,} ({DRIFT_BAR_BASIS})")
    if (date.fromisoformat(d_last) - date.fromisoformat(d_prev)).days != 7:
        print("  UNKNOWN: latest observations are not seven days apart; verify missing prints or the publisher's holiday schedule. Check NOT EVALUATED.")
        return False
    both_b0 = abs(c_prev) <= DRIFT_DEADBAND and abs(c_last) <= DRIFT_DEADBAND
    agg = c_prev + c_last
    print(f"  {d_prev} {c_prev:+,}  +  {d_last} {c_last:+,}  =  {agg:+,}")
    if not both_b0:
        outside = d_last if abs(c_last) > DRIFT_DEADBAND else d_prev
        print(f"  NOT APPLICABLE: {outside} moved outside the deadband and is graded on its own print.")
    elif abs(agg) > DRIFT_BAR:
        print(f"  DRIFT FLAG: two consecutive B0 prints aggregate {agg:+,}, beyond the {DRIFT_BAR:,} bar.")
        print("  READ the pair as one move. This is a flag to LOOK, not a grade;")
        print("  it re-arms nothing and is not an entry condition.")
    else:
        print(f"  No drift flag: aggregate {abs(agg):,} is within the {DRIFT_BAR:,} bar.")
    # B0 run length, advisory
    run = 0
    newer = None
    for d, c in reversed(rows):
        stamp = date.fromisoformat(d)
        if newer is not None and (newer - stamp).days != 7:
            break
        newer = stamp
        if abs(c) <= DRIFT_DEADBAND:
            run += 1
        else:
            break
    if run >= 3:
        print(f"  ADVISORY: {run} consecutive B0 prints. A long B0 run is the condition this check exists for.")
    # advisory live median — never used to grade
    mags = sorted(abs(c) for _, c in rows)
    n = len(mags)
    live_med = mags[n // 2] if n % 2 else (mags[n // 2 - 1] + mags[n // 2]) / 2
    print(f"  ADVISORY ONLY (never grades): live median|WoW| {live_med:,.0f} over n={n}; frozen basis used 12,325.")
    return True



def fetch_cftc_text():
    """Fetch CFTC deafut.txt content."""
    try:
        req = urllib.request.Request(CFTC_URL, headers=HEADERS)
        # 10s (not 30s): fail fast on a slow/dead CFTC endpoint rather than
        # hanging ~30s and eating boot.py's 60s per-script budget. Cached TSV
        # holds last-known positioning; a FAIL here is an honest "couldn't refresh".
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ERROR fetching CFTC data: {e}")
        return None


def find_jpy_row(text):
    """Locate the JPY row and parse its CSV fields. Returns list of fields or None."""
    for line in text.splitlines():
        if JPY_NAME in line and "EURO FX" not in line:
            # Use csv.reader to handle quoted fields
            reader = csv.reader(io.StringIO(line))
            return next(reader, None)
    return None


def parse_jpy_fields(fields):
    """
    Parse JPY CFTC fields. Returns dict or None.
    Field layout (futures-only short report):
       0: Market/Exchange name
       1: As-of YYMMDD
       2: As-of YYYY-MM-DD
       3: CFTC Contract Market Code
       4: Market Code
       5: Region
       6: Commodity Code
       7: Open Interest
       8: Noncomm Long
       9: Noncomm Short
      10: Noncomm Spread
      11: Commercial Long
      12: Commercial Short
      13: Total Long
      14: Total Short
      15: Nonrept Long
      16: Nonrept Short
      17-26: "Old" positions (same duplicated)
      27-36: "Other" positions (usually zeros)
      37: OI Change WoW
      38: Noncomm Long Change
      39: Noncomm Short Change
      40: Noncomm Spread Change
      ...
    Reference: CFTC short-format schema.
    """
    if not fields or len(fields) < 50:
        return None

    def ival(s):
        try:
            return int(s.replace(",", "").strip())
        except (ValueError, AttributeError):
            return None

    try:
        date_str = fields[2].strip()
        oi = ival(fields[7])
        nc_long = ival(fields[8])
        nc_short = ival(fields[9])
        nc_spread = ival(fields[10])
        # Skip "Old" (17-26) and "Other" (27-36) repetitions
        # Change columns start at index 37
        change_oi = ival(fields[37])
        change_nc_long = ival(fields[38])
        change_nc_short = ival(fields[39])
    except IndexError:
        return None

    if nc_long is None or nc_short is None:
        return None

    nc_net = nc_long - nc_short
    change_nc_net = None
    if change_nc_long is not None and change_nc_short is not None:
        change_nc_net = change_nc_long - change_nc_short

    return {
        "date": date_str,
        "oi": oi,
        "nc_long": nc_long,
        "nc_short": nc_short,
        "nc_net": nc_net,
        "nc_spread": nc_spread,
        "change_oi": change_oi,
        "change_nc_long": change_nc_long,
        "change_nc_short": change_nc_short,
        "change_nc_net": change_nc_net,
    }


def append_tsv(data):
    """Append latest CFTC JPY data to TSV."""
    existing = set()
    if CFTC_TSV.exists():
        with open(CFTC_TSV) as f:
            next(f, None)
            for line in f:
                parts = line.strip().split("\t")
                if parts:
                    existing.add(parts[0])
    else:
        with open(CFTC_TSV, "w") as f:
            f.write(TSV_HEADER)

    if data["date"] in existing:
        return False

    pct_peak = (data["nc_net"] / JUL_2024_PEAK_NET * 100) if JUL_2024_PEAK_NET else 0

    with open(CFTC_TSV, "a") as f:
        f.write(
            f"{data['date']}\t{data.get('oi', '')}\t{data['nc_long']}\t{data['nc_short']}\t"
            f"{data['nc_net']}\t"
            f"{data.get('change_nc_long', '') or ''}\t"
            f"{data.get('change_nc_short', '') or ''}\t"
            f"{data.get('change_nc_net', '') or ''}\t"
            f"{pct_peak:.1f}\n"
        )
    return True


def short_cover_pct(current_short, change_short):
    prior = current_short - change_short
    if current_short < 0 or prior <= 0:
        raise ValueError('Invalid current/prior gross shorts')
    return -change_short / prior * 100


def reference_description(net):
    if net > 0:
        return 'NET LONG; short-reference percentage not applicable'
    return f'Net short magnitude: {net / REFERENCE_NET * 100:.1f}% of the ratified historical reference'



def _selftest():
    """Frozen-fixture regression for multi_print_drift_check().

    Fixtures are FROZEN LITERALS, deliberately not the live TSV: a test pinned to
    a live surface certifies nothing past the next data append
    ([[finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit]]).
    Run: .venv/bin/python3 AGENTS/SAM/scripts/cftc_jpy.py --selftest
    """
    import contextlib
    import tempfile
    global CFTC_TSV
    saved = CFTC_TSV
    cases = [
        ("FIRE: KB-SAM-231 worked instance",
         [("2026-08-18", -10808), ("2026-08-25", -10405)], "DRIFT FLAG"),
        ("SILENT: sign-alternating whipsaw",
         [("2026-04-14", 10534), ("2026-04-21", -11252)], "No drift flag"),
        ("NOT-APPLICABLE: last print outside deadband",
         [("2026-08-25", -10405), ("2026-09-01", -28929)], "NOT APPLICABLE"),
        ("FIRE: independent April pair",
         [("2026-04-21", -11252), ("2026-04-28", -7599)], "DRIFT FLAG"),
        ("EDGE: aggregate exactly ON the bar stays silent (strict >)",
         [("2026-08-11", -9244), ("2026-08-18", -9244)], "No drift flag"),
        ("EDGE: one contract over the bar fires",
         [("2026-08-11", -9244), ("2026-08-18", -9245)], "DRIFT FLAG"),
        ("DEGENERATE: single row",
         [("2026-08-11", -5000)], "INSUFFICIENT HISTORY"),
        ("RUN: three consecutive B0 prints raise the advisory",
         [("2026-08-11", -5000), ("2026-08-18", -5000), ("2026-08-25", -5000)], "3 consecutive B0 prints"),
    ]
    failures = 0
    try:
        with tempfile.TemporaryDirectory() as td:
            for i, (name, rows, expect) in enumerate(cases):
                path = Path(td) / f"fixture{i}.tsv"
                with open(path, "w") as f:
                    f.write(TSV_HEADER)
                    for d, cn in rows:
                        f.write(f"{d}\t\t\t\t\t\t\t{cn}\t\n")
                CFTC_TSV = path
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    multi_print_drift_check()
                out = buf.getvalue()
                ok = expect in out
                failures += (not ok)
                print(("  PASS  " if ok else "  FAIL  ") + name)
                if not ok:
                    print(f"        expected {expect!r} in output; got:")
                    print("        " + out.strip().replace("\n", " | ")[:300])
    finally:
        CFTC_TSV = saved
    print(f"\n  SELFTEST: {len(cases) - failures}/{len(cases)} passed.")
    return 1 if failures else 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  SAM CFTC JPY Positioning Monitor — {now}")
    print(f"{'='*70}")

    text = fetch_cftc_text()
    if not text:
        print("\n  ERROR: Failed to fetch CFTC data.")
        return 1

    fields = find_jpy_row(text)
    if not fields:
        print("\n  ERROR: JPY row not found in CFTC data.")
        return 1

    data = parse_jpy_fields(fields)
    if not data:
        print("\n  ERROR: JPY row parse failed.")
        return 1

    print(f"\n  As of:             {data['date']}")
    print(f"  Open Interest:     {data['oi']:>10,}")
    print(f"\n  NON-COMMERCIAL (speculative) POSITIONING")
    print(f"  {'-'*60}")
    print(f"  Long:              {data['nc_long']:>10,} contracts")
    print(f"  Short:             {data['nc_short']:>10,} contracts")
    print(f"  Net:               {data['nc_net']:>+10,} contracts")
    print(f"  Spread:            {data['nc_spread']:>10,} contracts")

    # Week-over-week
    if data["change_nc_long"] is not None and data["change_nc_short"] is not None:
        print(f"\n  WEEK-OVER-WEEK CHANGE")
        print(f"  {'-'*60}")
        def arrow(x):
            return "↑" if x > 0 else "↓" if x < 0 else "·"
        cl = data["change_nc_long"]
        cs = data["change_nc_short"]
        cn = data["change_nc_net"]
        print(f"  Long  Δ:           {cl:>+10,}  {arrow(cl)}")
        print(f"  Short Δ:           {cs:>+10,}  {arrow(cs)}")
        if cn is not None:
            print(f"  Net   Δ:           {cn:>+10,}  {arrow(cn)}")

        print("\n  OBSERVED POSITION CHANGES")
        try:
            pct_cover = short_cover_pct(data['nc_short'], cs)
        except ValueError as exc:
            print(f"  ERROR: {exc}; short-cover percentage NOT EVALUATED")
            return 1
        if pct_cover > 10:
            print(f"  SHORT COVER: gross shorts down {pct_cover:.1f}% versus prior week (>10% watch)")
        elif cs < 0:
            print(f"  Gross shorts down {pct_cover:.1f}% versus prior week (no >10% watch)")
        elif cs > 0:
            print("  SHORT ADD: gross shorts increased")
        else:
            print("  Gross shorts unchanged")
        print("  Gross longs increased" if cl > 0 else "  Gross longs decreased" if cl < 0 else "  Gross longs unchanged")
        print("  Position changes alone do not establish forced liquidation.")

    print("\n  REFERENCE: -188,077 contracts on 2007-06-26; ratified from the record reviewed August 2026")
    print(f"  Current net: {data['nc_net']:+,}")
    print("  "+reference_description(data['nc_net']))
    print("  Historical storage: Pct_of_Jul24_Peak retains legacy -180,000 basis; not the current reference.")
    if data['nc_net'] < WARN_NET:
        print("  Net below -150,000 position-size watch; retired entry conditions do not rearm.")

    # TSV append
    appended = append_tsv(data)
    if appended:
        print(f"\n  Appended to CFTC_JPY.tsv")
    else:
        print(f"\n  TSV already has {data['date']} — no append")

    # Drift check runs AFTER the append so the latest print is included.
    drift_ok = multi_print_drift_check()

    print()
    return 2 if drift_ok is False else 0


if __name__ == "__main__":
    sys.exit(main())
