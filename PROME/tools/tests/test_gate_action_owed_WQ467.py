#!/usr/bin/env python3
"""WQ-467 (Will 2026-10-21): the ACTION OWED class. Acceptance:
PROME/tools/tests/ACCEPTANCE_gate_action_owed_WQ467_2026-10-21.md (AO1-AO6).
Drives prome_gate.main() with mode_boot replaced by a fixture that records known rows,
so nothing in the live repository is read or written."""
import contextlib
import io
import pathlib
import re
import sys
import tempfile
import unittest
from unittest import mock

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1]))
import prome_gate as g  # noqa: E402

SRC = (HERE.parents[1] / "prome_gate.py").read_text(encoding="utf-8")


def run(rows):
    def fake_boot(advance_board=False):
        for r in rows:
            g.record(*r)
    out = io.StringIO()
    with tempfile.TemporaryDirectory() as td, mock.patch.object(g, "mode_boot", fake_boot), \
            mock.patch.object(sys, "argv", ["prome_gate.py", "boot", "--log-dir", str(pathlib.Path(td) / "logs")]), \
            contextlib.redirect_stdout(out):
        rc = g.main()
    return rc, out.getvalue()


OK_B = (g.BLOCK, "a blocking check", True, "fine", "o")
BAD_B = (g.BLOCK, "a blocking check", False, "broken", "o")
ADV_FLAG = (g.ADVISE, "an advisory check", False, "flag", "o")
ACT_FLAG = (g.ACTION, "firetime (owner-routed flags persist)", False, "rc=1 · 26 flags", "act")
ACT_OK = (g.ACTION, "firetime (owner-routed flags persist)", True, "rc=0", "act")


class ActionOwed(unittest.TestCase):
    def test_AO1_flag_prints_action_owed_not_advisory(self):
        rc, out = run([OK_B, ACT_FLAG])
        line = [l for l in out.splitlines() if "firetime (owner-routed" in l][0]
        self.assertIn("[ACTION OWED]", line)
        self.assertNotIn("[advisory]", line)

    def test_AO1_clean_run_prints_check_mark(self):
        rc, out = run([OK_B, ACT_OK])
        line = [l for l in out.splitlines() if "firetime (owner-routed" in l][0]
        self.assertTrue(line.strip().startswith("✅"))
        self.assertIn("[action  ]", line)          # a passing action-class check owes nothing (read 1, W2)
        self.assertNotIn("ACTION OWED", line)
        self.assertRegex(out, r"0 action owed")

    def test_AO2_action_flag_alone_is_rc0_pass(self):
        rc, out = run([OK_B, ACT_FLAG])
        self.assertEqual(rc, 0)
        self.assertIn("✅ PASS", out)
        self.assertEqual(g.aggregate_rc([OK_B, ACT_FLAG], []), 0)

    def test_AO3_footer_counts_owed_lines(self):
        rc, out = run([OK_B, ACT_FLAG, ACT_FLAG, ADV_FLAG])
        self.assertIn("2 ACTION OWED line(s) need a disposition", out)
        self.assertIn("SKIPPED + PARTIAL", out)
        footer = [l for l in out.splitlines() if "ACTION OWED line(s) need a disposition" in l][0]
        # read 2, R2-1: "deferred" may appear only as a route to PARTIAL, never as a clean disposition
        self.assertIn("deferred, partial or none ⇒ SKIPPED + PARTIAL", footer)
        self.assertNotIn("deferred + reason", footer)

    def test_AO3_footer_unchanged_when_none_owed(self):
        rc, out = run([OK_B, ACT_OK, ADV_FLAG])
        self.assertIn("all blocking gates pass — advisories above are judgment calls, read them.", out)
        self.assertNotIn("ACTION OWED line(s)", out)

    def test_AO4_header_counts_class_separately(self):
        rc, out = run([OK_B, ACT_FLAG, ADV_FLAG])
        self.assertRegex(out, r"1 blocking / 1 action owed / 1 advisory")

    def test_overlap_blocking_failure_wins_and_action_still_prints(self):
        rc, out = run([BAD_B, ACT_FLAG])
        self.assertEqual(rc, 1)
        self.assertIn("BLOCKING gate(s) failed", out)
        self.assertIn("[ACTION OWED]", out)

    def test_AO6_exactly_the_three_named_checks_use_action(self):
        sites = re.findall(r'(?:record|run_script)\((?:ACTION|_owed_sev\(\)),\s*(?:f?)"([^"]+)"', SRC)
        self.assertEqual(sorted(set(sites)), sorted([
            "WILL_QUEUE present",
            "PROME/inbox drained (every unfiled file, BOOT step 6)",   # 2026-10-21 inbox drain
            "WILL_QUEUE fresh + nothing due/passed/aging",
            "exempt-desk BOARD gap (§3.5 pull-complete desks vs their ledgers)",
            "firetime (owner-routed flags persist)"]))

    def test_C1_missing_queue_file_is_action_at_boot(self):
        with tempfile.TemporaryDirectory() as td, mock.patch.object(g, "ROOT", pathlib.Path(td)):
            g.results.clear(); g.GATE_MODE = "boot"
            g.check_will_queue()
            self.assertEqual(g.results[-1][0], g.ACTION)
            self.assertFalse(g.results[-1][2])

    def test_C2_closeout_mode_keeps_queue_advisory(self):
        with tempfile.TemporaryDirectory() as td, mock.patch.object(g, "ROOT", pathlib.Path(td)):
            g.results.clear(); g.GATE_MODE = "closeout"
            g.check_will_queue()
            self.assertEqual(g.results[-1][0], g.ADVISE)
        g.GATE_MODE = "boot"

    def test_W1_blocked_footer_still_counts_owed(self):
        rc, out = run([BAD_B, ACT_FLAG])
        self.assertIn("1 ACTION OWED line(s) also need a disposition", out)

class InboxDrain(unittest.TestCase):
    """2026-10-21 inbox drain; independent read ❌1: count EVERY unfiled file, whatever its name."""

    def _run(self, files):
        with tempfile.TemporaryDirectory() as td, mock.patch.object(g, "ROOT", pathlib.Path(td)):
            base = pathlib.Path(td) / "PROME/inbox"
            (base / "processed").mkdir(parents=True)
            for f in files:
                (base / f).parent.mkdir(parents=True, exist_ok=True)
                (base / f).write_text("x")
            g.results.clear(); g.GATE_MODE = "boot"
            g.check_prome_inbox()
            return g.results[-1]

    def test_every_name_shape_counts(self):
        odd = ["2026-10-21_from-REGINALD-REG27.md", "MSG-PROME-001.md", "ANVIL-reconcile-report.md",
               "2026-10-21_from-PROME_self.md", "WALTER-to-PROME_x.md", "archive/misfiled.md",
               "2026-10-21_from-WALTERX_y.md", "SIG-W-20261021-001.md", "notes.txt"]
        sev, name, ok, detail, _ = self._run(odd)
        self.assertEqual(sev, g.ACTION)
        self.assertFalse(ok)
        self.assertIn("9 unfiled file(s)", detail)

    def test_processed_and_dotfiles_do_not_count(self):
        sev, name, ok, detail, _ = self._run(["processed/2026-10-19_from-WAL_a.md", ".gitkeep", "processed/.gitkeep"])
        self.assertTrue(ok)
        self.assertIn("empty", detail)


if __name__ == "__main__":
    unittest.main()
