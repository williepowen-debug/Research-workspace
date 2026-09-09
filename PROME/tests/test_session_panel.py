"""Supplied runtime snapshots must render safely without claiming live coverage."""
import contextlib
import datetime as dt
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock


SPEC = importlib.util.spec_from_file_location(
    "fleet_dashboard", Path(__file__).resolve().parents[1] / "tools/fleet_dashboard.py")
dashboard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dashboard)


class SessionPanelTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.path = self.root / "sessions.json"
        self.reference = dt.datetime(2026, 9, 8, 12, tzinfo=dt.timezone.utc)

    def render(self, data):
        self.path.write_text(json.dumps(data))
        with mock.patch.object(dashboard.subprocess, "run", side_effect=AssertionError("No discovery during rendering")):
            return dashboard.render_session_panel(self.path, self.reference)

    def test_opt_out_has_no_panel_or_file_read(self):
        with mock.patch("builtins.open", side_effect=AssertionError("No optional input requested")):
            self.assertEqual(dashboard.render_session_panel(None), "")

    def test_native_identity_parent_status_and_endpoint_scope(self):
        rendered = self.render({
            "observed_at": "2026-09-08T11:59:00Z", "host": "fixture-host",
            "coverage": "Visible namespace only", "processes": [], "claude": [],
            "codex": {"endpoint": "unix:///fixture/server.sock", "scope": "Only this endpoint",
                      "observed_at": "2026-09-08T11:58:00Z", "threads": [
                          {"id": "thread-child", "sessionId": "shared-tree", "parentThreadId": "thread-parent",
                           "cwd": "/fixture/PROME", "status": {"type": "active", "activeFlags": ["waitingOnApproval"]}}]}})
        for expected in ("thread-child", "shared-tree", "thread-parent", "/fixture/PROME",
                         "waitingOnApproval", "Only this endpoint", "1 minutes old", "2 minutes old"):
            self.assertIn(expected, rendered)
        self.assertIn("current liveness is UNKNOWN", rendered)

    def test_all_dynamic_fields_are_escaped(self):
        attack = '<script>alert("x")</script>'
        rendered = self.render({"observed_at": attack, "host": attack, "coverage": attack,
            "error": attack, "gaps": [{"gap": attack}],
            "processes": [{"runtime": attack, "identity": {"pid": attack}, "cwd": attack}],
            "claude": [{"id": attack, "cwd": attack, "status": attack, "parent": attack}],
            "codex": {"endpoint": attack, "scope": attack, "observed_at": attack, "threads": [
                {"id": attack, "cwd": attack, "parentThreadId": attack, "status": attack}]}})
        self.assertNotIn("<script>", rendered)
        self.assertNotIn('</script>', rendered)
        self.assertIn("&lt;script&gt;", rendered)
        self.assertIn("UNKNOWN age", rendered)

    def test_missing_and_malformed_input_render_visible_failure(self):
        for raw in (None, "{broken", "[]", '{"processes":{}}', '{"claude":[3]}',
                    '{"codex":{"threads":{}}}', '{"codex":[]}'):
            with self.subTest(raw=raw):
                path = self.root / ("missing" if raw is None else "bad.json")
                if raw is not None:
                    path.write_text(raw)
                rendered = dashboard.render_session_panel(path, self.reference)
                self.assertIn("UNKNOWN — PARSE FAILED", rendered)
                self.assertIn(str(path), rendered)

    def test_empty_or_unavailable_sources_never_claim_empty_fleet(self):
        for snapshot in ({}, {"processes": [], "claude": [], "codex": {
                "state": "UNKNOWN", "reason": "Endpoint unavailable"}}):
            with self.subTest(snapshot=snapshot):
                rendered = self.render(snapshot)
                self.assertIn("fleet presence UNKNOWN", rendered)
                self.assertIn("Missing rows do not prove a desk is absent", rendered)
                self.assertIn("UNKNOWN / reported gaps", rendered)
        self.assertIn("Endpoint unavailable", rendered)

    def test_stale_snapshot_keeps_original_time_separate_from_render_age(self):
        rendered = self.render({"observed_at": "2026-09-05T12:00:00+00:00", "processes": [], "claude": []})
        self.assertIn("2026-09-05T12:00:00+00:00", rendered)
        self.assertIn("4320 minutes old at render", rendered)
        self.assertIn("independent of dashboard build time", rendered)
        self.assertNotIn("built just now", rendered)

    def test_invalid_naive_future_timestamps_cannot_look_fresh(self):
        for stamp in (None, "2026-09-08T11:00:00", "invalid", "2026-09-09T12:00:00Z"):
            with self.subTest(stamp=stamp):
                self.assertIn("UNKNOWN age", self.render({"observed_at": stamp}))

    def test_process_presence_cannot_be_rendered_as_an_active_turn(self):
        rendered = self.render({"processes": [{"runtime": "codex", "identity": {"pid": 123},
                    "cwd": "/fixture/AGENTS/BRENT", "turn_status": "active"}]})
        self.assertIn("Turn status UNKNOWN — process presence only", rendered)
        self.assertIn("123", rendered)
        self.assertNotIn(">active<", rendered)

    def test_cli_passes_optional_file_to_build_with_temp_outputs_only(self):
        self.path.write_text('{}')
        output, state = self.root / "output.html", self.root / "state.json"
        def fixture_build(today, stamp, sessions_json=None):
            return dashboard.render_session_panel(sessions_json, self.reference), {"fixture": True}
        with mock.patch.object(dashboard, "build", side_effect=fixture_build) as build, \
             mock.patch.object(dashboard, "STATE_PATH", str(state)), \
             mock.patch("sys.argv", ["fleet_dashboard.py", "--sessions-json", str(self.path), "-o", str(output)]), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(dashboard.main(), 0)
        self.assertEqual(build.call_args.args[2], str(self.path))
        self.assertIn("runtime-sessions", output.read_text())
        self.assertEqual(json.loads(state.read_text()), {"fixture": True})


if __name__ == "__main__":
    unittest.main()
