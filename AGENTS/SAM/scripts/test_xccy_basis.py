"""Financial monitor regression checks: reject false freshness without erasing history."""
import unittest
from datetime import date
from xccy_basis import snapshot_error


class SnapshotGuardTests(unittest.TestCase):
    def test_old_hardcoded_cutoff_is_rejected(self):
        self.assertIsNotNone(snapshot_error(["2026-08-26", "2026-08-27"], date(2026, 9, 8)))

    def test_holiday_weekend_is_allowed(self):
        self.assertIsNone(snapshot_error(["2026-09-03", "2026-09-04"], date(2026, 9, 8)))

    def test_expired_pair_is_rejected_even_with_recent_prices(self):
        self.assertIsNotNone(snapshot_error(["2026-09-10", "2026-09-11"], date(2026, 9, 14)))

    def test_empty_single_and_future_samples_are_rejected(self):
        for dates in [[], ["2026-09-08"], ["2026-09-08", "2026-09-10"]]:
            with self.subTest(dates=dates):
                self.assertIsNotNone(snapshot_error(dates, date(2026, 9, 9)))


if __name__ == "__main__":
    unittest.main()
