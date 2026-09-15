import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from closeout_check import inspect, START, END

class CloseoutCheck(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.repo=Path(self.tmp.name); self.base=self.repo/'AGENTS/WALTER'; self.base.mkdir(parents=True)
        self.git('init','-q'); self.git('config','user.email','test@example.invalid');self.git('config','user.name','Test')
        self.handoff='AGENTS/BRENT/inbox/WALTER/SIG-W-20260915-001.md'
        self.put(self.handoff,'packet'); self.git('add','.');self.git('commit','-qm','packet')
        self.commit=self.git('rev-parse','HEAD');self.git('update-ref','refs/remotes/origin/master',self.commit)
        self.put('AGENTS/WALTER/STATUS.md','## BOTTOM LINE\nSee LAST_COMPLETION.md for obligations.\n')
        self.put('AGENTS/WALTER/routed/delivery_log.tsv','signal_id\trecipient\thandoff_path\twritten_state\nSIG-W-20260915-001\tBRENT\t'+self.handoff+'\tdelivered\n')
        self.put('owner.md','Owner evidence, not inferred completion')
        self.receipt={'schema':1,'as_of':'2026-01-01T00:00:00Z','next_review':'2026-09-16',
          'publication':[{'commit':self.commit,'state':'published'}],
          'delivery':{'signal_date':'20260915','total':1,'delivered':1},
          'owner_review':{'scope':'manual evidence review; no automatic completion',
          'evidence':[{'path':'owner.md','sha256':hashlib.sha256((self.repo/'owner.md').read_bytes()).hexdigest()}]}}
        self.save()
    def git(self,*args):return subprocess.check_output(['git',*args],cwd=self.repo,text=True).strip()
    def put(self,path,text):
        p=self.repo/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
    def save(self):self.put('AGENTS/WALTER/LAST_COMPLETION.md','## FOLLOW-UP\nReview owners.\n## OPEN DESIGN DECISIONS\nHeld.\n## WILL_NEEDS\nBasis.\n'+START+json.dumps(self.receipt)+END)
    def test_valid(self): self.assertEqual(inspect(self.repo)[0],[])
    def test_stale_pending_commit(self):
        self.receipt['publication'][0]['state']='pending';self.save()
        self.assertTrue(any('origin proves published' in x for x in inspect(self.repo)[0]))
    def test_unpublished_claim(self):
        self.put('later','local');self.git('add','later');self.git('commit','-qm','local')
        self.receipt['publication'][0]['commit']=self.git('rev-parse','HEAD');self.save()
        self.assertTrue(inspect(self.repo)[0])
    def test_stale_status_examples(self):
        for line in ['Five BRENT handoffs remain held during active owner edits.',
                     'Implementation0951f361e is local; five BRENT recipient-path commits await a safe write window.',
                     'All29 handoffs are delivered.', 'Repairs are complete and on origin.']:
            self.put('AGENTS/WALTER/STATUS.md','See LAST_COMPLETION.md\n'+line)
            self.assertTrue(inspect(self.repo)[0],line)
    def test_market_publication_is_not_git_claim(self):
        self.put('AGENTS/WALTER/STATUS.md','See LAST_COMPLETION.md\nNo9/15 published bar. Observation dated9/14.\n')
        self.assertEqual(inspect(self.repo)[0],[])
    def test_wrong_delivery_count(self):
        self.receipt['delivery']['delivered']=0;self.save();self.assertTrue(inspect(self.repo)[0])
    def test_pending_ledger_on_origin(self):
        p=self.base/'routed/delivery_log.tsv';p.write_text(p.read_text().replace('delivered','written_not_delivered_pending_push'))
        self.assertTrue(inspect(self.repo)[0])
    def test_missing_receipt(self):
        self.put('AGENTS/WALTER/LAST_COMPLETION.md','none')
        with self.assertRaises(ValueError):inspect(self.repo)
    def test_changed_owner_evidence(self):
        self.put('owner.md','New disposition');self.assertTrue(inspect(self.repo)[0])
    def test_history_proves_delivery_without_consumption(self):
        self.git('rm',self.handoff);self.git('commit','-qm','filed');self.git('update-ref','refs/remotes/origin/master',self.git('rev-parse','HEAD'))
        self.assertEqual(inspect(self.repo)[0],[])
    def test_missing_origin(self):
        self.git('update-ref','-d','refs/remotes/origin/master')
        with self.assertRaises(ValueError):inspect(self.repo)

if __name__=='__main__':unittest.main()
