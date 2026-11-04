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
from test_argus_contract import ContractFixture, sc, ac, PERIMETER
from unittest.mock import patch


# ------------------------------------------------------- F1 ROUND 3 (independent review)

class ArgusScopeRoundThree(ContractFixture):
    """Three rc-0 bypasses an independent adversarial reviewer found after I told Will the
    claim held. Each test below FAILS at 625cb7070 — that was checked, not assumed."""

    def setUp(self):
        super().setUp()
        self.fix, self.A = self.root, sc
        self.cwd0=os.getcwd();self.addCleanup(os.chdir,self.cwd0)
        self.write(sc.PERIMETER_FILE,PERIMETER)
        for name in ('argus_scope.py','argus_contract.py','argus_policy.py'):
            target=self.root/'PROME/tools'/name;target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/'PROME/tools'/name,target)
        self.base=self.commit(sc.PERIMETER_FILE,*['PROME/tools/'+n for n in ('argus_scope.py','argus_contract.py','argus_policy.py')])
        sc.record_baseline(self.base)
        self.surface=self.root/'PROME/result'
        self.freeze();sc.mark_reviewed('synthetic fixture')

    def _git(self, *a):
        return subprocess.run(["git", *a], cwd=self.fix, capture_output=True, text=True)

    # -------- ❌1 an empty candidate list establishes nothing
    def test_empty_paths_list_cannot_certify(self):
        (self.fix / "PROME/zz_r3_sneak.md").write_text("never reviewed\n")
        rc, out = self.A.verify_review(paths=[])
        self.assertEqual(rc, 2, f"an empty list must be CANNOT-EVALUATE, not a pass: {out}")
        self.assertTrue(any("empty" in l for l in out))

    def test_passing_paths_empty_is_never_safer_than_omitting_it(self):
        """THE SHAPE OF THE DEFECT: supplying the flag empty returned 0 while omitting it
        returned 1. A flag must never be more dangerous present than absent."""
        (self.fix / "PROME/zz_r3_sneak.md").write_text("never reviewed\n")
        rc_omitted, _ = self.A.verify_review(paths=None)
        rc_empty, _ = self.A.verify_review(paths=[])
        self.assertNotEqual(rc_omitted, 0)
        self.assertNotEqual(rc_empty, 0, "empty --paths certified what omitting it caught")

    def test_cli_rejects_an_empty_paths_expansion(self):
        """nargs='+' so an unset shell variable fails at the parser, not silently."""
        r = subprocess.run([sys.executable, str(self.fix / "PROME/tools/argus_scope.py"),
                            "--verify-review", "--paths"],
                           cwd=self.fix, capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("expected at least one argument", r.stderr)

    # -------- ❌2 discovery must read the repo whose content is compared
    def test_scope_discovery_ignores_the_callers_cwd(self):
        """From a second CLONE the baseline sha still resolves (shared object DB), so
        nothing raised and the OTHER checkout's empty scope certified the real one."""
        (self.fix / "PROME/zz_r3_sneak.md").write_text("never reviewed\n")
        clone = self.fix.parent / (self.fix.name + "-clone")
        subprocess.run(["git", "clone", "-q", str(self.fix), str(clone)],
                       capture_output=True, text=True)
        self.addCleanup(shutil.rmtree, clone, True)
        os.chdir(clone)
        try:
            rc, out = self.A.verify_review(paths=None)
        finally:
            os.chdir(self.fix)
        self.assertEqual(rc, 1, f"discovery followed the CWD instead of ROOT: {out}")
        self.assertTrue(any("UNCLASSIFIED" in l for l in out))

    def test_promotion_from_a_foreign_cwd_does_not_launder_the_real_repo(self):
        (self.fix / "PROME/zz_r3_sneak.md").write_text("never reviewed\n")
        clone = self.fix.parent / (self.fix.name + "-clone2")
        subprocess.run(["git", "clone", "-q", str(self.fix), str(clone)],
                       capture_output=True, text=True)
        self.addCleanup(shutil.rmtree, clone, True)
        os.chdir(clone)
        try:
            rc, msg = self.A.mark_reviewed("promote from elsewhere")
        finally:
            os.chdir(self.fix)
        self.assertNotEqual(rc, 0, f"promoted over an unreviewed addition: {msg}")

    # -------- ❌3 is REGISTERED (DOCKET L367), NOT FIXED — and this pins WHY.
    def test_the_reviewers_proposed_fix_for_excluded_paths_would_break_the_tool(self):
        """Appending `excluded` to the discovery list makes ANOTHER DESK'S dirty file block
        PROME's closeout. Recorded as a test so the next person to read that review does not
        apply the proposed fix. The diagnosis is right; the proposed remedy is not."""
        foreign = self.fix / "AGENTS/BRENT/STATUS.md"
        foreign.parent.mkdir(parents=True, exist_ok=True)
        foreign.write_text("BRENT's own live edit\n")
        lanes, excluded = self.A.build_scope(
            self.A.load_baseline()[0]["sha"], self.A.load_perimeter(), include_pending=True)
        self.assertIn("AGENTS/BRENT/STATUS.md", [e["path"] for e in excluded],
                      "the foreign file must land in `excluded` — that is what protects us")
        self.assertNotIn("AGENTS/BRENT/STATUS.md",
                         [e["path"] for e in lanes["OWNED"] + lanes["SHARED"]
                          + lanes["UNATTRIBUTED"]])

    # -------- A4: round 1 and round 2 must survive
    def test_round_one_and_two_behaviour_survives(self):
        self.assertEqual(self.A.verify_review(paths=None)[0], 0, "clean run must still pass")
        shutil.move(str(self.fix / ".git"), str(self.fix / ".git-hidden"))
        try:
            self.assertEqual(self.A.verify_review(paths=None)[0], 2, "round 2 regressed")
        finally:
            shutil.move(str(self.fix / ".git-hidden"), str(self.fix / ".git"))
        self.assertEqual(self.A.verify_review(paths=["PROME/result"])[0], 0,
                         "the explicit-complete-list escape regressed")


# ----------------------------------------------------------------- F1

class ArgusScopeFailsClosed(ContractFixture):
    """The bypass, driven end to end in a throwaway repo."""

    def setUp(self):
        super().setUp()
        self.fix,self.A=self.root,sc
        self.freeze();sc.mark_reviewed('synthetic fixture')
        self.addition=self.root/'PROME/zz_unreviewed_addition.md'
        self.reviewed_paths=['PROME/result']

    def _break_scope(self):
        broken=patch.object(ac,'inventory',side_effect=RuntimeError('git unavailable'))
        broken.start();self.addCleanup(broken.stop)

    # A6 — the guard must not make every run unevaluable
    def test_clean_run_still_returns_zero(self):
        self.assertEqual(self.A.verify_review(paths=None)[0], 0)

    # A1a — control: the check works when discovery works
    def test_unreviewed_addition_is_flagged_when_scope_discovery_works(self):
        self.addition.write_text("never reviewed\n")
        rc, out = self.A.verify_review(paths=None)
        self.assertEqual(rc, 1)
        self.assertTrue(any("UNCLASSIFIED" in l for l in out))

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
    def test_explicit_paths_do_not_bypass_broken_inventory(self):
        self.addition.write_text('never reviewed\n');self._break_scope()
        rc,out=self.A.verify_review(paths=['PROME/result'])
        self.assertEqual(rc,2,out)
        self.assertIn('CANNOT-EVALUATE',out[0])

    # ------------------------------------------------------------------
    # ROUND 2 (external, 2026-09-13): my first fix carved out "no baseline" as
    # merely NOT APPLICABLE so four content-only fixtures would keep passing.
    # load_baseline() returns None for SEVERAL conditions, not just absence —
    # including a recorded commit git cannot reach — so the carve-out WAS the
    # same bypass in a quieter form. These drive REAL git breakage, not a mocked
    # build_scope(), because the mock could never have found it.
    # ------------------------------------------------------------------

    def _hide_git(self):
        shutil.move(str(self.fix / ".git"), str(self.fix / ".git-hidden"))
        self.addCleanup(shutil.move, str(self.fix / ".git-hidden"), str(self.fix / ".git"))

    def test_real_git_breakage_makes_the_baseline_unusable(self):
        """The precondition, stated so the tests below cannot pass vacuously."""
        self._hide_git()
        base, why = self.A.load_baseline()
        self.assertIsNone(base)
        self.assertIn("not a commit", why)

    def test_unusable_baseline_cannot_certify(self):
        """THE ROUND-2 DEFECT: rc 0 over an unreviewed addition, with the output
        itself saying the recorded baseline was invalid."""
        self.addition.write_text("never reviewed\n")
        self._hide_git()
        rc, out = self.A.verify_review(paths=None)
        self.assertEqual(rc, 2, f"unusable baseline must not certify: {out}")
        self.assertTrue(any("CANNOT-EVALUATE" in l for l in out))

    def test_unusable_baseline_refuses_promotion_to_REVIEWED(self):
        self._hide_git()
        rc, msg = self.A.mark_reviewed("promote anyway")
        self.assertEqual(rc, 2, msg)

    def test_unusable_baseline_says_unknown_is_not_unnecessary(self):
        """Printing 'additions were not checked' did not protect a caller that
        accepts rc 0 — the message must carry the refusal, not a note."""
        self._hide_git()
        _, out = self.A.verify_review(paths=None)
        joined = " ".join(out)
        self.assertIn("CANNOT-EVALUATE", joined)
        self.assertIn("baseline unusable", joined)
        self.assertFalse(any("byte-identical" in l for l in out))

    def test_explicit_complete_list_cannot_escape_unusable_baseline(self):
        """Content-only comparison stays available as a DIAGNOSTIC — but only when
        the caller supplies the complete candidate list itself."""
        self.assertTrue(self.reviewed_paths, "fixture must have frozen a non-empty candidate")
        self._hide_git()
        rc, out = self.A.verify_review(paths=list(self.reviewed_paths))
        self.assertEqual(rc, 2, f"schema 3 requires an evaluable baseline: {out}")

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
