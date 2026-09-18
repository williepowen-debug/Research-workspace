#!/usr/bin/env python3
"""Queue-parser consistency selftest — prome_gate.py vs will_brief.py.

Born 2026-08-16 (RAV review, Will: "go on all four"): the 8/16 lettered-ID
fix (`^\\d` for 32b-class rows) and the MISFILED exclusion landed in
prome_gate.py's check_will_queue() but NOT in will_brief.py's
parse_actions() — the gate counted rows the Will-facing brief silently
skipped. The two parsers duplicate their row-visibility regexes by design
(the gate is a blocking boot surface and must not grow import coupling);
THIS TEST is the mechanism that keeps them agreeing.

Method: write a synthetic WILL_QUEUE.md into a temp tree — 21 actionable
rows (18 plain + 1 dated-future + 1 lettered `32b` + 1 undated-aging) plus
one closed-in-place row and one ⛔ blocked row — point both modules' ROOT
at it, and assert the two parsers agree on visibility and count class.
21 > the gate's 20-cap by construction, so the gate's actionable count is
observable off its own CAP message without refactoring the gate. Note the
count assertion alone can be fooled by COMPENSATING errors (pre-fix, the
missing 32b and the wrongly-visible misfiled row cancelled to 21) — the
per-class assertions are the ones that actually discriminate.

rc=0 all pass · rc=1 any assertion failed (~1s, no network, temp-dir only).
Wired: prome_gate.py mode_closeout advisory (edit-day drift gets caught at
the same session's closeout).
"""
import datetime as dt
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prome_gate
import will_brief


def build_synthetic(root: Path):
    today = dt.date.today()
    recent = f"{today.month}/{today.day}"
    old = today - dt.timedelta(days=30)
    rows = []
    for i in range(60, 78):        # 18 plain undated actionable rows
        rows.append(f"| {i} | Plain open item {i} | ACTION | none | {recent} | — | notes |")
    rows.append(f"| 78 | Dated future item | DECISION | 2026-12-01 | {recent} | — | notes |")
    rows.append(f"| 32b | Lettered successor row | ACTION | none | {recent} | — | notes |")
    rows.append(f"| 79 | Undated aging item | ACTION | none | {old.month}/{old.day} | — | notes |")
    rows.append(f"| 33 | ✅ RESOLVED closed-in-place item | ACTION | none | {recent} | — | notes |")
    rows.append(f"| 34 | Blocked item | ACTION | none | {recent} | — | ⛔ waits: row 78 (the documented form, start of Notes) |")
    # Row 35: ⛔ as the ordinary caveat/prohibition glyph, NOT a wait declaration.
    # This row IS Will-actionable and must count. Added 8/22 after both parsers
    # were found keying `blocked` on the bare glyph — they AGREED, so this test
    # passed clean while the live Helm demoted a dated RULE row (73, due 8/28) to
    # "in flight" and told Will 0 words were owed. Agreement is not correctness;
    # the guard needed a case that discriminates the rule, not just the pair.
    rows.append(f"| 35 | Caveat item ⛔ do not pre-empt the owner | DECISION | none | {recent} | — | notes |")
    # Row 36: ITEM prose that MENTIONS the wait marker ("a ⛔ waits row …") but is a
    # dated, Will-actionable RULE. Added 9/10 (WQ-221): every parser searched the
    # whole line for "⛔ wait", so the row proposing the aged-waits rule was filed
    # under "waiting on others" and rendered with no tap controls. The key is the
    # declaration at the START of the Notes cell, never the glyph in prose.
    rows.append(f"| 36 | Rule about a ⛔ waits row whose blocker is dark | DECISION | 2026-09-11 | {recent} | rec | notes |")
    # Rows 37–40 (2026-09-18, ACCEPTANCE_queue_parsers B1–B4): the split and the date classifier, exercised so that a
    # reversion of ANY parser's split fails this test (parserfixcold proved the 23-row set did not notice one).
    rows.append(f"| 37 | Escaped pipe in a code span `P(leg \\| fired)` | DECISION | 2026-09-19 | {recent} | rec | notes |")
    rows.append(f"| 38 | Unescaped pipe P(leg | fired) shifts this row | DECISION | 2026-09-19 | {recent} | rec | notes |")
    rows.append(f"| 39 | Short-form needed-by | DECISION | 9/19 | {recent} | rec | notes |")
    rows.append(f"| 40 | Fraction in a textual needed-by | DECISION | when 2/3 of the legs have filled | {recent} | rec | notes |")
    text = (
        f"# WILL_QUEUE (synthetic — selftest)\n**Last reconciled:** {today.isoformat()}\n\n"
        "## OPEN\n| # | Item | Type | Needed by | Since | PROME rec | Notes |\n"
        "|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n"
    )
    (root / "PROME").mkdir(parents=True)
    (root / "PROME" / "WILL_QUEUE.md").write_text(text, encoding="utf-8")


def main():
    fails = []
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        build_synthetic(root)

        # gate side — capture record() output; no boot side effects run
        captured = []
        prome_gate.ROOT = root
        prome_gate.record = lambda sev, name, ok, detail, owner: captured.append((name, detail))
        prome_gate.check_will_queue()
        detail = "; ".join(getattr(prome_gate.check_will_queue, "last_problems", None)
                           or [d for (n, d) in captured if "WILL_QUEUE" in n])   # the FULL problem list (the record detail shows five)
        cap = re.search(r"CAP: (\d+) actionable", detail)
        gate_count = int(cap.group(1)) if cap else None

        # brief side
        will_brief.ROOT = root
        will_brief.failures.clear()
        dec, chore = will_brief.parse_actions()
        vis = dec + chore
        ids = {r["n"] for r in vis}
        brief_count = sum(1 for r in vis if not r["blocked"])

        def check(name, cond):
            if not cond:
                fails.append(name)

        check(f"1 count agreement (gate={gate_count} brief={brief_count} expect 26: 23 + #37 + #39 + #40; #38 excluded as SHIFTED)",
              gate_count == 26 and brief_count == 26)
        check("2 lettered 32b visible to brief", "32b" in ids)
        check("3a misfiled #33 invisible to brief", "33" not in ids)
        check("3b misfiled #33 flagged by gate", "MISFILED #33" in detail)
        check("4 blocked #34 visible to brief, blocked=True",
              any(r["n"] == "34" and r["blocked"] for r in vis))
        check("4b caveat-glyph #35 visible to brief and NOT blocked",
              any(r["n"] == "35" and not r["blocked"] for r in vis))
        check("4c prose-mention #36 ('a ⛔ waits row' in ITEM) visible and NOT blocked",
              any(r["n"] == "36" and not r["blocked"] for r in vis))
        check("5a aging #79 flagged by gate", "AGING #79" in detail)
        check("5b aging #79 visible to brief", "79" in ids)
        # B1–B4 across all four parsers + table_check (2026-09-18)
        check("6a escaped-pipe #37 dated in brief", any(r["n"] == "37" and r["due"] == "2026-09-19" for r in vis))
        check("6b shifted #38 flagged BY NAME by gate", "SHIFTED #38" in detail)
        check("6c shifted #38 invisible to brief, with a named failure", "38" not in ids and any("WQ-38" in f[2] for f in will_brief.failures))
        check("6d NOT-ISO #39 flagged BY NAME by gate", "NOT-ISO #39" in detail)
        check("6e #39 visible to brief, undated, named failure", any(r["n"] == "39" and r["due"] is None for r in vis) and any("WQ-39" in f[2] for f in will_brief.failures))
        check("6f fraction #40 visible, undated, NO failure (B4)", any(r["n"] == "40" and r["due"] is None for r in vis) and not any("WQ-40" in f[2] for f in will_brief.failures))
        import willq_view, decision_deck, table_check
        qtext = (root / "PROME" / "WILL_QUEUE.md").read_text(encoding="utf-8")
        try:
            willq_view.parse_open(qtext); check("7a willq_view REFUSES the set naming #38 and #39", False)
        except willq_view.WillqError as e:
            check("7a willq_view REFUSES the set naming #38 and #39", "WQ-38" in str(e) and "WQ-39" in str(e))
        clean = "\n".join(l for l in qtext.split("\n") if not (l.startswith("| 38 |") or l.startswith("| 39 |")))
        wr = willq_view.parse_open(clean)
        check("7b willq_view: #37 dated, #40 undated", any(r["n"] == "37" and r["due"] == "2026-09-19" for r in wr) and any(r["n"] == "40" and r["due"] is None for r in wr))
        dr = decision_deck.parse_open(qtext)
        check("7c deck: #37 by=2026-09-19 · #38 absent · #39 and #40 by=None",
              any(r["n"] == "37" and r["by"] == "2026-09-19" for r in dr) and not any(r["n"] == "38" for r in dr)
              and any(r["n"] == "39" and r["by"] is None for r in dr) and any(r["n"] == "40" and r["by"] is None for r in dr))
        fx = ["| a \\| b | c || d |", "|\\| lead | mid \\| | trail \\||", "| `x | y` | z |", "| rec||", "|x|", "| 9/19 | `a|b` | \\| |"]
        for l in fx:
            ref = [x.strip() for x in table_check.split_cells(l)]
            check(f"8 split parity on {l!r}", willq_view.split_cells(l) == ref == prome_gate.split_cells(l) == will_brief.split_cells(l) == decision_deck.cells(l))
        for raw, want in [("9/19", True), ("9/19/26", True), ("2026-9-19", True), ("Sept 19", True), ("19 Sep", True), ("2026-09-19 (the 9/19 sitting)", False), ("when 2/3 of the legs have filled", False), ("at HEN-46's resolution", False), ("", False)]:
            check(f"9 date classifier parity on {raw!r}", willq_view.datelike_not_iso(raw) == prome_gate.datelike_not_iso(raw) == will_brief.datelike_not_iso(raw) == decision_deck.datelike_not_iso(raw) == want)

    if fails:
        print("QUEUE-PARSER SELFTEST ✗ " + " · ".join(fails))
        return 1
    print(f"QUEUE-PARSER SELFTEST ✓ gate · brief · willq_view · deck · table_check agree on the synthetic row set "
          f"({gate_count}/{brief_count}; split + date-classifier parity)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
