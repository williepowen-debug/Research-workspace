"""L594 transfer: malformed inputs, quiet/capable cases and state-write boundary."""
import datetime as dt
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import fleet_dashboard as fd
import will_handbook as wh

DAY = dt.date(2026, 10, 3)
HEADER = 'gate_id\tregistered\towner\tcondition\tconsequence_on_fire\tstate\tlast_checked\tsource\n'
def gate(state='LIVE', name='G-1'):
    return f'{name}\t2026-10-01\tA\tcondition\taction\t{state}\t2026-10-02\tsource\n'
def fleet_row(**updates):
    r = dict(name='A', days=0, word='0d (own)', cls='ok', parked=False)
    r.update(updates)
    return r

class TransferTests(unittest.TestCase):
    def setUp(self):
        wh.ALERTS.clear()
        self.addCleanup(wh.ALERTS.clear)

    def panel(self, text, rows=None):
        with patch.object(fd, 'read', return_value=text), patch.object(fd, 'parse_roster', return_value=([('A','domain')],[],[])), patch.object(fd, 'parse_fleet_map', return_value={}), patch.object(fd, 'collect_fleet_rows', return_value=[fleet_row()] if rows is None else rows):
            return wh.render_fleet_panels(DAY)

    def test_valid_counts_and_named_fired_escaped(self):
        page = self.panel(HEADER + gate() + gate('FIRED-UNEXECUTED <script>', 'G-<x>') + gate('RETIRED', 'G-3'))
        self.assertIn('LIVE 1', page)
        self.assertIn('FIRED-UNEXECUTED 1', page)
        self.assertIn('G-&lt;x&gt;', page)
        self.assertNotIn('<script>', page)
        self.assertEqual(wh.ALERTS, [])

    def test_executed_prefix_not_silently_counted_as_live(self):
        text=HEADER+gate('FIRED-EXECUTED')
        with patch.object(fd,'read',return_value=text):
            self.assertEqual(fd.parse_gates(DAY)[0]['kind'],'live')  # legacy unchanged
        page=self.panel(text)
        self.assertIn('Gate counts unavailable',page)
        self.assertNotIn('<strong>LIVE',page)
        self.assertTrue(wh.ALERTS)

    def test_partial_malformed_row_cannot_disappear(self):
        page=self.panel(HEADER+gate()+'G-FIRED\tshort\n')
        self.assertIn('Gate counts unavailable',page)
        self.assertTrue(wh.ALERTS)

    def test_unknown_empty_and_prefix_tokens(self):
        for state in ('','NONSENSE','FROZEN','LIVELY','FIRED-UNEXECUTEDNESS'):
            with self.subTest(state=state):
                self.assertIn('Gate counts unavailable',self.panel(HEADER+gate(state)))

    def test_empty_header_missing_header_and_wrong_schema(self):
        for text in ('',HEADER,gate(),HEADER.replace('state','wrong')+gate()):
            with self.subTest(text=text):
                self.assertIn('Gate counts unavailable',self.panel(text))

    def test_duplicate_or_missing_id(self):
        for text in (HEADER+gate()+gate(),HEADER+gate(name='')):
            self.assertIn('Gate counts unavailable',self.panel(text))

    def test_read_failure_unavailable(self):
        with patch.object(fd,'read',side_effect=OSError('missing')):
            page=wh.render_fleet_panels(DAY)
        self.assertIn('Gate counts unavailable',page)
        self.assertTrue(wh.ALERTS)

    def test_no_history_not_999_days(self):
        page=self.panel(HEADER+gate(),[fleet_row(days=999,word='no git history',cls='crit')])
        self.assertIn('unavailable / no history',page)
        self.assertNotIn('999',page)

    def test_parked_unknown_stays_parked(self):
        page=self.panel(HEADER+gate(),[fleet_row(days=999,word='parked → 10/5',cls='none',parked=True)])
        self.assertIn('parked → 10/5',page)
        self.assertIn('unavailable / no history',page)
        self.assertNotIn('999',page)

    def test_empty_fleet_degraded_and_review(self):
        page=self.panel(HEADER+gate(),[])
        self.assertIn('Fleet freshness unavailable',page)
        self.assertTrue(any(leg=='fleet-freshness' for leg,_ in wh.ALERTS))

    def test_calendar_boundary_classes_and_missing(self):
        ages={'N':None,'A':3,'B':4,'C':7,'D':8,'E':14,'F':15,'P':30}
        with patch.object(fd,'load_parked',return_value={'P':(DAY,'reason')}),patch.object(fd,'agent_git',return_value=(0,5)),patch.object(fd,'inbox_depth',return_value=0),patch.object(fd.agent_freshness,'own_surface_age_days',side_effect=ages.get):
            rows=fd.collect_fleet_rows(DAY,[(n,'domain') for n in ages],{})
        self.assertEqual({r['name']:r['cls'] for r in rows},dict(N='crit',A='ok',B='watch',C='watch',D='elev',E='elev',F='crit',P='none'))
        self.assertEqual([r['name'] for r in rows],['N','F','E','D','C','B','A','P'])

    def test_parking_expires_after_inclusive_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'PROME/tools';p.mkdir(parents=True)
            (p/'dashboard_parked.tsv').write_text('A\t2026-10-03\towner\treason\n')
            with patch.object(fd,'REPO',tmp):
                self.assertIn('A',fd.load_parked(DAY))
                self.assertNotIn('A',fd.load_parked(DAY+dt.timedelta(days=1)))

    def test_prome_uses_real_home_excluding_inbox(self):
        with patch.object(fd,'load_parked',return_value={}),patch.object(fd,'agent_git',return_value=(0,0)),patch.object(fd,'inbox_depth',return_value=0),patch.object(fd.agent_freshness,'git',return_value='') as git,patch.object(fd.agent_freshness,'own_surface_age_days',side_effect=AssertionError('wrong home')):
            rows=fd.collect_fleet_rows(DAY,[('PROME','coordinator')],{})
        self.assertEqual(rows[0]['cls'],'crit')
        git.assert_called_once_with('log','-1','--format=%ct','--','PROME',':(exclude)PROME/inbox')

    def test_shared_helpers_never_call_build_or_write(self):
        with patch.object(fd,'build',side_effect=AssertionError('build called')),patch.object(fd,'write_build_receipt',side_effect=AssertionError('receipt written')),patch.object(wh.wb,'_persist_state',side_effect=AssertionError('feed persisted')):
            self.panel(HEADER+gate())

if __name__=='__main__':unittest.main()
