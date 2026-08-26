from __future__ import annotations

import copy
import json
import multiprocessing
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLANNING_FIXTURE = ROOT / "tests" / "fixtures" / "planning" / "question_forecast_batch.json"
PERMISSION_FIXTURES = ROOT / "tests" / "fixtures" / "permissions"
sys.path.insert(0, str(ROOT / "tools"))

from locking import FixtureAcceptanceLock  # noqa: E402
from permissions import PermissionRegistry, authorize_command  # noqa: E402
from writer import FixtureResultStore, FixtureResultWriter  # noqa: E402


RECORDED_AT = "2026-08-25T12:06:00.000000Z"
EVENT_1 = "EVT-018f22e2-7d00-7000-8000-000000000201"
EVENT_2 = "EVT-018f22e2-7d00-7000-8000-000000000202"


def fixture_question() -> dict:
    fixture = json.loads(PLANNING_FIXTURE.read_text(encoding="utf-8"))
    return next(
        command
        for command in fixture["submissions"]
        if command["command_type"] == "RegisterQuestion"
    )


def _locked_pass_worker(
    label: str,
    store_root: str,
    command: dict,
    event_id: str,
    attempted,
    entered,
    release,
    outcomes,
) -> None:
    attempted.set()
    try:
        writer = FixtureResultWriter(FixtureResultStore(store_root), writer_id="PROME")
        with writer.acceptance_pass([command]) as acceptance:
            entered.set()
            if release is not None and not release.wait(5):
                raise TimeoutError("fixture worker was not released")
            if acceptance.plan.ready:
                outcome = acceptance.accept(
                    command,
                    event_id=event_id,
                    recorded_at=RECORDED_AT,
                )
                state = outcome.state
            elif command["command_id"] in acceptance.plan.completed:
                state = "COMPLETED"
            else:
                state = "NOT_READY"
        outcomes.put((label, state, None))
    except BaseException as exc:
        outcomes.put((label, "ERROR", f"{type(exc).__name__}: {exc}"))


class FixtureLockingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.workspace_root = Path(self.temporary.name)
        self.store_root = self.workspace_root / "KERNEL"
        self.command = fixture_question()

    def tearDown(self):
        self.temporary.cleanup()

    def test_lock_uses_injected_disposable_path_and_releases(self):
        lock = FixtureAcceptanceLock(self.workspace_root)
        self.assertEqual(
            lock.path,
            self.workspace_root / ".rw" / "locks" / "command.lock",
        )
        with lock:
            self.assertTrue(lock.held)
            self.assertTrue(lock.path.is_file())
        self.assertFalse(lock.held)
        with lock:
            self.assertTrue(lock.held)

    def test_lock_releases_when_critical_section_raises(self):
        lock = FixtureAcceptanceLock(self.workspace_root)
        with self.assertRaisesRegex(RuntimeError, "synthetic pass failure"):
            with lock:
                raise RuntimeError("synthetic pass failure")
        self.assertFalse(lock.held)
        with lock:
            self.assertTrue(lock.held)

    def test_lock_refuses_live_repository_workspace(self):
        with self.assertRaisesRegex(ValueError, "live repository"):
            FixtureAcceptanceLock(ROOT.parent)

    def test_locked_pass_cannot_be_used_after_release(self):
        writer = FixtureResultWriter(FixtureResultStore(self.store_root), writer_id="PROME")
        with writer.acceptance_pass([self.command]) as acceptance:
            self.assertEqual(
                [command["command_id"] for command in acceptance.plan.ready],
                [self.command["command_id"]],
            )
        with self.assertRaisesRegex(RuntimeError, "no longer lock-protected"):
            acceptance.accept(
                self.command,
                event_id=EVENT_1,
                recorded_at=RECORDED_AT,
            )

    def test_two_processes_cannot_both_publish_the_same_command(self):
        context = multiprocessing.get_context("fork")
        first_attempted = context.Event()
        first_entered = context.Event()
        release_first = context.Event()
        second_attempted = context.Event()
        second_entered = context.Event()
        outcomes = context.Queue()
        first = context.Process(
            target=_locked_pass_worker,
            args=(
                "first",
                str(self.store_root),
                self.command,
                EVENT_1,
                first_attempted,
                first_entered,
                release_first,
                outcomes,
            ),
        )
        second = context.Process(
            target=_locked_pass_worker,
            args=(
                "second",
                str(self.store_root),
                self.command,
                EVENT_2,
                second_attempted,
                second_entered,
                None,
                outcomes,
            ),
        )
        try:
            first.start()
            self.assertTrue(first_attempted.wait(3))
            self.assertTrue(first_entered.wait(3))
            second.start()
            self.assertTrue(second_attempted.wait(3))
            self.assertFalse(second_entered.wait(0.25))
            release_first.set()
            first.join(5)
            second.join(5)
            self.assertFalse(first.is_alive())
            self.assertFalse(second.is_alive())
            self.assertEqual(first.exitcode, 0)
            self.assertEqual(second.exitcode, 0)
            self.assertTrue(second_entered.is_set())
            records = {}
            for _ in range(2):
                label, state, error = outcomes.get(timeout=2)
                self.assertIsNone(error)
                records[label] = state
            self.assertEqual(records, {"first": "WRITTEN", "second": "COMPLETED"})
        finally:
            release_first.set()
            for process in (first, second):
                if process.is_alive():
                    process.terminate()
                process.join(1)
        inventory = FixtureResultStore(self.store_root).inventory()
        self.assertTrue(inventory.valid, inventory.findings)
        self.assertEqual(list(inventory.results), [self.command["command_id"]])
        stored = inventory.results[self.command["command_id"]]
        self.assertEqual(stored.document["event_id"], EVENT_1)

    def test_lock_custody_does_not_grant_research_authority(self):
        registry = PermissionRegistry.from_files(
            PERMISSION_FIXTURES / "actors.json",
            PERMISSION_FIXTURES / "capability-grants.json",
        )
        candidate = copy.deepcopy(self.command)
        candidate["actor_id"] = "PROME"
        candidate["payload"]["owner_actor_id"] = "PROME"
        submission_path = f"AGENTS/PROME/outbox/kernel/submissions/{candidate['command_id']}.json"
        with FixtureAcceptanceLock(self.workspace_root):
            result = authorize_command(candidate, submission_path, registry)
        self.assertIn("PERMISSION_DENIED", {finding.code for finding in result.findings})
        self.assertTrue(any("question.register" in finding.message for finding in result.findings))


if __name__ == "__main__":
    unittest.main()
