from __future__ import annotations

import copy
import json
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "events" / "valid_binary.json"
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from projection import (  # noqa: E402
    PROJECTION_VERSION,
    REPOSITORY_ROOT,
    ProjectionError,
    load_projection,
    rebuild_projection,
    verify_projection,
)
from render import VIEW_NAMES, render_views  # noqa: E402
from test_core import event  # noqa: E402
from test_lifecycle import (  # noqa: E402
    FORECAST_ID,
    QUESTION_ID,
    close_command,
    correct_command,
    forecast_command,
    propose_command,
    question_command,
    typed_id,
    verify_command,
)
from writer import FixtureResultStore, FixtureResultWriter  # noqa: E402


AS_OF = "2026-08-26T00:00:00.000000Z"


def fixture_events() -> list[dict]:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


class DisposableProjectionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.workspace = Path(self.temporary.name) / "workspace"
        self.workspace.mkdir()
        self.events = fixture_events()

    @property
    def projection_path(self) -> Path:
        return self.workspace / ".rw" / "projection.sqlite"

    def test_projection_is_created_only_at_disposable_path(self):
        snapshot = rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        self.assertEqual(snapshot.path, self.projection_path)
        self.assertTrue(self.projection_path.is_file())
        self.assertEqual(snapshot.metadata["projection_version"], PROJECTION_VERSION)
        self.assertEqual(snapshot.metadata["authority_mode"], "SHADOW")
        self.assertIn("NON-AUTHORITATIVE", snapshot.metadata["notice"])
        self.assertEqual(set(snapshot.views), set(VIEW_NAMES))
        self.assertEqual(snapshot.views, render_views(self.events, render_as_of=AS_OF))

    def test_live_workspace_rw_directory_is_gitignored(self):
        completed = subprocess.run(
            ["git", "-C", str(REPOSITORY_ROOT), "check-ignore", "-q", ".rw/projection.sqlite"],
            check=False,
        )
        self.assertEqual(completed.returncode, 0)

    def test_delete_rw_and_rebuild_reproduces_semantics_and_view_bytes(self):
        first = rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        first_semantics = copy.deepcopy(first.semantic_state)
        first_view_bytes = {name: value.encode("utf-8") for name, value in first.views.items()}

        shutil.rmtree(self.workspace / ".rw")
        self.assertFalse(self.projection_path.exists())
        with self.assertRaises(ProjectionError) as missing:
            load_projection(self.workspace)
        self.assertEqual(missing.exception.findings[0].code, "PROJECTION_MISSING")

        second = rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        self.assertEqual(second.semantic_state, first_semantics)
        self.assertEqual(
            {name: value.encode("utf-8") for name, value in second.views.items()},
            first_view_bytes,
        )
        self.assertEqual(second.metadata, first.metadata)

    def test_projection_reconciles_against_explicit_durable_events(self):
        rebuilt = rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        verified = verify_projection(self.workspace, copy.deepcopy(self.events), render_as_of=AS_OF)
        self.assertEqual(verified, rebuilt)

    def test_input_order_does_not_change_semantics_or_views(self):
        first = rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        second = rebuild_projection(self.workspace, list(reversed(self.events)), render_as_of=AS_OF)
        self.assertEqual(second.metadata, first.metadata)
        self.assertEqual(second.semantic_state, first.semantic_state)
        self.assertEqual(second.views, first.views)

    def test_empty_durable_history_rebuilds_deterministically(self):
        first = rebuild_projection(self.workspace, [], render_as_of=AS_OF)
        shutil.rmtree(self.workspace / ".rw")
        second = rebuild_projection(self.workspace, [], render_as_of=AS_OF)
        self.assertEqual(first.metadata, second.metadata)
        self.assertEqual(first.semantic_state, second.semantic_state)
        self.assertEqual(first.views, second.views)
        self.assertEqual(first.metadata["source_event_count"], "0")

    def test_conflicted_history_remains_visible_after_rebuild(self):
        first = event("QuestionRegistered")
        child_a = copy.deepcopy(first)
        child_a.update(
            event_id="EVT-018f22e2-7d00-7000-8000-000000000007",
            event_type="QuestionClosed",
            stream_version=2,
            previous_event_id=first["event_id"],
            payload={
                "question_id": first["payload"]["question_id"],
                "closed_by": "SAM",
                "closed_at": "2026-09-18T20:00:00.000000Z",
            },
        )
        child_b = copy.deepcopy(child_a)
        child_b["event_id"] = "EVT-018f22e2-7d00-7000-8000-000000000008"
        snapshot = rebuild_projection(self.workspace, [child_b, first, child_a], render_as_of=AS_OF)
        self.assertIn(first["stream_id"], snapshot.semantic_state["conflicts"])
        self.assertIn("STREAM_CONFLICT", snapshot.views["EXCEPTIONS.md"])

    def test_full_lifecycle_state_and_corrected_view_are_projected(self):
        store = FixtureResultStore(self.workspace / "fixture-results" / "KERNEL")
        writer = FixtureResultWriter(store, writer_id="PROME")
        commands = [
            question_command(),
            forecast_command(),
            forecast_command(503, version=2, expected_version=1),
            close_command(),
            propose_command(),
            verify_command(),
            correct_command(),
        ]
        for event_number, command in enumerate(commands, start=801):
            outcome = writer.accept(
                command,
                event_id=typed_id("EVT", event_number),
                recorded_at=command["submitted_at"],
            )
            self.assertEqual(outcome.state, "WRITTEN", outcome.finding)
        snapshot = rebuild_projection(
            self.workspace,
            store.accepted_events(),
            render_as_of="2026-09-20T00:00:00.000000Z",
        )
        question = snapshot.semantic_state["question_states"][QUESTION_ID]
        forecast = snapshot.semantic_state["forecast_states"][FORECAST_ID]
        self.assertEqual((question["state"], question["outcome"]), ("FINAL", "NO"))
        self.assertEqual(forecast["state"], "LOCKED")
        self.assertEqual([version["probability"] for version in forecast["versions"]], [0.65, 0.72])
        self.assertIn(f"{QUESTION_ID}\t{FORECAST_ID}\t2\t0.72\tNO\t0.5184\t", snapshot.views["CALIBRATION.tsv"])

    def test_invalid_event_fails_before_projection_is_created(self):
        invalid = copy.deepcopy(self.events[1])
        invalid["payload"]["probability"] = 1.5
        with self.assertRaises(ProjectionError) as raised:
            rebuild_projection(self.workspace, [self.events[0], invalid], render_as_of=AS_OF)
        self.assertEqual(raised.exception.findings[0].code, "PROJECTION_EVENT_INVALID")
        self.assertFalse(self.projection_path.exists())

    def test_invalid_render_time_fails_before_projection_is_created(self):
        with self.assertRaises(ProjectionError) as raised:
            rebuild_projection(self.workspace, self.events, render_as_of="2026-08-26")
        self.assertEqual(raised.exception.findings[0].code, "PROJECTION_RENDER_AS_OF_INVALID")
        self.assertFalse(self.projection_path.exists())

    def test_rw_path_collision_fails_as_projection_error(self):
        (self.workspace / ".rw").write_text("not a disposable directory\n", encoding="utf-8")
        with self.assertRaises(ProjectionError) as raised:
            rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        self.assertEqual(raised.exception.findings[0].code, "PROJECTION_REBUILD_FAILED")

    def test_changed_durable_inputs_cannot_match_stale_projection(self):
        rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        with self.assertRaises(ProjectionError) as raised:
            verify_projection(self.workspace, self.events[:1], render_as_of=AS_OF)
        self.assertIn(
            "PROJECTION_METADATA_MISMATCH",
            {finding.code for finding in raised.exception.findings},
        )

    def test_corrupted_cached_view_fails_closed_and_rebuild_repairs_it(self):
        rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        connection = sqlite3.connect(self.projection_path)
        with connection:
            connection.execute(
                "UPDATE registered_views SET content = ? WHERE name = ?",
                (b"corrupted fixture view\n", "OPEN_QUESTIONS.md"),
            )
        connection.close()
        with self.assertRaises(ProjectionError) as raised:
            load_projection(self.workspace)
        self.assertEqual(raised.exception.findings[0].code, "PROJECTION_VIEW_MISMATCH")
        repaired = rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        self.assertIn("SAM=0.65", repaired.views["OPEN_QUESTIONS.md"])

    def test_corrupted_semantic_snapshot_fails_closed(self):
        rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        connection = sqlite3.connect(self.projection_path)
        with connection:
            connection.execute(
                "UPDATE semantic_snapshot SET semantic_json = ? WHERE singleton = 1",
                ("{}",),
            )
        connection.close()
        with self.assertRaises(ProjectionError) as raised:
            load_projection(self.workspace)
        self.assertEqual(raised.exception.findings[0].code, "PROJECTION_SEMANTIC_MISMATCH")

    def test_unregistered_projection_table_fails_closed(self):
        rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        connection = sqlite3.connect(self.projection_path)
        with connection:
            connection.execute("CREATE TABLE invented_authority(value TEXT)")
        connection.close()
        with self.assertRaises(ProjectionError) as raised:
            load_projection(self.workspace)
        self.assertEqual(raised.exception.findings[0].code, "PROJECTION_SCHEMA_INVALID")

    def test_live_repository_and_ancestor_are_refused(self):
        for target in (REPOSITORY_ROOT, REPOSITORY_ROOT.parent):
            with self.subTest(target=target):
                with self.assertRaises(ProjectionError) as raised:
                    rebuild_projection(target, self.events, render_as_of=AS_OF)
                self.assertEqual(raised.exception.findings[0].code, "PROJECTION_BOUNDARY_REFUSED")

    def test_rw_symlink_into_live_repository_is_refused(self):
        (self.workspace / ".rw").symlink_to(REPOSITORY_ROOT, target_is_directory=True)
        with self.assertRaises(ProjectionError) as raised:
            rebuild_projection(self.workspace, self.events, render_as_of=AS_OF)
        self.assertEqual(raised.exception.findings[0].code, "PROJECTION_BOUNDARY_REFUSED")
        self.assertFalse((REPOSITORY_ROOT / "projection.sqlite").exists())

    def test_cli_rebuild_and_check_print_perimeter_and_non_authority(self):
        rebuild = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "projection.py"),
                "--workspace",
                str(self.workspace),
                "--events",
                str(FIXTURE),
                "--as-of",
                AS_OF,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(rebuild.returncode, 0, rebuild.stdout + rebuild.stderr)
        self.assertIn("perimeter:", rebuild.stdout)
        self.assertIn("PASS: disposable projection rebuilt", rebuild.stdout)
        self.assertIn("SQLite has no authority", rebuild.stdout)
        check = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "projection.py"),
                "--workspace",
                str(self.workspace),
                "--events",
                str(FIXTURE),
                "--as-of",
                AS_OF,
                "--check",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
        self.assertIn("PASS: disposable projection verified", check.stdout)

    def test_cli_refusal_prints_perimeter_and_exception(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "projection.py"),
                "--workspace",
                str(REPOSITORY_ROOT),
                "--events",
                str(FIXTURE),
                "--as-of",
                AS_OF,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("perimeter:", completed.stdout)
        self.assertIn("EXCEPTION: disposable projection rebuild failed", completed.stdout)
        self.assertIn("PROJECTION_BOUNDARY_REFUSED", completed.stdout)


if __name__ == "__main__":
    unittest.main()
