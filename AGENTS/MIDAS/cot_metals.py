#!/usr/bin/env python3
"""
MIDAS — CFTC COT metals puller (LEGACY futures-only): SILVER, PLATINUM, PALLADIUM.
Release-day safe. stdlib only (so a boot leg can import it without .venv).

WHY THIS FILE EXISTS (Will, 2026-09-25): silver, platinum and palladium are
first-class coverage alongside gold. Until now MIDAS had positioning for GOLD
only (cot_gold.py). This is the same instrument, same raw file, same guards,
generalised over a fixed CODE TABLE. Gold is in the table ONLY so this code path
can be cross-checked against cot_gold.py on the same vintage — gold's canonical
puller STAYS cot_gold.py (boot.py leg 3 imports it; do not repoint it here
without a deliberate decision).

WHY A RAW-FILE PULLER AND NOT SOCRATA (auto-memory
`finding_cftc_cot_raw_file_beats_socrata_lag`, inherited from cot_gold.py):
  - Socrata lags the 15:30 ET post by ~15-60+ min; the RAW file itself lagged
    ~20 min on 2026-08-07. Both serve a clean 200 carrying LAST week's vintage.
  - => NEVER grade the first response after 15:30. `--expect YYYY-MM-DD` exits 3
    (WAIT) if ANY requested metal's in-row date differs.

GUARDS (each one bought by a real defect — same five as cot_gold.py):
  1. CODE-KEYED extraction, not name-keyed. Contract names get relabeled (the
     WTI "CRUDE OIL, LIGHT SWEET" -> "WTI-PHYSICAL" precedent). Codes verified
     in the live deafut.txt 2026-09-25 (vintage 2026-09-15):
        silver    084691  "SILVER - COMMODITY EXCHANGE INC."
        platinum  076651  "PLATINUM - NEW YORK MERCANTILE EXCHANGE"
        palladium 075651  "PALLADIUM - NEW YORK MERCANTILE EXCHANGE"
        gold      088691  "GOLD - COMMODITY EXCHANGE INC."  (cross-check only)
     The name for each code must EQUAL the expected string (not merely contain
     it: "MICRO GOLD - COMMODITY EXCHANGE INC." CONTAINS the gold string). A
     relabel fails loud — investigate, then update the table deliberately.
  2. csv module, NOT naive comma-split — quoted market names contain commas and
     shift every field by +1.
  3. EXACT full-size contract only: exactly ONE row per code, else fail. A
     `like '%GOLD%'` filter mixed in MICRO GOLD and corrupted 6 of 15 weeks on
     MIDAS's first gold pull (2026-08-07, KB-036). Micro/mini variants carry
     DIFFERENT codes and are never read.
  4. TOTALS RECONCILIATION before any position number is read:
     OI == TotRept_long + NonRept_long, and == TotRept_short + NonRept_short;
     plus the reportable identities TotRept_long == NC_long + NC_spread +
     Comm_long and TotRept_short == NC_short + NC_spread + Comm_short.
     (cot_gold.py checks the long identity only; the short one is added here.)
     Fails loud (`finding_fail_loud_on_incomplete_data`).
  5. In-row report-date verification (`--expect`), per metal. Additionally all
     requested metals must share ONE in-row date — a mixed-vintage print is a
     parse failure (exit 2), never a table.

Exit codes: 0 ok · 2 pull/parse/guard failure · 3 WAIT (stale vintage vs --expect).

Usage:
  python3 cot_metals.py                         # silver, platinum, palladium
  python3 cot_metals.py --metal silver          # one metal (also: gold, for cross-check)
  python3 cot_metals.py --expect 2026-09-22     # exit 3 (WAIT) unless every in-row date matches
  python3 cot_metals.py --expect 2026-09-22 --poll 60 --max-wait 3600
  python3 cot_metals.py --tsv                   # machine rows (header + one row per metal)
  python3 cot_metals.py --file deafut.txt       # read a local copy instead of fetching (tests)

Importable:
  import cot_metals
  rows = cot_metals.parse(cot_metals.fetch())
  d = cot_metals.extract(rows, "silver")       # dict, same keys as cot_gold.extract_gold
"""
import argparse
import csv
from datetime import date, datetime
import io
import sys
import time
import urllib.request

URL = "https://www.cftc.gov/dea/newcot/deafut.txt"
UA = "Mozilla/5.0 (research; MIDAS metals agent; contact via repo)"  # 403 w/o a UA

# metal -> (CFTC contract market code, EXACT expected market name). Full-size only.
CONTRACTS = {
    "silver":    ("084691", "SILVER - COMMODITY EXCHANGE INC."),
    "platinum":  ("076651", "PLATINUM - NEW YORK MERCANTILE EXCHANGE"),
    "palladium": ("075651", "PALLADIUM - NEW YORK MERCANTILE EXCHANGE"),
    "gold":      ("088691", "GOLD - COMMODITY EXCHANGE INC."),  # cross-check vs cot_gold.py
}
DEFAULT_METALS = ("silver", "platinum", "palladium")

# Legacy futures-only short-format field indices (identical to cot_gold.py).
F_NAME, F_DATE_YMD, F_CODE = 0, 2, 3
F_OI = 7
F_NC_LONG, F_NC_SHORT, F_NC_SPREAD = 8, 9, 10
F_COM_LONG, F_COM_SHORT = 11, 12
F_TOT_LONG, F_TOT_SHORT = 13, 14
F_NONREPT_LONG, F_NONREPT_SHORT = 15, 16

TSV_HEADER = ("report_date", "metal", "code", "open_interest", "nc_long", "nc_short",
              "net_nc_long", "net_over_oi_pct")


def fetch(url=URL):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        if r.status != 200:
            raise RuntimeError(f"HTTP {r.status} from {url}")
        return r.read().decode("utf-8", errors="replace")


def parse(text):
    """GUARD 2 — csv module, never a comma split."""
    return list(csv.reader(io.StringIO(text)))


def extract(rows, metal):
    """Code-keyed extraction + name guard + totals reconciliation for one metal.
    `rows` = csv rows (list of lists) from parse(). Returns dict or raises."""
    if metal not in CONTRACTS:
        raise ValueError(f"unknown metal {metal!r}; choose from {sorted(CONTRACTS)}")
    code, name_expect = CONTRACTS[metal]

    # GUARDS 1+3 — code-keyed, exactly one full-size row.
    hits = [r for r in rows if len(r) > F_NONREPT_SHORT and r[F_CODE].strip() == code]
    if len(hits) != 1:
        raise RuntimeError(
            f"{metal}: expected exactly 1 row for contract code {code}, got {len(hits)} "
            "(guard 1/3: code-keyed, full-size only)"
        )
    r = hits[0]
    name = r[F_NAME].strip()
    if name.upper() != name_expect:
        raise RuntimeError(
            f"{metal}: code {code} resolved to unexpected name {name!r} "
            f"(expected exactly {name_expect!r}) — relabel or wrong contract; investigate"
        )

    def n(i):
        return int(float(r[i].strip()))

    d = {
        "metal": metal,
        "code": code,
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
            f"{metal}: TOTALS RECONCILIATION FAILED (field mapping suspect — do NOT read "
            f"positions): OI={d['oi']} totlong+nonrept={lhs} totshort+nonrept={rhs}"
        )
    if d["nc_long"] + d["nc_spread"] + d["com_long"] != d["tot_long"]:
        raise RuntimeError(f"{metal}: reportable-long identity failed — field mapping suspect")
    if d["nc_short"] + d["nc_spread"] + d["com_short"] != d["tot_short"]:
        raise RuntimeError(f"{metal}: reportable-short identity failed — field mapping suspect")

    try:
        datetime.strptime(d["report_date"], "%Y-%m-%d")
    except ValueError:
        raise RuntimeError(f"{metal}: in-row report date unparseable: {d['report_date']!r}")

    d["net_nc"] = d["nc_long"] - d["nc_short"]
    d["net_over_oi"] = 100.0 * d["net_nc"] / d["oi"]
    return d


def extract_all(rows, metals=DEFAULT_METALS):
    """Extract several metals; GUARD 5b — they must share ONE in-row date."""
    out = [extract(rows, m) for m in metals]
    dates = {d["report_date"] for d in out}
    if len(dates) != 1:
        raise RuntimeError(
            "MIXED VINTAGES across metals (do NOT read as one table): "
            + ", ".join(f"{d['metal']}={d['report_date']}" for d in out)
        )
    return out


def report(d, verified=False):
    """verified=True ONLY when --expect ran and MATCHED (PAT-074: no green words
    for a check that never ran). The reconciliation line is unconditional and
    that is correct: the guards raise on failure, so reaching here IS the pass."""
    print(f"  --- {d['metal'].upper()} ---")
    print(f"  market       : {d['market']}  (code {d['code']}, FULL-SIZE)")
    stamp = ("as-of Tuesday, in-row verified" if verified
             else "as-of Tuesday, UNVERIFIED — pass --expect YYYY-MM-DD to check")
    print(f"  report date  : {d['report_date']}  ({stamp})")
    try:
        age = (date.today() - datetime.strptime(d["report_date"], "%Y-%m-%d").date()).days
        flag = "  ⚠️ OLDER THAN A NORMAL WEEKLY CYCLE" if age > 10 else ""
        print(f"  in-row age   : {age}d before today{flag}")
    except Exception:  # noqa: BLE001
        print("  in-row age   : UNCOMPUTABLE (report_date unparseable)")
    print(f"  open interest: {d['oi']:,}")
    print(f"  NC long      : {d['nc_long']:,}")
    print(f"  NC short     : {d['nc_short']:,}")
    print(f"  NC spreading : {d['nc_spread']:,}")
    print(f"  NET NC long  : {d['net_nc']:,}")
    print(f"  net / OI     : {d['net_over_oi']:.2f}%")
    print(f"  nonreportable: long {d['nonrept_long']:,} / short {d['nonrept_short']:,}")
    print("  [reconciled: OI == TotRept + NonRept on BOTH sides; reportable long+short identities OK]")


def tsv_row(d):
    return "\t".join([d["report_date"], d["metal"], d["code"], str(d["oi"]), str(d["nc_long"]),
                      str(d["nc_short"]), str(d["net_nc"]), f"{d['net_over_oi']:.4f}"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--metal", choices=sorted(CONTRACTS),
                    help="one metal (default: silver, platinum, palladium; gold = cross-check)")
    ap.add_argument("--expect", help="required in-row report date YYYY-MM-DD; exit 3 if stale")
    ap.add_argument("--tsv", action="store_true", help="machine rows instead of the report")
    ap.add_argument("--file", help="read a local deafut.txt copy instead of fetching")
    ap.add_argument("--poll", type=int, default=0, help="seconds between retries (0 = single shot)")
    ap.add_argument("--max-wait", type=int, default=3600)
    a = ap.parse_args()
    metals = (a.metal,) if a.metal else DEFAULT_METALS

    waited = 0
    while True:
        try:
            if a.file:
                with open(a.file, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
            else:
                text = fetch()
            ds = extract_all(parse(text), metals)
        except Exception as e:  # noqa: BLE001
            print(f"  PULL/PARSE FAILED: {e}", file=sys.stderr)
            if a.poll and waited < a.max_wait and not a.file:
                time.sleep(a.poll)
                waited += a.poll
                continue
            return 2

        stale = [d for d in ds if a.expect and d["report_date"] != a.expect]
        if stale:
            msg = ("  WAIT — in-row vintage "
                   + ", ".join(f"{d['metal']}={d['report_date']}" for d in stale)
                   + f" != expected {a.expect} (stale file served as a clean 200; do NOT grade this)")
            if a.poll and waited < a.max_wait and not a.file:
                print(f"{msg}  [waited {waited}s]", flush=True)
                time.sleep(a.poll)
                waited += a.poll
                continue
            print(msg, file=sys.stderr)
            if not a.tsv:
                for d in ds:
                    report(d, verified=False)  # mismatch: the check ran and FAILED
            return 3

        if a.tsv:
            print("\t".join(TSV_HEADER))
            for d in ds:
                print(tsv_row(d))
            return 0

        print("=" * 72)
        print("  CFTC COT — LEGACY FUTURES-ONLY — " + " / ".join(m.upper() for m in metals)
              + " (raw deafut.txt)")
        print("=" * 72)
        for d in ds:
            report(d, verified=bool(a.expect))  # True only if --expect ran and matched
        return 0


if __name__ == "__main__":
    sys.exit(main())
