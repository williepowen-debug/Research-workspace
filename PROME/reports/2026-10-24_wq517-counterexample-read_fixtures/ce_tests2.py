import sys, unittest
sys.path.insert(0, '.')
from ce_tests import CE, sc, FP, UNC
class CE2(CE):
    def _ev_base(self):
        self.write('AGENTS/BROCK/ev.md', 'BROCK figure 42 is the basis\n'); self.git('add', '--', 'AGENTS/BROCK/ev.md')
        self.git('commit', '-qm', 'pre', '--', 'AGENTS/BROCK/ev.md'); self.base = self.git('rev-parse', 'HEAD'); sc.record_baseline(self.base)
    def test_ceI_historical_dep_live_file_pending(self):
        self._ev_base()
        self.plan['evidence'] = [{'path': 'AGENTS/BROCK/ev.md', 'commit': self.base, 'mode': 'historical', 'claims': {'PROME/result': 'cites 42'}}]
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/ev.md', 'BROCK revised figure 43\n')
        self.both('CE-I historical dep, live file edited after commit', ref=a, paths=['PROME/result'])
    def test_ceI2_current_dep_pending(self):
        self._ev_base()
        self.plan['evidence'] = [{'path': 'AGENTS/BROCK/ev.md', 'commit': self.base, 'mode': 'current', 'claims': {'PROME/result': 'cites 42'}}]
        self.freeze(); a = self.commit('PROME/result')
        self.write('AGENTS/BROCK/ev.md', 'BROCK revised figure 43\n')
        self.both('CE-I2 current dep edited after commit (--ref)', ref=a, paths=['PROME/result'])
        rc, l = sc.verify_review(); self.show('CE-I2 same at working-tree form', rc, l)
    def test_ceG3_head_below_target_history_path_pending(self):
        self.freeze()
        self.desk_commit('AGENTS/BROCK/h.md', 'desk\n', 'BROCK: h')
        self.desk_commit('AGENTS/BROCK/p.md', 'PROME wrote\n', 'PROME -> BROCK: p')
        a = self.commit('PROME/result')
        rc, l = sc.verify_review(ref=a, paths=['PROME/result']); self.show('CE-G3 control HEAD==a', rc, l)
        self.git('reset', '-q', '--soft', self.base)
        print('\nporcelain:', sc.porcelain_entries())
        rc, lines, *_ = self.both('CE-G3 HEAD reset to baseline, history paths now staged-pending', ref=a, paths=['PROME/result'])
        self.assertEqual(rc, 1)
if __name__ == '__main__':
    unittest.main()
