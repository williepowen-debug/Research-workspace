#!/usr/bin/env python3
"""Tests for PROME/tools/docket_line_stability.py — throwaway repositories only; the live
docket is never read or written. Acceptance: ACCEPTANCE_docket_line_stability_2026-10-21.md.
Neighbours: ordinary (in-place + append) · overlap (insert + edit of the next row; repeated
base lines) · wrong owner (account guard still first; hook runs for any committer) · missing
information (no base, not in index) · concurrent activity (unstaged edit vs --staged)."""
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))
import docket_line_stability as dls  # noqa: E402

HDR = "# header: rows are cited by line number\n"


def row(n, text="desc"):
    return f"2026-10-{10 + n:02d}\t{text}{n}\tPROME\tPENDING\t-\t-\n"


BASE = HDR + row(1) + row(2) + row(3) + row(4)


def kinds(base, cand):
    return [(f["kind"], f["line"]) for f in dls.scan(base.encode(), cand.encode())]


class Pure(unittest.TestCase):
    """P1/P2/P5 on scan(); no git."""

    def test_noop_passes(self):
        self.assertEqual(kinds(BASE, BASE), [])

    def test_in_place_edits_and_eof_append_pass(self):
        cand = HDR + row(1, "edited") + row(2) + row(3, "RESOLVED ") + row(4) + row(5) + row(6)
        self.assertEqual(kinds(BASE, cand), [])

    def test_mid_file_insert_is_refused(self):
        cand = HDR + row(1) + row(9) + row(2) + row(3) + row(4)
        self.assertIn(("MOVED", 4), kinds(BASE, cand))

    def test_insert_before_last_line_is_refused(self):
        cand = HDR + row(1) + row(2) + row(3) + row(9) + row(4)
        self.assertEqual(kinds(BASE, cand), [("MOVED", 6)])

    def test_swap_is_refused(self):
        cand = HDR + row(1) + row(3) + row(2) + row(4)
        self.assertEqual(kinds(BASE, cand), [("MOVED", 3), ("MOVED", 4)])

    def test_delete_plus_append_is_refused(self):
        cand = HDR + row(1) + row(3) + row(4) + row(9)
        self.assertIn(("MOVED", 3), kinds(BASE, cand))

    def test_delete_and_reappend_same_row_is_refused(self):
        cand = HDR + row(1) + row(3) + row(4) + row(2)
        self.assertIn(("MOVED", 5), kinds(BASE, cand))

    def test_eof_delete_is_refused(self):
        self.assertEqual(kinds(BASE, HDR + row(1) + row(2) + row(3)), [("ROWS-REMOVED", 5)])

    def test_insert_plus_edit_of_shifted_row_still_refused(self):
        # overlap: the row that shifts first is also edited; a later unedited row still shows it
        cand = HDR + row(1) + row(9) + row(2, "edited") + row(3) + row(4)
        self.assertIn(("MOVED", 5), kinds(BASE, cand))

    def test_repeated_base_lines_are_not_position_keys(self):
        base = HDR + "\n" + row(1) + "\n" + "# note\n" + row(2) + "# note\n"
        cand = HDR + row(9) + row(1) + "\n" + "# note\n" + row(2) + "# note\n"   # blank at L2 edited in place
        self.assertEqual(kinds(base, cand), [])

    def test_crlf_flip_plus_insert_is_refused(self):
        # reader counterexample CX1: a CRLF rewrite in the same commit must not hide an insert
        cand = (HDR + row(1) + row(9) + row(2) + row(3) + row(4)).replace("\n", "\r\n")
        self.assertIn(("MOVED", 4), kinds(BASE, cand))

    def test_crlf_flip_alone_passes(self):
        self.assertEqual(kinds(BASE, BASE.replace("\n", "\r\n")), [])

    def test_swap_with_both_rows_edited_is_a_declared_limit(self):
        # reader counterexample CX2: admitted BY DESIGN LIMIT (declared in the docstring);
        # if this ever starts failing, the limit text must change with it
        cand = HDR + row(1) + row(3, "RESOLVED ") + row(2, "RESOLVED ") + row(4)
        self.assertEqual(kinds(BASE, cand), [])

    def test_crlf_rows_compare_as_bytes(self):
        base = BASE.replace("\n", "\r\n")
        self.assertEqual(kinds(base, base + row(5).replace("\n", "\r\n")), [])
        swapped = (HDR + row(1) + row(3) + row(2) + row(4)).replace("\n", "\r\n")
        self.assertEqual(len(kinds(base, swapped)), 2)


class Repo(unittest.TestCase):
    """CLI + pre-commit hook against disposable repositories (P3/P4/P6/P7)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="docket-lines-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = pathlib.Path(self.tmp.name) / "repo"
        (self.repo / "PROME/tools").mkdir(parents=True)
        (self.repo / "scripts/githooks").mkdir(parents=True)
        for rel in ("PROME/tools/docket_line_stability.py", "PROME/tools/docket_row_cap.py",
                    "scripts/githooks/pre-commit"):
            shutil.copy2(ROOT / rel, self.repo / rel)
        self.docket = self.repo / "PROME/DOCKET.tsv"
        self.docket.write_text(BASE)
        self.git("init", "-q", "-b", "master")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("add", "--", "PROME", "scripts")
        self.git("commit", "-q", "-m", "baseline")
        self.git("config", "core.hooksPath", "scripts/githooks")

    def run_cmd(self, *args, env=None):
        e = dict(os.environ)
        e.pop("DOCKET_LINE_SHIFT_APPROVED", None)
        e.update(env or {})
        return subprocess.run(args, cwd=self.repo, capture_output=True, text=True, env=e)

    def git(self, *args, check=True, env=None):
        r = self.run_cmd("git", *args, env=env)
        if check:
            self.assertEqual(r.returncode, 0, r.stderr)
        return r

    def check(self, *extra):
        return self.run_cmd(sys.executable, "PROME/tools/docket_line_stability.py", *extra)

    def commits(self):
        return self.git("log", "--oneline").stdout.count("\n")

    def test_always_on_without_any_config(self):
        # P3: no harness_caps.env in this repo at all; row-cap is dormant, line check is not
        self.docket.write_text(HDR + row(1) + row(9) + row(2) + row(3) + row(4))
        r = self.git("commit", "-q", "PROME/DOCKET.tsv", "-m", "insert", check=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("DOCKET-LINES", r.stderr)
        self.assertEqual(self.commits(), 1)

    def test_hook_admits_in_place_edit_and_append(self):
        self.docket.write_text(HDR + row(1, "edited") + row(2) + row(3) + row(4) + row(5))
        self.git("commit", "-q", "PROME/DOCKET.tsv", "-m", "ok")
        self.assertEqual(self.commits(), 2)

    def test_hook_refuses_swap_via_index_commit(self):
        self.docket.write_text(HDR + row(1) + row(3) + row(2) + row(4))
        self.git("add", "--", "PROME/DOCKET.tsv")
        r = self.git("commit", "-q", "-m", "swap", check=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("MOVED", r.stderr)

    def test_staged_reads_index_not_worktree(self):
        # P6 / concurrent activity
        self.docket.write_text(BASE + row(5))
        self.git("add", "--", "PROME/DOCKET.tsv")
        self.docket.write_text(HDR + row(2) + row(1) + row(3) + row(4) + row(5))   # unstaged swap
        self.assertEqual(self.check("--staged").returncode, 0)
        self.assertEqual(self.check().returncode, 1)

    def test_missing_base_is_unknown_not_clean(self):
        r = self.check("--base", "HEAD~5")
        self.assertEqual(r.returncode, 2)
        self.assertIn("UNKNOWN", r.stdout)

    def test_not_in_index_is_unknown(self):
        self.git("rm", "-q", "--cached", "PROME/DOCKET.tsv")
        self.assertEqual(self.check("--staged").returncode, 2)

    def test_hook_refuses_when_checker_missing(self):
        (self.repo / "PROME/tools/docket_line_stability.py").unlink()
        self.docket.write_text(BASE + row(5))
        r = self.git("commit", "-q", "PROME/DOCKET.tsv", "-m", "x", check=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("docket_line_stability.py missing", r.stderr)

    def test_escape_passes_loudly(self):
        # P7
        self.docket.write_text(HDR + row(1) + row(3) + row(4))
        r = self.git("commit", "-q", "PROME/DOCKET.tsv", "-m", "rotation",
                     env={"DOCKET_LINE_SHIFT_APPROVED": "WQ-999 test ruling"}, check=False)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("PASSED under DOCKET_LINE_SHIFT_APPROVED=WQ-999 test ruling", r.stderr)

    def test_other_files_commit_untouched(self):
        # wrong owner: a commit without the docket never runs the docket checks
        (self.repo / "note.txt").write_text("x\n")
        self.docket.write_text(HDR + row(2) + row(1) + row(3) + row(4))   # unstaged swap present
        self.git("add", "--", "note.txt")
        self.git("commit", "-q", "note.txt", "-m", "note")
        self.assertEqual(self.commits(), 2)


if __name__ == "__main__":
    unittest.main()
