#!/usr/bin/env python3
"""Rent Growth band: share of HOMER's frozen 100 cities with negative YoY rent (Apartment List).

Will-ruled 2026-09-29: Apartment List source, levels UNCHANGED Yellow >20% / Orange >40% / Red >55%.
HOMER-computed breadth. Not Apollo's own figure; the levels are retained by Will's judgment, not
calibrated on outcomes (CATO review 2026-09-29, HR1).

Rules enforced here (CATO HR1/HR3):
  - Membership = workbook/RENT_BREADTH_ROSTER.tsv. The file is never re-ranked.
  - A month where any roster city lacks a valid pair (rent now AND rent 12 months earlier) is
    UNGRADED: the count and n are printed, and the denominator is never silently shrunk.
  - Band comparison is on integers: 100*neg > level*n. No float compare (a stored 55.00000000000001
    would falsely pass '> 55').
  - Prints the input file's SHA-256 so each refresh records its vintage.

Usage (from AGENTS/HOMER/):
  python3 tools/rent_breadth.py <Apartment_List_Rent_Estimates_YYYY_MM.csv> [--all]
Input: the city-level CSV from https://www.apartmentlist.com/research/category/data-rent-estimates
"""
import csv, hashlib, os, sys
from decimal import Decimal, InvalidOperation

LEVELS = [("RED", 55), ("ORANGE", 40), ("YELLOW", 20)]
HERE = os.path.dirname(os.path.abspath(__file__))
ROSTER = os.path.join(HERE, "..", "workbook", "RENT_BREADTH_ROSTER.tsv")


def band(neg, n):
    for name, lvl in LEVELS:
        if 100 * neg > lvl * n:
            return name
    return "BELOW-YELLOW"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    show_all = "--all" in sys.argv
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    lines = [l for l in open(ROSTER, encoding="utf-8").read().splitlines() if l and not l.startswith("#")]
    roster = {l.split("\t")[1] for l in lines[1:]}
    assert len(roster) == 100, f"roster has {len(roster)} cities, expected 100"

    rows = {}
    for r in csv.DictReader(open(path, encoding="utf-8")):
        if r["location_type"] == "City" and r["bed_size"] == "overall" and r["location_fips_code"] in roster:
            rows[r["location_fips_code"]] = r
    missing = roster - rows.keys()
    months = [c for c in next(iter(rows.values())).keys() if c[:2] == "20" and "_" in c]

    def val(r, m):
        try:
            v = Decimal(r[m])
            return v if v > 0 else None
        except (InvalidOperation, KeyError, TypeError):
            return None

    print(f"input  {os.path.basename(path)}  sha256 {sha}")
    print(f"roster {len(roster)} cities; found in file {len(rows)}; missing {sorted(missing) or 'none'}")
    out = []
    for i in range(12, len(months)):
        m, prior = months[i], months[i - 12]
        n = neg = 0
        for r in rows.values():
            a, b = val(r, m), val(r, prior)
            if a is not None and b is not None:
                n += 1
                neg += a < b
        grade = band(neg, n) if n == 100 else "UNGRADED (incomplete pairs)"
        out.append((m.replace("_", "-"), neg, n, grade))
    for m, neg, n, g in (out if show_all else out[-13:]):
        print(f"{m}  negative {neg:>3}/{n:<3}  {g}")
    m, neg, n, g = out[-1]
    if n == 100 and g != "RED":
        nxt = next(lvl for name, lvl in reversed(LEVELS) if not 100 * neg > lvl * n)
        need = nxt + 1 - neg
        print(f"LATEST {m}: {neg}/{n} = {g}; next rung >{nxt}% needs {need} more cities")
    else:
        print(f"LATEST {m}: {neg}/{n} = {g}")


if __name__ == "__main__":
    main()
