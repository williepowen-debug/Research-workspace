#!/usr/bin/env python3
"""L688 — the broker mirror's two clocks never substitute for each other.

Acceptance: PROME/tools/tests/ACCEPTANCE_L688_broker_asof_2026-10-15.md (A1–A7).
Inline header fixtures (the four header shapes the mirror has actually carried, plus a counterexample);
never the live book except one shape-only smoke test of the --book-line flag.
"""
import datetime as dt
import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1]))
import desk_attention as da  # noqa: E402
import will_brief as wb  # noqa: E402

FIX = HERE.parent / "fixtures" / "desk_attention"   # frozen 2026-09-09 fixture (pre-`marks =` header shape)
TODAY = dt.date.today().isoformat()

MONEY = ("**Fidelity cash (money market):** $18,155.75 (48.42%) · **Fidelity account total:** $37,494.54 "
         "(Today −$616.48). Vs the 10/14 mirror $36,432.23: +$1,062.31.")

# the 10/15 header shape: receipt date + "marks = UNKNOWN clock, 10/15 intraday (...)"
H_TODAY = ("# FORGE\n> ✅ **2026-10-15 (Thu) — RECONCILE** received Thursday 10/15 10:10 ET.\n>\n"
           "> **Updated:** 2026-10-15 = receipt date (10:10 ET) · marks = UNKNOWN clock, 10/15 intraday "
           "(all Fidelity cells `[10/15 rcv]` = `[broker export received 2026-10-15 10:10 ET; capture time UNKNOWN]`) · "
           + MONEY + "\n\n## Thesis\nbody\n")
# the 10/13 shape: "marks = UNKNOWN (...)"
H_1013 = ("> **Updated:** 2026-10-13 = receipt date only · marks = UNKNOWN (all Fidelity cells `[10/13 rcv]`) · "
          + MONEY + "\n\n## Thesis\n")
# the 9/27 shape: a stated marks date with a weekday and a qualifier, DIFFERENT from the receipt date
H_0927 = ("> **Updated:** 2026-09-27 · marks = Fri 2026-09-25 CLOSE `[Fidelity positions 9/25c]` / `[RH card 9/27]` · "
          + MONEY + "\n\n## Thesis\n")
# the 9/3 shape: no marks clause at all
H_0903 = "> **Updated:** 2026-09-03 [Fidelity positions, 9/3 ~15:07 ET intraday] · " + MONEY + "\n\n## Thesis\n"
# counterexample: other dates everywhere, no marks clause in the header, a marks clause in the BODY
H_COUNTER = ("> received Thursday 2026-10-15 10:10 ET; Vs the 10/14 mirror (2026-10-14).\n"
             "> **Updated:** 2026-10-15 · " + MONEY + "\n\n## Fidelity\n| note: marks = 2026-10-14 close |\n")
# a stated date whose clause also says the clock is unknown
H_DATE_UNKNOWN_CLOCK = ("> **Updated:** 2026-10-16 · marks = 2026-10-16 intraday, clock UNKNOWN · " + MONEY + "\n\n## T\n")
# no **Updated:** at all
H_NO_UPDATED = "> marks = 2026-10-14 close · " + MONEY + "\n\n## T\n"
# --- read-1 counterexamples (independent reader, 2026-10-15 17:05 ET) ---
# CX1: a banner sentence ABOVE the Updated line carries an older "marks =" clause; the Updated line says UNKNOWN
H_CX1_BANNER = ("> ✅ RECONCILE (prior marks = 2026-10-14 CLOSE) received 10/15.\n>\n"
                "> **Updated:** 2026-10-15 = receipt date · marks = UNKNOWN clock, 10/15 intraday (cells `[10/15 rcv]`) · "
                + MONEY + "\n\n## T\n")
# the 9/30 header shape (commit 33bc8c293): banner prose "stock marks = the 9/30 CLOSE" before the Updated clause
H_0930 = ("> ✅ **2026-09-30 — RECONCILE**: stock marks = the 9/30 CLOSE per Will's screen.\n>\n"
          "> **Updated:** 2026-09-30 · marks = 2026-09-30 post-close capture · " + MONEY + "\n\n## T\n")
# CX2: a dated clause whose PARENTHETICAL says the clock is unknown (today's shape with a date in front)
H_CX2_PAREN = ("> **Updated:** 2026-10-16 · marks = 2026-10-16 intraday (all Fidelity cells `[10/16 rcv]` = "
               "`[broker export received 2026-10-16 10:10 ET; capture time UNKNOWN]`) · " + MONEY + "\n\n## T\n")
# CX11: the same with a cell tag instead of a parenthetical
H_CX11_TAG = "> **Updated:** 2026-10-16 · marks = 2026-10-16 intraday [capture time UNKNOWN] · " + MONEY + "\n\n## T\n"
# --- read-2 counterexamples (second independent reader, 17:26 ET) ---
R1_BANNER_NAMES_TOKEN = ("> the **Updated:** token below is the receipt date.\n>\n"
                         "> **Updated:** 2026-10-16 · marks = UNKNOWN · " + MONEY + "\n\n## T\n")
R2_DATE_ON_NEXT_LINE = "> **Updated:**\n2026-10-16 · marks = 2026-10-16 close · " + MONEY + "\n\n## T\n"   # the reader's R2 shape: the date on the next physical line
R3_SEPARATOR_INSIDE_PAREN = ("> **Updated:** 2026-10-16 · marks = 2026-10-16 intraday (cells `[10/16 rcv]` · capture time UNKNOWN) · "
                             + MONEY + "\n\n## T\n")
R4_TWO_CLAUSES = ("> **Updated:** 2026-10-16 · (Robinhood marks = 2026-09-29 CLOSE, carried) · Fidelity marks = UNKNOWN clock · "
                  + MONEY + "\n\n## T\n")
R5_LONG_PROSE_THEN_TAG = ("> **Updated:** 2026-10-16 · marks = 2026-10-16 intraday capture taken by Will on the Fidelity positions page "
                          "some time after the regular close of session [capture time UNKNOWN] · " + MONEY + "\n\n## T\n")
R7_REMARKS = "> **Updated:** 2026-10-16 · remarks = 2026-10-14 close noted · " + MONEY + "\n\n## T\n"


class ForgeVintage(unittest.TestCase):
    def test_A1_unknown_clause_reads_unknown_in_the_headers_own_words_never_the_receipt(self):
        receipt, label, known = da.forge_vintage(H_TODAY)
        self.assertEqual(receipt, "2026-10-15")
        self.assertEqual(label, "UNKNOWN clock, 10/15 intraday")
        self.assertFalse(known)
        receipt, label, known = da.forge_vintage(H_1013)
        self.assertEqual((receipt, label, known), ("2026-10-13", "UNKNOWN", False))

    def test_A1_no_clause_reads_unknown_never_receipt_never_today(self):
        for h in (H_0903, H_COUNTER):
            receipt, label, known = da.forge_vintage(h)
            self.assertTrue(label.startswith("UNKNOWN (no marks clause"), label)
            self.assertFalse(known)
            self.assertNotIn(receipt, label)
            self.assertNotIn(TODAY, label)

    def test_A2_stated_marks_date_renders_with_its_qualifier(self):
        self.assertEqual(da.forge_vintage(H_0927), ("2026-09-27", "2026-09-25 close", True))

    def test_A3_overlap_receipt_and_marks_both_render_under_their_own_labels(self):
        money = wb.parse_money(head=H_0927)
        line = wb.book_line(money)
        self.assertIn("broker export received 2026-09-27", line)
        self.assertIn("marks as-of 2026-09-25 close", line)
        self.assertNotIn("marks as-of 2026-09-27", line)
        self.assertEqual(money["vintage"], "2026-09-27")
        self.assertEqual(money["marks"], "2026-09-25 close")

    def test_A3_stale_keys_on_receipt_age_or_unknown_marks(self):
        unknown = wb.parse_money(head=H_TODAY)
        unknown["age"] = 0
        self.assertTrue(wb.book_stale(unknown))                 # unknown marks ⇒ stale even at 0d
        known = wb.parse_money(head=H_0927)
        known["age"] = 0
        self.assertFalse(wb.book_stale(known))
        known["age"] = 5
        self.assertTrue(wb.book_stale(known))
        self.assertFalse(wb.book_stale(dict(known, age=5), days=5))   # the Helm's threshold is injectable

    def test_A4_only_the_header_marks_clause_is_read(self):
        receipt, label, known = da.forge_vintage(H_COUNTER)   # body carries "marks = 2026-10-14 close"
        self.assertEqual(receipt, "2026-10-15")
        self.assertNotIn("2026-10-14", label)
        self.assertFalse(known)
        money = wb.parse_money(head=H_COUNTER.split("\n## ", 1)[0])
        self.assertNotIn("2026-10-14", money["marks"])
        self.assertNotIn("2026-10-15", money["marks"])

    def test_A1_dated_clause_that_declares_an_unknown_clock_stays_unknown(self):
        receipt, label, known = da.forge_vintage(H_DATE_UNKNOWN_CLOCK)
        self.assertEqual(label, "2026-10-16 intraday, clock UNKNOWN")
        self.assertFalse(known)
        for h in (H_CX2_PAREN, H_CX11_TAG):          # read-1 ❌2: UNKNOWN inside the parenthetical / cell tag
            receipt, label, known = da.forge_vintage(h)
            self.assertEqual(label, "2026-10-16 intraday (clock UNKNOWN)", label)
            self.assertFalse(known)
            self.assertTrue(wb.book_stale(dict(wb.parse_money(head=h), age=0)))

    def test_A4_only_the_updated_lines_marks_clause_is_read_never_a_banner(self):
        # read-1 ❌1: a banner "marks =" above the Updated line must never win (it failed toward FRESH)
        receipt, label, known = da.forge_vintage(H_CX1_BANNER)
        self.assertEqual((receipt, label, known), ("2026-10-15", "UNKNOWN clock, 10/15 intraday", False))
        self.assertEqual(da.forge_vintage(H_0930), ("2026-09-30", "2026-09-30 post-close", True))

    def test_read2_one_receipt_reader_fails_loud_never_raises(self):
        # read-2 ❌1: a banner naming the token, or the date on the next line, must fail/parse through forge_vintage — never raise
        r, label, known = da.forge_vintage(R1_BANNER_NAMES_TOKEN)
        self.assertEqual((r, label, known), ("2026-10-16", "UNKNOWN", False))
        self.assertEqual(wb.parse_money(head=R1_BANNER_NAMES_TOKEN)["vintage"], "2026-10-16")
        self.assertEqual(da.forge_vintage(R2_DATE_ON_NEXT_LINE), ("2026-10-16", "2026-10-16 close", True))
        self.assertEqual(wb.parse_money(head=R2_DATE_ON_NEXT_LINE)["marks"], "2026-10-16 close")

    def test_read2_separator_inside_parenthetical_does_not_end_the_clause(self):
        # read-2 ❌2: a " · " nested in the parenthetical must not cut the UNKNOWN off
        r, label, known = da.forge_vintage(R3_SEPARATOR_INSIDE_PAREN)
        self.assertEqual(label, "2026-10-16 intraday (clock UNKNOWN)")
        self.assertFalse(known)
        self.assertTrue(wb.book_stale(dict(wb.parse_money(head=R3_SEPARATOR_INSIDE_PAREN), age=0)))

    def test_read2_label_cap_never_strips_the_unknown_marker(self):
        # read-2 ❌3: a label with marks_known False always carries UNKNOWN, cap or no cap
        r, label, known = da.forge_vintage(R5_LONG_PROSE_THEN_TAG)
        self.assertFalse(known)
        self.assertIn("UNKNOWN", label)
        self.assertLessEqual(len(label), 90)
        self.assertIn("UNKNOWN", wb.book_line(wb.parse_money(head=R5_LONG_PROSE_THEN_TAG)))

    def test_read2_two_clauses_and_remarks_guard(self):
        # read-2 ⚠️4 / ⚠️5: two clauses on the line read UNKNOWN (never the first); "remarks =" is not a clause
        self.assertEqual(da.forge_vintage(R4_TWO_CLAUSES), ("2026-10-16", "UNKNOWN (two marks clauses on the Updated line)", False))
        r, label, known = da.forge_vintage(R7_REMARKS)
        self.assertFalse(known)
        self.assertNotIn("2026-10-14", label)

    def test_read2_one_text_home_for_both_renders(self):
        # read-2 ⚠️7: the HTML book lines and --book-line all render book_vintage_line
        money = wb.parse_money(head=H_0927)
        self.assertTrue(wb.book_line(money).endswith(wb.book_vintage_line(money)))
        src_brief = (HERE.parents[1] / "will_brief.py").read_text(encoding="utf-8")
        src_helm = (HERE.parents[1] / "will_handbook.py").read_text(encoding="utf-8")
        self.assertIn("html.escape(book_vintage_line(money))", src_brief)
        self.assertIn("html.escape(wb.book_vintage_line(money))", src_helm)

    def test_A6_missing_updated_fails_loud_in_will_brief_and_reads_unknown_in_desk_attention(self):
        self.assertEqual(da.forge_vintage(H_NO_UPDATED)[0], "UNKNOWN")
        before = len(wb.failures)
        self.assertIsNone(wb.parse_money(head=H_NO_UPDATED))
        self.assertEqual(len(wb.failures), before + 1)
        wb.failures.pop()

    def test_A1_desk_attention_observation_label_carries_both_clocks(self):
        rows, errors = da.holdings(root=FIX)
        self.assertFalse(errors)
        fid = [r for r in rows if r["account"] == "Fidelity" and "screenshot" not in r["observation"].lower()]
        self.assertTrue(fid)
        for r in fid:
            self.assertTrue(r["observation"].startswith(
                "broker positions received 2026-09-03; marks as-of UNKNOWN (no marks clause"), r["observation"])
            self.assertNotIn("2026-09-03 broker positions", r["observation"])

    def test_A7_book_line_flag_runs_and_names_both_clocks(self):
        # shape-only against the live mirror: never asserts a value, so it cannot rot on the next reconcile
        out = subprocess.run([sys.executable, str(HERE.parents[1] / "will_brief.py"), "--book-line"],
                             capture_output=True, text=True, timeout=60)
        first = out.stdout.strip().splitlines()[0]
        if first.startswith("Book $"):
            self.assertEqual(out.returncode, 0, out.stderr)
            self.assertIn("broker export received ", first)
            self.assertIn("marks as-of ", first)
        else:                                          # read-1 ⚠️6: a failure line exits 1, never pasted as the book
            self.assertTrue(first.startswith("Book: PARSE-FAILED"), first)
            self.assertEqual(out.returncode, 1)


if __name__ == "__main__":
    unittest.main()
