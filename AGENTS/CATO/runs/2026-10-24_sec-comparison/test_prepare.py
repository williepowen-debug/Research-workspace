import copy
import json
from pathlib import Path
import unittest

from prepare import build, markdown


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.raw = Path(__file__).with_name('sec-response.json').read_bytes()
        self.data = json.loads(self.raw)
        self.args = dict(cik='0000320193', concept='NetIncomeLoss', unit='USD',
                         prior=['2025-03-30', '2025-06-28'],
                         current=['2026-03-29', '2026-06-27'], as_of='2026-10-24',
                         retrieved_at='2026-10-24T21:43:10.239847+00:00')

    def run_data(self, **args):
        return build(json.dumps(self.data).encode(), **(self.args | args))

    def current(self):
        return next(v for v in self.data['units']['USD'] if v.get('start') == '2026-03-29')

    def test_real_response_and_render(self):
        packet = build(self.raw, **self.args)
        self.assertEqual(packet['prior']['val'], 23434000000)
        self.assertEqual(packet['current']['val'], 29789000000)
        self.assertEqual(packet['calculation']['difference'], 6355000000)
        self.assertIn('2026-03-29 to 2026-06-27', markdown(packet))
        self.assertIn(packet['response_sha256'], markdown(packet))
        self.assertIn(packet['current']['filing_url'], markdown(packet))

    def test_quarter_vs_nine_months_rejected(self):
        with self.assertRaisesRegex(ValueError, 'mismatched durations'):
            self.run_data(current=['2025-09-28', '2026-06-27'])

    def test_missing_period_and_wrong_unit(self):
        for args in ({'unit': 'EUR'}, {'current': ['2026-03-28', '2026-06-26']}):
            with self.subTest(args=args), self.assertRaisesRegex(ValueError, 'Missing period'):
                self.run_data(**args)

    def test_wrong_issuer_or_concept(self):
        for args in ({'cik': '1'}, {'concept': 'Revenues'}):
            with self.subTest(args=args), self.assertRaisesRegex(ValueError, 'does not match'):
                self.run_data(**args)

    def test_missing_source_identity(self):
        del self.current()['accn']
        with self.assertRaisesRegex(ValueError, 'identity'):
            self.run_data()

    def test_conflicting_latest_record(self):
        other = copy.deepcopy(self.current())
        other['val'] += 1
        self.data['units']['USD'].append(other)
        with self.assertRaisesRegex(ValueError, 'Ambiguous'):
            self.run_data()

    def test_filing_cutoff_excludes_later_revision(self):
        other = copy.deepcopy(self.current())
        other.update(filed='2026-10-23', accn='0000320193-26-000099', val=1)
        self.data['units']['USD'].append(other)
        earlier = self.run_data(as_of='2026-08-01')
        later = self.run_data()
        self.assertEqual(earlier['current']['val'], 29789000000)
        self.assertEqual(later['current']['val'], 1)

    def test_cutoff_before_current_filing(self):
        with self.assertRaisesRegex(ValueError, 'No filing'):
            self.run_data(as_of='2026-07-01')

    def test_no_change(self):
        self.current()['val'] = 23434000000
        packet = self.run_data()
        self.assertEqual(packet['calculation']['difference'], 0)
        self.assertEqual(packet['calculation']['percent_change'], 0)

    def test_nonpositive_base_keeps_difference(self):
        for v in self.data['units']['USD']:
            if v.get('start') == '2025-03-30':
                v['val'] = 0
        packet = self.run_data()
        self.assertIsNone(packet['calculation']['percent_change'])
        self.assertEqual(packet['calculation']['difference'], 29789000000)

    def test_overlap_rejected(self):
        with self.assertRaisesRegex(ValueError, 'nonoverlapping'):
            self.run_data(prior=self.args['current'])

    def test_retrieval_requires_timezone(self):
        with self.assertRaisesRegex(ValueError, 'timezone'):
            self.run_data(retrieved_at='2026-10-24T21:43:10')


if __name__ == '__main__':
    unittest.main()
