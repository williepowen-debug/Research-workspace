"""L889 regression controls using the production WALTER validator, isolated inputs."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("read_cap_companion_subject", REPO / "scripts/read_cap_check.py")
cap = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cap)


class CompanionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.sid = "SIG-W-20260619-008"
        self.source = f"BOARD/{self.sid}-long-title.md"
        self.companion = f"AGENTS/WALTER/reading/{self.sid}.md"
        self.review = "AGENTS/WALTER/research/review.md"
        bodies = {self.source: f"signal_id: {self.sid}\n" + "x" * cap.BUDGET_BYTES,
                  self.companion: "Reviewed historical reading copy\n",
                  self.review: "Verdict: APPROVED\n"}
        self.record = dict(status="reviewed", reviewed_on="2026-01-01", review_due="2099-01-01",
                           source=self.source, companion=self.companion, review=self.review)
        for key in ("source", "companion", "review"):
            p = self.root / self.record[key]
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(bodies[self.record[key]])
            self.record[key + "_sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
        self.registry = self.root / "AGENTS/WALTER/registry/signal_read_companions.json"
        self.registry.parent.mkdir(parents=True)
        self.save_record()
        self.rows = [
            "ATTESTATION\tD\t.\tmanifest-complete\tboot\tD\t2026-11-02\tdeclared",
            f"READ\tD\tBOARD/SIG-W-*.md\twhole\tselected\tD\t2026-11-02\tMEMBER EXCEPTION {self.sid} via {self.companion}",
            f"READ\tD\t{self.companion}\twhole\tselected\tD\t2026-11-02\treading copy"]

    def save_record(self):
        self.registry.write_text(json.dumps({self.sid: self.record}))

    def run_rows(self, rows=None):
        manifest = self.root / "READS.tsv"
        manifest.write_text("row_kind\treader\tpath\tmode\tsource_boot_step\tdeclared_by\tdeclared_on\tnotes\n"
                            + "\n".join(self.rows if rows is None else rows) + "\n")
        return cap.declared_reads("D", str(manifest), str(self.root))

    def assert_retained(self, result):
        self.assertIn(str(self.root / self.source), result[0])

    def test_valid_substitute_both_row_orders(self):
        for rows in (self.rows, self.rows[::-1]):
            cb, vis, problems, att, note = self.run_rows(rows)
            self.assertNotIn(str(self.root / self.source), cb)
            self.assertIn(str(self.root / self.companion), cb)
            self.assertTrue(any("validated reading copy" in r[1] for r in vis))
            self.assertEqual(problems, [])

    def test_no_exception_keeps_original(self):
        self.assert_retained(self.run_rows([r.replace("MEMBER EXCEPTION", "historical mention") for r in self.rows]))

    def test_explicit_source_or_other_class_survives_both_orders(self):
        for target in (self.source, "BOARD/*.md"):
            extra = f"READ\tD\t{target}\twhole\tother-step\tD\t2026-11-02\tno substitution"
            for rows in (self.rows + [extra], [extra] + self.rows):
                self.assert_retained(self.run_rows(rows))

    def test_wrong_step_or_nonwhole_copy_keeps_original(self):
        for change in ("\tscoped\tselected", "\twhole\tother-step"):
            rows = self.rows[:2] + [self.rows[2].replace("\twhole\tselected", change)]
            r = self.run_rows(rows)
            self.assert_retained(r)
            self.assertTrue(any(sev == cap.P_DEFECT for sev, msg in r[2]))

    def test_unattested_never_substitutes(self):
        self.assert_retained(self.run_rows(self.rows[1:]))

    def test_changed_bound_bytes_keep_original(self):
        for key in ("source", "companion", "review"):
            p = self.root / self.record[key]
            original = p.read_bytes()
            p.write_bytes(original + b"changed")
            self.assert_retained(self.run_rows())
            p.write_bytes(original)

    def test_invalid_or_expired_record_keeps_original(self):
        for key, value in (("status", "unreviewed"), ("review_due", "2026-01-01"),
                           ("source", "BOARD/wrong.md"), ("companion", "../escape.md")):
            original = self.record[key]
            self.record[key] = value
            self.save_record()
            self.assert_retained(self.run_rows())
            self.record[key] = original
        self.save_record()

    def test_bad_registry_keeps_original_and_reports_defect(self):
        self.registry.write_text("{")
        r = self.run_rows()
        self.assert_retained(r)
        self.assertTrue(r[2])

    def test_missing_validator_keeps_original(self):
        with patch.object(cap.importlib.util, "spec_from_file_location", return_value=None):
            r = self.run_rows()
        self.assert_retained(r)
        self.assertTrue(r[2])


if __name__ == "__main__":
    unittest.main()
