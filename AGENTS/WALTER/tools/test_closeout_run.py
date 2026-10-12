"""Regression tests: tier selection, incomplete checks and source preservation."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from closeout_run import classify, plan, run


class CloseoutRun(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for p in ("PROME/DOCKET.tsv", "PROME/GATES.tsv", "PROME/WILL_QUEUE.md",
                  "AGENTS/WALTER/STATUS.md", "AGENTS/WALTER/MEMORY.md"):
            path = self.root / p; path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("unchanged\n")
        self.out = self.root / "AGENTS/WALTER/research/test-closeout"

    def ok(self, argv, root):
        if len(argv) > 1 and argv[1].endswith("walter_doctor.py"):
            return subprocess.CompletedProcess(
                argv, 0, "✓ no HIGH/MED findings — WALTER domain healthy.\n", "")
        return subprocess.CompletedProcess(argv, 0, "{}\n", "")

    def test_light_does_not_run_full_or_unselected_conditionals(self):
        names = {r[0] for r in plan(self.root, "light")}
        self.assertNotIn("doctor", names); self.assertNotIn("reads", names)
        self.assertNotIn("versions", names); self.assertNotIn("ledger-nudge", names)
        report, rc = run(self.root, "light", self.out, executor=self.ok)
        self.assertEqual(rc, 0)
        self.assertIn("UNVERIFIED", report["procedure_completion"])
        self.assertTrue(all(d["state"] == "UNVERIFIED" for d in report["manual_duties"]))

    def test_conditionals_and_full_tier(self):
        names = {r[0] for r in plan(self.root, "light", status_changed=True,
                    spec_changed=True, memory_slugs=["one"], superseded=[("old", "new")])}
        self.assertTrue({"versions", "ledger-nudge", "memory-index", "memory-length",
                         "consumer-1-peer", "consumer-1-self"} <= names)
        names = {r[0] for r in plan(self.root, "full")}
        self.assertTrue({"doctor", "reads", "basis", "versions"} <= names)

    def test_failure_and_unknown_are_not_success(self):
        for code, state in ((1, "REVIEW"), (2, "UNKNOWN")):
            def failed(argv, root):
                if argv[1].endswith("closeout_check.py"):
                    return subprocess.CompletedProcess(argv, code, "did not pass\n", "")
                return self.ok(argv, root)
            r, rc = run(self.root, "light", self.out, executor=failed)
            self.assertEqual((r["selected_check_state"], rc), (state, code))

    def test_timeout_is_visible_and_other_checks_continue(self):
        calls = []
        def timeout(argv, root):
            calls.append(argv)
            if len(calls) == 1: raise subprocess.TimeoutExpired(argv, 60)
            return self.ok(argv, root)
        r, rc = run(self.root, "light", self.out, executor=timeout)
        self.assertEqual(rc, 2); self.assertGreater(len(calls), 1)
        self.assertEqual(r["checks"][0]["state"], "UNKNOWN")

    def test_missing_required_weekday_input_not_silently_omitted(self):
        (self.root / "PROME/DOCKET.tsv").unlink()
        r, rc = run(self.root, "light", self.out, executor=self.ok)
        self.assertEqual(rc, 2)
        self.assertEqual(next(c for c in r["checks"] if c["check"] == "weekdays")["state"], "UNKNOWN")

    def test_memory_overflow_only_checked_at_full_tier(self):
        (self.root / "AGENTS/WALTER/MEMORY.md").write_text("line\n" * 101)
        r, rc = run(self.root, "full", self.out, executor=self.ok)
        self.assertEqual(rc, 1)
        self.assertEqual(next(c for c in r["checks"] if c["check"] == "local-memory-lines")["state"], "REVIEW")

    def test_runner_writes_only_evidence_not_owner_sources(self):
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        run(self.root, "light", self.out, executor=self.ok)
        self.assertTrue((self.out / "draft.md").exists())
        self.assertTrue(all(p.read_bytes() == data for p, data in before.items()))
        self.assertIn("not passes", json.loads((self.out / "checks.json").read_text())["limits"])

    def test_output_outside_owner_research_refused(self):
        with self.assertRaises(ValueError):
            run(self.root, "light", self.root / "PROME", executor=self.ok)

    def test_doctor_count_is_not_standard_rc_two(self):
        self.assertEqual(classify(2, "doctor",
            "✗ 2 item(s) need attention (HIGH/MED). See punch-list above.\n"), "REVIEW")
        self.assertEqual(classify(1, "doctor", "check raised ValueError"), "UNKNOWN")

    def actual_doctor(self, argv, root):
        if len(argv) > 1 and argv[1].endswith("walter_doctor.py"):
            return subprocess.run(argv, cwd=root, capture_output=True, text=True)
        return self.ok(argv, root)

    def assert_doctor_unrun(self):
        report, rc = run(self.root, "full", self.out, executor=self.actual_doctor)
        doctor = next(c for c in report["checks"] if c["check"] == "doctor")
        self.assertEqual(doctor["state"], "UNKNOWN")
        self.assertEqual((report["selected_check_state"], rc), ("UNKNOWN", 2))
        self.assertEqual(next(c for c in report["checks"] if c["check"] == "versions")["state"], "PASS")
        return doctor

    def test_missing_doctor_script_is_unknown_and_later_checks_continue(self):
        doctor = self.assert_doctor_unrun()
        self.assertEqual(doctor["rc"], 2)
        self.assertIn("can't open file", (self.root / doctor["output"]).read_text())

    def test_doctor_syntax_error_is_unknown_and_later_checks_continue(self):
        script = self.root / "AGENTS/WALTER/tools/walter_doctor.py"
        script.parent.mkdir(parents=True)
        script.write_text("def broken(:\n")
        doctor = self.assert_doctor_unrun()
        self.assertEqual(doctor["rc"], 1)
        self.assertIn("SyntaxError", (self.root / doctor["output"]).read_text())

    def test_completed_doctor_findings_remain_review(self):
        script = self.root / "AGENTS/WALTER/tools/walter_doctor.py"
        script.parent.mkdir(parents=True)
        script.write_text('print("✗ 2 item(s) need attention (HIGH/MED). See punch-list above.")\n'
                          'raise SystemExit(2)\n')
        report, rc = run(self.root, "full", self.out, executor=self.actual_doctor)
        doctor = next(c for c in report["checks"] if c["check"] == "doctor")
        self.assertEqual((doctor["state"], doctor["rc"]), ("REVIEW", 2))
        self.assertEqual((report["selected_check_state"], rc), ("REVIEW", 1))

    def test_doctor_incomplete_or_inconsistent_output_is_unknown(self):
        for code, output in [(0, ""), (2, "two MED findings"), (0, "partial report\n"),
                             (1, "✓ no HIGH/MED findings — WALTER domain healthy.\n")]:
            with self.subTest(code=code, output=output):
                self.assertEqual(classify(code, "doctor", output), "UNKNOWN")

    def test_crashed_check_is_unknown_not_a_completed_review(self):
        self.assertEqual(classify(1, "standard", "Traceback (most recent call last):"), "UNKNOWN")


if __name__ == "__main__": unittest.main()
