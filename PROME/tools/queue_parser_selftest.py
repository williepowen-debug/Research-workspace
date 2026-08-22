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
    rows.append(f"| 34 | Blocked item ⛔ waiting on row 78 | ACTION | none | {recent} | — | notes |")
    # Row 35: ⛔ as the ordinary caveat/prohibition glyph, NOT a wait declaration.
    # This row IS Will-actionable and must count. Added 8/22 after both parsers
    # were found keying `blocked` on the bare glyph — they AGREED, so this test
    # passed clean while the live Helm demoted a dated RULE row (73, due 8/28) to
    # "in flight" and told Will 0 words were owed. Agreement is not correctness;
    # the guard needed a case that discriminates the rule, not just the pair.
    rows.append(f"| 35 | Caveat item ⛔ do not pre-empt the owner | DECISION | none | {recent} | — | notes |")
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
        detail = "; ".join(d for (n, d) in captured if "WILL_QUEUE" in n)
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

        check(f"1 count agreement (gate={gate_count} brief={brief_count} expect 22)",
              gate_count == 22 and brief_count == 22)
        check("2 lettered 32b visible to brief", "32b" in ids)
        check("3a misfiled #33 invisible to brief", "33" not in ids)
        check("3b misfiled #33 flagged by gate", "MISFILED #33" in detail)
        check("4 blocked #34 visible to brief, blocked=True",
              any(r["n"] == "34" and r["blocked"] for r in vis))
        check("4b caveat-glyph #35 visible to brief and NOT blocked",
              any(r["n"] == "35" and not r["blocked"] for r in vis))
        check("5a aging #79 flagged by gate", "AGING #79" in detail)
        check("5b aging #79 visible to brief", "79" in ids)

    if fails:
        print("QUEUE-PARSER SELFTEST ✗ " + " · ".join(fails))
        return 1
    print(f"QUEUE-PARSER SELFTEST ✓ gate and brief agree on the synthetic row set "
          f"({gate_count}/{brief_count})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
