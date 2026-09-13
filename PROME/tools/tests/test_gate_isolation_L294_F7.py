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

⛔ FIXTURE CORRECTION (CODEX 2026-09-12 23:1x, Will-relayed). The first version of this
file DELETED the real PROME/CLOSEOUT.md, ran the live boot gate against the shared
checkout, and restored from a crc-verified copy. A `finally` plus a checksum is not
safety: a terminated process skips restoration, restoration can overwrite another
session's intervening edit, and the raw boot gate runs `board_scan --advance` and
other writers whose state one file's restoration does not cover. Both integration
tests now run against a throwaway repository (`gate_fixture.py`); only the FIXTURE's
CLOSEOUT is deleted and every gate write lands inside the fixture. No production file
is touched and no raw boot runs against the shared checkout.
⚠️ This is the SECOND live-state test defect in two sessions — the prior one chmod-000'd
a real credential file. The pattern, not the instance, is the finding.

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
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))  # gate_fixture

import gate_fixture  # noqa: E402
import prome_gate as g  # noqa: E402


# One fixture for the module: build it, run the gate CLEAN, then delete the
# FIXTURE's CLOSEOUT.md and run again. Two runs, one export, everything disposable.
_FIX = None
CLEAN = MISSING = None


def setUpModule():
    global _FIX, CLEAN, MISSING
    _FIX = gate_fixture.build()
    CLEAN = gate_fixture.run_gate(_FIX)
    (_FIX / "PROME/CLOSEOUT.md").unlink()          # the FIXTURE's copy, not the repo's
    MISSING = gate_fixture.run_gate(_FIX)


def tearDownModule():
    gate_fixture.destroy(_FIX)


class FixtureTouchesNothingReal(unittest.TestCase):
    """The correction itself, asserted rather than promised."""

    def test_the_fixture_is_not_the_real_repo(self):
        self.assertNotEqual(_FIX.resolve(), ROOT.resolve())
        self.assertTrue(str(_FIX).startswith(tempfile.gettempdir()))

    def test_the_real_closeout_is_present_and_untouched(self):
        self.assertTrue((ROOT / "PROME/CLOSEOUT.md").exists())

    def test_gate_writes_landed_INSIDE_the_fixture(self):
        """board_scan --advance and the dashboard receipt are writers. Their
        output must exist in the fixture, which proves it went there."""
        self.assertTrue((_FIX / "PROME/state/board_cursor.txt").exists())

    def test_the_real_board_cursor_was_not_advanced_by_these_tests(self):
        live = ROOT / "PROME/state/board_cursor.txt"
        committed = subprocess.run(
            ["git", "show", f"HEAD:PROME/state/board_cursor.txt"],
            cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(live.read_text(), committed.stdout,
                         "the live board cursor moved — a test wrote shared state")


class CleanFixturePasses(unittest.TestCase):
    """Category 1 — a controlled clean input must PASS, with no errors."""

    def test_rc_is_0(self):
        self.assertEqual(CLEAN.returncode, 0, CLEAN.stdout[-600:])

    def test_verdict_says_pass(self):
        self.assertIn("✅ PASS", CLEAN.stdout)

    def test_no_check_errored(self):
        self.assertNotIn("[ERROR", CLEAN.stdout)
        self.assertNotIn("NOT RUN", CLEAN.stdout)

    def test_stderr_clean(self):
        self.assertNotIn("Traceback", CLEAN.stderr)


class MissingInput(unittest.TestCase):
    """Conditions 1-3 against a fixture whose CLOSEOUT.md is absent.

    Pre-fix, this shape produced rc=1, EMPTY stdout, zero verdict lines and no
    summary — every already-passed check lost with it."""

    # ---- condition 1: identify the failed check
    def test_names_the_check_that_did_not_run(self):
        self.assertIn("check_symmetry DID NOT RUN", MISSING.stdout)

    def test_names_the_cause_and_the_missing_path(self):
        self.assertIn("FileNotFoundError", MISSING.stdout)
        self.assertIn("CLOSEOUT.md", MISSING.stdout)

    def test_says_the_subject_is_unknown_not_clean(self):
        self.assertIn("UNKNOWN, not clean", MISSING.stdout)

    # ---- condition 2: independent checks are RETAINED
    def test_independent_checks_still_report(self):
        printed = MISSING.stdout.count("[BLOCKING]") + MISSING.stdout.count("[advisory]")
        self.assertGreater(printed, 20, f"only {printed} checks printed")

    def test_it_retains_the_same_checks_the_clean_run_produced_minus_the_failed_one(self):
        """Stronger than a count: the surviving set must be the clean set less
        exactly the one that could not run."""
        def names(out):
            return {l.split("] ", 1)[1].split(":")[0].strip()
                    for l in out.split("\n")
                    if ("[BLOCKING]" in l or "[advisory]" in l) and "] " in l}
        lost = names(CLEAN.stdout) - names(MISSING.stdout)
        self.assertEqual(lost, {"boot↔closeout symmetry"}, f"unexpectedly lost: {lost}")

    def test_a_summary_block_is_printed_at_all(self):
        self.assertIn("PROME GATE · BOOT", MISSING.stdout)

    def test_nothing_escapes_to_stderr(self):
        self.assertNotIn("Traceback", MISSING.stderr)

    # ---- condition 3: not mistakable for PASS
    def test_rc_is_2_not_0_and_not_1(self):
        self.assertEqual(MISSING.returncode, 2)

    def test_the_verdict_line_refuses_the_word_pass(self):
        line = next(l for l in MISSING.stdout.split("\n") if "PROME GATE · BOOT" in l)
        self.assertIn("INCOMPLETE", line)
        self.assertIn("NOT A PASS", line)
        self.assertNotIn("✅", line)

    def test_the_closing_line_does_not_claim_gates_passed(self):
        self.assertNotIn("all blocking gates pass", MISSING.stdout)

    def test_the_closing_line_does_not_report_zero_blocking_failures_as_news(self):
        self.assertNotIn("0 BLOCKING gate(s) failed", MISSING.stdout)

    def test_the_not_run_count_is_in_the_header(self):
        self.assertIn("NOT RUN", MISSING.stdout)


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


if __name__ == "__main__":
    unittest.main()
