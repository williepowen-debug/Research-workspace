#!/usr/bin/env python3
"""Tests for PROME/tools/table_check.py.

The list comes from PROME/tools/tests/ACCEPTANCE_table_check_overcelled_rows.md,
written before the code, NOT from the reported symptom. Category 5 (concurrent
activity) is justified N/A there: single-pass, read-only, no state.
"""
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))

import table_check  # noqa: E402

H = "| a | b | c |\n|---|---|---|\n"


def kinds(text):
    return [(f["kind"], f["line"], f["observed"]) for f in table_check.scan_text(text)]


class TestOrdinary(unittest.TestCase):
    """Category 1 — the plain case works."""

    def test_wellformed_row_is_silent(self):
        self.assertEqual(kinds(H + "| 1 | 2 | 3 |\n"), [])

    def test_overcelled_row_is_flagged(self):
        f = table_check.scan_text(H + "| 1 | 2 | 3 | 4 | 5 |\n")
        self.assertEqual(len(f), 1)
        self.assertEqual(f[0]["kind"], "OVER")
        self.assertEqual((f[0]["width"], f[0]["observed"]), (3, 5))

    def test_report_names_the_dropped_cells(self):
        """Condition 6 — locatable without a second pass."""
        f = table_check.scan_text(H + "| 1 | 2 | 3 | LOST-A | LOST-B |\n")[0]
        self.assertEqual(f["dropped"], ["LOST-A", "LOST-B"])
        self.assertEqual(f["line"], 3)
        self.assertEqual(f["header_line"], 1)

    def test_the_real_regression_status_L21_shape(self):
        """The row that caused this: 5 cells, 3-column table, 2 cells lost."""
        row = ("| `CLOSEOUT.md` decision | `PROME/DOCKET.tsv` L338 | state text "
               "| L339 leg (g) lands here | NOT TAKEN 2026-09-12 |\n")
        f = table_check.scan_text(H + row)
        self.assertEqual([x["kind"] for x in f], ["OVER"])
        self.assertEqual(len(f[0]["dropped"]), 2)


class TestUnderCelledIsADifferentClass(unittest.TestCase):
    """Condition 2 — short rows are padded by markdown; not the same finding."""

    def test_short_row_is_UNDER_not_OVER(self):
        self.assertEqual(kinds(H + "| 1 | 2 |\n"), [("UNDER", 3, 2)])

    def test_short_row_alone_does_not_fail_the_run(self):
        p = _tmp("under.md", H + "| 1 | 2 |\n")
        self.assertEqual(_run(p).returncode, 0)

    def test_over_and_under_in_one_table_are_reported_apart(self):
        got = kinds(H + "| 1 | 2 |\n| 1 | 2 | 3 | 4 |\n")
        self.assertEqual(got, [("UNDER", 3, 2), ("OVER", 4, 4)])


class TestEscapedPipes(unittest.TestCase):
    """Condition 3 — `\\|` is prose, not a separator."""

    def test_escaped_pipe_does_not_inflate_a_good_row(self):
        self.assertEqual(kinds(H + r"| 1 | never `ls \| wc` | 3 |" + "\n"), [])

    def test_escaped_pipe_survives_into_the_reported_cell_text(self):
        f = table_check.scan_text(H + r"| 1 | 2 | 3 | `a \| b` |" + "\n")[0]
        self.assertEqual(f["dropped"], [r"`a \| b`"])


class TestOverlap(unittest.TestCase):
    """Category 2 — BOTH over-celled AND carrying an escaped pipe.

    The two rules interact: discount the escape and you still must flag; count
    the escape and you flag the wrong width. Either rule alone gets this wrong.
    """

    def test_overcelled_row_containing_an_escaped_pipe_still_flags_at_true_width(self):
        row = r"| 1 | `ls \| wc` | 3 | EXTRA |" + "\n"
        f = table_check.scan_text(H + row)
        self.assertEqual(len(f), 1)
        self.assertEqual((f[0]["kind"], f[0]["observed"]), ("OVER", 4))
        self.assertEqual(f[0]["dropped"], ["EXTRA"])

    def test_a_row_that_is_only_overcelled_via_escapes_is_NOT_flagged(self):
        """The inverse overlap: naive counting would call this 5 cells."""
        self.assertEqual(kinds(H + r"| a \| b | c \| d | e |" + "\n"), [])

    def test_pipe_in_an_inline_code_span_DOES_separate(self):
        """Condition 4 — agree with the renderer, not with intent."""
        f = table_check.scan_text(H + "| 1 | `a|b` | 3 |\n")
        self.assertEqual([x["kind"] for x in f], ["OVER"])


class TestWrongOwner(unittest.TestCase):
    """Category 3 — an EXAMPLE table is not a live table."""

    def test_table_inside_a_fenced_block_is_ignored(self):
        text = "```\n" + H + "| 1 | 2 | 3 | 4 |\n```\n"
        self.assertEqual(kinds(text), [])

    def test_tilde_fence_is_honoured(self):
        text = "~~~\n" + H + "| 1 | 2 | 3 | 4 |\n~~~\n"
        self.assertEqual(kinds(text), [])

    def test_a_backtick_fence_inside_a_tilde_fence_does_not_reopen(self):
        text = "~~~\n```\n" + H + "| 1 | 2 | 3 | 4 |\n~~~\n"
        self.assertEqual(kinds(text), [])

    def test_a_real_table_right_after_a_fence_closes_IS_flagged(self):
        text = "```\nnot a table\n```\n" + H + "| 1 | 2 | 3 | 4 |\n"
        self.assertEqual([k[0] for k in kinds(text)], ["OVER"])

    def test_a_path_outside_the_repo_scans_instead_of_crashing(self):
        """FOUND BY RUNNING IT, not by this suite: the first out-of-perimeter
        invocation (a `git show` extract under /tmp) raised out of `main()` and
        the traceback exited 1 — the same code as a real finding.
        `[[finding_test_the_guard_not_just_the_guarded]]`"""
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as fh:
            fh.write(H + "| 1 | 2 | 3 | 4 |\n")
            outside = fh.name
        try:
            r = _run(pathlib.Path(outside))
            self.assertEqual(r.returncode, 1)
            self.assertIn("DROPPED", r.stdout)
            self.assertNotIn("Traceback", r.stderr)
        finally:
            pathlib.Path(outside).unlink()


class TestMissingInformation(unittest.TestCase):
    """Category 4 — fail loud, never silently clean."""

    def test_pipe_line_with_no_separator_is_not_a_table(self):
        self.assertEqual(kinds("| a | b | c |\n| 1 | 2 | 3 | 4 |\n"), [])

    def test_separator_of_the_wrong_width_does_not_open_a_table(self):
        self.assertEqual(kinds("| a | b | c |\n|---|---|\n| 1 | 2 | 3 | 4 |\n"), [])

    def test_empty_file_and_no_tables(self):
        self.assertEqual(kinds(""), [])
        self.assertEqual(kinds("# heading\n\nprose only\n"), [])

    def test_missing_path_is_rc2_not_rc0(self):
        r = _run(ROOT / "PROME/tools/tests/fixtures/__does_not_exist__.md")
        self.assertEqual(r.returncode, 2)
        self.assertIn("does not exist", r.stdout)

    def test_clean_run_never_claims_files_it_could_not_open(self):
        r = _run(ROOT / "PROME/tools/tests/fixtures/__does_not_exist__.md")
        self.assertNotIn("ok", r.stdout.split("\n")[0])


class TestExitCodes(unittest.TestCase):

    def test_rc1_on_a_finding(self):
        p = _tmp("over.md", H + "| 1 | 2 | 3 | 4 |\n")
        r = _run(p)
        self.assertEqual(r.returncode, 1)
        self.assertIn("DROPPED", r.stdout)

    def test_rc0_on_clean(self):
        p = _tmp("clean.md", H + "| 1 | 2 | 3 |\n")
        self.assertEqual(_run(p).returncode, 0)


class TestPerimeterIsDerived(unittest.TestCase):
    """Condition 5 — from the manifest, not a hand-list."""

    def test_perimeter_comes_from_READS_tsv(self):
        got = {p.name for p in table_check.perimeter()}
        self.assertIn("STATUS.md", got)
        self.assertIn("HEARTBEAT.md", got)
        declared = {
            r.split("\t")[2].rsplit("/", 1)[-1]
            for r in (ROOT / "PROME/registry/READS.tsv").read_text().split("\n")
            if not r.startswith("#") and r.count("\t") >= 3
            and r.split("\t")[0] == "READ" and r.split("\t")[1] == "PROME"
            and r.split("\t")[3] == "whole"
        }
        self.assertEqual(got, declared)


class TestLiveSurfacesAreClean(unittest.TestCase):
    """The regression guard proper: PROME's own boot-read surfaces stay clean."""

    def test_declared_whole_reads_have_no_overcelled_rows(self):
        bad = []
        for p in table_check.perimeter():
            for f in table_check.scan_text(p.read_text(), p.name):
                if f["kind"] == "OVER":
                    bad.append(f"{f['path']}:{f['line']} ({f['observed']}>{f['width']})")
        self.assertEqual(bad, [], f"over-celled rows on boot-read surfaces: {bad}")


_TMPDIR = pathlib.Path(__file__).resolve().parent / "fixtures" / "_table_check_tmp"


def _tmp(name, text):
    _TMPDIR.mkdir(parents=True, exist_ok=True)
    p = _TMPDIR / name
    p.write_text(text)
    return p


def _run(path):
    return subprocess.run(
        [sys.executable, str(ROOT / "PROME/tools/table_check.py"), str(path)],
        capture_output=True, text=True)


def tearDownModule():
    import shutil
    if _TMPDIR.exists():
        shutil.rmtree(_TMPDIR)


if __name__ == "__main__":
    unittest.main()
