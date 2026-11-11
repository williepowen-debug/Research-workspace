import sys, tempfile, unittest, json, subprocess
from pathlib import Path
BASE=Path('/tmp/cato-wq639-independent-review')
tempfile.tempdir=str(BASE)
sys.path.insert(0,str(BASE/'tree/AGENTS/CATO/prototypes/decisions/mvp'))
from test_wq639 import CardTests
import author_card, delivery
from queue_store import QUEUE, current_source, check_current_snapshot, validate_reply, QueueStore

class Independent(unittest.TestCase):
    def setUp(self):
        self.f=CardTests(); self.f.setUp();self.addCleanup(self.f.doCleanups)
    def test_migration_patch_after_question_change(self):
        f=self.f; path=f.install_options()
        prepared=author_card.prepare(f.root,'901',f.spec(),replace_source=True)
        p=BASE/'stale-replacement.patch'; p.write_text(prepared['patch'])
        changed=f.repo.path(QUEUE).read_text().replace('A: one task','A: TEN tasks')
        f.put(QUEUE,changed)
        result=subprocess.run(['git','apply',str(p)],cwd=f.root,capture_output=True,text=True)
        print('STALE_REPLACEMENT_APPLY_EXIT',result.returncode,flush=True)
        self.assertEqual(result.returncode,0) # proves missing queue precondition
        self.assertEqual(f.repo.path(QUEUE).read_text(),changed)
        f.commit(publish=True)
        with self.assertRaisesRegex(ValueError,'bind this exact queue row'): current_source(f.repo,'901')
    def test_replacement_after_closed_row(self):
        f=self.f; f.install_options()
        prepared=author_card.prepare(f.root,'901',f.spec(),replace_source=True)
        p=BASE/'closed-replacement.patch';p.write_text(prepared['patch'])
        f.put(QUEUE,f.repo.path(QUEUE).read_text().replace('A: one task','CLOSED A: one task'))
        result=subprocess.run(['git','apply',str(p)],cwd=f.root,capture_output=True,text=True)
        print('CLOSED_REPLACEMENT_APPLY_EXIT',result.returncode,flush=True)
        self.assertEqual(result.returncode,0)
        f.commit(publish=True)
        with self.assertRaises(ValueError):current_source(f.repo,'901')
    def test_publish_only_source_then_only_queue(self):
        f=self.f; result=author_card.prepare(f.root,'901',f.spec())
        f.put(result['source_path'],result['source']); f.commit(publish=True)
        self.assertEqual(current_source(f.repo,'901')['kind'],'decisions-queue-display/1')
        # Source-first does not activate unseen options. Unpublished queue pointer refuses.
        f.put(QUEUE,f.repo.path(QUEUE).read_text().replace('Exact caveat |','Exact caveat <!-- decisions-options: '+result['source_path']+' --> |'))
        with self.assertRaises(ValueError):current_source(f.repo,'901')
    def test_notes_with_binding_lookalike_and_hold(self):
        f=self.f; f.install(); e=f.store.save(f.request(action='choose',choice_id='A'))
        original=f.repo.path(QUEUE).read_text()
        for notes in ['**⛔ waits: reviewer**; Exact caveat','Exact caveat decisions-options: bogus']:
            f.put(QUEUE,original.replace('Exact caveat',notes))
            with self.assertRaises(ValueError): check_current_snapshot(f.repo,e['display'])
        f.put(QUEUE,original.replace('Exact caveat','Log only: the prior item mentioned ⛔ waits: reviewer'))
        check_current_snapshot(f.repo,e['display']) # canonical declaration is Notes-prefix only
    def test_disjoint_notes_edit_roundtrip_and_closed_history(self):
        f=self.f;f.install(); e=f.store.save(f.request(action='choose',choice_id='B',note='Not until independent review.'))
        old=e['display']['queue_row']
        f.put(QUEUE,f.repo.path(QUEUE).read_text().replace('Exact caveat','Progress complete; next owner touch tomorrow.'))
        f.commit(publish=True); delivery.deliver(f.repo,e)
        restored=QueueStore(Path(f.tmp.name)/'independent-restore.sqlite',f.repo,'901',True).display()
        self.assertEqual(restored['last']['display']['queue_row'],old)
        self.assertEqual(restored['last']['selected_choice']['id'],'B')
        f.put(QUEUE,f.repo.path(QUEUE).read_text().replace('A: one task','CLOSED A: one task'));f.commit(publish=True)
        validate_reply(f.repo,e,'901')
        with self.assertRaises(ValueError):check_current_snapshot(f.repo,e['display'])
    def test_old_pointer_restored_in_worktree_cannot_hide_head_swap(self):
        f=self.f;f.install(); snap=f.display['snapshot'];original=f.repo.path(QUEUE).read_text()
        f.put(QUEUE,original.replace(f.path,'PROME/proposals/swapped.md'));f.commit()
        f.put(QUEUE,original)
        with self.assertRaises(ValueError):check_current_snapshot(f.repo,snap)
    def test_material_notes_are_not_semantically_inferred(self):
        f=self.f;f.install();snap=f.display['snapshot']
        f.put(QUEUE,f.repo.path(QUEUE).read_text().replace('Exact caveat','New restriction: do not proceed until Friday'))
        check_current_snapshot(f.repo,snap)
        self.assertNotIn('Friday',str(current_source(f.repo,'901')['record']))
        # Intentional /3 contract; owner must put material restrictions in bound fields.

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Independent))
    raise SystemExit(not result.wasSuccessful())
