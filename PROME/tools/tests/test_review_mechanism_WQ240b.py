#!/usr/bin/env python3
"""WQ-240 patch — the review mechanism, exercised through the REAL CLI and a REAL
commit in a throwaway git repo.

⛔ The first suite drove the library functions. That proved the functions and left
the CLI's actual argument wiring untested — which is exactly where the defects were
(`--verify-review` never passed `paths`, so unreviewed-addition detection was dead
code, and it read the working tree while claiming to verify the delivery).

Run: python3 PROME/tools/tests/test_review_mechanism_WQ240b.py
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
TOOL = ROOT / "PROME" / "tools" / "argus_scope.py"
PY = sys.executable


class RealRepo(unittest.TestCase):
    """Each test gets its own git repo with the real tool copied in."""

    def setUp(self):
        self.d = tempfile.TemporaryDirectory()
        self.addCleanup(self.d.cleanup)
        self.repo = pathlib.Path(self.d.name)
        for sub in ("PROME/tools", "PROME/state"):
            (self.repo / sub).mkdir(parents=True)
        shutil.copy2(TOOL, self.repo / "PROME/tools/argus_scope.py")
        shutil.copy2(ROOT / "PROME/state/AUDIT_PERIMETER.tsv", self.repo / "PROME/state/")
        self.git("init", "-q", "-b", "master")
        self.git("config", "user.email", "t@t"); self.git("config", "user.name", "t")
        (self.repo / "PROME/state/argus_baseline.json").write_text("{}", encoding="utf-8")
        self.write("seed.md", "seed\n")
        self.git("add", "-A"); self.git("commit", "-qm", "seed")
        self.base = self.git("rev-parse", "HEAD").strip()
        self.run_tool("--record-baseline", self.base)

    def git(self, *a):
        return subprocess.run(["git", *a], cwd=self.repo, capture_output=True,
                              text=True, check=True).stdout

    def write(self, rel, text):
        f = self.repo / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text, encoding="utf-8")
        return rel

    def run_tool(self, *args):
        return subprocess.run([PY, "PROME/tools/argus_scope.py", *args],
                              cwd=self.repo, capture_output=True, text=True)


class Repro1_VerifyTheActualDelivery(RealRepo):
    """'Supply the exact intended commit paths, detect unreviewed additions, and
    compare the resulting commit's contents before pushing.'"""

    def test_cli_detects_an_unreviewed_addition_when_given_the_paths(self):
        self.write("a.md", "one\n")
        self.run_tool("--record-review")
        self.write("sneaked_in.md", "never reviewed\n")
        r = self.run_tool("--verify-review", "--paths", "a.md", "sneaked_in.md")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("UNREVIEWED", r.stdout)
        self.assertIn("sneaked_in.md", r.stdout)

    def test_an_addition_is_detected_even_WITHOUT_an_explicit_path_list(self):
        """⛔ This test asserted the OPPOSITE until 2026-09-12 21:5x, pinning the defect
        as if it were the contract: without `--paths` an unreviewed addition was
        invisible, so `--mark-reviewed` and the closeout gate — which both call with no
        list — could not see one. With no list supplied the tool now falls back to its
        OWN computed scope, so every caller sees additions."""
        self.write("a.md", "one\n")
        self.run_tool("--record-review")
        self.write("sneaked_in.md", "never reviewed\n")
        r = self.run_tool("--verify-review")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("UNREVIEWED", r.stdout)

    def test_mark_reviewed_refuses_when_an_unreviewed_addition_exists(self):
        """ARGUS's reproduction: promotion used to succeed with an addition present."""
        self.write("a.md", "one\n")
        self.run_tool("--record-review")
        self.write("sneaked_in.md", "never reviewed\n")
        r = self.run_tool("--mark-reviewed", "audit ran")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("REFUSED", r.stdout)

    def test_ref_HEAD_verifies_the_COMMIT_not_the_working_tree(self):
        """Edited-then-reverted: the working tree matches the freeze, the commit does not."""
        self.write("a.md", "reviewed\n")
        self.run_tool("--record-review")
        self.write("a.md", "SHIPPED BUT NOT REVIEWED\n")
        self.git("add", "-A"); self.git("commit", "-qm", "c")
        self.write("a.md", "reviewed\n")                      # revert on disk only
        self.assertEqual(self.run_tool("--verify-review").returncode, 0,
                         "working-tree check cannot see this — that is the point")
        r = self.run_tool("--verify-review", "--ref", "HEAD")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("CHANGED-SINCE-REVIEW", r.stdout)

    def test_a_clean_commit_verifies_at_ref_HEAD(self):
        self.write("a.md", "reviewed\n")
        self.run_tool("--record-review")
        self.git("add", "-A"); self.git("commit", "-qm", "c")
        r = self.run_tool("--verify-review", "--ref", "HEAD", "--paths", "a.md")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class Repro2_RepeatedCloseouts(RealRepo):
    """'Keep review receipts outside their own content fingerprint... so re-freezing
    works and Light closeouts don't inherit stale failures.'"""

    def test_receipts_are_never_part_of_the_candidate(self):
        self.write("a.md", "x\n")
        self.run_tool("--record-review")
        man = json.loads((self.repo / "PROME/state/argus_review.json").read_text())
        self.assertNotIn("PROME/state/argus_review.json", man["paths"])
        self.assertNotIn("PROME/state/argus_baseline.json", man["paths"])

    def test_refreezing_is_stable(self):
        self.write("a.md", "x\n")
        self.run_tool("--record-review")
        self.assertEqual(self.run_tool("--verify-review").returncode, 0)
        self.run_tool("--record-review")
        self.assertEqual(self.run_tool("--verify-review").returncode, 0,
                         "re-freezing must not invalidate itself")

    def test_two_consecutive_closeouts(self):
        """Closeout 1: freeze, commit, re-baseline. Closeout 2 must not inherit it."""
        self.write("a.md", "first\n")
        self.run_tool("--record-review")
        self.git("add", "-A"); self.git("commit", "-qm", "closeout 1")
        self.run_tool("--record-baseline", "HEAD")
        r = self.run_tool("--verify-review")
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("PRIOR closeout", r.stdout)
        self.write("b.md", "second\n")
        self.run_tool("--record-review")
        self.assertEqual(self.run_tool("--verify-review").returncode, 0,
                         "the second closeout must be able to freeze cleanly")

    def test_a_stale_receipt_is_CANNOT_EVALUATE_not_a_failure(self):
        self.write("a.md", "first\n")
        self.run_tool("--record-review")
        self.git("add", "-A"); self.git("commit", "-qm", "c1")
        self.run_tool("--record-baseline", "HEAD")
        (self.repo / "a.md").write_text("changed next session\n", encoding="utf-8")
        r = self.run_tool("--verify-review")
        self.assertEqual(r.returncode, 2, "a prior-session receipt must not read as this session's failure")


class Repro3_FreezeIsNotReview(RealRepo):
    """'Freezing a candidate must not itself establish that ARGUS reviewed it.'"""

    def test_record_review_writes_FROZEN(self):
        self.write("a.md", "x\n")
        self.run_tool("--record-review")
        self.assertEqual(json.loads((self.repo / "PROME/state/argus_review.json")
                                    .read_text())["verdict"], "FROZEN")

    def test_mark_reviewed_promotes_only_after_an_audit(self):
        self.write("a.md", "x\n")
        self.run_tool("--record-review")
        r = self.run_tool("--mark-reviewed", "argus run 1")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(json.loads((self.repo / "PROME/state/argus_review.json")
                                    .read_text())["verdict"], "REVIEWED")

    def test_mark_reviewed_refuses_a_moved_candidate(self):
        self.write("a.md", "x\n")
        self.run_tool("--record-review")
        self.write("a.md", "moved after the freeze\n")
        r = self.run_tool("--mark-reviewed", "argus run 1")
        self.assertEqual(r.returncode, 1)
        self.assertIn("REFUSED", r.stdout)

    def test_mark_reviewed_with_nothing_frozen_cannot_evaluate(self):
        self.assertEqual(self.run_tool("--mark-reviewed", "x").returncode, 2)


class Repro4_RequiredReviewByTier(unittest.TestCase):
    """'Pass the closeout tier into the gate. Standard/Heavy must stop when required
    review is missing or cannot be evaluated.'

    ⛔ ISOLATED. An earlier version invoked the real closeout gate against the working
    checkout, so it neither CREATED the missing-review condition nor tested in a
    throwaway repo — it read whatever state the developer's tree happened to be in and
    asserted on a printed severity LABEL rather than the resulting failure status.
    These build each condition from a fixture manifest and assert `aggregate_rc`."""

    def setUp(self):
        sys.path.insert(0, str(ROOT / "PROME" / "tools"))
        import prome_gate, argus_scope
        self.g, self.a = prome_gate, argus_scope
        self._real = argus_scope.verify_review
        self.addCleanup(lambda: setattr(argus_scope, "verify_review", self._real))
        self.g.results.clear()

    def outcome(self, tier, rc=None, lines=None, raises=None, verdict=None):
        """Create the condition, run the REAL check, return (severity, ok, aggregate_rc)."""
        if raises is not None:
            self.a.verify_review = lambda *a, **k: (_ for _ in ()).throw(raises)
        else:
            self.a.verify_review = lambda *a, **k: (rc, lines or ["fixture"])
        real_read = pathlib.Path.read_text
        if verdict is not None:
            def fake(self_path, *a, **k):
                if self_path.name == "argus_review.json":
                    return json.dumps({"verdict": verdict, "paths": {}})
                return real_read(self_path, *a, **k)
            pathlib.Path.read_text = fake
        try:
            self.g.results.clear()
            self.g.check_review_manifest(tier)
        finally:
            pathlib.Path.read_text = real_read
        sev, _, ok, _, _ = self.g.results[0]
        return sev, ok, self.g.aggregate_rc(self.g.results, [])

    def test_tier_is_a_real_cli_argument(self):
        r = subprocess.run([PY, "PROME/tools/prome_gate.py", "closeout", "--help"],
                           cwd=ROOT, capture_output=True, text=True)
        self.assertIn("--tier", r.stdout)

    def test_standard_FAILS_when_review_cannot_be_evaluated(self):
        sev, ok, rc = self.outcome("standard", rc=2)
        self.assertEqual((sev, ok, rc), (self.g.BLOCK, False, 1))

    def test_light_does_not_fail_on_the_same_condition(self):
        sev, ok, rc = self.outcome("light", rc=2)
        self.assertEqual((sev, ok, rc), (self.g.ADVISE, True, 0))

    def test_standard_FAILS_when_the_verifier_CRASHES(self):
        """The reproduction: a malformed manifest made the probe raise, and severity
        was selected AFTER the handler ran, so the aggregate returned 0."""
        sev, ok, rc = self.outcome("standard", raises=ValueError("malformed manifest"))
        self.assertEqual((sev, ok, rc), (self.g.BLOCK, False, 1))

    def test_light_still_tolerates_a_verifier_crash(self):
        sev, ok, rc = self.outcome("light", raises=ValueError("malformed manifest"))
        self.assertEqual((sev, ok, rc), (self.g.ADVISE, True, 0))

    def test_standard_FAILS_on_a_merely_frozen_candidate(self):
        sev, ok, rc = self.outcome("standard", rc=0, verdict="FROZEN")
        self.assertEqual((sev, ok, rc), (self.g.BLOCK, False, 1))

    def test_standard_PASSES_only_when_actually_reviewed(self):
        sev, ok, rc = self.outcome("standard", rc=0, verdict="REVIEWED")
        self.assertEqual((sev, ok, rc), (self.g.BLOCK, True, 0))

    def test_a_changed_candidate_fails_at_every_tier(self):
        for tier in ("light", "standard", "heavy", None):
            _, ok, rc = self.outcome(tier, rc=1)
            self.assertEqual((ok, rc), (False, 1), f"tier {tier}")


class Repro5_GenerationBeforeFreeze(unittest.TestCase):
    """'Step 10 still renders after the declared last editing step... Move those
    writes before the freeze; publish the verified artifacts afterward.'"""

    def setUp(self):
        self.m = (ROOT / "PROME/CLOSEOUT.md").read_text(encoding="utf-8")

    def test_generation_precedes_the_freeze(self):
        self.assertLess(self.m.index("ALL generation"), self.m.index("FREEZE, then AUDIT"))

    def test_the_order_is_commit_then_verify_then_push_then_publish(self):
        """Anchor on COMMANDS, which are stable, not on headings, which get reworded.
        Three of this session's test failures were headings pinned as assertions."""
        i_commit = self.m.index("commit_check.py commit --stage -F")
        i_verify = self.m.index("--verify-review --ref HEAD --paths")
        i_push = self.m.index("safe-push.sh")
        i_publish = self.m.index("Publish the verified artifacts")
        self.assertLess(i_commit, i_verify, "commit must precede verification")
        self.assertLess(i_verify, i_push, "verification must GATE the push, not follow it")
        self.assertLess(i_push, i_publish, "publication ships what was pushed")

    def test_the_commit_step_forbids_push_in_the_same_command(self):
        self.assertIn("`--push` on the commit wrapper is forbidden at this step", self.m)
        self.assertNotIn("commit --stage --push", self.m)

    def test_no_surviving_gate_command_omits_the_tier(self):
        """The contradictory-old-instruction case: a --tier-less gate command left in
        the file is a second, wrong rule."""
        import re as _re
        for m in _re.finditer(r"prome_gate\.py closeout([^\n`]*)", self.m):
            self.assertIn("--tier", m.group(1), f"gate command without --tier: {m.group(0)[:80]}")

    def test_the_manual_says_renders_write_tracked_files(self):
        self.assertIn("Renders are NOT read-only", self.m)

    def test_both_runner_copies_are_in_the_audit_perimeter(self):
        peri = (ROOT / "PROME/state/AUDIT_PERIMETER.tsv").read_text(encoding="utf-8")
        self.assertIn(".claude/skills/**", peri)
        row = [l for l in peri.splitlines() if l.startswith(".claude/skills/**")][0]
        self.assertIn("OWNED", row)

    def test_the_runner_matches_the_manual_order(self):
        r = (ROOT / ".claude/skills/closeout/SKILL.md").read_text(encoding="utf-8")
        self.assertLess(r.index("ALL generation"), r.index("FREEZE, then AUDIT"))
        self.assertIn("--ref HEAD", r)
        self.assertIn("--paths", r)
        self.assertIn("--tier", r)


if __name__ == "__main__":
    unittest.main(verbosity=2)
