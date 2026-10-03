import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import render_directory as rd

class WatchForTests(unittest.TestCase):
    def parse(self,source):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'config.py';p.write_text(source)
            return rd.read_watch_for(p)

    def test_counts_empty_and_missing(self):
        counts,sha,error=self.parse("WATCH_FOR = {'A':['one','two'], 'B': []}")
        self.assertEqual(counts,{'A':2,'B':0});self.assertIsNone(error);self.assertEqual(len(sha),64)
        self.assertEqual(rd.watch_for_value('B',counts),'0')
        self.assertEqual(rd.watch_for_value('C',counts),'—')

    def test_unreadable_never_absence_or_exemption(self):
        with tempfile.TemporaryDirectory() as tmp:
            c,h,e=rd.read_watch_for(Path(tmp)/'missing')
        self.assertIsNone(c);self.assertIsNone(h);self.assertTrue(e)
        self.assertEqual(rd.watch_for_value('DAEDALUS',c),'UNKNOWN')

    def test_exemption_only_declared_and_source_present(self):
        self.assertEqual(rd.watch_for_value('DAEDALUS',{}),'n/a')
        self.assertEqual(rd.watch_for_value('DEWEY',{}),'n/a')
        self.assertEqual(rd.watch_for_value('RAV',{}),'—')
        self.assertEqual(rd.watch_for_value('DAEDALUS',{'DAEDALUS':2}),'2')
        with patch.object(rd,'REPO',Path('/absent-declaration')):
            self.assertEqual(rd.watch_for_value('DAEDALUS',{}),'—')

    def test_invalid_shape_keys_and_phrases(self):
        for source in ["WATCH_FOR={'A':'abc'}","WATCH_FOR={'A':['']}","WATCH_FOR={'A':[4]}","WATCH_FOR={4:[]}","WATCH_FOR={'A':[],'A':['x']}","WATCH_FOR=None","OTHER={}","WATCH_FOR = {"]:
            with self.subTest(source=source):self.assertIsNone(self.parse(source)[0])

    def test_aliases_mutation_and_shadowing_rejected(self):
        for source in ["WATCH_FOR = alias = {'A':['x']}","WATCH_FOR={'A':[]}\nWATCH_FOR['A'].append('x')","WATCH_FOR={}\nalias=WATCH_FOR","WATCH_FOR={}\nWATCH_FOR={}","WATCH_FOR={}\ndef WATCH_FOR(): pass", "WATCH_FOR={}\ndef f():pass\nf=3"]:
            with self.subTest(source=source):self.assertIsNone(self.parse(source)[0])

    def test_definition_time_execution_rejected(self):
        for source in ["WATCH_FOR={}\ndef f(x=WATCH_FOR.pop('A')): pass","WATCH_FOR={}\n@run()\ndef f(): pass","WATCH_FOR={}\ndef f(x:run()): pass"]:
            with self.subTest(source=source):self.assertIsNone(self.parse(source)[0])

    def test_never_executes_dynamic_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            sentinel=Path(tmp)/'written'
            source=f"WATCH_FOR={{}}\nopen({str(sentinel)!r},'w').write('bad')"
            self.assertIsNone(self.parse(source)[0]);self.assertFalse(sentinel.exists())
        self.assertIsNone(self.parse("WATCH_FOR={}\nexec('WATCH_FOR.clear()')")[0])

    def test_inert_functions_and_current_path_expression(self):
        c,_,e=self.parse("WATCH_FOR={'A':['x']}\nimport os\nBASE='/tmp'\nD=os.path.join(BASE,'AGENTS')\ndef match(x=None):\n return WATCH_FOR")
        self.assertEqual(c,{'A':1});self.assertIsNone(e)

    def test_check_does_not_write_or_change_rc_when_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'directory.md';out.write_text('sentinel')
            with patch.object(rd,'OUT',out),patch.object(rd,'REPO',Path(tmp)),patch.object(rd,'WATCH_CONFIG',Path(tmp)/'absent'),patch('sys.argv',['render_directory.py','--check']),contextlib.redirect_stdout(io.StringIO()) as buf:
                rd.main()
            self.assertEqual(out.read_text(),'sentinel')
            self.assertIn('rc=0',buf.getvalue())

    def test_extra_column_preserves_original_column_order(self):
        row=rd.row('A','utility','L4','H','2026-10-03','does','next',wf='3')
        self.assertEqual([x.strip() for x in row.split('|')[1:-1]],['A','utility','L4','H','2026-10-03','does','next','3'])

if __name__=='__main__':unittest.main()
