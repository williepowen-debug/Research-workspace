"""Offline regression checks for dated F-B grading."""
import contextlib
import datetime as dt
import importlib.util
import io
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch
from zoneinfo import ZoneInfo

spec = importlib.util.spec_from_file_location("fb_grade_review", Path(__file__).parents[1] / "fb_grade.py")
fb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fb)

class FBGradeTests(unittest.TestCase):
    def prices(self):
        return {d: 100.0 for d in [fb.BASE_DATE] + fb.WINDOW}

    def run_grade(self, values, day="2026-09-17"):
        prices = {dt.datetime.fromisoformat(d): v for d, v in values.items()}
        yf = types.SimpleNamespace(Ticker=lambda symbol: types.SimpleNamespace(history=lambda **kwargs: {"Close": prices}))
        now = dt.datetime.fromisoformat(day + "T12:00:00").replace(tzinfo=ZoneInfo("America/New_York"))
        out = io.StringIO()
        with patch.dict(sys.modules, {"yfinance": yf}), patch.object(fb, "now_et", return_value=now, create=True), contextlib.redirect_stdout(out):
            rc = fb.main([])
        return rc, out.getvalue()

    def test_final_day_intraday_bar_cannot_resolve(self):
        rc, out = self.run_grade(self.prices(), "2026-09-16")
        self.assertEqual(rc, 0)
        self.assertIn("IN PROGRESS", out)
        self.assertNotIn("F-B HELD", out)

    def test_invalid_close_is_unknown(self):
        for value in (float("nan"), float("inf"), 0.0, -1.0):
            with self.subTest(value=value):
                prices = self.prices()
                prices[fb.WINDOW[1]] = value
                self.assertEqual(self.run_grade(prices)[0], 2)

    def test_missing_elapsed_session_is_not_bridged(self):
        prices = self.prices()
        del prices[fb.WINDOW[1]]
        self.assertEqual(self.run_grade(prices)[0], 2)

    def test_complete_window_can_hold_or_refute(self):
        self.assertIn("F-B HELD", self.run_grade(self.prices())[1])
        prices = {d: 100 * 1.03 ** n for n, d in enumerate([fb.BASE_DATE] + fb.WINDOW)}
        rc, out = self.run_grade(prices)
        self.assertEqual(rc, 1)
        self.assertIn("F-B REFUTED", out)

if __name__ == "__main__":
    unittest.main()
