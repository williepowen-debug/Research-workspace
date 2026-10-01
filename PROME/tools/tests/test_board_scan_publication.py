#!/usr/bin/env python3
"""Falsification set for board_scan.py's publication barrier and consumed ledger (2026-09-30, CATO RC1).

Acceptance: PROME/tools/tests/ACCEPTANCE_board_scan_publication_2026-09-30.md (written before the edit).
Every test builds a throwaway git repository in a tempdir — never the live tree.
Run: python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_board_scan_publication.py
"""
import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import board_scan  # noqa: E402

GOOD = ("---\nsignal_id: {sid}\ndate: 2026-09-30\ntime_dispatched: 2026-09-30T12:00:00Z\n"
        "cluster: TEST\nprecedence: ROUTINE\naction: [{action}]\ninfo: [{info}]\n---\n# {head}\n")


class Repo(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="board-scan-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "user.name", "fixture")
        self.board = self.root / "BOARD"
        self.board.mkdir()
        (self.root / "README").write_text("fixture\n")
        self.git("add", "README")
        self.git("commit", "-q", "-m", "init")
        state = self.root / "PROME" / "state"
        self.cursor, self.ledger = state / "board_cursor.txt", state / "board_consumed.tsv"
        for name, value in (("BOARD", self.board), ("CURSOR", self.cursor), ("LEDGER", self.ledger)):
            p = patch.object(board_scan, name, value)
            p.start()
            self.addCleanup(p.stop)

    def git(self, *argv):
        subprocess.run(["git", "-C", str(self.root), *argv], check=True, capture_output=True)

    def write(self, num, action="BRENT", info="LIQUID", slug="x", body=None, day="20260930", head=None):
        sid = f"SIG-W-{day}-{num:03d}"
        p = self.board / f"{sid}-{slug}.md"
        p.write_text(body if body is not None else GOOD.format(
            sid=sid, action=action, info=info, head=head or f"headline {num} {slug}"), encoding="utf-8")
        return p

    def publish(self, *paths, msg="publish"):
        self.git("add", *[str(p) for p in paths])
        self.git("commit", "-q", "-m", msg)

    def scan(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with patch.object(sys, "argv", ["board_scan.py", *argv]), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = board_scan.main()
        return rc, out.getvalue() + err.getvalue()

    def consumed(self):
        if not self.ledger.exists():
            return {}
        return dict(l.split("\t") for l in self.ledger.read_text().splitlines() if l and not l.startswith("#"))


class Ordinary(Repo):
    def test_info_signal_is_listed_consumed_once_then_quiet(self):
        self.publish(self.write(1, info="PROME"))
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 0)
        self.assertIn("1 info", out)
        self.assertEqual(self.consumed(), {"SIG-W-20260930-001-x": "I"})
        self.assertEqual(self.cursor.read_text(), "SIG-W-20260930-001\n")
        rc, out = self.scan("--advance")
        self.assertEqual((rc, "nothing new" in out), (0, True))

    def test_bare_run_writes_no_state(self):
        self.publish(self.write(1))
        rc, out = self.scan()
        self.assertEqual(rc, 0)
        self.assertFalse(self.ledger.exists())
        self.assertFalse(self.cursor.exists())
        rc, out = self.scan()
        self.assertIn("1 new", out)          # still new: nothing was consumed by looking

    def test_action_line_holds_until_acknowledged(self):
        self.publish(self.write(1, action="PROME", head="do the thing"))
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertIn("ON ACTION LINE", out)
        self.assertIn("cursor NOT advanced", out)
        self.assertEqual(self.consumed(), {})
        rc, out = self.scan("--advance", "--ack-actions")
        self.assertEqual(rc, 1)              # the run that acknowledges still reports the line
        self.assertEqual(self.consumed(), {"SIG-W-20260930-001-x": "A"})
        self.assertEqual(self.scan("--advance")[0], 0)

    def test_action_hold_withholds_the_info_rows_of_the_same_run(self):
        self.publish(self.write(1, info="PROME"), self.write(2, action="PROME"))
        rc, _ = self.scan("--advance")
        self.assertEqual((rc, self.consumed()), (1, {}))


class Unpublished(Repo):
    def test_untracked_draft_is_held_then_surfaces_with_its_action(self):
        """CATO RC1 cases 1-2: an unfinished file must not be consumed; its finished version must surface."""
        self.publish(self.write(4))
        self.scan("--advance")
        draft = self.write(5, body="# Incomplete, unpublished draft\n", slug="draft")
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 0)
        self.assertIn("HELD BACK", out)
        self.assertNotIn("SIG-W-20260930-005-draft", self.consumed())
        self.assertEqual(self.cursor.read_text(), "SIG-W-20260930-004\n")
        draft.write_text(GOOD.format(sid="SIG-W-20260930-005", action="PROME", info="", head="now published"))
        self.publish(draft)
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertIn("now published", out)

    def test_ack_actions_never_consumes_a_draft(self):
        self.publish(self.write(1))
        self.write(2, action="PROME", slug="draft")          # complete metadata, but uncommitted
        rc, out = self.scan("--advance", "--ack-actions")
        self.assertEqual(rc, 0)
        self.assertEqual(set(self.consumed()), {"SIG-W-20260930-001-x"})

    def test_staged_but_uncommitted_file_is_held(self):
        self.publish(self.write(1))
        p = self.write(2, info="PROME")
        self.git("add", str(p))
        rc, out = self.scan("--advance")
        self.assertIn("HELD BACK", out)
        self.assertNotIn("SIG-W-20260930-002-x", self.consumed())

    def test_committed_then_modified_file_is_held_overlap(self):
        """Overlap: in HEAD's tree AND dirty in the working tree — the dirty state wins."""
        p = self.write(1, info="PROME")
        self.publish(p)
        p.write_text(p.read_text() + "\nan edit WALTER has not committed\n")
        rc, out = self.scan("--advance")
        self.assertIn("HELD BACK", out)
        self.assertEqual(self.consumed(), {})
        self.publish(p, msg="finish")
        rc, out = self.scan("--advance")
        self.assertEqual(self.consumed(), {"SIG-W-20260930-001-x": "I"})

    def test_guard_falsified_without_the_publication_check_the_draft_is_consumed(self):
        """The tests above depend on the barrier: disable it and the defect returns."""
        self.publish(self.write(4))
        self.write(5, slug="draft")
        everything = lambda files: ({p.name for p in files}, {})   # noqa: E731
        with patch.object(board_scan, "publication_state", everything):
            self.scan("--advance")
        self.assertIn("SIG-W-20260930-005-draft", self.consumed())


class Unreadable(Repo):
    BAD = {
        "no frontmatter": "# just a heading\n",
        "unclosed frontmatter": "---\nsignal_id: SIG-W-20260930-002\naction: [PROME]\n# never closed\n",
        "no signal_id": GOOD.replace("signal_id: {sid}\n", ""),
        "wrong signal_id": GOOD.replace("{sid}", "SIG-W-20260930-099"),
        "no info line": GOOD.replace("info: [{info}]\n", ""),
        "no action line": GOOD.replace("action: [{action}]\n", ""),
        "action not a list": GOOD.replace("action: [{action}]", "action: PROME"),
        "unstamped": GOOD.replace("time_dispatched: 2026-09-30T12:00:00Z", "time_dispatched:"),
    }

    def test_each_incomplete_committed_file_is_a_hard_stop_not_a_consume(self):
        for label, template in self.BAD.items():
            with self.subTest(label):
                self.setUp()
                body = template.replace("{sid}", "SIG-W-20260930-002").replace("{action}", "BRENT") \
                    .replace("{info}", "LIQUID").replace("{head}", "h")
                self.publish(self.write(2, body=body))
                rc, out = self.scan("--advance")
                self.assertEqual(rc, 1, out)
                self.assertIn("UNREADABLE", out)
                self.assertEqual(self.consumed(), {})
                rc, out = self.scan("--advance", "--ack-actions")
                self.assertEqual(self.consumed(), {"SIG-W-20260930-002-x": "U"})


class LateArrivals(Repo):
    def test_lower_id_published_after_a_higher_one_surfaces(self):
        """CATO RC1 case 4."""
        self.publish(self.write(4))
        self.publish(self.write(6, info="PROME"))
        self.scan("--advance")
        self.assertEqual(self.cursor.read_text(), "SIG-W-20260930-006\n")
        self.publish(self.write(5, action="PROME", head="lower id, later"))
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertIn("lower id, later", out)

    def test_action_added_to_a_consumed_signal_resurfaces(self):
        p = self.write(1, info="PROME")
        self.publish(p)
        self.scan("--advance")
        p.write_text(GOOD.format(sid="SIG-W-20260930-001", action="PROME", info="", head="ask added later"))
        self.publish(p, msg="walter amends routing")
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertIn("ACTION ADDED", out)
        self.assertEqual(self.consumed()["SIG-W-20260930-001-x"], "I")     # held until acknowledged
        self.scan("--advance", "--ack-actions")
        self.assertEqual(self.consumed()["SIG-W-20260930-001-x"], "A")
        self.assertEqual(self.scan("--advance")[0], 0)

    def test_two_published_files_sharing_one_id_both_surface(self):
        self.publish(self.write(1, slug="first"))
        self.scan("--advance")
        self.publish(self.write(1, slug="second", action="PROME", head="reused id"))
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertIn("reused id", out)

    def test_ids_order_numerically_past_999(self):
        self.publish(self.write(999), self.write(1000))
        self.scan("--advance")
        self.assertEqual(self.cursor.read_text(), "SIG-W-20260930-1000\n")


class Migration(Repo):
    def test_seed_from_cursor_floods_nothing_and_keeps_an_unpublished_low_id(self):
        legacy = "---\nto: [BRENT]\ncluster: OLD\n---\n# a legacy-schema signal\n"
        self.publish(self.write(1, body=legacy), self.write(2), self.write(3), self.write(4))
        self.publish(self.write(5, info="PROME", head="above the cursor"))
        draft = self.write(3, slug="draft-below-cursor", action="PROME", head="was a draft at seeding")
        self.cursor.parent.mkdir(parents=True)
        self.cursor.write_text("SIG-W-20260930-004\n")
        rc, out = self.scan()
        self.assertEqual(rc, 0)
        self.assertIn("1 new", out)
        self.assertIn("above the cursor", out)
        self.assertFalse(self.ledger.exists())                  # a bare run persists nothing
        rc, out = self.scan("--advance")
        got = self.consumed()
        self.assertEqual(len(got), 5)
        self.assertNotIn("SIG-W-20260930-003-draft-below-cursor", got)
        self.publish(draft)
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertIn("was a draft at seeding", out)

    def test_seed_is_persisted_even_when_an_action_line_holds_the_run(self):
        self.publish(self.write(1), self.write(2))
        self.publish(self.write(3, action="PROME"))
        self.cursor.parent.mkdir(parents=True)
        self.cursor.write_text("SIG-W-20260930-002\n")
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertEqual(set(self.consumed()), {"SIG-W-20260930-001-x", "SIG-W-20260930-002-x"})
        self.assertEqual(self.cursor.read_text(), "SIG-W-20260930-002\n")


class FailClosed(Repo):
    def test_board_outside_any_git_repository_is_rc2_and_writes_nothing(self):
        with tempfile.TemporaryDirectory(prefix="no-git-") as bare:
            board = Path(bare) / "BOARD"
            board.mkdir()
            (board / "SIG-W-20260930-001-x.md").write_text(GOOD.format(
                sid="SIG-W-20260930-001", action="PROME", info="", head="h"))
            with patch.object(board_scan, "BOARD", board), \
                    patch.dict("os.environ", {"GIT_CEILING_DIRECTORIES": bare}):
                rc, out = self.scan("--advance", "--ack-actions")
        self.assertEqual(rc, 2)
        self.assertIn("cannot run", out)
        self.assertFalse(self.ledger.exists())
        self.assertFalse(self.cursor.exists())

    def test_malformed_ledger_is_rc2_and_is_left_untouched(self):
        self.publish(self.write(1, info="PROME"))
        self.ledger.parent.mkdir(parents=True)
        self.ledger.write_text("SIG-W-20260930-001-x\tI\nthis row is garbage\n")
        before = self.ledger.read_bytes()
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 2)
        self.assertEqual(self.ledger.read_bytes(), before)

    def test_repository_with_no_commit_is_rc2(self):
        with tempfile.TemporaryDirectory(prefix="no-head-") as fresh:
            subprocess.run(["git", "init", "-q", fresh], check=True)
            board = Path(fresh) / "BOARD"
            board.mkdir()
            (board / "SIG-W-20260930-001-x.md").write_text("x\n")
            with patch.object(board_scan, "BOARD", board):
                rc, out = self.scan("--advance")
        self.assertEqual(rc, 2)


class Interfaces(Repo):
    def test_parser_helpers_keep_their_contract(self):
        p = self.write(7, action="PROME, red", info="LIQUID")
        fm = board_scan.parse_front(p)
        self.assertEqual(fm["action"], ["PROME", "red"])
        self.assertEqual(fm["_headline"], "headline 7 x")
        self.assertEqual(board_scan.sig_key(p.name), ("20260930", 7))
        self.assertEqual(board_scan.clean("**bold** `x`"), "bold x")
        self.assertEqual(board_scan.parse_front(self.board / "missing.md"), {})

    def test_since_lists_consumed_legacy_files_without_calling_them_unreadable(self):
        legacy = "---\nto: [BRENT]\ncluster: OLD\n---\n# legacy\n"
        self.publish(self.write(1, body=legacy), self.write(2))
        self.cursor.parent.mkdir(parents=True)
        self.cursor.write_text("SIG-W-20260930-002\n")
        rc, out = self.scan("--since", "20260930")
        self.assertEqual(rc, 0)
        self.assertNotIn("UNREADABLE", out)
        self.assertIn("2 new", out)

    def test_audit_mode_still_counts_action_lines(self):
        self.publish(self.write(1, action="PROME"), self.write(2))
        rc, out = self.scan("--audit", "20260101")
        self.assertEqual(rc, 0)
        self.assertIn("1 ACTION-line / 2 signals", out)

    def test_tool_never_writes_under_board(self):
        self.publish(self.write(1, info="PROME"))
        before = sorted(p.name for p in self.board.iterdir())
        self.scan("--advance")
        self.assertEqual(sorted(p.name for p in self.board.iterdir()), before)


if __name__ == "__main__":
    unittest.main()
