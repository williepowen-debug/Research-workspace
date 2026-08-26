from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "planning"
sys.path.insert(0, str(ROOT / "tools"))

from planner import plan_commands  # noqa: E402


def typed_id(prefix: str, number: int) -> str:
    return f"{prefix}-018f22e2-7d00-7000-8000-{number:012x}"


def native_ref(locator: str) -> dict:
    return {
        "repository": "williepowen-debug/Research-workspace",
        "source_commit": "a" * 40,
        "path": "KERNEL/tests/fixtures/native/predictions.tsv",
        "locator_type": "TSV_RECORD_ID",
        "locator": locator,
        "raw_record_sha256": "b" * 64,
    }


def question_command(
    number: int,
    *,
    submitted_at: str = "2026-08-25T12:05:00.000000Z",
    depends_on: list[str] | None = None,
) -> dict:
    command_id = typed_id("CMD", number)
    question_id = typed_id("Q", 1000 + number)
    return {
        "schema_version": "kernel.schema.1",
        "policy_version": "kernel.policy.1",
        "command_id": command_id,
        "command_type": "RegisterQuestion",
        "actor_id": "SAM",
        "submitted_at": submitted_at,
        "expected_version": 0,
        "target_stream_id": f"QS-{question_id}",
        "correlation_id": "fixture-planning",
        "caused_by": None,
        "depends_on": list(depends_on or []),
        "payload": {
            "question_id": question_id,
            "owner_actor_id": "SAM",
            "claim": f"Synthetic question {number} resolves YES.",
            "forecast_family": "BINARY_PROBABILITY",
            "opens_at": "2026-08-25T12:00:00.000000Z",
            "closes_at": "2026-09-18T20:00:00.000000Z",
            "resolver_anchor_type": "FIXED_DEADLINE",
            "resolution_condition": "Published fixture value is at or above 100.",
            "resolution_rule": "YES at or above 100; otherwise NO.",
            "resolution_sources": ["fixture://registered-source"],
            "fallback_resolution_source": None,
            "ambiguity_rule": "AMBIGUOUS when no replacement source exists.",
            "annulment_rules": ["SOURCE_PERMANENTLY_UNAVAILABLE"],
            "resolver_actor_id": "SAM",
            "independent_verifier_actor_id": "RED",
            "negative_search_procedure": None,
        },
        "native_refs": [native_ref(f"FIX-Q-{number:03d}")],
    }


def result(command_id: str, command_result: str, reason_code: str | None = None) -> dict:
    return {
        "command_id": command_id,
        "command_result": command_result,
        "reason_code": reason_code,
    }


def plan_signature(plan) -> tuple:
    return (
        tuple(plan.completed),
        tuple(command["command_id"] for command in plan.ready),
        tuple(plan.waiting.items()),
        tuple(plan.rejections.items()),
        tuple((finding.code, finding.message, finding.location) for finding in plan.findings),
    )


class DependencyPlannerTests(unittest.TestCase):
    def test_file_backed_forecast_follows_question_despite_input_order(self):
        fixture = json.loads((FIXTURES / "question_forecast_batch.json").read_text(encoding="utf-8"))
        plan = plan_commands(fixture["submissions"], fixture["durable_results"])
        self.assertTrue(plan.valid, plan.findings)
        self.assertEqual(
            [command["command_type"] for command in plan.ready],
            ["RegisterQuestion", "SubmitForecast"],
        )
        self.assertFalse(plan.waiting)
        self.assertFalse(plan.rejections)

    def test_independent_commands_use_timestamp_then_command_id(self):
        late = question_command(12, submitted_at="2026-08-25T12:06:00.000000Z")
        early_high_id = question_command(11)
        early_low_id = question_command(10)
        plan = plan_commands([late, early_high_id, early_low_id])
        self.assertEqual(
            [command["command_id"] for command in plan.ready],
            [early_low_id["command_id"], early_high_id["command_id"], late["command_id"]],
        )

    def test_accepted_dependency_is_satisfied_and_completed_command_is_separate(self):
        question = question_command(20)
        dependent = question_command(21, depends_on=[question["command_id"]])
        plan = plan_commands(
            [dependent, question],
            [result(question["command_id"], "ACCEPTED")],
        )
        self.assertEqual(tuple(plan.completed), (question["command_id"],))
        self.assertEqual([command["command_id"] for command in plan.ready], [dependent["command_id"]])

    def test_missing_dependency_remains_visible_and_unprocessed(self):
        missing = typed_id("CMD", 999)
        candidate = question_command(30, depends_on=[missing])
        plan = plan_commands([candidate])
        self.assertFalse(plan.ready)
        self.assertEqual(plan.waiting, {candidate["command_id"]: (missing,)})
        self.assertFalse(plan.rejections)

    def test_missing_root_propagates_through_pending_chain(self):
        missing = typed_id("CMD", 998)
        first = question_command(31, depends_on=[missing])
        second = question_command(32, depends_on=[first["command_id"]])
        plan = plan_commands([second, first])
        self.assertEqual(plan.waiting[first["command_id"]], (missing,))
        self.assertEqual(plan.waiting[second["command_id"]], (missing,))

    def test_rejected_durable_dependency_plans_dependency_rejection(self):
        dependency_id = typed_id("CMD", 40)
        candidate = question_command(41, depends_on=[dependency_id])
        plan = plan_commands(
            [candidate],
            [result(dependency_id, "REJECTED", "PERMISSION_DENIED")],
        )
        self.assertEqual(plan.rejections, {candidate["command_id"]: "DEPENDENCY_REJECTED"})
        self.assertFalse(plan.ready)

    def test_cycle_members_and_downstream_command_have_distinct_reasons(self):
        first_id = typed_id("CMD", 50)
        second_id = typed_id("CMD", 51)
        first = question_command(50, depends_on=[second_id])
        second = question_command(51, depends_on=[first_id])
        downstream = question_command(52, depends_on=[first_id])
        plan = plan_commands([downstream, second, first])
        self.assertEqual(plan.rejections[first_id], "DEPENDENCY_CYCLE")
        self.assertEqual(plan.rejections[second_id], "DEPENDENCY_CYCLE")
        self.assertEqual(plan.rejections[downstream["command_id"]], "DEPENDENCY_REJECTED")
        self.assertFalse(plan.ready)
        self.assertFalse(plan.waiting)

    def test_plan_is_independent_of_submission_and_result_input_order(self):
        accepted_id = typed_id("CMD", 60)
        first = question_command(61)
        second = question_command(62, depends_on=[first["command_id"]])
        third = question_command(63, depends_on=[accepted_id])
        results = [result(accepted_id, "ACCEPTED")]
        forward = plan_commands([first, second, third], results)
        reverse = plan_commands([third, second, first], list(reversed(results)))
        self.assertEqual(plan_signature(forward), plan_signature(reverse))

    def test_duplicate_submission_is_a_blocking_inventory_finding(self):
        candidate = question_command(70)
        plan = plan_commands([candidate, copy.deepcopy(candidate)])
        self.assertIn("DUPLICATE_COMMAND", {finding.code for finding in plan.findings})
        self.assertFalse(plan.ready)

    def test_duplicate_durable_result_is_a_blocking_inventory_finding(self):
        dependency_id = typed_id("CMD", 80)
        candidate = question_command(81, depends_on=[dependency_id])
        duplicate_results = [
            result(dependency_id, "ACCEPTED"),
            result(dependency_id, "REJECTED", "PERMISSION_DENIED"),
        ]
        plan = plan_commands([candidate], duplicate_results)
        self.assertIn("AUDIT_DUPLICATE_RESULT", {finding.code for finding in plan.findings})
        self.assertEqual(plan.waiting[candidate["command_id"]], (dependency_id,))

    def test_duplicate_dependency_is_schema_invalid(self):
        dependency_id = typed_id("CMD", 90)
        candidate = question_command(91, depends_on=[dependency_id, dependency_id])
        plan = plan_commands([candidate])
        self.assertIn("COMMAND_SCHEMA_INVALID", {finding.code for finding in plan.findings})
        self.assertFalse(plan.ready)

    def test_long_missing_chain_does_not_depend_on_python_recursion(self):
        missing = typed_id("CMD", 5000)
        commands = []
        dependency = missing
        for number in range(1000, 2200):
            candidate = question_command(number, depends_on=[dependency])
            commands.append(candidate)
            dependency = candidate["command_id"]
        plan = plan_commands(list(reversed(commands)))
        self.assertTrue(plan.valid, plan.findings)
        self.assertEqual(len(plan.waiting), 1200)
        self.assertEqual(plan.waiting[commands[-1]["command_id"]], (missing,))


if __name__ == "__main__":
    unittest.main()
