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
  python3 tools/rent_breadth.py <Apartment_List_Rent_Estimates_YYYY_MM.csv> [--all] [--prior-file=<last month's CSV>]
  Month pairing is BY CALENDAR DATE (same month one year earlier), never by column position;
  a month whose prior column is absent is UNGRADED; the latest month is chosen by date.
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


def month_cols(rows):
    """{(year, month): column name}, parsed from the header, never by position."""
    cols = {}
    for c in next(iter(rows.values())).keys():
        parts = c.split("_")
        if len(parts) == 2 and len(parts[0]) == 4 and parts[0].isdigit() and parts[1].isdigit():
            cols[(int(parts[0]), int(parts[1]))] = c
    return cols


def val(r, col):
    try:
        v = Decimal(r[col])
        return v if v > 0 else None
    except (InvalidOperation, KeyError, TypeError):
        return None


def series(rows, cols):
    """{(y, m): (neg, n, grade)} in calendar order. The prior is the SAME CALENDAR MONTH one
    year earlier, looked up by date. If that column is absent (and it falls inside the file's
    span), the month is UNGRADED, never paired with a neighbour."""
    out, first = {}, min(cols)
    for (y, mo) in sorted(cols):
        prior = (y - 1, mo)
        if prior < first:
            continue  # the file's first year has no prior by construction
        if prior not in cols:
            out[(y, mo)] = (0, 0, f"UNGRADED (no column for {y-1}-{mo:02d})")
            continue
        n = neg = 0
        for r in rows.values():
            a, b = val(r, cols[(y, mo)]), val(r, cols[prior])
            if a is not None and b is not None:
                n += 1
                neg += a < b
        out[(y, mo)] = (neg, n, band(neg, n) if n == 100 else "UNGRADED (incomplete pairs)")
    return out


def load(path, roster):
    rows = {}
    for r in csv.DictReader(open(path, encoding="utf-8")):
        if r["location_type"] == "City" and r["bed_size"] == "overall" and r["location_fips_code"] in roster:
            rows[r["location_fips_code"]] = r
    return rows


def gaps(cols):
    (y0, m0), (y1, m1) = min(cols), max(cols)
    miss, y, m = [], y0, m0
    while (y, m) <= (y1, m1):
        if (y, m) not in cols:
            miss.append(f"{y}-{m:02d}")
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return miss


def lab(k):
    return f"{k[0]}-{k[1]:02d}"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    path = args[0]
    show_all = "--all" in sys.argv
    prior_file = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--prior-file=")), None)
    lines = [l for l in open(ROSTER, encoding="utf-8").read().splitlines() if l and not l.startswith("#")]
    roster = {l.split("\t")[1] for l in lines[1:]}
    assert len(roster) == 100, f"roster has {len(roster)} cities, expected 100"

    rows = load(path, roster)
    cols = month_cols(rows)
    print(f"input  {os.path.basename(path)}  sha256 {hashlib.sha256(open(path, 'rb').read()).hexdigest()}")
    print(f"roster {len(roster)} cities; found in file {len(rows)}; missing {sorted(roster - rows.keys()) or 'none'}")
    g = gaps(cols)
    print(f"calendar span {lab(min(cols))} .. {lab(max(cols))}; months ABSENT from file: {g or 'none'}")
    out = series(rows, cols)
    keys = sorted(out)
    for k in (keys if show_all else keys[-13:]):
        neg, n, gr = out[k]
        print(f"{lab(k)}  negative {neg:>3}/{n:<3}  {gr}")

    latest = max(cols)  # latest month BY DATE, not the last column
    if latest not in out:
        print(f"LATEST {lab(latest)}: UNGRADED (no prior-year column)")
    else:
        neg, n, gr = out[latest]
        if n == 100 and gr not in ("RED",) and not gr.startswith("UNGRADED"):
            nxt = next(lvl for name, lvl in reversed(LEVELS) if not 100 * neg > lvl * n)
            print(f"LATEST {lab(latest)}: {neg}/{n} = {gr}; next rung >{nxt}% needs {nxt + 1 - neg} more cities")
        else:
            print(f"LATEST {lab(latest)}: {neg}/{n} = {gr}")

    if prior_file:
        # Apartment List revises history: compare every month present in BOTH files.
        prows = load(prior_file, roster)
        pout = series(prows, month_cols(prows))
        both = sorted(set(out) & set(pout))
        rev = [(k, pout[k], out[k]) for k in both if pout[k][:2] != out[k][:2]]
        print(f"REVISIONS vs {os.path.basename(prior_file)}: {len(both)} months in both files, {len(rev)} changed")
        for k, o, nw in rev:
            print(f"  {lab(k)}  {o[0]}/{o[1]} {o[2]}  ->  {nw[0]}/{nw[1]} {nw[2]}")


if __name__ == "__main__":
    main()
