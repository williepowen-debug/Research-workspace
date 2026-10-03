"""Independent L530/L538 acceptance cases, 2026-10-03.

Run: python3 -B -m unittest discover -s AGENTS/DAEDALUS/tests 
     -p test_read_cap_catchup_20261003.py -v
Synthetic parser counterexamples, not a claim of exhaustive natural-language coverage.
All writes are temporary; no production charters/manifests are changed.
"""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("read_cap_review", ROOT / "scripts/read_cap_check.py")
CAP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CAP)


class ReadCapCatchup(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.home = self.root / "AGENTS/X"
        self.home.mkdir(parents=True)
        self.manifest = self.root / "READS.tsv"
        self.manifest.write_text("row_kind\treader\tpath\tmode\tdeclared_by\n"
                                 "ATTESTATION\tOTHER\t\tmanifest-complete\tOTHER\n")
        self.addCleanup(patch.stopall)
        patch.object(CAP, "ROOT", str(self.root)).start()
        patch.object(CAP, "READS_TSV", str(self.manifest)).start()
        for name in ("A.md", "B.md", "C.md"):
            (self.home / name).write_text("small\n")

    def boot(self, body):
        (self.home / "CLAUDE.md").write_text("## BOOT\n" + body + "\n## End\n")
        found, _ = CAP.boot_reads("X")
        return {Path(p).name for p in found}

    def declared(self, path, mode="whole", present=None):
        if present:
            full = self.root / present
            full.parent.mkdir(parents=True, exist_ok=True)
            full.write_text("small\n")
        self.manifest.write_text("row_kind\treader\tpath\tmode\tdeclared_by\n"
                                 "ATTESTATION\tX\t\tmanifest-complete\tX\n"
                                 f"READ\tX\t{path}\t{mode}\tX\n")
        return CAP.declared_reads("X")

    def test_inherited_two_paths(self):
        self.assertEqual(self.boot("Read these in order:\n1. `A.md` + `B.md`"), {"A.md", "B.md"})

    def test_one_initial_blank(self):
        self.assertEqual(self.boot("Read these in order:\n\n1. `A.md` + `B.md`"), {"A.md", "B.md"})

    def test_list_siblings(self):
        self.assertEqual(self.boot("Read these in order:\n1. `A.md`\n2. `B.md`"), {"A.md", "B.md"})

    def test_long_inherited_enumeration(self):
        body = "Read these in order:\n1. " + "context " * 23 + "`A.md` + `B.md`"
        self.assertEqual(self.boot(body), {"A.md", "B.md"})

    def test_no_verb(self):
        self.assertEqual(self.boot("The available files:\n1. `A.md`"), set())

    def test_negated_parent(self):
        self.assertEqual(self.boot("Do not read these:\n1. `A.md`"), set())

    def test_never_read_parent(self):
        self.assertEqual(self.boot("Never read these:\n1. `A.md`"), set())

    def test_ondemand_before_verb(self):
        self.assertEqual(self.boot("On demand, read these:\n1. `A.md`"), set())

    def test_ondemand_after_verb(self):
        self.assertEqual(self.boot("Read these on demand:\n1. `A.md`"), set())

    def test_scoped_parent(self):
        self.assertEqual(self.boot("Read only the headers:\n1. `A.md`"), set())

    def test_write_parent(self):
        self.assertEqual(self.boot("Write these:\n1. `A.md`"), set())

    def test_child_write(self):
        self.assertEqual(self.boot("Read these:\n1. Write `A.md`"), set())

    def test_child_ondemand(self):
        self.assertEqual(self.boot("Read these:\n1. `A.md` on demand"), set())

    def test_nearest_unrelated_line(self):
        self.assertEqual(self.boot("Read these:\nAn unrelated sentence.\n1. `A.md`"), set())

    def test_unrelated_sibling_command(self):
        self.assertEqual(self.boot("1. Read `A.md`.\n2. `B.md` is the write destination."), {"A.md"})

    def test_heading_ends_parent(self):
        self.assertEqual(self.boot("Read these:\n### Details\n1. `A.md`"), set())

    def test_blank_ends_active_list(self):
        self.assertEqual(self.boot("Read these:\n1. `A.md`\n\n2. `B.md`"), {"A.md"})

    def test_own_command_resets_parent(self):
        self.assertEqual(self.boot("Read these:\n1. `A.md`\n2. Write `B.md`\n3. `C.md`"), {"A.md"})

    def test_changed_indentation_ends_parent(self):
        self.assertEqual(self.boot("Read these:\n1. `A.md`\n  - `B.md`\n2. `C.md`"), {"A.md"})

    def test_child_scope_does_not_contaminate_sibling(self):
        self.assertEqual(self.boot("Read these:\n1. `A.md` headers only\n2. `B.md`"), {"B.md"})

    def test_scoped_inherited_overcap_remains_visible(self):
        (self.home / "A.md").write_text("x" * (CAP.CAP_BYTES + 1))
        self.assertEqual(self.boot("Read only the headers:\n1. `A.md`"), set())
        self.assertEqual({Path(p).name for p in CAP.boot_reads.scoped_overcap}, {"A.md"})

    def test_capable_and_clean_output(self):
        self.boot("Read these:\n1. `A.md` + `B.md`")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc, _ = CAP.check_agent("X")
        self.assertEqual(rc, 0)
        self.assertIn("READ-CAP 0 [X]", out.getvalue())
        self.assertIn("under budget (2 file(s))", out.getvalue())
        (self.home / "B.md").write_text("x" * (CAP.CAP_BYTES + 1))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc, _ = CAP.check_agent("X")
        self.assertEqual(rc, 1)
        self.assertIn("B.md", out.getvalue())
        self.assertIn("OVER THE CAP", out.getvalue())

    def test_external_concrete(self):
        cap, visible, problems, _, _ = self.declared("RESEARCH-INTAKE/data/2026-09-28/news.json", "scoped")
        self.assertEqual(cap, {})
        self.assertEqual(problems, [])
        self.assertTrue(any("EXTERNAL" in row[1] for row in visible))

    def test_external_glob(self):
        cap, visible, problems, _, _ = self.declared("RESEARCH-INTAKE/data/*/news.json", "scoped")
        self.assertEqual(cap, {})
        self.assertEqual(problems, [])
        self.assertTrue(any("EXTERNAL" in row[1] for row in visible))

    def test_similar_prefix_is_local(self):
        cap, visible, problems, _, _ = self.declared("RESEARCH-INTAKE-backup/B.md", present="RESEARCH-INTAKE-backup/B.md")
        self.assertEqual(len(cap), 1)
        self.assertEqual(visible, [])
        self.assertEqual(problems, [])

    def test_embedded_prefix_is_local(self):
        cap, visible, problems, _, _ = self.declared("AGENTS/X/RESEARCH-INTAKE/B.md", present="AGENTS/X/RESEARCH-INTAKE/B.md")
        self.assertEqual(len(cap), 1)
        self.assertEqual(visible, [])
        self.assertEqual(problems, [])

    def test_external_mode_typo_not_suppressed(self):
        _, _, problems, _, _ = self.declared("RESEARCH-INTAKE/data/file.json", "bogus")
        self.assertTrue(any(severity == CAP.P_DEFECT for severity, _ in problems))

    def test_external_glob_mode_typo_not_suppressed(self):
        _, _, problems, _, _ = self.declared("RESEARCH-INTAKE/data/*/file.json", "bogus")
        self.assertTrue(any(severity == CAP.P_DEFECT for severity, _ in problems))

    def test_external_traversal_not_suppressed(self):
        cap, visible, problems, _, _ = self.declared("RESEARCH-INTAKE/../AGENTS/X/B.md")
        # Either reject this malformed external declaration or grade its local target;
        # silently labelling a local target EXTERNAL is never acceptable.
        self.assertTrue(cap or any(severity == CAP.P_DEFECT for severity, _ in problems))
        self.assertFalse(any("EXTERNAL repo" in row[1] for row in visible))


if __name__ == "__main__":
    unittest.main()
