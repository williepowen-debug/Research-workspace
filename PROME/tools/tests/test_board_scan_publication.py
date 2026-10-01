#!/usr/bin/env python3
"""Falsification set for board_scan.py's publication barrier and consumed ledger (2026-09-30, CATO RC1).

Acceptance: PROME/tools/tests/ACCEPTANCE_board_scan_publication_2026-09-30.md (written before the edit;
amended after independent reads 1 and 2; each finding F1-F6 and R2-1..R2-5 has a test here, named in its docstring).
Every test builds a throwaway git repository in a tempdir — never the live tree.
Run: python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_board_scan_publication.py
"""
import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
import urllib.parse
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

    def text(self, num, action="BRENT", info="LIQUID", head=None, day="20260930"):
        sid = f"SIG-W-{day}-{num:03d}"
        return GOOD.format(sid=sid, action=action, info=info, head=head or f"headline {num}")

    def write(self, num, action="BRENT", info="LIQUID", slug="x", body=None, day="20260930", head=None):
        p = self.board / f"SIG-W-{day}-{num:03d}-{slug}.md"
        p.write_text(body if body is not None else self.text(num, action, info, head, day), encoding="utf-8")
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
        return {urllib.parse.unquote(l.split("\t")[0]): l.split("\t")[1]
                for l in self.ledger.read_text().split("\n") if l and not l.startswith("#")}

    def set_cursor(self, value):
        self.cursor.parent.mkdir(parents=True, exist_ok=True)
        self.cursor.write_text(value + "\n")


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
        draft.write_text(self.text(5, action="PROME", info="", head="now published"))
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

    def test_published_content_comes_from_the_commit_not_the_working_copy(self):
        """Overlap (read-1 F7/F8): a file in HEAD AND edited in the working tree is read at its COMMITTED content."""
        p = self.write(1, action="PROME", head="committed ask")
        self.publish(p)
        p.write_text(self.text(1, action="BRENT", head="an uncommitted rewrite"))
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)                              # the published action is not hidden by the edit
        self.assertIn("committed ask", out)
        self.assertNotIn("an uncommitted rewrite", out)

    def test_published_action_signal_deleted_from_the_working_tree_still_stops(self):
        """Read-1 F1."""
        self.publish(self.write(1))
        self.scan("--advance")
        p = self.write(2, action="PROME", head="deleted locally")
        self.publish(p)
        p.unlink()
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertIn("deleted locally", out)

    def test_same_named_file_in_a_subdirectory_does_not_hide_a_published_signal(self):
        """Read-1 F2."""
        self.publish(self.write(1))
        self.scan("--advance")
        p = self.write(2, action="PROME", head="top level")
        self.publish(p)
        (self.board / "drafts").mkdir()
        shadow = self.board / "drafts" / p.name
        shadow.write_text(self.text(2, action="BRENT", head="a committed copy in a subfolder"))
        self.publish(shadow)
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertIn("top level", out)
        self.assertNotIn("subfolder", out)

    def test_guard_falsified_if_working_tree_files_count_as_published_the_draft_is_consumed(self):
        """The tests above depend on the HEAD barrier: replace it with the working tree and the defect returns."""
        self.publish(self.write(4))
        self.write(5, slug="draft")
        from_disk = lambda: {p.name: "0" * 39 + str(i) for i, p in enumerate(sorted(self.board.glob("SIG-W-*.md")))}  # noqa: E731
        disk_text = lambda shas: {s: sorted(self.board.glob("SIG-W-*.md"))[int(s[-1])].read_text() for s in shas}   # noqa: E731
        with patch.object(board_scan, "head_signals", from_disk), patch.object(board_scan, "read_blobs", disk_text):
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
        "duplicate action key (read-1 F6)": GOOD.replace("action: [{action}]", "action: [PROME]\naction: [{action}]"),
        "byte-order mark": "\ufeff" + GOOD,
        "indented second action inside a block scalar (read-2 R2-3)":
            GOOD.replace("action: [{action}]", "action: [PROME]\ndispatch_note: |\n  action: [{action}]"),
        "nested mapping carrying its own action (read-2 R2-3)":
            GOOD.replace("action: [{action}]", "action: [PROME]\nprior:\n  action: [{action}]"),
        "quoted second action key (read-2 R2-3)":
            GOOD.replace("action: [{action}]", "action: [{action}]\n\"action\": [PROME]"),
        "capitalised second action key": GOOD.replace("action: [{action}]", "action: [{action}]\nAction: [PROME]"),
        "the only action key is quoted": GOOD.replace("action: [{action}]", '"action": [{action}]'),
        "the only info key is indented": GOOD.replace("info: [{info}]", "  info: [{info}]"),
        "PROME inside a compound list element": GOOD.replace("action: [{action}]", "action: [PROME/TERRY]"),
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

    def test_acknowledged_unreadable_file_does_not_return_as_action_added(self):
        """Read-1 F9: nothing changed after the acknowledgement, so nothing re-surfaces."""
        body = GOOD.replace("signal_id: {sid}\n", "").replace("{action}", "PROME").replace("{info}", "").replace("{head}", "h")
        self.publish(self.write(2, body=body))
        p = self.board / "SIG-W-20260930-002-x.md"
        self.scan("--advance", "--ack-actions")
        rc, out = self.scan("--advance")
        self.assertEqual((rc, "nothing new" in out), (0, True))
        p.write_text(p.read_text() + "\na body-only edit\n")           # read-2 W3
        self.publish(p, msg="body edit")
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 0, out)
        self.assertNotIn("ACTION ADDED", out)

    def test_non_id_filename_can_be_acknowledged_without_bricking_the_ledger(self):
        """Read-1 F10: the writer may never emit a row its own reader rejects."""
        odd = self.board / "SIG-W-draft-oops.md"
        odd.write_text(self.text(1))
        self.publish(odd)
        self.assertEqual(self.scan("--advance")[0], 1)
        self.scan("--advance", "--ack-actions")
        self.assertEqual(self.consumed(), {"SIG-W-draft-oops": "U"})
        self.assertEqual(self.scan("--advance")[0], 0)


class OddNames(Repo):
    def test_names_with_separators_are_consumed_and_the_ledger_still_reads(self):
        """Read-2 R2-4: a tab, CR or Unicode line separator in a filename must not brick every later run."""
        for label, ch in {"tab": chr(9), "carriage return": chr(13), "U+2028": chr(0x2028), "U+0085": chr(0x85)}.items():
            with self.subTest(label):
                self.setUp()
                p = self.write(1, info="PROME", slug="a" + ch + "b")
                self.publish(p)
                rc, out = self.scan("--advance")
                self.assertEqual(rc, 0, out)
                self.assertEqual(self.consumed(), {p.name[:-3]: "I"})
                rc, out = self.scan("--advance")
                self.assertEqual((rc, "nothing new" in out), (0, True), out)

    def test_writer_refuses_a_ledger_its_reader_would_read_differently(self):
        """Falsify the write-back guard: with the key encoding disabled the save must fail closed, rc 2."""
        self.publish(self.write(1, info="PROME", slug="a" + chr(9) + "b"))
        with patch.object(board_scan, "_enc", lambda stem: stem):
            rc, out = self.scan("--advance")
        self.assertEqual(rc, 2, out)
        self.assertFalse(self.ledger.exists())


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
        p.write_text(self.text(1, action="PROME", info="", head="ask added later"))
        self.publish(p, msg="walter amends routing")
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertIn("ACTION ADDED", out)
        self.assertEqual(self.consumed()["SIG-W-20260930-001-x"], "I")     # held until acknowledged
        self.scan("--advance", "--ack-actions")
        self.assertEqual(self.consumed()["SIG-W-20260930-001-x"], "A")
        self.assertEqual(self.scan("--advance")[0], 0)

    def test_malformed_amendment_naming_prome_is_a_hard_stop(self):
        """Read-1 F4: the late path fails closed for the shapes the new-signal path fails closed on."""
        shapes = {
            "unbracketed": lambda t: t.replace("action: [PROME]", "action: PROME"),
            "block list": lambda t: t.replace("action: [PROME]", "action:\n  - PROME"),
            "lower case unbracketed": lambda t: t.replace("action: [PROME]", "action: prome"),
            "byte-order mark": lambda t: "\ufeff" + t,
            "duplicate key": lambda t: t.replace("action: [PROME]", "action: [PROME]\naction: [BRENT]"),
            "duplicate key, PROME absent (only the repeat check sees it)":
                lambda t: t.replace("action: [PROME]", "action: [BRENT]\naction: [TERRY]"),
            "double-quoted key (read-2 R2-2)": lambda t: t.replace("action: [PROME]", '"action": [PROME]'),
            "single-quoted key (read-2 R2-2)": lambda t: t.replace("action: [PROME]", "'action': [PROME]"),
            "stray --- before the action line (read-2 R2-2)": lambda t: t.replace("action: [PROME]", "---\naction: [PROME]"),
            "action key replaced by legacy to: (read-2 R2-2)": lambda t: t.replace("action: [PROME]", "to: [PROME]"),
        }
        for label, mangle in shapes.items():
            with self.subTest(label):
                self.setUp()
                p = self.write(1, info="PROME")
                self.publish(p)
                self.scan("--advance")
                p.write_text(mangle(self.text(1, action="PROME", info="")))
                self.publish(p, msg="amend")
                rc, out = self.scan("--advance")
                self.assertEqual(rc, 1, out)
                self.assertEqual(self.consumed()["SIG-W-20260930-001-x"], "I")

    def test_reader_added_after_an_earlier_removal_resurfaces(self):
        """Read-2 R2-1: 'late' is decided against the blob that was consumed, not a sticky class."""
        p = self.write(1, action="PROME", head="first ask")
        self.publish(p)
        self.scan("--advance", "--ack-actions")
        p.write_text(self.text(1, action="TERRY", head="ask withdrawn"))
        self.publish(p, msg="walter removes PROME")
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 0, out)
        self.assertIn("routing CHANGED", out)                 # read-2 R2-5: said, not hidden
        self.assertIn("action → not routed", out)
        self.assertEqual(self.consumed()["SIG-W-20260930-001-x"], "O")
        p.write_text(self.text(1, action="PROME", head="a NEW ask"))
        self.publish(p, msg="walter routes it back")
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1, out)
        self.assertIn("a NEW ask", out)

    def test_info_added_to_a_consumed_signal_is_listed_not_called_unchanged(self):
        """Read-2 R2-5."""
        p = self.write(1)
        self.publish(p)
        self.scan("--advance")
        p.write_text(self.text(1, info="PROME", head="now copied in"))
        self.publish(p, msg="amend")
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 0, out)
        self.assertIn("routing CHANGED", out)
        self.assertIn("not routed → info", out)
        self.assertNotIn("routing unchanged", out)
        self.assertEqual(self.consumed()["SIG-W-20260930-001-x"], "I")

    def test_consumed_blob_that_no_longer_exists_makes_the_signal_new_again(self):
        self.publish(self.write(1, action="PROME", head="still an ask"))
        self.ledger.parent.mkdir(parents=True, exist_ok=True)
        self.ledger.write_text("SIG-W-20260930-001-x\tO\t" + "f" * 40 + "\n")
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1, out)
        self.assertIn("still an ask", out)

    def test_amendment_that_leaves_routing_alone_is_quiet(self):
        p = self.write(1, info="PROME")
        self.publish(p)
        self.scan("--advance")
        p.write_text(p.read_text() + "\nstatus note appended by the publisher\n")
        self.publish(p, msg="amend body")
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 0)
        self.assertIn("amended since consumption", out)
        self.assertEqual((self.scan("--advance")[1]).count("amended since consumption"), 0)

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
        self.set_cursor("SIG-W-20260930-004")
        rc, out = self.scan("--seed-from-cursor")
        self.assertEqual(rc, 0)
        self.assertIn("1 new", out)
        self.assertIn("above the cursor", out)
        self.assertEqual(len(self.consumed()), 4)               # 001-004; 005 is new, not consumed by seeding
        self.assertNotIn("SIG-W-20260930-003-draft-below-cursor", self.consumed())
        self.scan("--advance")
        self.publish(draft)
        rc, out = self.scan("--advance")
        self.assertEqual(rc, 1)
        self.assertIn("was a draft at seeding", out)

    def test_seed_never_records_an_action_row(self):
        """Read-1 F3 completed at read 2: a seed cannot acknowledge an action; the row surfaces instead."""
        self.publish(self.write(1, action="PROME", head="old ask"), self.write(2))
        self.set_cursor("SIG-W-20260930-002")
        rc, out = self.scan("--seed-from-cursor")
        self.assertEqual(rc, 1, out)
        self.assertIn("old ask", out)
        self.assertEqual(self.consumed(), {"SIG-W-20260930-002-x": "O"})

    def test_seed_is_refused_when_the_ledger_is_in_head_but_lost_from_disk(self):
        """Read-2 W1: a lost ledger is restored from git, never re-seeded."""
        self.publish(self.write(4))
        self.publish(self.write(6, info="PROME"))
        self.scan("--advance")
        self.git("add", str(self.ledger), str(self.cursor))
        self.git("commit", "-q", "-m", "state")
        self.publish(self.write(5, action="PROME", head="held ask"))
        self.assertEqual(self.scan("--advance")[0], 1)
        self.ledger.unlink()
        rc, out = self.scan("--seed-from-cursor")
        self.assertEqual(rc, 2, out)
        self.assertIn("in HEAD", out)
        self.assertFalse(self.ledger.exists())

    def test_missing_ledger_with_a_cursor_is_rc2_and_never_reseeds(self):
        """Read-1 F3: a lost ledger must not acknowledge a held action signal nobody was shown."""
        self.publish(self.write(4))
        self.publish(self.write(6, info="PROME"))
        self.scan("--advance")
        self.publish(self.write(5, action="PROME", head="held ask"))
        self.assertEqual(self.scan("--advance")[0], 1)
        self.ledger.unlink()
        for argv in ((), ("--advance",), ("--advance", "--ack-actions")):
            rc, out = self.scan(*argv)
            self.assertEqual(rc, 2, out)
            self.assertIn("MISSING", out)
            self.assertFalse(self.ledger.exists())

    def test_seed_from_cursor_refuses_to_run_twice(self):
        self.publish(self.write(1))
        self.set_cursor("SIG-W-20260930-001")
        self.assertEqual(self.scan("--seed-from-cursor")[0], 0)
        before = self.ledger.read_bytes()
        rc, out = self.scan("--seed-from-cursor")
        self.assertEqual(rc, 2)
        self.assertEqual(self.ledger.read_bytes(), before)

    def test_first_run_with_neither_cursor_nor_ledger_shows_everything(self):
        self.publish(self.write(1), self.write(2, info="PROME"))
        rc, out = self.scan()
        self.assertEqual(rc, 0)
        self.assertIn("2 new", out)


class FailClosed(Repo):
    def test_board_outside_any_git_repository_is_rc2_and_writes_nothing(self):
        with tempfile.TemporaryDirectory(prefix="no-git-") as bare:
            board = Path(bare) / "BOARD"
            board.mkdir()
            (board / "SIG-W-20260930-001-x.md").write_text(self.text(1, action="PROME", info=""))
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
        self.ledger.write_text("SIG-W-20260930-001-x\tI\t" + "a" * 40 + "\nthis row is garbage\n")
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

    def test_cannot_run_conditions_exit_2_never_1(self):
        """Read-1 F5: a failure to run must not look like an action-line stop."""
        self.publish(self.write(1, action="PROME"))
        self.ledger.parent.mkdir(parents=True)
        self.ledger.write_bytes(b"SIG-W-20260930-001-x\tA\t" + b"a" * 40 + b"\n\xff\xfe\n")
        self.assertEqual(self.scan()[0], 2)                       # ledger not UTF-8
        self.ledger.write_text("")                                # a readable (empty) ledger is present
        self.assertEqual(self.scan()[0], 1)                       # control: with it the scan runs and stops on the action
        self.cursor.write_bytes(b"\xff\xfe\n")
        self.assertEqual(self.scan()[0], 2)                       # cursor not UTF-8 — the only thing that changed
        self.ledger.unlink()
        self.cursor.unlink()
        with patch.object(board_scan.subprocess, "run", side_effect=FileNotFoundError("git")):
            self.assertEqual(self.scan()[0], 2)                   # git not installed
        with patch.object(board_scan, "head_signals", side_effect=RuntimeError("boom")):
            rc, out = self.scan("--advance")
        self.assertEqual(rc, 2)                                   # anything unexpected
        self.assertFalse(self.ledger.exists())

    def test_module_imports_without_git(self):
        code = "import sys; sys.path.insert(0, %r); import board_scan; print(board_scan.REPO.name)" % str(
            Path(board_scan.__file__).resolve().parent)
        r = subprocess.run([sys.executable, "-B", "-c", code], capture_output=True, text=True,
                           cwd="/", env={"PATH": "/nonexistent"})
        self.assertEqual(r.returncode, 0, r.stderr)


class Interfaces(Repo):
    def test_parser_helpers_keep_their_contract(self):
        p = self.write(7, action="PROME, red", info="LIQUID", head="headline seven")
        fm = board_scan.parse_front(p)
        self.assertEqual(fm["action"], ["PROME", "red"])
        self.assertEqual(fm["_headline"], "headline seven")
        self.assertEqual(board_scan.sig_key(p.name), ("20260930", 7))
        self.assertEqual(board_scan.clean("**bold** `x`"), "bold x")
        self.assertEqual(board_scan.parse_front(self.board / "missing.md"), {})

    def test_since_lists_consumed_legacy_files_without_calling_them_unreadable(self):
        legacy = "---\nto: [BRENT]\ncluster: OLD\n---\n# legacy\n"
        self.publish(self.write(1, body=legacy), self.write(2))
        self.set_cursor("SIG-W-20260930-002")
        self.scan("--seed-from-cursor")
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
