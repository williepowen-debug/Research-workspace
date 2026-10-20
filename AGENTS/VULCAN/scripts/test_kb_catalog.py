#!/usr/bin/env python3
"""Offline migration/authority regressions; each mutation stays in a fresh sandbox."""
import csv
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from test_validate_workbook import AGENT, build_sandbox
import crwv_library


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.desk = Path(self.temp.name)
        self.validator = build_sandbox(self.desk)
        self.script = self.desk / "scripts/kb_catalog.py"

    def run_catalog(self, *args):
        return subprocess.run([sys.executable, str(self.script), *args],
                              capture_output=True, text=True, cwd=self.desk.parent)

    def table(self, name):
        path = self.desk / name
        with path.open(newline="") as stream:
            reader = csv.DictReader(stream, delimiter="\t")
            return reader.fieldnames, list(reader)

    def save(self, name, fields, rows):
        with (self.desk / name).open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    def test_control_and_legacy_lookup(self):
        self.assertEqual(self.run_catalog("--check").returncode, 0)
        result = self.run_catalog("--find", "KB-VULCAN-243")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["authority"], "CRWV/KB.tsv")

    def test_duplicate_across_authorities_refuses_write(self):
        fields, company = self.table("CRWV/KB.tsv")
        _, general = self.table("workbook/KB_GENERAL.tsv")
        before = (self.desk / "workbook/KB.tsv").read_bytes()
        self.save("workbook/KB_GENERAL.tsv", fields, general + [company[0]])
        result = self.run_catalog("--write")
        self.assertEqual(result.returncode, 2)
        self.assertIn("duplicate authority", result.stderr)
        self.assertEqual(before, (self.desk / "workbook/KB.tsv").read_bytes())

    def test_canonical_correction_requires_regeneration(self):
        fields, company = self.table("CRWV/KB.tsv")
        company[0]["notes"] += " TEST dated correction"
        self.save("CRWV/KB.tsv", fields, company)
        source_bytes = (self.desk / "CRWV/KB.tsv").read_bytes()
        self.assertEqual(self.run_catalog("--check").returncode, 2)
        self.assertEqual(self.run_catalog("--write").returncode, 0)
        self.assertEqual(self.run_catalog("--check").returncode, 0)
        self.assertEqual(source_bytes, (self.desk / "CRWV/KB.tsv").read_bytes())

    def test_manual_legacy_edit_is_detected_and_repaired(self):
        view = self.desk / "workbook/KB.tsv"
        original = view.read_bytes()
        view.write_bytes(original.replace(b"KB-VULCAN-001", b"KB-VULCAN-999", 1))
        self.assertEqual(self.run_catalog("--check").returncode, 2)
        self.assertEqual(self.run_catalog("--write").returncode, 0)
        self.assertEqual(view.read_bytes(), original)

    def test_loss_even_from_both_source_and_view_is_blocked(self):
        fields, company = self.table("CRWV/KB.tsv")
        lost = company.pop()["id"]
        self.save("CRWV/KB.tsv", fields, company)
        _, combined = self.table("workbook/KB.tsv")
        self.save("workbook/KB.tsv", fields, [r for r in combined if r["id"] != lost])
        self.assertEqual(self.run_catalog("--check").returncode, 2)
        self.assertEqual(self.run_catalog("--write").returncode, 2)

    def test_missing_company_source_is_not_silently_empty(self):
        (self.desk / "CRWV/KB.tsv").rename(self.desk / "CRWV/KB.test-backup")
        self.assertEqual(self.run_catalog("--check").returncode, 2)

    def test_ragged_source_row_refuses_write(self):
        with (self.desk / "CRWV/KB.tsv").open("a") as stream:
            stream.write("KB-VULCAN-999\tbroken\n")
        self.assertEqual(self.run_catalog("--write").returncode, 2)

    def test_source_enum_validation_reaches_boot_reader(self):
        fields, company = self.table("CRWV/KB.tsv")
        company[0]["confidence"] = "BANANA"
        self.save("CRWV/KB.tsv", fields, company)
        self.assertEqual(self.run_catalog("--write").returncode, 0)
        result = subprocess.run([sys.executable, str(self.validator), "--ledger", "../CRWV/KB.tsv"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("BANANA", result.stdout)

    def test_new_global_id_and_company_append(self):
        result = self.run_catalog("--next-id")
        self.assertEqual(result.returncode, 0)
        key = result.stdout.strip()
        fields, company = self.table("CRWV/KB.tsv")
        new = dict(company[-1], id=key, notes="TEST new evidence")
        self.save("CRWV/KB.tsv", fields, company + [new])
        self.assertEqual(self.run_catalog("--write").returncode, 0)
        self.assertEqual(self.run_catalog("--check").returncode, 0)
        self.assertEqual(json.loads(self.run_catalog("--find", key).stdout)["row"], new)

    def test_unknown_id_fails(self):
        self.assertEqual(self.run_catalog("--find", "KB-VULCAN-999999").returncode, 2)


class LibraryTests(unittest.TestCase):
    def test_aliases_cover_every_source_once(self):
        output = crwv_library.build()
        catalog = json.loads(output["CATALOG.json"])
        aliases = [a["source"] for entry in catalog["entries"] for a in entry["aliases"]]
        self.assertEqual(len(aliases), catalog["source_copies"])
        self.assertEqual(len(aliases), len(set(aliases)))
        self.assertLess(catalog["reading_entries"], catalog["unique_contents"])
        family = next(e for e in catalog["entries"] if e["key"] == "SIG-W-20260812-010")
        self.assertEqual(len(family["aliases"]), 6)
        self.assertEqual(family["distinct_contents"], 1)

    def test_changed_frozen_copy_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary) / "CRWV"
            shutil.copytree(AGENT / "CRWV", base)
            record = json.loads((base / "MANIFEST.json").read_text())["copied_sources"][0]
            (base / record["copy"]).write_text("TEST corrupted frozen evidence")
            with self.assertRaisesRegex(ValueError, "Frozen copy changed"):
                crwv_library.build(base)


if __name__ == "__main__":
    unittest.main()
