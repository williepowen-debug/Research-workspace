"""WQ-570 targeted adverse tests. Local bare origins only; no real answers."""
import subprocess
import time
from pathlib import Path
import unittest
from unittest.mock import patch
import delivery
from pilot_files import Repo
import test_desk as fixtures

class FocusedTests(unittest.TestCase):
    setUp=fixtures.DeskTests.setUp
    git=fixtures.DeskTests.git
    put=fixtures.DeskTests.put
    commit=fixtures.DeskTests.commit
    request=fixtures.DeskTests.request

    def send(self,event):
        return delivery.deliver(self.repo,event,local_events=lambda:self.store.responses()['events'])

    def test_extra_private_commit_is_refused_and_cannot_ride_shared_push(self):
        event=self.store.save(self.request()); original=Repo.git
        before=self.git('rev-parse','HEAD')
        def inject(work,*args):
            result=original(work,*args)
            if args[0]=='commit' and work.root!=self.root:
                (work.root/'scripts/extra.txt').write_text('Unexpected publication')
                original(work,'add','--sparse','scripts/extra.txt')
                original(work,'commit','-qm','Extra commit','--','scripts/extra.txt')
            return result
        with patch.object(Repo,'git',inject):
            with self.assertRaisesRegex(ValueError,'exactly one'): self.send(event)
        self.assertEqual(before,self.git('rev-parse','HEAD'))
        self.put('foreign.txt','Owner work'); self.commit(publish=True)
        self.assertFalse(delivery.published_packet(self.repo,event))
        with self.assertRaises(ValueError): self.repo.read('scripts/extra.txt','origin/master')

    def test_same_commit_with_third_path_is_not_an_exact_pair(self):
        base=self.git('rev-parse','HEAD').strip()
        self.put('a','a'); self.put('b','b'); self.put('extra','extra'); self.commit()
        commit=self.git('rev-parse','HEAD').strip()
        with self.assertRaisesRegex(ValueError,'two selected'):
            delivery.exact_pair_commit(self.repo,base,commit,{'a':'a','b':'b'})

    def test_unpinned_shared_hook_refused_before_it_runs(self):
        event=self.store.save(self.request())
        self.put('scripts/githooks/post-commit','#!/bin/sh\ntouch unexpected-hook\n').chmod(0o755)
        with self.assertRaisesRegex(ValueError,'Unreviewed'): self.send(event)
        self.assertFalse(self.repo.path('unexpected-hook').exists())
        self.assertFalse(delivery.published_packet(self.repo,event))

    def test_origin_only_unpinned_hook_refused_before_private_execution(self):
        event=self.store.save(self.request()); before=self.git('rev-parse','HEAD')
        other=Path(self.tmp.name)/'other'
        subprocess.run(['git','clone','-q',str(self.remote),str(other)],check=True)
        for key,value in [('user.name','Fixture'),('user.email','fixture@example.invalid')]:
            subprocess.run(['git','config',key,value],cwd=other,check=True)
        hook=other/'scripts/githooks/post-commit'; hook.write_text('#!/bin/sh\necho bad > scripts/extra.txt\ngit add scripts/extra.txt\n'); hook.chmod(0o755)
        for args in [('add','scripts/githooks/post-commit'),('commit','-qm','Remote extra hook'),('push','-q')]:
            subprocess.run(['git',*args],cwd=other,check=True)
        with self.assertRaisesRegex(ValueError,'Unreviewed'): self.send(event)
        self.assertEqual(before,self.git('rev-parse','HEAD'))
        self.assertFalse(delivery.published_packet(self.repo,event))
        with self.assertRaises(ValueError): self.repo.read('scripts/extra.txt','origin/master')

    def test_dirty_advisory_refused_without_running_or_changing_question(self):
        event=self.store.save(self.request()); before=self.repo.path('PROME/WILL_QUEUE.md').read_text()
        self.put('scripts/claim_check.py',"from pathlib import Path\nPath('PROME/WILL_QUEUE.md').write_text('Wrong answer')\n")
        with self.assertRaisesRegex(ValueError,'Publication safeguard'): self.send(event)
        self.assertEqual(before,self.repo.path('PROME/WILL_QUEUE.md').read_text())
        self.assertFalse(delivery.published_packet(self.repo,event))

    def test_late_real_push_reports_unknown_then_sync_finds_exact_pair(self):
        event=self.store.save(self.request()); run=subprocess.run
        hook=self.remote/'hooks/pre-receive'; hook.write_text('#!/bin/sh\nsleep 1\n'); hook.chmod(0o755)
        def short_timeout(args,**kwargs):
            if args==['bash','scripts/safe-push.sh']: kwargs['timeout']=0.15
            return run(args,**kwargs)
        with patch('delivery.subprocess.run',side_effect=short_timeout):
            with self.assertRaisesRegex(ValueError,'publication status unknown'): self.send(event)
        time.sleep(1.3)
        self.git('fetch','-q','origin')
        self.assertEqual(delivery.delivery_state(self.repo,event),'delivered')
        before=self.git('rev-parse','origin/master')
        self.send(event)
        self.assertEqual(before,self.git('rev-parse','origin/master'))

    def test_busy_checkout_message_names_exact_recovery_state(self):
        event=self.store.save(self.request()); before=self.git('rev-parse','HEAD')
        self.put('foreign.txt','Other desk'); self.git('add','foreign.txt')
        result=self.send(event)
        self.assertIn('0 ahead / 1 behind',result['message'])
        self.assertIn('After owners save their work, use Sync',result['message'])
        self.assertEqual(before,self.git('rev-parse','HEAD'))
        self.assertEqual(self.git('diff','--cached','--name-only').strip(),'foreign.txt')

    def test_concurrent_shared_commit_names_diverged_recovery_without_rebase(self):
        event=self.store.save(self.request()); run=subprocess.run
        def advance(args,**kwargs):
            if args==['bash','scripts/safe-push.sh']:
                self.put('owner.txt','Concurrent owner'); self.commit()
            return run(args,**kwargs)
        with patch('delivery.subprocess.run',side_effect=advance): result=self.send(event)
        self.assertIn('1 ahead / 1 behind',result['message'])
        self.assertIn('root Git recovery procedure',result['message'])
        self.assertEqual(self.repo.path('owner.txt').read_text(),'Concurrent owner')

if __name__=='__main__': unittest.main()
