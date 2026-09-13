#!/usr/bin/env python3
"""L294 F-3 — the `.claude` parity gate passed over nothing.

DEFECT (DAEDALUS's origin-proof sweep, reproduced by PROME 2026-09-12 before
accepting it): `check_claude_dir_drift` built its name set from `Path.glob()`.
Glob on a MISSING directory yields nothing and raises nothing, so an empty
result was indistinguishable from "every definition agrees" — both trees absent
recorded `[BLOCKING] PASS · 0 agent/skill definition(s) identical`. This is the
gate that protects the definitions PROME actually launches subagents from.

ACCEPTANCE CONDITIONS (written before the fix):
  A1 both definition directories must EXIST; a missing one fails and says which.
  A2 zero comparable definitions fails even when both directories exist —
     a parity gate over nothing establishes nothing.
  A3 the three states are DISTINGUISHED in the detail text, because each is a
     different repair: absent tree · empty tree · real drift.
  A4 real drift still blocks, and identical trees still pass — the working
     behaviour is not traded away for the new guard.
  A5 the check never raises; a gate that crashes takes every later check with it
     (that is L294 F-7, a different defect, and this fix must not create it).

NEIGHBOUR CATEGORIES
  ordinary ......... identical trees pass; drifted trees block.              TESTED
  overlap .......... one tree populated, the other ABSENT — both conditions
                     true at once; must report the absent directory, not only
                     N× "only in root".                                      TESTED
  wrong owner ...... a stray non-matching file (README.md in skills/, a .txt
                     in agents/) must not be counted as a definition.        TESTED
  missing info ..... both absent / both empty ⇒ fail, never pass.            TESTED
  concurrent ....... N/A — a mid-`cp` transient reads as drift, which is a
                     TRUE positive at that instant and fail-closed is correct;
                     the check holds no state and a re-run resolves it.
"""
import pathlib
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))

import prome_gate as g  # noqa: E402


def build(tmp, root_agents=(), prome_agents=(), root_skills=(), prome_skills=(),
          make_dirs=True, extra=()):
    """Lay out a fake repo; each *_agents entry is (name, bytes)."""
    for tree, agents, skills in (("", root_agents, root_skills),
                                 ("PROME", prome_agents, prome_skills)):
        base = tmp / tree / ".claude" if tree else tmp / ".claude"
        if make_dirs:
            (base / "agents").mkdir(parents=True, exist_ok=True)
            (base / "skills").mkdir(parents=True, exist_ok=True)
        for name, body in agents:
            (base / "agents" / name).write_text(body)
        for name, body in skills:
            (base / "skills" / name).mkdir(parents=True, exist_ok=True)
            (base / "skills" / name / "SKILL.md").write_text(body)
    for relpath, body in extra:
        p = tmp / relpath
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body)
    return tmp


def run(tmp):
    real = g.ROOT
    try:
        g.ROOT = tmp
        g.results.clear()
        g.check_claude_dir_drift()
        sev, name, ok, detail, owner = g.results[-1]
        return sev, ok, detail
    finally:
        g.ROOT = real
        g.results.clear()


class ParityGate(unittest.TestCase):

    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    # ---------------------------------------------------------------- A1 / A2
    def test_both_trees_absent_FAILS(self):
        """THE REPRODUCTION. Pre-fix this recorded PASS / '0 identical'."""
        sev, ok, detail = run(self.tmp)          # nothing created at all
        self.assertEqual(sev, g.BLOCK)
        self.assertFalse(ok)
        self.assertIn("CANNOT COMPARE", detail)

    def test_one_tree_absent_FAILS_and_names_it(self):
        build(self.tmp, root_agents=[("a.md", "x")], make_dirs=True)
        shutil.rmtree(self.tmp / "PROME/.claude/agents")
        sev, ok, detail = run(self.tmp)
        self.assertFalse(ok)
        self.assertIn("PROME:.claude/agents/", detail)

    def test_both_trees_present_but_EMPTY_FAILS(self):
        """A2 — directories exist, zero definitions. Pass here would certify
        a deletion or a silent glob-pattern break as agreement."""
        build(self.tmp)                          # dirs made, no files
        sev, ok, detail = run(self.tmp)
        self.assertFalse(ok)
        self.assertIn("ZERO agent/skill definitions", detail)

    # -------------------------------------------------------------------- A3
    def test_the_three_states_are_distinguishable(self):
        absent = run(self.tmp)[2]
        build(self.tmp)
        empty = run(self.tmp)[2]
        build(self.tmp, root_agents=[("a.md", "x")], prome_agents=[("a.md", "DIFFERENT")])
        drift = run(self.tmp)[2]
        self.assertEqual(len({absent, empty, drift}), 3)
        self.assertIn("absent", absent)
        self.assertIn("ZERO", empty)
        self.assertIn("drift:", drift)

    # -------------------------------------------------------------------- A4
    def test_identical_trees_PASS(self):
        build(self.tmp,
              root_agents=[("a.md", "same"), ("b.md", "same2")],
              prome_agents=[("a.md", "same"), ("b.md", "same2")],
              root_skills=[("boot", "s")], prome_skills=[("boot", "s")])
        sev, ok, detail = run(self.tmp)
        self.assertTrue(ok, detail)
        self.assertIn("3 agent/skill definition(s) identical", detail)

    def test_byte_drift_BLOCKS(self):
        build(self.tmp, root_agents=[("a.md", "canon")], prome_agents=[("a.md", "stale")])
        sev, ok, detail = run(self.tmp)
        self.assertEqual(sev, g.BLOCK)
        self.assertFalse(ok)
        self.assertIn("agents/a.md (differs)", detail)

    def test_file_present_in_only_one_tree_BLOCKS(self):
        build(self.tmp, root_agents=[("a.md", "x"), ("solo.md", "y")],
              prome_agents=[("a.md", "x")])
        sev, ok, detail = run(self.tmp)
        self.assertFalse(ok)
        self.assertIn("solo.md (only in root)", detail)

    # ------------------------------------------------------- overlap category
    def test_populated_root_with_absent_prome_tree_reports_the_DIRECTORY(self):
        """Both conditions true at once. Reporting only N× 'only in root' would
        send the reader to copy files into a directory that does not exist."""
        build(self.tmp, root_agents=[("a.md", "x"), ("b.md", "y")])
        shutil.rmtree(self.tmp / "PROME/.claude/agents")
        sev, ok, detail = run(self.tmp)
        self.assertFalse(ok)
        self.assertIn("CANNOT COMPARE", detail)
        self.assertIn("PROME:.claude/agents/", detail)
        self.assertIn("Also found drift", detail)   # the per-file facts survive

    # --------------------------------------------------- wrong-owner category
    def test_non_definition_files_are_not_counted(self):
        build(self.tmp,
              root_agents=[("a.md", "x")], prome_agents=[("a.md", "x")],
              extra=[(".claude/agents/notes.txt", "ignore me"),
                     ("PROME/.claude/agents/notes.txt", "ignore me too"),
                     (".claude/skills/README.md", "not a SKILL.md"),
                     ("PROME/.claude/skills/README.md", "not a SKILL.md")])
        sev, ok, detail = run(self.tmp)
        self.assertTrue(ok, detail)
        self.assertIn("1 agent/skill definition(s) identical", detail)

    # -------------------------------------------------------------------- A5
    def test_never_raises_on_a_hostile_layout(self):
        """A5 — F-7 is the class where one crash kills every later check.
        A file where a directory is expected must not take the gate down."""
        (self.tmp / ".claude").mkdir(parents=True)
        (self.tmp / ".claude/agents").write_text("I am a file, not a directory")
        (self.tmp / "PROME/.claude").mkdir(parents=True)
        (self.tmp / "PROME/.claude/agents").write_text("also a file")
        sev, ok, detail = run(self.tmp)          # must not raise
        self.assertFalse(ok)

    # ------------------------------------------------------- the live repo
    def test_the_real_repo_still_passes(self):
        sev, ok, detail = run(ROOT)
        self.assertTrue(ok, detail)
        self.assertNotIn("0 agent/skill", detail)


if __name__ == "__main__":
    unittest.main()
