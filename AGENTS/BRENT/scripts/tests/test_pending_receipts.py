"""False-green and false-positive receipt regressions; no network or broker writes."""
import contextlib
import importlib.util
import io
from datetime import date
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    'pending', Path(__file__).resolve().parents[1] / 'pending_receipts.py')
pending = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pending)


def document(execution='| 2026-09-15 | XLE exit | RESOLVED; receipt in hand |',
             position='| USO 37 shares | Shares | HELD | Owner |'):
    return ('## POSITIONS (live)\n| Position | Type | Status | Source |\n'
            '|---|---|---|---|\n' + position + '\n\n'
            '## Decision read paths\n| Position review / pending receipt | Read owner |\n'
            '## EXECUTION LOG\n| Date | Action | Detail |\n|---|---|---|\n'
            + execution + '\n## HISTORY\n| Yesterday | USO | PENDING |\n')


class Receipts(unittest.TestCase):
    def test_navigation_and_history_do_not_create_receipts(self):
        self.assertEqual(pending.rows_with_pending(document()), [])

    def test_historical_filled_word_does_not_hide_pending_exit(self):
        row = '| 2026-09-15 | USO exit | Entry FILLED; exit receipt PENDING |'
        self.assertEqual(pending.rows_with_pending(document(row)), [row])

    def test_unresolved_is_not_resolved(self):
        row = '| 2026-09-15 | USO exit | UNRESOLVED |'
        self.assertEqual(pending.rows_with_pending(document(row)), [row])

    def test_resolved_row_can_describe_former_pending_state(self):
        row = '| 2026-09-15 | XLE | ✅ **RECEIPT IN HAND:** row sat PENDING for days |'
        self.assertEqual(pending.rows_with_pending(document(row)), [])

    def test_explicit_pending_wins_over_fill_narrative(self):
        row = '| 2026-09-15 | USO | receipt_status=PENDING; entry FILLED |'
        self.assertEqual(pending.rows_with_pending(document(row)), [row])

    def test_qualified_legacy_hourglass_is_not_pending(self):
        row = '| 2026-09-10 | USO spread CLOSED | Source receipt. ⏳ RESOLVED — no further receipt owed |'
        self.assertEqual(pending.rows_with_pending(document(row)), [])
        separate = row.replace('Source receipt.', 'Separate fee receipt PENDING.')
        self.assertEqual(pending.rows_with_pending(document(separate)), [separate])

    def test_expiry_is_not_assumed_worthless(self):
        row = '| USO Sep-11 159C | Call | HELD; expiry=2026-09-11 | Other contract SOLD |'
        text = document(position=row)
        self.assertEqual(pending.expired_without_outcome(text, date(2026, 9, 15)), [row])
        self.assertEqual(pending.expired_without_outcome(text, date(2026, 9, 11)), [])

    def test_confirmed_sale_discharges_expiry_with_unknown_price(self):
        row = '| USO Sep-11 159C ×0 | CLOSED | Sold; expiry=2026-09-11 | Price UNKNOWN |'
        self.assertEqual(pending.expired_without_outcome(document(position=row), date(2026, 9, 15)), [])

    def run_check(self, text, forge=None):
        with tempfile.TemporaryDirectory() as d:
            trade_path, forge_path = Path(d) / 'TRADE.md', Path(d) / 'FORGE.md'
            trade_path.write_text(text)
            if forge is not None:
                forge_path.write_text(forge)
            out = io.StringIO()
            with patch.object(pending, 'TRADE', trade_path), patch.object(pending, 'FORGE', forge_path), contextlib.redirect_stdout(out):
                code = pending.main()
            return code, out.getvalue()

    def test_missing_section_cannot_pass(self):
        self.assertEqual(self.run_check('## Renamed\n| USO | PENDING |')[0], 2)

    def test_no_mirror_contradiction_does_not_clear_pending(self):
        text = document('| 2026-09-15 | USO exit | PENDING |')
        self.assertEqual(self.run_check(text, '| USO | Shares | HELD | 37 |')[0], 2)
        self.assertEqual(self.run_check(text)[0], 2)

    def test_other_contract_closure_is_candidate_not_proof(self):
        text = document('| 2026-09-15 | USO Sep-11 159C | PENDING |')
        code, out = self.run_check(text, '| USO Oct-16 135C | CLOSED | 0 | owner |')
        self.assertEqual(code, 2)
        self.assertIn('CANDIDATES', out)
        self.assertNotIn('contradicts a PENDING', out)

    def test_clean_receipt_surface_passes(self):
        self.assertEqual(self.run_check(document())[0], 0)


if __name__ == '__main__':
    unittest.main()
