#!/usr/bin/env python3
"""One reading of "is this row still open" — and a query that answers what a brief needs.

Origin, 2026-09-13: PROME prepared a CRUISE spawn brief by filtering DOCKET.tsv with an ad-hoc
`$4 ~ /PENDING/` SUBSTRING match. That matches the word PENDING inside TERMINAL rows' "prior:"
history chains — 77 terminal rows matched — so PROME fabricated an overdue backlog and told a
desk that a ladder Will had RETIRED on 2026-09-03 was "never Will-ratified and overdue". The desk
caught it. Will's disposition: the repair is to USE the shared interpretation when preparing
briefs, because "another annotation explaining the mistake won't prevent another ad-hoc query".

⛔ Every fixture below is a VERBATIM CAPTURE from the live DOCKET.tsv, not a hand-written string
in the canonical form. That is deliberate and is Will's standing requirement for this class: the
brittleness modes that matter are invisible to tidy hand-written fixtures.
"""
import csv
import datetime as dt
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))
sys.path.insert(0, str(ROOT / "scripts"))

import spawn_list          # noqa: E402
import docket_view         # noqa: E402

# --- verbatim captures from PROME/DOCKET.tsv, 2026-09-13 -------------------------------------
TRAP = ("RESOLVED · PENDING — COVERED:HOMER (RAN 8/22 after 8d dark: ★ the ATTOM-recheck half is "
        "RESOLVED-BY-CORRECTION — HOMER's 8/14 'no monthly since May' claim was itself the error")
COVERED_BUT_OWED = ("PENDING — COVERED:FLG spawn required in the ~11/14 window; NO gate registered "
                    "at birth (FERT discipline); scope checkpoint grades SAME sitting, PROME/")


class OneInterpretation(unittest.TestCase):
    def test_spawn_list_does_not_carry_its_own_copy_of_the_rule(self):
        """It used to. Two copies that agree are not one interpretation — they are a divergence
        waiting to happen, and the agreement is what makes it invisible."""
        src = (ROOT / "PROME/tools/spawn_list.py").read_text(encoding="utf-8")
        code = [l for l in src.splitlines() if not l.lstrip().startswith("#")]
        self.assertNotIn("def state_kind", "\n".join(code),
                         "spawn_list must IMPORT state_kind, never define it")
        self.assertIs(spawn_list.state_kind, docket_view.state_kind)

    def test_the_authority_is_reachable_and_not_silently_replaced(self):
        self.assertEqual(docket_view.state_kind.__module__, "docket_view")


class TheSubstringTrap(unittest.TestCase):
    """The exact defect, driven on the captured string that caused it."""

    def test_a_terminal_row_mentioning_PENDING_in_its_history_is_TERMINAL(self):
        self.assertIn("PENDING", TRAP, "fixture must still contain the trap word")
        self.assertEqual(spawn_list.state_kind(TRAP), "TERMINAL")

    def test_the_ad_hoc_substring_query_would_still_get_it_wrong(self):
        """Guard the guard: proves the fixture is a real trap, not a tautology."""
        self.assertIn("PENDING", TRAP)                      # what the bad query tested
        self.assertNotEqual(spawn_list.state_kind(TRAP), "PENDING")   # what is true

    def test_the_live_docket_still_contains_terminal_rows_carrying_the_word(self):
        rows = list(csv.reader((ROOT / "PROME/DOCKET.tsv").open(encoding="utf-8"), delimiter="\t"))
        trapped = [r for r in rows if len(r) > 3 and not r[0].startswith("#")
                   and "PENDING" in r[3] and spawn_list.state_kind(r[3]) == "TERMINAL"]
        self.assertGreater(len(trapped), 10,
                           "if this ever hits zero the trap is gone and so is the lesson")


class OwedIsNotSpawnable(unittest.TestCase):
    """Will 2026-09-13: the repair must distinguish ASSIGNED WORK STILL OWED from work COMPLETED
    OR OTHERWISE DISCHARGED. A COVERED annotation that PROMISES a future spawn is still owed."""

    def test_a_covered_row_promising_a_spawn_is_still_open(self):
        self.assertEqual(spawn_list.state_kind(COVERED_BUT_OWED), "PENDING")

    def test_list_open_does_not_apply_spawn_candidacy_suppression(self):
        text = (ROOT / "PROME/DOCKET.tsv").read_text(encoding="utf-8")
        rows = spawn_list.list_open(text, dt.date(2026, 9, 13))
        covered_open = [r for r in rows if "COVERED" in
                        text.split("\n")[r[0] - 1].split("\t")[3]]
        self.assertTrue(covered_open,
                        "rows whose coverage is a PROMISE must appear in what is still owed")

    def test_a_range_is_due_on_its_END_date_not_its_start(self):
        """The ad-hoc query compared the whole cell as a string, so '2026-08-14..2026-09-30'
        sorted as due. It is not due until 9/30."""
        text = "\t".join(["2026-08-14..2026-09-30", "ranged item", "OWNER", "PENDING", "", ""])
        rows = spawn_list.list_open(text, dt.date(2026, 9, 13))
        self.assertEqual(len(rows), 1)
        self.assertFalse(rows[0][3], "a range ending 9/30 is not due on 9/13")
        self.assertTrue(spawn_list.list_open(text, dt.date(2026, 10, 1))[0][3])

    def test_open_and_terminal_partition_the_live_docket(self):
        text = (ROOT / "PROME/DOCKET.tsv").read_text(encoding="utf-8")
        data = [l for l in text.split("\n") if l.strip() and not l.startswith("#")
                and len(l.split("\t")) >= 4]
        self.assertEqual(len(spawn_list.list_open(text, dt.date(2026, 9, 13)))
                         + sum(1 for l in data if spawn_list.state_kind(l.split("\t")[3]) != "PENDING"),
                         len(data))


if __name__ == "__main__":
    unittest.main(verbosity=2)
