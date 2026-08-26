from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "permissions"
sys.path.insert(0, str(ROOT / "tools"))

from permissions import PermissionRegistry, authorize_command  # noqa: E402


IDS = {
    "command_q": "CMD-018f22e2-7d00-7000-8000-000000000001",
    "command_f": "CMD-018f22e2-7d00-7000-8000-000000000002",
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


def command(command_type: str = "RegisterQuestion") -> dict:
    is_question = command_type == "RegisterQuestion"
    payload = question_payload()
    if not is_question:
        payload = {
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
        "correlation_id": "fixture-permissions-001",
        "caused_by": None,
        "depends_on": [] if is_question else [IDS["command_q"]],
        "payload": payload,
        "native_refs": [native_ref("FIX-Q-001" if is_question else "FIX-F-001")],
    }


def submission_path(candidate: dict, actor_name: str = "SAM") -> str:
    return f"AGENTS/{actor_name}/outbox/kernel/submissions/{candidate['command_id']}.json"


class PermissionTests(unittest.TestCase):
    def setUp(self):
        self.registry = PermissionRegistry.from_files(
            FIXTURES / "actors.json",
            FIXTURES / "capability-grants.json",
        )
        self.assertTrue(self.registry.valid, self.registry.findings)

    def test_file_backed_registry_authorizes_owned_question_and_forecast(self):
        question = command("RegisterQuestion")
        forecast = command("SubmitForecast")
        self.assertTrue(authorize_command(question, submission_path(question), self.registry).valid)
        self.assertTrue(authorize_command(forecast, submission_path(forecast), self.registry).valid)

    def test_unknown_actor_is_denied(self):
        candidate = command()
        candidate["actor_id"] = "UNKNOWN"
        candidate["payload"]["owner_actor_id"] = "UNKNOWN"
        result = authorize_command(candidate, submission_path(candidate, "UNKNOWN"), self.registry)
        self.assertEqual({finding.code for finding in result.findings}, {"PERMISSION_DENIED"})

    def test_submission_path_owner_mismatch_is_rejected(self):
        candidate = command()
        result = authorize_command(candidate, submission_path(candidate, "RED"), self.registry)
        self.assertIn("ACTOR_PATH_MISMATCH", {finding.code for finding in result.findings})

    def test_submission_filename_must_match_command_id(self):
        candidate = command()
        wrong_path = "AGENTS/SAM/outbox/kernel/submissions/CMD-018f22e2-7d00-7000-8000-000000000099.json"
        result = authorize_command(candidate, wrong_path, self.registry)
        self.assertIn("ACTOR_PATH_MISMATCH", {finding.code for finding in result.findings})

    def test_inactive_actor_is_denied_at_half_open_boundary(self):
        candidate = command()
        candidate["actor_id"] = "RETIRED_FIXTURE"
        candidate["payload"]["owner_actor_id"] = "RETIRED_FIXTURE"
        result = authorize_command(
            candidate,
            submission_path(candidate, "RETIRED_FIXTURE"),
            self.registry,
        )
        self.assertIn("PERMISSION_DENIED", {finding.code for finding in result.findings})

    def test_command_accept_custody_grants_no_research_capability(self):
        candidate = command()
        candidate["actor_id"] = "PROME"
        candidate["payload"]["owner_actor_id"] = "PROME"
        result = authorize_command(candidate, submission_path(candidate, "PROME"), self.registry)
        self.assertIn("PERMISSION_DENIED", {finding.code for finding in result.findings})
        self.assertTrue(any("question.register" in finding.message for finding in result.findings))

    def test_payload_owner_must_match_command_actor(self):
        candidate = command()
        candidate["payload"]["owner_actor_id"] = "RED"
        result = authorize_command(candidate, submission_path(candidate), self.registry)
        self.assertIn("PERMISSION_DENIED", {finding.code for finding in result.findings})

    def test_referenced_actor_must_be_registered(self):
        candidate = command()
        candidate["payload"]["independent_verifier_actor_id"] = "UNKNOWN"
        result = authorize_command(candidate, submission_path(candidate), self.registry)
        self.assertIn("PERMISSION_DENIED", {finding.code for finding in result.findings})
        self.assertTrue(any(finding.location.endswith("independent_verifier_actor_id") for finding in result.findings))

    def test_malformed_actor_reference_fails_closed(self):
        candidate = command()
        candidate["payload"]["independent_verifier_actor_id"] = []
        result = authorize_command(candidate, submission_path(candidate), self.registry)
        self.assertIn("COMMAND_SCHEMA_INVALID", {finding.code for finding in result.findings})

    def test_invalid_registry_fails_closed(self):
        actors = json.loads((FIXTURES / "actors.json").read_text(encoding="utf-8"))
        grants = json.loads((FIXTURES / "capability-grants.json").read_text(encoding="utf-8"))
        actors["actors"].append(copy.deepcopy(actors["actors"][0]))
        registry = PermissionRegistry.from_documents(actors, grants)
        self.assertFalse(registry.valid)
        candidate = command()
        result = authorize_command(candidate, submission_path(candidate), registry)
        self.assertEqual({finding.code for finding in result.findings}, {"PERMISSION_DENIED"})

    def test_unknown_capability_invalidates_policy(self):
        actors = json.loads((FIXTURES / "actors.json").read_text(encoding="utf-8"))
        grants = json.loads((FIXTURES / "capability-grants.json").read_text(encoding="utf-8"))
        grants["grants"][0]["capabilities"].append("research.decide")
        registry = PermissionRegistry.from_documents(actors, grants)
        self.assertFalse(registry.valid)
        self.assertIn("CAPABILITY_REGISTRY_INVALID", {finding.code for finding in registry.findings})


if __name__ == "__main__":
    unittest.main()
