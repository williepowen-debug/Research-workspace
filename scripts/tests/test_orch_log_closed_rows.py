"""Will-directed view-only omission contract; synthetic ledgers, no production writes."""
import contextlib
import copy
import datetime
import io
import json
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
                      '2-receipt'):
            with self.subTest(touch=touch):
                text = self.inflight(self.render([row(), row(touch=touch, delivered='DONE')]))
                self.assertIn('## IN-FLIGHT rows (0)', text)
                self.assertIn('Omitted 1 IN-FLIGHT row(s)', text)
                self.assertIn('same-desk', text)

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


    def structured(self, r, session='A', minute=0, state='UNKNOWN', resolves=None, owner='PROME'):
        r[0] = '2020-01-01'
        r[4] = 'fixture session ' + session
        stamp = f'2020-01-01T12:{minute:02d}:00+00:00'
        data = dict(owner=owner, session_id=session, touch_at=stamp, observed_at=stamp,
                    state=state, ask='actual closeout ask', receipt='actual closeout reply')
        if resolves is not None:
            data['resolves'] = resolves
        r[8] = 'closeout_v1=' + json.dumps(data)
        return r

    def receipt(self, original, touch='2-CLOSEOUT-RECEIPT', **changes):
        r = self.structured(row(touch=touch, delivered='DONE'), minute=1,
                            state='ASKED_RECEIPT', resolves=[orch.orch_closeout.touch_key(original)])
        if changes:
            data = json.loads(r[8].split('=', 1)[1])
            data.update(changes)
            r[8] = 'closeout_v1=' + json.dumps(data)
        return r

    def test_ce1_late_receipt_keeps_higher_numbered_reping(self):
        rows = [row(touch='3-REPING'), row(touch='5-REPING'),
                row(touch='4-REPING-RECEIPT', delivered='DONE')]
        self.assertEqual(orch._closed_inflight(rows), {0})
        text = self.inflight(self.render(rows))
        self.assertIn('| 5-REPING |', text)
        self.assertNotIn('| 3-REPING |', text)

    def test_ce2_explicit_receipt_closes_only_session_a(self):
        a = self.structured(row())
        b = self.structured(row(), session='B')
        rows = [a, b, self.receipt(a)]
        self.assertEqual(orch._closed_inflight(rows), {0})
        self.assertIn('## IN-FLIGHT rows (1)', self.render(rows))

    def test_ce2_ambiguous_legacy_session_prose_keeps_both(self):
        a, b, receipt = row(), row(), row(touch='2-CLOSEOUT-RECEIPT', delivered='DONE')
        a[8], b[8], receipt[8] = 'session A', 'session B', 'session A'
        self.assertEqual(orch._closed_inflight([a, b, receipt]), set())

    def test_ce3_time_corrections_never_close(self):
        for delivered, notes in [('TIME-CORRECTION (original time UNKNOWN)', ''),
                                 ('DONE', 'time_correction_v1={}')]:
            with self.subTest(delivered=delivered, notes=notes):
                correction = row(touch='CLOSE', delivered=delivered)
                correction[8] = notes
                self.assertEqual(orch._closed_inflight([row(), correction]), set())
                # Also exclude numbered receipts bearing either correction marker.
                correction[3] = '2-CLOSEOUT-RECEIPT'
                self.assertEqual(orch._closed_inflight([row(), correction]), set())

    def test_ce5_new_closeout_audit_keeps_spawn_and_audit_visible(self):
        rows = [row(desk='ARGUS'), row(desk='ARGUS', touch='1-CLOSEOUT-AUDIT')]
        text = self.inflight(self.render(rows))
        self.assertIn('## IN-FLIGHT rows (2)', text)
        self.assertIn('| 1-SPAWN |', text)
        self.assertIn('| 1-CLOSEOUT-AUDIT |', text)

    def test_closeout_asks_pings_plans_and_substrings_close_nothing(self):
        for touch in ('2-CLOSEOUT-ASK', '2-CLOSEOUT-PING', '1-CLOSEOUT-PLAN',
                      '2-CLOSEOUT-CHECK-ASK', '2-RECEIPT-FOLLOWUP', '2-POSTCLOSE'):
            with self.subTest(touch=touch):
                self.assertEqual(orch._closed_inflight([row(), row(touch=touch, delivered='DONE')]), set())
        pending = row(touch='2-RECEIPT', delivered='IN-FLIGHT; still working')
        self.assertEqual(orch._closed_inflight([row(), pending]), set())

    def test_one_legacy_receipt_closes_one_unique_highest_lower_touch(self):
        rows = [row(), row(touch='3-REPING'), row(touch='4-RECEIPT', delivered='DONE')]
        self.assertEqual(orch._closed_inflight(rows), {1})
        rows.append(row(touch='4-RECEIPT', delivered='DONE'))
        self.assertEqual(orch._closed_inflight(rows), {1})

    def test_unnumbered_close_requires_explicit_valid_resolution(self):
        self.assertEqual(orch._closed_inflight([row(), row(touch='CLOSE', delivered='DONE')]), set())
        original = self.structured(row())
        self.assertEqual(orch._closed_inflight([original, self.receipt(original, touch='CLOSE')]), {0})

    def test_bad_structured_links_never_fall_back(self):
        original = self.structured(row())
        for changes in ({'session_id': 'B'}, {'owner': 'WILL'}, {'resolves': ['f' * 64]},
                        {'resolves': []}, {'touch_at': '2019-01-01T12:00:00+00:00'},
                        {'observed_at': '2020-01-01T12:00:00+00:00'}):
            with self.subTest(changes=changes):
                self.assertEqual(orch._closed_inflight([original, self.receipt(original, **changes)]), set())
        receipt = self.receipt(original)
        data = json.loads(receipt[8].split('=', 1)[1]); data.pop('resolves')
        receipt[8] = 'closeout_v1=' + json.dumps(data)
        self.assertEqual(orch._closed_inflight([original, receipt]), set())
        # Both directions of a malformed payload must preserve the original.
        malformed = row(); malformed[8] = 'closeout_v1={'
        self.assertEqual(orch._closed_inflight([malformed, row(touch='2-RECEIPT', delivered='DONE')]), set())
        malformed = row(touch='2-RECEIPT', delivered='DONE'); malformed[8] = 'closeout_v1={'
        self.assertEqual(orch._closed_inflight([row(), malformed]), set())

    def test_valid_working_correction_reopens_original(self):
        original = self.structured(row())
        receipt = self.receipt(original)
        working = self.receipt(original, touch='3-CLOSEOUT-ASK', state='ASKED_WORKING',
                               touch_at='2020-01-01T12:02:00+00:00',
                               observed_at='2020-01-01T12:02:00+00:00')
        self.assertEqual(orch._closed_inflight([original, receipt, working]), set())

    def test_duplicate_structured_keys_remain_visible(self):
        original = self.structured(row())
        duplicate = copy.deepcopy(original)
        self.assertEqual(orch._closed_inflight([original, duplicate, self.receipt(original)]), set())

    def test_explicit_multi_target_event_does_not_hide_multiple_originals(self):
        a = self.structured(row())
        b = self.structured(row(touch='3-REPING'))
        receipt = self.receipt(a, touch='4-RECEIPT',
                               resolves=[orch.orch_closeout.touch_key(a), orch.orch_closeout.touch_key(b)])
        self.assertEqual(orch._closed_inflight([a, b, receipt]), set())


if __name__ == '__main__':
    unittest.main()
