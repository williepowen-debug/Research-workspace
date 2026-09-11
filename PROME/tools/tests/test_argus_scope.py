#!/usr/bin/env python3
"""Regression tests for argus_scope.py — the coverage the 2026-09-11 external audit proved was missing.

Audit F1 (P1): CLOSEOUT 1f runs ARGUS BEFORE the closeout commit, but scope() read only `watermark..HEAD`,
so the closeout's own pending writes were invisible to the audit that approves them. Plus two completeness
legs: subject-only attribution missed PROME work committed under a `FORGE:` subject.

Every test builds a throwaway git repo — no assertion touches the live tree, so these cannot rot against it
(`finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit`).
"""
import os, subprocess, sys, tempfile, unittest, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("argus_scope", os.path.join(ROOT, "argus_scope.py"))
A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)


def sh(*a, cwd):
    subprocess.run(a, cwd=cwd, check=True, capture_output=True, text=True)


def write(repo, rel, text="x\n"):
    p = os.path.join(repo, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as fh:
        fh.write(text)
    return rel


def append(repo, rel, text):
    with open(os.path.join(repo, rel), "a") as fh:
        fh.write(text)


def commit(repo, subject, paths):
    sh("git", "add", *paths, cwd=repo)
    sh("git", "commit", "-m", subject, *paths, cwd=repo)


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = self.tmp.name
        sh("git", "init", "-q", "-b", "master", cwd=self.repo)
        sh("git", "config", "user.email", "t@t", cwd=self.repo)
        sh("git", "config", "user.name", "t", cwd=self.repo)
        commit(self.repo, "PROME: STANDARD closeout 2026-09-10", [write(self.repo, "PROME/STATUS.md")])
        self.cwd = os.getcwd(); os.chdir(self.repo)

    def tearDown(self):
        os.chdir(self.cwd); self.tmp.cleanup()

    def scope(self, **kw):
        wm, _ = A.find_watermark()
        return A.scope(wm, **kw)


class TestPendingIsInScope(Fixture):
    """F1, the P1: the closeout's own uncommitted writes must reach the auditor."""

    def test_pending_tracked_modification_is_in_scope(self):
        commit(self.repo, "PROME: a tool change", [write(self.repo, "PROME/tools/t.py")])
        append(self.repo, "PROME/STATUS.md", "pending edit\n")
        _, committed, pending, _, _ = self.scope()
        self.assertIn("PROME/tools/t.py", committed)
        self.assertIn("PROME/STATUS.md", pending, "a pending closeout write must be audited")

    def test_pending_new_untracked_file_is_in_scope(self):
        commit(self.repo, "PROME: a tool change", [write(self.repo, "PROME/tools/t.py")])
        write(self.repo, "PROME/BRIEF.md")          # never committed
        _, _, pending, _, _ = self.scope()
        self.assertIn("PROME/BRIEF.md", pending, "a brand-new closeout file must be audited")

    def test_the_audited_repro_skips_without_the_fix(self):
        """The audit's exact reproduction: one committed tool change + two pending closeout docs.
        Committed-only scope = 1 path = SKIP. With pending = 3 = SPAWN."""
        commit(self.repo, "PROME: a tool change", [write(self.repo, "PROME/tools/t.py")])
        append(self.repo, "PROME/STATUS.md", "pending\n")
        write(self.repo, "PROME/BRIEF.md")
        _, committed, pending, _, _ = self.scope()
        self.assertLess(len(committed), A.MIN_PATHS, "committed-only is the pre-fix SKIP")
        self.assertGreaterEqual(len(committed) + len(pending), A.MIN_PATHS, "union must SPAWN")

    def test_another_desks_dirty_path_is_never_handed_to_argus(self):
        commit(self.repo, "TERRY: something", [write(self.repo, "AGENTS/TERRY/STATUS.md")])
        append(self.repo, "AGENTS/TERRY/STATUS.md", "terry is mid-session\n")
        write(self.repo, "AGENTS/TERRY/new.md")
        _, _, pending, _, _ = self.scope()
        self.assertEqual(pending, [], "the shared dirty tree is not PROME's to audit")

    def test_no_pending_flag_restores_committed_only(self):
        commit(self.repo, "PROME: a tool change", [write(self.repo, "PROME/tools/t.py")])
        write(self.repo, "PROME/BRIEF.md")
        _, _, pending, _, _ = self.scope(include_pending=False)
        self.assertEqual(pending, [])


class TestAttribution(Fixture):
    """F1's completeness legs: durable attribution, and its false-positive boundary."""

    def test_prome_work_under_a_forge_subject_is_attributed(self):
        commit(self.repo, "FORGE: reconcile the mirror", [write(self.repo, "FORGE/STATUS.md")])
        commits, paths, _, _, _ = self.scope()
        self.assertEqual([c["attribution"] for c in commits], ["paths"])
        self.assertIn("FORGE/STATUS.md", paths)

    def test_inbound_packet_in_prome_inbox_is_NOT_attributed_to_prome(self):
        """Self-caught while fixing F1: PROME/inbox/ holds OTHER desks' output.
        finding_path_scoped_git_log_measures_inbound_traffic."""
        commit(self.repo, "CARL -> PROME: a packet", [write(self.repo, "PROME/inbox/2026-09-11_from-CARL_x.md")])
        commits, paths, _, _, _ = self.scope()
        self.assertEqual(commits, [], "inbound mail is not PROME-authored work")
        self.assertEqual(paths, [])

    def test_shared_memory_commit_by_another_desk_is_NOT_attributed(self):
        commit(self.repo, "VIOLET: auto-memory extended", [write(self.repo, "memory/auto/finding_x.md")])
        commits, _, _, _, _ = self.scope()
        self.assertEqual(commits, [], "memory/auto is fleet-shared authorship")

    def test_prome_authored_packet_to_another_desk_IS_attributed(self):
        commit(self.repo, "PROME -> DAEDALUS: routed", [write(self.repo, "AGENTS/DAEDALUS/inbox/2026-09-11_from-PROME_x.md")])
        commits, _, _, _, _ = self.scope()
        self.assertEqual(len(commits), 1, "carve-out (1) packets are PROME's to audit")

    def test_mixed_path_commit_without_prome_subject_is_not_attributed(self):
        """all() not any(): a commit straddling PROME and another desk is not silently claimed."""
        commit(self.repo, "TERRY: touched both", [write(self.repo, "FORGE/x.md"), write(self.repo, "AGENTS/TERRY/y.md")])
        commits, _, _, _, _ = self.scope()
        self.assertEqual(commits, [])


class TestRepairReviewBoundaries(Fixture):
    """Boundaries the 2026-09-11 repair review reproduced against the FIRST fix. Each was a real miss."""

    def test_committed_then_edited_file_appears_in_BOTH_lists(self):
        """BLOCKING finding #1: `pend - paths` dropped the commonest closeout shape entirely."""
        commit(self.repo, "PROME: status write", [write(self.repo, "PROME/STATUS.md", "v1\n")])
        append(self.repo, "PROME/STATUS.md", "pending closeout correction\n")
        _, committed, pending, _, _ = self.scope()
        self.assertIn("PROME/STATUS.md", committed)
        self.assertIn("PROME/STATUS.md", pending,
                      "a committed-then-edited file needs BOTH reads; the committed diff omits the later edit")

    def test_overlap_is_not_double_counted_in_the_threshold(self):
        commit(self.repo, "PROME: status write", [write(self.repo, "PROME/STATUS.md", "v1\n")])
        append(self.repo, "PROME/STATUS.md", "edit\n")
        _, committed, pending, _, _ = self.scope()
        self.assertEqual(len(set(committed) | set(pending)), 1, "unique paths, not the sum")

    def test_new_directory_is_listed_as_its_FILES_not_the_directory(self):
        """`git status --porcelain` without -uall collapses a new dir, undercounting and handing ARGUS a dir."""
        commit(self.repo, "PROME: a tool change", [write(self.repo, "PROME/tools/t.py")])
        write(self.repo, "PROME/new_reports/a.md")
        write(self.repo, "PROME/new_reports/b.md")
        _, committed, pending, _, _ = self.scope()
        self.assertIn("PROME/new_reports/a.md", pending)
        self.assertIn("PROME/new_reports/b.md", pending)
        self.assertNotIn("PROME/new_reports/", pending)
        self.assertGreaterEqual(len(set(committed) | set(pending)), A.MIN_PATHS, "3 paths => SPAWN, not SKIP")

    def test_another_desks_PENDING_shared_memory_is_excluded_by_lineage(self):
        """Directory membership is not authorship. VIOLET's tracked memory file stays VIOLET's."""
        commit(self.repo, "VIOLET: auto-memory extended", [write(self.repo, "memory/auto/violet.md")])
        append(self.repo, "memory/auto/violet.md", "violet edits again\n")
        _, _, pending, inferred, unattr = self.scope()
        self.assertNotIn("memory/auto/violet.md", pending)
        self.assertNotIn("memory/auto/violet.md", inferred)
        self.assertNotIn("memory/auto/violet.md", unattr)

    def test_promes_own_PENDING_shared_memory_is_LINEAGE_INFERRED_not_owned(self):
        """Refinement 3: lineage says who committed LAST, not who edited TODAY. Label, do not launder."""
        commit(self.repo, "PROME: memory n+2", [write(self.repo, "memory/auto/prome_finding.md")])
        append(self.repo, "memory/auto/prome_finding.md", "extended tonight\n")
        _, _, pending, inferred, _ = self.scope()
        self.assertIn("memory/auto/prome_finding.md", inferred,
                      "PROME lineage is INFERRED, never asserted as owned — the uncertainty must travel")
        self.assertNotIn("memory/auto/prome_finding.md", pending)

    def test_untracked_shared_memory_is_UNATTRIBUTED_not_silently_claimed_or_dropped(self):
        commit(self.repo, "PROME: session work", [write(self.repo, "PROME/tools/t.py")])
        write(self.repo, "memory/auto/brand_new.md")
        _, _, pending, inferred, unattr = self.scope()
        self.assertNotIn("memory/auto/brand_new.md", pending, "no lineage => do not claim it")
        self.assertIn("memory/auto/brand_new.md", unattr, "...and do not drop it silently either")

    def test_daily_closeout_log_is_in_scope(self):
        """CLOSEOUT Chunk 2 writes memory/YYYY-MM-DD.md and Chunk 4 commits it."""
        commit(self.repo, "PROME: session work", [write(self.repo, "PROME/tools/t.py")])
        write(self.repo, "memory/2026-09-11.md")
        _, _, pending, _, _ = self.scope()
        self.assertIn("memory/2026-09-11.md", pending)

    def test_a_path_with_spaces_survives_nul_parsing(self):
        commit(self.repo, "PROME: session work", [write(self.repo, "PROME/tools/t.py")])
        write(self.repo, "PROME/a file with spaces.md")
        _, _, pending, _, _ = self.scope()
        self.assertIn("PROME/a file with spaces.md", pending)


class TestPerimeterUnit(unittest.TestCase):
    def test_authorship_vs_pending_perimeters_differ_exactly_where_intended(self):
        self.assertTrue(A.is_prome_authored("PROME/STATUS.md"))
        self.assertFalse(A.is_prome_authored("PROME/inbox/2026-09-11_from-CARL_x.md"))
        self.assertFalse(A.is_prome_authored("memory/auto/finding_x.md"))
        self.assertTrue(A.is_shared_location("memory/auto/finding_x.md"))   # lineage-attributed, not claimed
        self.assertFalse(A.is_prome_authored("AGENTS/TERRY/STATUS.md"))
        self.assertTrue(A.is_prome_authored("memory/2026-09-11.md"))         # daily closeout log
        self.assertFalse(A.is_prome_authored("memory/2026-09-11-notes.md"))  # anchored, not a prefix match

    def test_closeout_regex_matches_tiers_and_rejects_mere_mentions(self):
        for s in ("PROME: STANDARD closeout 2026-09-11", "PROME: closeout 9/10 evening", "PROME: LIGHT closeout"):
            self.assertTrue(A.CLOSEOUT_RE.match(s), s)
        self.assertFalse(A.CLOSEOUT_RE.match("PROME: WQ-227 registered (exempt-desk closeout assertion)"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
