from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLANNING_FIXTURE = ROOT / "tests" / "fixtures" / "planning" / "question_forecast_batch.json"
sys.path.insert(0, str(ROOT / "tools"))

from core import canonical_bytes, replay, validate_event, validate_receipt  # noqa: E402
from planner import plan_commands  # noqa: E402
from writer import (  # noqa: E402
    FixtureResultStore,
    FixtureResultWriter,
    build_accepted_event,
    build_rejected_receipt,
)


RECORDED_AT = "2026-08-25T12:06:00.000000Z"
EVENT_Q = "EVT-018f22e2-7d00-7000-8000-000000000101"
EVENT_F = "EVT-018f22e2-7d00-7000-8000-000000000102"


def fixture_commands() -> tuple[dict, dict]:
    fixture = json.loads(PLANNING_FIXTURE.read_text(encoding="utf-8"))
    by_type = {command["command_type"]: command for command in fixture["submissions"]}
    return by_type["RegisterQuestion"], by_type["SubmitForecast"]


class FixtureWriterTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "KERNEL"
        self.store = FixtureResultStore(self.root)
        self.writer = FixtureResultWriter(self.store, writer_id="PROME")
        self.question, self.forecast = fixture_commands()

    def tearDown(self):
        self.temporary.cleanup()

    def test_valid_command_writes_canonical_accepted_event(self):
        outcome = self.writer.accept(
            self.question,
            event_id=EVENT_Q,
            recorded_at=RECORDED_AT,
        )
        self.assertEqual(outcome.state, "WRITTEN")
        self.assertIsNotNone(outcome.document)
        self.assertTrue(validate_event(outcome.document).valid)
        expected = self.root / "shadow" / "events" / "2026" / "08" / f"{EVENT_Q}.json"
        self.assertEqual(outcome.path, expected)
        self.assertEqual(expected.read_bytes(), canonical_bytes(outcome.document) + b"\n")

    def test_invalid_command_is_durably_rejected_without_event(self):
        candidate = copy.deepcopy(self.forecast)
        candidate["payload"]["probability"] = 1.01
        outcome = self.writer.accept(
            candidate,
            event_id=EVENT_F,
            recorded_at=RECORDED_AT,
        )
        self.assertEqual(outcome.state, "WRITTEN")
        self.assertEqual(outcome.document["command_result"], "REJECTED")
        self.assertEqual(outcome.document["reason_code"], "COMMAND_SCHEMA_INVALID")
        self.assertTrue(validate_receipt(outcome.document).valid)
        self.assertFalse(list(self.root.glob("shadow/events/**/*.json")))
        self.assertEqual(len(list(self.root.glob("audit/commands/**/*.json"))), 1)

    def test_rejected_receipt_retains_invalid_native_reference(self):
        candidate = copy.deepcopy(self.question)
        candidate["native_refs"][0]["path"] = "../invalid.tsv"
        outcome = self.writer.reject(
            candidate,
            recorded_at=RECORDED_AT,
            reason_code="NATIVE_PATH_INVALID",
            reason_detail="native path traverses outside the repository",
        )
        self.assertEqual(outcome.state, "WRITTEN")
        self.assertEqual(outcome.document["native_refs"], candidate["native_refs"])
        self.assertTrue(validate_receipt(outcome.document).valid)

    def test_same_command_same_bytes_retry_returns_existing_result(self):
        first = self.writer.accept(self.question, event_id=EVENT_Q, recorded_at=RECORDED_AT)
        retry = self.writer.accept(
            copy.deepcopy(self.question),
            event_id="EVT-018f22e2-7d00-7000-8000-000000000199",
            recorded_at="2026-08-25T13:00:00.000000Z",
        )
        self.assertEqual(retry.state, "EXISTING")
        self.assertEqual(retry.path, first.path)
        self.assertEqual(retry.document, first.document)
        self.assertEqual(len(list(self.root.glob("**/*.json"))), 1)

    def test_same_command_id_different_bytes_never_overwrites_prior_result(self):
        first = self.writer.accept(self.question, event_id=EVENT_Q, recorded_at=RECORDED_AT)
        changed = copy.deepcopy(self.question)
        changed["payload"]["claim"] = "Different command bytes under the same identity."
        reused = self.writer.accept(
            changed,
            event_id="EVT-018f22e2-7d00-7000-8000-000000000198",
            recorded_at=RECORDED_AT,
        )
        self.assertEqual(reused.state, "REJECTED")
        self.assertEqual(reused.finding.code, "IDEMPOTENCY_KEY_REUSED")
        self.assertEqual(first.path.read_bytes(), canonical_bytes(first.document) + b"\n")
        self.assertEqual(len(list(self.root.glob("**/*.json"))), 1)

    def test_prior_accepted_result_cannot_be_replaced_by_rejection(self):
        first = self.writer.accept(self.question, event_id=EVENT_Q, recorded_at=RECORDED_AT)
        retry = self.writer.reject(
            self.question,
            recorded_at=RECORDED_AT,
            reason_code="PERMISSION_DENIED",
            reason_detail="later caller attempted a different disposition",
        )
        self.assertEqual(retry.state, "EXISTING")
        self.assertEqual(retry.document["command_result"], "ACCEPTED")
        self.assertEqual(retry.path, first.path)

    def test_same_rejected_command_retry_returns_existing_receipt(self):
        first = self.writer.reject(
            self.question,
            recorded_at=RECORDED_AT,
            reason_code="PERMISSION_DENIED",
            reason_detail="synthetic permission rejection",
        )
        retry = self.writer.reject(
            copy.deepcopy(self.question),
            recorded_at="2026-08-25T13:00:00.000000Z",
            reason_code="PERMISSION_DENIED",
            reason_detail="different retry detail is not a second result",
        )
        self.assertEqual(retry.state, "EXISTING")
        self.assertEqual(retry.path, first.path)
        self.assertEqual(retry.document, first.document)
        self.assertEqual(len(list(self.root.glob("**/*.json"))), 1)

    def test_crash_before_publish_leaves_no_result_and_retry_succeeds(self):
        fail = {"active": True}

        def before_publish(_temporary: Path, _destination: Path) -> None:
            if fail["active"]:
                fail["active"] = False
                raise RuntimeError("synthetic crash before atomic publish")

        store = FixtureResultStore(self.root, before_publish=before_publish)
        writer = FixtureResultWriter(store, writer_id="PROME")
        with self.assertRaisesRegex(RuntimeError, "synthetic crash"):
            writer.accept(self.question, event_id=EVENT_Q, recorded_at=RECORDED_AT)
        self.assertFalse(list(self.root.glob("**/*.json")))
        self.assertFalse(list(self.root.glob("**/.tmp-*")))
        retry = writer.accept(self.question, event_id=EVENT_Q, recorded_at=RECORDED_AT)
        self.assertEqual(retry.state, "WRITTEN")

    def test_duplicate_durable_results_block_lookup(self):
        event = build_accepted_event(
            self.question,
            event_id=EVENT_Q,
            recorded_at=RECORDED_AT,
            writer_id="PROME",
        )
        receipt = build_rejected_receipt(
            self.question,
            recorded_at=RECORDED_AT,
            writer_id="PROME",
            reason_code="PERMISSION_DENIED",
            reason_detail="synthetic duplicate result",
        )
        self.store.publish(event)
        self.store.publish(receipt)
        outcome = self.writer.accept(self.question, event_id=EVENT_Q, recorded_at=RECORDED_AT)
        self.assertEqual(outcome.state, "BLOCKED")
        self.assertEqual(outcome.finding.code, "AUDIT_DUPLICATE_RESULT")

    def test_event_identifier_collision_becomes_durable_rejection(self):
        self.writer.accept(self.question, event_id=EVENT_Q, recorded_at=RECORDED_AT)
        second = copy.deepcopy(self.question)
        second["command_id"] = "CMD-018f22e2-7d00-7000-8000-000000000109"
        second["payload"]["question_id"] = "Q-018f22e2-7d00-7000-8000-000000000119"
        second["target_stream_id"] = f"QS-{second['payload']['question_id']}"
        outcome = self.writer.accept(second, event_id=EVENT_Q, recorded_at=RECORDED_AT)
        self.assertEqual(outcome.state, "WRITTEN")
        self.assertEqual(outcome.document["reason_code"], "IDENTIFIER_COLLISION")
        self.assertEqual(len(list(self.root.glob("shadow/events/**/*.json"))), 1)
        self.assertEqual(len(list(self.root.glob("audit/commands/**/*.json"))), 1)

    def test_store_inventory_feeds_planner_result_summaries(self):
        self.writer.accept(self.question, event_id=EVENT_Q, recorded_at=RECORDED_AT)
        self.writer.reject(
            self.forecast,
            recorded_at=RECORDED_AT,
            reason_code="QUESTION_NOT_OPEN",
            reason_detail="synthetic lifecycle rejection",
        )
        inventory = self.store.inventory()
        self.assertTrue(inventory.valid, inventory.findings)
        plan = plan_commands(
            [self.question, self.forecast],
            inventory.planner_summaries(),
        )
        self.assertEqual(set(plan.completed), {self.question["command_id"], self.forecast["command_id"]})
        self.assertFalse(plan.ready)

    def test_planned_cycle_rejections_become_one_receipt_each(self):
        question = copy.deepcopy(self.question)
        forecast = copy.deepcopy(self.forecast)
        question["depends_on"] = [forecast["command_id"]]
        plan = plan_commands([forecast, question])
        self.assertEqual(set(plan.rejections.values()), {"DEPENDENCY_CYCLE"})
        commands = {command["command_id"]: command for command in (question, forecast)}
        for command_id, reason_code in plan.rejections.items():
            outcome = self.writer.reject(
                commands[command_id],
                recorded_at=RECORDED_AT,
                reason_code=reason_code,
                reason_detail="synthetic dependency cycle",
            )
            self.assertEqual(outcome.state, "WRITTEN")
        self.assertEqual(len(list(self.root.glob("audit/commands/**/*.json"))), 2)
        self.assertFalse(list(self.root.glob("shadow/events/**/*.json")))

    def test_rejection_does_not_change_replayed_domain_state(self):
        accepted = self.writer.accept(self.question, event_id=EVENT_Q, recorded_at=RECORDED_AT)
        before = replay([accepted.document])
        self.writer.reject(
            self.forecast,
            recorded_at=RECORDED_AT,
            reason_code="QUESTION_NOT_OPEN",
            reason_detail="synthetic rejection",
        )
        stored_events = [
            stored.document
            for stored in self.store.inventory().results.values()
            if stored.document["command_result"] == "ACCEPTED"
        ]
        after = replay(stored_events)
        self.assertEqual(before.current, after.current)

    def test_oversized_reason_detail_fails_closed_without_writing(self):
        outcome = self.writer.reject(
            self.question,
            recorded_at=RECORDED_AT,
            reason_code="PERMISSION_DENIED",
            reason_detail="x" * 513,
        )
        self.assertEqual(outcome.state, "BLOCKED")
        self.assertEqual(outcome.finding.code, "REASON_DETAIL_INVALID")
        self.assertFalse(list(self.root.glob("**/*.json")))

    def test_fixture_store_refuses_repository_targets(self):
        with self.assertRaisesRegex(ValueError, "live repository"):
            FixtureResultStore(ROOT / "fixture-output")


if __name__ == "__main__":
    unittest.main()
