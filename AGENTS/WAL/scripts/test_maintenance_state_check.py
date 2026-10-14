"""Regression cases from PROME's housekeeping audit; run with unittest."""
from pathlib import Path
import shutil,tempfile,unittest
from maintenance_state_check import current_fields,compare_history,fingerprint

DESK=Path(__file__).resolve().parents[1]

class MaintenanceRegressions(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        for name in ['workbook/KB.tsv','workbook/KB_INDEX.md','INDEX.md','POSITIONS.md','CLAUDE.md']:
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(DESK/name,p)
    def tearDown(self):self.temp.cleanup()
    def mutate(self,name,old,new):
        p=self.root/name;s=p.read_text();self.assertIn(old,s);p.write_text(s.replace(old,new,1))
    def test_repaired_current_state(self):self.assertEqual(current_fields(self.root),[])
    def test_old_charter_one_leg_is_detected(self):
        p=self.root/'CLAUDE.md';p.write_text(p.read_text()+'\nLive book = one Dec-18 $70P.\n')
        self.assertIn('position-mirror',[x[0] for x in current_fields(self.root)])
    def test_accepted_activity_date_cannot_stay_unknown(self):
        self.mutate('POSITIONS.md','**Bought October7**','Acquisition date / fill price / card: UNKNOWN')
        self.assertIn('position-acquisition',[x[0] for x in current_fields(self.root)])
    def test_old_unannounced_row_is_detected(self):
        p=self.root/'workbook/KB.tsv';s=p.read_text().splitlines()
        for i,line in enumerate(s):
            if line.startswith('KB-WAL-197\t'):s[i]=line.replace('\tSUPERSEDED\t','\tACTIVE\t',1)
        p.write_text('\n'.join(s)+'\n')
        self.assertIn('obsolete-earnings-date',[x[0] for x in current_fields(self.root)])
    def test_wrong_nav_group_count_is_detected(self):
        self.mutate('workbook/KB_INDEX.md','| HIDDEN_CRE | 39 |','| HIDDEN_CRE | 37 |')
        self.assertIn('KB-group',[x[0] for x in current_fields(self.root)])
    def test_old_index_auto_loading_is_detected(self):
        p=self.root/'INDEX.md';p.write_text(p.read_text()+'\nCLAUDE.md auto-loads when launched from this dir.\n')
        self.assertIn('runtime-loading',[x[0] for x in current_fields(self.root)])
    def test_cleared_history_does_not_offset_new_hit(self):
        old=[{'identity':'accepted-history-a'},{'identity':'accepted-history-b'}]
        now=[{'identity':'accepted-history-b'},{'identity':'new-live-error'}]
        new,cleared=compare_history(now,old)
        self.assertEqual(sum(new.values()),1);self.assertEqual(sum(cleared.values()),1)
    def test_line_number_changes_do_not_create_new_identity(self):
        a=['INDEX.md',10,'KBrows','209 (actual 227)'];b=['INDEX.md',90,'KBrows','209 (actual 229)']
        self.assertEqual(fingerprint('value',a,'Same historical row'),fingerprint('value',b,'Same historical row'))

if __name__=='__main__':unittest.main()
