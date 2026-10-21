import argparse
import datetime as dt
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(sys.argv.pop(1)).resolve()
sys.path.insert(0,str(ROOT/'scripts'))
import orch_time as t
import orch_log as w
spec=importlib.util.spec_from_file_location('oc',ROOT/'PROME/tools/orch_closeout.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
NOW=dt.datetime(2026,10,21,2,tzinfo=dt.timezone.utc)

def original():
    return ['2026-10-16','reader','subagent','1-SPAWN','read','', 'DELIVERED','','closeout_v1='+json.dumps(dict(owner='PROME',session_id='s',touch_at='2026-10-16T16:30:00Z',observed_at='2026-10-16T18:49:32Z',state='ALREADY_CLOSED',receipt='native record')),'','','','']

def correction(o):
    return ['2026-10-20',o[1],o[2],'CLOSE','invalidate','','TIME-CORRECTION (original time UNKNOWN)','','time_correction_v1='+json.dumps(dict(target=t.key(o),owner='PROME',session_id='s',replacement='UNKNOWN',recorded_at=NOW.isoformat(),reason='L748 placeholder predates source')),'','','','']

def modify(row,**values):
    d=t.payload(row,t.MARKER);d.update(values);row[8]=t.MARKER+json.dumps(d);return row

class Repair(unittest.TestCase):
    def test_valid_unknown_not_new_spawn(self):
        o=original();q=correction(o)
        result,issues=c.reconcile([(t.key(r),r) for r in (o,q)],NOW)
        self.assertFalse(issues);self.assertEqual(len(result),1);self.assertEqual(result[0]['state'],'UNKNOWN')
        self.assertEqual(w.event_type(q),'CLOSE_SUMMARY')
    def test_bad_corrections(self):
        for change in [dict(target='x'*64),dict(session_id='other'),dict(owner='WILL'),dict(replacement='2026-10-16T18:00:00Z'),dict(reason=''),dict(recorded_at='2026-10-22T00:00:00Z')]:
            with self.subTest(change=change):
                o=original();q=modify(correction(o),**change)
                rows,issues=c.reconcile([(t.key(r),r) for r in (o,q)],NOW)
                self.assertTrue(issues);self.assertEqual(rows[-1]['state'],'UNKNOWN')
    def test_duplicate_target(self):
        o=original()
        with self.assertRaises(ValueError):t.validate_correction(correction(o),[o,o],NOW)
    def test_correction_target_not_original(self):
        o=original();q=correction(o);z=modify(correction(o),target=t.key(q))
        with self.assertRaises(ValueError):t.validate_correction(z,[o,q],NOW)
    def test_malformed(self):
        o=original();q=correction(o);q[8]=t.MARKER+'['
        rows,issues=c.reconcile([(t.key(r),r) for r in (o,q)],NOW)
        self.assertTrue(issues);self.assertEqual(rows[-1]['state'],'UNKNOWN')
    def test_counts_refused(self):
        o=original();q=correction(o);q[5]='0'
        with self.assertRaises(ValueError):t.validate_correction(q,[o],NOW)
    def test_later_receipt_does_not_restore(self):
        o=original();q=correction(o);r=original();r[0]='2026-10-20';r[3]='2-RESOLVE';r[4]='receipt'
        d=t.payload(r,t.CLOSEOUT);d.update(touch_at=NOW.isoformat(),observed_at=NOW.isoformat(),resolves=[t.key(o)])
        r[8]=t.CLOSEOUT+json.dumps(d)
        result,issues=c.reconcile([(t.key(x),x) for x in (o,q,r)],NOW)
        self.assertFalse(issues);self.assertEqual(len(result),1);self.assertEqual(result[0]['state'],'UNKNOWN')
    def test_writer_and_rotation(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'log.tsv';v=Path(d)/'view.md';o=original()
            before='\t'.join(w.COLS)+'\n'+'\t'.join(o)+'\n';p.write_text(before)
            q=correction(o)
            self.assertEqual(w.append(argparse.Namespace(**dict(zip(w.COLS,q))),str(p),str(v)),0)
            self.assertTrue(p.read_text().startswith(before));self.assertEqual(len(w.check(str(p),True)[1]),2)
            self.assertNotIn('TIME-CORRECTION',v.read_text())
            frozen=p.read_bytes()
            self.assertEqual(w.rotate('2026-10',str(p),str(Path(d)/'archive'),dt.date(2026,11,1),str(v)),2)
            self.assertEqual(p.read_bytes(),frozen)
            q=modify(correction(o),target='x'*64)
            self.assertEqual(w.append(argparse.Namespace(**dict(zip(w.COLS,q))),str(p),str(v)),2)
            self.assertEqual(p.read_bytes(),frozen)
    def test_reader_includes_only_correction_close(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'log';o=original();q=correction(o);other=original();other[3]='CLOSE';other[4]='normal summary'
            p.write_text('\n'.join('\t'.join(r) for r in [w.COLS,o,q,other])+'\n')
            self.assertEqual(len(c.read_touches(p,dt.date(2026,10,20))),2)
    def test_mixed_marker_never_resolves_or_hides(self):
        o=original();q=correction(o)
        q[8]=t.MARKER+'{} '+o[8]
        result,issues=c.reconcile([(t.key(r),r) for r in (o,q)],NOW)
        self.assertTrue(issues);self.assertEqual(result[-1]['state'],'UNKNOWN')
    def test_malformed_correction_blocks_unrelated_rotation(self):
        o=original();q=modify(correction(o),reason='')
        unrelated=original();unrelated[4]='other'
        self.assertIsNotNone(t.rotation_problem([o,q,unrelated],[unrelated]))
    def test_empty_population_and_bad_header(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);log=p/'ledger'
            def git(*args):subprocess.run(['git','-C',d,*args],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            git('init');git('config','user.email','fixture@example.test');git('config','user.name','fixture')
            (p/'seed').write_text('seed');git('add','seed');git('commit','-m','seed')
            for content in ['', 'wrong header\n', '\t'.join(w.COLS)+'\n']:
                log.write_text(content);git('add','ledger');git('commit','-m','empty fixture')
                with self.assertRaises(ValueError):t.audit(p,log,'HEAD')
    def test_audit_bound_and_uncommitted(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); log=p/'ledger';o=original()
            def git(*args):subprocess.run(['git','-C',d,*args],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            git('init');git('config','user.email','fixture@example.test');git('config','user.name','fixture')
            (p/'seed').write_text('seed');git('add','seed');git('commit','-m','seed')
            log.write_text('\t'.join(w.COLS)+'\n'+'\t'.join(o)+'\n');git('add','ledger');git('commit','-m','ledger')
            self.assertEqual(t.audit(p,log,'HEAD')['rows'][0]['state'],'UPPER-BOUND-CONSISTENT')
            data=t.payload(o,t.CLOSEOUT);data['touch_at']='2099-01-01T00:00:00Z';o[8]=t.CLOSEOUT+json.dumps(data)
            log.write_text('\t'.join(w.COLS)+'\n'+'\t'.join(o)+'\n')
            with self.assertRaises(ValueError):t.audit(p,log,'HEAD')
            git('add','ledger');git('commit','-m','future')
            self.assertEqual(t.audit(p,log,'HEAD')['rows'][0]['state'],'INVALID-FUTURE')

if __name__=='__main__': unittest.main()
