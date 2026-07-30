"""Tests for `_daily_log.upsert_row` — the canary upsert (KB-VIO-160).

Run: .venv/bin/python3 AGENTS/VIOLET/scripts/test_daily_log.py

Tested in BOTH directions on purpose. VIOLET has now shipped two guards whose
own v1 failed on first run (7/30: the canary agreement check false-positived;
the H3 backtest shipped an inverted sign that produced a tidy, believable
table). A guard that is only tested on the case it was built for is a guard
whose failure mode is untested.
"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _daily_log import upsert_row, describe  # noqa: E402

COLS = ["date", "val", "state", "note", "stamp_utc"]
FAILS = []


def check(name, got, want):
    if got != want:
        FAILS.append(f"  ✗ {name}\n      got:  {got!r}\n      want: {want!r}")
    else:
        print(f"  ✓ {name}")


def rows(p):
    return [l.split("\t") for l in p.read_text().splitlines()[1:]]


def fresh():
    d = Path(tempfile.mkdtemp())
    return d / "T.tsv"


# 1 — appends into a file that does not exist yet (creates the header).
p = fresh()
st, ch = upsert_row(p, COLS, ["2026-07-30", "1.0", "CALM", "-", "t1"])
check("1 new file -> appended", (st, ch), ("appended", {}))
check("1 header written", p.read_text().splitlines()[0], "\t".join(COLS))

# 2 — THE BUG THIS MODULE EXISTS FOR: same date, state escalates. Must supersede
#     and must surface the state transition, not silently skip.
st, ch = upsert_row(p, COLS, ["2026-07-30", "15.7", "FIRE", "-", "t2"])
check("2 escalation -> superseded", st, "superseded")
check("2 state change reported", ch.get("state"), ("CALM", "FIRE"))
check("2 value change reported", ch.get("val"), ("1.0", "15.7"))
check("2 row actually rewritten", rows(p)[0][:3], ["2026-07-30", "15.7", "FIRE"])
check("2 still exactly one row", len(rows(p)), 1)

# 3 — identical re-run: no churn, no phantom change, stamp still refreshes.
st, ch = upsert_row(p, COLS, ["2026-07-30", "15.7", "FIRE", "-", "t3"])
check("3 identical -> skip-identical", (st, ch), ("skip-identical", {}))
check("3 stamp refreshed in place", rows(p)[0][4], "t3")
check("3 no duplicate row", len(rows(p)), 1)

# 4 — NULL-PRESERVING MERGE: a later degraded read (lost IV leg) must NOT
#     destroy the good stored value. This is the bug a blind overwrite would
#     have introduced while fixing the first one.
p2 = fresh()
upsert_row(p2, COLS, ["2026-07-30", "9.9", "CALM", "iv ok", "t1"])
st, ch = upsert_row(p2, COLS, ["2026-07-30", None, "CALM", "-", "t2"])
check("4 null does not overwrite", rows(p2)[0][1], "9.9")
check("4 dash does not overwrite", rows(p2)[0][3], "iv ok")
check("4 no change reported", (st, ch), ("skip-identical", {}))

# 4b — but a real value DOES replace a stored null (the recovery direction).
p2b = fresh()
upsert_row(p2b, COLS, ["2026-07-30", "-", "CALM", "-", "t1"])
st, ch = upsert_row(p2b, COLS, ["2026-07-30", "9.9", "CALM", "-", "t2"])
check("4b null -> value recovers", (rows(p2b)[0][1], st), ("9.9", "superseded"))

# 5 — supersede=False must still REPORT the divergence. A decline to write may
#     not be silent; that is the failure mode being fixed.
p3 = fresh()
upsert_row(p3, COLS, ["2026-07-30", "1.0", "CALM", "-", "t1"])
st, ch = upsert_row(p3, COLS, ["2026-07-30", "15.7", "FIRE", "-", "t2"])
_ = st
p4 = fresh()
upsert_row(p4, COLS, ["2026-07-30", "1.0", "CALM", "-", "t1"])
st, ch = upsert_row(p4, COLS, ["2026-07-30", "15.7", "FIRE", "-", "t2"], supersede=False)
check("5 declined write -> skip-exists", st, "skip-exists")
check("5 divergence still reported", ch.get("state"), ("CALM", "FIRE"))
check("5 file left untouched", rows(p4)[0][2], "CALM")

# 6 — a different date appends rather than overwriting the prior day.
p5 = fresh()
upsert_row(p5, COLS, ["2026-07-29", "1.0", "CALM", "-", "t1"])
upsert_row(p5, COLS, ["2026-07-30", "2.0", "FIRE", "-", "t2"])
check("6 new date appends", [r[0] for r in rows(p5)], ["2026-07-29", "2026-07-30"])
check("6 prior day untouched", rows(p5)[0][2], "CALM")

# 7 — updating a row that is NOT the last line must not disturb later rows or
#     their order. `today` is pinned to that row's date so this exercises the
#     mid-file rewrite mechanics, not the today-only guard (test 11 owns that).
st, ch = upsert_row(p5, COLS, ["2026-07-29", "1.5", "WATCH", "-", "t3"], today="2026-07-29")
check("7 mid-file update", (rows(p5)[0][1], rows(p5)[0][2]), ("1.5", "WATCH"))
check("7 order preserved", [r[0] for r in rows(p5)], ["2026-07-29", "2026-07-30"])
check("7 later row intact", rows(p5)[1][2], "FIRE")

# 8 — a ragged/short stored row is tolerated, not a crash.
p6 = fresh()
p6.write_text("\t".join(COLS) + "\n2026-07-30\t1.0\n", encoding="utf-8")
st, ch = upsert_row(p6, COLS, ["2026-07-30", "1.0", "FIRE", "-", "t2"])
check("8 ragged row tolerated", st, "superseded")
check("8 ragged row filled", rows(p6)[0][2], "FIRE")

# 9 — a pure stamp change is NOT a data change (else every run reads as churn).
p7 = fresh()
upsert_row(p7, COLS, ["2026-07-30", "1.0", "CALM", "-", "t1"])
st, ch = upsert_row(p7, COLS, ["2026-07-30", "1.0", "CALM", "-", "t999"])
check("9 stamp-only is not a change", (st, ch), ("skip-identical", {}))

# 10 — describe() must 🔴-flag a state transition and must not dress a declined
#      write up as a success.
msg = describe("superseded", "2026-07-30", {"state": ("CALM", "FIRE")}, "JPY_VOL.tsv")
check("10 state change is loud", "🔴 STATE CHANGED CALM → FIRE" in msg, True)
msg2 = describe("skip-exists", "2026-07-30", {"state": ("CALM", "FIRE")}, "JPY_VOL.tsv")
check("10 declined write says STALE", "STALE" in msg2 and "⚠️" in msg2, True)
msg3 = describe("skip-identical", "2026-07-30", {}, "JPY_VOL.tsv")
check("10 unchanged is quiet", "🔴" not in msg3, True)

# 11 — TODAY-ONLY GUARD. The regression that the first version of this module
#      actually shipped: re-running on 7/30 while the data still reads 7/29
#      rewrote the *7/29* row with *7/30*'s catalyst clock. A past-dated row must
#      be reported and left alone.
p8 = fresh()
upsert_row(p8, COLS, ["2026-07-29", "1.0", "CALM", "FOMC", "t1"], today="2026-07-29")
st, ch = upsert_row(p8, COLS, ["2026-07-29", "1.0", "CALM", "AMZN", "t2"], today="2026-07-30")
check("11 past-dated -> skip-past", st, "skip-past")
check("11 divergence still reported", ch.get("note"), ("FOMC", "AMZN"))
check("11 history NOT rewritten", rows(p8)[0][3], "FOMC")

# 11b — same row, same date as today: still supersedes normally.
st, ch = upsert_row(p8, COLS, ["2026-07-29", "1.0", "CALM", "AMZN", "t3"], today="2026-07-29")
check("11b today -> supersedes", (st, rows(p8)[0][3]), ("superseded", "AMZN"))

# 11c — a past-dated row that is IDENTICAL must stay quiet, not trip the guard.
st, ch = upsert_row(p8, COLS, ["2026-07-29", "1.0", "CALM", "AMZN", "t4"], today="2026-07-30")
check("11c past-dated identical is quiet", (st, ch), ("skip-identical", {}))

# 11d — appending a NEW past-dated row (a genuine backfill) is still allowed;
#       the guard blocks retro-EDITS, not gap-filling.
st, ch = upsert_row(p8, COLS, ["2026-07-28", "0.5", "CALM", "-", "t5"], today="2026-07-30")
check("11d backfill append allowed", st, "appended")

# 12 — describe() must not dress a blocked retro-edit up as a success.
msg4 = describe("skip-past", "2026-07-29", {"note": ("FOMC", "AMZN")}, "CHEAP_TAIL.tsv")
check("12 skip-past says NOT written", "NOT written" in msg4 and "⚠️" in msg4, True)

print()
if FAILS:
    print(f"❌ {len(FAILS)} FAILED\n" + "\n".join(FAILS))
    sys.exit(1)
print("✅ all daily-log upsert tests pass")
