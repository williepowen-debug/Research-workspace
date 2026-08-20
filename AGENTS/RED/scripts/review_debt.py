#!/usr/bin/env python3
"""
RED review-debt check — are the ROW-LEVEL review dates being honoured?

    (cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/RED/scripts/review_debt.py)
    ... --strict   exit 1 when anything is owed (CI / gate use)
    ... --quiet    one summary line, for boot

Read-only. Default exit 0 (advisory, like ledger_staleness).

WHY THIS EXISTS (S33, 2026-08-20; ML-RED-181/182). RED's CLAUDE.md says KB.tsv rows
"must be reviewed/refreshed by that date" and that VX strengths get reviewed each sweep.
NOTHING ENFORCED EITHER. `scripts/ledger_staleness.py` reads FILE vintage -- a single
mtime/commit-date per ledger -- so KB.tsv scored CLEAN while 33 of its 86 rows (38%) sat
past their own Stale_By, the worst by 61 days, and VX.tsv's own alert could not see that
9 of 18 live vectors were 59-79 days unreviewed. A file-level check cannot see row-level
debt; that is not a bug in it, it is a different question.

The S33 sweep measured the shape and it is the whole reason this file exists: every
INSTRUMENTED RED surface was green that morning (DUE-scan 0 overdue, docket 0 past-date,
board_log 0/0) while every UNINSTRUMENTED one carried 30-80 days of drift. Same agent,
same sessions. THE VARIABLE IS INSTRUMENTATION, NOT ATTENTION -- so the fix is a check,
not a resolution to be more careful. Editing the rows alone buys ~30 days.

THE RULE IT ENCODES IS TWO-DIMENSIONAL, and the second half is the part that is easy to
get wrong (it was found only mid-pass, by a row that broke the first half):

    STATUS   decides whether a review is SCHEDULED.
    CITATION decides whether the CONTENTS must be CURRENT.

A row in a terminal status (RESOLVED / INVALIDATED / REVISED / CORRECTED / VERIFIED /
DATED-HISTORICAL / ...) is owed no scheduled re-review -- Stale_By is a trigger for LIVE
facts, and a terminal row carrying a live date is noise that inflates the count until the
whole population reads as unaffordable and gets deferred. THAT IS THE FAILURE MODE THIS
CHECK IS TUNED AGAINST: "33 stale rows" reads as a project; the 9 that were actually owed
read as a session.

BUT terminal status does NOT make a row safe. KB-RED-001 is REVISED (terminal, no review
owed) and still feeds VX-RED-001 and VX-RED-006 -- both STRONG and live -- while its Fact
cell asserts "NFP +178K confirms employment channel stalled" against a -23K print. So a
terminal row that a LIVE SURFACE CITES gets flagged on the contents axis even though it is
flagged on neither date axis. Any check that only reads Stale_By misses exactly this row,
and this row is the dangerous one, because a terminal status reads as settled.

⚠️ Do NOT parse these TSVs with the csv module -- literal '"' in prose cells makes
csv.reader mangle rows (ML-RED-168). Split on '\t'.

⚠️ Deliberately NOT keyed on mtime anywhere: git sync restamps it, so an mtime-based
freshness check fails FALSE-NEGATIVE (finding_mtime_is_corrupted_by_git_sync). Every date
here is read from row CONTENT.
"""
import os, subprocess, sys, datetime

# Terminal = the row records a settled outcome. No scheduled re-review is owed.
TERMINAL = {
    "RESOLVED", "RESOLVED-GRADED", "RESOLVED-NOT-MET", "RESOLVED-SUPERSEDED",
    "RESOLVED-CONVERGED", "RESOLVED-VERIFIED", "RESOLVED-CORRECTED",
    "INVALIDATED", "REVISED", "CORRECTED", "VERIFIED", "SUPERSEDED", "RETIRED",
    "DATED-HISTORICAL", "DISPUTED-DEMOTED",
}

# Surfaces a stale FACT would reach a reader through. Citation => contents must be current.
LIVE_SURFACES = [
    "STATUS.md", "NEXUS_BRIEF.md", "CALENDAR.md", "SCRATCH.md",
    "workbook/VX.tsv", "registry/FALSIFICATION_TRIGGERS.tsv",
]

VX_MAX_AGE_DAYS = 45  # a vector unreviewed longer than this is CARRIED, not measured


def rows(path):
    """Header + data rows, tab-split.

    ⚠️ Skips leading '#' banner lines. VX.tsv and FLOW.tsv carry a two-clock banner on
    line 0 with the HEADER on line 1 — VX.tsv's own banner warns about this in prose, and
    it still bit: a naive `awk NR>1` on VX.tsv skips the banner and then reads the HEADER
    ROW AS A VECTOR. That is how S33 first published "9 of 18 live vectors" when the true
    denominator is 17. The numerator was unaffected (the header's Last_Reviewed cell is the
    literal string 'Last_Reviewed', which loses a date comparison), so the error surfaced
    ONLY in the total — an off-by-one that flattered the ratio and would never have been
    caught by eye. Prose warnings do not parse; this function is the fix.
    """
    with open(path, encoding="utf-8") as f:
        lines = [l for l in f.read().split("\n") if l != ""]
    while lines and lines[0].lstrip().startswith("#"):
        lines = lines[1:]
    head = lines[0].split("\t")
    return head, [l.split("\t") for l in lines[1:]]


def as_date(s):
    s = s.strip()
    if len(s) != 10 or s[4] != "-":
        return None                     # 'n/a-historical', '', prose -> no live date
    try:
        return datetime.date.fromisoformat(s)
    except ValueError:
        return None


def cited(ids, root):
    """Which ids appear on a live surface? One grep for all of them."""
    if not ids:
        return set()
    paths = [p for p in (os.path.join(root, s) for s in LIVE_SURFACES) if os.path.exists(p)]
    if not paths:
        return set()
    hits = set()
    args = ["grep", "-oh", "-F"]
    for i in sorted(ids):
        args += ["-e", i]
    out = subprocess.run(args + paths, capture_output=True, text=True)
    for line in out.stdout.split("\n"):
        if line.strip():
            hits.add(line.strip())
    return hits


def main():
    strict = "--strict" in sys.argv
    quiet = "--quiet" in sys.argv
    root = os.path.join(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                       capture_output=True, text=True).stdout.strip(), "AGENTS/RED")
    today = datetime.date.today()

    kb_path = os.path.join(root, "workbook/KB.tsv")
    vx_path = os.path.join(root, "workbook/VX.tsv")

    kb_head, kb = rows(kb_path)
    i_id, i_status, i_stale = kb_head.index("ID"), kb_head.index("Status"), kb_head.index("Stale_By")

    overdue, terminal_dated = [], []
    for c in kb:
        st, d = c[i_status].strip().upper(), as_date(c[i_stale])
        if d is None:
            continue
        if st in TERMINAL:
            # A PAST date on a terminal row is noise that inflates the count. A FUTURE one
            # is a deliberate schedule — the two-dimensional rule expressed through the date
            # field, for a terminal row a live surface cites (KB-RED-001). Do not tell a
            # future reader to undo that; only flag the past ones.
            if d < today:
                terminal_dated.append((c[i_id], c[i_stale], c[i_status]))
        elif d < today:
            overdue.append((c[i_id], c[i_stale], (today - d).days, c[i_status]))

    # CITATION axis: terminal rows a live surface still points at.
    term_ids = {r[0] for r in terminal_dated} | {
        c[i_id] for c in kb if c[i_status].strip().upper() in TERMINAL and as_date(c[i_stale]) is None
    }
    cited_terminal = sorted(cited(term_ids, root))

    vx_head, vx = rows(vx_path)
    v_id, v_tgt, v_str, v_rev = (vx_head.index("ID"), vx_head.index("Target"),
                                 vx_head.index("Strength"), vx_head.index("Last_Reviewed"))
    vx_stale, vx_live = [], 0
    for c in vx:
        if c[v_str].strip().upper().startswith("RESOLVED"):
            continue
        vx_live += 1
        d = as_date(c[v_rev])
        if d is None or (today - d).days > VX_MAX_AGE_DAYS:
            vx_stale.append((c[v_id], c[v_tgt][:28], c[v_str], c[v_rev],
                             (today - d).days if d else None))

    owed = len(overdue) + len(vx_stale)
    if quiet:
        print(f"[RED review-debt] KB {len(overdue)} row(s) past Stale_By · "
              f"VX {len(vx_stale)}/{vx_live} live vectors >{VX_MAX_AGE_DAYS}d · "
              f"{len(cited_terminal)} terminal row(s) cited live")
        return 1 if (strict and owed) else 0

    print("=" * 74)
    print(f"RED REVIEW-DEBT — row-level review dates, {today}")
    print("=" * 74)

    print(f"\n① KB.tsv — ACTIVE rows past their own Stale_By   [{len(overdue)}]")
    if overdue:
        for rid, sb, age, st in sorted(overdue, key=lambda r: -r[2]):
            print(f"   🔴 {rid:<13} due {sb}  {age:>4}d overdue   status={st}")
    else:
        print("   🟢 none — every live row is inside its own review date")

    print(f"\n② KB.tsv — TERMINAL rows still CITED by a live surface   [{len(cited_terminal)}]")
    print("   (no review SCHEDULED; contents must still be CURRENT — the KB-RED-001 class)")
    if cited_terminal:
        for rid in cited_terminal:
            print(f"   🟠 {rid}")
    else:
        print("   🟢 none")

    print(f"\n③ VX.tsv — live vectors unreviewed >{VX_MAX_AGE_DAYS}d   [{len(vx_stale)} of {vx_live} live]")
    if vx_stale:
        for vid, tgt, s, rev, age in sorted(vx_stale, key=lambda r: -(r[4] or 9999)):
            print(f"   🔴 {vid:<13} {tgt:<28} {s:<18} rev {rev} ({age}d)")
    else:
        print("   🟢 none")

    if terminal_dated and not quiet:
        print(f"\n   ℹ️  {len(terminal_dated)} terminal row(s) still carry a live Stale_By date — "
              f"noise, not debt.\n      Set them to n/a-historical / n/a-resolved so the count "
              f"means what it says.")
        for rid, sb, st in terminal_dated[:6]:
            print(f"        {rid} ({st}, {sb})")

    print(f"\n{'🔴' if owed else '🟢'} {owed} review(s) owed.  "
          f"Disposition: refresh · re-class DATED-HISTORICAL · or route to the owner "
          f"(never re-derive another desk's number to clear a flag).")
    return 1 if (strict and owed) else 0


if __name__ == "__main__":
    sys.exit(main())
