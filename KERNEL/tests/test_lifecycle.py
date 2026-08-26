from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PERMISSION_FIXTURES = ROOT / "tests" / "fixtures" / "permissions"
sys.path.insert(0, str(ROOT / "tools"))

from core import replay, validate_command, validate_event  # noqa: E402
from permissions import PermissionRegistry, authorize_command  # noqa: E402
from render import render_views  # noqa: E402
from writer import FixtureResultStore, FixtureResultWriter  # noqa: E402


def typed_id(prefix: str, number: int) -> str:
    return f"{prefix}-018f22e2-7d00-7000-8000-{number:012x}"


QUESTION_ID = typed_id("Q", 501)
FORECAST_ID = typed_id("F", 502)
RESOLUTION_ID = typed_id("R", 503)
SECOND_RESOLUTION_ID = typed_id("R", 504)


def native_ref(locator: str) -> dict:
    return {
        "repository": "williepowen-debug/Research-workspace",
        "source_commit": "a" * 40,
        "path": "KERNEL/tests/fixtures/native/predictions.tsv",
        "locator_type": "TSV_RECORD_ID",
        "locator": locator,
        "raw_record_sha256": "b" * 64,
    }


def envelope(
    command_type: str,
    number: int,
    actor_id: str,
    expected_version: int,
    target_stream_id: str,
    payload: dict,
    *,
    submitted_at: str,
    depends_on: list[str] | None = None,
) -> dict:
    return {
        "schema_version": "kernel.schema.1",
        "policy_version": "kernel.policy.1",
        "command_id": typed_id("CMD", number),
        "command_type": command_type,
        "actor_id": actor_id,
        "submitted_at": submitted_at,
        "expected_version": expected_version,
        "target_stream_id": target_stream_id,
        "correlation_id": "fixture-lifecycle-001",
        "caused_by": None,
        "depends_on": depends_on or [],
        "payload": payload,
        "native_refs": [native_ref(f"FIX-LIFE-{number}")],
    }


def question_command(number: int = 501) -> dict:
    return envelope(
        "RegisterQuestion",
        number,
        "SAM",
        0,
        f"QS-{QUESTION_ID}",
        {
            "question_id": QUESTION_ID,
            "owner_actor_id": "SAM",
            "claim": "The synthetic registered event occurs by the close time.",
            "forecast_family": "BINARY_PROBABILITY",
            "opens_at": "2026-08-25T12:00:00.000000Z",
            "closes_at": "2026-09-18T20:00:00.000000Z",
            "resolver_anchor_type": "FIXED_DEADLINE",
            "resolution_condition": "Published fixture value is at or above 100.",
            "resolution_rule": "YES at or above 100; otherwise NO.",
            "resolution_sources": ["fixture://registered-source"],
            "fallback_resolution_source": None,
            "ambiguity_rule": "AMBIGUOUS when the source is withdrawn.",
            "annulment_rules": ["SOURCE_PERMANENTLY_UNAVAILABLE"],
            "resolver_actor_id": "SAM",
            "independent_verifier_actor_id": "RED",
            "negative_search_procedure": None,
        },
        submitted_at="2026-08-25T12:05:00.000000Z",
    )


def forecast_command(number: int = 502, *, version: int = 1, expected_version: int = 0) -> dict:
    command_type = "SubmitForecast" if version == 1 else "AmendForecast"
    return envelope(
        command_type,
        number,
        "SAM",
        expected_version,
        f"FS-{FORECAST_ID}",
        {
            "forecast_id": FORECAST_ID,
            "question_id": QUESTION_ID,
            "forecaster_actor_id": "SAM",
            "forecast_version": version,
            "information_as_of": f"2026-08-{24 + version:02d}T12:00:00.000000Z",
            "probability": 0.65 if version == 1 else 0.72,
            "rationale_ref": f"fixture://rationale/v{version}",
            "evidence_refs": [f"fixture://evidence/v{version}"],
            "intervention_stage": "INITIAL" if version == 1 else "POST_CHALLENGE",
            "decision_consequence": None,
        },
        submitted_at=f"2026-08-{24 + version:02d}T12:05:00.000000Z",
        depends_on=[typed_id("CMD", 501)] if version == 1 else [typed_id("CMD", 502)],
    )


def close_command(number: int = 504, *, expected_version: int = 1) -> dict:
    return envelope(
        "CloseQuestion",
        number,
        "SAM",
        expected_version,
        f"QS-{QUESTION_ID}",
        {
            "question_id": QUESTION_ID,
            "closed_by": "SAM",
            "closed_at": "2026-09-18T20:00:00.000000Z",
        },
        submitted_at="2026-09-18T20:01:00.000000Z",
        depends_on=[typed_id("CMD", 501)],
    )


def propose_command(
    number: int = 505,
    *,
    expected_version: int = 2,
    resolution_id: str = RESOLUTION_ID,
) -> dict:
    return envelope(
        "ProposeResolution",
        number,
        "SAM",
        expected_version,
        f"QS-{QUESTION_ID}",
        {
            "resolution_id": resolution_id,
            "question_id": QUESTION_ID,
            "outcome_value": "YES",
            "proposed_by": "SAM",
            "resolution_evidence_refs": ["fixture://resolution-evidence"],
            "negative_search_attempt": None,
            "annulment_reason": None,
        },
        submitted_at="2026-09-18T21:00:00.000000Z",
        depends_on=[typed_id("CMD", 504)],
    )


def verify_command(number: int = 506, *, expected_version: int = 3, actor_id: str = "RED") -> dict:
    return envelope(
        "VerifyResolution",
        number,
        actor_id,
        expected_version,
        f"QS-{QUESTION_ID}",
        {
            "resolution_id": RESOLUTION_ID,
            "question_id": QUESTION_ID,
            "verified_outcome_value": "YES",
            "verified_by": actor_id,
            "verification_evidence_refs": ["fixture://verification-evidence"],
            "disposition": "VERIFY",
        },
        submitted_at="2026-09-18T22:00:00.000000Z",
        depends_on=[typed_id("CMD", 505)],
    )


def dispute_command(number: int = 507, *, expected_version: int = 3) -> dict:
    return envelope(
        "DisputeResolution",
        number,
        "RED",
        expected_version,
        f"QS-{QUESTION_ID}",
        {
            "resolution_id": RESOLUTION_ID,
            "question_id": QUESTION_ID,
            "disputed_by": "RED",
            "dispute_evidence_refs": ["fixture://dispute-evidence"],
        },
        submitted_at="2026-09-18T22:00:00.000000Z",
        depends_on=[typed_id("CMD", 505)],
    )


def correct_command(number: int = 508, *, expected_version: int = 4) -> dict:
    return envelope(
        "CorrectResolution",
        number,
        "WILL",
        expected_version,
        f"QS-{QUESTION_ID}",
        {
            "resolution_id": RESOLUTION_ID,
            "question_id": QUESTION_ID,
            "corrected_outcome_value": "NO",
            "corrected_by": "WILL",
            "correction_evidence_refs": ["fixture://correction-evidence"],
            "will_authorization_ref": "fixture://will-authorization/001",
        },
        submitted_at="2026-09-19T12:00:00.000000Z",
        depends_on=[typed_id("CMD", 506)],
    )


def withdraw_command(number: int = 509, *, expected_version: int = 1) -> dict:
    return envelope(
        "WithdrawForecast",
        number,
        "SAM",
        expected_version,
        f"FS-{FORECAST_ID}",
        {
            "forecast_id": FORECAST_ID,
            "question_id": QUESTION_ID,
            "forecaster_actor_id": "SAM",
        },
        submitted_at="2026-08-27T12:00:00.000000Z",
        depends_on=[typed_id("CMD", 502)],
    )


def annul_command(number: int = 510, *, expected_version: int = 1) -> dict:
    return envelope(
        "AnnulQuestion",
        number,
        "SAM",
        expected_version,
        f"QS-{QUESTION_ID}",
        {
            "question_id": QUESTION_ID,
            "annulled_by": "SAM",
            "annulment_reason": "SOURCE_PERMANENTLY_UNAVAILABLE",
            "independent_approval_ref": "fixture://red-approval/001",
        },
        submitted_at="2026-08-27T12:00:00.000000Z",
        depends_on=[typed_id("CMD", 501)],
    )


class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.store = FixtureResultStore(Path(self.temporary.name) / "KERNEL")
        self.writer = FixtureResultWriter(self.store, writer_id="PROME")

    def tearDown(self):
        self.temporary.cleanup()

    def accept(self, command: dict, event_number: int):
        outcome = self.writer.accept(
            command,
            event_id=typed_id("EVT", event_number),
            recorded_at=command["submitted_at"],
        )
        self.assertEqual(outcome.state, "WRITTEN", outcome.finding)
        self.assertEqual(outcome.document["command_result"], "ACCEPTED")
        self.assertTrue(validate_event(outcome.document).valid)
        return outcome.document

    def accepted_history(self) -> list[dict]:
        return self.store.accepted_events()

    def test_all_lifecycle_command_contracts_are_strict_and_valid(self):
        commands = [
            question_command(),
            forecast_command(),
            forecast_command(503, version=2, expected_version=1),
            close_command(),
            propose_command(),
            verify_command(),
            dispute_command(),
            correct_command(),
            withdraw_command(),
            annul_command(),
        ]
        for command in commands:
            with self.subTest(command_type=command["command_type"]):
                self.assertTrue(validate_command(command).valid, validate_command(command).findings)
        invalid = annul_command()
        invalid["payload"]["invented_judgment"] = "not allowed"
        self.assertIn("UNKNOWN_FIELD", {finding.code for finding in validate_command(invalid).findings})

    def test_full_resolution_path_and_correction_replay_deterministically(self):
        self.accept(question_command(), 601)
        self.accept(forecast_command(), 602)
        self.accept(forecast_command(503, version=2, expected_version=1), 603)
        closed = self.accept(close_command(), 604)
        proposed = self.accept(propose_command(), 605)
        verified = self.accept(verify_command(), 606)
        corrected = self.accept(correct_command(), 607)
        self.assertEqual(closed["previous_event_id"], typed_id("EVT", 601))
        self.assertEqual(proposed["previous_event_id"], closed["event_id"])
        self.assertEqual(verified["previous_event_id"], proposed["event_id"])
        self.assertEqual(corrected["previous_event_id"], verified["event_id"])
        result = replay(reversed(self.accepted_history()))
        self.assertTrue(result.valid, result.findings)
        question = result.question_states[QUESTION_ID]
        forecast = result.forecast_states[FORECAST_ID]
        self.assertEqual(question["state"], "FINAL")
        self.assertEqual(question["resolution"]["outcome_value"], "YES")
        self.assertEqual(question["outcome"], "NO")
        self.assertEqual(forecast["state"], "LOCKED")
        self.assertEqual([version["probability"] for version in forecast["versions"]], [0.65, 0.72])

    def test_forecast_withdrawal_retains_original_value(self):
        self.accept(question_command(), 611)
        self.accept(forecast_command(), 612)
        self.accept(withdraw_command(), 613)
        result = replay(self.accepted_history())
        forecast = result.forecast_states[FORECAST_ID]
        self.assertEqual(forecast["state"], "WITHDRAWN")
        self.assertEqual(len(forecast["versions"]), 1)
        self.assertEqual(forecast["versions"][0]["probability"], 0.65)

    def test_registered_views_follow_lifecycle_state_and_corrected_outcome(self):
        self.accept(question_command(), 614)
        self.accept(forecast_command(), 615)
        self.accept(forecast_command(503, version=2, expected_version=1), 616)
        self.accept(close_command(), 617)
        self.accept(propose_command(), 618)
        self.accept(verify_command(), 619)
        self.accept(correct_command(), 620)
        views = render_views(self.accepted_history(), render_as_of="2026-09-20T00:00:00.000000Z")
        self.assertNotIn(QUESTION_ID, views["OPEN_QUESTIONS.md"])
        self.assertNotIn(QUESTION_ID, views["RESOLUTION_QUEUE.md"])
        self.assertIn(f"{QUESTION_ID}\t{FORECAST_ID}\t1\t0.65\tNO\t0.4225\t", views["CALIBRATION.tsv"])
        self.assertIn(f"{QUESTION_ID}\t{FORECAST_ID}\t2\t0.72\tNO\t0.5184\t", views["CALIBRATION.tsv"])

    def test_dispute_requires_reproposal_before_verification(self):
        self.accept(question_command(), 621)
        self.accept(close_command(), 622)
        self.accept(propose_command(), 623)
        self.accept(dispute_command(), 624)
        reproposal = propose_command(511, expected_version=4, resolution_id=SECOND_RESOLUTION_ID)
        reproposal["depends_on"] = [typed_id("CMD", 507)]
        self.accept(reproposal, 625)
        verification = verify_command(512, expected_version=5)
        verification["payload"]["resolution_id"] = SECOND_RESOLUTION_ID
        verification["depends_on"] = [typed_id("CMD", 511)]
        self.accept(verification, 626)
        result = replay(self.accepted_history())
        self.assertEqual(result.question_states[QUESTION_ID]["state"], "FINAL")
        self.assertEqual(result.question_states[QUESTION_ID]["resolution"]["resolution_id"], SECOND_RESOLUTION_ID)

    def test_disputed_question_appears_in_resolution_queue(self):
        self.accept(question_command(), 627)
        self.accept(close_command(), 628)
        self.accept(propose_command(), 629)
        self.accept(dispute_command(), 630)
        views = render_views(self.accepted_history(), render_as_of="2026-09-20T00:00:00.000000Z")
        self.assertIn(f"| {QUESTION_ID} | DISPUTED |", views["RESOLUTION_QUEUE.md"])

    def test_registered_annulment_reaches_final_without_resolution(self):
        self.accept(question_command(), 631)
        self.accept(annul_command(), 632)
        result = replay(self.accepted_history())
        question = result.question_states[QUESTION_ID]
        self.assertEqual(question["state"], "FINAL")
        self.assertEqual(question["outcome"], "ANNULLED")
        self.assertIsNone(question["resolution"])

    def test_protected_annulment_without_independent_approval_is_rejected(self):
        self.accept(question_command(), 633)
        annulment = annul_command()
        annulment["payload"]["independent_approval_ref"] = None
        outcome = self.writer.accept(
            annulment,
            event_id=typed_id("EVT", 634),
            recorded_at=annulment["submitted_at"],
        )
        self.assertEqual(outcome.document["reason_code"], "EVIDENCE_REQUIRED")

    def test_stale_version_is_durably_rejected_without_state_mutation(self):
        self.accept(question_command(), 641)
        before = replay(self.accepted_history()).question_states
        stale = close_command(expected_version=0)
        outcome = self.writer.accept(
            stale,
            event_id=typed_id("EVT", 642),
            recorded_at=stale["submitted_at"],
        )
        self.assertEqual(outcome.document["command_result"], "REJECTED")
        self.assertEqual(outcome.document["reason_code"], "STALE_EXPECTED_VERSION")
        self.assertEqual(replay(self.accepted_history()).question_states, before)

    def test_forecast_amendment_after_close_is_rejected(self):
        self.accept(question_command(), 651)
        self.accept(forecast_command(), 652)
        self.accept(close_command(), 653)
        amendment = forecast_command(503, version=2, expected_version=1)
        outcome = self.writer.accept(
            amendment,
            event_id=typed_id("EVT", 654),
            recorded_at=amendment["submitted_at"],
        )
        self.assertEqual(outcome.document["reason_code"], "TRANSITION_FORBIDDEN")
        self.assertEqual(len(replay(self.accepted_history()).forecast_states[FORECAST_ID]["versions"]), 1)

    def test_forecast_amendment_after_deadline_is_rejected_even_without_close_event(self):
        self.accept(question_command(), 655)
        self.accept(forecast_command(), 656)
        amendment = forecast_command(503, version=2, expected_version=1)
        amendment["submitted_at"] = "2026-09-19T12:05:00.000000Z"
        amendment["payload"]["information_as_of"] = "2026-09-19T12:00:00.000000Z"
        outcome = self.writer.accept(
            amendment,
            event_id=typed_id("EVT", 657),
            recorded_at=amendment["submitted_at"],
        )
        self.assertEqual(outcome.document["reason_code"], "TRANSITION_FORBIDDEN")

    def test_resolution_without_evidence_is_durably_rejected(self):
        self.accept(question_command(), 661)
        self.accept(close_command(), 662)
        proposal = propose_command()
        proposal["payload"]["resolution_evidence_refs"] = []
        outcome = self.writer.accept(
            proposal,
            event_id=typed_id("EVT", 663),
            recorded_at=proposal["submitted_at"],
        )
        self.assertEqual(outcome.document["reason_code"], "EVIDENCE_REQUIRED")
        self.assertEqual(replay(self.accepted_history()).question_states[QUESTION_ID]["state"], "CLOSED")

    def test_absence_based_no_requires_registered_search_attempt(self):
        question = question_command()
        question["payload"]["negative_search_procedure"] = "fixture://negative-search-procedure"
        self.accept(question, 664)
        self.accept(close_command(), 665)
        proposal = propose_command()
        proposal["payload"]["outcome_value"] = "NO"
        proposal["payload"]["negative_search_attempt"] = None
        outcome = self.writer.accept(
            proposal,
            event_id=typed_id("EVT", 666),
            recorded_at=proposal["submitted_at"],
        )
        self.assertEqual(outcome.document["reason_code"], "EVIDENCE_REQUIRED")

    def test_protected_self_verification_is_durably_rejected(self):
        self.accept(question_command(), 671)
        self.accept(forecast_command(), 672)
        self.accept(close_command(), 673)
        self.accept(propose_command(), 674)
        verification = verify_command(actor_id="SAM")
        outcome = self.writer.accept(
            verification,
            event_id=typed_id("EVT", 675),
            recorded_at=verification["submitted_at"],
        )
        self.assertEqual(outcome.document["reason_code"], "PROTECTED_SELF_VERIFICATION")
        self.assertEqual(replay(self.accepted_history()).question_states[QUESTION_ID]["state"], "RESOLUTION_PROPOSED")

    def test_verification_disagreement_must_use_dispute(self):
        self.accept(question_command(), 681)
        self.accept(close_command(), 682)
        self.accept(propose_command(), 683)
        verification = verify_command()
        verification["payload"]["verified_outcome_value"] = "NO"
        outcome = self.writer.accept(
            verification,
            event_id=typed_id("EVT", 684),
            recorded_at=verification["submitted_at"],
        )
        self.assertEqual(outcome.document["reason_code"], "TRANSITION_FORBIDDEN")

    def test_unregistered_annulment_reason_is_rejected(self):
        self.accept(question_command(), 691)
        annulment = annul_command()
        annulment["payload"]["annulment_reason"] = "POOR_FORECAST_PERFORMANCE"
        outcome = self.writer.accept(
            annulment,
            event_id=typed_id("EVT", 692),
            recorded_at=annulment["submitted_at"],
        )
        self.assertEqual(outcome.document["reason_code"], "TRANSITION_FORBIDDEN")

    def test_close_own_cannot_be_used_on_another_actors_question(self):
        self.accept(question_command(), 693)
        closure = close_command()
        closure["actor_id"] = "RED"
        closure["payload"]["closed_by"] = "RED"
        outcome = self.writer.accept(
            closure,
            event_id=typed_id("EVT", 694),
            recorded_at=closure["submitted_at"],
        )
        self.assertEqual(outcome.document["reason_code"], "PERMISSION_DENIED")

    def test_lifecycle_permissions_are_explicit_and_custody_never_substitutes(self):
        registry = PermissionRegistry.from_files(
            PERMISSION_FIXTURES / "actors.json",
            PERMISSION_FIXTURES / "capability-grants.json",
        )
        commands = [
            question_command(),
            forecast_command(),
            forecast_command(503, version=2, expected_version=1),
            close_command(),
            propose_command(),
            verify_command(),
            dispute_command(),
            correct_command(),
            withdraw_command(),
            annul_command(),
        ]
        for command in commands:
            actor = command["actor_id"]
            path = f"AGENTS/{actor}/outbox/kernel/submissions/{command['command_id']}.json"
            with self.subTest(command_type=command["command_type"]):
                self.assertTrue(authorize_command(command, path, registry).valid)
        unauthorized = close_command()
        unauthorized["actor_id"] = "PROME"
        unauthorized["payload"]["closed_by"] = "PROME"
        path = f"AGENTS/PROME/outbox/kernel/submissions/{unauthorized['command_id']}.json"
        denied = authorize_command(unauthorized, path, registry)
        self.assertIn("PERMISSION_DENIED", {finding.code for finding in denied.findings})


if __name__ == "__main__":
    unittest.main()
