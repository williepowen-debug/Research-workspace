"""spawn_list coverage() redesign — DOCKET L368 (acceptance ACCEPTANCE_spawn_list_covered_L368_2026-10-30.md).
Run: python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_spawn_list_covered_L368.py
Synthetic cells for A1–A5 plus the PINNED excerpt of the live DOCKET (22 suppressed + 3 control rows at 2026-10-30)
under fixtures/spawn_list_covered_L368/. Condition letters in test names are the acceptance file's."""
import datetime as dt, pathlib, sys, unittest

REAL = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REAL / "PROME" / "tools"))
import spawn_list as S  # noqa: E402

TODAY = dt.date(2026, 10, 30)
FIX = REAL / "PROME/tools/tests/fixtures/spawn_list_covered_L368/DOCKET_2026-10-30_excerpt.tsv"


def _fixture_rows():
    out = {}
    for line in FIX.read_text(encoding="utf-8").split("\n"):
        if not line or line.startswith("#") or line.startswith("src_line"):
            continue
        c = line.split("\t")
        out[int(c[0])] = c[1:]
    return out


def _sup(state, notes="", today=TODAY):
    return S.coverage(state, notes, today)


class A1_token_form(unittest.TestCase):
    def test_recovered_is_prose(self):
        s, r, _ = _sup("PENDING · RE-DATED — script recovered from the transcript")
        self.assertFalse(s); self.assertEqual(r, "NOT-AN-ANNOTATION")

    def test_lowercase_covered_by_is_prose(self):
        s, r, _ = _sup("PENDING — its phrases are covered by CREED's rows")
        self.assertFalse(s); self.assertEqual(r, "NOT-AN-ANNOTATION")

    def test_uppercase_without_colon_is_prose(self):
        s, _, _ = _sup("PENDING — the row is COVERED only in spirit")
        self.assertFalse(s)

    def test_quoted_form_is_prose_about_the_form(self):
        # L368's own cell: "needs the literal `COVERED:` but house style writes `COVERED <date>:`" — a mention, not an annotation
        self.assertFalse(_sup("PENDING — it needs the literal `COVERED:` but house style writes `COVERED <date> <time>:`")[0])

    def test_form_colon_and_paren_both_count(self):
        self.assertTrue(_sup("PENDING · COVERED: BOND holds the standing carrier")[0])
        self.assertTrue(_sup("PENDING · COVERED (PROME 2026-09-04 19:5x): PRE-FETCHED")[0])


class A2_negation(unittest.TestCase):
    def test_not_covered(self):
        s, r, _ = _sup("PENDING · Not COVERED, not re-dated: the date stands")
        self.assertFalse(s); self.assertIn(r, ("NOT-AN-ANNOTATION", "NEGATED"))

    def test_NOT_COVERED_colon(self):
        s, r, _ = _sup("PENDING NOT COVERED: still owed")
        self.assertFalse(s); self.assertEqual(r, "NEGATED")

    def test_uncovered(self):
        self.assertFalse(_sup("PENDING · UNCOVERED: nobody holds it")[0])


class A3_self_slate(unittest.TestCase):
    def test_legacy_order_prome_then_spawn(self):
        s, r, _ = _sup("PENDING · COVERED: PROME 9/11 boot slate ③ — WATT L0 spawn (SLATED at the closeout)")
        self.assertFalse(s); self.assertEqual(r, "SELF-SLATE")

    def test_reverse_order_slated_then_prome(self):
        s, r, _ = _sup("PENDING · COVERED: HANS (owner, DARK) is slated for a Tier-1 WQ-184 wake at the first PROME boot on/after today")
        self.assertFalse(s); self.assertEqual(r, "SELF-SLATE")

    def test_prome_spawns_wording(self):
        self.assertFalse(_sup("PENDING · COVERED: L0 due-row spawn — PROME spawns at the next boot")[0])

    def test_wills_slate_from_prome_report(self):
        self.assertFalse(_sup("PENDING · COVERED: on Will's slate from the 10/29 morning boot report (DAEDALUS not woken, cap 8 reached; PROME re-presents)")[0])

    def test_other_desk_slate_without_prome_still_covers(self):
        # a desk slating ITS OWN work is coverage, not PROME's job
        self.assertTrue(_sup("PENDING · COVERED: WALTER — its own design; lands at WALTER's dated wake")[0])

    def test_bare_slate_word_and_stamp_do_not_collide(self):
        # L198 class: "calendar spawn suppressed" + an annotation stamp "by PROME" is coverage, not a self-slate
        s, r, _ = _sup("PENDING · COVERED:BRENT publication-event wait; calendar spawn suppressed. reconciled 2026-09-14 by PROME (prome-xx)")
        self.assertTrue(s); self.assertEqual(r, "COVERED")


class A4_lapsed_promise(unittest.TestCase):
    CELL = "PENDING · re-dated 2026-09-26→2026-10-25; COVERED:PROME-R1-review-sitting-2026-10-25 — M1 re-spec; batched to the 10/25 review sitting"

    def test_sitting_date_past_is_visible(self):
        s, r, _ = _sup(self.CELL, today=dt.date(2026, 10, 30))
        self.assertFalse(s); self.assertEqual(r, "LAPSED 2026-10-25")

    def test_sitting_date_future_still_suppresses(self):
        self.assertTrue(_sup(self.CELL, today=dt.date(2026, 10, 24))[0])

    def test_until_md_form(self):
        s, r, _ = _sup("PENDING · COVERED: YURI holds the window until 10/31", today=dt.date(2026, 11, 2))
        self.assertFalse(s); self.assertTrue(r.startswith("LAPSED"))
        self.assertTrue(_sup("PENDING · COVERED: YURI holds the window until 10/31", today=dt.date(2026, 10, 30))[0])

    def test_stamp_in_ET_parenthetical_is_not_a_promise(self):
        s, _, _ = _sup("PENDING · COVERED: FLG holds the 10-Q leg of the window (2026-10-29 10:2x ET, PROME prome-90)", today=dt.date(2026, 10, 30))
        self.assertTrue(s)


class A5_legitimate_coverage_and_fixture(unittest.TestCase):
    def test_fixture_rows(self):
        rows = _fixture_rows()
        visible = {800: "NOT-AN-ANNOTATION", 565: "NOT-AN-ANNOTATION", 734: "NOT-AN-ANNOTATION", 812: None,   # L812 carries a form-valid COVERED: clause naming PROME's wake elsewhere in the cell — visible either way
                   40: None, 263: None, 317: "SELF-SLATE", 490: "SELF-SLATE", 630: "SELF-SLATE",
                   440: "LAPSED 2026-10-25", 445: "LAPSED 2026-10-25",
                   517: "SELF-SLATE", 334: "SELF-SLATE"}   # L334: 'SLATED tonight, cap of 4 met' — PROME's closeout slate   # 'the hearing is read at the first PROME boot' — PROME's own read, the 9/11 class; wrongly listed as legitimate coverage in the acceptance draft
        suppressed = {52, 140, 198, 264, 265, 406, 432, 522, 729, 793, 150}
        for n, want in visible.items():
            s, r, cl = S.coverage(rows[n][3], rows[n][5], TODAY)
            self.assertFalse(s, f"L{n} must be visible; got {r}: {cl[:80]}")
            if want:
                self.assertEqual(r, want, f"L{n} reason")
        for n in suppressed:
            s, r, cl = S.coverage(rows[n][3], rows[n][5], TODAY)
            self.assertTrue(s, f"L{n} must stay suppressed; got {r}: {cl[:80]}")
        for n in (764, 795, 871):   # controls: no COVERED anywhere
            self.assertEqual(S.coverage(rows[n][3], rows[n][5], TODAY), (False, "", ""))

    def test_fixture_L264_L265_consumer_read_at_vintage(self):
        rows = _fixture_rows()
        for n in (264, 265):
            self.assertTrue(S.coverage(rows[n][3], rows[n][5], dt.date(2026, 9, 5))[0])


class A6_A7_contract(unittest.TestCase):
    def test_row_shape_unchanged(self):
        self.assertEqual(S.Row._fields, ("key", "due", "delta", "owner", "cls", "basis", "cadence", "catalyst"))

    def test_covered_wrapper_signature(self):
        self.assertFalse(S.covered("PENDING — recovered from the transcript", ""))
        self.assertTrue(S.covered("PENDING · COVERED: BOND holds it", "", TODAY))

    def test_covered_rows_lists_suppressed_only(self):
        text = "\n".join(["# hdr", "\t".join(("2026-10-30", "x", "BOND", "PENDING · COVERED: BOND holds it", "", "")),
                          "\t".join(("2026-10-30", "y", "VULCAN", "PENDING — recovered script", "", "")),
                          "\t".join(("2026-10-30", "z", "HANS", "PENDING · COVERED: HANS is slated for a PROME wake", "", ""))])
        got = S.covered_rows(text, TODAY, 0)
        self.assertEqual([g[0] for g in got], ["D:L2"]); self.assertEqual(got[0][3], "COVERED")


if __name__ == "__main__":
    unittest.main()
