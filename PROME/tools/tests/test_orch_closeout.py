import contextlib
import datetime as dt
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import orch_closeout as oc

DAY = dt.date(2026, 9, 16)
NOW = dt.datetime.fromisoformat('2026-09-16T17:00:00+00:00')


def row(desk='helper', touch='1', owner='PROME', state='ASKED_RECEIPT'):
    evidence = dict(owner=owner, session_id='runtime/session-1',
                    touch_at='2026-09-16T10:00:00-04:00', observed_at='2026-09-16T11:00:00-04:00',
                    state=state, ask='actual runtime closeout request', receipt='actual runtime reply', presence='native absence observation')
    if state == 'DARK_BEFORE_ASK':
        evidence['ask'] = ''
    return ['2026-09-16', desk, 'verifier', touch, 'bounded review', '0', 'delivered', 'OK',
            oc.MARKER + json.dumps(evidence), '', '', '', '']


class CloseoutTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'ORCH_LOG.tsv'

    def write(self, rows):
        self.path.write_text('\t'.join(oc.HEADER) + '\n' + ''.join('\t'.join(r) + '\n' for r in rows))

    def evaluate(self, rows, expected=None, complete=True):
        self.write(rows)
        return oc.evaluate(self.path, DAY, [oc.touch_key(r) for r in rows] if expected is None else expected, complete, NOW)

    def test_four_states_and_verifiers_kept(self):
        records = [row(touch=str(i), state=state) for i, state in enumerate(oc.LABELS, 1)]
        result, issues = self.evaluate(records)
        self.assertEqual([x['state'] for x in result], list(oc.LABELS))
        self.assertEqual(issues, [])

    def test_same_desk_wrong_owner_separate_touch(self):
        result, _ = self.evaluate([row(), row(touch='2-CLOSEOUT-PING', owner='WILL')])
        self.assertEqual([x['state'] for x in result], ['ASKED_RECEIPT', 'OUT_OF_SCOPE'])

    def test_old_prose_does_not_establish_receipt(self):
        r = row(); r[8] = 'PROME spawned; fully committed, closeout in commit title'
        result, _ = self.evaluate([r])
        self.assertEqual(result[0]['state'], 'UNKNOWN')

    def test_same_day_receipt_before_touch_refuses(self):
        r = row(); data = json.loads(r[8].split(oc.MARKER)[1]); data['observed_at'] = '2026-09-16T09:00:00-04:00'
        r[8] = oc.MARKER + json.dumps(data)
        result, _ = self.evaluate([r]); self.assertEqual(result[0]['state'], 'UNKNOWN')

    def test_absent_expected_and_reverse_mismatch(self):
        result, issues = self.evaluate([row()], expected=['missing'])
        self.assertEqual(len(issues), 2)
        self.assertIn('absent from ORCH_LOG', issues[0])
        self.assertIn('absent from declared complete inventory', issues[1])

    def test_empty_is_not_proof_without_inventory(self):
        _, issues = self.evaluate([], complete=False); self.assertTrue(issues)
        self.write([])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = oc.main(['--ledger', str(self.path), '--date', DAY.isoformat(), '--inventory-complete'])
        self.assertEqual((rc, out.getvalue()), (0, ''))

    def test_corrupt_or_partial_ledger_never_zero(self):
        for rows in ([row()[:-1]], [row(), row()], [row(touch='NOPE')]):
            self.write(rows)
            with self.assertRaises(ValueError): oc.evaluate(self.path, DAY)
        self.path.write_text('')
        with self.assertRaises(ValueError): oc.evaluate(self.path, DAY)

    def test_missing_evidence_and_future_observation(self):
        for field, value in [('ask', ''), ('session_id', ''), ('touch_at', ''), ('observed_at', '2099-01-01T00:00:00Z')]:
            r = row(); data = json.loads(r[8].split(oc.MARKER)[1]); data[field] = value
            r[8] = oc.MARKER + json.dumps(data)
            result, _ = self.evaluate([r]); self.assertEqual(result[0]['state'], 'UNKNOWN')

    def test_close_summary_not_a_touch(self):
        r = row(touch='CLOSE'); self.write([r])
        result, issues = oc.evaluate(self.path, DAY, inventory_complete=True, now=NOW)
        self.assertEqual((result, issues), ([], []))

    def prior_row(self, state='ASKED_WORKING', owner='PROME'):
        r = row(state=state, owner=owner)
        r[0] = '2026-09-15'
        data = json.loads(r[8].split(oc.MARKER)[1])
        data.update(session_id='overnight-helper', touch_at='2026-09-15T23:55:00-04:00',
                    observed_at='2026-09-15T23:56:00-04:00')
        r[8] = oc.MARKER + json.dumps(data)
        return r

    def test_overnight_working_retains_identity_and_inventory_uncertainty(self):
        r = self.prior_row()
        self.write([r])
        result, issues = oc.evaluate(self.path, DAY, now=NOW)
        self.assertEqual([(x['key'], x['state']) for x in result],
                         [(oc.touch_key(r), 'ASKED_WORKING')])
        self.assertIn('coverage UNKNOWN', issues[0])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = oc.main(['--ledger', str(self.path), '--date', str(DAY), '--inventory-complete'])
        self.assertEqual(rc, 1)
        self.assertIn(oc.touch_key(r), out.getvalue())
        self.assertIn('still working', out.getvalue())

    def test_prior_unresolved_persists_beyond_one_day(self):
        for state in ('ASKED_WORKING', 'DARK_BEFORE_ASK', 'UNKNOWN'):
            r = self.prior_row(state)
            self.write([r])
            result, issues = oc.evaluate(self.path, DAY + dt.timedelta(days=3),
                                        [oc.touch_key(r)], True, NOW + dt.timedelta(days=3))
            self.assertEqual([x['state'] for x in result], [state])
            self.assertEqual(issues, [])

    def test_prior_unknown_prose_is_not_silently_closed(self):
        r = self.prior_row(); r[8] = 'delivered and committed'
        self.write([r])
        result, _ = oc.evaluate(self.path, DAY, now=NOW)
        self.assertEqual([x['state'] for x in result], ['UNKNOWN'])

    def test_valid_prior_completion_and_will_ownership_leave_carryover(self):
        for state, owner in [('ASKED_RECEIPT', 'PROME'), ('ALREADY_CLOSED', 'PROME'),
                             ('ASKED_WORKING', 'WILL')]:
            r = self.prior_row(state, owner)
            self.write([r])
            result, issues = oc.evaluate(self.path, DAY, inventory_complete=True, now=NOW)
            self.assertEqual((result, issues), ([], []))

    def test_later_touch_cannot_clear_prior_unresolved_touch(self):
        old, current = self.prior_row(), row(touch='2')
        result, issues = self.evaluate([old, current])
        self.assertEqual([x['state'] for x in result], ['ASKED_WORKING', 'ASKED_RECEIPT'])
        self.assertEqual(issues, [])

    def test_future_touch_not_in_current_population(self):
        r = row(); r[0] = '2026-09-17'
        self.write([r])
        result, issues = oc.evaluate(self.path, DAY, inventory_complete=True, now=NOW)
        self.assertEqual((result, issues), ([], []))

    def test_overnight_completion_must_have_valid_receipt(self):
        r = self.prior_row('ASKED_RECEIPT')
        data = json.loads(r[8].split(oc.MARKER)[1])
        data['observed_at'] = '2026-09-16T00:30:00-04:00'
        data['receipt'] = ''
        r[8] = oc.MARKER + json.dumps(data)
        self.write([r])
        result, _ = oc.evaluate(self.path, DAY, now=NOW)
        self.assertEqual([x['state'] for x in result], ['UNKNOWN'])
        data['receipt'] = 'runtime completion after midnight'
        r[8] = oc.MARKER + json.dumps(data)
        self.write([r])
        result, issues = oc.evaluate(self.path, DAY, inventory_complete=True, now=NOW)
        self.assertEqual((result, issues), ([], []))

    def test_gate_calls_reader_at_both_boundaries(self):
        import prome_gate as gate
        import ast
        tree = ast.parse(Path(gate.__file__).read_text())
        functions = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
        for name in ('mode_boot', 'mode_closeout'):
            self.assertTrue(any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                                and n.func.id == 'check_orch_closeout' for n in ast.walk(functions[name])))
        with patch.object(gate, 'run_script') as run:
            gate.check_orch_closeout()
            self.assertEqual(run.call_args.args[0], gate.ADVISE)
            self.assertIn('PROME/tools/orch_closeout.py', run.call_args.args[2])


if __name__ == '__main__':
    unittest.main()
