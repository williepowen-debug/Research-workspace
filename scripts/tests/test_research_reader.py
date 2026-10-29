"""Read-only fixture tests; no agents, model calls, network or owner writes."""
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import research_reader as rr


class ReaderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='research-reader-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.desk = self.root / 'AGENTS/CARL'
        (self.desk / 'research/nested').mkdir(parents=True)
        self.config = self.root / 'sources.json'
        self.config.write_text(json.dumps({'version': 1, 'desks': [dict(name='CARL',root='AGENTS/CARL',overview=['STATUS.md'],directories=['research'])]}))
        (self.desk/'STATUS.md').write_text('# Status\nOverview only\n')
        self.path = 'AGENTS/CARL/research/nested/2026-10-29_report.md'
        self.source = '# Café 🧭\n\n| Item | Claim |\n| a | VOID, not MISS |\n\n`$(never-run)` & "quote"\n[link](../other.md)\n'
        (self.root/self.path).write_text(self.source)
        self.reader = rr.Reader(self.root, self.config)

    def test_full_source_and_literal_search(self):
        for query in ['café','VOID, not MISS','$(never-run)','[link]','🧭']:
            result = self.reader.search(query)
            self.assertTrue(result['complete'])
            self.assertEqual([r['path'] for r in result['documents']], [self.path])
        self.assertEqual(self.reader.read(self.path)[0], self.source)
        self.assertEqual(self.reader.search('not-there')['documents'], [])
        self.assertFalse((self.root/'never-run').exists())

    def test_source_bytes_not_written_and_snapshot_refresh(self):
        before = (self.root/self.path).read_bytes()
        self.reader.scan()
        (self.desk/'research/new.md').write_text('new-only-needle')
        self.assertEqual(self.reader.search('new-only-needle')['documents'], [])
        self.reader.scan()
        self.assertEqual(len(self.reader.search('new-only-needle')['documents']),1)
        self.assertEqual((self.root/self.path).read_bytes(),before)

    def test_exclusions_and_frozen_research(self):
        for directory in ['archive','raw','source','backups','.cache','data']:
            p=self.desk/'research'/directory;p.mkdir();(p/'excluded.md').write_text('excluded marker')
        (self.desk/'research/FROZEN.md').write_text('frozen marker')
        (self.desk/'research/source.txt').write_text('excluded marker')
        self.assertEqual(self.reader.search('excluded marker')['documents'],[])
        self.assertEqual(len(self.reader.search('frozen marker')['documents']),1)
        for path in ['AGENTS/CARL/research/raw/excluded.md','AGENTS/CARL/research/source.txt','AGENTS/CARL/CLAUDE.md']:
            with self.assertRaises(ValueError):self.reader.read(path)

    def test_missing_overview_and_directory_are_not_zero_success(self):
        (self.desk/'STATUS.md').unlink()
        self.reader.desks[0]['directories'].append('audits')
        result=self.reader.search('VOID')
        self.assertFalse(result['complete']);self.assertEqual(len(result['documents']),1)
        self.assertEqual(len(result['issues']),2)

    def test_oversize_bad_encoding_and_fifo(self):
        (self.desk/'research/large.md').write_bytes(b'x'*(rr.MAX_FILE+1))
        (self.desk/'research/invalid.md').write_bytes(b'\xff')
        os.mkfifo(self.desk/'research/pipe.md')
        result=self.reader.search()
        self.assertFalse(result['complete']);self.assertEqual(len(result['issues']),3)
        self.assertEqual(len(result['documents']),2)

    def test_control_character_cannot_silently_truncate_display(self):
        (self.root/self.path).write_text('Visible\x00hidden caveat')
        with self.assertRaisesRegex(ValueError, 'control character'):
            self.reader.read(self.path)
        result = self.reader.search('hidden caveat')
        self.assertFalse(result['complete'])
        self.assertEqual(result['documents'], [])

    def test_symlink_file_and_directory_refused(self):
        (self.root/'outside.md').write_text('secret marker')
        (self.desk/'research/link.md').symlink_to(self.root/'outside.md')
        (self.desk/'research/linked').symlink_to(self.root, target_is_directory=True)
        result=self.reader.search('secret marker');self.assertFalse(result['complete'])
        self.assertEqual(result['documents'],[])
        with self.assertRaises(OSError):self.reader.read('AGENTS/CARL/research/link.md')
        with self.assertRaises(OSError):self.reader.read('AGENTS/CARL/research/linked/outside.md')

    def test_traversal_absolute_backslash_and_other_desk(self):
        for path in ['/etc/passwd','AGENTS/CARL/research/../../secret.md',r'AGENTS\CARL\research\a.md','AGENTS/OTHER/research/a.md','AGENTS/CARL/research//a.md']:
            with self.assertRaises(ValueError):self.reader.read(path)

    def test_symlink_replacement_after_discovery(self):
        self.reader.scan();p=self.root/self.path;p.unlink();p.symlink_to(self.root/'sources.json')
        with self.assertRaises(OSError):self.reader.read(self.path)

    def test_atomic_replacement_during_read_refused(self):
        original=self.reader._open;calls=0
        def replaced(path,directory=False):
            nonlocal calls
            calls+=1
            if calls==2:
                temp=self.root/'replacement';temp.write_text('different version');temp.replace(self.root/self.path)
            return original(path,directory)
        with patch.object(self.reader,'_open',side_effect=replaced):
            with self.assertRaisesRegex(ValueError,'replaced'):self.reader.read(self.path)

    def test_parent_swap_during_read_refused(self):
        original=self.reader._open;calls=0
        def swapped(path,directory=False):
            nonlocal calls
            calls+=1
            if calls==2:
                folder=self.desk/'research/nested';folder.rename(self.desk/'research/old')
                folder.symlink_to(self.root,target_is_directory=True)
            return original(path,directory)
        with patch.object(self.reader,'_open',side_effect=swapped):
            with self.assertRaises(OSError):self.reader.read(self.path)

    def test_stat_change_and_missing(self):
        req=dict(id=1,op='stat',path=self.path)
        old=self.reader.handle(req)['version'];(self.root/self.path).write_text('different')
        self.assertNotEqual(old,self.reader.handle(req)['version'])
        (self.root/self.path).unlink()
        with self.assertRaises(OSError):self.reader.handle(req)

    def test_limits_are_incomplete(self):
        for name,value in [('MAX_DOCS',1),('MAX_BYTES',10),('MAX_SECONDS',-1),('MAX_ENTRIES',0),('MAX_DEPTH',1)]:
            with self.subTest(name=name),patch.object(rr,name,value):
                self.reader.scan();self.assertTrue(self.reader.issues)

    def test_title_collisions_dates_and_filters(self):
        (self.desk/'research/2026-10-28_same.md').write_text(self.source)
        result=self.reader.search(category='Research')
        self.assertEqual(len(result['documents']),2)
        self.assertEqual(result['documents'][0]['path_date'],'2026-10-29')
        self.assertNotEqual(result['documents'][0]['path'],result['documents'][1]['path'])
        self.assertEqual(len(self.reader.search(category='Overview')['documents']),1)
        for kw in [dict(desk='UNKNOWN'),dict(category='Secrets'),dict(query='x'*1001)]:
            with self.assertRaises(ValueError):self.reader.search(**kw)

    def test_bom_and_long_lines_preserved(self):
        text='# BOM\n'+'z'*10000+'\n'
        (self.root/self.path).write_bytes(b'\xef\xbb\xbf'+text.encode())
        self.assertEqual(self.reader.read(self.path)[0],text)

    def test_protocol_recovers_and_ids_are_exact(self):
        requests=['not json',json.dumps(dict(id=4,op='launch')),json.dumps(dict(id=5,op='open',path=self.path))]
        out=io.StringIO();rr.serve(self.reader,io.StringIO('\n'.join(requests)+'\n'),out)
        responses=[json.loads(line) for line in out.getvalue().splitlines()]
        self.assertFalse(responses[0]['ok']);self.assertFalse(responses[1]['ok'])
        self.assertEqual(responses[2]['id'],5);self.assertEqual(responses[2]['text'],self.source)
        out=io.StringIO();rr.serve(self.reader,io.StringIO('x'*17000+'\n'),out)
        self.assertEqual(len(out.getvalue().splitlines()),1)

    def test_bad_config_and_overlaps(self):
        config=json.loads(self.config.read_text());config['desks'].append(dict(name='CHILD',root='AGENTS/CARL/sub_agents',overview=[],directories=['research']))
        self.config.write_text(json.dumps(config))
        with self.assertRaises(ValueError):rr.Reader(self.root,self.config)


if __name__ == '__main__':
    unittest.main()
