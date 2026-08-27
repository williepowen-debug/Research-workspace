from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PERMISSION_FIXTURES = ROOT / "tests" / "fixtures" / "permissions"
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from acceptance import AcceptanceCheck, CLAIMS, FixtureAcceptanceRunner, format_acceptance_run  # noqa: E402
from core import Finding, canonical_bytes  # noqa: E402
from custody import load_custody, run_with_custody  # noqa: E402
from permissions import PermissionRegistry  # noqa: E402
from test_native import SyntheticGitRepository, ref, tsv_line  # noqa: E402
from test_permissions import command, submission_path  # noqa: E402
from writer import FixtureResultStore, FixtureResultWriter  # noqa: E402


RECORDED_AT = "2026-08-26T12:00:00.000000Z"
EVENT_IDS = {
    "CMD-018f22e2-7d00-7000-8000-000000000001": "EVT-018f22e2-7d00-7000-8000-000000000301",
    "CMD-018f22e2-7d00-7000-8000-000000000002": "EVT-018f22e2-7d00-7000-8000-000000000302",
}


class IntegratedAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.repo = SyntheticGitRepository(self)
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.store = FixtureResultStore(Path(self.temporary.name) / "KERNEL")
        self.registry = PermissionRegistry.from_files(
            PERMISSION_FIXTURES / "actors.json",
            PERMISSION_FIXTURES / "capability-grants.json",
        )
        self.question = command("RegisterQuestion")
        self.forecast = command("SubmitForecast")
        companion = json.loads(self.repo.blob("native/companion.json"))
        selected_question = canonical_bytes(companion["questions"]["FIX-Q-001"])
        self.question["native_refs"] = [ref(
            self.repo.commit,
            "native/companion.json",
            "JSON_POINTER",
            "/questions/FIX-Q-001",
            selected_question,
        )]
        selected_forecast = tsv_line(self.repo.blob("native/predictions.tsv"), b"FIX-F-001")
        self.forecast["native_refs"] = [ref(
            self.repo.commit,
            "native/predictions.tsv",
            "TSV_RECORD_ID",
            "record_id=FIX-F-001",
            selected_forecast,
        )]

    def runner(self, *, hooks=()) -> FixtureAcceptanceRunner:
        return FixtureAcceptanceRunner(
            self.store,
            writer_id="PROME",
            registry=self.registry,
            git=self.repo.git,
            event_id_for=lambda candidate: EVENT_IDS[candidate["command_id"]],
            recorded_at_for=lambda _candidate: RECORDED_AT,
            required_hooks=hooks,
        )

    def paths(self, *commands: dict) -> dict[str, str]:
        return {candidate["command_id"]: submission_path(candidate) for candidate in commands}

    def custody_policy(self):
        return {
            "schema_version": "kernel.custody.1",
            "policy_version": "kernel.policy.1",
            "primary_writer_id": "PROME",
            "substitutes": [
                {"writer_id": "RED", "command_accept_default": False, "registered_by": "WILL"},
            ],
        }

    def custody_activation(self):
        return {
            "schema_version": "kernel.custody.1",
            "policy_version": "kernel.policy.1",
            "activation_id": "CUSTODY-SYNTHETIC-001",
            "authorized_by": "WILL",
            "substitute_writer_id": "RED",
            "window_start": "2026-08-26T11:00:00.000000Z",
            "window_end": "2026-08-26T13:00:00.000000Z",
            "command_ids": [self.question["command_id"]],
            "revoked_at": None,
        }

    def test_custody_preflight_blocks_suspended_primary_before_any_write(self):
        loaded = load_custody(self.custody_policy(), self.custody_activation())
        run = run_with_custody(
            self.runner(),
            loaded,
            writer_id="PROME",
            recorded_at=RECORDED_AT,
            submissions=[self.question],
            submission_paths=self.paths(self.question),
        )
        self.assertEqual(run.status, "EXCEPTION")
        self.assertFalse(run.outcomes)
        self.assertFalse(list(self.store.root.glob("**/*.json")))
        self.assertEqual(run.checks[0].name, "custody")

    def test_activated_substitute_runs_identical_acceptance_binary(self):
        loaded = load_custody(self.custody_policy(), self.custody_activation())
        runner = FixtureAcceptanceRunner(
            self.store,
            writer_id="RED",
            registry=self.registry,
            git=self.repo.git,
            event_id_for=lambda candidate: EVENT_IDS[candidate["command_id"]],
            recorded_at_for=lambda _candidate: RECORDED_AT,
        )
        run = run_with_custody(
            runner,
            loaded,
            writer_id="RED",
            recorded_at=RECORDED_AT,
            submissions=[self.question],
            submission_paths=self.paths(self.question),
        )
        self.assertEqual(run.status, "PASS")
        self.assertEqual(run.outcomes[self.question["command_id"]].document["writer_id"], "RED")
        self.assertEqual(run.checks[0].status, "PASS")

    def test_valid_reverse_ordered_batch_runs_complete_path_in_dependency_order(self):
        run = self.runner().run(
            [self.forecast, self.question],
            self.paths(self.question, self.forecast),
        )
        self.assertEqual(run.status, "PASS")
        self.assertEqual(list(run.outcomes), [self.question["command_id"], self.forecast["command_id"]])
        self.assertTrue(all(outcome.document["command_result"] == "ACCEPTED" for outcome in run.outcomes.values()))
        inventory = self.store.inventory()
        self.assertTrue(inventory.valid, inventory.findings)
        self.assertEqual(len(inventory.results), 2)
        self.assertEqual(run.waiting, {})

    def test_invalid_native_reference_becomes_one_durable_rejection(self):
        candidate = copy.deepcopy(self.question)
        candidate["native_refs"][0]["source_commit"] = "0" * 40
        run = self.runner().run([candidate], self.paths(candidate))
        outcome = run.outcomes[candidate["command_id"]]
        self.assertEqual(run.status, "EXCEPTION")
        self.assertEqual(outcome.document["command_result"], "REJECTED")
        self.assertEqual(outcome.document["reason_code"], "NATIVE_RECORD_MISSING")
        self.assertFalse(list(self.store.root.glob("shadow/events/**/*.json")))
        self.assertEqual(len(list(self.store.root.glob("audit/commands/**/*.json"))), 1)

    def test_failed_native_dependency_durably_rejects_its_dependent(self):
        invalid_question = copy.deepcopy(self.question)
        invalid_question["native_refs"][0]["source_commit"] = "0" * 40
        run = self.runner().run(
            [self.forecast, invalid_question],
            self.paths(invalid_question, self.forecast),
        )
        self.assertEqual(
            run.outcomes[invalid_question["command_id"]].document["reason_code"],
            "NATIVE_RECORD_MISSING",
        )
        self.assertEqual(
            run.outcomes[self.forecast["command_id"]].document["reason_code"],
            "DEPENDENCY_REJECTED",
        )
        self.assertEqual(len(list(self.store.root.glob("audit/commands/**/*.json"))), 2)
        self.assertFalse(list(self.store.root.glob("shadow/events/**/*.json")))

    def test_unauthorized_actor_cannot_reach_an_accepted_event(self):
        candidate = copy.deepcopy(self.question)
        candidate["actor_id"] = "UNKNOWN"
        candidate["payload"]["owner_actor_id"] = "UNKNOWN"
        path = f"AGENTS/UNKNOWN/outbox/kernel/submissions/{candidate['command_id']}.json"
        run = self.runner().run([candidate], {candidate["command_id"]: path})
        outcome = run.outcomes[candidate["command_id"]]
        self.assertEqual(outcome.document["reason_code"], "PERMISSION_DENIED")
        self.assertFalse(list(self.store.root.glob("shadow/events/**/*.json")))

    def test_waiting_command_is_visible_unprocessed_and_blocks_green(self):
        run = self.runner().run([self.forecast], self.paths(self.forecast))
        self.assertEqual(run.status, "UNKNOWN")
        self.assertIn(self.forecast["command_id"], run.waiting)
        self.assertNotIn(self.forecast["command_id"], run.outcomes)
        self.assertFalse(list(self.store.root.glob("**/*.json")))

    def test_required_unknown_stops_acceptance_and_aggregate_green(self):
        def unknown_check(candidate: dict) -> AcceptanceCheck:
            return AcceptanceCheck(
                "injected-proof",
                "UNKNOWN",
                f"command_id={candidate['command_id']}",
                "the injected proof completed",
                "anything outside the injected proof",
                (Finding("INJECTED_UNKNOWN", "synthetic unavailable evidence", "$check"),),
            )

        run = self.runner(hooks=(unknown_check,)).run([self.question], self.paths(self.question))
        self.assertEqual(run.status, "UNKNOWN")
        self.assertNotIn(self.question["command_id"], run.outcomes)
        self.assertFalse(list(self.store.root.glob("**/*.json")))
        report = format_acceptance_run(run)
        self.assertIn("UNKNOWN: injected-proof", report)
        self.assertIn("UNKNOWN: aggregate", report)
        self.assertIn("PASS does not prove:", report)

    def test_unknown_discloses_every_selected_command_left_unprocessed(self):
        def unknown_check(candidate: dict) -> AcceptanceCheck:
            return AcceptanceCheck(
                "injected-proof",
                "UNKNOWN",
                f"command_id={candidate['command_id']}",
                "the injected proof completed",
                "anything outside the injected proof",
                (Finding("INJECTED_UNKNOWN", "synthetic unavailable evidence", "$check"),),
            )

        run = self.runner(hooks=(unknown_check,)).run(
            [self.forecast, self.question],
            self.paths(self.question, self.forecast),
        )
        self.assertEqual(run.status, "UNKNOWN")
        self.assertEqual(set(run.waiting), {self.question["command_id"], self.forecast["command_id"]})
        report = format_acceptance_run(run)
        self.assertIn("durable_outcomes=0 waiting=2", report)
        self.assertIn(f"command_id={self.forecast['command_id']} waiting_on=REQUIRED_CHECK_UNKNOWN", report)

    def test_locked_pass_refuses_a_command_that_is_not_ready(self):
        writer = FixtureResultWriter(self.store, writer_id="PROME")
        with writer.acceptance_pass([self.forecast]) as acceptance:
            self.assertFalse(acceptance.plan.ready)
            with self.assertRaisesRegex(RuntimeError, "not next"):
                acceptance.accept(
                    self.forecast,
                    event_id=EVENT_IDS[self.forecast["command_id"]],
                    recorded_at=RECORDED_AT,
                )

    def test_locked_pass_enforces_dependency_order_within_ready_plan(self):
        writer = FixtureResultWriter(self.store, writer_id="PROME")
        with writer.acceptance_pass([self.forecast, self.question]) as acceptance:
            self.assertEqual(
                [candidate["command_id"] for candidate in acceptance.plan.ready],
                [self.question["command_id"], self.forecast["command_id"]],
            )
            with self.assertRaisesRegex(RuntimeError, "not next"):
                acceptance.accept(
                    self.forecast,
                    event_id=EVENT_IDS[self.forecast["command_id"]],
                    recorded_at=RECORDED_AT,
                )

    def test_integrated_retry_detects_same_id_with_different_bytes(self):
        first = self.runner().run([self.question], self.paths(self.question))
        self.assertEqual(first.status, "PASS")
        changed = copy.deepcopy(self.question)
        changed["payload"]["claim"] = "Different bytes under the same command identity."
        retry = self.runner().run([changed], self.paths(changed))
        self.assertEqual(retry.status, "EXCEPTION")
        self.assertEqual(retry.outcomes[changed["command_id"]].state, "REJECTED")
        self.assertEqual(retry.outcomes[changed["command_id"]].finding.code, "IDEMPOTENCY_KEY_REUSED")
        self.assertEqual(len(list(self.store.root.glob("shadow/events/**/*.json"))), 1)

    def test_prior_rejected_result_cannot_return_aggregate_green(self):
        candidate = copy.deepcopy(self.question)
        candidate["actor_id"] = "UNKNOWN"
        candidate["payload"]["owner_actor_id"] = "UNKNOWN"
        path = f"AGENTS/UNKNOWN/outbox/kernel/submissions/{candidate['command_id']}.json"
        first = self.runner().run([candidate], {candidate["command_id"]: path})
        retry = self.runner().run([candidate], {candidate["command_id"]: path})
        self.assertEqual(first.status, "EXCEPTION")
        self.assertEqual(retry.status, "EXCEPTION")
        self.assertEqual(retry.outcomes[candidate["command_id"]].state, "EXISTING")
        self.assertEqual(retry.outcomes[candidate["command_id"]].document["command_result"], "REJECTED")

    def test_accepted_retry_rechecks_required_perimeter_and_blocks_changed_path(self):
        first = self.runner().run([self.question], self.paths(self.question))
        self.assertEqual(first.status, "PASS")
        changed_path = f"AGENTS/RED/outbox/kernel/submissions/{self.question['command_id']}.json"
        retry = self.runner().run(
            [copy.deepcopy(self.question)],
            {self.question["command_id"]: changed_path},
        )
        self.assertEqual(retry.status, "EXCEPTION")
        self.assertEqual(retry.outcomes[self.question["command_id"]].state, "EXISTING")
        permission_checks = [check for check in retry.checks if check.name == "permissions"]
        self.assertEqual(len(permission_checks), 1)
        self.assertEqual(permission_checks[0].status, "EXCEPTION")
        self.assertTrue(any(check.name == "native-reference" for check in retry.checks))
        self.assertTrue(any(check.name == "lifecycle" for check in retry.checks))

    def test_event_identifier_collision_blocks_aggregate_green(self):
        colliding_runner = FixtureAcceptanceRunner(
            self.store,
            writer_id="PROME",
            registry=self.registry,
            git=self.repo.git,
            event_id_for=lambda _candidate: EVENT_IDS[self.question["command_id"]],
            recorded_at_for=lambda _candidate: RECORDED_AT,
        )
        run = colliding_runner.run(
            [self.forecast, self.question],
            self.paths(self.question, self.forecast),
        )
        self.assertEqual(run.status, "EXCEPTION")
        self.assertEqual(
            run.outcomes[self.forecast["command_id"]].document["reason_code"],
            "IDENTIFIER_COLLISION",
        )

    def test_fresh_forecast_against_closed_question_is_durably_rejected(self):
        opened = self.runner().run([self.question], self.paths(self.question))
        self.assertEqual(opened.status, "PASS")
        close = {
            "schema_version": "kernel.schema.1",
            "policy_version": "kernel.policy.1",
            "command_id": "CMD-018f22e2-7d00-7000-8000-000000000399",
            "command_type": "CloseQuestion",
            "actor_id": "SAM",
            "submitted_at": "2026-09-18T20:01:00.000000Z",
            "expected_version": 1,
            "target_stream_id": self.question["target_stream_id"],
            "correlation_id": "fixture-closed-question",
            "caused_by": None,
            "depends_on": [self.question["command_id"]],
            "payload": {
                "question_id": self.question["payload"]["question_id"],
                "closed_by": "SAM",
                "closed_at": "2026-09-18T20:00:00.000000Z",
            },
            "native_refs": copy.deepcopy(self.question["native_refs"]),
        }
        closed = FixtureResultWriter(self.store, writer_id="PROME").accept(
            close,
            event_id="EVT-018f22e2-7d00-7000-8000-000000000399",
            recorded_at="2026-09-18T20:02:00.000000Z",
        )
        self.assertEqual(closed.document["command_result"], "ACCEPTED")
        run = self.runner().run([self.forecast], self.paths(self.forecast))
        self.assertEqual(run.status, "EXCEPTION")
        self.assertEqual(
            run.outcomes[self.forecast["command_id"]].document["reason_code"],
            "QUESTION_NOT_OPEN",
        )

    def test_cycle_is_durably_rejected_without_manual_caller_disposition(self):
        first = copy.deepcopy(self.question)
        second = copy.deepcopy(self.forecast)
        first["depends_on"] = [second["command_id"]]
        second["depends_on"] = [first["command_id"]]
        run = self.runner().run([first, second], self.paths(first, second))
        self.assertEqual(
            {outcome.document["reason_code"] for outcome in run.outcomes.values()},
            {"DEPENDENCY_CYCLE"},
        )
        self.assertEqual(len(list(self.store.root.glob("audit/commands/**/*.json"))), 2)

    def test_report_prints_every_standard_check_claim(self):
        run = self.runner().run([self.question], self.paths(self.question))
        report = format_acceptance_run(run)
        for check_name in ("schema", "planning", "permissions", "native-reference", "lifecycle", "writer", "durability", "aggregate"):
            self.assertIn(f"perimeter: check={check_name}", report)
        self.assertIn("PASS: aggregate", report)
        self.assertEqual(set(CLAIMS), {"schema", "permissions", "native-reference", "planning", "lifecycle", "writer", "durability", "aggregate"})

    def test_cli_runs_complete_fixture_batch_and_prints_aggregate_claims(self):
        inventory_path = Path(self.temporary.name) / "inventory.json"
        event_ids_path = Path(self.temporary.name) / "event-ids.json"
        store_path = Path(self.temporary.name) / "cli-workspace" / "KERNEL"
        inventory_path.write_text(json.dumps([
            {"path": submission_path(self.forecast), "command": self.forecast},
            {"path": submission_path(self.question), "command": self.question},
        ]), encoding="utf-8")
        event_ids_path.write_text(json.dumps(EVENT_IDS), encoding="utf-8")
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "acceptance.py"),
                "--inventory", str(inventory_path),
                "--actors", str(PERMISSION_FIXTURES / "actors.json"),
                "--capabilities", str(PERMISSION_FIXTURES / "capability-grants.json"),
                "--repository", str(self.repo.path),
                "--store", str(store_path),
                "--event-ids", str(event_ids_path),
                "--recorded-at", RECORDED_AT,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("perimeter: check=aggregate explicit_submissions=2 durable_outcomes=2 waiting=0", completed.stdout)
        self.assertIn("PASS: aggregate", completed.stdout)
        self.assertIn("PASS does not prove: live readiness", completed.stdout)
        self.assertEqual(len(list(store_path.glob("shadow/events/**/*.json"))), 2)

    def test_cli_refuses_live_repository_as_native_boundary(self):
        inventory_path = Path(self.temporary.name) / "inventory-live-refusal.json"
        event_ids_path = Path(self.temporary.name) / "event-ids-live-refusal.json"
        inventory_path.write_text(json.dumps([
            {"path": submission_path(self.question), "command": self.question},
        ]), encoding="utf-8")
        event_ids_path.write_text(json.dumps(EVENT_IDS), encoding="utf-8")
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "acceptance.py"),
                "--inventory", str(inventory_path),
                "--actors", str(PERMISSION_FIXTURES / "actors.json"),
                "--capabilities", str(PERMISSION_FIXTURES / "capability-grants.json"),
                "--repository", str(ROOT.parent),
                "--store", str(Path(self.temporary.name) / "refused" / "KERNEL"),
                "--event-ids", str(event_ids_path),
                "--recorded-at", RECORDED_AT,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertIn("EXCEPTION: aggregate", completed.stdout)
        self.assertIn("refuses the live repository boundary", completed.stdout)


if __name__ == "__main__":
    unittest.main()
