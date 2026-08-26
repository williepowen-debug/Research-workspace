from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from core import canonical_bytes  # noqa: E402
from native import SubprocessGitBoundary, normalized_repository_path, verify_native_references  # noqa: E402
from test_core import command  # noqa: E402
from test_lifecycle import propose_command  # noqa: E402


FIXTURES = Path(__file__).resolve().parent / "fixtures" / "native"


class SyntheticGitRepository:
    def __init__(self, testcase: unittest.TestCase):
        self._temporary = tempfile.TemporaryDirectory()
        testcase.addCleanup(self._temporary.cleanup)
        self.path = Path(self._temporary.name)
        subprocess.run(["git", "init", "-q", str(self.path)], check=True)
        subprocess.run(["git", "-C", str(self.path), "config", "user.name", "Kernel Fixture"], check=True)
        subprocess.run(["git", "-C", str(self.path), "config", "user.email", "fixture@example.invalid"], check=True)
        native = self.path / "native"
        native.mkdir()
        for fixture in FIXTURES.iterdir():
            shutil.copyfile(fixture, native / fixture.name)
        subprocess.run(["git", "-C", str(self.path), "add", "native"], check=True)
        subprocess.run(["git", "-C", str(self.path), "commit", "-q", "-m", "synthetic native fixtures"], check=True)
        self.commit = subprocess.run(
            ["git", "-C", str(self.path), "rev-parse", "HEAD"], check=True, capture_output=True, text=True
        ).stdout.strip()
        self.git = SubprocessGitBoundary(self.path)

    def blob(self, relative: str) -> bytes:
        value = self.git.read_blob(self.commit, relative)
        assert value is not None
        return value


def ref(commit: str, path: str, locator_type: str, locator: str, selected: bytes) -> dict:
    return {
        "repository": "williepowen-debug/Research-workspace",
        "source_commit": commit,
        "path": path,
        "locator_type": locator_type,
        "locator": locator,
        "raw_record_sha256": hashlib.sha256(selected).hexdigest(),
    }


def tsv_line(blob: bytes, record_id: bytes) -> bytes:
    return next(line for line in blob.splitlines(keepends=True) if line.startswith(record_id + b"\t"))


class NativeReferenceTests(unittest.TestCase):
    def setUp(self):
        self.repo = SyntheticGitRepository(self)

    def test_file_backed_tsv_happy_path_ignores_mutable_checkout(self):
        candidate = command("SubmitForecast")
        selected = tsv_line(self.repo.blob("native/predictions.tsv"), b"FIX-F-001")
        candidate["native_refs"] = [ref(
            self.repo.commit, "native/predictions.tsv", "TSV_RECORD_ID", "record_id=FIX-F-001", selected
        )]
        (self.repo.path / "native" / "predictions.tsv").write_text("mutable checkout corruption\n", encoding="utf-8")
        self.assertTrue(verify_native_references(candidate, self.repo.git).valid)

    def test_file_backed_json_companion_happy_path(self):
        candidate = command("RegisterQuestion")
        companion = json.loads(self.repo.blob("native/companion.json"))
        selected = canonical_bytes(companion["questions"]["FIX-Q-001"])
        candidate["native_refs"] = [ref(
            self.repo.commit, "native/companion.json", "JSON_POINTER", "/questions/FIX-Q-001", selected
        )]
        self.assertTrue(verify_native_references(candidate, self.repo.git).valid)

    def test_cli_end_to_end_against_temporary_git_repository(self):
        candidate = command("SubmitForecast")
        selected = tsv_line(self.repo.blob("native/predictions.tsv"), b"FIX-F-001")
        candidate["native_refs"] = [ref(
            self.repo.commit, "native/predictions.tsv", "TSV_RECORD_ID", "record_id=FIX-F-001", selected
        )]
        command_path = self.repo.path / "fixture-command.json"
        command_path.write_text(json.dumps(candidate), encoding="utf-8")
        completed = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "verify_native.py"), str(command_path),
             "--repository", str(self.repo.path)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("PASS: exact native bytes", completed.stdout)

    def test_missing_commit_fails_closed(self):
        candidate = command("SubmitForecast")
        candidate["native_refs"][0]["source_commit"] = "0" * 40
        self.assert_codes(candidate, "NATIVE_COMMIT_MISSING")

    def test_missing_path_fails_closed(self):
        candidate = command("SubmitForecast")
        candidate["native_refs"][0].update(source_commit=self.repo.commit, path="native/missing.tsv")
        self.assert_codes(candidate, "NATIVE_PATH_MISSING")

    def test_missing_record_fails_closed(self):
        candidate = self.forecast_candidate("native/predictions.tsv", "record_id=ABSENT", b"unused")
        self.assert_codes(candidate, "NATIVE_RECORD_MISSING")

    def test_duplicate_record_is_ambiguous(self):
        candidate = self.forecast_candidate("native/duplicate.tsv", "record_id=FIX-F-DUP", b"unused")
        self.assert_codes(candidate, "NATIVE_RECORD_AMBIGUOUS")

    def test_shifted_row_is_invalid(self):
        candidate = self.forecast_candidate("native/shifted.tsv", "record_id=FIX-F-SHIFT", b"unused")
        self.assert_codes(candidate, "NATIVE_RECORD_INVALID")

    def test_repeated_tsv_header_is_invalid(self):
        candidate = self.forecast_candidate("native/repeated_header.tsv", "record_id=FIX-F-ONE", b"unused")
        self.assert_codes(candidate, "NATIVE_RECORD_INVALID")

    def test_invalid_json_pointer_fails_closed(self):
        candidate = command("RegisterQuestion")
        candidate["native_refs"] = [ref(
            self.repo.commit, "native/companion.json", "JSON_POINTER", "questions/FIX-Q-001", b"unused"
        )]
        self.assert_codes(candidate, "NATIVE_JSON_POINTER_INVALID")

    def test_json_pointer_missing_value_fails_closed(self):
        candidate = command("RegisterQuestion")
        candidate["native_refs"] = [ref(
            self.repo.commit, "native/companion.json", "JSON_POINTER", "/questions/ABSENT", b"unused"
        )]
        self.assert_codes(candidate, "NATIVE_RECORD_MISSING")

    def test_duplicate_json_members_are_ambiguous_and_fail_closed(self):
        candidate = command("SubmitForecast")
        candidate["native_refs"] = [ref(
            self.repo.commit, "native/ambiguous.json", "JSON_POINTER", "/record", b"unused"
        )]
        self.assert_codes(candidate, "NATIVE_RECORD_AMBIGUOUS")

    def test_raw_hash_mismatch_fails_closed(self):
        candidate = self.forecast_candidate("native/predictions.tsv", "record_id=FIX-F-001", b"wrong")
        self.assert_codes(candidate, "NATIVE_BLOB_MISMATCH")

    def test_material_term_absent_from_native_records_fails_closed(self):
        candidate = command("SubmitForecast")
        selected = tsv_line(self.repo.blob("native/predictions.tsv"), b"FIX-F-001")
        candidate["native_refs"] = [ref(
            self.repo.commit, "native/predictions.tsv", "TSV_RECORD_ID", "record_id=FIX-F-001", selected
        )]
        candidate["payload"]["probability"] = 0.66
        self.assert_codes(candidate, "NATIVE_RECORD_MISMATCH")

    def test_lifecycle_resolution_terms_are_verified_exactly(self):
        candidate = propose_command()
        companion = json.loads(self.repo.blob("native/companion.json"))
        selected = canonical_bytes(companion["lifecycle"]["FIX-R-001"])
        candidate["native_refs"] = [ref(
            self.repo.commit, "native/companion.json", "JSON_POINTER", "/lifecycle/FIX-R-001", selected
        )]
        self.assertTrue(verify_native_references(candidate, self.repo.git).valid)
        candidate["payload"]["outcome_value"] = "NO"
        self.assert_codes(candidate, "NATIVE_RECORD_MISMATCH")

    def test_path_normalization_is_strict(self):
        invalid = ["/native/a.tsv", "../a.tsv", "native/./a.tsv", "native//a.tsv", "native\\a.tsv", "native/"]
        self.assertTrue(normalized_repository_path("native/a.tsv"))
        self.assertTrue(all(not normalized_repository_path(path) for path in invalid))

    def forecast_candidate(self, path: str, locator: str, selected: bytes) -> dict:
        candidate = command("SubmitForecast")
        candidate["native_refs"] = [ref(self.repo.commit, path, "TSV_RECORD_ID", locator, selected)]
        return candidate

    def assert_codes(self, candidate: dict, expected: str) -> None:
        codes = {finding.code for finding in verify_native_references(candidate, self.repo.git).findings}
        self.assertIn(expected, codes)


if __name__ == "__main__":
    unittest.main()
