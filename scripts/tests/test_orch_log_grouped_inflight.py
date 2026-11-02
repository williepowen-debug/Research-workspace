"""L911: old unresolved debt stays counted without an unbounded detail table."""
import copy
import datetime
import unittest

import orch_log as orch


TODAY = datetime.date(2026, 11, 2)


def row(date, desk='SAM', touch='1', delivered='IN-FLIGHT', drained='0'):
    return [date, desk, 'desk', touch, 'fixture', drained, delivered, 'OK', '', '', '', '', '']


class GroupedInflight(unittest.TestCase):
    def render(self, rows, **kw):
        return orch.render_view(rows, today=TODAY, **kw)

    def test_boundary_and_future_rows_remain_detailed(self):
        text = self.render([row('2026-10-25'), row('2026-10-26', touch='2'),
                            row('2026-11-03', touch='3')])
        self.assertIn('## IN-FLIGHT rows (3)', text)
        self.assertIn('Detailed 2 recent row(s); grouped 1 older OPEN row(s)', text)
        self.assertNotIn('| 2026-10-25 | SAM |', text)
        self.assertIn('| 2026-10-26 | SAM |', text)
        self.assertIn('| 2026-11-03 | SAM |', text)

    def test_grouping_counts_touches_and_exact_identities(self):
        rows = [row('2026-09-25', 'SAM (reader)', '1'),
                row('2026-10-01', 'SAM (reader)', '2'),
                row('2026-10-02', 'SAM', '3'), row('2026-10-03', 'MIDAS', '1')]
        before = copy.deepcopy(rows)
        text = self.render(rows)
        self.assertEqual(rows, before)
        self.assertIn('Detailed 0 recent row(s); grouped 4 older OPEN row(s) under 2 base', text)
        self.assertIn('| SAM | 3 | 2 | 2026-09-25 | 2026-10-02 |', text)
        self.assertIn('| MIDAS | 1 | 1 | 2026-10-03 | 2026-10-03 |', text)
        self.assertIn('Full exact identities and touches remain in the source ledger', text)
        self.assertIn('age proves neither closure nor liveness', text)

    def test_closed_rows_are_not_reintroduced_in_summary(self):
        rows = [row('2026-10-01'), row('2026-10-01', touch='2-RECEIPT', delivered='DONE')]
        text = self.render(rows)
        self.assertIn('## IN-FLIGHT rows (0)', text)
        self.assertIn('grouped 0 older OPEN row(s)', text)
        self.assertIn('Omitted 1 IN-FLIGHT row(s)', text)

    def test_detail_horizon_does_not_change_cadence_or_absence(self):
        rows = [row('2026-10-01', drained='3'), row('2026-11-01', 'RED')]
        short = self.render(rows, inflight_days=0)
        long = self.render(rows, inflight_days=90)
        self.assertEqual(short.split('## Last `drained>0`', 1)[1],
                         long.split('## Last `drained>0`', 1)[1])
        self.assertIn('window 30d', short.splitlines()[1])
        self.assertIn('IN-FLIGHT detail 0d', short.splitlines()[1])
        self.assertIn('| 2026-10-01 | SAM |', self.render(rows, window_days=40))

    def test_many_old_rows_grow_counts_not_detail(self):
        rows = [row('2026-10-01', f'SAM (reader {i})') for i in range(1000)]
        text = self.render(rows)
        self.assertIn('## IN-FLIGHT rows (1000)', text)
        self.assertIn('| SAM | 1000 | 1000 |', text)
        self.assertLess(len(text.encode()), 5000)


if __name__ == '__main__':
    unittest.main()
