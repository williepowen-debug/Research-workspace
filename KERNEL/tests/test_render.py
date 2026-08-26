from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from render import VIEW_NAMES, render_views, write_views  # noqa: E402
from test_core import event  # noqa: E402


AS_OF = "2026-08-26T00:00:00.000000Z"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


class RenderTests(unittest.TestCase):
    def test_file_backed_fixture_renders(self):
        events = json.loads((FIXTURES / "events" / "valid_binary.json").read_text(encoding="utf-8"))
        views = render_views(events, render_as_of=AS_OF)
        self.assertIn("SAM=0.65", views["OPEN_QUESTIONS.md"])

    def test_file_backed_adversarial_fixture_surfaces_exception(self):
        events = json.loads((FIXTURES / "events" / "orphan_forecast.json").read_text(encoding="utf-8"))
        views = render_views(events, render_as_of=AS_OF)
        self.assertIn("ORPHAN_FORECAST", views["EXCEPTIONS.md"])

    def test_registered_view_set_and_shadow_banners(self):
        views = render_views([event("QuestionRegistered"), event("ForecastSubmitted")], render_as_of=AS_OF)
        self.assertEqual(set(views), set(VIEW_NAMES))
        for value in views.values():
            self.assertIn("SHADOW", value)
            self.assertIn("NON-AUTHORITATIVE", value)

    def test_render_is_independent_of_input_order(self):
        question = event("QuestionRegistered")
        forecast = event("ForecastSubmitted")
        first = render_views([question, forecast], render_as_of=AS_OF)
        second = render_views([forecast, question], render_as_of=AS_OF)
        self.assertEqual(first, second)

    def test_write_then_check_is_byte_identical(self):
        views = render_views([event("QuestionRegistered"), event("ForecastSubmitted")], render_as_of=AS_OF)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            self.assertEqual(write_views(views, output), [])
            first_bytes = {name: (output / name).read_bytes() for name in VIEW_NAMES}
            self.assertEqual(write_views(views, output, check=True), [])
            for path in output.iterdir():
                path.unlink()
            self.assertEqual(write_views(views, output), [])
            second_bytes = {name: (output / name).read_bytes() for name in VIEW_NAMES}
        self.assertEqual(first_bytes, second_bytes)

    def test_check_detects_view_drift(self):
        views = render_views([], render_as_of=AS_OF)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            write_views(views, output)
            (output / "EXCEPTIONS.md").write_text("hand edit\n", encoding="utf-8")
            findings = write_views(views, output, check=True)
        self.assertIn("VIEW_DRIFT", {finding.code for finding in findings})

    def test_cli_check_prints_perimeter_status_and_claim_limits(self):
        events = FIXTURES / "events" / "valid_binary.json"
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            render = subprocess.run(
                [sys.executable, str(ROOT / "tools" / "render.py"), "--events", str(events),
                 "--output", str(output), "--as-of", AS_OF],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(render.returncode, 0, render.stdout + render.stderr)
            completed = subprocess.run(
                [sys.executable, str(ROOT / "tools" / "render.py"), "--events", str(events),
                 "--output", str(output), "--as-of", AS_OF, "--check"],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("perimeter: check=view-reproduction", completed.stdout)
        self.assertIn("PASS: registered fixture views verified deterministically", completed.stdout)
        self.assertIn("PASS proves:", completed.stdout)
        self.assertIn("PASS does not prove:", completed.stdout)

    def test_conflict_is_visible_and_stream_is_omitted(self):
        first = event("QuestionRegistered")
        child_a = copy.deepcopy(first)
        child_a["event_id"] = "EVT-018f22e2-7d00-7000-8000-000000000007"
        child_a["event_type"] = "QuestionClosed"
        child_a["stream_version"] = 2
        child_a["previous_event_id"] = first["event_id"]
        child_a["payload"] = {
            "question_id": first["payload"]["question_id"],
            "closed_by": "SAM",
            "closed_at": "2026-09-18T20:00:00.000000Z",
        }
        child_b = copy.deepcopy(child_a)
        child_b["event_id"] = "EVT-018f22e2-7d00-7000-8000-000000000008"
        views = render_views([first, child_a, child_b], render_as_of=AS_OF)
        self.assertIn("STREAM_CONFLICT", views["EXCEPTIONS.md"])
        self.assertNotIn(first["payload"]["claim"], views["OPEN_QUESTIONS.md"])

    def test_as_of_changes_overdue_state_explicitly(self):
        question = event("QuestionRegistered")
        before = render_views([question], render_as_of="2026-09-01T00:00:00.000000Z")
        after = render_views([question], render_as_of="2026-10-01T00:00:00.000000Z")
        self.assertIn("NOT_DUE", before["RESOLUTION_QUEUE.md"])
        self.assertIn("OVERDUE", after["RESOLUTION_QUEUE.md"])

    def test_invalid_as_of_is_rejected(self):
        with self.assertRaises(ValueError):
            render_views([], render_as_of="2026-08-26")


if __name__ == "__main__":
    unittest.main()
