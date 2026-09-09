"""Activity and identity fixtures never infer liveness from files or stored threads."""
import contextlib
import datetime as dt
import fcntl
import io
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import desk_activity as activity
import session_identity as identity
import session_presence as presence


class ActivityTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base = Path(temp.name)
        self.root = self.base / "repo"
        self.root.mkdir()
        self.desk = self.root / "AGENTS/SAM"
        self.desk.mkdir(parents=True)
        self.state = self.base / "activity.json"
        self.clock = dt.datetime(2026, 9, 9, 20, tzinfo=dt.timezone.utc)
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        (self.desk / "work.md").write_text("initial")
        (self.root / ".gitignore").write_text("*.ignored\n")
        self.git("add", "--", "AGENTS/SAM/work.md", ".gitignore")
        self.git("commit", "-qm", "SAM: initial work")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, capture_output=True, check=True)

    def observe(self):
        self.clock += dt.timedelta(seconds=1)
        return activity.observe(self.root, ["SAM"], self.state, self.clock)

    def test_first_same_changed_restored_mtime_and_no_longer_pending(self):
        path = self.desk / "work.md"
        path.write_text("dirty first")
        first = self.observe()
        self.assertEqual(first["desks"]["SAM"]["comparison"]["changed"], [])
        self.assertIn("first observation", first["desks"]["SAM"]["comparison"]["meaning"])
        second = self.observe()
        self.assertEqual(second["desks"]["SAM"]["comparison"]["changed"], [])
        old_stat = path.stat()
        path.write_text("dirty second")
        os.utime(path, ns=(old_stat.st_atime_ns, old_stat.st_mtime_ns))
        third = self.observe()
        self.assertEqual(third["desks"]["SAM"]["comparison"]["changed"], ["AGENTS/SAM/work.md"])
        self.assertEqual(third["desks"]["SAM"]["comparison"]["baseline_observed_at"], second["observed_at"])
        path.write_text("initial")
        fourth = self.observe()
        self.assertEqual(fourth["desks"]["SAM"]["comparison"]["no_longer_pending"], ["AGENTS/SAM/work.md"])
        view = activity.public_view(fourth, "SAM")
        self.assertEqual(view["current_session_state"], "UNKNOWN")

    def test_untracked_ignored_rename_and_deletion(self):
        (self.desk / "literal*\nname.md").write_text("new")
        (self.desk / "secret.ignored").write_text("do not inventory")
        self.git("mv", "AGENTS/SAM/work.md", "AGENTS/SAM/renamed.md")
        data = self.observe()["desks"]["SAM"]["pending"]
        self.assertIn("AGENTS/SAM/literal*\nname.md", data)
        self.assertNotIn("AGENTS/SAM/secret.ignored", data)
        self.assertEqual(data["AGENTS/SAM/renamed.md"]["original_path"], "AGENTS/SAM/work.md")
        self.git("commit", "-qm", "SAM: rename", "--", "AGENTS/SAM/work.md", "AGENTS/SAM/renamed.md")
        (self.desk / "renamed.md").unlink()
        self.assertEqual(self.observe()["desks"]["SAM"]["pending"]["AGENTS/SAM/renamed.md"]["fingerprint"], "ABSENT")

    def test_foreign_commit_and_message_body_do_not_become_self_commit(self):
        (self.desk / "work.md").write_text("foreign write")
        self.git("commit", "-qam", "PROME: packet\n\nSAM: quoted body")
        self.assertEqual(activity.last_commit(self.root, "SAM")["subject"], "SAM: initial work")

    def test_corrupt_foreign_future_locked_snapshot_preserves_existing_bytes(self):
        good = self.observe()
        for mutate in (lambda x: x.update(repository="elsewhere"), lambda x: x.update(host="other-host"),
                       lambda x: x.update(observed_at="2999-01-01T00:00:00+00:00"),
                       lambda x: x.update(desks=[])):
            data = json.loads(json.dumps(good))
            mutate(data)
            self.state.write_text(json.dumps(data))
            before = self.state.read_bytes()
            with self.assertRaises((ValueError, TypeError, KeyError)):
                self.observe()
            self.assertEqual(before, self.state.read_bytes())
        self.state.write_text("{broken")
        with self.assertRaises(ValueError):
            self.observe()
        self.assertEqual(self.state.read_text(), "{broken")
        self.state.write_text(json.dumps(good))
        with self.state.with_suffix(".json.lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.assertRaises(BlockingIOError):
                self.observe()
        self.assertEqual(json.loads(self.state.read_text()), good)

    def test_unmeasured_content_stays_unknown_while_git_failure_preserves_baseline(self):
        self.observe()
        before = self.state.read_bytes()
        (self.desk / "large.md").write_bytes(b"x" * (activity.MAX_FILE_BYTES + 1))
        value = self.observe()
        self.assertTrue(value["baseline_advanced"])
        self.assertFalse(value["desks"]["SAM"]["content_complete"])
        self.assertEqual(value["desks"]["SAM"]["comparison"]["changed"], [])
        before = self.state.read_bytes()
        with mock.patch.object(activity, "git", side_effect=ValueError("Git failed")):
            with self.assertRaises(ValueError):
                self.observe()
        self.assertEqual(before, self.state.read_bytes())

    def test_symlinks_special_files_and_sensitive_paths_are_not_read(self):
        (self.desk / "link.md").symlink_to(self.root / ".gitignore")
        os.mkfifo(self.desk / "pipe")
        for name in ("link.md", "pipe", ".env", "transcripts/private.jsonl", "test.events.jsonl", "test.input.txt"):
            with self.subTest(name=name):
                digest, reason, used = activity.fingerprint(self.root, "AGENTS/SAM/" + name, 1024)
                self.assertIsNone(digest)
        (self.desk / "linked-dir").symlink_to(self.root, target_is_directory=True)
        self.assertIsNone(activity.fingerprint(self.root, "AGENTS/SAM/linked-dir/.gitignore", 1024)[0])

    def test_snapshot_cannot_overwrite_repo_file(self):
        with self.assertRaises(ValueError):
            activity.observe(self.root, ["SAM"], self.desk / "work.md", self.clock)
        self.assertEqual((self.desk / "work.md").read_text(), "initial")

    def test_failed_enumeration_cannot_claim_commit_or_file_changes(self):
        self.observe()
        before = self.state.read_bytes()
        with mock.patch.object(activity, "pending", side_effect=ValueError("failed enumeration")):
            result = self.observe()
        self.assertFalse(result["baseline_advanced"])
        comparison = result["desks"]["SAM"]["comparison"]
        for key in ("changed", "no_longer_pending", "self_commit_changed"):
            self.assertIsNone(comparison[key])
        self.assertIn("UNKNOWN", comparison["meaning"])
        self.assertEqual(before, self.state.read_bytes())


class IdentityTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.database = self.root / "state.sqlite"
        with sqlite3.connect(self.database) as c:
            c.execute("CREATE TABLE threads (id TEXT, cwd TEXT, source TEXT, archived INT, updated_at INT, first_user_message TEXT)")
            for tid, desk, source in (("prome", "PROME", "cli"), ("sam1", "AGENTS/SAM", "cli"),
                    ("sam2", "AGENTS/SAM", "cli"), ("child", "AGENTS/SAM", '{"subagent":{"thread_spawn":{"parent_thread_id":"sam1"}}}')):
                c.execute("INSERT INTO threads VALUES (?,?,?,?,?,?)", (tid, str(self.root / desk), source, 0, 100, "PRIVATE DO NOT READ"))
        self.before = self.database.read_bytes()

    def test_self_exact_cwd_multiple_candidates_helpers_read_only(self):
        value = identity.collect(self.root, ["PROME", "SAM"], self.database, self.root, "prome")
        self.assertTrue(value["PROME"]["caller_session"]["metadata_corroborated"])
        self.assertEqual(len(value["SAM"]["stored_candidates"]), 3)
        self.assertIsNone(value["SAM"]["caller_session"])
        child = next(x for x in value["SAM"]["stored_candidates"] if x["id"] == "child")
        self.assertEqual((child["kind"], child["parent_id"]), ("helper", "sam1"))
        self.assertNotIn("PRIVATE", json.dumps(value))
        self.assertEqual(self.database.read_bytes(), self.before)
        self.assertTrue(all(x["current_presence"] == "UNKNOWN" for x in value.values()))

    def test_missing_wrong_schema_and_wrong_cwd_are_unknown_without_creation(self):
        missing = self.root / "missing.sqlite"
        result = identity.collect(self.root, ["SAM"], missing, self.root / "other/AGENTS/SAM", "unknown")
        self.assertFalse(missing.exists())
        self.assertIsNone(result["SAM"]["caller_session"])
        self.assertIn("UNKNOWN", result["SAM"]["stored_coverage"])
        wrong = self.root / "wrong.sqlite"
        with sqlite3.connect(wrong):
            pass
        self.assertEqual(identity.collect(self.root, ["SAM"], wrong, self.root, "prome")["SAM"]["stored_candidates"], [])

    def test_no_database_does_not_assign_sam_from_another_caller(self):
        result = identity.collect(self.root, ["SAM"], None, self.root / "PROME", "prome")
        self.assertIsNone(result["SAM"]["caller_session"])

    def test_overview_includes_sam_without_due_row_when_runtime_missing(self):
        activities = {"observed_at": "2026-09-09T20:00:00Z", "desks": {"SAM": {"complete": True,
            "pending": {"AGENTS/SAM/work.md": {"status": " M", "fingerprint": "hidden"}},
            "last_self_commit": None, "comparison": {"meaning": "first observation"}}}}
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            rc = presence.report([], {}, activities=activities, identities={}, desks=["SAM"])
        output = stream.getvalue()
        self.assertEqual(rc, 1)
        self.assertIn("SAM\t", output)
        self.assertIn("AGENTS/SAM/work.md", output)
        self.assertNotIn("hidden", output)
        self.assertIn('"spawn_authorized": false', output)


if __name__ == "__main__":
    unittest.main()
