from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from core import sha256_hex  # noqa: E402
from custody import audit_return, authorize_writer, load_custody  # noqa: E402


COMMAND = "CMD-018f22e2-7d00-7000-8000-000000000001"


def policy():
    return {
        "schema_version": "kernel.custody.1",
        "policy_version": "kernel.policy.1",
        "primary_writer_id": "PROME",
        "substitutes": [
            {"writer_id": "RED", "command_accept_default": False, "registered_by": "WILL"},
        ],
    }


def activation():
    return {
        "schema_version": "kernel.custody.1",
        "policy_version": "kernel.policy.1",
        "activation_id": "CUSTODY-SYNTHETIC-001",
        "authorized_by": "WILL",
        "substitute_writer_id": "RED",
        "window_start": "2026-08-26T12:00:00.000000Z",
        "window_end": "2026-08-26T13:00:00.000000Z",
        "command_ids": [COMMAND],
        "revoked_at": None,
    }


def result_document():
    return {"command_id": COMMAND, "writer_id": "RED", "recorded_at": "2026-08-26T12:15:00.000000Z", "command_result": "ACCEPTED"}


def review(document):
    return {
        "schema_version": "kernel.custody.1",
        "policy_version": "kernel.policy.1",
        "activation_id": "CUSTODY-SYNTHETIC-001",
        "reviewed_by": "PROME",
        "reviewed_at": "2026-08-26T13:00:00.000000Z",
        "result_hashes": {COMMAND: sha256_hex(document)},
    }


class CustodyTests(unittest.TestCase):
    def test_primary_is_active_without_activation(self):
        loaded = load_custody(policy())
        self.assertTrue(loaded.valid, loaded.findings)
        self.assertTrue(authorize_writer(loaded, "PROME", COMMAND, "2026-08-26T12:15:00.000000Z").valid)

    def test_substitute_is_dormant_by_default(self):
        decision = authorize_writer(load_custody(policy()), "RED", COMMAND, "2026-08-26T12:15:00.000000Z")
        self.assertEqual({f.code for f in decision.findings}, {"CUSTODY_DENIED"})

    def test_substitute_must_be_disabled_in_policy(self):
        changed = policy()
        changed["substitutes"][0]["command_accept_default"] = True
        self.assertFalse(load_custody(changed).valid)

    def test_only_will_can_register_and_activate_substitute(self):
        changed_policy = policy()
        changed_policy["substitutes"][0]["registered_by"] = "PROME"
        self.assertFalse(load_custody(changed_policy).valid)
        changed_activation = activation()
        changed_activation["authorized_by"] = "PROME"
        self.assertFalse(load_custody(policy(), changed_activation).valid)

    def test_activated_substitute_is_bounded_by_time_and_command(self):
        loaded = load_custody(policy(), activation())
        self.assertTrue(authorize_writer(loaded, "RED", COMMAND, "2026-08-26T12:15:00.000000Z").valid)
        for command_id, instant in (
            ("CMD-OTHER", "2026-08-26T12:15:00.000000Z"),
            (COMMAND, "2026-08-26T11:59:59.999999Z"),
            (COMMAND, "2026-08-26T13:00:00.000000Z"),
        ):
            with self.subTest(command_id=command_id, instant=instant):
                self.assertFalse(authorize_writer(loaded, "RED", command_id, instant).valid)

    def test_primary_is_suspended_during_substitute_window(self):
        loaded = load_custody(policy(), activation())
        self.assertFalse(authorize_writer(loaded, "PROME", COMMAND, "2026-08-26T12:15:00.000000Z").valid)
        self.assertTrue(authorize_writer(loaded, "PROME", COMMAND, "2026-08-26T13:00:00.000000Z").valid)

    def test_revocation_ends_substitute_and_restores_primary(self):
        changed = activation()
        changed["revoked_at"] = "2026-08-26T12:20:00.000000Z"
        loaded = load_custody(policy(), changed)
        self.assertFalse(authorize_writer(loaded, "RED", COMMAND, "2026-08-26T12:20:00.000000Z").valid)
        self.assertTrue(authorize_writer(loaded, "PROME", COMMAND, "2026-08-26T12:20:00.000000Z").valid)

    def test_unknown_writer_and_bad_clock_fail_closed(self):
        loaded = load_custody(policy())
        self.assertFalse(authorize_writer(loaded, "CI", COMMAND, "2026-08-26T12:15:00.000000Z").valid)
        decision = authorize_writer(loaded, "PROME", COMMAND, "not-a-time")
        self.assertEqual({f.code for f in decision.findings}, {"CUSTODY_UNKNOWN"})

    def test_return_audit_reconciles_exact_results_and_hashes(self):
        loaded = load_custody(policy(), activation())
        document = result_document()
        self.assertTrue(audit_return(loaded, [document], review(document)).valid)

    def test_return_audit_requires_primary_after_window(self):
        loaded = load_custody(policy(), activation())
        document = result_document()
        changed = review(document)
        changed["reviewed_by"] = "RED"
        changed["reviewed_at"] = "2026-08-26T12:30:00.000000Z"
        self.assertFalse(audit_return(loaded, [document], changed).valid)

    def test_return_audit_blocks_missing_extra_or_changed_results(self):
        loaded = load_custody(policy(), activation())
        document = result_document()
        self.assertFalse(audit_return(loaded, [], review(document)).valid)
        changed = copy.deepcopy(document)
        changed["command_result"] = "REJECTED"
        self.assertFalse(audit_return(loaded, [changed], review(document)).valid)

    def test_invalid_window_or_revocation_fails_closed(self):
        for field, value in (
            ("window_end", "2026-08-26T12:00:00.000000Z"),
            ("revoked_at", "2026-08-26T13:00:00.000001Z"),
        ):
            changed = activation()
            changed[field] = value
            with self.subTest(field=field):
                self.assertFalse(load_custody(policy(), changed).valid)


if __name__ == "__main__":
    unittest.main()
