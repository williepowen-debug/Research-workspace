"""Will-directed view-only omission contract; synthetic ledgers, no production writes."""
import contextlib
import copy
import datetime
import io
from pathlib import Path
import tempfile
import unittest

import orch_log as orch


DAY = datetime.date(2026, 10, 21)


def row(desk='OZK', touch='1-SPAWN', delivered='IN-FLIGHT', date='2026-10-21', drained='0'):
    return [date, desk, 'desk', touch, 'fixture', drained, delivered, 'OK', '', '', '', '', '']


class ClosedRows(unittest.TestCase):
    def render(self, rows):
        return orch.render_view(rows, today=DAY)

    def inflight(self, text):
        return text.split('## Last `drained>0`', 1)[0]

    def test_open_spawn_and_zero_disclosure(self):
        text = self.inflight(self.render([row()]))
        self.assertIn('## IN-FLIGHT rows (1)', text)
        self.assertIn('| OZK | desk | 1-SPAWN |', text)
        self.assertIn('Omitted 0 IN-FLIGHT row(s)', text)

    def test_later_receipt_variants_and_close_summary(self):
        for touch in ('2-CLOSEOUT-RECEIPT', '4-REPING-RECEIPT', '6-REPING-RECEIPT',
                      'CLOSE', '2-receipt', '2-CLOSEOUT-PING'):
            with self.subTest(touch=touch):
                text = self.inflight(self.render([row(), row(touch=touch, delivered='DONE')]))
                self.assertIn('## IN-FLIGHT rows (0)', text)
                self.assertIn('Omitted 1 IN-FLIGHT row(s)', text)
                self.assertIn('exact same desk string', text)

    def test_different_desk_strings_do_not_close(self):
        for desk in ('RED', 'OZK (owner)', 'ozk', 'OZK '):
            with self.subTest(desk=desk):
                text = self.inflight(self.render([row(), row(desk=desk, touch='2-RECEIPT', delivered='DONE')]))
                self.assertIn('## IN-FLIGHT rows (1)', text)
                self.assertIn('Omitted 0 IN-FLIGHT row(s)', text)

    def test_earlier_receipt_cannot_close_later_spawn(self):
        text = self.inflight(self.render([row(touch='2-RECEIPT', delivered='DONE'), row()]))
        self.assertIn('## IN-FLIGHT rows (1)', text)
        self.assertIn('Omitted 0 IN-FLIGHT row(s)', text)

    def test_file_position_not_date_decides(self):
        text = self.inflight(self.render([row(), row(touch='2-RECEIPT', delivered='DONE', date='2026-10-20')]))
        self.assertIn('## IN-FLIGHT rows (0)', text)
        text = self.inflight(self.render([row(touch='2-RECEIPT', delivered='DONE', date='2026-10-22'), row()]))
        self.assertIn('## IN-FLIGHT rows (1)', text)

    def test_reopened_spawn_stays_and_repeated_receipts_do_not_double_count(self):
        rows = [row(), row(touch='2-RECEIPT', delivered='DONE'),
                row(touch='3-RECEIPT', delivered='DONE'), row(touch='4-SPAWN')]
        text = self.inflight(self.render(rows))
        self.assertIn('## IN-FLIGHT rows (1)', text)
        self.assertIn('Omitted 1 IN-FLIGHT row(s)', text)
        self.assertIn('| 4-SPAWN |', text)

    def test_row_cannot_close_itself(self):
        text = self.inflight(self.render([row(touch='2-CLOSEOUT-RECEIPT')]))
        self.assertIn('## IN-FLIGHT rows (1)', text)
        self.assertIn('Omitted 0 IN-FLIGHT row(s)', text)

    def test_non_closing_touch_and_other_columns_do_not_close(self):
        later = row(touch='2-PING', delivered='RECEIPT CLOSE')
        later[8] = 'CLOSEOUT-RECEIPT'
        text = self.inflight(self.render([row(), later]))
        self.assertIn('## IN-FLIGHT rows (1)', text)
        self.assertIn('Omitted 0 IN-FLIGHT row(s)', text)

    def test_other_sections_metadata_order_and_input_preserved(self):
        rows = [row(desk='Z', touch='1-Z'), row(touch='1-OLD', drained='3'),
                row(touch='2-RECEIPT', delivered='DONE'),
                row(desk='A', touch='1-FIRST'), row(desk='A', touch='2-SECOND')]
        before = copy.deepcopy(rows)
        text = self.render(rows)
        self.assertEqual(rows, before)
        self.assertIn(f'({len(rows)} data rows)', text.splitlines()[1])
        self.assertLess(text.index('| A |'), text.index('| Z |'))
        self.assertLess(text.index('| 1-FIRST |'), text.index('| 2-SECOND |'))
        # A close changes only visibility in the first table: the closed spawn's
        # positive drain still supplies cadence; the no-drain desk set also stays.
        control = copy.deepcopy(rows)
        control[2][3] = '2-PING'
        self.assertEqual(text.splitlines()[:3], self.render(control).splitlines()[:3])
        self.assertEqual(text.split('## Last `drained>0`', 1)[1],
                         self.render(control).split('## Last `drained>0`', 1)[1])
        self.assertIn('| OZK | desk | 1-OLD | 3 |', text.split('## Last `drained>0`', 1)[1])

    def test_regeneration_leaves_ledger_bytes_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger, view = Path(tmp) / 'ledger.tsv', Path(tmp) / 'view.md'
            rows = [row(), row(touch='2-RECEIPT', delivered='DONE')]
            raw = ('# preserved fixture\n' + '\t'.join(orch.COLS) + '\n' +
                   ''.join('\t'.join(r) + '\n' for r in rows)).encode()
            ledger.write_bytes(raw)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(orch.write_view(str(ledger), str(view), today=DAY), 0)
            self.assertEqual(ledger.read_bytes(), raw)
            self.assertIn('Omitted 1 IN-FLIGHT row(s)', view.read_text())


if __name__ == '__main__':
    unittest.main()
