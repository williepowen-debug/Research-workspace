#!/usr/bin/env python3
"""L925 open half: a `day` futures bar dated today with an old last trade is marked.
Acceptance: ACCEPTANCE_fetch_day_age_L925_2026-11-08.md. No network, no yfinance call."""
import contextlib
import datetime
import importlib.util
import io
import pathlib
import sys
import types
import unittest
from unittest.mock import patch
from zoneinfo import ZoneInfo

PATH = pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/fetch.py"
ET = ZoneInfo("America/New_York")


def load():
    sys.modules.setdefault("yfinance", types.ModuleType("yfinance"))
    spec = importlib.util.spec_from_file_location("fetch_l925_age", PATH)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def et(y, m, d, hh, mm, ss=0):
    return int(datetime.datetime(y, m, d, hh, mm, ss, tzinfo=ET).timestamp())


def md(last_trade, price=95.0):
    return {"regularMarketPrice": price, "regularMarketTime": last_trade,
            "exchangeTimezoneName": "America/New_York", "gmtoffset": -18000}


class DayAge(unittest.TestCase):
    def setUp(self):
        self.f = load()

    def sess(self, last, now, asof="2026-11-09", prev="2026-11-06"):
        return self.f.futures_bar_session(md(last), asof, prev, 95.0, now=now)

    # condition 1 + 2: ordinary — 09:00 trade read at 13:00 on the bar date
    def test_morning_trade_read_in_afternoon_is_flagged(self):
        r = self.sess(et(2026, 11, 9, 9, 0), et(2026, 11, 9, 13, 0))
        self.assertEqual(r["session"], "day")
        self.assertEqual(r["last_trade_age_min"], 240.0)
        self.assertTrue(r["age_flag"])
        self.assertFalse(r["withhold"])                       # price and change kept

    # condition 3: boundary at the limit
    def test_at_limit_is_clean_just_over_is_flagged(self):
        at = self.sess(et(2026, 11, 9, 12, 15), et(2026, 11, 9, 13, 0))
        self.assertEqual(at["last_trade_age_min"], 45.0)
        self.assertFalse(at["age_flag"])
        over = self.sess(et(2026, 11, 9, 12, 14, 54), et(2026, 11, 9, 13, 0))
        self.assertTrue(over["age_flag"])

    # condition 4: a bar dated before today is never age-flagged (⚠stale covers it)
    def test_prior_day_bar_not_age_flagged(self):
        r = self.sess(et(2026, 11, 6, 9, 0), et(2026, 11, 9, 13, 0), asof="2026-11-06", prev="2026-11-05")
        self.assertEqual(r["session"], "day")
        self.assertGreater(r["last_trade_age_min"], 45)
        self.assertFalse(r["age_flag"])

    # condition 4: evening row carries the age, never the flag
    def test_evening_row_carries_age_not_flag(self):
        r = self.sess(et(2026, 11, 8, 18, 5), et(2026, 11, 8, 20, 0))
        self.assertEqual(r["session"], "evening-next-session")
        self.assertIn("last_trade_age_min", r)
        self.assertFalse(r["age_flag"])

    # condition 5: vendor clock ahead of ours
    def test_negative_age_never_flagged(self):
        r = self.sess(et(2026, 11, 9, 13, 5), et(2026, 11, 9, 13, 0))
        self.assertEqual(r["last_trade_age_min"], -5.0)
        self.assertFalse(r["age_flag"])

    # "today" is the ET date of the clock, not UTC: 19:30 ET on 11/9 is already 11/10 UTC
    def test_today_is_et_not_utc(self):
        r = self.sess(et(2026, 11, 8, 23, 0), et(2026, 11, 8, 23, 50), asof="2026-11-08")
        self.assertEqual(r["session"], "non-session-date")    # Sunday bar: never flagged
        r = self.sess(et(2026, 11, 9, 9, 0), et(2026, 11, 9, 16, 59))
        self.assertTrue(r["age_flag"])

    # read ❌1: after the 17:00 close the bar is final or in the halt, never "frozen"
    def test_after_close_never_flagged(self):
        fri = self.sess(et(2026, 11, 13, 16, 59), et(2026, 11, 13, 19, 0), asof="2026-11-13", prev="2026-11-12")
        self.assertEqual(fri["session"], "day")
        self.assertEqual(fri["last_trade_age_min"], 121.0)
        self.assertFalse(fri["age_flag"])
        halt = self.sess(et(2026, 11, 9, 16, 0), et(2026, 11, 9, 17, 30))
        self.assertFalse(halt["age_flag"])

    # read ⚠5: a flagged 45.9 must not print as the clean-looking 45
    def test_stamp_rounds_up(self):
        out = self.render(self.row(last_trade_age_min=45.9, age_flag=True))
        self.assertIn("⚠46m old", out)

    # --- display -------------------------------------------------------------------
    def render(self, row, today="2026-11-09"):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), \
                patch.object(self.f.time, "strftime",
                             side_effect=lambda f, *a: today if f == "%Y-%m-%d" and not a else "x"):
            self.f.display_prices({"CLZ26.NYM": row})
        return buf.getvalue()

    def row(self, **kw):
        d = {"price": 95.0, "prev": 94.0, "change_pct": 1.06, "name": "Crude", "asof": "2026-11-09",
             "contract_month": "2026-12", "contract_basis": "x", "is_future": True, "session": "day",
             "trade_date": "2026-11-09", "session_basis": "day session; b",
             "change_basis": "regularMarketPreviousClose (prior bar 2026-11-06)"}
        d.update(kw)
        return d

    def test_flagged_row_shows_mark_and_note(self):
        out = self.render(self.row(last_trade_age_min=240.0, age_flag=True))
        self.assertIn("⚠240m old", out)
        self.assertIn("may be frozen", out)
        self.assertIn("+1.06%", out)                          # change kept

    def test_fresh_row_prints_as_before(self):
        out = self.render(self.row(last_trade_age_min=8.0, age_flag=False))
        self.assertNotIn("m old", out)
        self.assertNotIn("frozen", out)
        legacy = self.render(self.row())                       # rows without the new keys
        self.assertNotIn("m old", legacy)

    def test_gap_and_age_both_shown(self):
        out = self.render(self.row(change_pct=None, last_trade_age_min=120.0, age_flag=True,
                                   change_basis="withheld: prior bar None is absent; expected 2026-11-06"))
        self.assertIn("⚠gap", out)
        self.assertIn("⚠120m old", out)
        self.assertIn("may be frozen", out)
        self.assertIn("withheld: prior bar", out)


if __name__ == "__main__":
    unittest.main()
