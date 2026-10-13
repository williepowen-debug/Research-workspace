"""Exercise input failures and actual watch output; do not mirror band formulas."""
from contextlib import redirect_stdout, redirect_stderr
from datetime import date, datetime, timezone
import io
import unittest
from unittest.mock import patch

import metals_watch as watch


class CapturedDatetime(datetime):
    @classmethod
    def now(cls, tz=None):
        captured = cls(2026, 10, 12, 23, 0, tzinfo=timezone.utc)
        return captured.astimezone(tz) if tz else captured.replace(tzinfo=None)


def history(close, volume=100000):
    return {"history": [dict(date=d, close=c, volume=volume) for d, c in
                        [("2026-07-10", close * 1.15), ("2026-09-11", close * 1.08),
                         ("2026-09-17", close * 1.05), ("2026-09-18", close * 1.04),
                         ("2026-09-25", close * 1.02), ("2026-10-02", close * 1.01),
                         ("2026-10-08", close), ("2026-10-09", close),
                         ("2026-10-12", close), ("2026-10-13", close * 1.5)]]}


class InputTests(unittest.TestCase):
    def setUp(self):
        prices = {"GC=F": 4200., "SI=F": 60., "HG=F": 6., "PL=F": 1700., "PA=F": 1150.}
        self.data = {front: history(prices[ptr]) for ptr, front in watch.FRONT_MONTHS.items()}
        self.data.update({ptr: history(prices[ptr], 10) for ptr in prices})
        self.data["GC=F"] = history(9000., 10)  # would manufacture GSR=150
        self.data["GLD"] = history(380.)
        self.obs = [dict(date="2026-10-08", value="2.45"),
                    dict(date="2026-10-02", value="2.43"),
                    dict(date="2026-09-25", value="2.41"),
                    dict(date="2026-09-18", value="2.39"),
                    dict(date="2026-09-17", value="2.40"),
                    dict(date="2026-09-11", value="2.38"),
                    dict(date="2026-07-10", value="2.00")]

    def snapshot(self):
        return watch.read_contract_snapshot(history=self.data, today=date(2026, 10, 12))

    def run_watch(self, inventory=233025):
        def read(tickers, days):
            return {t: self.data.get(t, {"error": "fixture missing"}) for t in tickers}
        rows = [("09. October 2026", inventory), ("08. October 2026", inventory - 10)]
        spots = {t: dict(price=100., prev=100., change_pct=0.) for t in watch.ETF_PROXIES}
        out, err = io.StringIO(), io.StringIO()
        with patch.object(watch.fetch, "price_history", side_effect=read), \
             patch.object(watch, "datetime", CapturedDatetime), \
             patch.object(watch, "read_contract_history", side_effect=read), \
             patch.object(watch.fetch, "fred_fetch", return_value=self.obs), \
             patch.object(watch, "read_real_yield", return_value=(self.obs[0], self.obs[-1])), \
             patch.object(watch, "read_spot", return_value=spots), \
             patch.object(watch, "contract_map_review", return_value=[]), \
             patch.object(watch, "read_lme_copper_stocks", return_value=(rows, rows[0], rows[-1])), \
             patch.object(watch, "read_lme_copper_baseline", return_value=(200000., 507, datetime(2026, 10, 9))), \
             redirect_stdout(out), redirect_stderr(err):
            rc = watch.main()
        return rc, out.getvalue(), err.getvalue()

    def test_wrong_pointer_cannot_manufacture_a_ratio_alarm(self):
        rc, out, err = self.run_watch()
        self.assertEqual(rc, 1)  # identity warning remains visible
        self.assertIn("GOLD/SILVER RATIO: 70.00", out)
        self.assertIn("current benign", out)
        self.assertNotIn("GOLD/SILVER RATIO: 150.00", out)
        self.assertIn("GCZ26.CMX", out)
        self.assertEqual(err, "")

    def test_genuine_named_contract_crossing_is_still_reported(self):
        self.data["SIZ26.CMX"] = history(40.)
        _, out, _ = self.run_watch()
        self.assertIn("GOLD/SILVER RATIO: 105.00", out)
        self.assertIn("current RED", out)

    def test_named_contract_failure_never_falls_back_to_pointer(self):
        self.data["SIZ26.CMX"] = {"error": "offline"}
        rc, out, err = self.run_watch()
        self.assertEqual(rc, 2)
        self.assertNotIn("GOLD/SILVER RATIO:", out)
        self.assertIn("GSR not graded", err)

    def test_pointer_failure_keeps_named_price_but_requires_review(self):
        self.data["GC=F"] = {"error": "pointer absent"}
        primary, _, flags = self.snapshot()
        self.assertEqual(watch.primary_gsr(primary), 70.)
        self.assertIn("GC=F", flags)

    def test_different_dates_block_the_ratio(self):
        self.data["SIZ26.CMX"]["history"][-2]["date"] = "2026-10-11"
        primary, _, _ = self.snapshot()
        with self.assertRaisesRegex(ValueError, "dates disagree"):
            watch.primary_gsr(primary)

    def test_different_delivery_months_block_the_ratio(self):
        primary, _, _ = self.snapshot()
        primary["SI=F"]["contract"] = "SIH27.CMX"
        with self.assertRaisesRegex(ValueError, "delivery months"):
            watch.primary_gsr(primary)

    def test_newest_mutable_bar_does_not_bind_price_or_ratio(self):
        primary, _, _ = self.snapshot()
        self.assertEqual(primary["GC=F"]["date"], "2026-10-12")
        self.assertEqual(primary["GC=F"]["price"], 4200.)

    def test_vendor_tick_precision_survives_the_adapter(self):
        import pandas as pd
        from types import SimpleNamespace
        frame = pd.DataFrame({"Close": [61.041, 61.048, 62.], "Volume": [100, 200, 300]},
                             index=pd.to_datetime(["2026-10-08", "2026-10-09", "2026-10-12"]))
        with patch("yfinance.Ticker", return_value=SimpleNamespace(history=lambda **kw: frame)):
            raw = watch.read_contract_history(["SIZ26.CMX"])
        self.assertEqual(watch._prior_vendor_bar(raw["SIZ26.CMX"])["close"], 61.048)

    def test_zero_volume_and_bad_close_are_unknown(self):
        self.data["SIZ26.CMX"] = history(60., 0)
        primary, _, _ = self.snapshot()
        self.assertIn("error", primary["SI=F"])
        self.data["SIZ26.CMX"] = history(float("nan"))
        primary, _, _ = self.snapshot()
        self.assertIn("error", primary["SI=F"])

    def test_duplicate_dates_are_not_silently_deduplicated(self):
        self.data["SIZ26.CMX"]["history"][-2]["date"] = "2026-10-09"
        primary, _, _ = self.snapshot()
        self.assertIn("error", primary["SI=F"])

    def test_expired_delivery_month_is_not_gradeable(self):
        primary, _, _ = watch.read_contract_snapshot(history=self.data, today=date(2027, 2, 1))
        self.assertTrue(all("error" in d for d in primary.values()))
        self.assertTrue(watch.contract_map_review(date(2027, 2, 1)))

    def test_stale_named_quote_is_not_current_just_because_contract_is_unexpired(self):
        primary, _, _ = watch.read_contract_snapshot(history=self.data, today=date(2026, 10, 30))
        self.assertIn("older than", primary["GC=F"]["error"])

    def test_mapping_a_different_metal_blocks_a_primary_price(self):
        primary, _, _ = watch.read_contract_snapshot(front_months={"GC=F": "PLF27.NYM"},
                                                     history=self.data, today=date(2026, 10, 12))
        self.assertIn("expected metal", primary["GC=F"]["error"])

    def test_weekly_map_review_is_visible(self):
        self.assertEqual(watch.contract_map_review(date(2026, 10, 12)), [])
        self.assertTrue(watch.contract_map_review(date(2026, 10, 19)))

    def test_inventory_crossing_does_not_invent_a_price_leg(self):
        _, out, _ = self.run_watch(inventory=420000)
        self.assertIn("Inventory leg REACHED", out)
        self.assertIn("Copper price leg UNMEASURED", out)
        self.assertNotIn("price UP = NOT firing", out)

    def test_red_inventory_leg_requires_review_with_a_clean_price_feed(self):
        for ptr, front in watch.FRONT_MONTHS.items():
            self.data[ptr] = self.data[front]
        rc, out, _ = self.run_watch(inventory=420000)
        self.assertEqual(rc, 1)
        self.assertIn("full price/inventory conjunction is not graded", out)

    def test_missing_gld_blocks_the_registered_shape(self):
        self.data["GLD"] = {"error": "GLD offline"}
        rc, _, err = self.run_watch()
        self.assertEqual(rc, 2)
        self.assertIn("GLD arbiter unavailable", err)

    def test_same_yield_dates_grade_gld_and_exact_five_bp(self):
        m = watch.measure_three_week(self.obs, self.data["GLD"], "2026-10-08")
        self.assertEqual(m["dy_bp"], 5)
        self.assertEqual(m["gld_start"]["date"], "2026-09-17")
        self.assertEqual(m["gld_end"]["date"], "2026-10-08")
        self.assertLess(m["return_pct"], 0)

    def test_thursday_observation_does_not_move_the_ruled_friday_clock(self):
        m = watch.measure_weekly_shape(self.obs, self.data["GLD"], "2026-10-08")
        self.assertEqual(m['points'][-1]['date'], '2026-10-02')
        self.assertEqual(m['points'][0]['date'], '2026-09-11')
        self.assertEqual(len(m['weekly_signs']), 3)

    def test_positive_daily_shape_cannot_override_negative_weekly_grade(self):
        for r in self.data['GLD']['history']:
            if r['date']=='2026-09-17':r['close']=360.
        _, out, _ = self.run_watch()
        self.assertIn('Rolling21-calendar-day diagnostic: +5bp / +5.56%', out)
        self.assertIn('no kill-cond-#3 endpoint shape on the ruled weekly basis', out)

    def test_completed_friday_with_unpublished_yield_uses_prior_common_date(self):
        m = watch.measure_weekly_shape(self.obs, self.data['GLD'], '2026-10-08', '2026-10-12')
        self.assertEqual(m['points'][-1]['friday'], '2026-10-09')
        self.assertEqual(m['points'][-1]['date'], '2026-10-08')
        self.assertEqual(m['points'][0]['date'], '2026-09-18')
        self.assertEqual(len(m['weekly_signs']), 3)

    def test_weekly_shape_requires_four_distinct_available_endpoints(self):
        with self.assertRaisesRegex(ValueError, 'stale|four distinct'):
            watch.measure_weekly_shape(self.obs[-1:],self.data['GLD'],'2026-10-08')

    def test_output_does_not_certify_vendor_settlements(self):
        _, out, _ = self.run_watch()
        self.assertNotIn("settled closes", out)
        self.assertIn("not certified exchange settlements", out)


if __name__ == "__main__":
    unittest.main()
