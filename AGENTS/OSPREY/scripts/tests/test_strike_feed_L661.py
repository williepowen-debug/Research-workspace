#!/usr/bin/env python3
"""DOCKET L661 — strike_feed.py READ-3 residue: acceptance tests (AC13-AC21; numbering continues L624's AC1-AC12).

Acceptance conditions (written first, committed alone in e5fe3a692): ACCEPTANCE_L661_strike_feed_read3_residue.md (same dir).
READ-3 ledger these answer: PROME/reports/2026-10-09_L624_strike-feed-patch_read_3.md (R3-Q, R3-H, R3-I2; mutants M4, M5).

Run (stdlib only, no network, never reads the live ledger or feed dir):
    python3 -B -W error::ResourceWarning -m unittest AGENTS/OSPREY/scripts/tests/test_strike_feed_L661.py -v
Fails first against the released code (AC20):
    STRIKE_FEED_PATH=/path/to/4ea2b4539/strike_feed.py python3 -B -m unittest <this file>
Reuses the L624 harness (run, src_rows, index, post) by import: same injected fetch and date, same temp config/ledger/out_dir.
Tests marked NON-DISCRIMINATING pass on the released code by design (must-not-fire, or a pin of behaviour it already has).
"""
import datetime as _dt, importlib.util, os, sys, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
from test_strike_feed_L624 import (run, src_rows, index, post, BASE, PAL, OCT, SEP, DEC, CX1_NEW, BODY_OK, Err,  # noqa: E402
                                   MOD_PATH, REAL_INDEX)

REAL_INDEX_1016 = os.path.join(HERE, "fixtures", "palaemon_index_2026-10-16_anchors.html")
REAL_NEWEST_1016 = "https://www.palaemonmaritime.com/post/maritime-security-report-5th-11th-october-2026"


def module():
    spec = importlib.util.spec_from_file_location("strike_feed_under_test_l661", MOD_PATH)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


D = _dt.date
# R3-Q: a pinned "most read" copy of last week's bulletin on top; the real newest past-year-typo'd below it.
TYPO25 = (post("5th-11th-october-2025"), "Maritime Security Report: 5th - 11th October 2025")
# R3-H: slug 2025, title 2026 (the title is right).
R3H = (post("5th-11th-october-2025"), "Maritime Security Report: 5th - 11th October 2026")
# R3-I2: the two-year title form, slug carries both years.
R3I2 = (post("29th-december-2026-4th-january-2027"), "Maritime Security Report: 29th December 2026 - 4th January 2027")


def one(rows):
    p = src_rows(rows)
    assert len(p) == 1, [r["url"] for r in p]
    return p[0]


class AC13_OrderSignalBelowTheFollowedLink(unittest.TestCase):
    def test_R3Q_past_typo_newest_below_pinned_last_week(self):
        """R3-Q: ENDs down the page run 10-04, 2025-10-11, 09-27 -- the typo'd link is out of date order."""
        rows, nr, _ = run("2026-10-13", {BASE: index(OCT, TYPO25, SEP), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertEqual(r["url"], OCT[0])
        self.assertTrue(r["ledger_match"].startswith("BULLETIN_NEWEST_UNSURE"), r["ledger_match"])
        self.assertIn(TYPO25[0], r["note"]); self.assertIn("out of date order", r["note"])
        self.assertEqual(nr, 1)

    def test_must_not_fire_monotone_with_ties(self):
        """NON-DISCRIMINATING by design: ENDs that never increase (a tie included) raise no order doubt."""
        tie = (post("21st-27th-september-2026-1"), "Maritime Security Report: 21st - 27th September 2026")
        rows, nr, _ = run("2026-10-09", {BASE: index(OCT, SEP, tie), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN — read manually"), r["ledger_match"])
        self.assertEqual(nr, 0)

    def test_must_not_fire_real_index_1016(self):
        """NON-DISCRIMINATING by design (AC21): the live 10/16 index -- 14 links, each listed once, newest-first."""
        with open(REAL_INDEX_1016, encoding="utf-8") as f: html_ = f.read()
        src = dict(PAL, url="https://www.palaemonmaritime.com/blog")
        rows, nr, _ = run("2026-10-16", {src["url"]: html_, REAL_NEWEST_1016: BODY_OK}, sources=(src,))
        r = one(rows)
        self.assertEqual(r["url"], REAL_NEWEST_1016)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN — read manually"), r["ledger_match"])
        self.assertIn("window 2026-10-05..2026-10-11 (title)", r["note"]); self.assertIn("position 1 of 14", r["note"])
        self.assertNotIn("doubt", r["note"]); self.assertEqual(nr, 0)

    def test_declared_limit_typo_newest_last_on_page_is_still_silent(self):
        """DECLARED LIMIT (ACCEPTANCE_L661 'Not in scope' (i)), pinned so no surface can claim it closed: R3-B2 --
        a past-typo'd real newest LAST on the page, title and slug agreeing. No index-level signal exists.
        If this test ever fails, the limit moved: update the acceptance residue and the README, do not delete the test."""
        rows, nr, _ = run("2026-10-13", {BASE: index(OCT, TYPO25), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN — read manually"), r["ledger_match"])
        self.assertEqual(nr, 0)


class AC14_DuplicateListingsKeepTheirPosition(unittest.TestCase):
    def test_featured_copy_of_last_week_on_top_real_newest_between_listings(self):
        """Featured OCT on top, then the list: typo'd real newest, OCT again; nothing below (AC13 has nothing to compare)."""
        rows, nr, _ = run("2026-10-13", {BASE: index(OCT, TYPO25, OCT), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertEqual(r["url"], OCT[0])
        self.assertTrue(r["ledger_match"].startswith("BULLETIN_NEWEST_UNSURE"), r["ledger_match"])
        self.assertIn(TYPO25[0], r["note"]); self.assertIn("lower listing", r["note"])
        self.assertEqual(nr, 1)

    def test_must_not_fire_featured_copy_directly_above_its_own_entry(self):
        rows, nr, _ = run("2026-10-09", {BASE: index(OCT, OCT, SEP), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN — read manually"), r["ledger_match"])
        self.assertIn("listed 2 times", r["note"])
        self.assertEqual(nr, 0)


class AC15_TitleSlugDisagreementNeverSilent(unittest.TestCase):
    def test_R3H_followed_link_slug_2025_title_2026(self):
        rows, nr, _ = run("2026-10-13", {BASE: index(R3H), R3H[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN_NEWEST_UNSURE"), r["ledger_match"])
        self.assertIn("title/slug dates disagree", r["note"]); self.assertIn("FOLLOWED", r["note"])
        self.assertIn("2025-10-11", r["note"]); self.assertIn("2026-10-11", r["note"])
        self.assertEqual(nr, 1)

    def test_CX1_shape_below_the_followed_link_and_last_on_page(self):
        """Title year typo, slug right, listed BELOW the followed link and LAST: neither AC10(a) nor AC13 can see it."""
        rows, nr, _ = run("2027-01-07", {BASE: index(DEC, CX1_NEW), DEC[0]: BODY_OK})
        r = one(rows)
        self.assertEqual(r["url"], DEC[0])
        self.assertTrue(r["ledger_match"].startswith("BULLETIN_NEWEST_UNSURE"), r["ledger_match"])
        self.assertIn(CX1_NEW[0], r["note"]); self.assertIn("title/slug dates disagree", r["note"])
        self.assertEqual(nr, 1)

    def test_must_not_fire_old_link_disagreement_both_readings_older(self):
        """NON-DISCRIMINATING by design: under either reading the link is older than the followed one."""
        old = (post("21st-27th-september-2025"), "Maritime Security Report: 21st - 27th September 2026")
        rows, nr, _ = run("2026-10-09", {BASE: index(OCT, old), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN — read manually"), r["ledger_match"]); self.assertEqual(nr, 0)

    def test_must_not_fire_future_slug_reading(self):
        """NON-DISCRIMINATING by design: a slug reading that starts after the run date is impossible."""
        fut = (post("5th-11th-october-2027"), "Maritime Security Report: 5th - 11th October 2026")
        rows, nr, _ = run("2026-10-13", {BASE: index(fut), fut[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN — read manually"), r["ledger_match"]); self.assertEqual(nr, 0)

    def test_must_not_fire_live_mis_slug_one_day_apart(self):
        """NON-DISCRIMINATING by design: the live -1 slug (title 14-20 Sep, slug 7-13 Sep) is 1 day apart, not year-class."""
        rows, nr, _ = run("2026-09-22", {BASE: index((post("7th-13th-september-2026-1"), "Maritime Security Report: 14th - 20th September 2026"),
                                                    (post("7th-13th-september-2026"), "Maritime Security Report: 7th - 13th September 2026")),
                                         post("7th-13th-september-2026-1"): BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN — read manually"), r["ledger_match"]); self.assertEqual(nr, 0)


class AC16_TwoYearWindowAndSingleDateBasis(unittest.TestCase):
    def test_bulletin_window_two_year_title_and_slug(self):
        m = module()
        self.assertEqual(m.bulletin_window(R3I2[1]), (D(2026, 12, 29), D(2027, 1, 4)))
        self.assertEqual(m.bulletin_window(R3I2[0]), (D(2026, 12, 29), D(2027, 1, 4)))
        self.assertEqual(m.bulletin_window("29th December 2026 to 4th January 2027"), (D(2026, 12, 29), D(2027, 1, 4)))

    def test_two_year_guards(self):
        """The second year must be the first or the first + 1, and the span check still applies.
        NON-DISCRIMINATING on the released code (it parses no two-year string at all); mutant M15 (the span guard on
        the two-year form dropped) must fail this. The year condition is implied by the span check (one guard, not two)."""
        m = module()
        self.assertEqual(m.bulletin_window("29th December 2025 - 4th January 2027"), (None, None))
        self.assertEqual(m.bulletin_window("1st December 2026 - 4th January 2027"), (None, None))

    def test_R3I2_read_2027_01_12_is_fresh_not_stale(self):
        rows, nr, _ = run("2027-01-12", {BASE: index(R3I2), R3I2[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN — read manually"), r["ledger_match"])
        self.assertEqual(r["pub_date"], "2027-01-04"); self.assertIn("window 2026-12-29..2027-01-04 (title)", r["note"])
        self.assertEqual(nr, 0)

    def test_single_date_basis_never_claims_window_end(self):
        single = (post("12th-october-2026"), "Maritime Security Report")
        rows, nr, _ = run("2026-10-16", {BASE: index(single), single[0]: BODY_OK})
        r = one(rows)
        self.assertNotIn("pub_date = window END", r["note"]); self.assertIn("END unknown", r["note"])
        self.assertEqual(nr, 0)
        rows, nr, _ = run("2026-10-23", {BASE: index(single), single[0]: BODY_OK})
        lm = one(rows)["ledger_match"]
        self.assertTrue(lm.startswith("BULLETIN_STALE"), lm); self.assertIn("7 days early", lm)   # AC26 (read 1 ⚠️4): was ~6
        self.assertEqual(nr, 1)

    def test_no_regression_one_year_forms_real_fixtures(self):
        """NON-DISCRIMINATING by design: every real title already parsed must parse to the same window."""
        m = module()
        want_1016 = [((10, 5), (10, 11)), ((9, 28), (10, 4)), ((9, 21), (9, 27)), ((9, 14), (9, 20)), ((9, 7), (9, 13)),
                     ((8, 31), (9, 6)), ((8, 24), (8, 30)), ((8, 17), (8, 23)), ((8, 10), (8, 16)), ((8, 3), (8, 9)),
                     ((7, 27), (8, 2)), ((7, 19), (7, 26)), ((7, 6), (7, 12)), ((6, 29), (7, 5))]
        want_1009 = want_1016[1:] + [((6, 22), (6, 29))]
        for path, want, base in ((REAL_INDEX_1016, want_1016, "https://www.palaemonmaritime.com/blog"),
                                 (REAL_INDEX, want_1009, "https://www.palaemonmaritime.com/blog")):
            with open(path, encoding="utf-8") as f: items = m.parse_html_index(f.read(), "maritime-security-report", base)
            got = [m.bulletin_window(it["title"]) for it in items]
            self.assertEqual(got, [(D(2026, *a), D(2026, *b)) for a, b in want], path)


class AC17_AC10ClausesPinned(unittest.TestCase):
    def test_up_to_five_named_then_plus_n_more(self):
        """NON-DISCRIMINATING on the released code (it already holds); mutant M4 (doubts[:5] -> [:1]) must fail this."""
        weeks = [(post(f"week-{n}-2026"), f"Maritime Security Report: Week {n}") for n in range(30, 37)]
        rows, nr, _ = run("2026-10-09", {BASE: index(*weeks[:6], OCT, weeks[6]), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertEqual(sum(1 for u, _ in weeks if u in r["note"]), 5, r["note"])
        self.assertIn("+2 more", r["note"]); self.assertEqual(nr, 1)

    def test_undated_row_names_the_other_unusable_links(self):
        """NON-DISCRIMINATING on the released code (it already holds); mutant M5 (doubt note dropped when UNDATED) must fail this."""
        u1, u2 = (post("latest"), "Maritime Security Report"), (post("week-41-2026"), "Maritime Security Report: Week 41")
        rows, nr, _ = run("2026-10-09", {BASE: index(u1, u2), u1[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN_UNDATED"), r["ledger_match"])
        self.assertIn(u2[0], r["note"]); self.assertIn("no parseable date", r["note"]); self.assertEqual(nr, 1)


class Neighbours_L661(unittest.TestCase):
    def test_overlap_order_and_title_slug_on_one_link_counted_once(self):
        both = (post("5th-11th-october-2026"), "Maritime Security Report: 5th - 11th October 2025")   # title typo, slug right
        rows, nr, _ = run("2026-10-13", {BASE: index(OCT, both, SEP), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN_NEWEST_UNSURE — 1 doubt"), r["ledger_match"])
        self.assertIn("out of date order", r["note"]); self.assertIn("title/slug dates disagree", r["note"])
        self.assertEqual(r["note"].count(both[0]), 1); self.assertEqual(nr, 1)

    def test_overlap_new_doubt_and_stale_one_row(self):
        rows, nr, _ = run("2026-10-20", {BASE: index(OCT, TYPO25, SEP), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN_NEWEST_UNSURE"), r["ledger_match"])
        self.assertIn("BULLETIN_STALE", r["ledger_match"]); self.assertIn(TYPO25[0], r["note"]); self.assertEqual(nr, 1)

    def test_overlap_new_doubt_and_body_fetch_fails(self):
        rows, nr, _ = run("2026-10-13", {BASE: index(OCT, TYPO25, SEP), OCT[0]: Err("HTTP Error 503: Service Unavailable")})
        r = one(rows)
        self.assertTrue(r["title"].startswith("FETCH_FAILED (newest post)"))
        self.assertIn("BULLETIN_NEWEST_UNSURE", r["note"]); self.assertIn(TYPO25[0], r["note"]); self.assertEqual(nr, 1)

    def test_wrong_owner_non_follow_index_with_disorder_and_duplicates_unchanged(self):
        """NON-DISCRIMINATING by design: the new rules run only under follow_newest."""
        a = ("https://ww.example/blog/tanker-hit-novorossiysk-2nd-october-2026", "Tanker hit off Novorossiysk")
        b = ("https://ww.example/blog/tanker-hit-novorossiysk-8th-october-2026", "Tanker hit off Novorossiysk again")
        ww = index(a, b, a)
        srcs = (PAL, {"id": "ww", "kind": "html_index", "url": "https://ww.example/blog", "link_pattern": "ww.example/blog/", "follow_newest": False})
        rows, nr, _ = run("2026-10-09", {BASE: index(OCT), OCT[0]: BODY_OK, "https://ww.example/blog": ww}, sources=srcs)
        self.assertFalse(any("doubt" in r["note"] or "NEWEST_UNSURE" in r["ledger_match"] for r in rows))
        self.assertEqual([r["url"] for r in src_rows(rows, "ww")], [a[0], b[0]])
        self.assertEqual(nr, 0)

    def test_missing_info_unusable_links_left_out_of_order_comparison(self):
        """An undated link and a FUTURE-start link below the followed one stay AC10(b) doubts; AC13 compares DATED links only.
        NON-DISCRIMINATING on the released code (no AC13 there); mutant M21 -- unusable links compared -- must fail this
        (an undated END cannot be ordered; a future END outranks every honest link above it)."""
        und = (post("week-39-2026"), "Maritime Security Report: Week 39")
        fut = (post("5th-11th-october-2062"), "Maritime Security Report: 5th - 11th October 2062")
        jun = (post("1st-7th-june-2026"), "Maritime Security Report: 1st - 7th June 2026")
        rows, nr, _ = run("2026-10-09", {BASE: index(OCT, SEP, und, fut, jun), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN_NEWEST_UNSURE"), r["ledger_match"]); self.assertIn("2 doubt link(s)", r["note"])
        self.assertIn(und[0], r["note"]); self.assertIn(fut[0], r["note"]); self.assertNotIn("out of date order", r["note"])
        self.assertEqual(nr, 1)

    def test_missing_info_title_only_and_slug_only_links_no_comparison(self):
        """NON-DISCRIMINATING by design: with one reading missing there is nothing to disagree."""
        title_only = (post("latest-report"), "Maritime Security Report: 5th - 11th October 2026")
        slug_only = (post("5th-11th-october-2026"), "Maritime Security Report")
        for top in (title_only, slug_only):
            rows, nr, _ = run("2026-10-13", {BASE: index(top, OCT), top[0]: BODY_OK})
            r = one(rows)
            self.assertEqual(r["url"], top[0])
            self.assertTrue(r["ledger_match"].startswith("BULLETIN — read manually"), r["ledger_match"]); self.assertEqual(nr, 0)


# ---------------------------------------------------------------------------------------------------------------
# READ-1 FIX (AC22-AC26; ACCEPTANCE_L661 "READ-1 FIX", committed alone in 31053d1f6 before this code edit).
# Ledger: PROME/reports/2026-10-16_L661_strike-feed_read_1.md (❌1 CX-A; ⚠️2 mutants MR2/MR4/MR5/MR7; ⚠️1 CX-E).
CXA_TITLE = ("Maritime Security Report: 21st - 27th September 2026. Our next report, covering "
             "28th September 2026 - 4th October 2026, will follow.")
CXA = (post("21st-27th-september-2026"), CXA_TITLE)


class AC22_LeftmostWindowWins(unittest.TestCase):
    def test_CXA_later_two_year_pair_in_anchor_text_never_makes_stale_read_fresh(self):
        """❌1 CX-A: the title's own window ends 09-27 (< cutoff 09-28); the later 'next report' pair must not govern.
        DISCRIMINATING against 48342e63a (HEAD before AC22: BULLETIN, NOT_READ 0, pub 10-04). Passes on 4ea2b4539 (the
        released code parsed no two-year form), so it is a regression test, labelled here per AC20."""
        rows, nr, _ = run("2026-10-08", {BASE: index(CXA), CXA[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN_STALE"), r["ledger_match"])
        self.assertEqual(r["pub_date"], "2026-09-27")
        self.assertEqual(nr, 1)

    def test_direct_leftmost_one_year_window_governs(self):
        """❌1 direct. DISCRIMINATING against 48342e63a (later END 01-04); passes on 4ea2b4539 (regression test)."""
        m = module()
        self.assertEqual(m.bulletin_window(CXA_TITLE), (D(2026, 9, 21), D(2026, 9, 27)))
        self.assertEqual(m.bulletin_window("Maritime Security Report: 22nd - 28th December 2026 - 4th January 2027"),
                         (D(2026, 12, 22), D(2026, 12, 28)))

    def test_two_year_forms_still_parse_when_they_start_first(self):
        """NON-DISCRIMINATING against 48342e63a by design (must-not-regress): R3-I2 title/slug, the 'to' and no-space forms.
        Fails on 4ea2b4539 (it parsed no two-year form); its discrimination against AC22 is shown by mutant MR7."""
        m = module()
        for t in (R3I2[1], R3I2[0], "29th December 2026 to 4th January 2027", "29th December 2026-4th January 2027"):
            self.assertEqual(m.bulletin_window(t), (D(2026, 12, 29), D(2027, 1, 4)), t)


class AC23_ReaderPins(unittest.TestCase):
    def test_CXF_duplicate_then_typo_newest_then_older_is_unsure(self):
        """⚠️2 CX-F (kills read-1 mutant MR2, listing positions compressed): OCT, OCT, TYPO25, SEP at 10/13.
        Fails on 4ea2b4539 (the released code was silent here)."""
        rows, nr, _ = run("2026-10-13", {BASE: index(OCT, OCT, TYPO25, SEP), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertEqual(r["url"], OCT[0])
        self.assertTrue(r["ledger_match"].startswith("BULLETIN_NEWEST_UNSURE"), r["ledger_match"])
        self.assertIn(TYPO25[0], r["note"]); self.assertEqual(nr, 1)

    def test_two_year_span_bound_is_14_days(self):
        """⚠️2 (kills MR4, span bound loosened): a 15-day two-year span is unparsed; a 14-day one parses.
        Fails on 4ea2b4539 through the 14-day half (it parsed no two-year form); the 15-day half passes there by design."""
        m = module()
        self.assertEqual(m.bulletin_window("21st December 2026 - 5th January 2027"), (None, None))
        self.assertEqual(m.bulletin_window("22nd December 2026 - 5th January 2027"), (D(2026, 12, 22), D(2027, 1, 5)))

    def test_reversed_two_year_is_unparsed(self):
        """⚠️2 (kills MR5, END-before-START allowed). Fails on 4ea2b4539 (N2 mis-parse to 12-27..12-29)."""
        self.assertEqual(module().bulletin_window("4th January 2027 - 29th December 2026"), (None, None))

    def test_year_apart_two_year_string_is_unparsed_not_misparsed(self):
        """⚠️2 (kills MR7, 'final' removed). Fails on 4ea2b4539 (N2 mis-parse to 12-25..12-27)."""
        self.assertEqual(module().bulletin_window("15th December 2025 - 27th December 2026"), (None, None))


class AC24_DeclaredLimitFirstListingOrder(unittest.TestCase):
    def test_declared_limit_CXE_repeat_listing_below_typo_newest_is_still_silent(self):
        """DECLARED LIMIT (ACCEPTANCE_L661 READ-1 FIX AC24; read 1 ⚠️1), pinned so no surface can claim it closed:
        OCT, SEP, TYPO25, SEP -- AC13 compares FIRST listings only, and the only later-ending link below TYPO25 is a
        repeat listing of SEP. If this test ever fails, the limit moved: update the residue and README, do not delete it."""
        rows, nr, _ = run("2026-10-13", {BASE: index(OCT, SEP, TYPO25, SEP), OCT[0]: BODY_OK})
        r = one(rows)
        self.assertTrue(r["ledger_match"].startswith("BULLETIN — read manually"), r["ledger_match"])
        self.assertEqual(nr, 0)


if __name__ == "__main__":
    unittest.main()
