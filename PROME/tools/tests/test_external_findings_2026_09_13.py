#!/usr/bin/env python3
"""Regressions for the two external findings of 2026-09-13 that are not F2.

Conditions: PROME/tools/tests/ACCEPTANCE_three_external_findings_2026-09-13.md
(written before the edits).

F1 — `argus_scope.verify_review()` failed OPEN when scope discovery failed: it
     skipped the unreviewed-additions test and returned 0. ⛔ This is the SAME
     bypass class I previously reported CLOSED; the earlier repair added the
     fallback and wrapped it in `except: paths = None  # ... stay silent`.
     STAYING SILENT IS THE FAIL-OPEN.

F3 — `fleet_dashboard.parse_pending_will()` terminated on `[^.\\n]+`, so an item
     containing a period truncated and DROPPED its successors; and a missing
     label returned `[]`, making an empty queue and a failed parse identical.

⛔ Every test here runs against a throwaway fixture or a temp directory. Nothing
writes into the live checkout — that is F2, and it is not repeated here.
"""
import importlib.util
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import fleet_dashboard as FD  # noqa: E402
import gate_fixture  # noqa: E402


# ----------------------------------------------------------------- F1

class ArgusScopeFailsClosed(unittest.TestCase):
    """The bypass, driven end to end in a throwaway repo."""

    @classmethod
    def setUpClass(cls):
        cls.fix = gate_fixture.build()
        # The fixture exports HEAD; overlay the working-tree file under repair so the
        # suite tests the change and not the last commit.
        shutil.copy2(ROOT / "PROME/tools/argus_scope.py",
                     cls.fix / "PROME/tools/argus_scope.py")
        cls.cwd0 = os.getcwd()
        os.chdir(cls.fix)                      # argus_scope's git() has no cwd of its own
        spec = importlib.util.spec_from_file_location(
            "argus_scope_fixture", cls.fix / "PROME/tools/argus_scope.py")
        cls.A = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.A)
        cls.A.ROOT = cls.fix
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=cls.fix,
                             capture_output=True, text=True).stdout.strip()
        cls.A.record_baseline(sha)
        lanes, _ = cls.A.build_scope(sha, cls.A.load_perimeter(), include_pending=True)
        paths = [e["path"] for e in
                 lanes["OWNED"] + lanes["SHARED"] + lanes["UNATTRIBUTED"]]
        cls.A.record_review(paths)
        cls.A.mark_reviewed("fixture")
        cls.real_build_scope = cls.A.build_scope

    @classmethod
    def tearDownClass(cls):
        os.chdir(cls.cwd0)
        gate_fixture.destroy(cls.fix)

    def setUp(self):
        self.A = type(self).A
        self.A.build_scope = type(self).real_build_scope
        self.addition = self.fix / "PROME/zz_unreviewed_addition.md"

    def tearDown(self):
        self.A.build_scope = type(self).real_build_scope
        if self.addition.exists():
            self.addition.unlink()

    def _break_scope(self):
        self.A.build_scope = lambda *a, **k: (_ for _ in ()).throw(
            RuntimeError("git unavailable"))

    # A6 — the guard must not make every run unevaluable
    def test_clean_run_still_returns_zero(self):
        self.assertEqual(self.A.verify_review(paths=None)[0], 0)

    # A1a — control: the check works when discovery works
    def test_unreviewed_addition_is_flagged_when_scope_discovery_works(self):
        self.addition.write_text("never reviewed\n")
        rc, out = self.A.verify_review(paths=None)
        self.assertEqual(rc, 1)
        self.assertTrue(any("UNREVIEWED" in l for l in out))

    # A1b — THE DEFECT
    def test_scope_failure_returns_CANNOT_EVALUATE_not_a_pass(self):
        self.addition.write_text("never reviewed\n")
        self._break_scope()
        rc, out = self.A.verify_review(paths=None)
        self.assertEqual(rc, 2, "scope failure must be rc 2; 0 is the bypass")
        self.assertTrue(any("CANNOT-EVALUATE" in l for l in out))

    # A4 — the two outcomes must not render the same
    def test_it_does_not_claim_byte_identical_when_it_could_not_look(self):
        self.addition.write_text("never reviewed\n")
        self._break_scope()
        _, out = self.A.verify_review(paths=None)
        self.assertFalse(any("byte-identical" in l for l in out),
                         "a run that could not look must not print a completeness receipt")

    # A2 — promotion must refuse
    def test_promotion_to_REVIEWED_is_refused_under_scope_failure(self):
        self._break_scope()
        rc, msg = self.A.mark_reviewed("attempt")
        self.assertEqual(rc, 2)
        self.assertIn("CANNOT-EVALUATE", msg)

    # A5 + overlap — an explicit list is still honoured while discovery is broken
    def test_explicit_paths_still_work_while_discovery_is_broken(self):
        self.addition.write_text("never reviewed\n")
        self._break_scope()
        rc, out = self.A.verify_review(paths=["PROME/zz_unreviewed_addition.md"])
        self.assertEqual(rc, 1)
        self.assertTrue(any("UNREVIEWED" in l for l in out))

    def test_absent_baseline_is_named_not_silently_passed(self):
        """⚠️ A DECISION, pinned so it cannot drift into an accident.

        Two things can stop the additions check, and they are NOT the same:
          · scope discovery RAISED (git unavailable) — the reported bypass ⇒ rc 2.
          · NO BASELINE recorded — nothing to enumerate against. The content
            comparison is still complete and still governs rc, so this stays
            non-blocking, but the output must SAY the additions half did not run.
        Conflating them made four legitimate content-only verifications unevaluable;
        hiding the second would re-open a quieter version of the same hole."""
        import tempfile as _t, pathlib as _p
        d = _p.Path(_t.mkdtemp())
        (d / "PROME" / "state").mkdir(parents=True)
        (d / "surface.md").write_text("x\n", encoding="utf-8")
        saved = self.A.ROOT
        try:
            self.A.ROOT = d
            self.A.record_review(["surface.md"])
            rc, out = self.A.verify_review()
            self.assertEqual(rc, 0, out)
            self.assertTrue(any("additions were NOT checked" in l for l in out),
                            "an unchecked half must be stated, never implied complete")
            self.assertFalse(any("CANNOT-EVALUATE" in l for l in out))
        finally:
            self.A.ROOT = saved
            shutil.rmtree(d, ignore_errors=True)

    # A3 — the gate blocks at the tiers that require a review
    def test_the_closeout_gate_treats_rc2_as_blocking_at_standard(self):
        src = (ROOT / "PROME/tools/prome_gate.py").read_text()
        self.assertIn("sev = BLOCK if required else ADVISE", src)
        self.assertIn("if rc == 2:", src)


# ----------------------------------------------------------------- F3

class PendingWillParser(unittest.TestCase):
    """Generator and consumer tested TOGETHER — the contract broke because each
    was correct alone."""

    B, E = "<!-- WILLQ-VIEW BEGIN -->", "<!-- WILLQ-VIEW END -->"

    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        (self.tmp / "PROME").mkdir(parents=True)
        self.saved = FD.REPO
        FD.REPO = str(self.tmp)

    def tearDown(self):
        FD.REPO = self.saved
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write(self, body):
        (self.tmp / "PROME/SCRATCH.md").write_text(body)

    def block(self, items, label="Pending Will (2 open)"):
        return f"{self.B}\n- **{label}:** {items}\n{self.E}\n"

    # A2 — THE REPORTED CASE
    def test_an_item_containing_a_period_does_not_truncate(self):
        self.write(self.block("WQ-169 (e.g. next week) · WQ-238 (9/19)"))
        self.assertEqual(FD.parse_pending_will(),
                         ["WQ-169 (e.g. next week)", "WQ-238 (9/19)"])

    def test_the_successor_of_a_period_item_is_not_dropped(self):
        self.write(self.block("WQ-1 (v1.2 ships) · WQ-2 (x) · WQ-3 (y)"))
        self.assertEqual(len(FD.parse_pending_will()), 3)

    # A3 — empty vs unparsed
    def test_missing_block_is_UNPARSED_not_empty(self):
        self.write("no block here at all\n")
        self.assertIs(FD.parse_pending_will(), FD.PENDING_UNPARSED)

    def test_empty_queue_is_an_empty_list_not_UNPARSED(self):
        self.write(self.block("", label="Pending Will (0 open)"))
        self.assertEqual(FD.parse_pending_will(), [])

    def test_the_two_render_differently(self):
        self.write("no block\n")
        unparsed = FD.parse_pending_will()
        self.write(self.block("", label="Pending Will (0 open)"))
        empty = FD.parse_pending_will()
        self.assertIsNot(unparsed, empty)
        self.assertIs(unparsed, FD.PENDING_UNPARSED)

    # A4 — the 8/16 grouped-sub-item rule survives
    def test_grouped_sub_items_stay_one_item(self):
        self.write(self.block("(D-1 AAPL · D-10 MAIN) · WQ-9 (x)"))
        self.assertEqual(FD.parse_pending_will(), ["(D-1 AAPL · D-10 MAIN)", "WQ-9 (x)"])

    # A5
    def test_no_bold_residue_leaks_into_item_one(self):
        self.write(self.block("WQ-1 (a) · WQ-2 (b)"))
        self.assertFalse(FD.parse_pending_will()[0].startswith("*"))

    # wrong owner — prose elsewhere must not be mistaken for the block
    def test_prose_mentioning_the_label_does_not_win_over_the_block(self):
        self.write("Pending Will: PROSE-DECOY\n" + self.block("WQ-7 (real)"))
        got = FD.parse_pending_will()
        self.assertEqual(got, ["WQ-7 (real)"])

    # A6 ★ — the REAL generator driving the REAL consumer
    def test_the_actual_generator_output_parses(self):
        """willq_view.py writes the block; fleet_dashboard reads it. Neither tool
        was wrong alone — the CONTRACT between them broke, so the contract is what
        gets tested."""
        out = subprocess.run(
            [sys.executable, str(ROOT / "PROME/tools/willq_view.py"), "--check",
             str(ROOT / "PROME/SCRATCH.md")],
            capture_output=True, text=True)
        self.assertIn(out.returncode, (0, 1), out.stdout + out.stderr)
        live = FD.__dict__["REPO"]
        FD.REPO = str(ROOT)
        try:
            got = FD.parse_pending_will()
        finally:
            FD.REPO = live
        self.assertIsNot(got, FD.PENDING_UNPARSED,
                         "the live generated block no longer parses")
        self.assertTrue(all(x.startswith(("WQ-", "⛔")) for x in got),
                        f"unexpected item shape from the real generator: {got}")


if __name__ == "__main__":
    unittest.main()
