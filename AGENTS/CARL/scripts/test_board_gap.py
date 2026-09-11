#!/usr/bin/env python3
"""Regression tests for board_gap.py.

⛔ WHY THESE EXIST: the first version of board_gap.py shipped with TWO defects that
my own two negative tests could not have caught, because both tests varied the
LEDGER and never the INPUT:
  (1) missing/empty BOARD/INDEX.md returned 0 with "✅ no unrecorded ids"
  (2) "CARL (ACTION)" — 26 live occurrences — never matched the recipient parse
An external review found them. [[finding_test_the_guard_not_just_the_guarded]]
says falsify the guard's own v1; I falsified only the half I had imagined.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import board_gap  # noqa: E402

FAILS = []


def check(name, got, want):
    ok = got == want
    print(f"  {'✅' if ok else '❌'} {name}: got={got!r} want={want!r}")
    if not ok:
        FAILS.append(name)


def test_action_names():
    a = board_gap.action_names
    check("plain", "CARL" in a("WALTER → CARL · info: HENRY"), True)
    check("annotated (ACTION)", "CARL" in a("WALTER → CARL (ACTION) · info: RED"), True)
    check("annotated (lead)", "CARL" in a("WALTER → CARL (lead) · info: RED"), True)
    check("bold markup", "CARL" in a("WALTER → **CARL** · info: RED"), True)
    check("comma list", "CARL" in a("WALTER → FALCON, CARL · info: RED"), True)
    check("slash list", "CARL" in a("WALTER → HAWK/CARL"), True)
    check("'and' list", "CARL" in a("WALTER → HOMER and CARL"), True)
    # the critical negative: info-only must NOT count as an action recipient
    check("info-only excluded", "CARL" in a("WALTER → HOMER · info: CARL, REGINALD"), False)
    check("info-only no-arrow", "CARL" in a("WALTER → (info only) · info: CARL"), False)
    check("other desk only", "CARL" in a("WALTER → BRENT · info: SAM"), False)


def test_fail_closed(tmp):
    real = board_gap.INDEX
    try:
        board_gap.INDEX = tmp / "nope.md"
        check("missing INDEX fails closed", board_gap.main(), 2)
        empty = tmp / "empty.md"
        empty.write_text("")
        board_gap.INDEX = empty
        check("empty INDEX fails closed", board_gap.main(), 2)
        norows = tmp / "norows.md"
        norows.write_text("# BOARD\n\nprose only, no table rows\n")
        board_gap.INDEX = norows
        check("zero parsed rows fails closed", board_gap.main(), 2)
    finally:
        board_gap.INDEX = real


def test_live_clean():
    check("live INDEX returns 0 or 1 (never 2)", board_gap.main() in (0, 1), True)


if __name__ == "__main__":
    import tempfile
    print("board_gap regression tests")
    test_action_names()
    with tempfile.TemporaryDirectory() as d:
        test_fail_closed(Path(d))
    test_live_clean()
    print(f"\n{'ALL PASS' if not FAILS else 'FAILURES: ' + ', '.join(FAILS)}")
    sys.exit(1 if FAILS else 0)
