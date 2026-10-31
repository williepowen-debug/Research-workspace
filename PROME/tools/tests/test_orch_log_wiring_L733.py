#!/usr/bin/env python3
"""L733 (2026-10-15) — the orchestration-log writer is WIRED and its use is OBSERVED.

Acceptance: PROME/tools/tests/ACCEPTANCE_L733_orch_log_wiring_2026-10-15.md (A1–A9). The defect: a validated
writer (`scripts/orch_log.py append`, 9/3) existed and no procedure routed to it, so rows were typed by hand
and the view's own header fell behind the ledger (10/15: view 1038 rows, ledger 1097).

2026-10-31 (WQ-578 batch 2, #37): the OBSERVED view-count check and its tests (A3–A6, the LIMIT case) RETIRED —
its own notes said equality was not evidence of zero hand rows. The writer wiring (A1, A2, A7) is still tested here.

Run: python3 -m unittest PROME/tools/tests/test_orch_log_wiring_L733.py   (from repo root)
"""
import ast
import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1]))          # PROME/tools
import prome_gate as gate  # noqa: E402

REPO = HERE.parents[3]


class GateWiring(unittest.TestCase):
    def test_A2_mode_closeout_runs_the_validator_blocking(self):
        tree = ast.parse(Path(gate.__file__).read_text(encoding="utf-8"))
        fn = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}["mode_closeout"]
        calls = [n for n in ast.walk(fn) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]
        checks = [c for c in calls if c.func.id == "run_script"
                  and any(isinstance(a, ast.List) and any(isinstance(e, ast.Constant) and e.value == "scripts/orch_log.py" for e in a.elts)
                          for a in c.args)]
        self.assertEqual(len(checks), 1)
        self.assertEqual(checks[0].args[0].id, "BLOCK")
        self.assertTrue(any(isinstance(e, ast.Constant) and e.value == "check" for e in checks[0].args[2].elts))
        # OBSERVED retired 2026-10-31 (WQ-578 batch 2, #37): neither wired nor defined
        self.assertFalse(any(isinstance(n, ast.Name) and n.id == "check_orch_log_observed" for n in ast.walk(fn)))
        self.assertFalse(hasattr(gate, "check_orch_log_observed"))

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
