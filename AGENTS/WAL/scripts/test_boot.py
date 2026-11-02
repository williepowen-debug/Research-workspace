"""Offline regression cases for boot.py; run with unittest from scripts/. Live owner files are read, never hard-coded values."""
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from unittest import mock
import base64,contextlib,io,json,re,unittest
from boot import (Report,latest_quarter_end,periodic_report,call_report_due,jwt_expiry,form4_codes,classify,
                  thesis_ev,exit_level,exit_log_last,mi3_last_quarter,kb_latest_finra_settlement,status_last_updated,
                  tracker_last,filings_section)

DESK=Path(__file__).resolve().parents[1];ROOT=DESK.parents[1]

def form4(*codes,table='nonDerivative'):
    tx=''.join(f'<{table}Transaction><transactionCoding><transactionCode>{c}</transactionCode></transactionCoding></{table}Transaction>' for c in codes)
    return f'<ownershipDocument><{table}Table>{tx}</{table}Table></ownershipDocument>'

class Calendar(unittest.TestCase):
    def test_quarter_end_is_strictly_before_today(self):
        self.assertEqual(latest_quarter_end(date(2026,10,28)),date(2026,9,30))
        self.assertEqual(latest_quarter_end(date(2026,9,30)),date(2026,6,30))
        self.assertEqual(latest_quarter_end(date(2027,1,5)),date(2026,12,31))
    def test_statutory_dates_match_the_desk_record(self):
        # 9/30 10-Q statutory Mon 11/9 and Call Report due 10/30 are the dates STATUS carries.
        self.assertEqual(periodic_report(date(2026,9,30)),('10-Q',date(2026,11,9)))
        self.assertEqual(periodic_report(date(2026,12,31)),('10-K',date(2027,3,1)))
        self.assertEqual(call_report_due(date(2026,9,30)),date(2026,10,30))

class Parsers(unittest.TestCase):
    def test_jwt_expiry_reads_exp_and_refuses_garbage(self):
        payload=base64.urlsafe_b64encode(json.dumps({'exp':1793851200}).encode()).decode().rstrip('=')
        self.assertIsNotNone(jwt_expiry('h.'+payload+'.s'))
        self.assertIsNone(jwt_expiry('not-a-jwt'))
    def test_form4_open_market_codes_are_separated_from_settlements(self):
        self.assertEqual(form4_codes(form4('M','D')),(['M','D'],[]))
        self.assertEqual(form4_codes(form4('S')),(['S'],[]))
        self.assertEqual(form4_codes(form4('M',table='derivative')),([],['M']))
    def test_classification(self):
        self.assertEqual(classify('10-Q',[])[0],'carrier')
        self.assertIn('detected',classify('10-Q',[])[1])
        self.assertNotIn('run the frozen',classify('10-Q',[])[1])
        self.assertIn('amendment detected',classify('10-Q/A',[])[1])
        self.assertEqual(classify('144',[])[0],'attention')
        self.assertEqual(classify('SCHEDULE 13G/A',[])[0],'attention')
        self.assertIn('🔴',classify('8-K',['2.06','9.01'])[1])
        self.assertNotIn('🔴',classify('8-K',['2.02','9.01'])[1])
        self.assertEqual(classify('DEF 14A',[])[0],'info')

class FilingAlerts(unittest.TestCase):
    def test_report_and_amendment_are_detected_without_repeat_grading_instruction(self):
        rows=[{'form':'10-Q','filingDate':'2026-10-30','reportDate':'2026-09-30','accessionNumber':'0001628280-26-068599','items':'','primaryDocument':'wal-20260930.htm'},
              {'form':'10-Q/A','filingDate':'2026-11-02','reportDate':'2026-09-30','accessionNumber':'0001628280-26-000000','items':'','primaryDocument':'wal-20260930a.htm'}]
        recent={k:[r[k] for r in rows] for k in rows[0]}
        payload=json.dumps({'filings':{'recent':recent}})
        rep=Report();out=io.StringIO()
        with mock.patch('boot.http',return_value=payload),contextlib.redirect_stdout(out):
            filings_section(rep,date(2026,11,2),date(2026,10,30),SimpleNamespace(offline=False))
        text=out.getvalue()
        self.assertEqual(len(rep.attention),2)
        self.assertIn('10-Q/A',text);self.assertIn('amendment detected',text)
        self.assertIn('0001628280-26-068599',text);self.assertIn('0001628280-26-000000',text)
        self.assertNotIn('run the frozen frame',text)
    def test_offline_sec_source_remains_visible(self):
        rep=Report();out=io.StringIO()
        with contextlib.redirect_stdout(out):
            filings_section(rep,date(2026,11,2),date(2026,10,30),SimpleNamespace(offline=True))
        self.assertEqual(rep.unchecked,['SEC EDGAR (offline)'])
        self.assertIn('UNCHECKED: SEC EDGAR (offline)',out.getvalue())

class OwnerFiles(unittest.TestCase):
    """Each reader must find its value in the live owner file; a reader returning None would print a silent blank."""
    def test_ev_is_read_from_thesis_and_agrees_with_status_mirror(self):
        ev=thesis_ev((DESK/'THESIS.md').read_text())
        self.assertIsNotNone(ev)
        self.assertIsNotNone(re.search(rf'EV \${ev:.2f}\b',(DESK/'STATUS.md').read_text()))
    def test_exit_level_and_log_are_read_from_reginald(self):
        lvl=exit_level((ROOT/'AGENTS/REGINALD/registry/THRESHOLDS.tsv').read_text())
        self.assertIsNotNone(lvl)
        self.assertIsNotNone(exit_log_last((ROOT/'AGENTS/REGINALD/registry/REG_T02_EXIT_LOG.tsv').read_text()))
    def test_mi3_status_and_kb_dates_parse(self):
        self.assertIsNotNone(mi3_last_quarter((DESK/'workbook/MI3_SERIES.tsv').read_text()))
        self.assertIsNotNone(status_last_updated((DESK/'STATUS.md').read_text()))
        kb=(DESK/'workbook/KB.tsv').read_text();d=kb_latest_finra_settlement(kb)
        self.assertIsNotNone(d);self.assertIn(f'FINRA settlement {d.isoformat()}',kb)
    def test_superseded_short_interest_rows_are_ignored(self):
        kb=(DESK/'workbook/KB.tsv').read_text().splitlines()
        hdr=next(l for l in kb if l.startswith('ID\t'));cols=hdr.split('\t')
        row=['']*len(cols);row[cols.index('ID')]='KB-WAL-999';row[cols.index('Status')]='SUPERSEDED'
        row[cols.index('Fact')]='FINRA settlement 2099-01-15: test row'
        self.assertIsNone(re.search('2099',str(kb_latest_finra_settlement(hdr+'\n'+'\t'.join(row)))))
    def test_tracker_last_reads_the_live_ledger_and_ignores_comment_lines(self):
        t=(DESK/'workbook/MARKET_TRACKER.tsv').read_text()
        for m in ('short_interest_shares','close_WAL','shares_outstanding'):
            d=tracker_last(t,m);self.assertIsNotNone(d,m);self.assertIn(f'{d.isoformat()}\t{m}\t',t)
        self.assertIsNone(tracker_last('# 2099-01-01\tclose_WAL\tx\n',"close_WAL"))

class Tracker(unittest.TestCase):
    def test_denominator_is_the_latest_cover_count_on_or_before_the_settlement(self):
        from market_tracker import denominator
        sh=[('2026-05-04',109185360),('2026-07-28',109100864)]
        self.assertEqual(denominator(sh,'2026-07-27'),('2026-05-04',109185360))
        self.assertEqual(denominator(sh,'2026-07-28'),('2026-07-28',109100864))
        self.assertIsNone(denominator(sh,'2026-05-03'))
    def test_every_short_pct_row_recomputes_from_its_own_ledger_inputs(self):
        from market_tracker import read_rows,denominator
        rows=read_rows((DESK/'workbook/MARKET_TRACKER.tsv').read_text())
        sh=[(r['Date'],int(r['Value'])) for r in rows if r['Metric']=='shares_outstanding']
        si={r['Date']:int(r['Value']) for r in rows if r['Metric']=='short_interest_shares'}
        pct=[r for r in rows if r['Metric']=='short_pct_shares_out'];self.assertTrue(pct)
        for r in pct:self.assertEqual(r['Value'],f"{si[r['Date']]/denominator(sh,r['Date'])[1]*100:.2f}")
    def test_vol_and_beta_on_a_known_series(self):
        from market_tracker import realized_vol,beta
        x=[100*(1.01 if i%2 else 0.99)**i for i in range(70)]
        self.assertAlmostEqual(beta(x,x,60),1.0,places=9)
        self.assertGreater(realized_vol(x,20),0)

if __name__=='__main__':unittest.main()
