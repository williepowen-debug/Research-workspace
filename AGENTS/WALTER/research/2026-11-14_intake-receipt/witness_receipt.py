"""Isolated review witness, not a recurring checker. Run from repository root.

WALTER copy, 2026-11-14: CATO's AGENTS/CATO/runs/2026-11-14_intake-mark-witness.py (5d228e7bf6) with three
changes only: the operator captures the scan receipt instead of calling collect_alerts, the mark quotes that
receipt, and a refused mark (no state file) is read as unchanged state. CATO's own file is CATO's and is
untouched; it now stops with FileNotFoundError because its bare --mark is refused and writes nothing.

Tests the intake scanner (originally reviewed at ee86bf5fb4) using its temporary-lane fixture.
Never reads or marks the live intake lane.
"""
import contextlib
import io
import json
import sys
from unittest import mock

sys.dont_write_bytecode = True
sys.path.insert(0, "AGENTS/WALTER/tools")
import test_intake_catchup as fixture

scanner = fixture.s
case = fixture.CatchUp()
case.setUp()
try:
    read_fp = case.receipt()  # The operator reads this version.
    case.rewrite("2026-11-04", [fixture.item("late ordinary headline", "NEW")])
    case.live["jobs"]["newsweep"]["by_class"] = {"NEW": 1}
    case.lane.joinpath("liveness.json").write_text(json.dumps(case.live))
    output = io.StringIO()
    with mock.patch.object(sys, "argv", ["intake_scan.py", "--mark", "--through",
                                        "data/2026-11-04/news.json", "--receipt", read_fp]), contextlib.redirect_stdout(output):
        rc = scanner.main()
    state = json.loads(case.seen.read_text()) if case.seen.exists() else {"last_marked_batch": None, "last_marked_sha": None}
    case.lane.joinpath("data/2026-11-05").mkdir()
    case.lane.joinpath("data/2026-11-05/news.json").write_text(json.dumps({"items": []}))
    batches = scanner.news_batches("data/2026-11-05/news.json",
                                   state["last_marked_batch"], state["last_marked_sha"])
    print(json.dumps({
        "scenario": "rewrite after operator read, before mark; unchanged pathname",
        "mark_rc": rc,
        "mark_output": output.getvalue(),
        "stored_sha_is_unread_rewrite": state["last_marked_sha"] == scanner.batch_sha(
            "data/2026-11-04/news.json"),
        "next_day_scanned_batches": batches,
        "unread_rewrite_replayed": "data/2026-11-04/news.json" in batches,
    }, indent=2))
finally:
    case.tearDown()
