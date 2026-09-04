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

# ⚠️ PIN THE CLOCK. `upsert_row`'s TODAY-ONLY GUARD reads the real ET date when
# `today` is not passed, so any supersede-path assertion against a fixture dated
# 2026-07-30 passes ONLY on 2026-07-30 and returns `skip-past` every day after.
# That is exactly how this file broke: test 8 omitted it, went green on the day
# it was written, and had been failing ever since (DAEDALUS 2026-09-03, 9 days
# documented in the Codex audit). Tests that deliberately exercise the guard
# (11, 11b, 11c, 11d) pass their own explicit dates and must NOT use T.
T = "2026-07-30"

FAILS = []


def check(name, got, want):
    if got != want:
        # Print on failure too. Previously a failing check was silent until the
        # summary, so a later crash hid every failure before it — which is how
        # one IndexError masked the rest of the run.
        line = f"  ✗ {name}\n      got:  {got!r}\n      want: {want!r}"
        FAILS.append(line)
        print(line)
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
st, ch = upsert_row(p, COLS, ["2026-07-30", "15.7", "FIRE", "-", "t2"], today=T)
check("2 escalation -> superseded", st, "superseded")
check("2 state change reported", ch.get("state"), ("CALM", "FIRE"))
check("2 value change reported", ch.get("val"), ("1.0", "15.7"))
check("2 row actually rewritten", rows(p)[0][:3], ["2026-07-30", "15.7", "FIRE"])
check("2 still exactly one row", len(rows(p)), 1)

# 3 — identical re-run: no churn, no phantom change, stamp still refreshes.
st, ch = upsert_row(p, COLS, ["2026-07-30", "15.7", "FIRE", "-", "t3"], today=T)
check("3 identical -> skip-identical", (st, ch), ("skip-identical", {}))
check("3 stamp refreshed in place", rows(p)[0][4], "t3")
check("3 no duplicate row", len(rows(p)), 1)

# 4 — NULL-PRESERVING MERGE: a later degraded read (lost IV leg) must NOT
#     destroy the good stored value. This is the bug a blind overwrite would
#     have introduced while fixing the first one.
p2 = fresh()
upsert_row(p2, COLS, ["2026-07-30", "9.9", "CALM", "iv ok", "t1"])
st, ch = upsert_row(p2, COLS, ["2026-07-30", None, "CALM", "-", "t2"], today=T)
check("4 null does not overwrite", rows(p2)[0][1], "9.9")
check("4 dash does not overwrite", rows(p2)[0][3], "iv ok")
check("4 no change reported", (st, ch), ("skip-identical", {}))

# 4b — but a real value DOES replace a stored null (the recovery direction).
p2b = fresh()
upsert_row(p2b, COLS, ["2026-07-30", "-", "CALM", "-", "t1"])
st, ch = upsert_row(p2b, COLS, ["2026-07-30", "9.9", "CALM", "-", "t2"], today=T)
check("4b null -> value recovers", (rows(p2b)[0][1], st), ("9.9", "superseded"))

# 5 — supersede=False must still REPORT the divergence. A decline to write may
#     not be silent; that is the failure mode being fixed.
p3 = fresh()
upsert_row(p3, COLS, ["2026-07-30", "1.0", "CALM", "-", "t1"])
st, ch = upsert_row(p3, COLS, ["2026-07-30", "15.7", "FIRE", "-", "t2"], today=T)
_ = st
p4 = fresh()
upsert_row(p4, COLS, ["2026-07-30", "1.0", "CALM", "-", "t1"])
st, ch = upsert_row(p4, COLS, ["2026-07-30", "15.7", "FIRE", "-", "t2"], supersede=False, today=T)
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
st, ch = upsert_row(p6, COLS, ["2026-07-30", "1.0", "FIRE", "-", "t2"], today=T)
check("8 ragged row tolerated", st, "superseded")
check("8 ragged row filled", rows(p6)[0][2], "FIRE")

# 9 — a pure stamp change is NOT a data change (else every run reads as churn).
p7 = fresh()
upsert_row(p7, COLS, ["2026-07-30", "1.0", "CALM", "-", "t1"])
st, ch = upsert_row(p7, COLS, ["2026-07-30", "1.0", "CALM", "-", "t999"], today=T)
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

# 13 — COMPOSITE KEY (VIX_OPTIONS.tsv is one row per (date, expiry)). Two rows
#      sharing a date must NOT collide; the wrong one being updated would be a
#      silent data swap, so this is tested before the wiring is trusted.
KCOLS = ["date", "expiry", "call_oi", "call_vol", "state", "stamp_utc"]
p9 = fresh()
upsert_row(p9, KCOLS, ["2026-07-30", "2026-08-05", "100", "10", "-", "t1"],
           key_cols=["date", "expiry"], today="2026-07-30")
st, ch = upsert_row(p9, KCOLS, ["2026-07-30", "2026-08-19", "200", "20", "-", "t1"],
                    key_cols=["date", "expiry"], today="2026-07-30")
check("13 same date, new expiry -> appended", st, "appended")
check("13 both rows present", len(rows(p9)), 2)

# 13b — updating one expiry must leave its same-date sibling untouched.
st, ch = upsert_row(p9, KCOLS, ["2026-07-30", "2026-08-05", "100", "99", "-", "t2"],
                    key_cols=["date", "expiry"], today="2026-07-30")
check("13b right row updated", (st, rows(p9)[0][3]), ("superseded", "99"))
check("13b sibling untouched", rows(p9)[1][3], "20")
check("13b volume change reported", ch.get("call_vol"), ("10", "99"))

# 13c — the after-hours OI=0 artifact must NOT overwrite a good stored OI.
#       (0 is a real value, not a null, so this is guarded by the CALLER passing
#       "" — assert the merge honours that, which is what vix_options relies on.)
st, ch = upsert_row(p9, KCOLS, ["2026-07-30", "2026-08-05", "", "150", "-", "t3"],
                    key_cols=["date", "expiry"], today="2026-07-30")
check("13c blank OI preserves stored", rows(p9)[0][2], "100")
check("13c volume still updates", rows(p9)[0][3], "150")

# 14 — state_col=None (vix_options has no state column) must not crash describe().
msg5 = describe("superseded", "2026-07-30", {"call_vol": ("10", "99")},
                "VIX_OPTIONS.tsv", state_col=None)
check("14 no state col -> values-moved wording", "↻ values moved" in msg5, True)

print()
if FAILS:
    print(f"❌ {len(FAILS)} FAILED\n" + "\n".join(FAILS))
    sys.exit(1)
print("✅ all daily-log upsert tests pass")
