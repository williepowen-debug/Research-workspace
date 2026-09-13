#!/usr/bin/env python3
"""L294 F-7 — one missing input discarded the entire gate run.

REPRODUCED 2026-09-12 before repair, by removing PROME/CLOSEOUT.md (restored from a
verified crc32 copy) and running `prome_gate.py boot`:

    rc = 1                      <- the SAME code a legitimate blocking failure returns
    stdout = "" (empty)         <- zero verdict lines, no summary block
    checks printed = 0          <- the ~20 that had already PASSED were lost too
    stderr = FileNotFoundError traceback

So a gate that evaluated NOTHING was indistinguishable, by return code, from a gate
that evaluated everything and found a problem. DAEDALUS classed this "fail-LOUD, so
not false assurance — silent LOSS OF COVERAGE"; the louder half is real, but rc=1
carries no loudness to a caller that only branches on zero/non-zero.

SCOPE (Will, 2026-09-12 23:08): identify the failed check · continue checks
independent of its missing input · produce a final result that cannot be mistaken for
PASS · do NOT fabricate defaults so dependent checks can continue. These four are the
acceptance conditions; the test classes below are named for them.

rc=2 is not a new vocabulary: PROME/BOOT.md:65 already documents "rc=1 means blocking
failure, rc=2 unknown execution". The gate had simply never produced it.

NEIGHBOUR CATEGORIES
  ordinary ....... a clean run still returns 0 and still says PASS.            TESTED
  overlap ........ an ERROR *and* a real BLOCKING failure in one run — both
                   must survive into the summary, and rc must report the
                   weaker-knowledge state (2), not the stronger claim (1).     TESTED
  wrong owner .... guard() must not swallow a check's OWN recorded failure and
                   restyle it as an error; a check that runs and fails is a
                   BLOCKING fail, not a NOT-RUN.                               TESTED
  missing info ... the reproduction itself: input absent -> named ERROR.       TESTED
  concurrent ..... N/A — `results` is module-level state within one process and
                   main() clears it per run; the gate is not re-entrant and is
                   never invoked concurrently in-process.
"""
import pathlib
import shutil
import subprocess
import sys
import unittest
import zlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))

import prome_gate as g  # noqa: E402


class MissingInput(unittest.TestCase):
    """Category 4 + conditions 1, 2, 3 — the live reproduction, end to end.

    Driven through the CLI because rc and stdout ARE the contract. The input is
    restored in setUpClass's own `finally` and re-checked in tearDownClass, both
    crc-verified, so a failing test cannot leave the repo short a file."""

    TARGET = ROOT / "PROME/CLOSEOUT.md"

    # ONE gate run for the whole class, not one per test. Per-test setUp cost 144s
    # for twelve assertions about a single run, and a two-minute suite is a suite
    # people stop running. The file is restored in tearDownClass and the restore is
    # crc-verified there; each test also re-asserts the file is present, so a
    # half-restored state cannot pass silently.
    @classmethod
    def setUpClass(cls):
        cls.crc = zlib.crc32(cls.TARGET.read_bytes())
        cls.backup = pathlib.Path(f"/tmp/claude-1000/tc/_f7_{cls.TARGET.name}")
        cls.backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cls.TARGET, cls.backup)
        try:
            cls.TARGET.unlink()
            p = subprocess.run([sys.executable, str(ROOT / "PROME/tools/prome_gate.py"), "boot"],
                               cwd=ROOT, capture_output=True, text=True)
            cls.rc, cls.out, cls.err = p.returncode, p.stdout, p.stderr
        finally:
            shutil.copy2(cls.backup, cls.TARGET)

    @classmethod
    def tearDownClass(cls):
        if not cls.TARGET.exists():
            shutil.copy2(cls.backup, cls.TARGET)
        assert zlib.crc32(cls.TARGET.read_bytes()) == cls.crc, \
            "the test did not restore its input byte-for-byte"

    def setUp(self):
        self.assertTrue(self.TARGET.exists(), "input was not restored before this test")

    # ---- condition 1: identify the failed check
    def test_names_the_check_that_did_not_run(self):
        self.assertIn("check_symmetry DID NOT RUN", self.out)

    def test_names_the_cause_and_the_missing_path(self):
        self.assertIn("FileNotFoundError", self.out)
        self.assertIn("CLOSEOUT.md", self.out)

    def test_says_the_subject_is_unknown_not_clean(self):
        self.assertIn("UNKNOWN, not clean", self.out)

    # ---- condition 2: independent checks continue
    def test_the_other_checks_still_run(self):
        """Pre-fix: 0. The whole point is that the rest of the run survives."""
        printed = self.out.count("[BLOCKING]") + self.out.count("[advisory]")
        self.assertGreater(printed, 20, f"only {printed} checks printed")

    def test_a_summary_block_is_printed_at_all(self):
        """Pre-fix stdout was completely empty."""
        self.assertIn("PROME GATE · BOOT", self.out)

    def test_nothing_escapes_to_stderr(self):
        self.assertNotIn("Traceback", self.err)

    # ---- condition 3: not mistakable for PASS
    def test_rc_is_2_not_0_and_not_1(self):
        """2 = could not establish. Distinct from PASS(0) AND from BLOCKED(1),
        so a caller can tell 'we found a problem' from 'we did not look'."""
        self.assertEqual(self.rc, 2)

    def test_the_verdict_line_refuses_the_word_pass(self):
        line = next(l for l in self.out.split("\n") if "PROME GATE · BOOT" in l)
        self.assertIn("INCOMPLETE", line)
        self.assertIn("NOT A PASS", line)
        self.assertNotIn("✅", line)

    def test_the_closing_line_does_not_claim_gates_passed(self):
        self.assertNotIn("all blocking gates pass", self.out)

    def test_the_closing_line_does_not_report_zero_blocking_failures_as_news(self):
        """rc=2 with no blocking failures used to fall into the `if rc:` branch and
        print '0 BLOCKING gate(s) failed', which reads like good news."""
        self.assertNotIn("0 BLOCKING gate(s) failed", self.out)

    def test_the_not_run_count_is_in_the_header(self):
        self.assertIn("NOT RUN", self.out)


class NoFabricatedDefaults(unittest.TestCase):
    """Condition 4 — guard() records and moves on; it never invents input."""

    def test_guard_returns_None_and_does_not_retry_with_a_stub(self):
        calls = []

        def boom():
            calls.append(1)
            raise FileNotFoundError("no such input")

        g.results.clear()
        try:
            self.assertIsNone(g.guard(boom))
            self.assertEqual(len(calls), 1, "guard re-ran the check")
            self.assertEqual(len(g.results), 1)
            sev, name, ok, detail, owner = g.results[0]
            self.assertEqual(sev, g.ERROR)
            self.assertFalse(ok)
            self.assertIn("boom DID NOT RUN", name)
        finally:
            g.results.clear()

    def test_guard_passes_arguments_through_untouched(self):
        seen = {}

        def check(tier=None):
            seen["tier"] = tier

        g.results.clear()
        try:
            g.guard(check, tier="standard")
            self.assertEqual(seen, {"tier": "standard"})
            self.assertEqual(g.results, [])
        finally:
            g.results.clear()

    def test_no_bare_check_call_sites_remain(self):
        """Every check must go through guard(), or one of them is still able to
        take the whole run down. Reads CODE, not comments."""
        bare = [ln.rstrip() for ln in
                (ROOT / "PROME/tools/prome_gate.py").read_text().splitlines()
                if ln.split("#", 1)[0].startswith("    check_")]
        self.assertEqual(bare, [], f"unguarded call sites: {bare}")


class AggregateRc(unittest.TestCase):
    """The rc contract as a pure function — testable without running a boot."""

    OK = (g.BLOCK, "x", True, "", "")
    FAIL = (g.BLOCK, "x", False, "", "")
    ADV = (g.ADVISE, "x", False, "", "")
    ERR = (g.ERROR, "y DID NOT RUN", False, "", "")

    def test_clean_is_0(self):
        self.assertEqual(g.aggregate_rc([self.OK, self.ADV], []), 0)

    def test_blocking_failure_is_1(self):
        self.assertEqual(g.aggregate_rc([self.OK, self.FAIL], []), 1)

    def test_error_is_2(self):
        self.assertEqual(g.aggregate_rc([self.OK, self.ERR], []), 2)

    def test_error_OUTRANKS_a_blocking_failure(self):
        """Overlap category. With both present the run must report the weaker
        knowledge state: '1' would claim we evaluated everything and found a
        problem, when in fact some subjects were never looked at."""
        self.assertEqual(g.aggregate_rc([self.FAIL, self.ERR], []), 2)
        self.assertEqual(g.aggregate_rc([self.ERR, self.FAIL], []), 2)

    def test_an_advisory_failure_alone_is_still_0(self):
        self.assertEqual(g.aggregate_rc([self.ADV], []), 0)

    def test_capabilities_still_never_affect_rc(self):
        """WQ-239's contract must survive this change."""
        caps = [("machine credentials", g.CAP_UNAVAILABLE, "", "", "", "238")]
        self.assertEqual(g.aggregate_rc([self.OK], caps), 0)
        self.assertEqual(g.aggregate_rc([self.ERR], caps), 2)


class WrongOwner(unittest.TestCase):
    """Category 3 — a check that RUNS and fails is a BLOCKING failure, not an
    ERROR. Restyling ordinary failures as 'did not run' would inflate rc=2 and
    train the reader to ignore it."""

    def test_a_check_that_records_its_own_failure_is_not_an_ERROR(self):
        def failing_check():
            g.record(g.BLOCK, "real check", False, "found a genuine problem", "owner")

        g.results.clear()
        try:
            g.guard(failing_check)
            self.assertEqual(len(g.results), 1)
            self.assertEqual(g.results[0][0], g.BLOCK)
            self.assertEqual(g.aggregate_rc(g.results, []), 1)
        finally:
            g.results.clear()


class CleanRunUnchanged(unittest.TestCase):
    """Category 1 — the repair must not change a healthy run."""

    def test_real_boot_is_rc0_and_says_PASS(self):
        p = subprocess.run([sys.executable, str(ROOT / "PROME/tools/prome_gate.py"), "boot"],
                           cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout[-800:])
        self.assertIn("✅ PASS", p.stdout)
        self.assertNotIn("NOT RUN", p.stdout)
        self.assertNotIn("[ERROR", p.stdout)


if __name__ == "__main__":
    unittest.main()
