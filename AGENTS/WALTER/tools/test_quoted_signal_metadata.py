"""Quoted YAML metadata must keep its cluster and timestamp meaning."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import gen_board_index as index
import walter_doctor as doctor


class QuotedMetadataTests(unittest.TestCase):
    def test_index_quoted_scalars_match_plain(self):
        fields = {'cluster': 'IRAN_HORMUZ', 'date': '2026-10-20',
                  'timestamp': '2026-10-20T20:26:26Z', 'precedence': 'PRIORITY',
                  'domain': 'GEOPOL_ENERGY'}
        plain = '---\n' + ''.join(f'{k}: {v}\n' for k, v in fields.items()) + '---\nbody'
        for quote in ('"', "'"):
            quoted = '---\n' + ''.join(f'{k}: {quote}{v}{quote}\n' for k, v in fields.items()) + '---\nbody'
            self.assertEqual(index.parse_front(plain), index.parse_front(quoted))

    def test_arrays_and_malformed_quote_remain_visible(self):
        value = index.parse_front('---\naction: ["HENRY", "LIQUID"]\ncluster: "IRAN_HORMUZ\n---\n')
        self.assertEqual(index.listify(value['action']), ['HENRY', 'LIQUID'])
        self.assertEqual(value['cluster'], '"IRAN_HORMUZ')

    def verdict(self, board_value, log_value='2026-10-19T00:00:00Z'):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'BOARD').mkdir()
            desk = root / 'AGENTS/WALTER'
            (desk / 'routed').mkdir(parents=True)
            (desk / 'routed/delivery_log.tsv').write_text('timestamp_routed\tsignal_id\n' + log_value + '\tfixture\n')
            fixture = root / f'BOARD/SIG-W-{doctor.TODAY:%Y%m%d}-001-fixture.md'
            fixture.write_text('---\ntimestamp: ' + board_value + '\n---\n')
            with patch.object(doctor, 'REPO', root), patch.object(doctor, 'WALTER', desk):
                return [severity for severity, _ in doctor.check_future_timestamps()]

    def test_valid_quoted_board_timestamp(self):
        self.assertNotIn(doctor.MED, self.verdict('"2026-10-19T00:00:00Z"'))

    def test_quoted_future_still_high(self):
        self.assertIn(doctor.HIGH, self.verdict('"2099-01-01T00:00:00Z"'))

    def test_quoted_invalid_still_malformed(self):
        self.assertIn(doctor.MED, self.verdict('"NOT-A-TIMESTAMP"'))

    def test_tsv_timestamp_does_not_gain_yaml_quoting(self):
        self.assertIn(doctor.MED, self.verdict('2026-10-19T00:00:00Z', '"2026-10-19T00:00:00Z"'))


if __name__ == '__main__':
    unittest.main()
