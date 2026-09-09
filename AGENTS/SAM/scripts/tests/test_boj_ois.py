"""Regression cases for replacing the impeached pricing feed with reviewed OIS."""
import contextlib
import copy
import importlib.util
import io
import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

SAM = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('boj_ois', SAM/'scripts/boj_ois.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
EVIDENCE = SAM/'research/outputs/2026-09-08_integration'
REVIEW = json.loads((SAM/'workbook/boj_ois_reviews/2026-09-09T1115-JST.json').read_text())
NOW = datetime.fromisoformat('2026-09-09T03:30:00+00:00')
IMAGE = (EVIDENCE/'totan-table.png').read_bytes()
HTML = (EVIDENCE/'totan-page.html').read_text()


class PricingTests(unittest.TestCase):
    def validate(self, review=None, image=IMAGE, now=NOW):
        return m.validate(REVIEW if review is None else review, image, REVIEW['image_url'], now)

    def test_saved_primary_image_curve_and_units(self):
        self.assertEqual(m.table_url(HTML), REVIEW['image_url'])
        rows = self.validate()
        self.assertEqual(len(rows), 5)
        self.assertEqual(rows[0]['incremental_25bp_equivalent_pct'], 98)
        self.assertEqual(rows[-1]['cumulative_expected_hikes'], 2.65)
        self.assertNotIn('cum_hike_pct', rows[-1])

    def test_changed_image_or_error_html_rejected(self):
        for image in (IMAGE+b'changed', b'<html>200 error</html>'):
            with self.subTest(image=image[:12]), self.assertRaises(m.SourceError):
                self.validate(image=image)

    def test_stale_and_future_dates_rejected(self):
        for now in ('2026-09-14T03:30:00+00:00', '2026-09-09T00:00:00+00:00'):
            with self.subTest(now=now), self.assertRaises(m.SourceError):
                self.validate(now=datetime.fromisoformat(now))

    def test_policy_date_expiry_even_if_quote_recent(self):
        review = copy.deepcopy(REVIEW)
        review['quote_as_of'] = '2026-09-17T11:15:00+09:00'
        with self.assertRaisesRegex(m.SourceError, 'expired'):
            self.validate(review, now=datetime.fromisoformat('2026-09-18T00:01:00+09:00'))

    def test_arithmetic_nonfinite_and_incomplete_rows_rejected(self):
        for field,value in [('ois_pct', 1.39), ('difference_pct', .1688),
                            ('incremental_25bp_equivalent_pct', 128),
                            ('cumulative_expected_hikes', 125), ('ois_pct', float('nan'))]:
            review = copy.deepcopy(REVIEW)
            review['rows'][1][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(m.SourceError):
                self.validate(review)
        review = copy.deepcopy(REVIEW)
        review['rows'].pop()
        with self.assertRaises(m.SourceError):
            self.validate(review)

    def test_duplicate_and_overlapping_terms_rejected(self):
        for field,value in [('meeting_month', '2026-09'), ('term_start', '2026-10-01')]:
            review = copy.deepcopy(REVIEW)
            review['rows'][1][field] = value
            with self.subTest(field=field), self.assertRaises(m.SourceError):
                self.validate(review)

    def test_methodology_and_image_layout_drift_rejected(self):
        for html in (HTML.replace('increments of 0.25%', 'increments of 0.50%'),
                     HTML.replace('wp-image-25784', 'changed-table')):
            with self.assertRaises(m.SourceError):
                m.table_url(html)

    def test_idempotency_and_same_vintage_revision_preserve_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'curve.tsv'
            rows = self.validate()
            self.assertEqual(m.append_rows(rows, path), 5)
            before = path.read_bytes()
            rows[0]['pulled_at'] = '2026-09-09T04:00:00+00:00'
            self.assertEqual(m.append_rows(rows, path), 0)
            self.assertEqual(path.read_bytes(), before)
            rows[0]['ois_pct'] = 1.2225
            with self.assertRaisesRegex(m.SourceError, 'Same-vintage revision'):
                m.append_rows(rows, path)
            self.assertEqual(path.read_bytes(), before)

    def test_boot_failure_never_writes_or_uses_old_quote(self):
        with patch.object(m, 'fetch', side_effect=[HTML.encode(), IMAGE+b'new']), \
             patch.object(m, 'append_rows') as writer, contextlib.redirect_stderr(io.StringIO()) as err:
            self.assertEqual(m.main([]), 2)
            writer.assert_not_called()
            self.assertIn('visual review required', err.getvalue())

    def test_no_write_success_and_network_failure(self):
        with patch.object(m, 'fetch', side_effect=[HTML.encode(), IMAGE]), \
             patch.object(m, 'datetime') as clock, patch.object(m, 'append_rows') as writer, \
             contextlib.redirect_stdout(io.StringIO()):
            clock.now.return_value = NOW
            clock.fromisoformat.side_effect = datetime.fromisoformat
            self.assertEqual(m.main(['--no-write']), 0)
            writer.assert_not_called()
        with patch.object(m, 'fetch', side_effect=OSError('offline')), \
             patch.object(m, 'append_rows') as writer, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(m.main([]), 2)
            writer.assert_not_called()


if __name__ == '__main__':
    unittest.main()
