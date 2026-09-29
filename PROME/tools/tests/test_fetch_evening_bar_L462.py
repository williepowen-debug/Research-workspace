#!/usr/bin/env python3
"""L462 — futures EVENING-BAR detector: fixtures only, NO network.

Acceptance conditions: PROME/tools/tests/ACCEPTANCE_fetch_evening_bar_L462_2026-09-29.md (A–F).
Every test loads an isolated copy of fetch.py with a fake yfinance; nothing reads the live
cache, credentials or audit log. FETCH_REVIEW_SOURCE selects an exported revision.

    python3 -W error::ResourceWarning PROME/tools/tests/test_fetch_evening_bar_L462.py
"""
import contextlib
import datetime
import importlib.util
import io
import os
import pathlib
import sys
import tempfile
import types
import unittest
from unittest.mock import patch
from zoneinfo import ZoneInfo

SOURCE = pathlib.Path(os.environ.get("FETCH_REVIEW_SOURCE", str(
    pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/fetch.py"
))).resolve()
ET = ZoneInfo("America/New_York")


def et(y, m, d, hh, mm, ss=0):
    """Epoch seconds for a wall-clock time in America/New_York."""
    return int(datetime.datetime(y, m, d, hh, mm, ss, tzinfo=ET).timestamp())


class EveningBar(unittest.TestCase):
    def setUp(self):
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(patch.dict(os.environ, {
            "MKTDATA_REEXEC": "1", "FRED_API_KEY": "offline-fixture-only", "FORGE_CACHE_DIR": ""}))
        temp = pathlib.Path(self.stack.enter_context(tempfile.TemporaryDirectory()))
        module_path = temp / "FORGE/tools/market-data/fetch.py"
        module_path.parent.mkdir(parents=True)
        module_path.write_bytes(SOURCE.read_bytes())
        spec = importlib.util.spec_from_file_location("l462_fetch", module_path)
        self.fetch = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.fetch)
        self.stack.enter_context(patch.object(self.fetch, "_audit_log"))
        self.stack.enter_context(patch.object(self.fetch, "_cache_get", return_value=None))
        self.stack.enter_context(patch.object(self.fetch, "_cache_set"))
        owner = self
        # per-symbol vendor state: (metadata dict, bar dates, fast_info dict)
        self.vendor = {}

        class History:
            def __init__(self, dates):
                self.index = [datetime.datetime(*d, tzinfo=ET) for d in dates]
                self.empty = not dates

            def __len__(self):
                return len(self.index)

        class Ticker:
            def __init__(self, symbol):
                self.symbol = symbol

            @property
            def fast_info(self):
                return owner.vendor[self.symbol]["fast_info"]

            @property
            def history_metadata(self):
                return owner.vendor[self.symbol]["md"]

            def history(self, **kwargs):
                return History(owner.vendor[self.symbol]["bars"])

        yf = types.ModuleType("yfinance")
        yf.Ticker = Ticker
        self.stack.enter_context(patch.dict(sys.modules, {"yfinance": yf}))

    # --- fixtures --------------------------------------------------------------------
    def future(self, sym="BZX26.NYM", last_trade=et(2026, 9, 23, 12, 0), bars=((2026, 9, 22), (2026, 9, 23)),
               price=102.38, prev=99.25, tz="America/New_York", md_extra=None, drop=()):
        md = {"symbol": sym, "regularMarketPrice": price, "regularMarketTime": last_trade,
              "shortName": "Brent Crude Oil Last Day Financ", "instrumentType": "FUTURE",
              "exchangeTimezoneName": tz, "gmtoffset": -14400}
        md.update(md_extra or {})
        for k in drop:
            md.pop(k, None)
        self.vendor[sym] = {"md": md, "bars": list(bars),
                            "fast_info": {"lastPrice": price, "regularMarketPreviousClose": prev,
                                          "previousClose": prev, "lastVolume": 612}}
        return sym

    def equity(self, sym="TLT", last_trade=et(2026, 9, 23, 20, 47), bars=((2026, 9, 22), (2026, 9, 23)),
               price=80.10, prev=80.46):
        md = {"symbol": sym, "regularMarketPrice": price, "regularMarketTime": last_trade,
              "shortName": "iShares 20+ Year Treasury Bond ETF", "instrumentType": "ETF",
              "exchangeTimezoneName": "America/New_York", "gmtoffset": -14400}
        self.vendor[sym] = {"md": md, "bars": list(bars),
                            "fast_info": {"lastPrice": price, "regularMarketPreviousClose": prev,
                                          "previousClose": prev, "lastVolume": 1000}}
        return sym

    def fetch_one(self, sym):
        return self.fetch.price_fetch([sym])[sym]

    # --- A / ordinary ----------------------------------------------------------------
    def test_day_session_future_is_day_with_change(self):
        r = self.fetch_one(self.future())
        self.assertEqual(r["session"], "day")
        self.assertEqual(r["asof"], "2026-09-23")
        self.assertIsNotNone(r["change_pct"])
        self.assertIn("regularMarketPreviousClose", r["change_basis"])

    def test_evening_trade_is_next_session_and_change_withheld(self):
        # BRENT 2026-09-23 20:47 ET: the "9/23" bar was the 9/24 evening session.
        r = self.fetch_one(self.future(last_trade=et(2026, 9, 23, 20, 47)))
        self.assertEqual(r["session"], "evening-next-session")
        self.assertEqual(r["trade_date"], "2026-09-24")
        self.assertEqual(r["price"], 102.38)                 # price survives (B)
        self.assertIsNone(r["change_pct"])                   # change withheld (B)
        self.assertIn("withheld", r["change_basis"])
        self.assertIn("2026-09-23", r["session_basis"])

    # --- overlap: the 17:00 boundary, Friday, Sunday-labelled bar -----------------------
    def test_boundary_1659_is_day_1700_is_evening(self):
        day = self.fetch_one(self.future(sym="CLX26.NYM", last_trade=et(2026, 9, 23, 16, 59, 59)))
        self.assertEqual(day["session"], "day")
        eve = self.fetch_one(self.future(sym="HOX26.NYM", last_trade=et(2026, 9, 23, 17, 0, 0)))
        self.assertEqual(eve["session"], "evening-next-session")

    def test_friday_evening_trade_date_is_monday(self):
        # 2026-09-25 is a Friday; the evening session that opens Sunday 18:00 belongs to Mon 9/28,
        # but a Friday-evening stamp (none should exist on CME) still maps to the next weekday.
        r = self.fetch_one(self.future(last_trade=et(2026, 9, 25, 18, 5), bars=((2026, 9, 24), (2026, 9, 25))))
        self.assertEqual(r["session"], "evening-next-session")
        self.assertEqual(r["trade_date"], "2026-09-28")

    def test_holiday_skipped_in_trade_date(self):
        # 2026-09-04 (Fri) evening: Mon 9/07 is Labor Day in US_MARKET_HOLIDAYS => Tue 9/08.
        r = self.fetch_one(self.future(last_trade=et(2026, 9, 4, 18, 30), bars=((2026, 9, 3), (2026, 9, 4))))
        self.assertEqual(r["trade_date"], "2026-09-08")

    def test_sunday_labelled_bar_is_non_session_date(self):
        # 2026-09-27 is a Sunday: a bar carrying that date is not a session.
        r = self.fetch_one(self.future(last_trade=et(2026, 9, 27, 19, 0), bars=((2026, 9, 25), (2026, 9, 27))))
        self.assertEqual(r["session"], "non-session-date")
        self.assertIsNone(r["change_pct"])

    # --- C: equities untouched -----------------------------------------------------------
    def test_equity_after_hours_untouched(self):
        r = self.fetch_one(self.equity())
        self.assertNotIn("session", r)
        self.assertNotIn("change_basis", r)
        self.assertAlmostEqual(r["change_pct"], round((80.10 - 80.46) / 80.46 * 100, 2))
        self.assertEqual(r["asof"], "2026-09-23")

    # --- F: loud on missing information --------------------------------------------------
    def test_missing_regular_market_time_is_unverified_price_kept(self):
        r = self.fetch_one(self.future(drop=("regularMarketTime",)))
        self.assertEqual(r["session"], "unverified")
        self.assertEqual(r["price"], 102.38)
        self.assertIsNone(r["change_pct"])
        self.assertIn("regularMarketTime", r["session_basis"])

    def test_unresolvable_timezone_falls_back_to_gmtoffset(self):
        r = self.fetch_one(self.future(last_trade=et(2026, 9, 23, 20, 47), tz="Not/AZone"))
        self.assertEqual(r["session"], "evening-next-session")
        self.assertIn("gmtoffset", r["session_basis"])

    def test_no_timezone_at_all_is_unverified(self):
        r = self.fetch_one(self.future(last_trade=et(2026, 9, 23, 20, 47), tz="Not/AZone", drop=("gmtoffset",)))
        self.assertEqual(r["session"], "unverified")

    # --- renderer: A on the CLI, E on a pre-fix cache entry ---------------------------------
    def render(self, results):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), \
                patch.object(self.fetch.time, "strftime", side_effect=lambda f, *a: "2026-09-23" if f == "%Y-%m-%d" and not a else "x"):
            self.fetch.display_prices(results)
        return buf.getvalue()

    def test_display_marks_evening_bar_never_plain_today(self):
        r = self.fetch_one(self.future(last_trade=et(2026, 9, 23, 20, 47)))
        out = self.render({"BZX26.NYM": r})
        self.assertIn("09-23⚠eve→09-24", out)
        self.assertNotIn(" 2026-09-23 ", out.split("BZX26.NYM")[1].split("\n")[0] + " ")

    def test_display_prefix_cache_entry_unchanged(self):
        prefix = {"price": 102.38, "prev": 99.25, "change_pct": 3.15, "name": "Brent", "asof": "2026-09-23",
                  "contract_month": None, "contract_basis": "x", "is_future": True}
        out = self.render({"BZX26.NYM": prefix})
        self.assertNotIn("eve→", out)
        self.assertIn("+3.15%", out)                          # the cached figure prints as cached ...
        self.assertIn("⚠pre-fix", out)                        # ... but never as a verified day bar (E)
        self.assertIn("pre-L462 cache entry", out)
        eq = self.render({"TLT": {"price": 80.1, "prev": 80.46, "change_pct": -0.45, "name": "TLT", "asof": "2026-09-23"}})
        self.assertNotIn("pre-fix", eq)                       # equities untouched (C)

    def test_millisecond_epoch_is_unverified_not_history_failure(self):
        # result-read counterexample: a ms epoch raised 'year out of range' and escaped into the
        # history-failure branch, whose stated cause ("metadata unavailable") was false.
        r = self.fetch_one(self.future(last_trade=et(2026, 9, 23, 20, 47) * 1000))
        self.assertEqual(r["session"], "unverified")
        self.assertIn("not a usable epoch", r["session_basis"])
        self.assertEqual(r["asof"], "2026-09-23")             # history was NOT lost
        self.assertIsNone(r["change_pct"])


# --- dashboard.py side (conditions A/B/E on the Will-facing surface) ------------------------
DASH = pathlib.Path(os.environ.get("DASHBOARD_REVIEW_SOURCE", str(
    pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/dashboard.py"
))).resolve()
TODAY = "2026-09-23"


def _load_dashboard():
    fake_fetch = types.ModuleType("fetch")
    fake_fetch.fred_fetch = lambda *a, **k: []
    fake_fetch.price_fetch = lambda *a, **k: {}
    fake_fetch.eia_fetch = lambda *a, **k: []
    fake_config = types.ModuleType("config")
    fake_config.SERIES = []
    fake_config.classify = lambda v, s: "green"
    fake_config.get_emoji = lambda z: "🟢"
    fake_config.get_tier = fake_config.get_agent = lambda *a: None
    fake_config.format_value = lambda v, s: f"{v}"
    with patch.dict(sys.modules, {"fetch": fake_fetch, "config": fake_config,
                                  "yfinance": types.ModuleType("yfinance")}), \
            patch.dict(os.environ, {"MKTDATA_REEXEC": "1"}):
        spec = importlib.util.spec_from_file_location("l462_dashboard", DASH)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    return mod


class DashboardEveningBar(unittest.TestCase):
    def setUp(self):
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.d = _load_dashboard()
        import time as _t
        real = _t.strftime
        self.stack.enter_context(patch.object(
            self.d.time, "strftime",
            side_effect=lambda fmt, *a: TODAY if fmt == "%Y-%m-%d" and not a else real(fmt, *a)))

    def entry(self, sid, **pd):
        s = {"name": sid, "agent": "X", "tier": 1, "direction": "higher_worse", "source": "price", "id": sid}
        with patch.object(self.d, "price_fetch", return_value={sid: pd}):
            return self.d.fetch_all([s])[0]

    def test_evening_bar_labelled_next_session_change_withheld(self):
        e = self.entry("BZX26.NYM", price=102.38, prev=99.25, change_pct=None, asof=TODAY, is_future=True,
                       session="evening-next-session", trade_date="2026-09-24",
                       change_basis="withheld: evening bar spans two sessions")
        self.assertEqual(self.d._date_stamp(e).split(" ")[0], "[9/23")
        self.assertIn("eve→9/24]", self.d._date_stamp(e))
        self.assertIsNone(e["change"])
        self.assertEqual(e["value"], 102.38)                    # price and zone stand
        self.assertNotIn("⚠stale", e["flags"])
        self.assertIn("⚠evening bar, Δ withheld", e["flags"])

    def test_relabelled_bar_dated_tomorrow_is_not_stale(self):
        e = self.entry("BZX26.NYM", price=102.38, prev=99.25, change_pct=None, asof="2026-09-24", is_future=True,
                       session="evening-next-session", trade_date="2026-09-24", change_basis="withheld: x")
        self.assertNotIn("⚠stale", e["flags"])
        self.assertIn("[9/24 eve→9/24]", self.d._date_stamp(e))

    def test_day_bar_unchanged(self):
        e = self.entry("BZX26.NYM", price=103.39, prev=105.28, change_pct=-1.8, asof=TODAY, is_future=True,
                       session="day", trade_date=TODAY, change_basis="regularMarketPreviousClose (prior bar 2026-09-22)")
        self.assertEqual(self.d._date_stamp(e), "[9/23]")
        self.assertAlmostEqual(e["change"], -1.89)
        self.assertEqual(e["flags"], [])

    def test_day_bar_with_prior_gap_withholds_change(self):
        e = self.entry("BZX26.NYM", price=103.39, prev=105.28, change_pct=None, asof=TODAY, is_future=True,
                       session="day", trade_date=TODAY, change_basis="withheld: prior bar is '2026-09-21', expected 2026-09-22")
        self.assertIsNone(e["change"])
        self.assertIn("⚠prior bar missing, Δ withheld", e["flags"])

    def test_prefix_cache_futures_row_is_marked_not_verified(self):
        e = self.entry("BZX26.NYM", price=102.38, prev=99.25, change_pct=3.15, asof=TODAY, is_future=True)
        self.assertIn("⚠pre-L462 cache, re-pull --no-cache", e["flags"])
        self.assertAlmostEqual(e["change"], 3.13)               # renders as before, but marked

    def test_equity_row_untouched(self):
        e = self.entry("TLT", price=80.10, prev=80.46, change_pct=-0.45, asof=TODAY)
        self.assertEqual(e["flags"], [])
        self.assertNotIn("session", e)
        self.assertEqual(self.d._date_stamp(e), "[9/23]")


if __name__ == "__main__":
    unittest.main(verbosity=1)
