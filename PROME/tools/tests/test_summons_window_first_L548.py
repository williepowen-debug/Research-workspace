#!/usr/bin/env python3
"""Falsification set for DOCKET L548 — the desk-catalyst summons check must never hide the rows it exists to show.

Defect: check_desk_catalyst_summons sorted every flag by date ASCENDING and printed detail_bits[:4] with no
full-output log, so a ledger carrying past-due rows pushed every in-window row into '(+N more)'.
Test list = the acceptance conditions written BEFORE the edit
(AGENTS/DAEDALUS/builds/summons_fix_2026-10-08/ACCEPTANCE.md, AC-a..AC-g), not the bug report.

Frozen fixtures in a tempdir — never the live ledgers. The clock is injected (AC-g).
Rebased 2026-10-14 onto PROME's 10/10 VIOLET registration + EMPTY-FORWARD advisory
(ACCEPTANCE_summons_ledger_VIOLET_empty-forward_2026-10-10.md AC1-AC6): a past-only ledger now
flags EMPTY-FORWARD by that ruling, so the two tests that assumed otherwise were re-cut, and the
TestRebase class covers the merged behaviour.
Run: python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_summons_window_first_L548.py
"""
import datetime as dt
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import prome_gate  # noqa: E402

TODAY = dt.date(2026, 9, 29)
HEADER = "date\tevent\twhat_to_check\tthreshold_signal\tpriority\twho_cares\tnotes\tdate_class\n"
NAME = "desk catalyst summons (BD-02)"


def row(date, event, pri="P1"):
    return f"{date}\t{event}\tcheck\tsignal\t{pri}\tPROME\tnote\tFIXED\n"


class SummonsFixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.logs = self.root / "_logs"
        self.logs.mkdir()
        self._saved = (prome_gate.ROOT, prome_gate.SUMMONS_LEDGERS, prome_gate.LOG_DIR,
                       prome_gate.SUMMONS_WINDOW_DAYS, prome_gate.EMPTY_FORWARD_DAYS)
        prome_gate.ROOT = self.root
        prome_gate.LOG_DIR = self.logs
        prome_gate.SUMMONS_WINDOW_DAYS = 2
        prome_gate.EMPTY_FORWARD_DAYS = 14
        prome_gate.SUMMONS_LEDGERS = {}
        prome_gate.results.clear()
        self.addCleanup(self._restore)

    def _restore(self):
        (prome_gate.ROOT, prome_gate.SUMMONS_LEDGERS, prome_gate.LOG_DIR,
         prome_gate.SUMMONS_WINDOW_DAYS, prome_gate.EMPTY_FORWARD_DAYS) = self._saved
        prome_gate.results.clear()
        self._tmp.cleanup()

    def ledger(self, desk, rows, raw=None):
        rel = f"AGENTS/{desk}/docket/CATALYSTS.tsv"
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(raw if raw is not None else HEADER + "".join(rows), encoding="utf-8")
        prome_gate.SUMMONS_LEDGERS[desk] = rel

    def run_check(self):
        prome_gate.results.clear()
        try:
            prome_gate.check_desk_catalyst_summons(today=TODAY)
        except TypeError:
            # pre-fix signature has no clock: patch date.today via a subclass so the
            # FAILING run still evaluates the defect itself rather than erroring out
            class _D(dt.date):
                @classmethod
                def today(cls):
                    return TODAY
            saved = prome_gate.dt.date
            prome_gate.dt.date = _D
            try:
                prome_gate.check_desk_catalyst_summons()
            finally:
                prome_gate.dt.date = saved
        res = [r for r in prome_gate.results if r[1] == NAME]
        self.assertEqual(len(res), 1)
        return res[0]

    def head(self, detail):
        return detail.split("\n")[0]


class TestWindowFirst(SummonsFixture):
    def test_vulcan_reproduction_25_past_4_window(self):
        """AC-a/AC-b: the 9/29 shape — 25 past-due rows never hide the 4 in-window rows."""
        past = [row((TODAY - dt.timedelta(days=i + 1)).isoformat(), f"old {i}") for i in range(25)]
        window = [row("2026-09-30", f"window {i}") for i in range(4)]
        self.ledger("VULCAN", past + window)
        sev, name, ok, detail, owner = self.run_check()
        head = self.head(detail)
        for i in range(4):
            self.assertIn(f"window {i}", head)
        self.assertIn("VULCAN 25 past-due (oldest 2026-09-04) — owner prunes", head)
        self.assertLess(head.index("window 3"), head.index("past-due"))
        self.assertNotIn("more)", head)
        self.assertNotIn("old 0", head)            # past-due rows are summarized, not listed

    def test_two_desks_interleaved_with_past_due(self):
        """Overlap: LABOR's in-window row is not displaced by VULCAN's rows (9/29 ARGUS r1 ❌2)."""
        self.ledger("LABOR", [row("2026-10-01", "claims"), row("2026-09-01", "labor stale")])
        self.ledger("VULCAN", [row("2026-09-30", f"v{i}") for i in range(4)]
                    + [row("2026-08-28", "v stale"), row("2026-09-04", "v stale2")])
        head = self.head(self.run_check()[3])
        self.assertIn("LABOR 2026-10-01 [P1] claims (in 2d)", head)
        for i in range(4):
            self.assertIn(f"VULCAN 2026-09-30 [P1] v{i} (in 1d)", head)
        self.assertLess(head.index("2026-09-30"), head.index("2026-10-01"))   # window sorted by date
        self.assertIn("LABOR 1 past-due (oldest 2026-09-01) — owner prunes", head)
        self.assertIn("VULCAN 2 past-due (oldest 2026-08-28) — owner prunes", head)
        self.assertLess(head.index("claims"), head.index("past-due"))

    def test_today_and_horizon_rows(self):
        """Ordinary: TODAY flags as TODAY; today+N is in the window; today+N+1 is not."""
        self.ledger("LABOR", [row("2026-09-29", "today row"), row("2026-10-01", "edge row"),
                              row("2026-10-02", "beyond row")])
        sev, name, ok, detail, owner = self.run_check()
        head = self.head(detail)
        self.assertIn("today row (TODAY)", head)
        self.assertIn("edge row (in 2d)", head)
        self.assertNotIn("beyond row", detail)
        self.assertFalse(ok)

    def test_only_past_due(self):
        """Past-only ledger: one past-due bit, and (10/10 VIOLET AC4) EMPTY-FORWARD ahead of it."""
        self.ledger("VULCAN", [row("2026-09-01", "a"), row("2026-09-10", "b")])
        sev, name, ok, detail, owner = self.run_check()
        self.assertFalse(ok)
        self.assertEqual(self.head(detail),
                         "VULCAN ledger EMPTY-FORWARD (no row within 14d) — nothing to summon on; "
                         "the owner's calendar needs rows or the desk goes unwoken"
                         " · VULCAN 2 past-due (oldest 2026-09-01) — owner prunes")

    def test_only_past_due_with_forward_row_beyond_window(self):
        """Past-only inside the 2d window but a row inside 14d: no EMPTY-FORWARD, past-due bit alone."""
        self.ledger("VULCAN", [row("2026-09-01", "a"), row("2026-09-10", "b"), row("2026-10-09", "ahead")])
        sev, name, ok, detail, owner = self.run_check()
        self.assertFalse(ok)
        self.assertEqual(self.head(detail), "VULCAN 2 past-due (oldest 2026-09-01) — owner prunes")

    def test_full_list_written_to_run_log(self):
        """AC-c: every row, untruncated, in a LOG_DIR file named as run_script names its logs."""
        past = [row((TODAY - dt.timedelta(days=i + 1)).isoformat(), f"old {i}") for i in range(25)]
        self.ledger("VULCAN", past + [row("2026-09-30", "win")])
        detail = self.run_check()[3]
        self.assertIn("\n       full output: ", detail)
        log = Path(detail.split("full output: ")[1].strip())
        self.assertEqual(log.parent, self.logs)
        self.assertRegex(log.name, r"^\d{2}-desk-catalyst-summons-bd-02-?\.txt$")
        body = log.read_text(encoding="utf-8")
        for i in range(25):
            self.assertIn(f"old {i}", body)
        self.assertIn("win (in 1d)", body)
        self.assertIn("PAST-DUE 1d — ungraded?", body)

    def test_log_failure_never_loses_the_check(self):
        """AC-c: an unwritable LOG_DIR degrades to a named UNAVAILABLE, the detail still carries the window."""
        prome_gate.LOG_DIR = self.root / "no" / "such" / "dir"
        self.ledger("VULCAN", [row("2026-09-30", "win")])
        sev, name, ok, detail, owner = self.run_check()
        self.assertIn("win (in 1d)", self.head(detail))
        self.assertIn("full output: UNAVAILABLE", detail)


class TestContractUnchanged(SummonsFixture):
    def test_missing_and_unreadable_ledgers_surface(self):
        """AC-d: dead ledgers flag, text unchanged."""
        prome_gate.SUMMONS_LEDGERS["BOGUS"] = "AGENTS/BOGUS/docket/CATALYSTS.tsv"
        self.ledger("BAD", [], raw="date\tevent\tpriority\n2026-09-30\tx\tP1\n")
        (self.root / prome_gate.SUMMONS_LEDGERS["BAD"]).write_bytes(b"\xff\xfe\x00bad")
        sev, name, ok, detail, owner = self.run_check()
        self.assertFalse(ok)
        self.assertIn("BOGUS ledger MISSING (AGENTS/BOGUS/docket/CATALYSTS.tsv)", detail)
        self.assertIn("BAD unreadable: UnicodeDecodeError", detail)

    def test_quiet_case_unchanged(self):
        """AC-f: nothing in window or past-due -> exact legacy quiet detail, no log suffix."""
        self.ledger("LABOR", [row("2026-10-05", "inside 14d, outside 2d")])
        self.ledger("VULCAN", [row("2026-10-13", "exactly at 14d")])
        sev, name, ok, detail, owner = self.run_check()
        self.assertTrue(ok)
        self.assertEqual(detail, "2 desk ledger(s) quiet inside 2d")
        self.assertEqual(list(self.logs.iterdir()), [])

    def test_severity_name_owner_unchanged(self):
        """AC-e: ADVISE, same name, same WQ-184 owner text; the gate rc does not move."""
        self.ledger("VULCAN", [row("2026-09-01", "stale")])
        sev, name, ok, detail, owner = self.run_check()
        self.assertEqual(sev, prome_gate.ADVISE)
        self.assertEqual(name, NAME)
        self.assertTrue(owner.startswith("WQ-184 L0 applies: a due desk-ledger row with a dark owner is a Tier-1 spawn"))
        self.assertTrue(owner.endswith("registry = SUMMONS_LEDGERS above"))
        self.assertEqual(prome_gate.aggregate_rc(prome_gate.results, []), 0)

    def test_undated_rows_skipped_but_counted_in_log(self):
        """Missing information: an undated row is not invented into the detail, and is not silent."""
        self.ledger("LABOR", [row("TBD", "undated event"), row("2026-09-30", "dated")])
        detail = self.run_check()[3]
        self.assertNotIn("undated event", self.head(detail))
        body = Path(detail.split("full output: ")[1].strip()).read_text(encoding="utf-8")
        self.assertIn("LABOR 1 row(s) with no parseable date — skipped", body)

    def test_live_call_sites_take_no_arguments(self):
        """AC-g: both live call sites still call the check bare."""
        src = (Path(prome_gate.__file__)).read_text(encoding="utf-8")
        self.assertEqual(src.count("guard(check_desk_catalyst_summons)"), 2)


VIOLET_HEADER = "date\tevent\ttype\tagent_domain\texpected_vol_impact\tsource\tnotes\n"


class TestRebase(SummonsFixture):
    """The merge of L548 with the 10/10 VIOLET registration + EMPTY-FORWARD branch."""

    def violet(self, rows):
        rel = "AGENTS/VIOLET/workbook/CATALYSTS.tsv"
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(VIOLET_HEADER + "".join(
            f"{d}\t{ev}\tMACRO_DATA\tCARL\t{imp}\tsrc\tnote\n" for d, ev, imp in rows), encoding="utf-8")
        prome_gate.SUMMONS_LEDGERS["VIOLET"] = rel

    def test_cato_reproduction_four_old_vulcan_rows_never_hide_violet(self):
        """CATO 10/10: four older VULCAN rows hid an imminent VIOLET event behind '+1 more'."""
        self.ledger("VULCAN", [row(f"2026-09-2{i}", f"v old {i}") for i in range(4)]
                    + [row("2026-10-08", "keeps vulcan forward")])
        self.violet([("2026-09-30", "imminent VIOLET event", "HIGH")])
        head = self.head(self.run_check()[3])
        self.assertTrue(head.startswith("VIOLET 2026-09-30 [HIGH] imminent VIOLET event (in 1d)"), head)
        self.assertIn("VULCAN 4 past-due (oldest 2026-09-20) — owner prunes", head)
        self.assertNotIn("more)", head)

    def test_violet_schema_impact_fallback_never_question_mark(self):
        """VIOLET AC3: no priority column -> the slot prints expected_vol_impact, never '?'."""
        self.violet([("2026-09-29", "CPI", "LOW")])
        head = self.head(self.run_check()[3])
        self.assertIn("VIOLET 2026-09-29 [LOW] CPI (TODAY)", head)
        self.assertNotIn("[?]", head)

    def test_empty_forward_ordering_and_suppression(self):
        """VIOLET AC4 under the new layout: window rows first, then dead/EMPTY-FORWARD, then past-due;
        a ledger with any row inside 14d does not flag EMPTY-FORWARD; an empty-but-headed ledger does."""
        self.ledger("LABOR", [row("2026-09-30", "claims")])
        self.ledger("VULCAN", [row("2026-09-01", "stale")])
        self.violet([])
        head = self.head(self.run_check()[3])
        bits = head.split(" · ")
        self.assertEqual(bits[0], "LABOR 2026-09-30 [P1] claims (in 1d)")
        self.assertIn("VULCAN ledger EMPTY-FORWARD (no row within 14d)", bits[1])
        self.assertIn("VIOLET ledger EMPTY-FORWARD (no row within 14d)", bits[2])
        self.assertEqual(bits[3], "VULCAN 1 past-due (oldest 2026-09-01) — owner prunes")
        self.assertNotIn("LABOR ledger EMPTY-FORWARD", head)

    def test_empty_forward_in_full_log(self):
        """AC-c covers the new branch: EMPTY-FORWARD lines reach the full log too."""
        self.ledger("VULCAN", [row("2026-09-01", "stale")])
        detail = self.run_check()[3]
        body = Path(detail.split("full output: ")[1].strip()).read_text(encoding="utf-8")
        self.assertIn("VULCAN ledger EMPTY-FORWARD", body)
        self.assertIn("VULCAN 2026-09-01 [P1] stale (PAST-DUE 28d — ungraded?)", body)


if __name__ == "__main__":
    unittest.main()
