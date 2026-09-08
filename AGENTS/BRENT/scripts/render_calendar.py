#!/usr/bin/env python3
"""Render the STATUS.md § CATALYST CALENDAR from docket/CATALYSTS.tsv.

DAEDALUS architecture review ACTION 8 (Will-approved 2026-09-07). supersedes: the HAND-EDITED
STATUS calendar table, and the twin-diff that policed it — a twin-diff is a MIGRATION
instrument and retires when this generator lands (the packet says so in terms).

⛔ WHY A GENERATOR AND NOT A BETTER HABIT. The calendar and CATALYSTS.tsv were declared
"HUMAN TWIN ... must not diverge in event SET" on 2026-08-10. Measured 2026-09-07, they had
diverged in BOTH directions:
    MISSING from STATUS : 2026-09-04 · 2026-09-08 (IMMINENT, next day) · 2026-09-18
                          (the USO 150/165 EXPIRY — a dated capital event) · 2026-10-04
    STALE in STATUS     : ~7 fired August rows CATALYSTS had already pruned under its own
                          1-week retention.
A rule that says "must not diverge" is not a mechanism. One record, two renders, regenerated
at closeout, is. [[finding_a_ruling_governs_the_next_write_not_the_existing_state]]

★ AND IT IS GRADE-BEARING: the dated demote trigger (record §4) names "twin calendar event
set" disagreement at the cycle closing the 9/11 Friday pair -> L4 at PR#6.

Modes:
  --check   fail-closed. rc=1 if STATUS's rendered block differs from what CATALYSTS implies.
            Use at closeout. A generator nobody verifies is a hand-edited file with extra steps.
  --write   rewrite the block in STATUS.md in place.
  (default) print the rendered block to stdout.

⚠️ SCOPE: renders the EVENT SET and its dates from the canonical record. It does NOT invent
priority glyphs or prose — those come from CATALYSTS' own columns. The TRADE.md catalysts
table is the second render and is NOT yet wired (P2); until it is, it stays hand-maintained
and is the remaining divergence risk. Stated so the gap is not mistaken for covered.
"""
import csv
import io
import re
import sys
from datetime import datetime
from pathlib import Path

BRENT = Path(__file__).resolve().parent.parent
CAT = BRENT / "docket" / "CATALYSTS.tsv"
STATUS = BRENT / "STATUS.md"

BEGIN = "<!-- CALENDAR:BEGIN generated from docket/CATALYSTS.tsv — do not hand-edit -->"
END = "<!-- CALENDAR:END -->"


def load():
    rows = []
    with io.open(CAT, encoding="utf-8", newline="") as f:
        for r in csv.reader(f, delimiter="\t"):
            if not r or not r[0].strip() or r[0].lstrip().startswith("#"):
                continue
            if r[0].strip().lower() == "date":
                continue
            date_s = r[0].strip()
            approx = date_s.startswith("~")
            core = date_s.lstrip("~")
            try:
                d = datetime.strptime(core, "%Y-%m-%d").date()
            except ValueError:
                continue
            event = (r[1].strip() if len(r) > 1 else "")
            pri = (r[4].strip() if len(r) > 4 else "")
            rows.append((d, approx, event, pri))
    rows.sort(key=lambda x: x[0])
    return rows


def render():
    rows = load()
    out = [BEGIN,
           "",
           "| Date | Release | Priority |",
           "|------|---------|----------|"]
    for d, approx, event, pri in rows:
        # ONE LINE PER EVENT, text from the record. Long graded text is NOT restated here —
        # the row points at CATALYSTS, which is canonical for the full grade.
        text = re.sub(r"\s+", " ", event).strip()
        if len(text) > 190:
            text = text[:187].rstrip() + "…"
        stamp = ("~" if approx else "") + d.strftime("%a %b %-d").replace(" 0", " ")
        out.append(f"| **{stamp}** | {text} | {pri or ''} |")
    out += ["",
            f"*{len(rows)} event(s), generated from `docket/CATALYSTS.tsv` — the canonical "
            f"forward-state record. Full graded text lives there and is deliberately not "
            f"restated. Regenerate with `scripts/render_calendar.py --write`; verify with "
            f"`--check` at closeout.*",
            "",
            END]
    return "\n".join(out)


def current_block(text):
    if BEGIN not in text or END not in text:
        return None
    a = text.index(BEGIN)
    b = text.index(END) + len(END)
    return text[a:b]


def main():
    block = render()
    if "--write" in sys.argv:
        t = STATUS.read_text(encoding="utf-8")
        cur = current_block(t)
        if cur is None:
            print("no CALENDAR:BEGIN/END markers in STATUS.md — insert them first", file=sys.stderr)
            return 1
        STATUS.write_text(t.replace(cur, block), encoding="utf-8")
        print(f"calendar rewritten from {CAT.name}")
        return 0
    if "--check" in sys.argv:
        t = STATUS.read_text(encoding="utf-8")
        cur = current_block(t)
        if cur is None:
            print("🔴 CALENDAR: no generated block in STATUS.md — the twin is hand-edited again")
            return 1
        if cur.strip() != block.strip():
            print("🔴 CALENDAR DRIFT: STATUS's block != render(docket/CATALYSTS.tsv). "
                  "Run --write. (Never hand-fix: the record is the source.)")
            return 1
        n = block.count("\n| **")
        print(f"✅ CALENDAR: STATUS block matches docket/CATALYSTS.tsv ({n} events)")
        return 0
    print(block)
    return 0


if __name__ == "__main__":
    sys.exit(main())
