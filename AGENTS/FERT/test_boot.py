#!/usr/bin/env python3
"""
test_boot.py — falsification tests for FERT's boot instrument (boot.py).

Added 2026-10-28 (Will-approved, peer-comparison gap 5). A guard is only trusted
after it has been shown to FAIL when it should (finding_test_the_guard_not_just_the_guarded).
Each test plants one condition in a temp register and checks the verdict.

Run from anywhere:  python3 AGENTS/FERT/test_boot.py      (pure stdlib, no network)
"""
import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("fert_boot", HERE / "boot.py")
boot = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(boot)

TODAY = date(2026, 10, 28)
PRED_HDR = "ID\tDate\tPrediction\tConfidence\tTimeframe\tResolve_By\tStatus\tDate_Resolved\tOutcome\tIf_Falsified_Action\tNotes"
TRIG_HDR = "ID\tTrigger\tInstrument\tNext_Check\tCadence\tWhy_It_Wakes_You\tNotes"


def pred(rid, resolve_by, status):
    return f"{rid}\t2026-09-01\tclaim {rid}\t60%\twindow\t{resolve_by}\t{status}\t\t\tact\tnote"


def trig(rid, next_check):
    return f"{rid}\ttrigger {rid}\tsrc\t{next_check}\tweekly\twhy\tnote"


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, header, rows, comments=("# LIVE — comment line",)):
        p = self.dir / name
        p.write_text("\n".join([*comments, header, *rows]) + "\n", encoding="utf-8")
        return p

    def scan_pred(self, rows):
        p = self.write("PREDICTIONS.tsv", PRED_HDR, rows)
        return boot.dated_scan(p, "Resolve_By", "predictions", status_col="Status",
                               live_statuses={"OPEN"}, today=TODAY)

    def scan_trig(self, rows):
        p = self.write("TRIGGERS.tsv", TRIG_HDR, rows)
        return boot.dated_scan(p, "Next_Check", "triggers", today=TODAY)


class PredictionsDue(Base):
    def test_open_past_due_flags(self):
        rc, lines = self.scan_pred([pred("P-1", "2026-10-27", "OPEN")])
        self.assertEqual(rc, 1)
        self.assertIn("P-1", "\n".join(lines))

    def test_open_due_today_flags(self):
        rc, _ = self.scan_pred([pred("P-1", "2026-10-28", "OPEN")])
        self.assertEqual(rc, 1)

    def test_open_future_is_quiet_and_states_scope(self):
        rc, lines = self.scan_pred([pred("P-1", "2026-12-31", "OPEN")])
        self.assertEqual(rc, 0)
        self.assertIn("1 data row(s) scanned", lines[0])

    def test_resolved_past_due_not_flagged(self):
        rc, _ = self.scan_pred([pred("P-1", "2026-01-01", "HIT"),
                                pred("P-2", "2026-01-01", "MISS (so far — window open)")])
        self.assertEqual(rc, 0)

    def test_open_with_parenthetical_still_live(self):
        rc, _ = self.scan_pred([pred("P-1", "2026-10-01", "OPEN (re-marked 10/14)")])
        self.assertEqual(rc, 1)

    def test_open_with_unparseable_date_is_not_silent(self):
        # A live row whose due date cannot be read must never pass as "none due".
        rc, lines = self.scan_pred([pred("P-1", "TBD", "OPEN")])
        self.assertEqual(rc, 1, lines)
        self.assertIn("MALFORMED", "\n".join(lines))

    def test_open_with_blank_date_is_not_silent(self):
        rc, lines = self.scan_pred([pred("P-1", "", "OPEN")])
        self.assertEqual(rc, 1, lines)

    def test_missing_register_is_failure(self):
        rc, _ = boot.dated_scan(self.dir / "nope.tsv", "Resolve_By", "predictions",
                                status_col="Status", live_statuses={"OPEN"}, today=TODAY)
        self.assertEqual(rc, 2)


class TriggersDue(Base):
    def test_past_trigger_flags(self):
        rc, lines = self.scan_trig([trig("T1", "2026-10-20"), trig("T2", "2026-11-04")])
        self.assertEqual(rc, 1)
        joined = "\n".join(lines)
        self.assertIn("T1", joined)
        self.assertNotIn("T2", joined)

    def test_retired_rows_are_skipped(self):
        rc, _ = self.scan_trig([trig("T5", "RETIRED-PENDING-REPLACEMENT"),
                                trig("T6", "RETIRED-CONSUMED")])
        self.assertEqual(rc, 0)

    def test_unknown_non_date_trigger_is_not_silent(self):
        rc, lines = self.scan_trig([trig("T9", "next week")])
        self.assertEqual(rc, 1, lines)

    def test_no_comment_lines_still_parses(self):
        p = self.write("TRIGGERS.tsv", TRIG_HDR, [trig("T1", "2026-10-01")], comments=())
        rc, _ = boot.dated_scan(p, "Next_Check", "triggers", today=TODAY)
        self.assertEqual(rc, 1)


class AlertRunner(Base):
    def stub(self, body):
        p = self.dir / "stub.py"
        p.write_text(body, encoding="utf-8")
        return [str(p)]

    def test_clean_scope_line_is_quiet(self):
        self.assertEqual(boot.run_alert(self.stub("print('trade perimeter: 1 agent graded')")), 0)

    def test_marker_on_rc0_is_review(self):
        self.assertEqual(boot.run_alert(self.stub("print('⚠️ stale ledger')")), 1)

    def test_rc1_is_review(self):
        self.assertEqual(boot.run_alert(self.stub("import sys; print('x'); sys.exit(1)")), 1)

    def test_rc3_is_failure(self):
        self.assertEqual(boot.run_alert(self.stub("import sys; sys.exit(3)")), 2)

    def test_traceback_is_failure_not_review(self):
        # A crashed checker exits 1, like a real finding; the output tells them apart.
        self.assertEqual(boot.run_alert(self.stub("raise RuntimeError('boom')")), 2)

    def test_missing_script_is_failure(self):
        self.assertEqual(boot.run_alert([str(self.dir / "absent.py")]), 2)


_cspec = importlib.util.spec_from_file_location("fert_closeout", HERE / "closeout_check.py")
closeout = importlib.util.module_from_spec(_cspec)
_cspec.loader.exec_module(closeout)


class CloseoutClassify(Base):
    """closeout_check.py's verdict logic — the runner must not certify a crash."""

    def test_crash_text_on_rc0_is_fail(self):
        v, _ = closeout.classify(0, "Traceback (most recent call last):\n boom\nCLAIM-CHECK ✓",
                                 r"CLAIM-CHECK", lambda o: True)
        self.assertEqual(v, "FAIL")

    def test_missing_marker_on_rc0_is_fail(self):
        v, _ = closeout.classify(0, "", r"READ-CAP-RESULT v1", lambda o: True)
        self.assertEqual(v, "FAIL")

    def test_did_not_launch_is_fail(self):
        v, _ = closeout.classify(None, "FileNotFoundError", None, lambda o: True)
        self.assertEqual(v, "FAIL")

    def test_marker_and_pass(self):
        v, _ = closeout.classify(0, "CLAIM-CHECK ✓ 9 file(s) clean", r"CLAIM-CHECK",
                                 lambda o: "CLAIM-CHECK ✓" in o)
        self.assertEqual(v, "PASS")

    def test_marker_but_finding_is_look(self):
        v, _ = closeout.classify(1, "CLAIM-CHECK flagged 1", r"CLAIM-CHECK",
                                 lambda o: "CLAIM-CHECK ✓" in o)
        self.assertEqual(v, "LOOK")

    def test_real_broken_tsv_is_look(self):
        bad = self.dir / "bad.tsv"
        bad.write_text("A\tB\tC\nx\ty\n", encoding="utf-8")
        rc, out = closeout.run([closeout.PY, "scripts/tsv_append.py", "--check", str(bad)])
        v, _ = closeout.classify(rc, out, r": OK \(|inconsistent|mismatch", lambda o: ": OK (" in o)
        self.assertEqual(v, "LOOK", out)


class LiveRegisters(unittest.TestCase):
    """The real registers parse with no MALFORMED line (read-only)."""

    def test_live_predictions_and_triggers_parse(self):
        for path, col, kw in [
            (boot.PREDICTIONS, "Resolve_By", dict(status_col="Status", live_statuses={"OPEN"})),
            (boot.TRIGGERS, "Next_Check", {}),
        ]:
            rc, lines = boot.dated_scan(path, col, path.stem, **kw)
            self.assertNotEqual(rc, 2, lines)
            self.assertNotIn("MALFORMED", "\n".join(lines))


if __name__ == "__main__":
    unittest.main(verbosity=1)
