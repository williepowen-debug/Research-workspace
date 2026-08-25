from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from core import replay, sha256_hex, validate_command, validate_event  # noqa: E402


IDS = {
    "command_q": "CMD-018f22e2-7d00-7000-8000-000000000001",
    "command_f": "CMD-018f22e2-7d00-7000-8000-000000000002",
    "event_q": "EVT-018f22e2-7d00-7000-8000-000000000003",
    "event_f": "EVT-018f22e2-7d00-7000-8000-000000000004",
    "question": "Q-018f22e2-7d00-7000-8000-000000000005",
    "forecast": "F-018f22e2-7d00-7000-8000-000000000006",
}


def native_ref(locator: str) -> dict:
    return {
        "repository": "williepowen-debug/Research-workspace",
        "source_commit": "a" * 40,
        "path": "KERNEL/tests/fixtures/native/predictions.tsv",
        "locator_type": "TSV_RECORD_ID",
        "locator": locator,
        "raw_record_sha256": "b" * 64,
    }


def question_payload() -> dict:
    return {
        "question_id": IDS["question"],
        "owner_actor_id": "SAM",
        "claim": "The registered event occurs by the close time.",
        "forecast_family": "BINARY_PROBABILITY",
        "opens_at": "2026-08-25T12:00:00.000000Z",
        "closes_at": "2026-09-18T20:00:00.000000Z",
        "resolver_anchor_type": "FIXED_DEADLINE",
        "resolution_condition": "Published fixture value is at or above 100.",
        "resolution_rule": "YES when the fixture value is at or above 100; otherwise NO.",
        "resolution_sources": ["fixture://registered-source"],
        "fallback_resolution_source": None,
        "ambiguity_rule": "AMBIGUOUS when the source is withdrawn without replacement.",
        "annulment_rules": ["SOURCE_PERMANENTLY_UNAVAILABLE"],
        "resolver_actor_id": "SAM",
        "independent_verifier_actor_id": "RED",
        "negative_search_procedure": None,
    }


def forecast_payload() -> dict:
    return {
        "forecast_id": IDS["forecast"],
        "question_id": IDS["question"],
        "forecaster_actor_id": "SAM",
        "forecast_version": 1,
        "information_as_of": "2026-08-25T12:00:00.000000Z",
        "probability": 0.65,
        "rationale_ref": "fixture://rationale",
        "evidence_refs": ["fixture://evidence"],
        "intervention_stage": "INITIAL",
        "decision_consequence": None,
    }


def command(command_type: str) -> dict:
    is_question = command_type == "RegisterQuestion"
    payload = question_payload() if is_question else forecast_payload()
    command_id = IDS["command_q"] if is_question else IDS["command_f"]
    return {
        "schema_version": "kernel.schema.1",
        "policy_version": "kernel.policy.1",
        "command_id": command_id,
        "command_type": command_type,
        "actor_id": "SAM",
        "submitted_at": "2026-08-25T12:05:00.000000Z",
        "expected_version": 0,
        "target_stream_id": f"QS-{IDS['question']}" if is_question else f"FS-{IDS['forecast']}",
        "correlation_id": "fixture-binary-001",
        "caused_by": None,
        "depends_on": [] if is_question else [IDS["command_q"]],
        "payload": payload,
        "native_refs": [native_ref("FIX-Q-001" if is_question else "FIX-F-001")],
    }


def event(event_type: str) -> dict:
    is_question = event_type == "QuestionRegistered"
    source_command = command("RegisterQuestion" if is_question else "SubmitForecast")
    return {
        "schema_version": "kernel.schema.1",
        "policy_version": "kernel.policy.1",
        "writer_version": "kernel.writer.1",
        "event_id": IDS["event_q"] if is_question else IDS["event_f"],
        "event_type": event_type,
        "command_id": source_command["command_id"],
        "command_hash": sha256_hex(source_command),
        "command_result": "ACCEPTED",
        "stream_id": source_command["target_stream_id"],
        "stream_version": 1,
        "previous_event_id": None,
        "object_id": IDS["question"] if is_question else IDS["forecast"],
        "object_type": "QUESTION" if is_question else "FORECAST",
        "actor_id": "SAM",
        "writer_id": "PROME",
        "submitted_at": source_command["submitted_at"],
        "recorded_at": "2026-08-25T12:06:00.000000Z",
        "effective_at": None,
        "correlation_id": "fixture-binary-001",
        "caused_by": None if is_question else IDS["event_q"],
        "authority_mode": "SHADOW",
        "native_refs": source_command["native_refs"],
        "evidence_refs": [],
        "payload": source_command["payload"],
    }


class ContractTests(unittest.TestCase):
    def test_valid_question_and_forecast_commands(self):
        self.assertTrue(validate_command(command("RegisterQuestion")).valid)
        self.assertTrue(validate_command(command("SubmitForecast")).valid)

    def test_unknown_command_field_fails_closed(self):
        candidate = command("RegisterQuestion")
        candidate["surprise"] = True
        result = validate_command(candidate)
        self.assertFalse(result.valid)
        self.assertIn("UNKNOWN_FIELD", {finding.code for finding in result.findings})

    def test_disabled_family_is_rejected(self):
        candidate = command("RegisterQuestion")
        candidate["payload"]["forecast_family"] = "THRESHOLD_CROSSING"
        self.assertIn("FAMILY_NOT_ENABLED", {finding.code for finding in validate_command(candidate).findings})

    def test_probability_out_of_range_is_rejected(self):
        candidate = command("SubmitForecast")
        candidate["payload"]["probability"] = 1.01
        self.assertIn("PROBABILITY_INVALID", {finding.code for finding in validate_command(candidate).findings})

    def test_non_finite_probability_is_rejected(self):
        candidate = command("SubmitForecast")
        candidate["payload"]["probability"] = float("nan")
        self.assertIn("PROBABILITY_INVALID", {finding.code for finding in validate_command(candidate).findings})

    def test_future_information_cutoff_is_rejected(self):
        candidate = command("SubmitForecast")
        candidate["payload"]["information_as_of"] = "2026-08-25T13:00:00.000000Z"
        self.assertIn("INVALID_INFORMATION_CUTOFF", {finding.code for finding in validate_command(candidate).findings})

    def test_invalid_native_path_is_rejected(self):
        candidate = command("RegisterQuestion")
        candidate["native_refs"][0]["path"] = "../escape.tsv"
        self.assertIn("NATIVE_PATH_INVALID", {finding.code for finding in validate_command(candidate).findings})

    def test_valid_fixture_events_replay(self):
        events = [event("ForecastSubmitted"), event("QuestionRegistered")]
        result = replay(events)
        self.assertTrue(result.valid, result.findings)
        self.assertEqual(set(result.current), {f"QS-{IDS['question']}", f"FS-{IDS['forecast']}"})

    def test_orphan_forecast_is_an_exception(self):
        forecast = event("ForecastSubmitted")
        result = replay([forecast])
        self.assertIn("ORPHAN_FORECAST", {finding.code for finding in result.findings})
        self.assertNotIn(forecast["stream_id"], result.current)

    def test_competing_children_quarantine_stream(self):
        first = event("QuestionRegistered")
        child_a = copy.deepcopy(first)
        child_a["event_id"] = "EVT-018f22e2-7d00-7000-8000-000000000007"
        child_a["stream_version"] = 2
        child_a["previous_event_id"] = first["event_id"]
        child_b = copy.deepcopy(child_a)
        child_b["event_id"] = "EVT-018f22e2-7d00-7000-8000-000000000008"
        result = replay([first, child_a, child_b])
        self.assertIn(first["stream_id"], result.conflicts)
        self.assertNotIn(first["stream_id"], result.current)


if __name__ == "__main__":
    unittest.main()
