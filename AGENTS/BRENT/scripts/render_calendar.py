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
# "GRADED 2026-09-06" / "graded 2026-09-06" inside a catalyst's own text.
GRADED_RE = re.compile(r"\bGRADED\s+(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
STANDING_HDR = "## 📌 STANDING STATE"


def standing_rows(text):
    """Every table row INSIDE the STANDING STATE section. Bounded by its own heading and the
    next `## `, so a stamp anywhere else in STATUS.md cannot satisfy this check."""
    if STANDING_HDR not in text:
        return None
    seg = text[text.index(STANDING_HDR):]
    nxt = seg.find("\n## ", 1)
    if nxt != -1:
        seg = seg[:nxt]
    out = []
    for ln in seg.split("\n"):
        t = ln.strip()
        if not t.startswith("| **"):      # table rows only; skips the |---| separator
            continue
        label = t[2:120].split("|")[0].strip().strip("*").strip()
        out.append((label, ln))
    return out


def check_standing():
    """Acceptance test ③, second half: do STANDING STATE values agree with their records?

    ⛔ REWRITTEN 2026-09-07 (CODEX verification #2). The FIRST version was a FALSE GREEN in two
    independent ways, both demonstrated against it:
      (a) IT COUNTED STAMPS, NOT ROWS. It took min() over every `reconciled` date found
          ANYWHERE in STATUS.md. Delete BRT-26's stamp -> still passed. Delete ALL standing
          stamps and drop one into an unrelated history section -> still passed. It answered
          "does a stamp exist?" while claiming to answer "is each standing row reconciled?"
          [[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]
      (b) IT COMPARED AGAINST THE WRONG DATE. It used the catalyst's EVENT date. The 2026-09-04
          Friday pair was GRADED 2026-09-06 — so `reconciled 2026-09-05` passed while the grade
          that invalidated it landed the NEXT DAY.
    ★ THERE ARE FOUR DISTINCT DATES HERE and I collapsed them twice in a row:
        event date  — when the thing happened (catalyst row's date column)
        as-of       — the DATA VINTAGE a standing value describes
        GRADE date  — when the print was actually adjudicated (often days after the event)
        reconciled  — when a human last checked the standing row against its record
    Version 1 confused as-of with grade date. Version 2 fixed that and confused EVENT date with
    grade date. Naming two of four is not naming them.
    [[finding_level_and_rate_look_like_agreement_until_you_name_which]]

    Now: EVERY row in the STANDING STATE section must carry `✓ **reconciled `<ISO>`` `, and each
    is compared against the newest GRADE date (falling back to the event date only when a
    catalyst declares none). Flags for review; never auto-edits — a standing value is a
    judgement, not a render.
    """
    t = STATUS.read_text(encoding="utf-8")
    rows = standing_rows(t)
    if rows is None:
        print(f"🔴 STANDING STATE: section {STANDING_HDR!r} not found in STATUS.md — the guard "
              f"cannot locate what it is supposed to supervise. Treat as FAILURE.")
        return 1
    if not rows:
        print("🔴 STANDING STATE: section present but contains NO table rows — inert guard.")
        return 1

    unstamped = [lbl for lbl, ln in rows if not RECONCILED_RE.search(ln)]
    if unstamped:
        print(f"🔴 STANDING STATE: {len(unstamped)} of {len(rows)} row(s) carry NO "
              f"`✓ reconciled` stamp — they are UNSUPERVISED, not verified:")
        for lbl in unstamped:
            print(f"     🔴 {lbl[:96]}")
        print("     ⇒ every standing row is a claim about current state; an unstamped one is a "
              "claim nobody has checked. Re-read against its canonical record and stamp it.")
        return 1

    # newest date at which ANY catalyst became known (grade date if declared, else event date)
    known = []
    for d, approx, event, pri, dclass in load():
        g = GRADED_RE.search(event)
        if g:
            try:
                known.append((datetime.strptime(g.group(1), "%Y-%m-%d").date(), d, "graded"))
                continue
            except ValueError:
                pass
        if re.search(r"\bFIRED\b|\bGRADED\b", event, re.IGNORECASE):
            known.append((d, d, "fired"))
    behind = []
    for lbl, ln in rows:
        rec = datetime.strptime(RECONCILED_RE.search(ln).group(1), "%Y-%m-%d").date()
        newer = [k for k in known if k[0] > rec]
        if newer:
            behind.append((lbl, rec, max(newer)))
    if behind:
        print(f"🟠 STANDING STATE: {len(behind)} of {len(rows)} row(s) reconciled BEFORE a "
              f"catalyst was graded — proven UNVERIFIED, not proven wrong:")
        for lbl, rec, (kd, ed, kind) in behind:
            print(f"     🟠 {lbl[:72]} — reconciled {rec}, but the {ed} catalyst was "
                  f"{kind} {kd}")
        print("     ⇒ RE-READ each against its canonical record and re-stamp. NOT auto-fixed.")
        return 2
    newest = max((k[0] for k in known), default=None)
    print(f"✅ STANDING STATE: all {len(rows)} row(s) stamped and reconciled at or after the "
          f"newest graded catalyst ({newest}).")
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
