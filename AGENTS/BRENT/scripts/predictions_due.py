#!/usr/bin/env python3
"""
Predictions-due scanner — the boot backstop for OPEN predictions whose Timeframe
has passed (or is imminent). Prevents the silent OPEN-but-stale miss (e.g. BRT-09
Q1-Q2 2026 sat unresolved past Q2-close until caught mid-session Jul-1).

Reads thesis/PREDICTIONS.tsv, parses each OPEN row's Timeframe into a best-effort
END date, and flags:
  🔴 DUE     — end date <= today (resolve at closeout: resolve / re-arm / push-date)
  🟠 SOON    — end date within the next 7 days
Event-conditional / open-ended timeframes ("Within X of <event>", "Ongoing") have
no fixed date and are intentionally skipped (their precondition, not a calendar, gates them).

Run standalone or via boot.py. Exit 0 always (informational).
"""
import io
import re
import sys
from datetime import date, timedelta
from pathlib import Path

PRED = Path(__file__).resolve().parent.parent / "thesis" / "PREDICTIONS.tsv"

MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}
Q_END = {1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}


def _last_day(y, m):
    return (date(y + (m // 12), (m % 12) + 1, 1) - timedelta(days=1)).day


def parse_end_date(tf):
    """Best-effort LATEST resolvable end-date from a free-text timeframe. None if none."""
    s = tf.lower()
    cands = []

    # Explicit month day, year  e.g. "By Jul 3 2026", "By Jul 3, 2026"
    for m, d, y in re.findall(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})", s):
        try:
            cands.append(date(int(y), MONTHS[m], min(int(d), _last_day(int(y), MONTHS[m]))))
        except ValueError:
            pass

    # Quarters (incl. ranges "Q1-Q2 2026", "end-Q3 2026") — year attaches to the group
    for ym in re.finditer(r"((?:q[1-4][\s\-–to]*)+)\s*(\d{4})", s):
        yr = int(ym.group(2))
        qs = [int(q) for q in re.findall(r"q([1-4])", ym.group(1))]
        if qs:
            mm, dd = Q_END[max(qs)]
            cands.append(date(yr, mm, dd))

    # Halves "H2 2026", "H1 2027"
    for h, y in re.findall(r"h([12])\s*(\d{4})", s):
        cands.append(date(int(y), 6, 30) if h == "1" else date(int(y), 12, 31))

    # Month range "May-June 2026" / "May–Jun 2026" (no day) -> end of 2nd month
    for m1, m2, y in re.findall(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[\s\-–to]+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(\d{4})", s):
        yr, mm = int(y), MONTHS[m2]
        cands.append(date(yr, mm, _last_day(yr, mm)))

    # Single "Month YYYY" (no day) -> end of month
    for m, y in re.findall(r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(\d{4})", s):
        yr, mm = int(y), MONTHS[m]
        cands.append(date(yr, mm, _last_day(yr, mm)))

    return max(cands) if cands else None


def scan(today=None, debug=False):
    today = today or date.today()
    soon = today + timedelta(days=7)
    due, upcoming = [], []
    with io.open(PRED, "r", encoding="utf-8", newline="\n") as f:
        for ln in f:
            if ln.startswith("#") or ln.startswith("Pred_ID"):
                continue
            fx = ln.rstrip("\n").split("\t")
            if len(fx) < 6 or not fx[0].startswith("BRT-"):
                continue
            pid, tf, status = fx[0], fx[4], fx[5]
            if status != "OPEN":
                continue
            end = parse_end_date(tf)
            if debug:
                print(f"    {pid}: tf={tf!r} -> end={end}")
            if end is None:
                continue
            if end <= today:
                due.append((pid, tf, end))
            elif end <= soon:
                upcoming.append((pid, tf, end))
    return due, upcoming


def main():
    debug = "--debug" in sys.argv
    print("  ⏳ Predictions-Due Scan...")
    due, upcoming = scan(debug=debug)
    if not due and not upcoming:
        print("      ✅ no OPEN predictions past (or within 7d of) their timeframe")
        return 0
    if due:
        print("      🔴 DUE — resolve at closeout (resolve / re-arm-with-reason / push-date-with-reason):")
        for pid, tf, end in due:
            print(f"      🔴 {pid}  (timeframe {tf!r} ended {end})")
    if upcoming:
        print("      🟠 SOON (≤7d) — pre-stage resolution:")
        for pid, tf, end in upcoming:
            print(f"      🟠 {pid}  (timeframe {tf!r} ends {end})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
