#!/usr/bin/env python3
"""Offline regressions: clock time and delayed quotes cannot certify SETTLE."""
import io
import sys
import unittest
from datetime import date, datetime, timezone
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import thresholds as t

DAY = date(2026, 10, 14)
FINAL = dict(vix=17.0, vix9d=15.0, vix3m=19.0, vix6m=21.0, vvix=98.0, skew=154.0)


class BasisTests(unittest.TestCase):
    def report(self, official, hour=21, source="CBOE"):
        class Clock(datetime):
            @classmethod
            def now(cls, tz=None):
                return datetime(2026, 10, 14, hour, 0, tzinfo=timezone.utc).astimezone(tz)

        spot = dict(FINAL, vix=16.0, vix3m=18.0, skew=None,
                    skew_stale=True, skew_stale_date="2026-10-13",
                    skew_suppressed_value=154.74)
        spot.update({f"{k}_src": source for k in FINAL})
        with patch.object(t, "datetime", Clock), patch.object(t, "fetch_spot", return_value=spot), \
             patch.object(t, "fetch_m1m2", return_value={"_error": "not published"}), \
             patch.object(t, "fetch_official_spot", return_value=official) as fetch, \
             patch.object(t, "append_daily_log", return_value="updated"):
            return t.build_report(supersede=True), fetch.call_count

    def test_after_close_missing_daily_bar_stays_tick(self):
        report, _ = self.report({k: v for k, v in FINAL.items() if k != "skew"})
        self.assertEqual(report["row"]["basis"], "TICK")
        self.assertEqual(report["row"]["skew"], "")
        self.assertEqual(report["stale_dates"]["skew"], "2026-10-13")

    def test_yahoo_same_date_never_certifies_daily_basis(self):
        report, _ = self.report({}, source="yfinance")
        self.assertEqual(report["row"]["basis"], "TICK")

    def test_complete_daily_values_replace_delayed_values_before_ratios(self):
        report, _ = self.report(FINAL)
        self.assertEqual(report["row"]["basis"], "SETTLE")
        self.assertEqual(report["row"]["vix"], 17.0)
        self.assertEqual(report["row"]["skew"], 154.0)
        self.assertEqual(report["row"]["vix3m_vix_ratio"], round(19/17, 4))
        self.assertEqual(set(report["spot_sources"].values()), {"CBOE_HISTORY"})
        self.assertEqual(report["stale_suppressed"], {})
        self.assertEqual(report["row"]["m1m2_settle_date"], "")

    def test_before_close_does_not_promote_early_history(self):
        report, calls = self.report(FINAL, hour=19)
        self.assertEqual(report["row"]["basis"], "TICK")
        self.assertEqual(calls, 0)

    def histories(self, text=None, error=False):
        def answer(req, timeout):
            if error:
                raise OSError("offline transport failure")
            sym = req.full_url.rsplit("/", 1)[1].split("_History")[0]
            body = text if text is not None else f"DATE,{sym}\n10/13/2026,150\n10/14/2026,{FINAL[sym.lower()]}\n"
            return io.BytesIO(body.encode())
        with patch("urllib.request.urlopen", side_effect=answer):
            return t.fetch_official_spot(DAY)

    def test_exact_date_history(self):
        self.assertEqual(self.histories(), FINAL)

    def test_prior_date_not_forward_filled(self):
        self.assertEqual(self.histories("DATE,CLOSE\n10/13/2026,154.74\n"), {})

    def test_wrong_shape_is_not_authoritative_empty(self):
        self.assertEqual(self.histories("<html>error</html>"), {})

    def test_transport_failure_cannot_certify(self):
        self.assertEqual(self.histories(error=True), {})

    def test_nonfinite_and_zero_values_rejected(self):
        for bad in ("nan", "inf", "0", "-1"):
            self.assertEqual(self.histories(f"DATE,CLOSE\n10/14/2026,{bad}\n"), {})


if __name__ == "__main__":
    unittest.main()
