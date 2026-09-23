#!/usr/bin/env python3
"""L409 — first-published (ALFRED) basis for FORGE fetch.py: acceptance fixtures.

Plan + acceptance conditions: PROME/plans/2026-09-22_L409-market-data-vintage-repair-PLAN.md
Offline by default: every test loads an isolated copy of fetch.py and a fake FRED that
implements ALFRED's output_type=4 window semantics (a row is returned only when its FIRST
release falls inside [realtime_start, realtime_end]). No live cache, .env or audit log.

L409_LIVE=1 adds the live-pull list (declared gate series + PAYEMS/IORB fixtures) and the
D8 same-run freshness check. FETCH_REVIEW_SOURCE optionally selects another fetch.py.
"""
import contextlib
import datetime
import importlib.util
import io
import json
import os
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

SOURCE = pathlib.Path(os.environ.get("FETCH_REVIEW_SOURCE", str(
    pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/fetch.py"
))).resolve()
LIVE_SOURCE = pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/fetch.py"
TODAY = datetime.date(2026, 9, 23)

# (date, first_published, first_value, latest_revised_value)
PAYEMS = [
    ("2026-05-01", "2026-06-05", "159001", "158950"),
    ("2026-06-01", "2026-07-02", "158984", "158892"),
    ("2026-07-01", "2026-08-07", "158858", "158913"),
    ("2026-08-01", "2026-09-04", "159075", "159075"),
]
# IORB is stamped on its EFFECTIVE date: 9/20 and 9/21 were first published 9/18 (❌7).
IORB = [
    ("2026-09-18", "2026-09-18", "3.90", "3.90"),
    ("2026-09-19", "2026-09-18", "3.90", "3.90"),
    ("2026-09-20", "2026-09-18", "3.90", "3.90"),
    ("2026-09-21", "2026-09-18", "3.90", "3.90"),
    ("2026-09-22", "2026-09-22", "3.90", "3.90"),
    ("2026-09-23", "2026-09-22", "3.90", "3.90"),
]
DGS10 = [
    ("2026-09-15", "2026-09-16", "5.00", "5.00"),
    ("2026-09-16", "2026-09-17", "5.02", "5.02"),
    ("2026-09-17", "2026-09-18", ".", "."),
    ("2026-09-18", "2026-09-21", "5.01", "5.01"),
    ("2026-09-21", "2026-09-22", "4.96", "4.96"),
    ("2026-09-22", "2026-09-23", "4.96", "4.96"),
]
# A SPARSE daily series: valid only every 5th calendar day (the RIFSPPNA2P2D90NB shape the
# result reader used for CE-2). The frequency-derived window for limit=10 is 38 days and holds
# only ~7 valid rows.
SPARSE = [((datetime.date(2026, 9, 22) - datetime.timedelta(days=i)).isoformat(),
           (datetime.date(2026, 9, 23) - datetime.timedelta(days=i)).isoformat(),
           ("1.0" if i % 5 == 0 else "."), ("1.0" if i % 5 == 0 else "."))
          for i in range(120)]
FREQ = {"PAYEMS": "M", "IORB": "D", "DGS10": "D", "VIXCLS": "D", "SPARSE": "D"}


class FakeFred:
    """ALFRED semantics for the two endpoints fred_fetch_vintage uses."""

    def __init__(self, tables, cap_error=False, fail=None, drop=()):
        self.tables, self.cap_error, self.fail, self.drop = tables, cap_error, fail, set(drop)
        self.calls = []

    def __call__(self, base, params):
        self.calls.append((base, dict(params)))
        if self.fail:
            return {"error": self.fail}
        sid = params["series_id"]
        if base.endswith("/fred/series"):
            return {"seriess": [{"frequency_short": FREQ[sid]}]}
        rows = self.tables[sid]
        ostart = params.get("observation_start", "0000-00-00")
        if params.get("output_type") == 4:
            if self.cap_error:
                return {"error": "HTTP 400: There are 2916 vintage dates in the specified real-time "
                                 "period ... exceeds the maximum ... (2000)."}
            rs, re_ = params["realtime_start"], params["realtime_end"]
            obs = [{"date": d, "value": fv, "realtime_start": fp, "realtime_end": "9999-12-31"}
                   for d, fp, fv, _ in rows
                   if d >= ostart and rs <= fp <= re_ and d not in self.drop]
            return {"observations": obs}
        # latest-revised; deliberately NOT filtered by observation_start so the
        # function's own ≥ observation_start filter is exercised (⚠️9)
        obs = [{"date": d, "value": lv} for d, _, _, lv in rows]
        return {"observations": sorted(obs, key=lambda o: o["date"], reverse=True)}


class FixedDate(datetime.date):
    @classmethod
    def today(cls):
        return TODAY


def load_fetch(stack, source=SOURCE):
    temp = pathlib.Path(stack.enter_context(tempfile.TemporaryDirectory()))
    cache = temp / "cache"
    stack.enter_context(patch.dict(os.environ, {
        "MKTDATA_REEXEC": "1", "FRED_API_KEY": "SECRET-FIXTURE-KEY", "FORGE_CACHE_DIR": str(cache)}))
    module_path = temp / "FORGE/tools/market-data/fetch.py"
    module_path.parent.mkdir(parents=True)
    module_path.write_bytes(source.read_bytes())
    spec = importlib.util.spec_from_file_location("l409_fetch", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    stack.enter_context(patch.object(mod, "_audit_log"))
    return mod, cache


class Vintage(unittest.TestCase):
    def setUp(self):
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.f, self.cache = load_fetch(self.stack)
        self.stack.enter_context(patch.object(self.f, "date", FixedDate))
        self.fake = FakeFred({"PAYEMS": PAYEMS, "IORB": IORB, "DGS10": DGS10, "SPARSE": SPARSE})
        self.stack.enter_context(patch.object(self.f, "_fred_get", self.fake))

    def vintage_calls(self):
        return [p for _, p in self.fake.calls if p.get("output_type") == 4]

    # --- A1: basis explicit, values are FIRST-release values -------------------------
    def test_a1_first_published_values_and_basis(self):
        r = self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-05-01")
        self.assertNotIn("error", r)
        self.assertEqual(r["basis"], "first-published")
        jul = [x for x in r["rows"] if x["date"] == "2026-07-01"][0]
        self.assertEqual(jul["value"], "158858")          # not the revised 158913
        self.assertEqual(jul["first_published"], "2026-08-07")
        self.assertEqual([x["date"] for x in r["rows"]],
                         ["2026-08-01", "2026-07-01", "2026-06-01", "2026-05-01"])

    def test_a1_unsupported_basis_is_an_error_not_latest_revised(self):
        r = self.f.fred_fetch_vintage("PAYEMS", 4, basis="latest-revised")
        self.assertIn("error", r)
        self.assertEqual(r["rows"], [])
        self.assertEqual(self.fake.calls, [])

    # --- D2/❌7: lead buffer admits early publications, never extra observations -------
    def test_d2_lead_buffer_keeps_forward_stamped_rows(self):
        r = self.f.fred_fetch_vintage("IORB", 10, observation_start="2026-09-20")
        self.assertEqual(r["request"]["realtime_start"], "2026-09-06")   # 9/20 − 14d
        self.assertEqual(sorted(x["date"] for x in r["rows"]),
                         ["2026-09-20", "2026-09-21", "2026-09-22", "2026-09-23"])
        self.assertFalse(r["short"])

    def test_d2_fixture_discriminates_without_the_buffer(self):
        # The counterexample the buffer exists for: with realtime_start = observation_start
        # ALFRED drops 9/20 and 9/21. Proves the IORB fixture can fail.
        got = self.fake("…/fred/series/observations", {
            "series_id": "IORB", "output_type": 4, "observation_start": "2026-09-20",
            "realtime_start": "2026-09-20", "realtime_end": "9999-12-31"})
        self.assertEqual([o["date"] for o in got["observations"]], ["2026-09-22", "2026-09-23"])

    def test_d2_derived_window_monthly(self):
        r = self.f.fred_fetch_vintage("PAYEMS", 2)
        # ceil(2 × 31 × 2) + 10 = 134 days before 9/23; lead = max(14, 62) = 62
        self.assertEqual(r["request"]["observation_start"], "2026-05-12")
        self.assertEqual(r["request"]["realtime_start"], "2026-03-11")
        self.assertEqual([x["date"] for x in r["rows"]], ["2026-08-01", "2026-07-01"])

    # --- D3/❌4: a silently dropped row is reported, never completed ---------------------
    def test_d3_missing_row_sets_short_and_is_not_cached(self):
        self.fake.drop = {"2026-06-01"}
        r = self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-05-01")
        self.assertTrue(r["short"])
        self.assertEqual(r["missing"], ["2026-06-01"])
        self.assertNotIn("2026-06-01", [x["date"] for x in r["rows"]])
        self.assertFalse(list(self.cache.glob("fredv_*")))

    def test_d3_missing_ignores_dates_before_observation_start(self):
        r = self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-07-01")
        self.assertEqual(r["missing"], [])
        self.assertFalse(r["short"])

    def test_d3_holiday_dot_is_not_missing(self):
        r = self.f.fred_fetch_vintage("DGS10", 10, observation_start="2026-09-15")
        self.assertFalse(r["short"], r["missing"])
        self.assertNotIn("2026-09-17", [x["date"] for x in r["rows"]])

    # --- ❌1 (result read CE-2): a sparse series must fill `limit` or say it did not -----
    def test_sparse_series_derived_window_fills_limit(self):
        r = self.f.fred_fetch_vintage("SPARSE", 10)
        self.assertNotIn("error", r)
        self.assertEqual(len(r["rows"]), 10)
        self.assertFalse(r["under_limit"])

    def test_explicit_short_window_reports_under_limit_and_is_not_cached(self):
        r = self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-07-01")
        self.assertEqual(len(r["rows"]), 2)
        self.assertTrue(r["under_limit"])
        self.assertFalse(list(self.cache.glob("fredv_*")))

    def test_zero_rows_is_an_error(self):
        r = self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-09-01")
        self.assertIn("error", r)
        self.assertFalse(list(self.cache.glob("fredv_*")))

    # --- D4/❌12/A3: cache keys, never cache a failure -----------------------------------
    def test_d4_success_cached_then_served_without_a_request(self):
        self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-05-01")
        files = list(self.cache.glob("fredv_*"))
        self.assertEqual(len(files), 1)
        n = len(self.fake.calls)
        again = self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-05-01")
        self.assertEqual(len(self.fake.calls), n)
        self.assertEqual(again["basis"], "first-published")

    def test_d4_every_param_in_key(self):
        self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-05-01")
        self.f.fred_fetch_vintage("PAYEMS", 3, observation_start="2026-05-01")
        self.f.fred_fetch_vintage("PAYEMS", 3, observation_start="2026-06-01")   # 3 rows fit
        self.assertEqual(len(list(self.cache.glob("fredv_*"))), 3)
        self.assertEqual(len(self.vintage_calls()), 3)

    def test_a3_latest_revised_cache_never_serves_vintage(self):
        # a latest-revised entry under the old key shape must not be read by the vintage path
        self.f._cache_set("fred_PAYEMS_4", [{"date": "2026-07-01", "value": "158913"}])
        r = self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-05-01")
        self.assertEqual(len(self.vintage_calls()), 1)
        self.assertEqual([x for x in r["rows"] if x["date"] == "2026-07-01"][0]["value"], "158858")
        self.assertEqual(self.f._cache_get("fred_PAYEMS_4"), [{"date": "2026-07-01", "value": "158913"}])

    def test_d4_error_never_cached(self):
        self.fake.fail = "HTTP 500: upstream"
        r = self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-05-01")
        self.assertIn("error", r)
        self.assertFalse(list(self.cache.glob("fredv_*")))

    def test_cap_400_is_explicit_and_names_the_window(self):
        self.fake.cap_error = True
        r = self.f.fred_fetch_vintage("DGS10", 5, observation_start="2015-01-01")
        self.assertIn("2000", r["error"])
        self.assertIn("2014-12-18", r["error"])      # realtime_start of the window it tried
        self.assertEqual(len(self.vintage_calls()), 1)  # no silent narrower retry
        self.assertEqual(r["rows"], [])

    # --- ⚠️13: the key never leaves the request ------------------------------------------
    def test_api_key_absent_from_result_and_cache(self):
        r = self.f.fred_fetch_vintage("PAYEMS", 4, observation_start="2026-05-01")
        self.assertNotIn("SECRET-FIXTURE-KEY", json.dumps(r))
        self.assertNotIn("api_key", r["request"])
        for p in self.cache.glob("*"):
            self.assertNotIn("SECRET-FIXTURE-KEY", p.read_text())

    # --- ⚠️11: TTL class -------------------------------------------------------------------
    def test_ttl_fredv_is_econ_even_with_a_ticker_substring(self):
        self.assertEqual(self.f._cache_ttl("fredv_PAYEMS_first-published_x_y_z_4"), self.f.CACHE_TTL_ECON)
        self.assertEqual(self.f._cache_ttl("fredv_VIXCLS_first-published_x_y_z_4"), self.f.CACHE_TTL_ECON)

    def test_cache_dir_override(self):
        self.assertEqual(self.f.CACHE_DIR, self.cache)

    # --- CLI opt-in; default path untouched ------------------------------------------------
    def run_cli(self, *argv):
        buf, err = io.StringIO(), io.StringIO()
        rc = 0
        with patch.object(sys, "argv", ["fetch.py", *argv]), \
                contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
            try:
                self.f.main()
            except SystemExit as e:
                rc = e.code or 0
        return rc, buf.getvalue(), err.getvalue()

    def test_cli_first_published_json(self):
        rc, out, _ = self.run_cli("fred", "PAYEMS", "--periods", "2", "--first-published", "--json")
        self.assertEqual(rc, 0)
        d = json.loads(out)
        self.assertEqual(d["basis"], "first-published")
        self.assertEqual(d["rows"][0]["date"], "2026-08-01")

    def test_cli_first_published_error_exits_3(self):
        self.fake.fail = "HTTP 500: upstream"
        rc, _, err = self.run_cli("fred", "PAYEMS", "--first-published")
        self.assertEqual(rc, 3)
        self.assertIn("first-published", err)

    def test_cli_default_does_not_touch_vintage_path(self):
        with patch.object(self.f, "fred_fetch", return_value=[{"date": "2026-09-22", "value": "4.96"}]):
            rc, out, _ = self.run_cli("fred", "DGS10", "--json")
        self.assertEqual(rc, 0)
        self.assertEqual(json.loads(out)["observations"], [{"date": "2026-09-22", "value": "4.96"}])
        self.assertEqual(self.fake.calls, [])


@unittest.skipUnless(os.environ.get("L409_LIVE") == "1", "live FRED pulls: set L409_LIVE=1")
class Live(unittest.TestCase):
    """Declared gate series pull under the default window rule; D8 freshness in one run."""

    def setUp(self):
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        tmp = self.stack.enter_context(tempfile.TemporaryDirectory())
        self.stack.enter_context(patch.dict(os.environ, {"FORGE_CACHE_DIR": tmp, "MKTDATA_REEXEC": "1"}))
        spec = importlib.util.spec_from_file_location("l409_live_fetch", LIVE_SOURCE)
        self.f = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.f)   # real .env for the key
        self.stack.enter_context(patch.object(self.f, "_audit_log"))

    def test_declared_series_default_window(self):
        for sid in ("BAMLH0A0HYM2", "DGS10", "DFII10", "PAYEMS", "IORB"):
            with self.subTest(sid=sid):
                r = self.f.fred_fetch_vintage(sid, 5)
                self.assertNotIn("error", r, r.get("error"))
                self.assertEqual(len(r["rows"]), 5)
                self.assertFalse(r["short"], r["missing"])

    def test_payems_discriminates(self):
        fp = {x["date"]: x["value"] for x in self.f.fred_fetch_vintage("PAYEMS", 6)["rows"]}
        lr = {x["date"]: x["value"] for x in self.f.fred_fetch("PAYEMS", 6)}
        self.assertTrue(any(fp[d] != lr.get(d) for d in fp), (fp, lr))

    def test_d8_newest_date_agrees_across_limits_and_an_independent_probe(self):
        import urllib.parse, urllib.request
        for sid in ("DGS10", "BAMLH0A0HYM2"):
            with self.subTest(sid=sid):
                q = urllib.parse.urlencode({"series_id": sid, "api_key": self.f.FRED_API_KEY,
                                            "file_type": "json", "sort_order": "desc", "limit": 1})
                with urllib.request.urlopen(f"{self.f.FRED_BASE}?{q}", timeout=20) as resp:
                    probe = json.loads(resp.read())["observations"][0]["date"]
                a = self.f.fred_fetch(sid, 2)[0]["date"]
                b = self.f.fred_fetch(sid, 20000)[0]["date"]
                c = self.f.fred_fetch_vintage(sid, 2)["rows"][0]["date"]
                self.assertEqual({a, b, c}, {probe}, (a, b, c, probe))


if __name__ == "__main__":
    unittest.main(verbosity=2)
