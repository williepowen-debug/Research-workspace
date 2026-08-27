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

from gate_c_boundary import GateCBoundaryError, SyntheticMirrorBoundary, run_synthetic  # noqa: E402
from test_native import SyntheticGitRepository, ref  # noqa: E402
from test_permissions import command, submission_path  # noqa: E402
from core import canonical_bytes  # noqa: E402


RECORDED_AT = "2026-08-26T12:00:00.000000Z"
EVENT_ID = "EVT-018f22e2-7d00-7000-8000-000000000301"


class GateCBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.repo = SyntheticGitRepository(self)
        (self.repo.path / ".gate-c-synthetic-mirror.json").write_text(
            json.dumps({"authority": "NON_AUTHORITATIVE", "mode": "SYNTHETIC_MIRROR"}),
            encoding="utf-8",
        )
        self.boundary = SyntheticMirrorBoundary(self.repo.path)
        self.question = command("RegisterQuestion")
        companion = json.loads(self.repo.blob("native/companion.json"))
        selected = canonical_bytes(companion["questions"]["FIX-Q-001"])
        self.question["native_refs"] = [ref(
            self.repo.commit, "native/companion.json", "JSON_POINTER", "/questions/FIX-Q-001", selected
        )]
        self.path = submission_path(self.question)
        target = self.repo.path / self.path
        target.parent.mkdir(parents=True)
        target.write_text(json.dumps(self.question), encoding="utf-8")
        subprocess.run(["git", "-C", str(self.repo.path), "add", self.path], check=True)
        subprocess.run(["git", "-C", str(self.repo.path), "commit", "-q", "-m", "synthetic submission"], check=True)
        self.submission_commit = subprocess.run(
            ["git", "-C", str(self.repo.path), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.inventory = Path(self.temporary.name) / "inventory.json"
        self.inventory.write_text(json.dumps([self.path]), encoding="utf-8")

    def test_explicit_inventory_loads_exact_canonical_submission(self):
        loaded = self.boundary.load_inventory(self.inventory, self.submission_commit)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].path, self.path)
        self.assertEqual(loaded[0].command, self.question)

    def test_inventory_refuses_embedded_command_objects(self):
        self.inventory.write_text(json.dumps([{"path": self.path, "command": self.question}]), encoding="utf-8")
        with self.assertRaisesRegex(GateCBoundaryError, "path strings"):
            self.boundary.load_inventory(self.inventory, self.submission_commit)

    def test_inventory_refuses_traversal_and_non_allowlisted_paths(self):
        for path in ("../command.json", "KERNEL/shadow/events/fake.json"):
            with self.subTest(path=path):
                self.inventory.write_text(json.dumps([path]), encoding="utf-8")
                with self.assertRaises(GateCBoundaryError):
                    self.boundary.load_inventory(self.inventory, self.submission_commit)

    def test_inventory_refuses_more_than_three_commands(self):
        self.inventory.write_text(json.dumps([self.path] * 4), encoding="utf-8")
        with self.assertRaisesRegex(GateCBoundaryError, "1 to 3"):
            self.boundary.load_inventory(self.inventory, self.submission_commit)

    def test_path_actor_and_command_identity_must_agree(self):
        changed = copy.deepcopy(self.question)
        changed["actor_id"] = "RED"
        (self.repo.path / self.path).write_text(json.dumps(changed), encoding="utf-8")
        subprocess.run(["git", "-C", str(self.repo.path), "add", self.path], check=True)
        subprocess.run(["git", "-C", str(self.repo.path), "commit", "-q", "-m", "mismatched actor"], check=True)
        mismatched_commit = subprocess.run(
            ["git", "-C", str(self.repo.path), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        with self.assertRaisesRegex(GateCBoundaryError, "do not agree"):
            self.boundary.load_inventory(self.inventory, mismatched_commit)

    def test_mutable_submission_checkout_is_ignored(self):
        changed = copy.deepcopy(self.question)
        changed["actor_id"] = "RED"
        (self.repo.path / self.path).write_text(json.dumps(changed), encoding="utf-8")
        loaded = self.boundary.load_inventory(self.inventory, self.submission_commit)
        self.assertEqual(loaded[0].command, self.question)

    def test_missing_or_abbreviated_submission_commit_is_refused(self):
        for commit in ("0" * 40, self.submission_commit[:12]):
            with self.subTest(commit=commit):
                with self.assertRaisesRegex(GateCBoundaryError, "full commit SHA"):
                    self.boundary.load_inventory(self.inventory, commit)

    def test_unmarked_mirror_is_refused(self):
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(GateCBoundaryError, "marker required"):
                SyntheticMirrorBoundary(temporary)

    def test_live_repository_is_refused_before_marker_read(self):
        with self.assertRaisesRegex(GateCBoundaryError, "live repository"):
            SyntheticMirrorBoundary(ROOT.parent)

    def test_dry_run_is_ephemeral_and_does_not_write_mirror_results(self):
        loaded = self.boundary.load_inventory(self.inventory, self.submission_commit)
        event_ids = Path(self.temporary.name) / "event_ids.json"
        event_ids.write_text(json.dumps({self.question["command_id"]: EVENT_ID}), encoding="utf-8")
        run, result_root = run_synthetic(
            self.boundary,
            loaded,
            actors=ROOT / "tests/fixtures/permissions/actors.json",
            capabilities=ROOT / "tests/fixtures/permissions/capability-grants.json",
            event_ids=event_ids,
            recorded_at=RECORDED_AT,
            dry_run=True,
        )
        self.assertEqual(run.status, "PASS")
        self.assertFalse(result_root.exists())
        self.assertFalse(list((self.repo.path / "KERNEL").glob("shadow/events/**/*.json")))

    def test_synthetic_apply_writes_only_canonical_result_path(self):
        loaded = self.boundary.load_inventory(self.inventory, self.submission_commit)
        event_ids = Path(self.temporary.name) / "event_ids.json"
        event_ids.write_text(json.dumps({self.question["command_id"]: EVENT_ID}), encoding="utf-8")
        run, _ = run_synthetic(
            self.boundary,
            loaded,
            actors=ROOT / "tests/fixtures/permissions/actors.json",
            capabilities=ROOT / "tests/fixtures/permissions/capability-grants.json",
            event_ids=event_ids,
            recorded_at=RECORDED_AT,
            dry_run=False,
        )
        self.assertEqual(run.status, "PASS")
        results = list((self.repo.path / "KERNEL").glob("**/*.json"))
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].relative_to(self.repo.path).as_posix(), f"KERNEL/shadow/events/2026/08/{EVENT_ID}.json")


if __name__ == "__main__":
    unittest.main()
