#!/usr/bin/env python3
"""HOMER boot-time threshold scan — reads registry/THRESHOLDS.tsv and grades each reading cell.

Built 2026-10-28 (Will-approved; pattern from CREED/scripts/threshold_scan.py).

What it does, per band row:
  * compares the reading to Yellow/Orange/Red with EXACT decimals (never float) — rent breadth
    as integers 100*neg > level*n — honouring the row's comparator ('>' or '<');
  * reports the HIGHEST UNCROSSED rung and the distance to it (CLAUDE.md reporting rule), or
    "NO UNCROSSED RUNG" with the distance past the top;
  * flags STALE (data period older than max_age_days), UNGRADED (native instrument did not
    print) and NEAR (within near_margin of the next rung).

What it refuses to do:
  * It never prints "all clear". Every row is printed every run; a band with no flag is still
    only as current as its reading cell, which a session wrote by hand from a ledger row.
  * It is not an adjudicator. A flag means "go read the primary and the ledger", not a grade.
  * Malformed rows FAIL CLOSED: the row prints as BROKEN and the exit code is 2.

Usage: python3 tools/threshold_scan.py [--today=YYYY-MM-DD] [--file=path]
Exit: 0 = no STALE/UNGRADED/NEAR/BROKEN rows · 1 = at least one flag · 2 = a BROKEN row or unreadable file.
"""
import datetime
import os
import sys
from decimal import Decimal, InvalidOperation

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT = os.path.join(HERE, "registry", "THRESHOLDS.tsv")
REQUIRED = ["band_id", "metric", "comparator", "yellow", "orange", "red", "value_unit",
            "max_age_days", "near_margin", "reading", "reading_as_of", "reading_source"]
RUNGS = ["YELLOW", "ORANGE", "RED"]


def crossed(value, level, comp):
    return value > level if comp == ">" else value < level


def grade(row):
    """Return (state, detail, flags). Raises ValueError on malformed cells."""
    comp = row["comparator"]
    if comp not in (">", "<"):
        raise ValueError(f"comparator {comp!r} not '>' or '<'")
    levels = [Decimal(row[k]) for k in ("yellow", "orange", "red")]
    if comp == ">" and not levels[0] < levels[1] < levels[2]:
        raise ValueError("levels not increasing for '>'")
    if comp == "<" and not levels[0] > levels[1] > levels[2]:
        raise ValueError("levels not decreasing for '<'")
    near = Decimal(row["near_margin"])
    reading = row["reading"].strip()
    if reading.upper() == "UNGRADED":
        return "UNGRADED", "native instrument did not print — not calm", ["UNGRADED"]
    if row["value_unit"] == "count_of_n":
        neg, n = reading.split("/")
        neg, n = int(neg), int(n)
        if n <= 0 or not 0 <= neg <= n:
            raise ValueError("count_of_n out of range")
        hits = [100 * neg > lv * n for lv in levels]   # integer compare, exact
        value = Decimal(100 * neg) / Decimal(n)          # display only
    else:
        value = Decimal(reading)
        hits = [crossed(value, lv, comp) for lv in levels]
    if hits != sorted(hits, reverse=True):
        raise ValueError("rung crossing not monotone")
    n_crossed = sum(hits)
    band = RUNGS[n_crossed - 1] if n_crossed else "BELOW-YELLOW"
    flags = []
    if n_crossed == 3:
        dist = abs(value - levels[2])
        return band, f"NO UNCROSSED RUNG — {dist} {row['value_unit']} past Red; the ladder carries no information upward", flags
    nxt = levels[n_crossed]
    dist = abs(nxt - value)
    if dist <= near:
        flags.append("NEAR")
    return band, f"next uncrossed = {RUNGS[n_crossed]} ({comp}{nxt}), {dist} {row['value_unit']} away", flags


def main():
    today = datetime.date.today()
    path = DEFAULT
    for a in sys.argv[1:]:
        if a.startswith("--today="):
            today = datetime.date.fromisoformat(a.split("=", 1)[1])
        elif a.startswith("--file="):
            path = a.split("=", 1)[1]
    try:
        lines = [l.rstrip("\n") for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    except OSError as e:
        print(f"BROKEN: cannot read {path}: {e}")
        return 2
    header = lines[0].split("\t")
    missing = [c for c in REQUIRED if c not in header]
    if missing:
        print(f"BROKEN: header missing {missing}")
        return 2
    worst, counts = 0, {}
    print(f"HOMER threshold scan — {path} — today {today} — {len(lines) - 1} band rows")
    for raw in lines[1:]:
        cells = raw.split("\t")
        bid = cells[0] if cells else "?"
        if len(cells) != len(header):
            print(f"  {bid:6} BROKEN  column count {len(cells)} != {len(header)}")
            worst = 2; counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            continue
        row = dict(zip(header, cells))
        try:
            band, detail, flags = grade(row)
            as_of = datetime.date.fromisoformat(row["reading_as_of"])
            age = (today - as_of).days
            if age > int(row["max_age_days"]):
                flags.append(f"STALE({age}d>{row['max_age_days']}d)")
        except (ValueError, InvalidOperation, KeyError) as e:
            print(f"  {bid:6} BROKEN  {row.get('metric', '?')}: {e}")
            worst = 2; counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            continue
        for f in flags:
            key = f.split("(")[0]
            counts[key] = counts.get(key, 0) + 1
        if flags:
            worst = max(worst, 1)
        print(f"  {bid:6} {band:12} {row['metric']}: {row['reading']} [{row['reading_as_of']}] — {detail}"
              + (f"  ⚑ {' '.join(flags)}" if flags else ""))
    summary = ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "no flags"
    print(f"SUMMARY: {summary}. Not an all-clear: each row is only as current as its reading cell; "
          f"ledgers are the record.")
    return worst


if __name__ == "__main__":
    sys.exit(main())
