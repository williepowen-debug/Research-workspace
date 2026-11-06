"""Freshness guards must fail loudly without changing scores or consuming rows."""
import csv
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import boot
import cot_metals


class FreshnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.ledger = Path(self.temp.name) / 'consumed.tsv'
        source = Path(__file__).parent / 'sources/2026-10-12_review/deafut.txt'
        self.raw = source.read_text()
        self.live = cot_metals.extract_all(cot_metals.parse(self.raw))
        self.rows = [dict(metal=d['metal'], code=d['code'], report_date=d['report_date'],
                          open_interest=d['oi'], net_nc_long=d['net_nc'],
                          net_over_oi_pct=f"{d['net_over_oi']:.4f}") for d in self.live]

    def write(self, rows=None):
        with self.ledger.open('w') as f:
            w = csv.DictWriter(f, fieldnames=list(self.rows[0]), delimiter='\t')
            w.writeheader()
            w.writerows(self.rows if rows is None else rows)

    def grade(self):
        return boot.cot_metals_vintage_leg(self.ledger, self.raw)[0]

    def test_current_read_is_quiet(self):
        self.write()
        before = self.ledger.read_bytes()
        self.assertEqual(self.grade(), 0)
        self.assertEqual(self.ledger.read_bytes(), before)

    def test_one_unread_metal_requires_review(self):
        self.rows[1]['report_date'] = '2026-09-29'
        self.write()
        self.assertEqual(self.grade(), 1)

    def test_source_older_than_consumed_cannot_certify(self):
        self.rows[0]['report_date'] = '2026-10-13'
        self.write()
        self.assertEqual(self.grade(), 2)

    def test_missing_file_cannot_certify(self):
        self.assertEqual(self.grade(), 2)

    def test_missing_one_metal_cannot_certify(self):
        self.write(self.rows[:2])
        self.assertEqual(self.grade(), 2)

    def test_wrong_code_cannot_certify(self):
        self.rows[0]['code'] = '088691'
        self.write()
        self.assertEqual(self.grade(), 2)

    def test_broken_ledger_identity_cannot_certify(self):
        self.rows[0]['net_over_oi_pct'] = '0.0000'
        self.write()
        self.assertEqual(self.grade(), 2)

    def test_same_vintage_source_changed_cannot_certify(self):
        self.rows[0]['net_nc_long'] += 1
        self.rows[0]['net_over_oi_pct'] = f"{100*self.rows[0]['net_nc_long']/self.rows[0]['open_interest']:.4f}"
        self.write()
        self.assertEqual(self.grade(), 2)

    def test_mixed_source_vintages_cannot_certify(self):
        self.write()
        rows = cot_metals.parse(self.raw)
        for r in rows:
            if len(r) > 16 and r[3].strip() == '076651':
                r[2] = '2026-09-29'
        import io
        f = io.StringIO()
        csv.writer(f).writerows(rows)
        self.assertEqual(boot.cot_metals_vintage_leg(self.ledger, f.getvalue())[0], 2)

    def test_pull_failure_cannot_certify(self):
        self.write()
        with patch.object(cot_metals, 'fetch', side_effect=OSError('offline')):
            self.assertEqual(boot.cot_metals_vintage_leg(self.ledger)[0], 2)

    def test_exact_five_bp_is_outside_strict_noise_interval(self):
        # The production assignment is exercised, not a mirror of its formula.
        import ast
        tree = ast.parse((Path(__file__).parent/'metals_watch.py').read_text())
        expr = next(n.value for n in ast.walk(tree) if isinstance(n, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id=='dy_bp' for t in n.targets))
        for a, b, expected in [('2.45','2.40',5),('2.44','2.40',4),('2.40','2.40',0)]:
            value = eval(compile(ast.Expression(expr), '<production dy_bp>', 'eval'),
                         {'latest_y':{'value':a},'y_then':{'value':b}})
            self.assertEqual(value, expected)
            self.assertEqual(0 < value < 5, expected == 4)


class PredictionAndGoldGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'p.tsv'

    def scan(self, text):
        self.path.write_text(text)
        with patch.object(boot, 'PREDICTIONS', self.path):
            return boot.predictions_due()

    def test_empty_ledger_is_newborn(self):
        self.assertEqual(self.scan(''), (0, []))

    def test_bad_date_on_open_row_fails(self):
        self.assertEqual(self.scan('id\tresolve_date\tstatus\nA\tsoon\tOPEN\n'), (2, []))

    def test_missing_column_fails(self):
        self.assertEqual(self.scan('id\tstatus\nA\tOPEN\n'), (2, []))

    def test_valid_due_row_reports(self):
        self.assertEqual(self.scan('id\tresolve_date\tstatus\nA\t2026-01-01\tOPEN\n')[0], 1)

    def test_closed_row_with_bad_date_is_ignored(self):
        self.assertEqual(self.scan('id\tresolve_date\tstatus\nA\tsoon\tHIT\n'), (0, []))

    def gold(self, live):
        ledger = Path(self.temp.name) / 'gold.tsv'
        ledger.write_text('report_date\ta\tb\tc\td\tnet\n2026-10-27\t1\t1\t1\t1\t47.0000\n')
        fake = type('F', (), {'fetch': staticmethod(lambda: ''),
                              'extract_gold': staticmethod(lambda _: {'report_date': '2026-10-27',
                                                                      'net_over_oi': live})})
        with patch.object(boot, 'COT_VINTAGES', ledger), patch.dict('sys.modules', {'cot_gold': fake}):
            return boot.cot_vintage_leg()

    def test_gold_same_vintage_changed_value_flags(self):
        self.assertEqual(self.gold(48.0)[0], 1)

    def test_gold_same_vintage_same_value_quiet(self):
        self.assertEqual(self.gold(47.0)[0], 0)


if __name__ == '__main__':
    unittest.main()
