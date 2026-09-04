#!/usr/bin/env python3
"""CALENDAR.md ⇄ CATALYSTS.tsv twin check — WHICH IS RIGHT, never merely WHETHER THEY AGREE.

WHY THIS EXISTS, AND WHY ITS SHAPE IS THE WHOLE POINT
-----------------------------------------------------
`CLAUDE.md` write-back step 10 says `CATALYSTS.tsv` is the source of truth and
`CALENDAR.md` is the human twin that "must not diverge." **That rule had no
mechanism** — nothing in boot compared them — so on 2026-09-04 a session found the
twins disagreeing on Micron's earnings date and closed the gap by hand.

**It closed it the wrong way, and the audit trail says why (KB-VIO-235).**

    CALENDAR    ~2026-09-29  ESTIMATED   <- 1 day from the truth
    CATALYSTS   ~2026-09-22  MODELED     <- 8 days from the truth
    TRUTH        2026-09-30  ANNOUNCED   <- Micron press release, 2026-08-26

The session made the stale twin match the "reconciled" one and recorded it as a
divergence fix. **It moved the surface AWAY from the answer, and it felt like
hygiene.** A day later the same value was propagated a second time.

🔑 **A check that asks only WHETHER two surfaces agree converts every disagreement
into propagation of whichever was touched last.** Agreement is not correctness,
and the cheapest way to reach agreement is always to overwrite the other one.

So this tool **REFUSES TO NOMINATE A WINNER.** It reports the disagreement, prints
the `source` and `date_class` of the CATALYSTS row beside it, and — when that row
is `MODELED`/`ESTIMATED`/`DERIVED` — says in as many words that **it is not a
tiebreaker and the operator must go to the primary.** A `CONFIRMED` row with a
real source is the only case where it will say CATALYSTS should win, and even then
it names the source rather than asserting authority.

⚠️ ALSO NOT A TIEBREAKER: recency. The more recently edited surface is not the more
correct one — in the incident above it was the wrong one, twice.

`[[finding_owner_of_record_means_authoritative_not_correct]]`

Exit codes: 0 = twins consistent; 1 = divergence needing an operator decision.
"""
from __future__ import annotations
import argparse, csv, re, sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALYSTS = ROOT / "workbook" / "CATALYSTS.tsv"
CALENDAR = ROOT / "CALENDAR.md"

MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1)}

# ⚠️ THE CLASS MUST BE READ FROM AN EXPLICIT `date_class` DECLARATION, NEVER FROM
# FREE PROSE. First version of this file scanned the whole event+notes text for
# the bare words, and the falsification run caught it immediately: a row correctly
# marked `date_class CONFIRMED` was reported as MODELED, because its notes said
# "CORRECTED ... from ~9/22 MODELED to 2026-09-30" — a HISTORICAL mention of the
# class it had left behind. The supersession note contained the superseded token.
# [[finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it]]
DECL = re.compile(r"date[_ ]?class\W{0,4}\*{0,2}([A-Za-z-]+)", re.I)
SOFT = {"modeled", "modelled", "estimated", "derived", "date-estimated", "provisional"}
HARD = {"confirmed", "announced", "verified"}


def date_class_of(row: dict) -> tuple[str | None, str]:
    """(class_or_None, where_it_was_found). The EVENT field wins over notes.

    Fails toward 'unlabelled', which this tool treats as NOT a tiebreaker — the
    safe direction, because the cost of wrongly withholding a tiebreak is one
    operator glance and the cost of wrongly granting one is a propagated error.
    """
    for field in ("event", "notes"):
        m = DECL.search(row.get(field, "") or "")
        if m:
            return m.group(1).lower(), field
    return None, "—"

# The forward section is the only one whose rows are live obligations. RESOLVED
# rows are history and are SUPPOSED to hold their as-of values.
FORWARD_HEADING = "## ACTIVE FORWARD CATALYSTS"


def load_catalysts() -> list[dict]:
    with open(CATALYSTS, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f, delimiter="\t") if r.get("date")]


def calendar_forward_rows() -> list[tuple[int, date, str]]:
    """(line_no, date, row_text) for dated rows in the ACTIVE FORWARD section only."""
    text = CALENDAR.read_text(encoding="utf-8").splitlines()
    try:
        start = next(i for i, l in enumerate(text) if l.strip() == FORWARD_HEADING)
    except StopIteration:
        print(f"⛔ {CALENDAR.name} has no '{FORWARD_HEADING}' heading — "
              f"cannot scope the check. FAILING CLOSED rather than scanning the whole file.")
        sys.exit(2)
    end = next((i for i in range(start + 1, len(text))
                if text[i].startswith("## ")), len(text))
    out = []
    for i in range(start, end):
        line = text[i]
        m = re.match(r"\|\s*\*{0,2}([A-Z][a-z]{2})\s+(\d{1,2})", line)
        if not m:
            continue
        mon, day = MONTHS.get(m.group(1)), int(m.group(2))
        if not mon:
            continue
        yr_m = re.search(r"\b(20\d{2})\b", line[:60])
        yr = int(yr_m.group(1)) if yr_m else date.today().year
        try:
            out.append((i + 1, date(yr, mon, day), line))
        except ValueError:
            continue
    return out


def key_words(s: str) -> set[str]:
    """Content words used to pair a CALENDAR row with a CATALYSTS row."""
    s = re.sub(r"[^A-Za-z0-9 ]", " ", s)
    stop = {"the", "and", "for", "a", "an", "of", "on", "at", "in", "to", "is",
            "et", "am", "pm", "date", "class", "after", "close", "was", "not"}
    return {w.lower() for w in s.split() if len(w) > 2 and w.lower() not in stop}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)

    cats = load_catalysts()
    cal = calendar_forward_rows()
    today = date.today()
    problems: list[str] = []

    if not a.quiet:
        print(f"TWIN CHECK  •  CALENDAR.md ⇄ CATALYSTS.tsv  •  {today}")
        fwd = [c for c in cats if c.get("date", "") >= today.isoformat()]
        print(f"  CATALYSTS rows: {len(cats)} ({len(fwd)} forward)   "
              f"CALENDAR forward-section rows: {len(cal)}")
        print("  ⚠️  This tool reports divergence. It does NOT pick a winner — see the docstring.")
        print("─" * 92)

    # ── ① PAST-DATED ROWS STILL IN THE ACTIVE FORWARD SECTION ────────────────
    # v1 never checked this and the external review found three August events
    # sitting under "ACTIVE FORWARD CATALYSTS" while the check returned green.
    for ln, ld, ltext in cal:
        if ld < today:
            problems.append(
                f"🟠 PAST EVENT STILL IN 'ACTIVE FORWARD' — CALENDAR.md line {ln}: {ld}\n"
                f"     {ltext[:110].strip()}\n"
                f"     A fired catalyst under a FORWARD heading is a live-looking dead row.\n"
                f"     Move it to the RESOLVED section (with its grade) — do not delete it.")

    # ── ①b PAST-DATED ROWS STILL IN CATALYSTS ────────────────────────────────
    # SYMMETRY, and it was missing: v2 of this file reported past rows on the
    # CALENDAR side and SILENTLY SKIPPED them on the CATALYSTS side (`if cd <
    # today: continue`). Both surfaces were carrying the SAME three fired August
    # rows; the external review saw only the CALENDAR half, and the first
    # bidirectional run still would not have reported the other. Fixing one
    # direction of a symmetric check and leaving the other is how a defect
    # survives its own fix.
    for c in cats:
        try:
            cd = datetime.strptime(c["date"], "%Y-%m-%d").date()
        except ValueError:
            continue
        if cd < today:
            problems.append(
                f"🟠 FIRED ROW STILL IN CATALYSTS.tsv — {cd}  {c['event'][:70]}\n"
                f"     Write-back step 10 prunes fired rows. Grade it into CALENDAR's\n"
                f"     RESOLVED section first — pruning has a trigger (the event fires)\n"
                f"     and grading has none, so an ungraded prune loses the obligation.")

    # ── ② CATALYSTS → CALENDAR, ONE-TO-ONE ───────────────────────────────────
    # v1 let ONE CALENDAR row satisfy MANY CATALYSTS rows, so 8 catalysts matched
    # against 7 calendar rows and still returned green. Each CALENDAR row may now
    # be claimed at most once, and the claim must be unambiguous.
    claimed: dict[int, str] = {}
    for c in cats:
        try:
            cd = datetime.strptime(c["date"], "%Y-%m-%d").date()
        except ValueError:
            continue
        if cd < today:
            continue
        ck = key_words(c["event"])
        scored = sorted(((len(ck & key_words(t)), ln, ld, t) for ln, ld, t in cal),
                        key=lambda x: -x[0])
        best = scored[0] if scored else None
        if best is None or best[0] < 2:
            problems.append(
                f"🟠 MISSING FROM CALENDAR — {c['date']}  {c['event'][:70]}\n"
                f"     CATALYSTS is the source of truth, so the human twin is INCOMPLETE.\n"
                f"     Add it; do not delete the CATALYSTS row to make them agree.")
            continue
        score, ln, ld, _ = best
        if ln in claimed:
            problems.append(
                f"🔴 TWO CATALYSTS ROWS MATCH ONE CALENDAR ROW (line {ln}) — ambiguous twin\n"
                f"     · {claimed[ln][:80]}\n"
                f"     · {c['event'][:80]}\n"
                f"     One CALENDAR row cannot represent two dated obligations. Split it,\n"
                f"     or this check silently certifies a surface that is missing one.")
            continue
        claimed[ln] = c["event"]
        cls, where = date_class_of(c)
        src = (c.get("source") or "").strip()
        if ld != cd:
            if cls in HARD:
                verdict = (
                    f"     ✅ CATALYSTS declares date_class {cls.upper()} (found in `{where}`).\n"
                    f"     IF the source below is a primary YOU have opened, CALENDAR moves to it.\n"
                    f"     Opening it is the step — a CONFIRMED label is a claim, not the document.")
            else:
                shown = cls.upper() if cls else "UNLABELLED"
                verdict = (
                    f"     ⛔ DO NOT RESOLVE BY MAKING ONE MATCH THE OTHER. Go to the primary.\n"
                    f"     CATALYSTS date_class is {shown} (found in `{where}`) — NOT a tiebreaker.\n"
                    f"     A derivation with no tunable knobs is still not a confirmation:\n"
                    f"     \"zero free parameters\" describes what could be tuned, never what was assumed.")
            problems.append(
                f"🔴 DATE DIVERGENCE — {c['event'][:66]}\n"
                f"     CATALYSTS.tsv : {cd}\n"
                f"     CALENDAR.md   : {ld}   (line {ln})\n"
                f"     source        : {src[:150] or '(none recorded — that is itself the finding)'}\n"
                f"{verdict}\n"
                f"     ⚠️  Recency is NOT a tiebreaker either: on 2026-09-04 the more recently\n"
                f"     edited surface was the wrong one, twice (KB-VIO-235).")

    # ── ③ CALENDAR → CATALYSTS (the direction v1 never ran) ──────────────────
    # Without this, a forward CALENDAR row that no catalyst backs is invisible —
    # and CATALYSTS is the declared source of truth, so an unbacked forward row
    # is either a missing catalyst or a row that should not be forward.
    for ln, ld, ltext in cal:
        if ld < today or ln in claimed:
            continue
        problems.append(
            f"🟠 CALENDAR FORWARD ROW WITH NO CATALYSTS BACKING — line {ln}: {ld}\n"
            f"     {ltext[:110].strip()}\n"
            f"     CATALYSTS.tsv is the source of truth and has no matching row.\n"
            f"     Either add the catalyst or demote this row — an unbacked forward row\n"
            f"     is a dated obligation nothing machine-readable knows about.")

    if problems:
        for p_ in problems:
            print(p_)
            print()
        print(f"🔴 TWIN CHECK — {len(problems)} item(s) need an OPERATOR decision, not an edit.")
        return 1
    if not a.quiet:
        print(f"  ✅ {len(claimed)} forward CATALYSTS row(s) matched 1:1 to CALENDAR rows on the")
        print(f"     same date; no past rows under the forward heading; no unbacked forward rows.")
        print(f"  ⚠️  Consistent ≠ correct — this proves the twins agree, never that either is right.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
