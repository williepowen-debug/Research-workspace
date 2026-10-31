#!/usr/bin/env python3
"""Boot↔closeout symmetry: a boot read counts as registered only by a table row's first
cell or the explicit one-way line (CATO CM1, 2026-10-20, `AGENTS/CATO/runs/2026-10-20_calendar-review.md`).

Every case edits the LIVE BOOT.md / CLOSEOUT.md text in memory and drives the real
`prome_gate.symmetry_missing`. Nothing is reimplemented.

Run: python3 PROME/tools/tests/test_symmetry_registration_2026-10-20.py
"""
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME" / "tools"))
import prome_gate  # noqa: E402

BOOT = (ROOT / "PROME/BOOT.md").read_text()
CLOSE = (ROOT / "PROME/CLOSEOUT.md").read_text()
CAL_ROW = re.compile(r"^\| `PROME/state/CALENDAR\.md` \|.*\n", re.M)


class SymmetryRegistration(unittest.TestCase):
    def test_ordinary_live_documents_pass(self):
        self.assertEqual(prome_gate.symmetry_missing(BOOT, CLOSE), [])

    def test_lowercase_directory_reads_are_harvested(self):
        reads = prome_gate.symmetry_boot_reads(BOOT)
        self.assertIn("PROME/state/CALENDAR.md", reads)
        self.assertIn("PROME/state/SPAWN_SLATE.md", reads)

    def test_removing_only_the_calendar_row_fails(self):
        # CATO CM1: incidental mentions elsewhere (the DOCKET row) stay in place.
        close = CAL_ROW.sub("", CLOSE, count=1)
        self.assertNotEqual(close, CLOSE, "fixture did not remove the row")
        self.assertIn("state/CALENDAR.md", close.split("## Boot↔Closeout symmetry", 1)[1])
        self.assertEqual(prome_gate.symmetry_missing(BOOT, close), ["PROME/state/CALENDAR.md"])

    def test_wrong_owner_same_basename_fails(self):
        close = CLOSE.replace("| `PROME/state/CALENDAR.md` |", "| `AGENTS/BRENT/CALENDAR.md` |", 1)
        self.assertIn("PROME/state/CALENDAR.md", prome_gate.symmetry_missing(BOOT, close))

    def test_comment_mention_does_not_register(self):
        close = CAL_ROW.sub("<!-- TODO CALENDAR.md `PROME/state/CALENDAR.md` -->\n", CLOSE, count=1)
        self.assertEqual(prome_gate.symmetry_missing(BOOT, close), ["PROME/state/CALENDAR.md"])

    def test_one_way_declaration_still_registers(self):
        close = CAL_ROW.sub("", CLOSE, count=1).replace(
            "**Intentionally one-way (no write-back):** ",
            "**Intentionally one-way (no write-back):** `PROME/state/CALENDAR.md` (test) · ", 1)
        self.assertEqual(prome_gate.symmetry_missing(BOOT, close), [])

    def test_removing_a_one_way_entry_fails(self):
        close = CLOSE.replace("`PROME/BOOT_MODULES.md` (boot procedure modules, edited only as canon) · ", "", 1)
        self.assertNotEqual(close, CLOSE)
        self.assertIn("PROME/BOOT_MODULES.md", prome_gate.symmetry_missing(BOOT, close))

    def test_new_boot_read_without_registration_fails(self):
        boot = BOOT.replace("2. **Read `PROME/SCRATCH.md`**", "2. **Read `PROME/state/NEW_SURFACE.md`** then **Read `PROME/SCRATCH.md`**", 1)
        self.assertEqual(prome_gate.symmetry_missing(boot, CLOSE), ["PROME/state/NEW_SURFACE.md"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
