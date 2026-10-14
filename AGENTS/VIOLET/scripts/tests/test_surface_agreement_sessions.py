#!/usr/bin/env python3
"""Offline Git fixtures: closeout boundaries, addenda, moves, missing witnesses."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import surface_agreement as sa

DAY = "2026-10-14"
AGREE = "Convergence score 30/50. FT-10 sustain count 3 of 4.\n"
OLD = "Convergence score 29/50. FT-10 sustain count 0 of 4.\n"
DRIFT = "Convergence score 31/50. FT-10 sustain count 3 of 4.\n"


class SessionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="violet_memo_session_")
        self.root = Path(self.temp.name)
        (self.root / "memos" / "processed").mkdir(parents=True)
        self.config = patch.multiple(sa, REPO=self.root, AGENT_DIR=self.root,
                                     MEMO_DIRS=("memos", "memos/processed"))
        self.config.start()
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        for name in ("STATUS.md", "NEXUS_BRIEF.md", "SCRATCH.md"):
            (self.root / name).write_text(OLD)
        self.git("add", "STATUS.md", "NEXUS_BRIEF.md", "SCRATCH.md")
        self.git("commit", "-qm", "earlier STATUS")
        self.old = self.memo("earlier", OLD, commit=True)
        for name in ("STATUS.md", "NEXUS_BRIEF.md", "SCRATCH.md"):
            (self.root / name).write_text(AGREE)
        self.git("add", "STATUS.md", "NEXUS_BRIEF.md", "SCRATCH.md")
        self.git("commit", "-qm", "current STATUS")

    def tearDown(self):
        self.config.stop()
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, check=True,
                              capture_output=True, text=True)

    def memo(self, slug, body=AGREE, commit=False):
        rel = f"memos/{DAY}_from-VIOLET_{slug}.md"
        path = self.root / rel
        path.write_text(body)
        if commit:
            self.git("add", rel)
            self.git("commit", "-qm", slug)
        return path

    def check_main(self, want):
        self.assertEqual(sa.main(["--quiet", "--date", DAY]), want)

    def test_prior_same_day_closeout_is_historical(self):
        self.memo("current", commit=True)
        self.check_main(0)

    def test_current_committed_addendum_still_fails(self):
        self.memo("current", commit=True)
        self.memo("addendum", DRIFT, commit=True)
        self.check_main(1)

    def test_current_uncommitted_addendum_still_fails(self):
        self.memo("current", commit=True)
        self.memo("addendum", DRIFT)
        self.check_main(1)

    def test_latest_agreeing_memo_does_not_hide_earlier_current_drift(self):
        self.memo("addendum", DRIFT, commit=True)
        self.memo("latest_agrees", commit=True)
        self.check_main(1)

    def test_later_recipient_move_does_not_revive_prior_closeout(self):
        self.memo("current", commit=True)
        self.git("mv", self.old.relative_to(self.root).as_posix(), "memos/processed/" + self.old.name)
        self.git("commit", "-qm", "recipient consumed earlier memo")
        self.check_main(0)

    def test_current_recipient_move_preserves_drift_detection(self):
        self.memo("current", commit=True)
        addition = self.memo("addendum", DRIFT, commit=True)
        self.git("mv", addition.relative_to(self.root).as_posix(), "memos/processed/" + addition.name)
        self.git("commit", "-qm", "recipient consumed addendum")
        self.check_main(1)

    def test_no_current_memo_is_not_agreement(self):
        self.check_main(1)

    def test_unavailable_git_witness_fails_closed(self):
        self.memo("current")
        with patch.object(sa, "git_read", side_effect=sa.EvidenceUnavailable("fixture unavailable")):
            self.check_main(1)


if __name__ == "__main__":
    unittest.main()
