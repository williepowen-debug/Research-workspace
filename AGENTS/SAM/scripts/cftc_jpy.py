#!/usr/bin/env python3
"""
SAM CFTC JPY Positioning Monitor
Fetches CFTC Commitments of Traders (futures-only short report) for JPY.

Source: https://www.cftc.gov/dea/newcot/deafut.txt
Release: Fridays ~3:30pm ET, reflects positions through the prior Tuesday.

Extracts JPY non-commercial (speculative) long, short, and net position.
Compares vs:
  - Prior week (delta from CFTC's built-in change columns)
  - July 2024 carry-unwind peak: -180,000 contracts
Alerts:
  🔴 Shorts closing >10% WoW (early unwind signal — shorts buying to cover)
  🟠 Net position approaching -150,000 (near Jul 2024 peak, max fuel for unwind)

Appends to workbook/CFTC_JPY.tsv.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/cftc_jpy.py
"""

import csv
import io
import sys
import urllib.request
from datetime import datetime
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
WARN_NET = -150000            # SAM alert level

TSV_HEADER = "Date\tOI\tNoncomm_Long\tNoncomm_Short\tNoncomm_Net\tChange_Long\tChange_Short\tChange_Net\tPct_of_Jul24_Peak\n"


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


def main():
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

    # Compute derived metrics
    pct_peak = (data["nc_net"] / JUL_2024_PEAK_NET * 100) if JUL_2024_PEAK_NET else 0

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

        # Interpret direction
        print(f"\n  INTERPRETATION")
        print(f"  {'-'*60}")
        if cs < -0.1 * data["nc_short"]:
            pct_cover = abs(cs) / (data["nc_short"] - cs) * 100
            print(f"  🔴 SHORT COVER: shorts down {pct_cover:.1f}% WoW — early unwind signal")
        elif cs > 0 and cl < 0:
            print(f"  🔴 SHORT BUILD: longs exiting, shorts adding — bearish for JPY (bullish crowded)")
        elif cs > 0:
            print(f"  🟠 SHORT ADD: shorts growing — more fuel for eventual unwind")
        elif cs < 0 and cl > 0:
            print(f"  🟢 SENTIMENT FLIP: shorts covering, longs adding — unwind underway")
        else:
            print(f"  ⚪ Mixed / sideways")

    # Comparison to Jul 2024 peak
    print(f"\n  REFERENCE: JUL 2024 CARRY UNWIND PEAK")
    print(f"  {'-'*60}")
    print(f"  Jul 2024 peak net:     {JUL_2024_PEAK_NET:>+10,}")
    print(f"  Current net:           {data['nc_net']:>+10,}")
    print(f"  % of peak:             {pct_peak:>9.1f}%")
    if data["nc_net"] < WARN_NET:
        print(f"  🟠 Net position approaching Jul 2024 peak — max fuel for unwind")

    # TSV append
    appended = append_tsv(data)
    if appended:
        print(f"\n  Appended to CFTC_JPY.tsv")
    else:
        print(f"\n  TSV already has {data['date']} — no append")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
