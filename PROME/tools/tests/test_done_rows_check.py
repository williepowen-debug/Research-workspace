#!/usr/bin/env python3
"""Tests for PROME/tools/done_rows_check.py — the list is ACCEPTANCE_argus_P1_done-rows_2026-10-10.md (AC1–AC7 as
re-specified after read 1) plus the reader's counterexamples (coldread-wq417-p1, 2026-10-10 17:19 ET), kept as fixtures."""
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))
import done_rows_check as drc  # noqa: E402
import decision_deck as dd      # noqa: E402

FX = ROOT / "PROME/tools/tests/fixtures"
TOOL = str(ROOT / "PROME/tools/done_rows_check.py")
HDR = "wq\tevent\tat\ttitle\ttype\tneeded_by\tsince\tstatus_after\tverdict\twill_verbatim\trec\trecord\tsource\twritten_at\n"
TODAY = "2026-10-10"


def led(*rows):
    return drc.read_ledger(HDR + "".join(rows))


def ev(wq, event, at, status, verdict, verbatim="", written=None):
    """written_at defaults to the event's own date — the grandfather clause keys on written_at, never on `at` (read 2 ❌1)."""
    stamp = (at + " 12:00") if written is None else written          # written="" = an event with NO stamp (fail-closed case)
    return f"{wq}\t{event}\t{at}\tT\t\t\t\t{status}\t{verdict}\t{verbatim}\t\t\tS\t{stamp}\n"


Q = ("## OPEN\n\n| # | Item | Type | Needed by | Since | PROME rec | Notes |\n|---|---|---|---|---|---|---|\n"
     "| 901 | item | RULE | 2026-10-17 | 10/10 | rec | notes |\n\n## RECENTLY DONE (rolls off ~7d)\n")
GOOD = "| **902 X — RULED APPROVE** | Will 2026-10-10, verbatim *\"yes\"* | RULED 2026-10-10 — Will APPROVE, verbatim *\"yes\"* |\n"
GOOD_EV = ev(902, "RULED", TODAY, "RULED", "APPROVE", "yes")


def kinds(f):
    return [(x["kind"], x["wq"]) for x in f]


class TestIndependence(unittest.TestCase):                                  # AC1
    def test_no_shared_parser_import(self):
        import re
        src = (ROOT / "PROME/tools/done_rows_check.py").read_text()
        self.assertIsNone(re.search(r"^\s*(import|from)\s+decision_deck\b", src, re.M))
        self.assertIsNone(re.search(r"^\s*(import|from)\s+wq_ledger\b", src, re.M))

    def test_contract_agreement_with_the_deck(self):
        self.assertEqual(drc.DONE_MIN, dd.DONE_ROW_MIN_CELLS)

    def test_broader_than_the_parser_row316_shape(self):                     # reader ❌1, the historical case
        f, _, _ = drc.scan((FX / "WILL_QUEUE_row316_shape_2026-10-10.md").read_text(), {}, today=TODAY)
        self.assertIn(("UNPARSED", "316"), kinds(f))
        dd.DONE_ROWS_SKIPPED.clear()
        self.assertEqual(dd.parse_done_table((FX / "WILL_QUEUE_row316_shape_2026-10-10.md").read_text().split("## RECENTLY DONE")[1], "fx"), [])

    def test_broader_wq_prefix_indent_empty_number(self):
        q = Q + GOOD + "| **WQ-418 NEW — RULED APPROVE** | d | RULED 2026-10-10 — Will APPROVE |\n"
        self.assertIn(("UNPARSED", "418"), kinds(drc.scan(q, led(GOOD_EV), today=TODAY)[0]))
        q = Q + GOOD + "  | **419 NEW — RULED APPROVE** | d | RULED 2026-10-10 — Will APPROVE |\n"
        self.assertIn(("UNPARSED", "419"), kinds(drc.scan(q, led(GOOD_EV), today=TODAY)[0]))
        q = Q + GOOD + "| | **420 NEW — RULED APPROVE** | d | RULED |\n"
        self.assertIn(("UNPARSED", "420"), kinds(drc.scan(q, led(GOOD_EV), today=TODAY)[0]))

    def test_orphan_ruling_outside_a_row(self):
        q = Q + GOOD + "RULED 2026-10-10 — Will APPROVE the thing (written as prose, no row)\n"
        self.assertIn("ORPHAN-RULING", [k for k, _ in kinds(drc.scan(q, led(GOOD_EV), today=TODAY)[0])])

    def test_heading_case_and_duplicate_section(self):
        q = Q.replace("## RECENTLY DONE (rolls off ~7d)", "## Recently Done") + GOOD
        with self.assertRaises(ValueError):                                   # the exact heading is absent → rc 2 …
            drc.scan(q, led(GOOD_EV), today=TODAY)
        q = Q + GOOD + "\n## RECENTLY DONE (again)\n| **903 Y — RULED APPROVE** | d | RULED 2026-10-10 — Will APPROVE |\n"
        f, _, _ = drc.scan(q, led(GOOD_EV, ev(903, "RULED", TODAY, "RULED", "APPROVE")), today=TODAY)
        self.assertIn("DUPLICATE-SECTION", [k for k, _ in kinds(f)])          # … and a second block is a finding
        self.assertNotIn(("NO-LEDGER-EVENT", "903"), kinds(f))                # rows of the second block are NOT read (as the Deck)

    def test_open_heading_required(self):
        with self.assertRaises(ValueError):
            drc.scan(Q.replace("## OPEN", "## ⚖️ OPEN") + GOOD, led(GOOD_EV), today=TODAY)


class TestOriginalRowIsCaught(unittest.TestCase):                           # AC2
    def test_fixture_flags_short_and_no_event(self):
        f, _, _ = drc.scan((FX / "WILL_QUEUE_2cell_416_2026-10-10.md").read_text(), drc.read_ledger((FX / "WQ_LEDGER_no416_2026-10-10.tsv").read_text()), today=TODAY)
        self.assertIn(("SHORT", "416"), kinds(f))
        self.assertIn(("NO-LEDGER-EVENT", "416"), kinds(f))
        self.assertEqual([x for x in f if x["wq"] == "902"], [])

    def test_deck_parser_disagrees_and_names_it(self):                       # AC4
        done = (FX / "WILL_QUEUE_2cell_416_2026-10-10.md").read_text().split("## RECENTLY DONE")[1]
        dd.DONE_ROWS_SKIPPED.clear()
        ns = {r["n"] for r in dd.parse_done_table(done, "fx")}
        self.assertNotIn("416", ns)
        self.assertIn("902", ns)
        self.assertEqual([s["n"] for s in dd.DONE_ROWS_SKIPPED], ["416"])

    def test_cli_rc1_on_fixture(self):
        r = subprocess.run([sys.executable, TOOL, "--queue", str(FX / "WILL_QUEUE_2cell_416_2026-10-10.md"), "--ledger", str(FX / "WQ_LEDGER_no416_2026-10-10.tsv"), "--no-archives"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("WQ-416 SHORT", r.stdout)
        self.assertIn("WQ-416 NO-LEDGER-EVENT", r.stdout)


class TestRepairedFormReachesBoth(unittest.TestCase):                        # AC3 — durable fixture, not live rows (reader ⚠️8)
    def test_repaired_415_416(self):
        q = (FX / "WILL_QUEUE_repaired_415_416_2026-10-10.md").read_text()
        f, _, _ = drc.scan(q, drc.read_ledger((FX / "WQ_LEDGER_415_416_2026-10-10.tsv").read_text()), today=TODAY)
        self.assertEqual([x for x in f if x["wq"] in ("415", "416")], [], f)
        ns = {r["n"] for r in dd.parse_done_table(q.split("## RECENTLY DONE")[1], "fx")}
        self.assertTrue({"415", "416"} <= ns)


class TestTerminalRulingVerbatim(unittest.TestCase):                        # AC5
    def test_last_state_not_terminal(self):                                   # reader ⚠️1
        f, _, _ = drc.scan(Q + GOOD, led(ev(902, "RULED", TODAY, "RULED", "APPROVE", "yes"), ev(902, "UPDATED", TODAY, "OPEN", "—")), today=TODAY)
        self.assertEqual(kinds(f), [("NOT-TERMINAL", "902")])

    def test_verdict_dash_blocks_recent_ruling_rows_only(self):
        row = "| **902 X — RULED APPROVE** | Will 2026-10-10 | Owner encode = the charter |\n"
        f, w, _ = drc.scan(Q + row, led(ev(902, "REGISTERED", TODAY, "CLOSED", "—")), today=TODAY)
        self.assertIn(("VERDICT-DASH", "902"), kinds(f))                                       # ruling-class, recent → ❌
        f, w, _ = drc.scan(Q + row, led(ev(902, "REGISTERED", "2026-10-04", "CLOSED", "—")), today=TODAY)
        self.assertEqual(f, []); self.assertIn(("VERDICT-DASH", "902"), kinds(w))                # grandfathered → ⚠️
        row2 = "| **902 X — housekeeping done** | PROME 2026-10-10 | Owner encode = the charter |\n"
        f, w, _ = drc.scan(Q + row2, led(ev(902, "REGISTERED", TODAY, "CLOSED", "—")), today=TODAY)
        self.assertEqual(f, []); self.assertIn(("VERDICT-DASH", "902"), kinds(w))                # not a ruling row → ⚠️

    def test_verbatim_lost(self):
        row = "| **902 X — RULED APPROVE** | Will 2026-10-10, verbatim *\"yes\"* | RULED 2026-10-10 — Will APPROVE |\n"
        f, _, _ = drc.scan(Q + row, led(ev(902, "RULED", TODAY, "RULED", "APPROVE", "")), today=TODAY)
        self.assertIn(("VERBATIM-LOST", "902"), kinds(f))
        f, _, _ = drc.scan(Q + row, led(ev(902, "RULED", TODAY, "RULED", "APPROVE", "yes")), today=TODAY)
        self.assertEqual(f, [])

    def test_original_416_plus_empty_trailing_cell(self):                     # reader ❌2 counterexample
        row = (FX / "WILL_QUEUE_2cell_416_2026-10-10.md").read_text().split("## RECENTLY DONE")[1].split("\n")[1].rstrip() + " |\n"
        self.assertEqual(row.count("|"), 4)
        f, _, _ = drc.scan(Q + row, led(ev(416, "REGISTERED", TODAY, "CLOSED", "—", "")), today=TODAY)
        self.assertIn(("VERDICT-DASH", "416"), kinds(f))
        self.assertIn(("VERBATIM-LOST", "416"), kinds(f))

    def test_pipe_in_code_span_shifts_cells(self):                            # reader ❌2 / ⚠️3
        row = "| **902 X — RULED APPROVE (`a|b`)** | Will 2026-10-10 | RULED 2026-10-10 — Will APPROVE |\n"
        f, _, _ = drc.scan(Q + row, led(ev(902, "REGISTERED", TODAY, "CLOSED", "—")), today=TODAY)
        self.assertIn(("OVER-DONE", "902"), kinds(f))

    def test_new_ruling_with_an_old_pointer_date_is_not_grandfathered(self):   # read 2 ❌1 (counterexample N8)
        row = "| **902 X — RULED APPROVE** | PROME/proposals/2026-10-08_x-RULED.md, Will 10/14, verbatim *\"go\"* | pointer only |\n"
        f, w, _ = drc.scan(Q + row, led(ev(902, "REGISTERED", "2026-10-08", "CLOSED", "—", "", written="2026-10-14 09:00")), today="2026-10-14")
        self.assertIn(("VERDICT-DASH", "902"), kinds(f)); self.assertIn(("VERBATIM-LOST", "902"), kinds(f))
        f, w, _ = drc.scan(Q + row, led(ev(902, "REGISTERED", "2026-10-08", "CLOSED", "—", "", written="2026-10-09 09:00")), today="2026-10-14")
        self.assertEqual(f, []); self.assertIn(("VERDICT-DASH", "902"), kinds(w))                      # written before the repair → ⚠️
        f, w, _ = drc.scan(Q + row, led(ev(902, "REGISTERED", "2026-10-08", "CLOSED", "—", "", written="")), today="2026-10-14")
        self.assertIn(("VERDICT-DASH", "902"), kinds(f))                                                # no written_at → fail closed

    def test_ruling_row_under_another_heading(self):                           # read 2 ❌2 (counterexample N7)
        q = Q + GOOD + "\n## DECIDED TODAY\n| **903 Y — RULED APPROVE** | d | RULED 2026-10-10 — Will APPROVE |\n"
        f, _, _ = drc.scan(q, led(GOOD_EV), today=TODAY)
        self.assertIn(("ROW-OUTSIDE-SECTIONS", "903"), kinds(f))
        q = Q + GOOD + "\n## NOTES\n| Item | Count |\n|---|---|\n| packets | 12 |\n"                      # a plain table, no ruling word → nothing
        self.assertEqual(drc.scan(q, led(GOOD_EV), today=TODAY)[0], [])

    def test_date_future_is_advisory(self):
        f, w, _ = drc.scan(Q + GOOD, led(ev(902, "REGISTERED", "2027-05-01", "CLOSED", "—"), GOOD_EV), today=TODAY)
        self.assertEqual(f, [])
        self.assertIn(("DATE-FUTURE", "902"), kinds(w))


class TestArchives(unittest.TestCase):                                        # AC1 archives (CATO's letter)
    def test_legacy_unnumbered_rows_counted_not_flagged(self):
        arch = {"A.md": "| Item | Done | Record |\n|---|---|---|\n| — root rule-6 mirror | 8/23 | **APPROVED** |\n| **310 OLD — RULED** | d | RULED 2026-09-01 — Will APPROVE |\n"}
        f, w, s = drc.scan(Q + GOOD, led(GOOD_EV, ev(310, "RULED", "2026-09-01", "RULED", "APPROVE")), today=TODAY, archives=arch)
        self.assertEqual(f, []); self.assertEqual((s["archive_rows"], s["archive_legacy_rows"]), (1, 1))

    def test_archive_short_and_unparsed(self):
        arch = {"A.md": "| Item | Done | Record |\n|---|---|---|\n| **311 OLD — RULED** | d |\n| | **316 OLD** | d | r |\n"}
        f, _, _ = drc.scan(Q + GOOD, led(GOOD_EV), today=TODAY, archives=arch)
        self.assertIn(("SHORT-ARCHIVE", "311"), kinds(f)); self.assertIn(("UNPARSED-ARCHIVE", "316"), kinds(f))
        self.assertTrue(all(x["file"] == "A.md" for x in f))


class TestNeighbours(unittest.TestCase):
    def test_ordinary_clean(self):
        f, w, s = drc.scan(Q + GOOD, led(ev(901, "REGISTERED", TODAY, "OPEN", "—"), GOOD_EV), today=TODAY)
        self.assertEqual((f, w), ([], []))
        self.assertEqual((s["open_rows"], s["done_rows"], s["open_width"]), (1, 1, 7))

    def test_overlap_number_in_both_sections(self):
        q = Q + "| **901 X — RULED APPROVE** | d | RULED 2026-10-10 — Will APPROVE |\n"
        self.assertIn("DUPLICATE", [k for k, _ in kinds(drc.scan(q, led(ev(901, "RULED", TODAY, "RULED", "APPROVE")), today=TODAY)[0])])

    def test_short_and_unparsed_open_rows(self):
        q = Q.replace("| 901 | item | RULE | 2026-10-17 | 10/10 | rec | notes |", "| 901 | item | RULE | 2026-10-17 |\n| WQ-905 | item | RULE | d | s | r | n |") + GOOD
        f, _, _ = drc.scan(q, led(GOOD_EV), today=TODAY)
        self.assertIn(("SHORT-OPEN", "901"), kinds(f)); self.assertIn(("UNPARSED-OPEN", "905"), kinds(f))

    def test_missing_information_rc2(self):
        r = subprocess.run([sys.executable, TOOL, "--ledger", "/nonexistent.tsv"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)

    def test_quiet_mode_prints_advisory_summary(self):                        # reader ⚠️6
        q = FX / "WILL_QUEUE_repaired_415_416_2026-10-10.md"
        r = subprocess.run([sys.executable, TOOL, "--queue", str(q), "--ledger", str(FX / "WQ_LEDGER_415_416_2026-10-10.tsv"), "--quiet", "--no-archives"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("advisories:", r.stdout)                                 # the 415 REGISTERED 2027-05-01 event → DATE-FUTURE


if __name__ == "__main__":
    unittest.main()
