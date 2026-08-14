#!/usr/bin/env python3
"""
MIDAS — CFTC COT gold puller (LEGACY futures-only), release-day safe.

Closes the long-standing "COT weekly-cadence leg" open item (SCRATCH carryover
since 2026-07-12).

WHY A RAW-FILE PULLER AND NOT SOCRATA (auto-memory
`finding_cftc_cot_raw_file_beats_socrata_lag`):
  - The Socrata dataset lags the 15:30 ET website post by ~15-60+ min. Worse,
    the RAW file itself lagged ~20 min on 2026-08-07. Both serve a clean 200
    carrying LAST week's vintage — the
    `finding_partitioned_source_returns_stale_window_at_200` shape, on a schedule.
  - => NEVER grade the first response after 15:30. Poll until the as-of date
    IN-ROW equals the expected Tuesday. `--expect YYYY-MM-DD` exits 3 (WAIT) on
    a stale vintage rather than returning a number.

GUARDS (each one bought by a real defect):
  1. CODE-KEYED extraction (088691), not name-keyed. Contract names get relabeled
     (the WTI "CRUDE OIL, LIGHT SWEET" -> "WTI-PHYSICAL" precedent).
  2. csv module, NOT naive comma-split — quoted market names contain commas and
     shift every field by +1.
  3. EXACT full-size contract only. A `like '%GOLD%'` filter mixes in MICRO GOLD
     and corrupted 6 of 15 weeks on MIDAS's first pull (2026-08-07, KB-036).
  4. TOTALS RECONCILIATION before any position number is read:
     OI == TotRept_long + NonRept_long, and == TotRept_short + NonRept_short.
     Fails loud (`finding_fail_loud_on_incomplete_data`).
  5. In-row report-date verification (`--expect`).

Usage:
  python3 cot_gold.py                      # latest vintage, whatever it is
  python3 cot_gold.py --expect 2026-08-11  # exit 3 (WAIT) unless in-row date matches
  python3 cot_gold.py --expect 2026-08-11 --poll 60 --max-wait 3600
"""
import argparse
import csv
import io
import sys
import time
import urllib.request

URL = "https://www.cftc.gov/dea/newcot/deafut.txt"
GOLD_CODE = "088691"          # COMEX full-size gold. Micro gold is a DIFFERENT code.
GOLD_NAME_EXPECT = "GOLD - COMMODITY EXCHANGE INC."
UA = "Mozilla/5.0 (research; MIDAS metals agent; contact via repo)"  # 403 w/o a UA

# Legacy futures-only short-format field indices.
F_NAME, F_DATE_YMD, F_CODE = 0, 2, 3
F_OI = 7
F_NC_LONG, F_NC_SHORT, F_NC_SPREAD = 8, 9, 10
F_COM_LONG, F_COM_SHORT = 11, 12
F_TOT_LONG, F_TOT_SHORT = 13, 14
F_NONREPT_LONG, F_NONREPT_SHORT = 15, 16


def fetch(url=URL):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        if r.status != 200:
            raise RuntimeError(f"HTTP {r.status} from {url}")
        return r.read().decode("utf-8", errors="replace")


def extract_gold(text):
    """Code-keyed extraction + totals reconciliation. Returns dict or raises."""
    rows = list(csv.reader(io.StringIO(text)))
    hits = [r for r in rows if len(r) > F_NONREPT_SHORT and r[F_CODE].strip() == GOLD_CODE]
    if len(hits) != 1:
        raise RuntimeError(
            f"expected exactly 1 row for contract code {GOLD_CODE}, got {len(hits)} "
            "(guard 1/3: code-keyed, full-size only)"
        )
    r = hits[0]
    name = r[F_NAME].strip()
    if GOLD_NAME_EXPECT not in name.upper():
        raise RuntimeError(f"code {GOLD_CODE} resolved to unexpected name {name!r}")

    def n(i):
        return int(float(r[i].strip()))

    d = {
        "report_date": r[F_DATE_YMD].strip(),
        "market": name,
        "oi": n(F_OI),
        "nc_long": n(F_NC_LONG),
        "nc_short": n(F_NC_SHORT),
        "nc_spread": n(F_NC_SPREAD),
        "com_long": n(F_COM_LONG),
        "com_short": n(F_COM_SHORT),
        "tot_long": n(F_TOT_LONG),
        "tot_short": n(F_TOT_SHORT),
        "nonrept_long": n(F_NONREPT_LONG),
        "nonrept_short": n(F_NONREPT_SHORT),
    }

    # GUARD 4 — totals reconciliation. Catches a field shift before any read.
    lhs = d["tot_long"] + d["nonrept_long"]
    rhs = d["tot_short"] + d["nonrept_short"]
    if lhs != d["oi"] or rhs != d["oi"]:
        raise RuntimeError(
            "TOTALS RECONCILIATION FAILED (field mapping suspect — do NOT read positions): "
            f"OI={d['oi']} totlong+nonrept={lhs} totshort+nonrept={rhs}"
        )
    # Legacy reportable identity: TotRept long = NC long + NC spread + Comm long
    if d["nc_long"] + d["nc_spread"] + d["com_long"] != d["tot_long"]:
        raise RuntimeError("reportable-long identity failed — field mapping suspect")

    d["net_nc"] = d["nc_long"] - d["nc_short"]
    d["net_over_oi"] = 100.0 * d["net_nc"] / d["oi"]
    return d


def report(d):
    print(f"  market       : {d['market']}  (code {GOLD_CODE}, FULL-SIZE)")
    print(f"  report date  : {d['report_date']}  (as-of Tuesday, in-row verified)")
    print(f"  open interest: {d['oi']:,}")
    print(f"  NC long      : {d['nc_long']:,}")
    print(f"  NC short     : {d['nc_short']:,}")
    print(f"  NC spreading : {d['nc_spread']:,}")
    print(f"  NET NC long  : {d['net_nc']:,}")
    print(f"  net / OI     : {d['net_over_oi']:.2f}%")
    print(f"  nonreportable: long {d['nonrept_long']:,} / short {d['nonrept_short']:,}")
    print("  [reconciled: OI == TotRept + NonRept on BOTH sides; reportable-long identity OK]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--expect", help="required in-row report date YYYY-MM-DD; exit 3 if stale")
    ap.add_argument("--poll", type=int, default=0, help="seconds between retries (0 = single shot)")
    ap.add_argument("--max-wait", type=int, default=3600)
    a = ap.parse_args()

    waited = 0
    while True:
        try:
            d = extract_gold(fetch())
        except Exception as e:
            print(f"  PULL/PARSE FAILED: {e}", file=sys.stderr)
            if a.poll and waited < a.max_wait:
                time.sleep(a.poll)
                waited += a.poll
                continue
            return 2

        if a.expect and d["report_date"] != a.expect:
            msg = (f"  WAIT — in-row vintage {d['report_date']} != expected {a.expect} "
                   "(stale file served as a clean 200; do NOT grade this)")
            if a.poll and waited < a.max_wait:
                print(f"{msg}  [waited {waited}s]", flush=True)
                time.sleep(a.poll)
                waited += a.poll
                continue
            print(msg, file=sys.stderr)
            report(d)
            return 3

        print("=" * 72)
        print("  CFTC COT — LEGACY FUTURES-ONLY — COMEX GOLD (raw deafut.txt)")
        print("=" * 72)
        report(d)
        return 0


if __name__ == "__main__":
    sys.exit(main())
