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
            # ⛔ date_class ADDED 2026-09-07 (CODEX P1 verification). The first version of this
            # renderer read the date and DROPPED this column, so all 6 `modeled` rows — incl.
            # 2026-09-08 and 2026-09-09, both imminent — rendered identically to `confirmed`
            # ones. The hand table it replaced HAD carried a `~` marker.
            # ★ A GENERATED VIEW THAT AGREES WITH ITS RECORD CAN STILL BE WRONG: --check
            # compared render-to-render and passed, because both sides had already lost the
            # column. Matching generated text is not sufficient if GENERATION drops information
            # — the check can only see what the renderer chose to look at.
            # [[finding_output_shape_implies_more_than_the_measurement]]
            dclass = (r[7].strip().lower() if len(r) > 7 else "")
            rows.append((d, approx or dclass == "modeled", event, pri, dclass))
    rows.sort(key=lambda x: x[0])
    return rows


def render():
    rows = load()
    out = [BEGIN,
           "",
           "| Date | Release | Priority |",
           "|------|---------|----------|"]
    for d, approx, event, pri, dclass in rows:
        # ONE LINE PER EVENT, text from the record. Long graded text is NOT restated here —
        # the row points at CATALYSTS, which is canonical for the full grade.
        text = re.sub(r"\s+", " ", event).strip()
        if len(text) > 190:
            text = text[:187].rstrip() + "…"
        stamp = ("~" if approx else "") + d.strftime("%a %b %-d").replace(" 0", " ")
        mark = " ⌁*modeled*" if dclass == "modeled" else ""
        out.append(f"| **{stamp}**{mark} | {text} | {pri or ''} |")
    nmod = sum(1 for r in rows if r[4] == "modeled")
    out += ["",
            f"*`~` + ⌁*modeled* = `date_class=modeled` in the record: a PROJECTED date, not a "
            f"published one — do not grade a row against a modeled date as though it were "
            f"confirmed. {nmod} of {len(rows)} rows are modeled.*",
            "",
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


RECONCILED_RE = re.compile(r"✓ \*\*reconciled `(\d{4}-\d{2}-\d{2})`")


def check_standing():
    """Acceptance test ③, second half: do STANDING STATE values agree with their records?

    ⛔ WHY THIS EXISTS (CODEX P1 verification, 2026-09-07). The P1 rotation left the BRT-26
    ladder at its 8/28 vintage (447 rigs, distance 10, 4 prints) and the COT-FUEL-35B base at
    the TRUNCATED `122,904` — while the canonical records carried 449/8/3 and `122,904.5`,
    corrected at the 9/6 grade. Rotation therefore moved the FRESHER value to the cold file and
    left the STALER one hot: the hot surface became the least current.

    ★ AND MY OWN ③ CHECK PASSED OVER IT, which is the part worth keeping: I verified the two
    things I had just fixed (calendar agreement, version pointer) and reported "③ AGREEMENT ✅".
    A check scoped to what you just changed cannot find what you did not.
    [[finding_gate_pass_is_not_evidence_it_found_the_best_reason]]

    Mechanism: every STANDING STATE row carries TWO different dates and they are NOT
    interchangeable:
        as-of      = the DATA VINTAGE the value describes (COT vintage #4 is legitimately
                     as-of 9/1 and does not become stale by the calendar turning).
        reconciled = when a human last CHECKED this row against its canonical record.
    The check reads `reconciled` ONLY. Comparing `as-of` against grade dates was the first
    version of this guard and it fired a FALSE POSITIVE immediately: it flagged a correctly-
    current COT row because the 9/4 catalyst that GRADED the 9/1 vintage post-dated the
    vintage. A guard that compares two different units produces confident nonsense.
    [[finding_level_and_rate_look_like_agreement_until_you_name_which]]

    A GRADED catalyst dated after `reconciled` means a print has landed since anyone last
    verified the row: not proven wrong, proven UNVERIFIED — the state that must never be
    silent. Flags for review; never auto-edits (a standing value is a judgement, not a render).
    """
    t = STATUS.read_text(encoding="utf-8")
    stamps = RECONCILED_RE.findall(t)
    if not stamps:
        print("🔴 STANDING STATE: no `✓ reconciled` stamps found — the freshness check is INERT. "
              "Every standing row must carry one, or this guard silently certifies nothing.")
        return 1
    oldest = min(datetime.strptime(x, "%Y-%m-%d").date() for x in stamps)
    graded = []
    for d, approx, event, pri, dclass in load():
        if re.search(r"\bGRADED\b|\bFIRED\b", event, re.IGNORECASE):
            graded.append(d)
    newer = sorted(x for x in graded if x > oldest)
    if newer:
        print(f"🟠 STANDING STATE may be BEHIND: oldest `reconciled` stamp is {oldest}, but "
              f"{len(newer)} graded catalyst(s) are dated after it "
              f"({', '.join(str(x) for x in newer[-3:])}). "
              f"⇒ RE-READ each standing row against its canonical record and re-stamp. "
              f"NOT auto-fixed: a standing value is a judgement, not a render.")
        return 2
    print(f"✅ STANDING STATE: {len(stamps)} stamped row(s), oldest as-of {oldest}; "
          f"no graded catalyst is newer.")
    return 0


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
        return check_standing()
    print(block)
    return 0


if __name__ == "__main__":
    sys.exit(main())
