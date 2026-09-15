"""Behavioral regressions for the September 15 boot repair; fixtures never write live state."""
import contextlib
import datetime as dt
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import intake_scan
import walter_doctor as doctor
from version_drift_check import current_version_claims, spec_version

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "FORGE/tools/market-data"))
spec = importlib.util.spec_from_file_location("boot_test_dashboard", REPO / "FORGE/tools/market-data/dashboard.py")
dashboard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dashboard)


class BootRepairs(unittest.TestCase):
    def test_weekday_health(self):
        for today, want_med in [(14, False), (15, False), (16, True)]:
            now = dt.datetime(2026, 9, today, 20, tzinfo=dt.timezone.utc)
            with patch.object(intake_scan, "_now_utc", return_value=now):
                result = intake_scan.health({"last_run_utc": "2026-09-11T19:00:00Z", "status": "ok"})
            self.assertEqual(any(level == "MED" for level, _ in result), want_med)
            self.assertEqual(doctor._missed_weekday_runs(dt.date(2026, 9, 11), now.date()), today - 13)

    def test_invalid_freshness(self):
        for stamp in ["bad", "2026-09-11T19:00:00", "2099-01-01T00:00:00Z"]:
            self.assertTrue(any(level == "MED" for level, _ in intake_scan.health({"last_run_utc": stamp, "status": "ok"})))

    def test_dropzone_files_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dz = root / "inbox/WILL"
            dz.mkdir(parents=True)
            (dz / "nested").mkdir()
            for name in ["image.jfif", "image.jfif:Zone.Identifier", "README.md", ".gitkeep"]:
                (dz / name).touch()
            with patch.object(doctor, "WALTER", root):
                result = doctor.check_dropzone_pending()
            self.assertIn("1 item(s)", result[0][1])
            (dz / "image.jfif").unlink()
            with patch.object(doctor, "WALTER", root):
                self.assertEqual(doctor.check_dropzone_pending()[0][0], doctor.INFO)

    def test_current_claims_exclude_history(self):
        body = '| `design/X.md` | **v0.30 (current) · v0.29 (history)** |\n'
        body += '**CANONICAL —** `design/X.md` (**v0.29**) owns it. Feature introduced in X.md v0.1.'
        self.assertEqual(current_version_claims(body, "X.md"), ["0.30", "0.29"])
        self.assertIsNone(spec_version(Path('/nonexistent-boot-repair-spec.md')))

    def test_inline_drift_reaches_production_verdict(self):
        import version_drift_check as versions
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'design').mkdir()
            (root / 'design/X.md').write_text('# X v0.30\n')
            (root / 'design/SPEC_OWNERSHIP.md').write_text('| `design/X.md` | **v0.30** |\n')
            (root / 'CLAUDE.md').write_text('**CANONICAL —** `design/X.md` (**v0.29**) owns it.\n')
            with patch.object(doctor, 'WALTER', root), patch.object(versions, 'SPECS', ['design/X.md']), patch.object(versions, 'COMPANIONS', {}):
                result = doctor.check_claude_md_version_drift()
                self.assertTrue(any(level == doctor.MED and 'v0.29' in message for level, message in result))
                (root / 'CLAUDE.md').write_text('Feature landed at X.md v0.29 (history).\n')
                self.assertTrue(all(level == doctor.INFO for level, _ in doctor.check_claude_md_version_drift()))
                (root / 'design/X.md').unlink()
                self.assertTrue(any(level == doctor.MED for level, _ in doctor.check_claude_md_version_drift()))

    def test_owner_session_date_is_not_commit_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'STATUS.md').write_text('# BOND\n**Last session:** 2026-09-14 (prior 2026-09-10)\n')
            with patch.object(doctor, 'REPO', root), patch.object(doctor, '_agent_paths', return_value=('STATUS.md', '')):
                self.assertEqual(doctor._status_header_date('BOND'), dt.date(2026, 9, 14))

    def run_dashboard(self, rows, *args):
        out, err = io.StringIO(), io.StringIO()
        with patch.object(sys, "argv", ["dashboard.py", "--json", "--no-save", *args]), \
                patch.object(dashboard, "fetch_all", return_value=rows), \
                patch.object(dashboard, "load_last_state", return_value={}), \
                patch.object(dashboard, "detect_transitions", return_value={}), \
                patch.object(dashboard, "save_state") as save, \
                patch.object(dashboard, "append_log") as log, \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit) as exit_result:
                dashboard.main()
            save.assert_not_called()
            log.assert_not_called()
        return exit_result.exception.code, json.loads(out.getvalue()), err.getvalue()

    def test_missing_data_cannot_look_clean(self):
        for rows in [[], [{"name": "a", "value": None, "zone": "unknown"}],
                     [{"name": "a", "value": 5, "zone": "green"}, {"name": "b", "value": None, "zone": "unknown"}]]:
            for args in [(), ("--quiet",)]:
                code, data, err = self.run_dashboard(rows, *args)
                self.assertEqual(code, 3)
                self.assertEqual(data["data_completeness"]["status"], "INCOMPLETE")
                self.assertIn("DATA INCOMPLETE", err)

    def test_zero_and_red_are_valid_data(self):
        for value, zone in [(0, "green"), (100, "red")]:
            code, data, err = self.run_dashboard([{"name": "a", "value": value, "zone": zone}])
            self.assertEqual(code, 0)
            self.assertEqual(data["data_completeness"]["available"], 1)
            self.assertEqual(err, "")


if __name__ == "__main__":
    unittest.main()
