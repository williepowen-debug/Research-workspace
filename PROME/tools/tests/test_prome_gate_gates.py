#!/usr/bin/env python3
"""Discriminating test for prome_gate.scan_gates_rows (Codex audit H1, 2026-08-28):
a LIVE row whose consumed_by is still VALID but whose review_by has PASSED must
flag — and an INSTRUMENT row must land in the blocking bucket. Before 8/28 the
checker read consumed_by only and reported such a row unqualified green.

Run: python3 -m unittest PROME/tools/tests/test_prome_gate_gates.py  (from repo root)
"""
import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import prome_gate  # noqa: E402

TODAY = dt.date(2026, 8, 28)


def row(gate, state="LIVE — x", last_checked="", consumed_by="2026-09-30 | exit | TERRY",
        scannable="INSTRUMENT", review_by=""):
    r = [""] * 12
    r[0], r[5], r[6], r[8], r[9], r[11] = gate, state, last_checked, consumed_by, scannable, review_by
    return r


class ReviewByLeg(unittest.TestCase):
    def test_valid_consumer_but_passed_review_instrument_blocks(self):
        o = prome_gate.scan_gates_rows([row("G-INST", review_by="2026-08-24 CONFIRMED 8/23")], TODAY)
        self.assertEqual(o["stale_live"], [])                       # consumed_by still valid
        self.assertEqual(len(o["review_overdue_instrument"]), 1)    # …and it still flags
        self.assertIn("G-INST review_by 2026-08-24 passed", o["review_overdue_instrument"][0])
        self.assertIn("last_checked BLANK", o["review_overdue_instrument"][0])
        self.assertEqual(o["instrument_unchecked"], ["G-INST"])

    def test_passed_review_judgement_is_advisory_bucket(self):
        o = prome_gate.scan_gates_rows([row("G-JUDG", scannable="JUDGEMENT (re-tagged)",
                                            last_checked="2026-08-23", review_by="2026-08-27 x")], TODAY)
        self.assertEqual(o["review_overdue_instrument"], [])
        self.assertEqual(len(o["review_overdue_judgement"]), 1)
        self.assertEqual(o["instrument_unchecked"], [])

    def test_review_today_or_future_is_quiet(self):
        o = prome_gate.scan_gates_rows([row("G-TODAY", last_checked="2026-08-28", review_by="2026-08-28 today"),
                                        row("G-FUT", last_checked="2026-08-28", review_by="2026-09-04 cadence")], TODAY)
        self.assertEqual(o["review_overdue_instrument"], [])
        self.assertEqual(o["review_overdue_judgement"], [])

    def test_non_live_rows_ignored(self):
        o = prome_gate.scan_gates_rows([row("G-RES", state="RESOLVED(2026-08-01)", review_by="2026-08-01")], TODAY)
        self.assertEqual(sum(len(v) for v in o.values()), 0)


if __name__ == "__main__":
    unittest.main()
