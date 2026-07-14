import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate import load_agents, validate  # noqa: E402


FIXTURES = Path(__file__).parent / "fixtures"
AGENTS = load_agents(None, FIXTURES / "agents.txt")


class ValidatorTests(unittest.TestCase):
    def write(self, directory: Path, name: str, content: str) -> Path:
        path = directory / name
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_action_and_receipt(self):
        report = validate([FIXTURES / "valid_action.md", FIXTURES / "valid_receipt.md"], AGENTS)
        self.assertEqual(report.errors, 0, report.findings)
        self.assertEqual(len(report.messages), 1)
        self.assertEqual(len(report.obligations), 1)
        self.assertEqual(report.receipts, 1)

    def test_invalid_timestamp_is_rejected(self):
        text = (FIXTURES / "valid_action.md").read_text().replace("14:00:00", "14:60:00")
        with tempfile.TemporaryDirectory() as tmp:
            report = validate([self.write(Path(tmp), "bad.md", text)], AGENTS)
        self.assertGreater(report.errors, 0)
        self.assertTrue({"created_at", "front_matter"} & {finding.code for finding in report.findings})

    def test_info_cannot_hide_action(self):
        text = (FIXTURES / "valid_action.md").read_text()
        text = text.replace("role: ACTION", "role: INFO").replace("receipt_required: true", "receipt_required: false")
        with tempfile.TemporaryDirectory() as tmp:
            report = validate([self.write(Path(tmp), "bad.md", text)], AGENTS)
        self.assertIn("info_action", {finding.code for finding in report.findings})

    def test_integrated_requires_target_and_effect(self):
        text = (FIXTURES / "valid_receipt.md").read_text()
        text = text.replace("NO_CHANGE |  | AGENTS/BRENT/STATUS.md | Existing grade remains valid after review", "INTEGRATED |  |  | ")
        with tempfile.TemporaryDirectory() as tmp:
            report = validate([FIXTURES / "valid_action.md", self.write(Path(tmp), "bad-receipt.md", text)], AGENTS)
        codes = {finding.code for finding in report.findings}
        self.assertIn("target_path", codes)
        self.assertIn("effect_or_reason", codes)

    def test_wrong_receipt_owner_is_rejected(self):
        text = (FIXTURES / "valid_receipt.md").read_text().replace("recipient: BRENT", "recipient: SAM")
        with tempfile.TemporaryDirectory() as tmp:
            report = validate([self.write(Path(tmp), "bad-receipt.md", text)], AGENTS)
        self.assertIn("receipt_obligation", {finding.code for finding in report.findings})

    def test_identical_multi_recipient_copy_is_idempotent(self):
        text = (FIXTURES / "valid_action.md").read_text()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = validate([self.write(root, "copy-a.md", text), self.write(root, "copy-b.md", text)], AGENTS)
        self.assertEqual(report.errors, 0, report.findings)
        self.assertEqual(len(report.messages), 1)
        self.assertEqual(len(report.obligations), 1)

    def test_conflicting_duplicate_message_is_rejected(self):
        text = (FIXTURES / "valid_action.md").read_text()
        changed = text.replace("subject: Grade the KOC platform hit", "subject: Conflicting payload")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = validate([self.write(root, "copy-a.md", text), self.write(root, "copy-b.md", changed)], AGENTS)
        self.assertIn("duplicate_message_conflict", {finding.code for finding in report.findings})

    def test_legacy_brent_fixture_preserves_all_source_items(self):
        data = json.loads((FIXTURES / "legacy_brent_split.json").read_text())
        represented = sorted({item for obligation in data["normalized_obligations"] for item in obligation["source_items"]})
        self.assertEqual(represented, data["source_items"])
        self.assertEqual(len(data["normalized_obligations"]), 4)
        self.assertEqual(data["normalized_obligations"][0]["source_items"], [1, 5])


if __name__ == "__main__":
    unittest.main()
