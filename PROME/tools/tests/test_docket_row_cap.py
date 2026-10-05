#!/usr/bin/env python3
"""Tests for PROME/tools/docket_row_cap.py — throwaway repositories only; the live docket
is never read or written. Five neighbour categories: ordinary · overlap (grandfathered
rows, comments, multibyte) · wrong owner (other files staged) · missing information
(no base, not a repo) · concurrent activity (pathspec commit uses a temporary index)."""
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
import docket_row_cap as cap  # noqa: E402

CAP = 100          # Pure tests
D = 2000           # Repo/hook tests: the fixture's harness_caps.env sets DOCKET_ROW_CAP_BYTES=2000
HDR = "# header comment\n"
ROW = "2026-10-10\tshort row\tPROME\tPENDING\t-\t-\n"


def row(n, size):
    base = f"2026-10-{10 + n:02d}\tdesc{n}\tPROME\tPENDING\t-\t"
    return base + "x" * (size - len(base.encode())) + "\n"


class Pure(unittest.TestCase):
    """scan() is pure; these need no git."""

    def test_new_row_under_cap_is_silent(self):
        self.assertEqual(cap.scan(HDR.encode(), (HDR + row(1, 80)).encode(), CAP), [])

    def test_new_row_over_cap_is_flagged(self):
        f = cap.scan(HDR.encode(), (HDR + row(1, 150)).encode(), CAP)
        self.assertEqual([(x["kind"], x["line"]) for x in f], [("NEW-OVER-CAP", 2)])

    def test_unchanged_oversize_row_is_grandfathered(self):
        big = HDR + row(1, 500)
        self.assertEqual(cap.scan(big.encode(), (big + row(2, 50)).encode(), CAP), [])

    def test_grandfathered_row_may_shrink_but_not_grow(self):
        base = (HDR + row(1, 500)).encode()
        self.assertEqual(cap.scan(base, (HDR + row(1, 400)).encode(), CAP), [])
        self.assertEqual(cap.scan(base, (HDR + row(1, 500)).encode(), CAP), [])
        f = cap.scan(base, (HDR + row(1, 501)).encode(), CAP)
        self.assertEqual([x["kind"] for x in f], ["GREW-OVER-CAP"])
        self.assertEqual(f[0]["base_size"], 500)

    def test_edit_pushing_small_row_over_cap_is_flagged(self):
        f = cap.scan((HDR + row(1, 80)).encode(), (HDR + row(1, 120)).encode(), CAP)
        self.assertEqual([x["kind"] for x in f], ["EDIT-OVER-CAP"])

    def test_comment_lines_are_never_findings(self):
        self.assertEqual(cap.scan(HDR.encode(), ("# " + "c" * 900 + "\n").encode(), CAP), [])

    def test_multibyte_counts_bytes_not_characters(self):
        # 60 × 'é' = 60 chars = 120 B; with a 100 B cap this is over.
        r = "2026-10-11\t" + "é" * 60 + "\tPROME\tPENDING\t-\t-\n"
        self.assertEqual(len(r.encode()), len(r) + 60)   # each é is 2 B: bytes = chars + 60
        self.assertEqual([x["kind"] for x in cap.scan(HDR.encode(), (HDR + r).encode(), 200)], [])
        self.assertEqual([x["kind"] for x in cap.scan(HDR.encode(), (HDR + r).encode(), 100)], ["NEW-OVER-CAP"])

    def test_removed_rows_are_a_finding(self):
        base = (HDR + row(1, 50) + row(2, 50)).encode()
        f = cap.scan(base, (HDR + row(1, 50)).encode(), CAP)
        self.assertEqual([(x["kind"], x["removed"]) for x in f], [("ROWS-REMOVED", 1)])

    def test_no_base_means_every_row_is_new(self):
        self.assertEqual([x["kind"] for x in cap.scan(None, (HDR + row(1, 150)).encode(), CAP)],
                         ["NEW-OVER-CAP"])


class Repo(unittest.TestCase):
    """The CLI and the pre-commit hook against disposable repositories."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="docket-cap-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = pathlib.Path(self.tmp.name) / "repo"
        (self.repo / "PROME/tools").mkdir(parents=True)
        (self.repo / "scripts/githooks").mkdir(parents=True)
        shutil.copy2(ROOT / "PROME/tools/docket_row_cap.py", self.repo / "PROME/tools/docket_row_cap.py")
        shutil.copy2(ROOT / "scripts/githooks/pre-commit", self.repo / "scripts/githooks/pre-commit")
        (self.repo / "scripts/harness_caps.env").write_text(f"# fixture\nDOCKET_ROW_CAP_BYTES={D}\n")
        self.docket = self.repo / "PROME/DOCKET.tsv"
        self.docket.write_text(HDR + row(1, 50) + row(2, D + 300))    # L3 is grandfathered (over cap at base)
        self.git("init", "-q", "-b", "master")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("add", "--", "PROME/DOCKET.tsv", "PROME/tools/docket_row_cap.py", "scripts/githooks/pre-commit",
                 "scripts/harness_caps.env")
        self.git("commit", "-q", "-m", "baseline")
        self.git("config", "core.hooksPath", "scripts/githooks")

    def run_cmd(self, *args, **kw):
        return subprocess.run(args, cwd=self.repo, capture_output=True, text=True, **kw)

    def git(self, *args, check=True):
        r = self.run_cmd("git", *args)
        if check:
            self.assertEqual(r.returncode, 0, r.stderr)
        return r

    def check(self, *extra):
        return self.run_cmd(sys.executable, "PROME/tools/docket_row_cap.py", *extra)

    def test_worktree_clean_and_flagged(self):
        self.assertEqual(self.check().returncode, 0)
        self.docket.write_text(self.docket.read_text() + row(3, D + 50))
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn(":L4 — NEW-OVER-CAP", r.stdout)

    def test_staged_reads_index_not_worktree(self):
        self.docket.write_text(self.docket.read_text() + row(3, 50))
        self.git("add", "--", "PROME/DOCKET.tsv")
        self.docket.write_text(self.docket.read_text() + row(4, D + 50))   # worktree only
        self.assertEqual(self.check("--staged").returncode, 0)
        self.assertEqual(self.check().returncode, 1)

    def test_hook_refuses_plain_and_pathspec_commits(self):
        self.docket.write_text(self.docket.read_text() + row(3, D + 50))
        self.git("add", "--", "PROME/DOCKET.tsv")
        r = self.git("commit", "-q", "-m", "over", check=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("DOCKET-ROW-CAP", r.stderr)
        # Root Git Protocol form: `git commit <path>` builds a TEMPORARY index; the hook must see it.
        self.git("reset", "-q", "--", "PROME/DOCKET.tsv")
        r = self.git("commit", "-q", "PROME/DOCKET.tsv", "-m", "over via pathspec", check=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("DOCKET-ROW-CAP", r.stderr)
        self.assertEqual(self.git("log", "--oneline").stdout.count("\n"), 1)

    def test_hook_allows_in_cap_row_and_grandfathered_shrink(self):
        text = self.docket.read_text().split("\n")
        text[2] = row(2, D + 200).rstrip("\n")                              # shrink L3 (still over cap)
        self.docket.write_text("\n".join(text) + row(3, 80))
        self.git("commit", "-q", "PROME/DOCKET.tsv", "-m", "ok")
        self.assertEqual(self.git("log", "--oneline").stdout.count("\n"), 2)

    def test_hook_silent_when_docket_not_in_commit(self):
        self.docket.write_text(self.docket.read_text() + row(3, D + 50))  # dirty but unstaged
        (self.repo / "other.txt").write_text("x\n")
        self.git("add", "--", "other.txt")
        self.git("commit", "-q", "other.txt", "-m", "unrelated")           # pathspec: docket excluded

    def test_hook_fails_closed_when_check_missing(self):
        (self.repo / "PROME/tools/docket_row_cap.py").unlink()
        self.docket.write_text(self.docket.read_text() + row(3, 50))
        r = self.git("commit", "-q", "PROME/DOCKET.tsv", "-m", "x", check=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("cannot be checked", r.stderr)

    def test_unconfigured_cap_is_dormant_and_says_so(self):
        (self.repo / "scripts/harness_caps.env").write_text("# no docket key\n")
        self.docket.write_text(self.docket.read_text() + row(3, D + 50))
        r = self.check()
        self.assertEqual(r.returncode, 0)
        self.assertIn("not configured", r.stdout)
        self.assertEqual(self.check("--cap", str(D)).returncode, 1)         # explicit cap still works
        r = self.git("commit", "-q", "PROME/DOCKET.tsv", "-m", "dormant")  # hook lets it through…
        self.assertIn("not configured", r.stderr)                            # …and git relays the notice

    def test_malformed_cap_is_unknown_and_hook_refuses(self):
        (self.repo / "scripts/harness_caps.env").write_text("DOCKET_ROW_CAP_BYTES=abc\n")
        self.docket.write_text(self.docket.read_text() + row(3, 50))
        self.assertEqual(self.check().returncode, 2)
        r = self.git("commit", "-q", "PROME/DOCKET.tsv", "-m", "x", check=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("could not run", r.stderr)

    def test_no_base_blob_is_unknown_not_clean(self):
        r = self.run_cmd(sys.executable, "PROME/tools/docket_row_cap.py", "--cap", "100", "--docket", "PROME/OTHER.tsv")
        self.assertEqual(r.returncode, 2)
        self.assertIn("UNKNOWN", r.stdout)

    def test_outside_repo_is_unknown(self):
        r = subprocess.run([sys.executable, str(self.repo / "PROME/tools/docket_row_cap.py"), "--cap", "100"],
                           cwd=self.tmp.name, capture_output=True, text=True,
                           env=dict(os.environ, GIT_CEILING_DIRECTORIES=self.tmp.name))
        self.assertEqual(r.returncode, 2)


if __name__ == "__main__":
    unittest.main()
