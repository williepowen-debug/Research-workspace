"""Behavioral checks for operator decisions, contract coverage and stale evidence."""
import csv
import datetime as dt
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import desk_attention as da
import fleet_dashboard as fd
import will_brief as wb


class AttentionTests(unittest.TestCase):
    def test_all_schemas_keep_lots_spreads_and_live_rows_with_historical_closure_words(self):
        rows, errors = da.holdings()
        self.assertFalse(errors)
        keys = [da.key(r) for r in rows]
        self.assertIn(('Fidelity', 'QQQ', '$715P', '2026-09-10'), keys)
        self.assertIn(('Fidelity', 'TLT', '$77P', '2026-09-30'), keys)
        self.assertIn(('Fidelity', 'WAL', '$70P', '2026-09-18'), keys)
        self.assertIn(('Fidelity', 'WAL', '$67.5P', '2026-09-18'), keys)
        self.assertIn(('Robinhood', 'USO', '$150/$165 call spread', '2026-09-18'), keys)
        self.assertEqual(keys.count(('Fidelity', 'KRE', '$60P', '2026-12-18')), 2)
        self.assertFalse(any(r['instrument'] == '$135C' for r in rows))
        self.assertFalse(any(r['expiry'] == '2026-08-31' for r in rows))
        self.assertEqual(da.instrument_name('$20C/$25C call debit spread'), '$20C/$25C')

    def test_expiry_uses_book_year_never_rolls_expired_option_to_next_year(self):
        self.assertEqual(da.expiry_date('Jan-15', 2026), '2026-01-15')
        self.assertEqual(da.expiry_date('1/15/2027', 2026), '2027-01-15')
        self.assertEqual(da.expiry_date('Sep-10-2026', 2025), '2026-09-10')

    def test_exact_contract_mapping_does_not_inherit_other_strikes_or_accounts(self):
        rows, errors = da.coverage()
        self.assertFalse(errors)
        get = lambda a,t,i,e: next(r for r in rows if da.key(r) == (a,t,i,e))
        self.assertEqual(get('Fidelity','USO','Stock','')['gates'], [])
        self.assertEqual(get('Fidelity','TLT','$82P','2026-10-16')['gates'], [])
        self.assertEqual(get('Fidelity','TLT','$85P','2026-09-30')['gates'], [])
        self.assertEqual(get('Fidelity','TLT','$77P','2026-09-30')['gates'][0][0], 'GATE-TERRY-007')
        self.assertEqual(get('Fidelity','WAL','$70P','2026-09-18')['gates'], [])
        self.assertEqual(get('Robinhood','WAL','$70P','2026-12-18')['gates'][0][0], 'GATE-TERRY-ROLL70-EXIT')
        qqq = get('Fidelity','QQQ','$715P','2026-09-10')
        self.assertIn('capture timestamp and account header absent', qqq['observation'])
        self.assertEqual(qqq['management']['approval'], 'NOT_RECORDED')
        for tick, strike in [('XLE','$65C'), ('TLT','$85P')]:
            m = get('Fidelity',tick,strike,'2026-09-30')['management']
            self.assertEqual((m['approval'],m['order'],m['fill']), ('APPROVED','UNKNOWN','UNKNOWN'))

    def fixture(self, directory):
        root = Path(directory)
        for name in ('FORGE/STATUS.md','FORGE/position_management.tsv','PROME/GATES.tsv'):
            path = root/name;path.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(da.ROOT/name,path)
        with (da.ROOT/'FORGE/position_management.tsv').open() as f:
            for row in csv.DictReader(f,delimiter='\t'):
                path = root/row['source']
                if not path.exists():
                    path.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copyfile(da.ROOT/row['source'],path)
        return root

    def test_changed_source_withholds_only_its_mapping(self):
        with tempfile.TemporaryDirectory() as d:
            root=self.fixture(d)
            p=root/'AGENTS/TERRY/setups/TLT85P_approved-exit-tracking_2026-09-08.md'
            p.write_text(p.read_text()+'\nChanged ruling\n')
            rows,errors=da.coverage(root)
            self.assertTrue(errors)
            tlt85=next(r for r in rows if r['instrument']=='$85P')
            self.assertIsNone(tlt85['management'])
            self.assertEqual(tlt85['qty'],'1')
            xle=next(r for r in rows if r['ticker']=='XLE')
            self.assertIsNotNone(xle['management'])

    def test_duplicate_registry_or_missing_evidence_never_says_covered(self):
        with tempfile.TemporaryDirectory() as d:
            root=self.fixture(d); p=root/'FORGE/position_management.tsv'
            s=p.read_text();p.write_text(s+s.splitlines()[1]+'\n')
            rows,errors=da.coverage(root)
            self.assertTrue(errors)
            self.assertTrue(all(r['management'] is None for r in rows))
            p.write_text(s)
            (root/'PROME/reports/2026-09-09_morning-priorities.md').unlink()
            rows,errors=da.coverage(root)
            self.assertTrue(errors)
            self.assertIsNone(next(r for r in rows if r['ticker']=='XLE')['management'])

    def test_docket_includes_overdue_preserves_line_and_excludes_terminal_and_distant(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'PROME').mkdir()
            (root/'PROME/DOCKET.tsv').write_text('# header\n2026-09-08\tPrior\tPROME\tPENDING\treceipt\tVerify delivery\n2026-09-10\tDone\tPROME\tRESOLVED\tx\tx\n2026-10-01\tLater\tPROME\tPENDING\tx\tx\n2026-09-10\tDesk\tBRENT\tPENDING\tx\tx\n')
            rows=da.pending_work(root,dt.date(2026,9,9))
            self.assertEqual([(r['line'],r['title'],r['timing']) for r in rows],[(2,'Prior','OVERDUE')])

    def test_receipt_amount_and_settlement_come_from_receipt_not_account_cash(self):
        receipts=da.confirmed_receipts()
        self.assertEqual(len(receipts),1)
        f=receipts[0][1]
        self.assertEqual(f['Net amount'],'$1,754.30')
        self.assertEqual(f['Settlement'],'September 10, 2026')
        page,errors=da.render()
        self.assertFalse(errors)
        self.assertIn('Settlement date is not confirmation of settled cash',page)
        self.assertIn('Complete when: Share exit/profit-protection proposal delivered',page)
        self.assertIn('Complete when: Hold/exit assessment and explicit management proposal delivered',page)
        self.assertNotIn('$19,243.32',page)

    def test_actual_pages_show_actions_unknown_coverage_and_no_old_decision_asks(self):
        for path in ('PROME/artifacts/handbook.html','PROME/artifacts/fleet_dashboard.html'):
            page=(da.ROOT/path).read_text()
            for token in ('broker-actions','management-coverage','confirmed-changes','prome-work','Approval: APPROVED · Order: UNKNOWN · Fill: UNKNOWN','Management mapping UNRECORDED','hosted publication unverified'):
                self.assertIn(token,page)
        dec,chore=wb.parse_actions()
        self.assertFalse({str(n) for n in (151,159,162,164,196,197,198,199)} & {r['n'] for r in dec+chore})
        page=(da.ROOT/'PROME/artifacts/handbook.html').read_text()
        self.assertNotIn('CboeSeptember8 and PJM post23:59 outcome remain ungraded',page)
        self.assertNotIn('no LIVE gate — last: GATE-TERRY-USO135C',page)

    def test_failed_attention_does_not_advance_dashboard_baseline(self):
        with tempfile.TemporaryDirectory() as d:
            out,state=Path(d)/'out.html',Path(d)/'state.json';state.write_text('before')
            with patch.object(fd,'STATE_PATH',str(state)),patch.object(fd,'build',return_value=('visible error',{'heartbeat_errors':[],'attention_errors':['missing source']})),patch.object(sys,'argv',['fleet_dashboard','-o',str(out)]):
                self.assertEqual(fd.main(),1)
            self.assertEqual(state.read_text(),'before')

if __name__=='__main__':unittest.main()
