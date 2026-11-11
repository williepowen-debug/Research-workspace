"""WQ-639 authoring, versioned binding and concurrent-change counterexamples."""
import json
from pathlib import Path
import subprocess
import unittest
import io
from contextlib import redirect_stderr

import author_card
import delivery
from options import terms_hash
from pilot_files import record_block
from queue_store import QUEUE, QueueStore, check_current_snapshot, open_rows, validate_reply
from store import HERE, digest
from test_desk import DeskTests


class CardTests(unittest.TestCase):
    setUp = DeskTests.setUp
    git = DeskTests.git
    put = DeskTests.put
    commit = DeskTests.commit
    request = DeskTests.request
    install_options = DeskTests.install_options

    def spec(self):
        return dict(choices=[dict(id='A', label='Do it', meaning='One bounded task.', consequence='No ongoing job.'),
                             dict(id='B', label='Decline', meaning='Do not do it.', consequence='No change.')],
                    recommended_choice_id='A', context='Exact source explanation.', conditions=['Only after review.'])

    def install(self):
        result = author_card.prepare(self.root, '901', self.spec())
        before = self.git('status', '--porcelain')
        self.assertEqual(before, '')
        patch = Path(self.tmp.name) / 'card.patch'; patch.write_text(result['patch'])
        self.git('apply', '--check', str(patch)); self.git('apply', str(patch))
        self.commit(publish=True)
        self.display = self.store.display()
        self.assertEqual(self.display['snapshot']['kind'], 'decisions-queue-display/3')
        self.assertTrue(self.display['requires_confirmation'])
        self.path = result['source_path']
        return result

    def notes(self, *, publish=False, commit=False):
        old = self.repo.path(QUEUE).read_text()
        self.put(QUEUE, old.replace('Exact caveat', 'Owner progress updated; no change to decision terms'))
        if publish or commit:
            self.commit(publish=publish)

    def test_author_patch_preserves_other_rows_and_pins_conditions(self):
        before = open_rows(self.text)['902']['row']
        result = self.install()
        self.assertEqual(open_rows(self.repo.path(QUEUE).read_text())['902']['row'], before)
        self.assertEqual(self.display['unit']['proposal']['caveats'], ['Only after review.'])
        self.assertEqual(self.display['unit']['proposal']['context'], 'Exact source explanation.')
        self.assertEqual(result['queue_terms_sha256'], terms_hash(open_rows(self.repo.path(QUEUE).read_text())['901']))
        with self.assertRaisesRegex(ValueError, 'Existing source'):
            author_card.prepare(self.root, '901', self.spec())
        self.assertEqual(self.git('status', '--porcelain'), '')

    def test_notes_dirty_committed_published_preserve_saved_answer_and_provenance(self):
        self.install()
        snapshot = self.display['snapshot']
        self.notes()
        event = self.store.save(self.request(action='choose', choice_id='A'))
        self.assertEqual(event['display'], snapshot)  # unpublished notes are not laundered into history
        check_current_snapshot(self.repo, event['display'])
        self.commit()
        check_current_snapshot(self.repo, event['display'])
        self.git('push', '-q')
        check_current_snapshot(self.repo, event['display'])
        validate_reply(self.repo, event, '901')
        delivery.deliver(self.repo, event)
        self.assertEqual(delivery.delivery_state(self.repo, event), 'delivered')
        restored = QueueStore(Path(self.tmp.name)/'restored.sqlite3', self.repo, '901', True).display()
        self.assertEqual(restored['last'], event)
        self.assertTrue(restored['can_respond'])

    def test_question_date_recommendation_kind_and_hold_still_block(self):
        self.install()
        original = self.repo.path(QUEUE).read_text()
        variants = [('A: one task', 'A: two tasks'), ('2026-11-06', '2026-11-07'),
                    ('A with a condition', 'B instead'), ('| DECISION |', '| HANDS |'),
                    ('Exact caveat', '⛔ waits: owner; Exact caveat')]
        for old, new in variants:
            with self.subTest(change=old):
                self.put(QUEUE, original.replace(old, new, 1))
                with self.assertRaises(ValueError):
                    self.store.save(self.request(action='choose', choice_id='A'))
                self.assertEqual(self.store.responses()['events'], [])
        self.put(QUEUE, original)
        self.put(QUEUE, original.replace('A: one task', 'CLOSED A: one task'))
        with self.assertRaises(ValueError): check_current_snapshot(self.repo, self.display['snapshot'])

    def test_source_changes_and_pointer_changes_block(self):
        self.install()
        original = self.repo.path(self.path).read_text()
        record = record_block(original, 'decisions-options')
        for key, value in [('recommended_choice_id','B'), ('conditions',['New condition']),
                           ('context','New explanation'), ('choices', self.spec()['choices'][::-1]),
                           ('confirmation', dict(mode='chat', scope='security', reason='Different scope'))]:
            with self.subTest(key=key):
                changed = {**record, key:value}
                self.put(self.path, '```decisions-options\n'+json.dumps(changed)+'\n```\n')
                with self.assertRaises(ValueError): check_current_snapshot(self.repo,self.display['snapshot'])
                self.commit(publish=True)
                with self.assertRaises(ValueError): check_current_snapshot(self.repo,self.display['snapshot'])
                self.put(self.path, original); self.commit(publish=True)
        self.put(QUEUE,self.repo.path(QUEUE).read_text().replace(self.path,'PROME/proposals/different.md'))
        with self.assertRaises(ValueError): check_current_snapshot(self.repo,self.display['snapshot'])

    def test_legacy_notes_binding_and_history_unchanged(self):
        self.install_options()
        event = self.store.save(self.request(action='choose',choice_id='A'))
        self.notes()
        with self.assertRaises(ValueError): check_current_snapshot(self.repo,event['display'])
        self.commit(publish=True)
        with self.assertRaises(ValueError): check_current_snapshot(self.repo,event['display'])
        validate_reply(self.repo,event,'901')

    def test_forged_version_or_context_does_not_reclassify_old_answer(self):
        self.install()
        event = self.store.save(self.request(action='choose',choice_id='A'))
        for change in ('kind','context'):
            bad = json.loads(json.dumps(event))
            if change=='kind': bad['display']['kind']='decisions-queue-display/2'
            else: bad['display']['record']['units'][0]['proposal']['context']='Invented'
            bad['request']['display_hash']=digest(bad['display'])
            bad['sha256']=digest({k:v for k,v in bad.items() if k!='sha256'})
            with self.assertRaises(ValueError): validate_reply(self.repo,bad,'901')

    def test_stale_generated_patch_refuses_without_overwriting_owner(self):
        result=author_card.prepare(self.root,'901',self.spec())
        patch=Path(self.tmp.name)/'stale.patch';patch.write_text(result['patch'])
        self.notes(); before=self.repo.path(QUEUE).read_bytes()
        with self.assertRaises(subprocess.CalledProcessError): self.git('apply',str(patch))
        self.assertEqual(self.repo.path(QUEUE).read_bytes(),before)
        self.assertFalse(self.repo.path(result['source_path']).exists())

    def prepared_directory(self, result):
        directory = Path(self.tmp.name) / 'replacement'
        directory.mkdir()
        (directory/'card.patch').write_text(result['patch'])
        (directory/'manifest.json').write_text(json.dumps({k:v for k,v in result.items() if k not in ('source','patch')}))
        return directory

    def test_replacement_apply_checks_both_preimages_and_preserves_owner(self):
        path = self.install_options()
        queue, source = self.repo.path(QUEUE), self.repo.path(path)
        original_queue, original_source = queue.read_bytes(), source.read_bytes()
        result = author_card.prepare(self.root, '901', self.spec(), replace_source=True)
        directory = self.prepared_directory(result)
        variants = [original_queue.replace(b'A: one task', b'A: TEN tasks'),
                    original_queue.replace(b'A: one task', b'CLOSED A: one task'),
                    original_queue.replace(path.encode(), b'PROME/proposals/swapped.md'),
                    original_queue + b'Owner appended another row.\n']
        for changed in variants:
            queue.write_bytes(changed)
            with self.assertRaisesRegex(ValueError, 'Owner file changed'):
                author_card.apply_prepared(self.root, directory)
            self.assertEqual(queue.read_bytes(), changed)
            self.assertEqual(source.read_bytes(), original_source)
        queue.write_bytes(original_queue)
        for changed in (original_source.replace(b'```', b'Changed\n```', 1), original_source+b'Owner new condition.\n'):
            source.write_bytes(changed)
            with self.assertRaisesRegex(ValueError, 'Owner file changed'):
                author_card.apply_prepared(self.root, directory)
            self.assertEqual(source.read_bytes(), changed)
            self.assertEqual(queue.read_bytes(), original_queue)
        source.write_bytes(original_source)
        author_card.apply_prepared(self.root, directory)
        self.assertEqual(queue.read_bytes(), original_queue)
        self.assertEqual(source.read_text(), result['source'])
        self.assertEqual(self.git('diff','--cached','--name-only'), '')

    def test_replacement_raw_patch_also_guards_changed_target_row(self):
        path = self.install_options()
        result = author_card.prepare(self.root, '901', self.spec(), replace_source=True)
        directory = self.prepared_directory(result)
        source = self.repo.path(path).read_bytes()
        queue = self.repo.path(QUEUE)
        original = queue.read_bytes()
        for changed in (original.replace(b'A: one task', b'A: TEN tasks'),
                        original.replace(b'A: one task', b'CLOSED A: one task'),
                        original.replace(path.encode(), b'PROME/proposals/other.md')):
            queue.write_bytes(changed)
            with self.assertRaises(subprocess.CalledProcessError): self.git('apply', str(directory/'card.patch'))
            self.assertEqual(queue.read_bytes(),changed)
            self.assertEqual(self.repo.path(path).read_bytes(),source)

    def test_apply_cli_and_patch_integrity(self):
        result = author_card.prepare(self.root, '901', self.spec())
        directory = self.prepared_directory(result)
        original = self.repo.path(QUEUE).read_bytes()
        patch = directory/'card.patch'
        patch.write_text(result['patch']+'\n')
        with self.assertRaisesRegex(ValueError, 'patch changed'):
            author_card.apply_prepared(self.root, directory)
        self.assertEqual(self.repo.path(QUEUE).read_bytes(), original)
        self.assertFalse(self.repo.path(result['source_path']).exists())
        patch.write_text(result['patch'])
        from contextlib import redirect_stdout
        with redirect_stdout(io.StringIO()):
            self.assertEqual(author_card.main(['--root',str(self.root),'--apply',str(directory)]),0)
        self.assertEqual(self.repo.path(result['source_path']).read_text(),result['source'])

    def test_invalid_author_inputs_never_touch_sources(self):
        original=self.repo.path(QUEUE).read_bytes()
        for wq in ('902','903','../901'):
            with self.assertRaises(ValueError): author_card.prepare(self.root,wq,self.spec())
        for change in [dict(recommended_choice_id='C'),dict(conditions='none'),dict(context=''),dict(choices=[]),dict(extra='x')]:
            with self.assertRaises(ValueError): author_card.prepare(self.root,'901',{**self.spec(),**change})
        self.assertEqual(self.repo.path(QUEUE).read_bytes(),original)
        self.assertFalse(self.repo.path('PROME/proposals/wq901-app-options.md').exists())

    def test_cli_prepares_artifacts_without_queue_or_index_writes(self):
        import io
        from contextlib import redirect_stdout
        source=Path(self.tmp.name)/'input.json';source.write_text(json.dumps(self.spec()))
        output=Path(self.tmp.name)/'prepared'
        args=['--root',str(self.root),'--wq','901','--input',str(source),'--output',str(output)]
        with redirect_stdout(io.StringIO()): self.assertEqual(author_card.main(args),0)
        self.assertTrue((output/'card.patch').is_file())
        self.assertEqual(self.git('status','--porcelain'),'')
        self.assertEqual(self.git('diff','--cached','--name-only'),'')
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit): author_card.main(args)

    def test_real_preserved_producer_can_be_explicitly_migrated(self):
        fixture=json.loads((HERE/'fixtures/wq639-real-producer.json').read_text())
        row=fixture['row']
        self.put(QUEUE,'## OPEN\n\n| # | Item | Type | Needed by | Since | PROME rec | Notes |\n|---|---|---|---|---|---|---|\n'+row+'\n\n## RECENTLY DONE\n')
        parsed=open_rows(self.repo.path(QUEUE).read_text())['639']
        from options import pointer_for
        self.put(pointer_for(parsed),fixture['options_source'])
        self.commit(publish=True)
        producer=record_block(fixture['options_source'],'decisions-options')
        spec=dict(choices=producer['choices'],recommended_choice_id=producer.get('recommended_choice_id','A'),
                  context=parsed['cells'][6],conditions=['Every answer still requires matching chat confirmation.'])
        result=author_card.prepare(self.root,'639',spec,replace_source=True)
        patch=Path(self.tmp.name)/'real.patch';patch.write_text(result['patch'])
        self.git('apply',str(patch));self.commit(publish=True)
        store=QueueStore(Path(self.tmp.name)/'real.sqlite3',self.repo,'639',True)
        card=store.display()
        self.assertEqual(card['unit']['proposal']['choices'],producer['choices'])
        self.assertEqual(card['snapshot']['kind'],'decisions-queue-display/3')
        self.assertTrue(card['requires_confirmation'])

if __name__ == '__main__': unittest.main()
