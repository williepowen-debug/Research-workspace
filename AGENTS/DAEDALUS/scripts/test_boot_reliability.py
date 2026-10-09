"""Bounded October 9 boot regressions; fixtures never mutate the shared Git tree."""
import contextlib
import datetime as dt
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import daedalus_gate as gate
import sweeps_due as sweeps


class BootReporting(unittest.TestCase):
    def test_rotation_survives_successful_checker_and_receipt(self):
        warning = "🟡 AGENTS/DAEDALUS/EVOLUTION.md 24,518 B rotate-tier — " + "context " * 30 + "ROTATE TO BELOW 22,785 B"
        output = "\n".join(["header over budget means grade, not failure"] * 5 + [
            warning, "  Required action: rotate the named file before writing.", "  ↳ rule 5 STOP: REMOVE 1,734 MORE B",
            "READ-CAP-RESULT v1 mode=agent desk=DAEDALUS rc=0 assessed=1 rotation_due=1"])
        ctx = {"root": "/unused", "args": SimpleNamespace(candidate=None)}
        step, argv = gate.read_cap_step("B4", "read-cap", ["fixture"], {0: gate.CLEAN, 1: gate.ADVISORY, 2: gate.UNKNOWN})
        with tempfile.TemporaryDirectory() as td, patch.object(gate, "sh", return_value=(0, output)), patch.object(gate, "fingerprint", return_value=("fixture", "a" * 40)):
            console = io.StringIO()
            with contextlib.redirect_stdout(console):
                rc = gate.run("boot", [(step, argv)], ctx, td, log_row=False)
            receipt = json.loads(next(Path(td).glob("*_boot.json")).read_text())
        self.assertEqual(rc, 0)  # DUE never becomes a failure.
        self.assertEqual(receipt["steps"][0]["rc"], 0)
        self.assertEqual(receipt["steps"][0]["class"], gate.DUE)
        for expected in (warning, "Required action: rotate the named file before writing.", "REMOVE 1,734 MORE B", "DUE"):
            self.assertIn(expected, console.getvalue())
        self.assertIn(warning, receipt["steps"][0]["findings"])

    def test_more_than_four_warnings_survive(self):
        warnings = [f"⚠️ actionable warning {i}" for i in range(7)]
        found = gate.finding_lines("\n".join(["overview over threshold"] * 8 + warnings))
        self.assertTrue(all(w in found for w in warnings))

    def test_nested_warning_keeps_unmarked_sibling_action(self):
        out = "  🟡 file needs rotation\n      ↳ ⛔ Stop below target\n      Rotate named path before writing\n"
        self.assertIn("Rotate named path before writing", gate.finding_lines(out))

    def test_read_cap_clean_and_failure_classes(self):
        for rc, expected in [(0, gate.CLEAN), (1, gate.ADVISORY), (2, gate.UNKNOWN)]:
            with self.subTest(rc=rc), patch.object(gate, "sh", return_value=(rc, f"READ-CAP-RESULT v1 mode=agent desk=DAEDALUS rc={rc} assessed=1 rotation_due=0")):
                step, _ = gate.read_cap_step("B4", "read-cap", ["fixture"], {0: gate.CLEAN, 1: gate.ADVISORY, 2: gate.UNKNOWN})
                result = step.fn({"root": "/unused"})
                self.assertEqual((result[0], result[3]), (expected, rc))
        with patch.object(gate, "sh", return_value=(1, "READ-CAP-RESULT v1 rc=1 rotation_due=2")):
            step, _ = gate.read_cap_step("C7", "read-cap", ["fixture"], {0: gate.CLEAN, 1: gate.BLOCKING, 2: gate.UNKNOWN})
            self.assertEqual(step.fn({"root": "/unused"})[0], gate.BLOCKING)

    def test_invalid_success_result_is_unknown(self):
        good = "READ-CAP-RESULT v1 mode=agent desk=DAEDALUS rc=0 assessed=1 rotation_due=0"
        bad = ["", good + "\n" + good, good + "\ntrailing output", good.replace("v1", "v2"),
               good.replace("DAEDALUS", "PROME"), good.replace("mode=agent", "mode=fleet"),
               good.replace("assessed=1", "assessed=0"), good.replace("rc=0", "rc=2"),
               good.replace("rotation_due=0", "rotation_due=-1"),
               good.replace("rotation_due=0", "rotation_due=unknown"),
               good.replace("rotation_due=0", ""), good + " rotation_due=0", good + " broken"]
        for out in bad:
            with self.subTest(out=out), patch.object(gate, "sh", return_value=(0, out)):
                step, _ = gate.read_cap_step("B4", "read-cap", ["fixture"], {0: gate.CLEAN})
                result = step.fn({"root": "/unused"})
                self.assertEqual((result[0], result[3]), (gate.UNKNOWN, 0))
        with patch.object(gate, "sh", return_value=(0, good + " future_key=ok")):
            step, _ = gate.read_cap_step("B4", "read-cap", ["fixture"], {0: gate.CLEAN})
            self.assertEqual(step.fn({"root": "/unused"})[0], gate.CLEAN)

    def test_git_failure_reports_actual_error_and_preserves_pull_hold(self):
        for rc, error in [(255, "error: cannot open '.git/FETCH_HEAD': Read-only file system\n"),
                          (128, "fatal: Could not resolve host: example.invalid\n"),
                          (None, "child timed out after 60s")]:
            with self.subTest(error=error), patch.object(gate, "sh", side_effect=[(rc, error), (0, "1\t0\n"), (0, " M AGENTS/WALTER/STATUS.md\n")]):
                step = gate.boot_registry({"root": "/unused"})[0][0]
                cls, reason, _, native_rc = step.fn({"root": "/unused"})
                self.assertEqual((cls, native_rc), (gate.UNKNOWN, rc))
                self.assertIn(error.strip(), reason)
                self.assertIn("CACHED", reason)
                self.assertIn("do NOT pull", reason)
                self.assertNotIn("offline?", reason)

    def test_git_success_still_preserves_dirty_pull_hold(self):
        with patch.object(gate, "sh", side_effect=[(0, ""), (0, "0\t0\n"), (0, " M PROME/STATUS.md\n")]):
            step = gate.boot_registry({"root": "/unused"})[0][0]
            cls, reason, _, rc = step.fn({"root": "/unused"})
        self.assertEqual((cls, rc), (gate.ENUM, 0))
        self.assertIn("do NOT pull", reason)
        self.assertNotIn("FAILED", reason)
        self.assertNotIn("CACHED", reason)


class DatedWording(unittest.TestCase):
    def check_date(self, date):
        with tempfile.TemporaryDirectory() as td:
            pb = Path(td) / "playbook.md"
            pb.write_text("fixture")
            registry = Path(td) / "registry.tsv"
            registry.write_text("task\tcadence_days\tlast_run\tplaybook\tstatus\tresolve_by\tlast_findings\n"
                                f"Scorecard\tDATED\t2026-01-01\t{pb}\tactive\t{date}\tfixture\n")
            console = io.StringIO()
            with patch.object(sweeps, "REGISTRY", str(registry)), patch.object(sweeps, "today_et", return_value=dt.date(2026, 10, 9)), patch.object(sys, "argv", ["sweeps_due.py", "--no-profile-clock", "--no-live-checks"]), contextlib.redirect_stdout(console):
                rc = sweeps.main()
            return rc, console.getvalue()

    def test_yesterday(self):
        rc, out = self.check_date("2026-10-08")
        self.assertEqual(rc, 1)
        self.assertIn("RESOLVE_BY PASSED", out)
        self.assertIn("1d past", out)

    def test_today(self):
        rc, out = self.check_date("2026-10-09")
        self.assertEqual(rc, 1)
        self.assertIn("DUE TODAY", out)
        self.assertNotIn("PASSED", out)
        self.assertNotIn("0d past", out)

    def test_tomorrow(self):
        rc, out = self.check_date("2026-10-10")
        self.assertEqual(rc, 0)
        self.assertIn("none due", out)
        self.assertNotIn("DUE TODAY", out)

    def test_invalid_date(self):
        rc, out = self.check_date("not-a-date")
        self.assertEqual(rc, 2)
        self.assertIn("NOT checked", out)

    def test_et_date_before_and_after_midnight(self):
        real_datetime = dt.datetime
        for hour, expected in [(3, dt.date(2026, 10, 8)), (4, dt.date(2026, 10, 9))]:
            with self.subTest(hour=hour), patch.object(sweeps.datetime, "datetime") as clock:
                clock.now.side_effect = lambda tz: real_datetime(2026, 10, 9, hour, 30, tzinfo=dt.timezone.utc).astimezone(tz)
                self.assertEqual(sweeps.today_et(), expected)
                self.assertEqual(str(clock.now.call_args.args[0]), "America/New_York")


if __name__ == "__main__":
    unittest.main(verbosity=2)
