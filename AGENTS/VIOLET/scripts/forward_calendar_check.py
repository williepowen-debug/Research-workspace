#!/usr/bin/env python3
"""VIOLET forward-calendar coverage check — the L667 tooling rider (built 2026-10-21).

WHY THIS EXISTS (KB-VIO-324, DOCKET L667)
-----------------------------------------
From 2026-09-30 to 2026-10-09 `workbook/CATALYSTS.tsv` carried no HIGH or MEDIUM
row (one October 7 LOW checkpoint existed), while the cheap-tail alert read OPEN
on 10/02 and 10/05-10/08 with nowhere to route. The countdown printed an empty
table, which looked like a calm calendar. Missing calendar coverage is not
market calm.

Will, 2026-10-10 13:45 ET (via PROME's packet): a boot-only warning only this
desk can see is not enough. So the OUTPUT of an empty window is a packet in
`PROME/inbox/` asking for a DOCKET row (or a calendar row), not a local line.
PROME's boot gate separately flags EMPTY-FORWARD for a desk that never boots;
this script is the desk-side half.

RULE
----
At least one HIGH or MEDIUM row dated in (as_of, as_of + window] (calendar days,
default 14). A row dated as_of itself does not count: it is due, not forward.
A LOW row does not count (PROME's gate is an any-row check; this one is
deliberately stricter).

Exit codes: 0 = covered · 1 = EMPTY-FORWARD (packet written or already present)
· 2 = UNKNOWN (calendar missing/unreadable, or a row date that will not parse).

Self-test (one line):
  .venv/bin/python3 -m unittest AGENTS/VIOLET/scripts/tests/test_forward_calendar_check.py

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/forward_calendar_check.py
  ... --as-of 2026-10-21 --window 14 --catalysts-file F --inbox-dir D --no-packet
"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
WORKSPACE = VIOLET_DIR.parent.parent
CATALYSTS = VIOLET_DIR / "workbook" / "CATALYSTS.tsv"
PROME_INBOX = WORKSPACE / "PROME" / "inbox"
COUNTED = {"HIGH", "MEDIUM", "MED"}
IMPACT_COLUMNS = ("expected_vol_impact", "impact")


def today_et() -> date:
    if ZoneInfo is not None:
        return datetime.now(ZoneInfo("America/New_York")).date()
    return date.today()


def load_rows(path: Path) -> list[dict]:
    with path.open(newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if rows and not any(c in rows[0] for c in IMPACT_COLUMNS):
        raise ValueError(f"no impact column ({' / '.join(IMPACT_COLUMNS)}) in {path}")
    return rows


def forward_rows(rows: list[dict], as_of: date, window: int) -> tuple[list[tuple[date, str, str]], list[str]]:
    hits, bad = [], []
    end = as_of + timedelta(days=window)
    for r in rows:
        raw = (r.get("date") or "").strip()
        try:
            d = date.fromisoformat(raw[:10])
        except ValueError:
            bad.append(raw or "<blank>")
            continue
        impact = next(((r.get(c) or "").strip().upper() for c in IMPACT_COLUMNS if r.get(c)), "")
        if impact in COUNTED and as_of < d <= end:
            hits.append((d, impact, (r.get("event") or "").strip()))
    return sorted(hits), bad


def packet_text(as_of: date, window: int, path: Path) -> str:
    end = as_of + timedelta(days=window)
    return (
        f"# VIOLET -> PROME — EMPTY-FORWARD: no HIGH/MEDIUM catalyst row {as_of + timedelta(days=1)}..{end}\n\n"
        f"**Written by:** `AGENTS/VIOLET/scripts/forward_calendar_check.py` (DOCKET L667 tooling rider), "
        f"as-of {as_of}, window {window} calendar days.\n\n"
        f"`{path}` has no HIGH or MEDIUM row in that window. Missing calendar coverage is not market "
        f"calm (KB-VIO-324: the 9/30-10/09 gap, cheap-tail OPEN with no route).\n\n"
        f"ACTION (PROME): register a DOCKET row naming VIOLET dated on or before {end} so the desk is woken "
        f"to re-populate its calendar, unless a VIOLET calendar row lands first.\n"
        f"ACTION (VIOLET, next session): add the dated HIGH/MEDIUM rows (FOMC, CPI, NFP, VIX expiry, "
        f"BOJ) to workbook/CATALYSTS.tsv and CALENDAR.md, then commit this packet (carve-out 1).\n"
        f"ASK: none. $0.\n"
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--as-of", type=date.fromisoformat, default=None)
    ap.add_argument("--window", type=int, default=14)
    ap.add_argument("--catalysts-file", type=Path, default=CATALYSTS)
    ap.add_argument("--inbox-dir", type=Path, default=PROME_INBOX)
    ap.add_argument("--no-packet", action="store_true", help="report only; never write the PROME packet")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)
    as_of = a.as_of or today_et()

    try:
        rows = load_rows(a.catalysts_file)
        hits, bad = forward_rows(rows, as_of, a.window)
    except (OSError, ValueError, csv.Error) as e:
        print(f"🔴 FORWARD CALENDAR UNKNOWN — cannot read {a.catalysts_file}: {e}. An unread calendar is not a covered one.")
        return 2
    if bad:
        print(f"🔴 FORWARD CALENDAR UNKNOWN — {len(bad)} row date(s) do not parse: {', '.join(bad[:5])}")
        return 2

    end = as_of + timedelta(days=a.window)
    if hits:
        if not a.quiet:
            first = hits[0]
            print(f"✓ FORWARD CALENDAR — {len(hits)} HIGH/MED row(s) in ({as_of}, {end}]; "
                  f"first {first[0]} {first[1]} {first[2][:60]}")
        return 0

    msg = f"🔴 EMPTY-FORWARD — no HIGH/MED row in ({as_of}, {end}] of {a.catalysts_file.name}."
    if a.no_packet:
        print(msg + " (--no-packet: PROME packet NOT written)")
        return 1
    pkt = a.inbox_dir / f"{as_of}_from-VIOLET_EMPTY-FORWARD-calendar.md"
    if pkt.exists():
        print(msg + f" Packet already present: {pkt}")
    else:
        a.inbox_dir.mkdir(parents=True, exist_ok=True)
        pkt.write_text(packet_text(as_of, a.window, a.catalysts_file))
        print(msg + f" ⚠️ Packet WRITTEN: {pkt} — commit it at closeout (carve-out 1).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
