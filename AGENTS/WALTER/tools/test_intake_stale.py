"""Display-only stale flag (WQ-757 A item 1, 2026-11-27): counts and label tag, never a key or receipt change."""
import unittest
from unittest import mock
import intake_scan as s


class Stale(unittest.TestCase):
    def test_S1_counts_flagged_rows_and_skips_unflagged_batches(self):
        batches = {"data/2099-01-02/news.json": [{"title": "a", "stale": True, "age_days": 12},
                                                 {"title": "b", "stale": False, "age_days": 0},
                                                 {"title": "c", "stale": None, "age_days": None},
                                                 {"title": "d"}],
                   "data/2099-01-01/news.json": [{"title": "old"}]}
        with mock.patch.object(s, "read_batch_items", side_effect=lambda b: (batches[b], None)):
            out = s.stale_lines(list(batches))
        self.assertEqual(len(out), 1)
        self.assertIn("1 of 3 flagged rows", out[0][1])
        self.assertIn("1 with no readable date", out[0][1])

    def test_S2_tag_only_on_true(self):
        self.assertIn("12 days", s._stale_tag({"stale": True, "age_days": 12}))
        self.assertEqual(s._stale_tag({"stale": False}), "")
        self.assertEqual(s._stale_tag({"stale": None}), "")
        self.assertEqual(s._stale_tag({}), "")


if __name__ == "__main__":
    unittest.main()
