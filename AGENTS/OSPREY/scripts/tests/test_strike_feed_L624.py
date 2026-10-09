#!/usr/bin/env python3
"""DOCKET L624 — strike_feed.py follow_newest bulletin: acceptance tests.

Acceptance conditions (written first, committed alone): ACCEPTANCE_L624_strike_feed_follow_newest.md (same dir).
Read-1 ledger these answer: PROME/reports/2026-10-09_L624_strike-feed-patch_read_1.md (fixtures X1-X4).

Run (stdlib only, no network, never reads the live ledger or feed dir):
    python3 -W error::ResourceWarning -m unittest AGENTS/OSPREY/scripts/tests/test_strike_feed_L624.py -v
Point at another copy of the script (e.g. a pre-fix commit) to see it fail first:
    STRIKE_FEED_PATH=/path/to/old/strike_feed.py python3 -m unittest <this file>

Each fixture builds its own config, ledger and out_dir in a temp dir; `fetch` and `date.today()` are injected.
The one REAL fixture is fixtures/palaemon_index_2026-10-09_anchors.html (trimmed live index; header says how).
"""
import contextlib, csv, datetime as _dt, importlib.util, io, json, os, re, sys, tempfile, types, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
MOD_PATH = os.environ.get("STRIKE_FEED_PATH", os.path.join(os.path.dirname(HERE), "strike_feed.py"))
REAL_INDEX = os.path.join(HERE, "fixtures", "palaemon_index_2026-10-09_anchors.html")

BASE = "https://pal.example/blog"
def post(slug): return "https://pal.example/post/maritime-security-report-" + slug
def index(*links): return "<html><body>" + "".join(f'<a href="{u}"><h2>{t}</h2></a>' for u, t in links) + "</body></html>"

BODY_OK = "<html><body>" + "incident report " * 200 + "</body></html>"   # > 1500 chars after tag-strip
BODY_SHORT = "<html><body><div id='root'>Loading…</div></body></html>"
BODY_EMPTY = ""

PAL = {"id": "palaemon", "kind": "html_index", "url": BASE, "link_pattern": "maritime-security-report", "follow_newest": True}

OCT = (post("28th-september-4th-october-2026"), "Maritime Security Report: 28th September - 4th October 2026")
SEP = (post("21st-27th-september-2026"), "Maritime Security Report: 21st - 27th September 2026")
JUN = (post("1st-7th-june-2026"), "Maritime Security Report: 1st - 7th June 2026")
MAY = (post("4th-10th-may-2026"), "Maritime Security Report: 4th - 10th May 2026")

LEDGER = ("# swept-complete through: 2026-09-20\n"
          "strike_id\tDate\tc2\tc3\tFacility\tRegion\t" + "\t".join(f"c{i}" for i in range(6, 16)) + "\n"
          "RU-20260909-NOVOROSSIYSK-OIL-TERMINAL\t2026-09-09\tx\tx\tNovorossiysk Sheskharis terminal\tKrasnodar\t" + "\t".join("x" for _ in range(10)) + "\n")


class Err(Exception):
    pass


def run(today, pages, sources=(PAL,), days=10):
    """Run the module's main() against injected pages. Returns (rows, not_read, stdout)."""
    spec = importlib.util.spec_from_file_location("strike_feed_under_test", MOD_PATH)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

    class FixedDate(_dt.date):
        @classmethod
        def today(cls): return _dt.date.fromisoformat(today)
    m.dt = types.SimpleNamespace(date=FixedDate, datetime=_dt.datetime, timedelta=_dt.timedelta)

    def fake_fetch(url, timeout=25):
        if url not in pages:
            raise Err(f"HTTP Error 404: no fixture for {url}")
        v = pages[url]
        if isinstance(v, Exception):
            raise v
        return v
    m.fetch = fake_fetch

    with tempfile.TemporaryDirectory() as td:
        lp = os.path.join(td, "STRIKES.tsv")
        with open(lp, "w", encoding="utf-8") as f: f.write(LEDGER)
        cfg = {"sources": list(sources), "days_back": days, "ledger": lp, "out_dir": os.path.join(td, "feed"),
               "context_tokens": ["drone", "strike"], "maritime_tokens": ["tanker", "black sea"],
               "asset_tokens": ["refiner", "tanker", "oil terminal"], "place_tokens": ["novorossiysk"]}
        cp = os.path.join(td, "cfg.json")
        with open(cp, "w", encoding="utf-8") as f: json.dump(cfg, f)
        argv, out = sys.argv, io.StringIO()
        sys.argv = ["strike_feed.py", "--config", cp]
        try:
            with contextlib.redirect_stdout(out):
                rc = m.main()
        finally:
            sys.argv = argv
        assert rc == 0, rc
        with open(os.path.join(td, "feed", f"FEED_CANDIDATES_{today}.tsv"), encoding="utf-8") as f:
            lines = [ln for ln in f if not ln.startswith("#")]
        rows = list(csv.DictReader(lines, delimiter="\t"))
    mm = re.search(r"NOT_READ=(\d+)", out.getvalue())
    return rows, int(mm[1]) if mm else None, out.getvalue()


def src_rows(rows, sid="palaemon"):
    return [r for r in rows if r["source"] == sid]


class AC4_L309ReproductionDiscriminates(unittest.TestCase):
    def test_within_month_bulletin_start_before_cutoff_end_inside(self):
        """21st-27th Sep read 10/2: slug start 9/21 < cutoff 9/22, window end 9/27 inside. Pre-patch: 0 rows (silent)."""
        rows, nr, _ = run("2026-10-02", {BASE: index(SEP), SEP[0]: BODY_OK})
        p = src_rows(rows)
        self.assertEqual(len(p), 1)
        self.assertTrue(p[0]["ledger_match"].startswith("BULLETIN — read manually"), p[0]["ledger_match"])
        self.assertEqual(nr, 0)

    def test_1009_cross_month_shape_regression_only(self):
        """NON-DISCRIMINATING (read-1 ❌3): this passes on pre-patch code too. Kept as ordinary-case regression."""
        rows, nr, _ = run("2026-10-09", {BASE: index(OCT), OCT[0]: BODY_OK})
        p = src_rows(rows)
        self.assertEqual(len(p), 1)
        self.assertTrue(p[0]["ledger_match"].startswith("BULLETIN — read manually"))
        self.assertEqual(nr, 0)


class AC1_NewestByDateNotDocumentOrder(unittest.TestCase):
    def test_X2_older_link_first_on_page(self):
        """Read-1 X2: a June 'most read' link precedes the real newest in document order."""
        most_read = (JUN[0], "Most read: " + JUN[1])
        rows, nr, _ = run("2026-10-09", {BASE: index(most_read, OCT), OCT[0]: BODY_OK, JUN[0]: BODY_OK})
        p = src_rows(rows)
        self.assertEqual([r["url"] for r in p], [OCT[0]])
        self.assertFalse(any(JUN[0] == r["url"] for r in rows))
        self.assertEqual(nr, 0)

    def test_real_index_2026_10_09(self):
        """REAL fixture (live index, trimmed): newest-first document order, 14 bulletin links."""
        with open(REAL_INDEX, encoding="utf-8") as f: html_ = f.read()
        newest = "https://www.palaemonmaritime.com/post/maritime-security-report-28th-september-4th-october-2026"
        src = dict(PAL, url="https://www.palaemonmaritime.com/blog")
        rows, nr, _ = run("2026-10-09", {src["url"]: html_, newest: BODY_OK}, sources=(src,))
        p = src_rows(rows)
        self.assertEqual([r["url"] for r in p], [newest])
        self.assertTrue(p[0]["ledger_match"].startswith("BULLETIN — read manually"))
        self.assertIn("window 2026-09-28..2026-10-04 (title)", p[0]["note"])
        self.assertEqual(nr, 0)
        # same real index, read 10/20 with no newer post: the publisher looks stopped -> labelled, counted
        rows, nr, _ = run("2026-10-20", {src["url"]: html_, newest: BODY_OK}, sources=(src,))
        p = src_rows(rows)
        self.assertTrue(p[0]["ledger_match"].startswith("BULLETIN_STALE"), p[0]["ledger_match"])
        self.assertEqual(nr, 1)

    def test_real_slug_defect_window_from_title(self):
        """Live slug ...-7th-13th-september-2026-1 is TITLED 14th - 20th September 2026: the title wins."""
        rows, _, _ = run("2026-09-22", {BASE: index((post("7th-13th-september-2026-1"), "Maritime Security Report: 14th - 20th September 2026"),
                                                    (post("7th-13th-september-2026"), "Maritime Security Report: 7th - 13th September 2026")),
                                        post("7th-13th-september-2026-1"): BODY_OK})
        p = src_rows(rows)
        self.assertEqual(p[0]["url"], post("7th-13th-september-2026-1"))
        self.assertIn("window 2026-09-14..2026-09-20 (title)", p[0]["note"])

    def test_overlap_tie_on_window_end_keeps_document_order(self):
        a = (post("7th-13th-september-2026"), "Maritime Security Report: 7th - 13th September 2026")
        b = (post("7th-13th-september-2026-1"), "Maritime Security Report: 7th - 13th September 2026")
        rows, _, _ = run("2026-09-16", {BASE: index(a, b), a[0]: BODY_OK, b[0]: BODY_OK})
        self.assertEqual([r["url"] for r in src_rows(rows)], [a[0]])


class AC2_ExemptionIsOneItem(unittest.TestCase):
    def test_X1_body_fetch_fails(self):
        """Read-1 X1: body 503 used to let EVERY index link skip the age filter (May/June rows)."""
        rows, nr, _ = run("2026-10-09", {BASE: index(OCT, SEP, JUN, MAY), OCT[0]: Err("HTTP Error 503: Service Unavailable")})
        p = src_rows(rows)
        self.assertEqual(len(p), 1, [r["url"] for r in p])
        self.assertTrue(p[0]["title"].startswith("FETCH_FAILED (newest post)"))
        self.assertEqual(p[0]["url"], OCT[0])
        self.assertEqual(p[0]["pub_date"], "2026-10-04")
        self.assertFalse(any(r["url"] in (JUN[0], MAY[0], SEP[0]) for r in rows))
        self.assertEqual(nr, 1)

    def test_body_success_emits_only_the_followed_item(self):
        rows, _, _ = run("2026-10-09", {BASE: index(OCT, SEP, JUN, MAY), OCT[0]: BODY_OK})
        self.assertEqual([r["url"] for r in src_rows(rows)], [OCT[0]])

    def test_overlap_body_fails_AND_stale_counts_once(self):
        rows, nr, _ = run("2026-10-09", {BASE: index(JUN), JUN[0]: Err("timed out")})
        p = src_rows(rows)
        self.assertEqual(len(p), 1)
        self.assertTrue(p[0]["title"].startswith("FETCH_FAILED (newest post)"))
        self.assertIn("BULLETIN_STALE", p[0]["note"])
        self.assertEqual(nr, 1)


class AC3_StaleBulletinLabelledAndCounted(unittest.TestCase):
    def test_d_stale_months(self):
        rows, nr, _ = run("2026-10-09", {BASE: index(JUN), JUN[0]: BODY_OK})
        p = src_rows(rows)
        self.assertEqual(len(p), 1)
        self.assertTrue(p[0]["ledger_match"].startswith("BULLETIN_STALE"), p[0]["ledger_match"])
        self.assertIn("2026-06-07", p[0]["ledger_match"]); self.assertIn("2026-09-29", p[0]["ledger_match"])
        self.assertEqual(nr, 1)

    def test_boundary_end_on_cutoff_is_fresh_one_day_before_is_stale(self):
        """Falsify the guard at its edge: cutoff 10/9 - 10 d = 9/29."""
        on = (post("23rd-29th-september-2026"), "Maritime Security Report: 23rd - 29th September 2026")
        before = (post("22nd-28th-september-2026"), "Maritime Security Report: 22nd - 28th September 2026")
        rows, nr, _ = run("2026-10-09", {BASE: index(on), on[0]: BODY_OK})
        self.assertTrue(src_rows(rows)[0]["ledger_match"].startswith("BULLETIN — read manually")); self.assertEqual(nr, 0)
        rows, nr, _ = run("2026-10-09", {BASE: index(before), before[0]: BODY_OK})
        self.assertTrue(src_rows(rows)[0]["ledger_match"].startswith("BULLETIN_STALE")); self.assertEqual(nr, 1)


class AC5_UndatedOrImplausible(unittest.TestCase):
    def test_undated_slug(self):
        u = (post("latest"), "Maritime Security Report")
        rows, nr, _ = run("2026-10-09", {BASE: index(u), u[0]: BODY_OK})
        p = src_rows(rows)
        self.assertEqual(len(p), 1)
        self.assertTrue(p[0]["ledger_match"].startswith("BULLETIN_UNDATED"), p[0]["ledger_match"])
        self.assertEqual(nr, 1)

    def test_X3_future_typo_is_not_newest(self):
        typo = (post("5th-11th-october-2062"), "Maritime Security Report: 5th - 11th October 2062")
        rows, nr, _ = run("2026-10-09", {BASE: index(typo, OCT), OCT[0]: BODY_OK, typo[0]: BODY_OK})
        p = src_rows(rows)
        self.assertEqual([r["url"] for r in p], [OCT[0]])
        self.assertIn("FUTURE", p[0]["note"]); self.assertIn(typo[0], p[0]["note"])
        self.assertEqual(nr, 0)

    def test_only_future_typo_is_undated(self):
        typo = (post("5th-11th-october-2062"), "Maritime Security Report: 5th - 11th October 2062")
        rows, nr, _ = run("2026-10-09", {BASE: index(typo), typo[0]: BODY_OK})
        self.assertTrue(src_rows(rows)[0]["ledger_match"].startswith("BULLETIN_UNDATED")); self.assertEqual(nr, 1)


class AC6_BodyWarningReachesOutput(unittest.TestCase):
    def test_short_body(self):
        rows, _, _ = run("2026-10-09", {BASE: index(OCT), OCT[0]: BODY_SHORT})
        n = src_rows(rows)[0]["note"]
        self.assertIn("[body not machine-readable", n); self.assertNotIn("EMPTY", n)

    def test_X4_empty_body_distinguishable(self):
        rows, _, _ = run("2026-10-09", {BASE: index(OCT), OCT[0]: BODY_EMPTY})
        n = src_rows(rows)[0]["note"]
        self.assertIn("[body not machine-readable", n); self.assertIn("EMPTY", n)

    def test_long_body_no_warning(self):
        rows, _, _ = run("2026-10-09", {BASE: index(OCT), OCT[0]: BODY_OK})
        self.assertNotIn("not machine-readable", src_rows(rows)[0]["note"])


class AC7_NoChangeElsewhere(unittest.TestCase):
    def test_wrong_owner_exemption_does_not_leak(self):
        rss = ('<?xml version="1.0"?><rss><channel>'
               '<item><title>Drone strike on Novorossiysk oil terminal</title><link>https://rss.example/old</link><pubDate>Tue, 01 Sep 2026 08:00:00 GMT</pubDate></item>'
               '<item><title>Drone strike on Novorossiysk oil terminal again</title><link>https://rss.example/new</link><pubDate>Thu, 08 Oct 2026 08:00:00 GMT</pubDate></item>'
               '</channel></rss>')
        ww = index(("https://ww.example/blog/tanker-hit-novorossiysk-1st-september-2026", "Tanker hit off Novorossiysk"),
                   ("https://ww.example/blog/tanker-hit-novorossiysk-7th-october-2026", "Tanker hit off Novorossiysk"))
        srcs = (PAL, {"id": "rss1", "kind": "rss", "url": "https://rss.example/feed"},
                {"id": "ww", "kind": "html_index", "url": "https://ww.example/blog", "link_pattern": "ww.example/blog/", "follow_newest": False})
        rows, nr, _ = run("2026-10-09", {BASE: index(OCT, JUN), OCT[0]: BODY_OK, "https://rss.example/feed": rss, "https://ww.example/blog": ww}, sources=srcs)
        urls = {r["url"] for r in rows}
        self.assertIn("https://rss.example/new", urls); self.assertNotIn("https://rss.example/old", urls)
        self.assertIn("https://ww.example/blog/tanker-hit-novorossiysk-7th-october-2026", urls)
        self.assertNotIn("https://ww.example/blog/tanker-hit-novorossiysk-1st-september-2026", urls)
        self.assertEqual(nr, 0)

    def test_index_404_and_empty_unchanged(self):
        rows, nr, _ = run("2026-10-09", {})
        self.assertTrue(src_rows(rows)[0]["title"].startswith("FETCH_FAILED")); self.assertEqual(nr, 1)
        rows, nr, _ = run("2026-10-09", {BASE: "<html><body>nothing</body></html>"})
        self.assertTrue(src_rows(rows)[0]["title"].startswith("EMPTY_FEED")); self.assertEqual(nr, 1)

    def test_columns_unchanged(self):
        rows, _, _ = run("2026-10-09", {BASE: index(OCT), OCT[0]: BODY_OK})
        self.assertEqual(list(rows[0].keys()), ["run_date", "pub_date", "source", "title", "url", "matched_tokens", "ledger_match", "note"])


if __name__ == "__main__":
    unittest.main()
