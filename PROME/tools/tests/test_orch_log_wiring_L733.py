#!/usr/bin/env python3
"""L733 (2026-10-15) — the orchestration-log writer is WIRED and its use is OBSERVED.

Acceptance: PROME/tools/tests/ACCEPTANCE_L733_orch_log_wiring_2026-10-15.md (A1–A9). The defect: a validated
writer (`scripts/orch_log.py append`, 9/3) existed and no procedure routed to it, so rows were typed by hand
and the view's own header fell behind the ledger (10/15: view 1038 rows, ledger 1097).

Run: python3 -m unittest PROME/tools/tests/test_orch_log_wiring_L733.py   (from repo root)
"""
import argparse
import ast
import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1]))          # PROME/tools
import prome_gate as gate  # noqa: E402

REPO = HERE.parents[3]
_spec = importlib.util.spec_from_file_location("orch_log", REPO / "scripts" / "orch_log.py")
orch_log = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(orch_log)

HDR = "\t".join(orch_log.COLS) + "\n"


def row(date, desk, touch="1", drained="", delivered="OK"):
    return "\t".join([date, desk, "subagent", touch, "trig", drained, delivered, "OK", "n", "", "", "", ""])


def view_text(n, date="2026-10-15"):
    """The writer's own header form (orch_log.render_view line 2)."""
    return ("# ORCH_INFLIGHT — GENERATED in-flight view of `PROME/state/ORCH_LOG.tsv` … DO NOT EDIT.\n"
            f"# generated {date} · source PROME/state/ORCH_LOG.tsv ({n} data rows) · window 30d (cutoff …)\n\n"
            "## IN-FLIGHT rows (0)\n")


class ObservedCheck(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.ledger = Path(self.td.name) / "ORCH_LOG.tsv"
        self.view = Path(self.td.name) / "ORCH_INFLIGHT.md"
        self.ledger.write_text(HDR + row("2026-10-14", "SAM") + "\n" + row("2026-10-15", "HOMER", "2") + "\n", encoding="utf-8")
        gate.results.clear()

    def tearDown(self):
        self.td.cleanup()

    def last(self):
        sev, name, ok, detail, owner = gate.results[-1]
        return sev, ok, detail

    def test_A3_equal_counts_pass(self):                       # category 1: ordinary
        self.view.write_text(view_text(2), encoding="utf-8")
        self.assertTrue(gate.check_orch_log_observed(self.ledger, self.view))
        sev, ok, detail = self.last()
        self.assertEqual((sev, ok), (gate.BLOCK, True))
        self.assertIn("2 data rows == ledger 2", detail)

    def test_A3_hand_row_fails_and_names_the_delta(self):      # the 10/15 class
        self.view.write_text(view_text(2), encoding="utf-8")
        with self.ledger.open("a", encoding="utf-8") as fh:
            fh.write(row("2026-10-15", "BROCK") + "\n")       # typed by hand: the view is not regenerated
        self.assertFalse(gate.check_orch_log_observed(self.ledger, self.view))
        sev, ok, detail = self.last()
        self.assertEqual((sev, ok), (gate.BLOCK, False))
        self.assertIn("1 row(s) entered WITHOUT the writer", detail)
        self.assertIn("orch_log.py view", detail)

    def test_A3_count_not_date_same_day_hand_row(self):        # a date test would pass this; the count does not
        self.view.write_text(view_text(2, date="2026-10-15"), encoding="utf-8")
        with self.ledger.open("a", encoding="utf-8") as fh:
            fh.write(row("2026-10-15", "BROCK") + "\n")
        self.assertFalse(gate.check_orch_log_observed(self.ledger, self.view))

    def test_A5_writer_append_regenerates_and_passes(self):    # the remedy is the writer's own view
        self.view.write_text(view_text(2), encoding="utf-8")
        ns = argparse.Namespace(**{c: "" for c in orch_log.COLS})
        ns.date, ns.desk, ns.tier, ns.touch, ns.delivered = "2026-10-15", "BROCK", "subagent", "1", "IN-FLIGHT"
        self.assertEqual(orch_log.append(ns, str(self.ledger), view_path=str(self.view)), 0)
        self.assertTrue(gate.check_orch_log_observed(self.ledger, self.view))

    def test_A5_hand_row_then_view_passes(self):
        self.view.write_text(view_text(2), encoding="utf-8")
        with self.ledger.open("a", encoding="utf-8") as fh:
            fh.write(row("2026-10-15", "BROCK") + "\n")
        self.assertFalse(gate.check_orch_log_observed(self.ledger, self.view))
        self.assertEqual(orch_log.write_view(str(self.ledger), str(self.view), quiet=True), 0)
        gate.results.clear()
        self.assertTrue(gate.check_orch_log_observed(self.ledger, self.view))

    def test_A3_view_ahead_of_ledger_fails(self):
        self.view.write_text(view_text(5), encoding="utf-8")
        self.assertFalse(gate.check_orch_log_observed(self.ledger, self.view))
        self.assertIn("rows left the ledger", self.last()[2])

    def test_A4_missing_view_fails_unknown(self):              # category 4: missing information, loud
        self.assertFalse(gate.check_orch_log_observed(self.ledger, self.view))
        sev, ok, detail = self.last()
        self.assertEqual((sev, ok), (gate.BLOCK, False))
        self.assertIn("UNKNOWN", detail)

    def test_A4_header_without_count_fails_unknown(self):
        self.view.write_text("# ORCH_INFLIGHT — hand-written\n# generated 2026-10-15 by someone\n", encoding="utf-8")
        self.assertFalse(gate.check_orch_log_observed(self.ledger, self.view))
        self.assertIn("UNKNOWN", self.last()[2])

    def test_A4_unreadable_ledger_fails_unknown(self):
        self.view.write_text(view_text(2), encoding="utf-8")
        self.assertFalse(gate.check_orch_log_observed(Path(self.td.name) / "absent.tsv", self.view))
        self.assertIn("UNKNOWN: ledger unreadable", self.last()[2])

    def test_A6_archive_container_never_counted(self):         # categories 2/3: overlap + wrong owner
        self.view.write_text(view_text(2), encoding="utf-8")
        arc = Path(self.td.name) / "ORCH_LOG_2026-10.tsv"
        arc.write_text(HDR + row("2026-09-01", "SAM") + "\n" + row("2026-10-14", "SAM") + "\n", encoding="utf-8")
        self.assertTrue(gate.check_orch_log_observed(self.ledger, self.view))   # a row present in BOTH files counts once, from the hot ledger
        self.assertEqual(gate.orch_ledger_rows(self.ledger), (2, "2026-10-15"))

    def test_count_matches_the_writers_own_count(self):        # the two instruments agree on what a data row is
        with self.ledger.open("a", encoding="utf-8") as fh:
            fh.write("\n# a comment\n" + "\t".join(["2026-10-15", "PROME", "session", "CLOSE", "t", "0", "d", "OK", "n", "", "", "", ""]) + "\n")
        rc, rows = orch_log.check(str(self.ledger), quiet=True)
        self.assertEqual(rc, 0)
        self.assertEqual(gate.orch_ledger_rows(self.ledger)[0], len(rows))


class GateWiring(unittest.TestCase):
    def test_A2_A3_mode_closeout_runs_both_blocking(self):
        tree = ast.parse(Path(gate.__file__).read_text(encoding="utf-8"))
        fn = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}["mode_closeout"]
        calls = [n for n in ast.walk(fn) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]
        checks = [c for c in calls if c.func.id == "run_script"
                  and any(isinstance(a, ast.List) and any(isinstance(e, ast.Constant) and e.value == "scripts/orch_log.py" for e in a.elts)
                          for a in c.args)]
        self.assertEqual(len(checks), 1)
        self.assertEqual(checks[0].args[0].id, "BLOCK")
        self.assertTrue(any(isinstance(e, ast.Constant) and e.value == "check" for e in checks[0].args[2].elts))
        self.assertTrue(any(c.func.id == "guard" and c.args and isinstance(c.args[0], ast.Name)
                            and c.args[0].id == "check_orch_log_observed" for c in calls))

    def test_A1_every_write_site_names_the_writer(self):
        sites = ["PROME/CLOSEOUT.md", "PROME/ORCHESTRATION_PLAYBOOK.md",
                 "PROME/.claude/skills/closeout/SKILL.md", ".claude/skills/closeout/SKILL.md"]
        for s in sites:
            self.assertIn("orch_log.py append", (REPO / s).read_text(encoding="utf-8"), s)
        self.assertNotIn("every touch logs to", (REPO / "PROME/ORCHESTRATION_PLAYBOOK.md").read_text(encoding="utf-8"))
        closeout = (REPO / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        self.assertIn("scripts/orch_log.py check", closeout)          # step 7's deterministic list

    def test_A7_runner_copies_identical(self):
        a = (REPO / "PROME/.claude/skills/closeout/SKILL.md").read_bytes()
        b = (REPO / ".claude/skills/closeout/SKILL.md").read_bytes()
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
