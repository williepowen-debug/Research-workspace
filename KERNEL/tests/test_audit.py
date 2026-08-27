from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLANNING_FIXTURE = ROOT / "tests" / "fixtures" / "planning" / "question_forecast_batch.json"
sys.path.insert(0, str(ROOT / "tools"))

from audit import (  # noqa: E402
    REPOSITORY_ROOT,
    SubprocessGitHistoryBoundary,
    verify_additions_only,
    verify_durable_results,
)


class SyntheticAuditRepository:
    def __init__(self, testcase: unittest.TestCase):
        self._temporary = tempfile.TemporaryDirectory()
        testcase.addCleanup(self._temporary.cleanup)
        self.path = Path(self._temporary.name)
        subprocess.run(["git", "init", "-q", str(self.path)], check=True)
        subprocess.run(["git", "-C", str(self.path), "config", "user.name", "Kernel Fixture"], check=True)
        subprocess.run(
            ["git", "-C", str(self.path), "config", "user.email", "fixture@example.invalid"],
            check=True,
        )
        self.write("README.md", "synthetic audit history\n")
        self.base = self.commit("synthetic history boundary")
        self.git = SubprocessGitHistoryBoundary(self.path)

    def write(self, relative: str, content: str) -> None:
        destination = self.path / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")

    def delete(self, relative: str) -> None:
        (self.path / relative).unlink()

    def rename(self, source: str, destination: str) -> None:
        target = self.path / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        (self.path / source).rename(target)

    def commit(self, message: str) -> str:
        subprocess.run(["git", "-C", str(self.path), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(self.path), "commit", "-q", "-m", message], check=True)
        return subprocess.run(
            ["git", "-C", str(self.path), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()


def fixture_commands() -> tuple[dict, dict]:
    fixture = json.loads(PLANNING_FIXTURE.read_text(encoding="utf-8"))
    by_type = {command["command_type"]: command for command in fixture["submissions"]}
    return by_type["RegisterQuestion"], by_type["SubmitForecast"]


def accepted(command: dict) -> dict:
    return {
        "command_id": command["command_id"],
        "command_result": "ACCEPTED",
        "reason_code": None,
    }


def rejected(command: dict) -> dict:
    return {
        "command_id": command["command_id"],
        "command_result": "REJECTED",
        "reason_code": "PERMISSION_DENIED",
    }


class AdditionsOnlyAuditTests(unittest.TestCase):
    def setUp(self):
        self.repo = SyntheticAuditRepository(self)

    def test_new_event_and_receipt_files_pass(self):
        self.repo.write("KERNEL/shadow/events/2026/08/EVT-fixture.json", "{\"fixture\":1}\n")
        self.repo.write("KERNEL/audit/commands/2026/08/CMD-fixture.json", "{\"fixture\":2}\n")
        head = self.repo.commit("add synthetic durable results")
        result = verify_additions_only(self.repo.git, self.repo.base, head)
        self.assertEqual(result.status, "PASS")
        self.assertEqual(result.checked_commits, (head,))

    def test_modified_event_is_blocking(self):
        self.repo.write("KERNEL/shadow/events/2026/08/EVT-fixture.json", "{\"fixture\":1}\n")
        self.repo.commit("add synthetic event")
        self.repo.write("KERNEL/shadow/events/2026/08/EVT-fixture.json", "{\"fixture\":99}\n")
        head = self.repo.commit("modify synthetic event")
        result = verify_additions_only(self.repo.git, self.repo.base, head)
        self.assertEqual(result.status, "EXCEPTION")
        self.assertEqual([finding.code for finding in result.findings], ["ADDITIONS_ONLY_VIOLATION"])
        self.assertIn("M KERNEL/shadow/events/", result.findings[0].message)

    def test_deleted_receipt_is_blocking(self):
        path = "KERNEL/audit/commands/2026/08/CMD-fixture.json"
        self.repo.write(path, "{\"fixture\":1}\n")
        self.repo.commit("add synthetic receipt")
        self.repo.delete(path)
        head = self.repo.commit("delete synthetic receipt")
        result = verify_additions_only(self.repo.git, self.repo.base, head)
        self.assertEqual(result.status, "EXCEPTION")
        self.assertIn("D KERNEL/audit/commands/", result.findings[0].message)

    def test_rename_away_cannot_hide_deletion(self):
        source = "KERNEL/shadow/events/2026/08/EVT-fixture.json"
        self.repo.write(source, "{\"fixture\":1}\n")
        self.repo.commit("add synthetic event")
        self.repo.rename(source, "archive/EVT-fixture.json")
        head = self.repo.commit("rename event outside protected history")
        result = verify_additions_only(self.repo.git, self.repo.base, head)
        self.assertEqual(result.status, "EXCEPTION")
        self.assertIn("D KERNEL/shadow/events/", result.findings[0].message)

    def test_nonprotected_changes_do_not_expand_the_perimeter(self):
        self.repo.write("notes.txt", "one\n")
        self.repo.commit("add unrelated fixture file")
        self.repo.write("notes.txt", "two\n")
        head = self.repo.commit("modify unrelated fixture file")
        result = verify_additions_only(self.repo.git, self.repo.base, head)
        self.assertEqual(result.status, "PASS")

    def test_unresolved_or_non_full_commit_is_unknown_and_blocking(self):
        result = verify_additions_only(self.repo.git, self.repo.base[:12], self.repo.base)
        self.assertEqual(result.status, "UNKNOWN")
        self.assertTrue(result.blocking)
        self.assertEqual(result.unknowns[0].code, "AUDIT_HISTORY_UNKNOWN")

    def test_live_repository_boundary_is_refused(self):
        with self.assertRaisesRegex(ValueError, "cannot inspect the live repository"):
            SubprocessGitHistoryBoundary(REPOSITORY_ROOT)
        with self.assertRaisesRegex(ValueError, "cannot inspect the live repository"):
            SubprocessGitHistoryBoundary(REPOSITORY_ROOT.parent)

    def test_cli_live_repository_refusal_prints_perimeter_and_exception(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "audit.py"),
                "additions-only",
                "--repository",
                str(REPOSITORY_ROOT),
                "--live-repository-root",
                str(REPOSITORY_ROOT),
                "--base",
                self.repo.base,
                "--head",
                self.repo.base,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("perimeter: check=additions-only", completed.stdout)
        self.assertIn("EXCEPTION: additions-only verification did not pass", completed.stdout)
        self.assertIn("AUDIT_BOUNDARY_REFUSED", completed.stdout)

    def test_cli_prints_perimeter_and_pass(self):
        self.repo.write("KERNEL/shadow/events/2026/08/EVT-fixture.json", "{}\n")
        head = self.repo.commit("add synthetic event")
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "audit.py"),
                "additions-only",
                "--repository",
                str(self.repo.path),
                "--live-repository-root",
                str(REPOSITORY_ROOT),
                "--base",
                self.repo.base,
                "--head",
                head,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("perimeter: check=additions-only", completed.stdout)
        self.assertIn("PASS: protected accepted-event and receipt paths", completed.stdout)


class DurableResultAuditTests(unittest.TestCase):
    def setUp(self):
        self.question, self.forecast = fixture_commands()

    def test_exactly_one_result_per_submission_passes(self):
        result = verify_durable_results(
            [self.question, self.forecast],
            [accepted(self.question), rejected(self.forecast)],
            pass_reported_success=True,
        )
        self.assertEqual(result.status, "PASS")
        self.assertIn("explicit_submissions=2", result.perimeter)

    def test_duplicate_result_is_blocking(self):
        result = verify_durable_results(
            [self.question],
            [accepted(self.question), rejected(self.question)],
            pass_reported_success=True,
        )
        self.assertEqual(result.status, "EXCEPTION")
        self.assertIn("AUDIT_DUPLICATE_RESULT", {finding.code for finding in result.findings})

    def test_duplicate_results_outside_submission_inventory_still_block(self):
        result = verify_durable_results(
            [self.question],
            [
                accepted(self.question),
                accepted(self.forecast),
                rejected(self.forecast),
            ],
            pass_reported_success=True,
        )
        self.assertEqual(result.status, "EXCEPTION")
        duplicates = [finding for finding in result.findings if finding.code == "AUDIT_DUPLICATE_RESULT"]
        self.assertEqual([finding.message for finding in duplicates], [self.forecast["command_id"]])

    def test_result_outside_submission_inventory_is_blocking(self):
        result = verify_durable_results(
            [self.question],
            [accepted(self.question), accepted(self.forecast)],
            pass_reported_success=True,
        )
        self.assertEqual(result.status, "EXCEPTION")
        unexpected = [finding for finding in result.findings if finding.code == "AUDIT_UNEXPECTED_RESULT"]
        self.assertEqual([finding.message for finding in unexpected], [self.forecast["command_id"]])

    def test_missing_result_after_reported_success_is_audit_gap(self):
        result = verify_durable_results(
            [self.question, self.forecast],
            [accepted(self.question)],
            pass_reported_success=True,
        )
        self.assertEqual(result.status, "EXCEPTION")
        gaps = [finding for finding in result.findings if finding.code == "AUDIT_GAP"]
        self.assertEqual([finding.message for finding in gaps], [self.forecast["command_id"]])

    def test_missing_result_without_success_claim_is_unknown_not_gap(self):
        result = verify_durable_results(
            [self.question],
            [],
            pass_reported_success=False,
        )
        self.assertEqual(result.status, "UNKNOWN")
        self.assertFalse(result.findings)
        self.assertEqual(result.unknowns[0].code, "AUDIT_COMPLETENESS_UNKNOWN")

    def test_invalid_result_inventory_fails_closed(self):
        invalid = accepted(self.question)
        invalid["unexpected"] = True
        result = verify_durable_results(
            [self.question],
            [invalid],
            pass_reported_success=True,
        )
        self.assertEqual(result.status, "EXCEPTION")
        self.assertEqual(
            {finding.code for finding in result.findings},
            {"AUDIT_GAP", "RESULT_INVENTORY_INVALID"},
        )

    def test_duplicate_submission_inventory_fails_closed(self):
        result = verify_durable_results(
            [self.question, copy.deepcopy(self.question)],
            [accepted(self.question)],
            pass_reported_success=True,
        )
        self.assertEqual(result.status, "EXCEPTION")
        self.assertIn("DUPLICATE_COMMAND", {finding.code for finding in result.findings})

    def test_cli_prints_perimeter_and_audit_gap(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            submissions_path = root / "submissions.json"
            results_path = root / "results.json"
            submissions_path.write_text(json.dumps([self.question, self.forecast]), encoding="utf-8")
            results_path.write_text(json.dumps([accepted(self.question)]), encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools" / "audit.py"),
                    "durable-results",
                    "--submissions",
                    str(submissions_path),
                    "--results",
                    str(results_path),
                    "--live-repository-root",
                    str(REPOSITORY_ROOT),
                    "--pass-reported-success",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("perimeter: check=durable-results", completed.stdout)
        self.assertIn("EXCEPTION: durable-results verification did not pass", completed.stdout)
        self.assertIn("AUDIT_GAP", completed.stdout)

    def test_cli_unreadable_inventory_prints_perimeter_and_exception(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            missing = root / "missing.json"
            results_path = root / "results.json"
            results_path.write_text("[]", encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools" / "audit.py"),
                    "durable-results",
                    "--submissions",
                    str(missing),
                    "--results",
                    str(results_path),
                    "--live-repository-root",
                    str(REPOSITORY_ROOT),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("perimeter: check=durable-results", completed.stdout)
        self.assertIn("AUDIT_INVENTORY_UNREADABLE", completed.stdout)


if __name__ == "__main__":
    unittest.main()
