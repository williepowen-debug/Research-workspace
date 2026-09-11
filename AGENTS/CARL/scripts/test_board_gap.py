"""BOARD guard regression and offline boot integration tests."""
import contextlib
import importlib.util
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

def load(name, file):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

gap = load("carl_gap_review", "board_gap.py")
boot = load("carl_boot_review", "boot.py")

class BoardGapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.index, self.ledger = self.root / "INDEX.md", self.root / "ledger.tsv"
        self.ids = ["SIG-W-20260901-015", "SIG-W-20260910-005", "SIG-W-20260910-006"]
        self.index.write_text("# BOARD\n" + "\n".join(
            f"| {sid} | 2026-09-10 | CONSUMER | IMMEDIATE | WALTER → {who} | headline | file.md |"
            for sid, who in zip(self.ids, ["CARL · info: RED", "CARL", "RED · info: CARL"])))
        self.receipts([])
        self.canonical = {sid: dict(action=acts, precedence="IMMEDIATE") for sid, acts in
                          zip(self.ids, [["CARL"], ["CARL"], ["RED"]])}

    def receipts(self, ids):
        self.ledger.write_text("Signal_ID\tDisposition\n" + "".join(f"{sid}\tACTED\n" for sid in ids))

    def run_guard(self):
        out = io.StringIO()
        with patch.object(gap, "INDEX", self.index), patch.object(gap, "LEDGER", self.ledger), patch.object(gap, "load_board_signals", return_value=self.canonical, create=True), contextlib.redirect_stdout(out):
            rc = gap.main()
        return rc, out.getvalue()

    def test_action_gaps_fail_and_restored_receipts_clear(self):
        rc, out = self.run_guard()
        self.assertEqual(rc, 1)
        self.assertIn(self.ids[0], out)
        self.assertIn(self.ids[1], out)
        self.assertNotIn(self.ids[2], out)
        self.receipts(self.ids[:2])
        before = self.ledger.read_bytes()
        self.assertEqual(self.run_guard()[0], 0)
        self.assertEqual(self.ledger.read_bytes(), before)

    def test_legacy_annotated_action_and_info_only(self):
        self.index.write_text(self.index.read_text().replace("CARL · info: RED", "CARL (action — credit / labor primary) · info: RED").replace("RED · info: CARL", "(info only) · info: CARL"))
        self.canonical[self.ids[0]]["action"] = ["CARL (action — credit / labor primary)"]
        self.canonical[self.ids[2]]["action"] = []
        rc, out = self.run_guard()
        self.assertEqual(rc, 1)
        self.assertIn(self.ids[0], out)
        self.receipts(self.ids[:2])
        self.assertEqual(self.run_guard()[0], 0)

    def test_missing_or_empty_index_cannot_clear(self):
        self.index.unlink()
        self.assertEqual(self.run_guard()[0], 2)
        self.index.write_text("# BOARD\n")
        self.assertEqual(self.run_guard()[0], 2)

    def test_missing_ledger_cannot_clear(self):
        self.ledger.unlink()
        self.assertEqual(self.run_guard()[0], 2)

    def test_stale_index_cannot_hide_new_or_rerouted_signal(self):
        self.receipts(self.ids)
        self.canonical["SIG-W-20260911-001"] = dict(action=["CARL"], precedence="IMMEDIATE")
        self.assertEqual(self.run_guard()[0], 2)
        del self.canonical["SIG-W-20260911-001"]
        self.canonical[self.ids[2]]["action"] = ["CARL"]
        self.assertEqual(self.run_guard()[0], 2)

    def test_boot_propagates_gap_in_normal_and_quick_modes(self):
        for args in (["boot.py"], ["boot.py", "--quick"], ["boot.py", "--skip-abs"]):
            with self.subTest(args=args):
                def run(label, path, argv, timeout):
                    if path.name == "board_gap.py":
                        rc, output = self.run_guard()
                        return rc == 0, output, 0
                    return True, "", 0
                out = io.StringIO()
                with patch.object(sys, "argv", args), patch.object(boot, "run_script", side_effect=run), patch.object(boot, "check_ledger_staleness", return_value=[]), contextlib.redirect_stdout(out):
                    rc = boot.main()
                self.assertEqual(rc, 1)
                self.assertIn("UNRECORDED", out.getvalue())
                self.assertIn("FAIL", out.getvalue())

if __name__ == "__main__":
    unittest.main()
