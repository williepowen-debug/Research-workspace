"""Boot safety fixtures; never advance the real BOARD cursor."""
import contextlib
import datetime as dt
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import boot_read
import boot_session
import prome_gate
import session_bridge
import session_presence


class BootTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)

    def test_pages_reconstruct_unicode_and_long_lines_and_require_digest(self):
        path = self.root / "doc.md"
        original = "😀x" * 9000 + "\nend\n"
        path.write_text(original)
        chunks, offset, sha = [], 0, None
        while True:
            page = boot_read.page(path, offset, sha)
            self.assertLessEqual(len(page["text"]), boot_read.PAGE_CHARS)
            chunks.append(page["text"])
            if page["eof"]:
                self.assertIsNone(page["next_offset"])
                break
            offset, sha = page["next_offset"], page["sha256"]
        self.assertEqual("".join(chunks), original)
        with self.assertRaises(ValueError):
            boot_read.page(path, 1)
        path.write_text(original + "changed")
        with self.assertRaisesRegex(ValueError, "Source changed"):
            boot_read.page(path, offset, sha)

    def test_completed_boot_replays_verdict_without_another_gate(self):
        run_dir = self.root / "boot"
        def gate(cmd, **kwargs):
            self.assertTrue((run_dir / "attempt.json").exists())
            kwargs["stdout"].write("fixture blocking failure\n")
            return subprocess.CompletedProcess(cmd, 1)
        with mock.patch.object(boot_session.subprocess, "run", side_effect=gate) as run, \
                contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(boot_session.run_once(run_dir), 1)
            self.assertEqual(boot_session.run_once(run_dir), 1)
        self.assertEqual(run.call_count, 1)
        self.assertIn("blocking failure", (run_dir / "gate.txt").read_text())

    def test_serialized_unicode_and_escaped_pages_are_bounded_and_reconstruct(self):
        path = self.root / "escaped.md"
        original = ("\x00\\\"😀漢\n" * 2500) + "end"
        path.write_text(original)
        chunks, offset, sha = [], 0, None
        while True:
            cli = subprocess.run([sys.executable, boot_read.__file__, str(path), "--offset", str(offset),
                *(["--sha256", sha] if sha else [])], capture_output=True, text=True, check=True)
            value = json.loads(cli.stdout)
            self.assertLessEqual(len(json.dumps(value["text"], ensure_ascii=False).encode("utf-8")) - 2,
                                 boot_read.PAGE_TEXT_BYTES)
            self.assertLess(len(cli.stdout.encode("utf-8")), boot_read.PAGE_TEXT_BYTES + 1024)
            chunks.append(value["text"])
            if value["eof"]:
                break
            offset, sha = value["next_offset"], value["sha256"]
        self.assertEqual("".join(chunks), original)

    def test_second_attempt_while_first_running_does_not_start_gate(self):
        run_dir = self.root / "boot"
        def gate(cmd, **kwargs):
            self.assertEqual(boot_session.run_once(run_dir), 2)
            return subprocess.CompletedProcess(cmd, 0)
        with mock.patch.object(boot_session.subprocess, "run", side_effect=gate) as run, \
                contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(boot_session.run_once(run_dir), 0)
        self.assertEqual(run.call_count, 1)

    def test_crash_and_wrong_repo_cannot_replay(self):
        run_dir = self.root / "boot"
        with mock.patch.object(boot_session.subprocess, "run", side_effect=OSError("crash")) as run, \
                contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(OSError):
                boot_session.run_once(run_dir)
            self.assertEqual(boot_session.run_once(run_dir), 2)
            (run_dir / "attempt.json").write_text(json.dumps({"repository": "wrong", "mode": "boot"}))
            self.assertEqual(boot_session.run_once(run_dir), 2)
        self.assertEqual(run.call_count, 1)

    def test_fourth_warning_saved_and_omission_visible(self):
        with mock.patch.object(prome_gate, "LOG_DIR", self.root), \
                mock.patch.object(prome_gate, "results", []):
            ok = prome_gate.run_script(prome_gate.ADVISE, "fixture", [sys.executable, "-c",
                "print('⚠️ first\\n⚠️ second\\n⚠️ third\\n⚠️ fourth'); raise SystemExit(1)"], "fixture")
            self.assertFalse(ok)
            self.assertIn("1 additional flag", prome_gate.results[0][3])
            self.assertIn("⚠️ fourth", next(self.root.glob("*.txt")).read_text())
            self.assertEqual(prome_gate.results[0][0], prome_gate.ADVISE)


class PresenceTests(unittest.TestCase):
    def setUp(self):
        self.reference = dt.datetime(2026, 9, 9, 20, tzinfo=dt.timezone.utc)
        self.snapshot = {"observed_at": self.reference.isoformat(), "host": "fixture", "claude": [],
            "processes": [], "codex": {"observed_at": self.reference.isoformat(), "endpoint": "fixture",
                "threads": [{"id": "child", "sessionId": "tree", "parentThreadId": "parent",
                    "cwd": str(session_presence.ROOT / "AGENTS/BRENT"), "status": {"type": "idle"}}]}}
        self.rows = [(f"D:L{i}", "2026-09-09", 0, "BRENT", "DARK", "old commit", "due") for i in range(1, 5)]

    def render(self, data):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            rc = session_presence.report(self.rows, data, self.reference, "fixture")
        return rc, stream.getvalue()

    def test_exact_desk_parent_idle_preserved_without_spawn_grant(self):
        rc, output = self.render(self.snapshot)
        self.assertEqual(rc, 0)
        for value in ('"parentThreadId": "parent"', '"type": "idle"', '"spawn_authorized": false', "D:L4"):
            self.assertIn(value, output)
        view = session_presence.evidence("BRENT", self.snapshot, self.reference)
        self.assertEqual(len(view["sessions_observed"]), 1)
        self.assertEqual(view["current_presence"], "UNKNOWN")
        self.snapshot["codex"]["threads"][0]["cwd"] = "/different/repo/AGENTS/BRENT"
        self.assertEqual(session_presence.evidence("BRENT", self.snapshot, self.reference)["sessions_observed"], [])

    def test_empty_and_process_only_never_become_absence_or_active_turn(self):
        self.snapshot["codex"]["threads"] = []
        self.snapshot["processes"] = [{"runtime": "codex", "identity": {"pid": 123},
            "cwd": str(session_presence.ROOT / "AGENTS/BRENT"), "turn_status": "active"}]
        view = session_presence.evidence("BRENT", self.snapshot, self.reference)
        self.assertEqual(view["sessions_observed"], [])
        self.assertEqual(view["processes_observed"][0]["turn_status"], "UNKNOWN")
        self.assertFalse(view["spawn_authorized"])
        self.assertIn("Missing sightings NEVER prove absence", self.render(self.snapshot)[1])

    def test_stale_future_naive_wrong_host_malformed_keep_all_rows_unknown(self):
        variants = [[], {**self.snapshot, "host": "other"}, {**self.snapshot, "claude": [3]},
            {**self.snapshot, "codex": {"threads": {}}}]
        for stamp in (None, "2026-09-09T19:58:59Z", "2026-09-09T20:00:01Z", "2026-09-09T20:00:00"):
            variants.append({**self.snapshot, "observed_at": stamp})
        for data in variants:
            with self.subTest(data=data):
                rc, output = self.render(data)
                self.assertEqual(rc, 1)
                self.assertIn("D:L4", output)
                for line in output.splitlines():
                    if line.startswith("D:"):
                        self.assertNotIn("sessions_observed", line)
                        self.assertIn('"current_presence": "UNKNOWN"', line)

    def test_stale_endpoint_timestamp_cannot_borrow_fresh_snapshot_time(self):
        self.snapshot["codex"]["observed_at"] = "2026-09-09T19:00:00Z"
        self.assertEqual(session_presence.evidence("BRENT", self.snapshot, self.reference)["sessions_observed"], [])

    def test_inventory_rejects_thread_identity_mismatch(self):
        rpc = mock.Mock()
        rpc.call.side_effect = [{"data": ["wanted"]}, {"thread": {"id": "other"}}]
        with self.assertRaises(session_bridge.BridgeError):
            session_bridge.codex_inventory(rpc)


if __name__ == "__main__":
    unittest.main()
