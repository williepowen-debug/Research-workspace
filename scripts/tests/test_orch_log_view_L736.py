"""Public-view refusal contract; temp files only, never production state."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import types
import unittest

spec = importlib.util.spec_from_file_location('orch', Path(__file__).parents[1] / 'orch_log.py')
orch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(orch)

class ViewContract(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.ledger = str(Path(self.tmp.name) / 'ledger.tsv')
        self.view = str(Path(self.tmp.name) / 'view.md')
        self.row = ['2026-10-20', 'TEST', 'window', '1', 'test', '0', 'DONE', 'OK', 'test', '', '', '', '0']
        Path(self.ledger).write_text('\t'.join(orch.COLS)+'\n'+'\t'.join(self.row)+'\n')
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(orch.write_view(self.ledger, self.view), 0)

    def call(self, ack=None):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            rc=orch.guarded_view(self.ledger,self.view,acknowledge_unobserved=ack)
        return rc,out.getvalue()

    def refused_unchanged(self, ack=None):
        before=(Path(self.ledger).read_bytes(),Path(self.view).read_bytes())
        self.assertEqual(self.call(ack)[0],2)
        self.assertEqual(before,(Path(self.ledger).read_bytes(),Path(self.view).read_bytes()))

    def test_equal_count(self):
        self.assertEqual(self.call()[0],0)
        self.assertEqual(self.call(0)[0],0)

    def test_rise_and_legitimate_ack_append(self):
        with open(self.ledger,'a') as f: f.write('\t'.join(self.row)+'\n')
        self.refused_unchanged()
        args=types.SimpleNamespace(**dict(zip(orch.COLS,self.row)),acknowledge_unobserved=1)
        args.touch='2'
        with contextlib.redirect_stdout(io.StringIO()): self.assertEqual(orch.append(args,self.ledger,self.view),0)
        self.assertIn('ACK-UNOBSERVED 1',Path(self.ledger).read_text())
        self.assertEqual(self.call()[0],0)

    def test_ahead(self):
        p=Path(self.view);p.write_text(p.read_text().replace('(1 data rows)','(2 data rows)'))
        self.refused_unchanged()

    def test_bad_header(self):
        Path(self.view).write_text('no baseline\n');self.refused_unchanged()

    def test_invalid_ledger(self):
        with open(self.ledger,'a') as f:f.write('bad\trow\n')
        self.refused_unchanged()

    def test_missing_baseline(self):
        Path(self.view).rename(Path(self.view+'.old'))
        rc,out=self.call();self.assertEqual(rc,0);self.assertIn('does not establish writer provenance',out)

    def test_ack_not_silently_accepted(self):
        for ack in (1,-1): self.refused_unchanged(ack)

if __name__=='__main__': unittest.main()
