#!/usr/bin/env python3
"""WQ-578 batch 2 (Will 2026-10-31 15:57 ET "Okay approved go ahead"; DOCKET L908) — the three behaviours the batch
ADDS rather than removes: W4 (a malformed ⏰ marker on a HANDS row is flagged, never silent), #13–15 (one GATES upkeep
line that keeps each flag's own label) and #32 (one spawn line that says whether the slate was regenerated).

Run: python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_wq578_batch2.py   (from repo root)
"""
import datetime as dt
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1]))          # PROME/tools
import prome_gate as gate  # noqa: E402

TODAY = dt.date.today()
PAST, FUTURE = (TODAY - dt.timedelta(days=1)).isoformat(), (TODAY + dt.timedelta(days=30)).isoformat()


def queue(rows):
    return (f"# WILL_QUEUE (fixture)\n**Last reconciled:** {TODAY.isoformat()}\n\n"
            "## OPEN\n| # | Item | Type | Needed by | Since | PROME rec | Notes |\n"
            "|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")


class HandsMarker(unittest.TestCase):
    """W4: parse-or-flag. Five neighbour categories: ordinary (canonical marker) · overlap (a DECISION row with a ⏰ in
    its rec cell is outside the HANDS rule) · wrong place (⏰ in the rec cell of a HANDS row) · missing information
    (M/D date, no date, impossible date) · concurrent activity N/A — a pure read of one file."""

    def problems(self, rows):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "PROME").mkdir()
            (Path(td) / "PROME/WILL_QUEUE.md").write_text(queue(rows), encoding="utf-8")
            with patch.object(gate, "ROOT", Path(td)), patch.object(gate, "results", []):
                gate.check_will_queue()
                return list(gate.check_will_queue.last_problems)

    def hands(self, n, rec="rec", notes="notes"):
        return f"| {n} | **Your hands: an errand** | HANDS | {PAST} | 10/1 | {rec} | {notes} |"

    def test_canonical_due_marker_re_presents(self):
        p = self.problems([self.hands(1, notes=f"⏰ re-present {PAST}")])
        self.assertTrue(any(x.startswith("RE-PRESENT #1") for x in p), p)
        self.assertFalse(any("MALFORMED" in x for x in p), p)

    def test_future_marker_and_no_marker_are_silent(self):
        p = self.problems([self.hands(2, notes=f"⏰ re-present {FUTURE}"), self.hands(3)])
        self.assertEqual([x for x in p if "#2" in x or "#3" in x], [], p)   # a passed needed-by never triggers (WQ-538 A)

    def test_colon_form_parses(self):
        p = self.problems([self.hands(4, notes=f"⏰ re-present: {PAST}")])
        self.assertTrue(any(x.startswith("RE-PRESENT #4") for x in p), p)

    def test_marker_in_rec_cell_is_flagged(self):
        p = self.problems([self.hands(5, rec=f"⏰ re-present {PAST}")])
        self.assertTrue(any(x.startswith("MALFORMED ⏰ #5") for x in p), p)

    def test_md_date_and_missing_date_are_flagged(self):
        p = self.problems([self.hands(6, notes="⏰ re-present 11/1"), self.hands(7, notes="⏰ re-present soon")])
        self.assertTrue(any(x.startswith("MALFORMED ⏰ #6") for x in p), p)
        self.assertTrue(any(x.startswith("MALFORMED ⏰ #7") for x in p), p)

    def test_emoji_form_parses_and_a_bare_clock_is_not_a_marker(self):
        # batch-2 review ⚠️ W8: emoji pickers type U+23F0 U+FE0F; a ⏰ with no "re-present" after it is prose, not a marker
        p = self.problems([self.hands(10, notes=f"⏰\ufe0f re-present {PAST}"),
                           self.hands(11, notes="see the ⏰ in the card"), self.hands(12, rec="https://x.example/⏰")])
        self.assertTrue(any(x.startswith("RE-PRESENT #10") for x in p), p)
        self.assertFalse(any("MALFORMED" in x for x in p), p)

    def test_impossible_date_is_named(self):
        p = self.problems([self.hands(8, notes="⏰ re-present 2026-02-30")])
        self.assertTrue(any(x.startswith("IMPOSSIBLE DATE #8") for x in p), p)

    def test_decision_row_rec_marker_is_outside_the_hands_rule(self):
        row = f"| 9 | Decide a thing | DECISION | {FUTURE} | 10/30 | rec ⏰ re-present {FUTURE} | notes |"
        self.assertFalse(any("MALFORMED" in x for x in self.problems([row])))


def gates_row(gate_id, state="LIVE — x", last_checked="2026-10-30", consumed_by="2030-01-01 | exit | TERRY",
              scannable="JUDGEMENT", review_by="2030-01-01"):
    r = [""] * 12
    r[0], r[5], r[6], r[8], r[9], r[11] = gate_id, state, last_checked, consumed_by, scannable, review_by
    return r


class GatesUpkeep(unittest.TestCase):
    def run_check(self, rows):
        hdr = ["gate_id", "a", "b", "condition", "c", "state", "last_checked", "d", "consumed_by", "scannable",
               "definition_surface", "review_by"]
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "PROME").mkdir()
            (Path(td) / "PROME/GATES.tsv").write_text("\n".join("\t".join(r) for r in [hdr] + rows) + "\n",
                                                      encoding="utf-8")
            with patch.object(gate, "ROOT", Path(td)), patch.object(gate, "results", []), \
                 patch.object(gate, "record_gate_citability"):
                gate.check_gates_tsv()
                return {name: (sev, ok, detail) for sev, name, ok, detail, _owner in gate.results}

    def test_three_advisories_print_as_one_labelled_line(self):
        out = self.run_check([gates_row("G-CONS", consumed_by="2020-01-01 | x"),
                              gates_row("G-JUDG", review_by="2020-01-01"),
                              gates_row("G-INST", scannable="INSTRUMENT", last_checked="")])
        upkeep = [k for k in out if k.startswith("GATES upkeep")]
        self.assertEqual(len(upkeep), 1, list(out))
        sev, ok, detail = out[upkeep[0]]
        self.assertEqual((sev, ok), (gate.ADVISE, False))
        for label, gid in (("consumer:", "G-CONS"), ("JUDGEMENT review:", "G-JUDG"), ("INSTRUMENT last_checked BLANK:", "G-INST")):
            self.assertIn(f"{label} {gid}", detail)
        for retired in ("GATES consumed_by (consumer passed / cell empty)", "GATES review_by passed — LIVE JUDGEMENT rows",
                        "GATES last_checked blank on LIVE INSTRUMENT rows"):
            self.assertNotIn(retired, out)

    def test_blocking_lines_unchanged(self):
        out = self.run_check([gates_row("G-FIRED", state="FIRED-UNEXECUTED — x"),
                              gates_row("G-LATE", scannable="INSTRUMENT", review_by="2020-01-01")])
        self.assertEqual(out["GATES fired-unexecuted"][:2], (gate.BLOCK, False))
        self.assertEqual(out["GATES review_by passed — LIVE INSTRUMENT rows"][:2], (gate.BLOCK, False))

    def test_clean_registry_passes(self):
        out = self.run_check([gates_row("G-OK")])
        self.assertTrue(next(v for k, v in out.items() if k.startswith("GATES upkeep"))[1])


class SpawnLine(unittest.TestCase):
    LIST = "spawn_list · as-of 2026-10-31 · horizon +0d · 1 row(s): DARK 1 · ACTIVE 0\nD:L1\t2026-10-31\t0\tSAM\tDARK\tb\tc\td\n"

    WROTE = "spawn_slate · as-of 2026-10-31 · horizon +0d · 1 row(s) → PROME/state/SPAWN_SLATE.md (4,000 B, 13% of budget)\n"
    BANNER = "spawn_slate · ⛔ FAILED (OSError) — banner written to PROME/state/SPAWN_SLATE.md; use spawn_list.py\n"

    def run_line(self, slate_rc, list_body=None, list_rc=0, slate_out=None, slate_file="# SPAWN SLATE\ncensus rows 1 · OK\n"):
        recorded = []
        with tempfile.TemporaryDirectory() as td, patch.object(gate, "LOG_DIR", Path(td) / "logs"), \
             patch.object(gate, "ROOT", Path(td)), patch.object(gate, "results", []):
            (Path(td) / "logs").mkdir()
            (Path(td) / "PROME/state").mkdir(parents=True)
            if slate_file is not None:
                (Path(td) / "PROME/state/SPAWN_SLATE.md").write_text(slate_file, encoding="utf-8")
            def fake_run(cmd, **kw):
                body = list_body if list_body is not None else self.LIST
                is_slate = "PROME/tools/spawn_slate.py" in cmd
                kw["stdout"].write((self.WROTE if slate_out is None else slate_out) if is_slate else body)
                return type("P", (), {"returncode": slate_rc if is_slate else list_rc})()
            with patch.object(gate.subprocess, "run", side_effect=fake_run):
                gate.spawn_list_and_slate("0", "spawn list fixture", "owner")
            recorded = list(gate.results)
        self.assertEqual(len(recorded), 1)    # ONE line, success or failure
        _sev, _name, ok, detail, _owner = recorded[0]
        return ok, detail

    def test_success_names_the_regenerated_slate(self):
        ok, detail = self.run_line(0)
        self.assertTrue(ok)
        self.assertIn("DARK: D:L1 SAM", detail)
        self.assertIn("slate PROME/state/SPAWN_SLATE.md regenerated", detail)

    def test_dark_or_unknown_rc_after_a_write_still_reads_regenerated(self):
        # ❌ X1 (batch-2 review): spawn_slate exits 1 on a DARK row and 2 on an UNKNOWN row AFTER writing the slate
        for rc in (1, 2):
            with self.subTest(rc=rc):
                ok, detail = self.run_line(rc, list_rc=1)
                self.assertFalse(ok)                      # a DARK row is itself a flag (act on it)
                self.assertIn("slate PROME/state/SPAWN_SLATE.md regenerated", detail)
                self.assertNotIn("NOT regenerated", detail)

    def test_failed_banner_or_no_write_line_is_loud_on_the_same_line(self):
        for out in (self.BANNER, "Traceback (most recent call last):\nOSError\n"):
            with self.subTest(out=out[:20]):
                ok, detail = self.run_line(2, slate_out=out)
                self.assertFalse(ok)
                self.assertIn("slate NOT regenerated (spawn_slate.py rc=2", detail)

    def test_conservation_failed_slate_is_named_incomplete(self):
        ok, detail = self.run_line(2, slate_file="> ⛔ **SLATE INCOMPLETE — conservation FAILED** (3 rows in ≠ …)\n")
        self.assertFalse(ok)
        self.assertIn("INCOMPLETE: conservation FAILED", detail)

    def test_unreadable_list_keeps_the_slate_status(self):
        ok, detail = self.run_line(0, list_body="garbage\n")
        self.assertFalse(ok)
        self.assertIn("UNKNOWN", detail)
        self.assertIn("slate PROME/state/SPAWN_SLATE.md regenerated", detail)


if __name__ == "__main__":
    unittest.main()
