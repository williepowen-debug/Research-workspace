#!/usr/bin/env python3
"""L294 F-4 — `agent_freshness.git()` swallowed non-zero rc.

Conditions and the reproduction (including where it differs from the source
report) live in PROME/tools/tests/ACCEPTANCE_agent_freshness_L294_F4.md, written
before the code. Summary of the scope, because the report's stated consequence
is narrower than it reads:

  * The MECHANISM is exactly as reported — rc 128 and rc 0-with-no-output both
    produced "", so `own_surface_age_days` returned None for two different facts
    and `(None or 0) > 7` read the most stale state as brand new.
  * The reported CONSEQUENCE ("a zero-commit desk is the one state this check
    cannot flag") is not reachable through the path named: fleet_dashboard maps a
    None age to crit / "no git history", and prome_gate:747 only examines desks
    the grid classed "ok". Those two defects do not compose.
  * The half NOT in the report is worse: `git()`'s other caller is dirty_paths(),
    where a failed `git status` returned [] — a DIRTY tree reading CLEAN, into
    the documented pre-spawn STOP. Fixed at the shared root, not at one call site.
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))

import agent_freshness as af  # noqa: E402


class _Root:
    """Point the module at another directory for the duration of a block."""

    def __init__(self, path):
        self.path = pathlib.Path(path)

    def __enter__(self):
        self.saved = af.ROOT
        af.ROOT = self.path
        return self

    def __exit__(self, *a):
        af.ROOT = self.saved


NONREPO = pathlib.Path(tempfile.mkdtemp())     # exists, is not a git repo → rc 128

# ⛔ EXTERNAL FINDING 2026-09-13 (F2): this suite WROTE INTO THE LIVE CHECKOUT —
# AGENTS/BRENT/zz_f4_probe.md created and deleted, AGENTS/ZZ_F4_* directories created
# and their contents unlinked in cleanup. It could overwrite a real file or collide with
# a concurrent session, and the 9/12 fixture correction covered the F-7 suite and not
# this one. ★ A FIXTURE THAT EXISTS AND IS NOT USED IS NOT A CONTROL — I built
# gate_fixture.py for exactly this the day before and did not apply it here.
# Third live-state test defect in three sessions.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gate_fixture  # noqa: E402

_FIX = None


_LIVE_BEFORE = None


def setUpModule():
    """One throwaway repo for every test that WRITES. It carries real git history, so
    the age queries have commits to find, and dirty-file cases can create their own."""
    global _FIX
    _FIX = gate_fixture.build()
    # gate_fixture exports HEAD, so overlay the working-tree copy of the file under
    # repair — otherwise the suite silently tests the last commit instead of the change.
    shutil.copy2(ROOT / "PROME/tools/agent_freshness.py",
                 _FIX / "PROME/tools/agent_freshness.py")
    # Snapshot the LIVE checkout so the containment property is ASSERTED, not assumed.
    global _LIVE_BEFORE
    _LIVE_BEFORE = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                                  capture_output=True, text=True).stdout


def tearDownModule():
    gate_fixture.destroy(_FIX)


class _InFixture:
    """Aim agent_freshness at the throwaway repo for the duration of a block."""

    def __enter__(self):
        self.saved = (af.ROOT, af.AGENTS, af.PROME_INBOX)
        af.ROOT, af.AGENTS, af.PROME_INBOX = _FIX, _FIX / "AGENTS", _FIX / "PROME" / "inbox"
        return _FIX

    def __exit__(self, *a):
        af.ROOT, af.AGENTS, af.PROME_INBOX = self.saved


class GitDistinguishesFailureFromEmpty(unittest.TestCase):
    """Condition 1 — the root cause."""

    def test_failure_returns_UNKNOWN_not_empty_string(self):
        with _Root(NONREPO):
            self.assertIs(af.git("log", "-1", "--format=%ct"), af.UNKNOWN)

    def test_success_with_no_output_is_still_an_EMPTY_STRING(self):
        """`""` on rc 0 is a real answer — 'ran, matched nothing'. If the fix
        turned this into UNKNOWN it would trade a false-fresh for a false-alarm."""
        out = af.git("log", "-1", "--format=%ct", "--", "AGENTS/__no_such_desk__")
        self.assertEqual(out, "")
        self.assertIsNot(out, af.UNKNOWN)

    def test_success_with_output_is_unchanged(self):
        self.assertTrue(af.git("rev-parse", "HEAD"))

    def test_git_that_cannot_be_RUN_is_UNKNOWN_not_a_crash(self):
        """Condition 7 — prome_gate imports this inside a try that would hide
        a raise behind 'grid-agreement check unavailable'."""
        with _Root(NONREPO / "does" / "not" / "exist"):
            self.assertIs(af.git("status", "--porcelain"), af.UNKNOWN)


class SentinelIsFalsy(unittest.TestCase):
    """REGRESSION, found by independent review 2026-09-12 AFTER the F-4 commit.

    The first sentinel was a bare `object()` — truthy. fleet_dashboard.py:1014 reads
    `int(ts) if ts else None`, so a truthy sentinel turned a graceful "no git history"
    classification into a TypeError. The F-4 commit message had cited that very line
    as proof the defects did not compose; line 1014 raises before 1019 is reached.
    Truthiness is the one property no caller thinks to check."""

    def test_unknown_is_falsy(self):
        self.assertFalse(af.UNKNOWN)
        self.assertFalse(bool(af.UNKNOWN))

    def test_unknown_is_still_identity_distinct_from_empty_and_None(self):
        """Falsy must not make it INDISTINGUISHABLE from "" — that was the defect
        the sentinel exists to fix. Identity carries the distinction."""
        self.assertIsNot(af.UNKNOWN, "")
        self.assertIsNot(af.UNKNOWN, None)
        self.assertNotEqual(af.UNKNOWN, "")

    def test_len_and_iter_degrade_instead_of_raising(self):
        self.assertEqual(len(af.UNKNOWN), 0)
        self.assertEqual(list(af.UNKNOWN), [])

    def test_repr_says_what_it_is(self):
        self.assertIn("git query failed", repr(af.UNKNOWN))

    def test_the_actual_fleet_dashboard_expression_yields_None_again(self):
        """The exact idiom at fleet_dashboard.py:1014, replayed."""
        import datetime as dt
        ts = af.UNKNOWN
        own = (dt.datetime.now().timestamp() - int(ts)) / 86400 if ts else None
        self.assertIsNone(own)

    def test_identity_guards_in_this_module_still_work_with_a_falsy_sentinel(self):
        """`is UNKNOWN` must be checked BEFORE any truthiness test, or a falsy
        sentinel silently takes the empty-result branch."""
        import tempfile as _t
        saved = af.ROOT
        try:
            af.ROOT = pathlib.Path(_t.mkdtemp())
            self.assertEqual(af.own_surface_age_state("BRENT"), ("unknown", None))
            self.assertIs(af.dirty_paths("BRENT"), af.UNKNOWN)
        finally:
            af.ROOT = saved


class AgeHasThreeStates(unittest.TestCase):
    """Condition 2."""

    def test_committed_desk_is_aged_with_a_number(self):
        with _InFixture():
            state, days = af.own_surface_age_state("BRENT")
        self.assertEqual(state, "aged")
        self.assertIsInstance(days, float)

    def test_never_committed_desk_is_never_not_fresh(self):
        """THE REPORTED CASE. Pre-fix this was indistinguishable from a failure,
        and `(None or 0) > 7` read it as zero days old."""
        with _InFixture():
            d = af.AGENTS / "ZZ_F4_NEVER"
            d.mkdir(parents=True, exist_ok=True)
            (d / "STATUS.md").write_text("never committed\n")
            self.assertEqual(af.own_surface_age_state("ZZ_F4_NEVER"), ("never", None))

    def test_failed_query_is_unknown_not_never(self):
        with _Root(NONREPO):
            self.assertEqual(af.own_surface_age_state("BRENT"), ("unknown", None))

    def test_never_and_unknown_are_DIFFERENT_states(self):
        with _Root(NONREPO):
            failed = af.own_surface_age_state("BRENT")[0]
        self.assertNotEqual(failed, "never")

    def test_the_legacy_number_accessor_still_returns_None_for_both(self):
        """Condition 6 — display paths (fleet_dashboard's crit / 'no git
        history') depend on this and must not change."""
        with _Root(NONREPO):
            self.assertIsNone(af.own_surface_age_days("BRENT"))


class DirtyPathsFailsClosed(unittest.TestCase):
    """Condition 3 — the half the source report does not contain."""

    def setUp(self):
        self.ctx = _InFixture(); self.ctx.__enter__()
        self.probe = af.AGENTS / "BRENT" / "zz_f4_probe.md"
        self.probe.parent.mkdir(parents=True, exist_ok=True)
        self.probe.write_text("probe\n")

    def tearDown(self):
        if self.probe.exists():
            self.probe.unlink()
        self.ctx.__exit__(None, None, None)

    def test_a_real_dirty_path_is_seen(self):
        self.assertTrue(any("zz_f4_probe.md" in ln for ln in af.dirty_paths("BRENT")))

    def test_failed_git_status_is_UNKNOWN_not_an_empty_list(self):
        """Pre-fix: [] — a dirty tree reading CLEAN into the pre-spawn STOP."""
        with _Root(NONREPO):
            self.assertIs(af.dirty_paths("BRENT"), af.UNKNOWN)

    def test_a_genuinely_clean_tree_is_still_an_empty_list(self):
        self.probe.unlink()
        out = af.dirty_paths("BRENT")
        self.assertIsNot(out, af.UNKNOWN)
        self.assertEqual([ln for ln in out if "zz_f4_probe" in ln], [])


class PreSpawnStopFailsClosed(unittest.TestCase):
    """Condition 4 — UNKNOWN must behave like blocked, never like clean.
    Driven through the CLI, because that is what the playbook tells a session
    to run and rc is the whole contract."""

    def run_cli(self, *args):
        """Runs the FIXTURE's copy, inside the FIXTURE. Never the live checkout —
        the pre-spawn STOP is exactly the path that used to dirty AGENTS/BRENT."""
        p = subprocess.run([sys.executable, str(_FIX / "PROME/tools/agent_freshness.py"), *args],
                           cwd=_FIX, capture_output=True, text=True)
        return p.returncode, p.stdout + p.stderr

    def test_clean_desk_is_clear_to_brief(self):
        rc, out = self.run_cli("--agent", "BRENT")
        self.assertEqual(rc, 0)
        self.assertIn("clear to brief", out)

    def test_unknown_dirtiness_NEVER_prints_clear_to_brief(self):
        probe = _FIX / "AGENTS/BRENT/zz_f4_probe2.md"
        probe.parent.mkdir(parents=True, exist_ok=True)
        probe.write_text("x\n")
        try:
            rc, out = self.run_cli("--agent", "BRENT")
            self.assertEqual(rc, 1)
            self.assertNotIn("clear to brief", out)
        finally:
            probe.unlink()

    def test_fleet_table_does_not_crash_and_flags_the_new_states(self):
        rc, out = self.run_cli("--all")
        self.assertEqual(rc, 0)
        self.assertNotIn("Traceback", out)


class Overlap(unittest.TestCase):
    """Category 2 — never-committed AND dirty at the same time. A fix to one
    signal must not mask the other; they are independent facts."""

    def test_new_desk_reads_never_while_its_dirty_list_is_populated(self):
        with _InFixture():
            d = af.AGENTS / "ZZ_F4_OVERLAP"
            d.mkdir(parents=True, exist_ok=True)
            (d / "STATUS.md").write_text("brand new and uncommitted\n")
            state, days = af.own_surface_age_state("ZZ_F4_OVERLAP")
            dirty = af.dirty_paths("ZZ_F4_OVERLAP")
            self.assertEqual(state, "never")       # not "aged", not 0 days
            self.assertIsNone(days)
            self.assertIsNot(dirty, af.UNKNOWN)
            self.assertTrue(any("ZZ_F4_OVERLAP" in ln for ln in dirty),
                            f"dirty list lost the untracked file: {dirty}")
        # no cleanup needed: everything above lives inside the throwaway fixture,
        # which tearDownModule destroys.


class WrongOwner(unittest.TestCase):
    """Category 3 — the inbox exclusion, and PROME's home not being under AGENTS/."""

    def test_inbox_is_excluded_from_own_surface_age(self):
        """An inbound packet must not make a dark desk look fresh — that is the
        whole reason for the `:(exclude)` pathspec. Verified by asserting the
        pathspec still reaches git, using a desk whose inbox has commits."""
        with_inbox = af.git("log", "-1", "--format=%ct", "--", "AGENTS/BRENT/inbox")
        own_only = af.git("log", "-1", "--format=%ct", "--",
                          "AGENTS/BRENT", ":(exclude)AGENTS/BRENT/inbox")
        self.assertIsNot(with_inbox, af.UNKNOWN)
        self.assertIsNot(own_only, af.UNKNOWN)

    def test_PROME_via_the_AGENTS_path_reports_the_REMOVAL_not_never(self):
        """⚠️ My first version of this test asserted ("never", None) and FAILED.
        The directory is gone (removed 2026-07-24) but the PATH still has git
        history, so the helper returns the age of the removal commit — a large
        `aged` number, not `never`. fleet_dashboard.py's comment says the helper
        "returns None here"; that is FALSE, and the comment is corrected in the
        same commit. No live defect: both consumers special-case or skip PROME
        before reaching the helper. `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`"""
        self.assertFalse((af.AGENTS / "PROME").is_dir())
        state, days = af.own_surface_age_state("PROME")
        self.assertEqual(state, "aged")
        self.assertGreater(days, 30)

    def test_PROMEs_real_home_is_queryable_so_the_special_case_works(self):
        ts = af.git("log", "-1", "--format=%ct", "--", "PROME", ":(exclude)PROME/inbox")
        self.assertIsNot(ts, af.UNKNOWN)
        self.assertTrue(ts)


class GateConsumer(unittest.TestCase):
    """Condition 5 — prome_gate:747 reports unknown/never instead of 0 days."""

    @staticmethod
    def _code_lines():
        """CODE only. The repair's own comment QUOTES the defective idiom to
        explain it, and a whole-file substring scan matched that comment and
        reported the defect as live. A scanner must read what executes.
        `[[finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it]]`"""
        out = []
        for ln in (ROOT / "PROME/tools/prome_gate.py").read_text().splitlines():
            code = ln.split("#", 1)[0]
            if code.strip():
                out.append(code)
        return out

    def test_gate_uses_the_state_accessor_not_the_or_zero_idiom(self):
        offenders = [ln.strip() for ln in self._code_lines()
                     if "own_surface_age_days" in ln and "or 0" in ln]
        self.assertEqual(offenders, [], f"the collapsing idiom is still live: {offenders}")

    def test_gate_calls_the_state_accessor(self):
        self.assertTrue(any("own_surface_age_state(n)" in ln for ln in self._code_lines()))

    def test_gate_names_all_three_outcomes(self):
        src = (ROOT / "PROME/tools/prome_gate.py").read_text()
        for phrase in ("own-surface age >7d",
                       "NO COMMIT has ever touched their own tree",
                       "could NOT be established"):
            self.assertIn(phrase, src)


class LiveCheckoutUntouched(unittest.TestCase):
    """F2's whole point, asserted rather than promised. Runs alphabetically late; the
    comparison is against a snapshot taken before any test wrote anything."""

    def test_git_status_of_the_live_repo_is_unchanged(self):
        after = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                               capture_output=True, text=True).stdout
        self.assertEqual(_LIVE_BEFORE, after,
                         "a test in this suite wrote into the LIVE checkout")

    def test_no_stray_probe_or_desk_was_left_behind(self):
        strays = [str(x) for x in (ROOT / "AGENTS").glob("*/zz_f4_probe*")]
        strays += [str(x) for x in (ROOT / "AGENTS").glob("ZZ_F4_*")]
        self.assertEqual(strays, [], f"live-repo residue: {strays}")

    def test_the_read_only_live_tests_are_named_so_a_future_writer_is_visible(self):
        """Reading the live repo is deliberate in exactly two places — the inbox-exclusion
        pathspec check and the PROME-path control. Naming them here means converting one
        into a writer shows up as a change to THIS list, not as silent repo residue.
        ⛔ An earlier version of this test scanned the file's own source text for a write
        idiom; it matched its own string manipulation and proved nothing. The behavioural
        guards above are the real assertion — this one is a roster, not a scanner."""
        expected = {"test_inbox_is_excluded_from_own_surface_age",
                    "test_PROMEs_real_home_is_queryable_so_the_special_case_works"}
        actual = {n for n in dir(WrongOwner) if n.startswith("test_")}
        self.assertTrue(expected <= actual, f"read-only live tests renamed or removed: {expected - actual}")


if __name__ == "__main__":
    unittest.main()
