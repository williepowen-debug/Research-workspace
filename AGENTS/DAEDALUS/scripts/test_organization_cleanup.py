"""Adversarial owner assignment and global dependency context tests; temporary Git repos only."""
import datetime as dt
import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

HERE=Path(__file__).resolve().parent

def module(name):
    spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

docket=module('docket_owed');gate=module('daedalus_gate')

class Owners(unittest.TestCase):
    def test_accountable_shapes(self):
        cases=['PROME (DAEDALUS informed) / DAEDALUS (writer packet)',
               'DAEDALUS(writer)/PROME(DAEDALUS informed)',
               'DAEDALUS (writer; PROME informed)', 'DAEDALUS (informed; writer)',
               'DAEDALUS (not informed)', 'DAEDALUS informed / DAEDALUS (reviewer)',
               'DAEDALUS informed; DAEDALUS writer', 'DAEDALUS (informed / PROME',
               'DAEDALUS (tool owner for scripts/; writer; informed)']
        for owners in cases:
            with self.subTest(owners=owners),tempfile.TemporaryDirectory() as td:
                dk=Path(td)/'d';st=Path(td)/'s';st.write_text('nothing acknowledged')
                dk.write_text(docket.FIX_HEAD+docket._fx_row('2026-10-20',owners,'PENDING'))
                rc,lines=docket.assess(str(dk),str(st),dt.date(2026,10,20),30)
                self.assertEqual(rc,1);self.assertIn('uncited=1','\n'.join(lines))
                self.assertIn('L2','\n'.join(lines))
    def test_pure_informed_and_existing_descriptors(self):
        for owners in ['PROME / DAEDALUS informed','DAEDALUS (informed)',
                       'PROME(DAEDALUS informed)/DAEDALUS(informed-only)',
                       'DAEDALUS (cadence spec owner, informed)',
                       'DAEDALUS (tool owner for scripts/; informed)',
                       'DAEDALUS (informed, rule 19 owner)',
                       'DAEDALUS informed (tool owner, scripts/ grant)']:
            with self.subTest(owners=owners):self.assertTrue(docket.informed_only(owners))
    def test_roles_visible(self):
        text='PROME (DAEDALUS informed) / DAEDALUS (writer packet)'
        self.assertEqual(docket.owner_segment(text),text)
    def test_uncertain_and_negated_are_not_exempt(self):
        for owners in ['DAEDALUS uninformed','DAEDALUS informed (also writes)','DAEDALUS (never informed)',
                       'DAEDALUS (informed) writer','DAEDALUS(informed))','DAEDALUS(informed']:
            with self.subTest(owners=owners):self.assertFalse(docket.informed_only(owners))

class GlobalContext(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.git('init');self.git('config','user.email','test@example.test');self.git('config','user.name','fixture')
        (self.root/'seed').write_text('seed');self.git('add','seed');self.git('commit','-m','seed')
    def tearDown(self):self.temp.cleanup()
    def git(self,*args):
        return subprocess.check_output(['git','-C',str(self.root),*args],stderr=subprocess.DEVNULL,text=True).strip()
    def context(self,kind,**extra):
        return gate.context_value(str(self.root),dict(kind=kind,basis='current',reason='test',**extra))
    def test_untracked_child_and_default_status(self):
        d=self.root/'other';d.mkdir();(d/'first').write_text('a')
        before=self.context('global-status');(d/'second').write_text('b');after=self.context('global-status')
        self.assertEqual(before['porcelain'],after['porcelain'])
        self.assertNotEqual(before['all_untracked'],after['all_untracked'])
    def test_staged_change(self):
        before=self.context('global-status');(self.root/'seed').write_text('changed');self.git('add','seed')
        self.assertNotEqual(before,self.context('global-status'))
    def test_empty_and_outside_path_commits(self):
        before=self.context('global-history');self.git('commit','--allow-empty','-m','DAEDALUS empty claim')
        mid=self.context('global-history');self.assertNotEqual(before,mid)
        (self.root/'packet').write_text('owner');self.git('add','packet');self.git('commit','-m','DAEDALUS outside packet')
        self.assertNotEqual(mid,self.context('global-history'))
    def test_no_paths_or_commands(self):
        for kind in ['global-status','global-history']:
            for extra in [dict(paths=[]),dict(command='echo bypass')]:
                with self.subTest(kind=kind,extra=extra),self.assertRaises(ValueError):self.context(kind,**extra)
    def test_replacements_refused(self):
        first=self.git('rev-parse','HEAD');self.git('commit','--allow-empty','-m','other');second=self.git('rev-parse','HEAD')
        self.git('replace',first,second)
        with self.assertRaises(ValueError):self.context('global-history')
    def test_grafts_refused(self):
        p=self.root/'.git/info/grafts';p.write_text(self.git('rev-parse','HEAD')+'\n')
        with self.assertRaises(ValueError):self.context('global-history')
    def test_shallow_refused(self):
        (self.root/'.git/shallow').write_text(self.git('rev-parse','HEAD')+'\n')
        with self.assertRaises(ValueError):self.context('global-history')
    def test_unsupported_still_refused(self):
        with self.assertRaises((ValueError,KeyError)):self.context('arbitrary-query',paths=['seed'])
    def test_historical_vs_current_snapshot(self):
        candidate='AGENTS/DAEDALUS/fixture';p=self.root/candidate;p.parent.mkdir(parents=True);p.write_text('candidate')
        scope={'candidates':[{'path':candidate}],'dependencies':{'C8':{'context':[dict(kind='global-history',basis='historical',reason='original check')]}}}
        scope_path=self.root/'scope.json';scope_path.write_text('{}');base=self.git('rev-parse','HEAD')
        before=gate.candidate_snapshot(str(self.root),scope,str(scope_path),base)
        self.git('commit','--allow-empty','-m','DAEDALUS new claim')
        historic=gate.candidate_snapshot(str(self.root),scope,str(scope_path),base,historical=before)
        self.assertEqual(before,historic)
        scope['dependencies']['C8']['context'][0]['basis']='current'
        self.assertNotEqual(before,gate.candidate_snapshot(str(self.root),scope,str(scope_path),base,historical=before))

if __name__=='__main__':unittest.main()
