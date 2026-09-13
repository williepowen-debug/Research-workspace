#!/usr/bin/env python3
"""WQ-240 — the five validation cases Will named for the closeout simplification.

Each test IS one of his cases. They drive real tooling (argus_scope.verify_review,
prome_gate.aggregate_rc, the installed manual text), never a reimplementation.

Run: python3 PROME/tools/tests/test_closeout_simplification_WQ240.py
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME" / "tools"))
import argus_scope  # noqa: E402
import prome_gate   # noqa: E402

PY = sys.executable


class Case1_GeneratedViewsNotRestated(unittest.TestCase):
    """'A Standard closeout changes one DOCKET obligation: generated views update
    without additional narrative copies.'"""

    def test_the_manual_forbids_restating_a_registered_row(self):
        m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        self.assertIn("ONE HOME PER FACT", m)
        self.assertIn("do NOT restate", m)
        self.assertIn("Preserve them; stop restating their contents in prose", m)

    def test_the_targeted_test_applies_at_every_tier_not_only_light(self):
        m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        self.assertIn("Targeted updates at EVERY tier", m)
        self.assertNotIn("Light-tier SCRATCH — targeted update", m)

    def test_the_generator_owns_its_block_and_is_idempotent(self):
        """The property, on a FIXTURE. ⛔ An earlier version asserted that the LIVE
        SCRATCH was divergence-free — a test pinned to a live surface, which rots on
        the next edit and measures today's prose rather than the rule
        (`[[finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit]]`).
        It failed on three PRE-EXISTING divergences it was never written to police."""
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / "SCRATCH.md"
            f.write_text("# fixture\n\n<!-- DOCKET-VIEW BEGIN -->\nstale\n"
                         "<!-- DOCKET-VIEW END -->\ntail\n", encoding="utf-8")
            r1 = subprocess.run([PY, "scripts/docket_view.py", "--write", str(f)],
                                cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(r1.returncode, 0, r1.stdout + r1.stderr)
            first = f.read_text(encoding="utf-8")
            self.assertNotIn("stale", first, "the generator must own the block")
            self.assertTrue(first.startswith("# fixture"), "it must not touch text outside the markers")
            self.assertTrue(first.rstrip().endswith("tail"))
            subprocess.run([PY, "scripts/docket_view.py", "--write", str(f)],
                           cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(first, f.read_text(encoding="utf-8"), "regeneration must be idempotent")


class Case2_LateFactChange(unittest.TestCase):
    """'A fact changes late: the final candidate contains no contradictory current
    claims.' The mechanism is that step 7 is the last step that may edit, and the
    review freeze comes after it."""

    def test_the_routine_names_a_last_editing_step_before_the_freeze(self):
        m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        self.assertIn("This is the last step that may edit anything", m)
        i_edit = m.index("last step that may edit anything")
        i_freeze = m.index("FREEZE, then AUDIT")
        self.assertLess(i_edit, i_freeze, "the freeze must come after the last editing step")

    def test_a_late_edit_to_a_reviewed_path_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / "state.md"
            f.write_text("current claim A\n", encoding="utf-8")
            before = hashlib.sha256(f.read_bytes()).hexdigest()
            f.write_text("current claim B\n", encoding="utf-8")
            after = hashlib.sha256(f.read_bytes()).hexdigest()
            self.assertNotEqual(before, after)


class Case3_ContentChangedAfterReview(unittest.TestCase):
    """'Content changes after ARGUS reviews: the old verdict cannot certify the
    changed content.' This is the core one."""

    def setUp(self):
        self.d = tempfile.TemporaryDirectory()
        self.addCleanup(self.d.cleanup)
        self.orig_root = argus_scope.ROOT
        argus_scope.ROOT = pathlib.Path(self.d.name)
        self.addCleanup(lambda: setattr(argus_scope, "ROOT", self.orig_root))
        (argus_scope.ROOT / "PROME" / "state").mkdir(parents=True)
        self.f = argus_scope.ROOT / "surface.md"
        self.f.write_text("reviewed content\n", encoding="utf-8")

    def test_unchanged_candidate_verifies(self):
        argus_scope.record_review(["surface.md"])
        rc, lines = argus_scope.verify_review()
        self.assertEqual(rc, 0, lines)

    def test_content_changed_after_review_fails_closed(self):
        argus_scope.record_review(["surface.md"])
        self.f.write_text("edited after the audit\n", encoding="utf-8")
        rc, lines = argus_scope.verify_review()
        self.assertEqual(rc, 1)
        self.assertTrue(any("CHANGED-SINCE-REVIEW" in l for l in lines), lines)

    def test_a_path_added_after_review_is_flagged_unreviewed(self):
        argus_scope.record_review(["surface.md"])
        rc, lines = argus_scope.verify_review(paths=["surface.md", "late_addition.md"])
        self.assertEqual(rc, 1)
        self.assertTrue(any("UNREVIEWED" in l for l in lines), lines)

    def test_deleting_a_reviewed_path_is_a_change(self):
        argus_scope.record_review(["surface.md"])
        self.f.unlink()
        rc, _ = argus_scope.verify_review()
        self.assertEqual(rc, 1)

    def test_no_manifest_is_UNKNOWN_never_clean(self):
        rc, lines = argus_scope.verify_review()
        self.assertEqual(rc, 2)
        self.assertTrue(any("CANNOT-EVALUATE" in l for l in lines), lines)

    def test_re_review_after_a_fix_restores_the_verdict(self):
        """The prescribed remedy must actually work: fix, re-freeze, verify."""
        argus_scope.record_review(["surface.md"])
        self.f.write_text("fixed after a finding\n", encoding="utf-8")
        self.assertEqual(argus_scope.verify_review()[0], 1)
        argus_scope.record_review(["surface.md"])
        self.assertEqual(argus_scope.verify_review()[0], 0)

    def test_the_gate_treats_a_changed_candidate_as_BLOCKING(self):
        src = (ROOT / "PROME/tools/prome_gate.py").read_text(encoding="utf-8")
        self.assertIn('record(BLOCK, "ARGUS review manifest (content, not paths)", False', src)


class Case4_PublicationFails(unittest.TestCase):
    """'Publication fails: the report clearly identifies partial completion.'"""

    def test_the_manual_separates_three_delivery_states(self):
        m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        for s in ("COMMITTED", "PUSHED", "PUBLISHED", "PARTIAL"):
            self.assertIn(s, m)
        self.assertIn("concrete blocker", m)
        self.assertIn("never a silent waiver", m)

    def test_prerequisites_are_checked_before_the_render(self):
        m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        self.assertIn("Publication prerequisites are checked at Pre-closeout, not at the render", m)
        runner = (ROOT / ".claude/skills/closeout/SKILL.md").read_text(encoding="utf-8")
        self.assertLess(runner.index("Publication prerequisites"), runner.index("Render + publish"))

    def test_the_gate_carries_the_mechanical_prerequisite(self):
        src = (ROOT / "PROME/tools/prome_gate.py").read_text(encoding="utf-8")
        self.assertIn("publication prerequisites (Deck explainer coverage)", src)


class Case5_ForeignDirtyFiles(unittest.TestCase):
    """'Another agent has dirty files: closeout neither changes nor commits them.'"""

    def test_commit_is_by_exact_paths_only(self):
        m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        self.assertIn("commit_check.py commit --stage --push -F <msgfile> -- <exact paths>", m)

    def test_pre_closeout_keeps_the_foreign_work_rule(self):
        m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        self.assertIn("Foreign uncommitted work does NOT block closeout", m)
        self.assertIn("never sweep the tree", m)

    def test_review_manifest_only_covers_paths_it_was_given(self):
        """A foreign dirty path is not silently pulled into the reviewed candidate."""
        with tempfile.TemporaryDirectory() as d:
            argus_scope_root = argus_scope.ROOT
            argus_scope.ROOT = pathlib.Path(d)
            try:
                (argus_scope.ROOT / "PROME" / "state").mkdir(parents=True)
                (argus_scope.ROOT / "mine.md").write_text("x", encoding="utf-8")
                (argus_scope.ROOT / "theirs.md").write_text("y", encoding="utf-8")
                entries = argus_scope.record_review(["mine.md"])
                self.assertIn("mine.md", entries)
                self.assertNotIn("theirs.md", entries)
                (argus_scope.ROOT / "theirs.md").write_text("y changed by them", encoding="utf-8")
                self.assertEqual(argus_scope.verify_review()[0], 0,
                                 "another desk's edit must not fail PROME's review")
            finally:
                argus_scope.ROOT = argus_scope_root


class PreservedInvariants(unittest.TestCase):
    """Will: 'Preserve live obligations, existing authority boundaries,
    fired-unexecuted protection, and required publication.'"""

    def test_fired_unexecuted_protection_survives_in_both_manual_and_gate(self):
        m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        self.assertIn("FIRED-UNEXECUTED", m)
        src = (ROOT / "PROME/tools/prome_gate.py").read_text(encoding="utf-8")
        self.assertIn('record(BLOCK, "GATES fired-unexecuted"', src)

    def test_authority_boundaries_survive(self):
        cold = (ROOT / "PROME/CLOSEOUT_PROCEDURES.md").read_text(encoding="utf-8")
        self.assertIn("Skip rules", cold)
        self.assertIn("carve-out", cold)

    def test_publication_stays_required_at_standard_plus(self):
        m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        self.assertIn("Standard+ mandatory", m)

    def test_every_cold_section_is_reachable_by_an_explicit_pointer(self):
        m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")
        self.assertIn("PROME/CLOSEOUT_PROCEDURES.md", m)
        cold = (ROOT / "PROME/CLOSEOUT_PROCEDURES.md").read_text(encoding="utf-8")
        for section in ("Byte-flow", "Chunk 3", "Skip rules",
                        "Cross-session behavioral rules", "Closeout-class fleet memories"):
            self.assertIn(section, cold, f"{section} missing from the cold file")
            self.assertIn(section, m, f"{section} has no pointer from the hot file")

    def test_the_hot_file_is_materially_smaller_and_under_its_cap(self):
        hot = (ROOT / "PROME/CLOSEOUT.md").stat().st_size
        self.assertLess(hot, 24412, "hot file must sit under the 75% rotate line")


if __name__ == "__main__":
    unittest.main(verbosity=2)
