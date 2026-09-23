#!/usr/bin/env python3
"""L409 D6/D7 — FORGE dashboard.py stale marks and two-leg spread dating: fixtures.

Plan: PROME/plans/2026-09-22_L409-market-data-vintage-repair-PLAN.md (A6, A7, ⚠️17).
Offline: dashboard.py is loaded from DASHBOARD_REVIEW_SOURCE (default: the live file) with
fetch/config stubbed, so no network, cache, state file or credential is touched.
"""
import contextlib
import importlib.util
import os
import pathlib
import sys
import time
import types
import unittest
from unittest.mock import patch

SOURCE = pathlib.Path(os.environ.get("DASHBOARD_REVIEW_SOURCE", str(
    pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/dashboard.py"
))).resolve()
TODAY = "2026-09-23"


def load_dashboard():
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
    # yfinance stub: a copy loaded outside the repo has no .venv beside it, so the
    # self-heal probe would import the real package; the stub keeps the load offline.
    with patch.dict(sys.modules, {"fetch": fake_fetch, "config": fake_config,
                                  "yfinance": types.ModuleType("yfinance")}), \
            patch.dict(os.environ, {"MKTDATA_REEXEC": "1"}):
        spec = importlib.util.spec_from_file_location("l409_dashboard", SOURCE)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    return mod


def series(sid, source="price"):
    return {"name": str(sid), "agent": "X", "tier": 1, "direction": "higher_worse",
            "source": source, "id": sid}


def obs(*pairs):
    return [{"date": d, "value": v} for d, v in pairs]


class Marks(unittest.TestCase):
    def setUp(self):
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.d = load_dashboard()
        real = time.strftime
        self.stack.enter_context(patch.object(
            self.d.time, "strftime",
            side_effect=lambda fmt, *a: TODAY if fmt == "%Y-%m-%d" and not a else real(fmt, *a)))

    def price(self, sid, **pd):
        with patch.object(self.d, "price_fetch", return_value={sid: pd}):
            return self.d.fetch_all([series(sid)])[0]

    def spread(self, a, b):
        tables = {"A": a, "B": b}
        with patch.object(self.d, "fred_fetch", side_effect=lambda sid, limit=5: tables[sid][:limit]):
            return self.d.fetch_all([series(["A", "B"], "fred_spread")])[0]

    # --- D6 ------------------------------------------------------------------------------
    def test_stale_asof_marked(self):
        e = self.price("KRE", price=70.0, prev=71.0, asof="2026-09-22")
        self.assertIn("⚠stale", e["flags"])
        self.assertIn("⚠stale", self.d._date_stamp(e))

    def test_today_asof_unmarked(self):
        e = self.price("KRE", price=70.0, prev=71.0, asof=TODAY)
        self.assertEqual(e["flags"], [])
        self.assertEqual(self.d._date_stamp(e), "[9/23]")

    def test_missing_asof_is_date_query_not_live(self):
        e = self.price("KRE", price=70.0, prev=71.0, asof=None)
        self.assertEqual(self.d._date_stamp(e), "date?")

    def test_vol_zero_change_flagged(self):
        e = self.price("^MOVE", price=76.22, prev=76.22, asof=TODAY)
        self.assertIn("⚠Δ≈0 possible fill-forward", e["flags"])

    def test_vol_nonzero_change_not_flagged_and_nonvol_zero_not_flagged(self):
        self.assertEqual(self.price("^VIX", price=15.18, prev=14.87, asof=TODAY)["flags"], [])
        self.assertEqual(self.price("KRE", price=70.0, prev=70.0, asof=TODAY)["flags"], [])

    # --- D7 ------------------------------------------------------------------------------
    def test_spread_aligns_on_latest_common_date(self):
        # IORB-style leg B stamped ahead of leg A (the SOFR-IORB counterexample)
        a = obs(("2026-09-22", "3.87"), ("2026-09-21", "3.85"))
        b = obs(("2026-09-24", "4.15"), ("2026-09-23", "4.15"), ("2026-09-22", "3.90"), ("2026-09-21", "3.90"))
        e = self.spread(a, b)
        self.assertEqual(e["date"], "2026-09-22")
        self.assertAlmostEqual(e["value"], -0.03)        # 3.87 − 3.90, same date; NOT 3.87 − 4.15
        self.assertAlmostEqual(e["prev"], -0.05)
        self.assertEqual(e["legs"], {"A": "2026-09-22", "B": "2026-09-24"})
        self.assertEqual(e["flags"], [])

    def test_spread_leg_a_ahead_is_not_the_date(self):
        # The pre-L409 code dated the spread by leg A; here leg A is AHEAD of leg B.
        a = obs(("2026-09-23", "4.30"), ("2026-09-22", "4.20"))
        b = obs(("2026-09-22", "4.00"), ("2026-09-21", "3.95"))
        e = self.spread(a, b)
        self.assertEqual(e["date"], "2026-09-22")
        self.assertAlmostEqual(e["value"], 0.20)
        self.assertIsNone(e["prev"])                      # only one common date in the rows

    def test_spread_no_common_date_shows_both_and_no_value(self):
        a = obs(("2026-09-22", "3.87"))
        b = obs(("2026-09-24", "3.90"))
        e = self.spread(a, b)
        self.assertIsNone(e["value"])
        self.assertEqual(self.d._date_stamp(e), "a 2026-09-22 / b 2026-09-24")
        self.assertIn("error", e)

    def test_spread_multi_session_gap_marked(self):
        a = obs(("2026-09-21", "4.20"), ("2026-09-11", "4.10"))     # DCPF3M '.' gap
        b = obs(("2026-09-21", "4.15"), ("2026-09-18", "4.12"), ("2026-09-11", "4.11"))
        e = self.spread(a, b)
        self.assertEqual(e["change_span"], 6)
        self.assertIn("Δ over 6 sessions", self.d._date_stamp(e))

    def test_spread_adjacent_sessions_unmarked(self):
        a = obs(("2026-09-21", "4.20"), ("2026-09-18", "4.10"))     # Fri → Mon = 1 session
        b = obs(("2026-09-21", "4.15"), ("2026-09-18", "4.12"))
        self.assertEqual(self.spread(a, b)["flags"], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
