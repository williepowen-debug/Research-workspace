"""Independent review regressions for WQ-286 G1; run from any cwd with unittest.

Synthetic cases isolate parser directions; live tests compare the current FERT/FLG
header forms without changing owner files. They do not certify owner date truth.
"""
import datetime
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location('ledger_review_subject', ROOT / 'scripts/ledger_staleness.py')
SUBJECT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SUBJECT)
NOW = datetime.datetime(2026, 10, 3).timestamp()

class AttentionContract(unittest.TestCase):
    def parse(self, header):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'case.tsv'
            path.write_text(header + '\na\tb\n1\t2\n')
            return SUBJECT.attention_info(path, NOW)

    def test_alias_far_right_real_segment(self):
        for alias in ('Staleness sweep', 'Staleness sweep (no data)', 'Last staleness check'):
            with self.subTest(alias=alias):
                self.assertEqual(self.parse('# LIVE | ' + 'x' * 140 + ' | ' + alias + ': 2026-10-01')[1], '2026-10-01')

    def test_unrelated_pipe_prose_cannot_waive_column_cap(self):
        self.assertIsNone(self.parse('# LIVE | ' + 'x' * 140 + ' Planned future label Staleness sweep: 2026-10-01'))

    def test_legacy_keys_keep_original_column_cap(self):
        for key in ('Last attention check', 'Last re-pull ATTEMPTED', 'Last hygiene/no-event check', 'Last reviewed'):
            with self.subTest(key=key):
                self.assertIsNone(self.parse('# LIVE | ' + 'x' * 140 + ' | ' + key + ': 2026-10-01'))

    def test_repeated_alias_newest_wins(self):
        self.assertEqual(self.parse('# Staleness sweep: 2026-07-01 | Staleness sweep: 2026-10-01')[1], '2026-10-01')

    def test_invalid_first_alias_does_not_hide_valid_second(self):
        self.assertEqual(self.parse('# Staleness sweep: 2026-99-99 | Staleness sweep: 2026-10-01')[1], '2026-10-01')

    def test_colon_is_required(self):
        self.assertIsNone(self.parse('# Staleness sweep 2026-10-01'))

    def test_far_right_without_pipe_rejected(self):
        self.assertIsNone(self.parse('# ' + 'x' * 140 + ' Staleness sweep: 2026-10-01'))

    def test_data_rows_do_not_become_attention_header(self):
        self.assertIsNone(self.parse('# LIVE\na\tb\n1\tStaleness sweep: 2026-10-01'))

    def test_live_fert_flg_immediate_segments(self):
        checked = 0
        for desk in ('FERT', 'FLG'):
            for path in (ROOT / 'AGENTS' / desk / 'workbook').glob('*.tsv'):
                valid = []
                for line in SUBJECT._header_block(path):
                    for _, regex in SUBJECT.ATTENTION_RES[-2:]:
                        for match in regex.finditer(line):
                            prefix = line[:match.start()]
                            if match.start() < SUBJECT.MARKER_COL_CAP or ('|' in prefix and not prefix.rsplit('|', 1)[1].strip()):
                                try:
                                    valid.append(datetime.date.fromisoformat(match.group(1)).isoformat())
                                except ValueError:
                                    pass
                if valid:
                    checked += 1
                    with self.subTest(path=str(path.relative_to(ROOT))):
                        result = SUBJECT.attention_info(path, NOW)
                        self.assertIsNotNone(result)
                        self.assertGreaterEqual(result[1], max(valid))
        self.assertGreaterEqual(checked, 10, 'Production acceptance population disappeared; re-pick live files')

if __name__ == '__main__':
    unittest.main()
