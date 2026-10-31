"""WQ-579 author counterexamples. All attacks use disposable local fixture origins."""
import os
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

import delivery
from pilot_files import Repo
from store import reader
import test_desk as fixtures


class ImportIsolationTests(unittest.TestCase):
    setUp = fixtures.DeskTests.setUp
    git = fixtures.DeskTests.git
    put = fixtures.DeskTests.put
    commit = fixtures.DeskTests.commit
    request = fixtures.DeskTests.request

    def send(self, event):
        return delivery.deliver(self.repo, event, local_events=lambda: self.store.responses()['events'])

    def real_helpers(self):
        for name in ['scripts/account_guard.py', 'scripts/claim_check.py', 'scripts/githooks/pre-commit', 'scripts/githooks/commit-msg']:
            self.put(name, (reader.ROOT / name).read_text())
        self.commit(publish=True)

    def shadow(self, name):
        marker = Path(self.tmp.name) / ('executed-' + name)
        code = ("from pathlib import Path\nimport sysconfig\n"
                + f"Path({str(marker)!r}).write_text('unreviewed code executed')\n"
                + f"source = Path(sysconfig.get_path('stdlib')) / {name + '.py'!r}\n"
                + "exec(compile(source.read_text(),str(source),'exec'),globals())\n")
        return marker, code

    def test_real_shared_hook_ignores_planted_hashlib_even_for_desk_commits(self):
        self.real_helpers()
        marker, code = self.shadow('hashlib')
        self.put('scripts/hashlib.py', code)
        # Positive control: the original ordinary Python invocation really executes this file.
        subprocess.run(['python3', 'scripts/account_guard.py'], cwd=self.root, check=True, capture_output=True)
        self.assertTrue(marker.exists())
        marker.rename(marker.with_suffix('.control'))
        self.commit(publish=True)  # The actual revised shared pre-commit uses -I.
        self.assertFalse(marker.exists())
        event = self.store.save(self.request())
        self.send(event)
        self.assertFalse(marker.exists())
        self.assertEqual(delivery.delivery_state(self.repo, event), 'delivered')

    def test_origin_only_shadow_is_not_materialized_or_executed(self):
        self.real_helpers()
        event = self.store.save(self.request())
        marker, code = self.shadow('hashlib')
        other = Path(self.tmp.name) / 'writer'
        subprocess.run(['git', 'clone', '-q', str(self.remote), str(other)], check=True)
        (other / 'scripts/hashlib.py').write_text(code)
        for args in [('config', 'user.name', 'Fixture'), ('config', 'user.email', 'fixture@example.invalid'),
                     ('add', 'scripts/hashlib.py'), ('commit', '-qm', 'Planted origin module'), ('push', '-q')]:
            subprocess.run(['git', *args], cwd=other, check=True, capture_output=True)
        observed = []
        original = delivery.publication_checkout
        def inspect(*args):
            work = original(*args)
            files = {p.relative_to(work.root).as_posix() for p in (work.root / 'scripts').rglob('*') if p.is_file()}
            observed.append(files)
            return work
        with patch.object(delivery, 'publication_checkout', side_effect=inspect):
            self.send(event)
        self.assertEqual(observed, [set(delivery.TRANSPORT_FILES)])
        self.assertFalse(marker.exists())

    def test_real_weekday_helper_ignores_shadow_argparse(self):
        self.real_helpers()
        marker, code = self.shadow('argparse')
        self.put('scripts/argparse.py', code)
        subprocess.run(['python3', 'scripts/claim_check.py', '--help'], cwd=self.root, check=True, capture_output=True)
        self.assertTrue(marker.exists())
        marker.rename(marker.with_suffix('.control'))
        self.commit(publish=True)
        before = self.repo.path('PROME/WILL_QUEUE.md').read_bytes()
        event = self.store.save(self.request())
        self.send(event)
        self.assertFalse(marker.exists())
        self.assertEqual(before, self.repo.path('PROME/WILL_QUEUE.md').read_bytes())

    def test_pythonpath_sitecustomize_does_not_run_in_helpers_or_stdin_hook(self):
        self.real_helpers()
        shadow = Path(self.tmp.name) / 'pythonpath'; shadow.mkdir()
        marker = shadow / 'executed'
        (shadow / 'sitecustomize.py').write_text(f"from pathlib import Path\nPath({str(marker)!r}).write_text('bad')\n")
        event = self.store.save(self.request())
        with patch.dict(os.environ, {'PYTHONPATH': str(shadow)}):
            self.send(event)
        self.assertFalse(marker.exists())

    def test_advisory_commit_refuses_without_undoing_owner_work(self):
        event = self.store.save(self.request()); original = delivery.run_advisory
        origin = self.git('rev-parse', 'origin/master')
        def change(repo, command, label):
            result = original(repo, command, label)
            if label == 'Weekday check':
                self.put('owner.txt', 'Concurrent saved owner work')
                self.commit()
            return result
        with patch.object(delivery, 'run_advisory', side_effect=change):
            with self.assertRaisesRegex(ValueError, 'HEAD or index changed'):
                self.send(event)
        self.assertEqual(self.repo.path('owner.txt').read_text(), 'Concurrent saved owner work')
        self.assertEqual(origin, self.git('rev-parse', 'origin/master'))
        self.assertFalse(delivery.published_packet(self.repo, event))

    def test_advisory_index_change_refuses_and_preserves_staging(self):
        event = self.store.save(self.request()); original = delivery.run_advisory
        def change(repo, command, label):
            result = original(repo, command, label)
            if label == 'Weekday check':
                self.put('owner.txt', 'Concurrent staged owner work'); self.git('add', 'owner.txt')
            return result
        with patch.object(delivery, 'run_advisory', side_effect=change):
            with self.assertRaisesRegex(ValueError, 'HEAD or index changed'):
                self.send(event)
        self.assertEqual(self.git('diff', '--cached', '--name-only').strip(), 'owner.txt')
        self.assertFalse(delivery.published_packet(self.repo, event))

    def test_real_git_objects_defeat_replace_ref_hiding_third_path(self):
        base = self.git('rev-parse', 'HEAD').strip()
        self.put('a', 'a'); self.put('b', 'b'); self.commit()
        good = self.git('rev-parse', 'HEAD').strip()
        self.put('third', 'third'); self.git('add', 'third')
        tree = self.git('write-tree').strip()
        bad = self.git('commit-tree', tree, '-p', base, '-m', 'Third path').strip()
        self.git('replace', bad, good)
        self.assertEqual(set(self.git('diff-tree', '--no-commit-id', '--name-only', '-r', bad).splitlines()), {'a', 'b'})
        with self.assertRaisesRegex(ValueError, 'two selected'):
            delivery.exact_pair_commit(self.repo, base, bad, {'a': 'a', 'b': 'b'}, check_worktree=False)
        with self.assertRaisesRegex(ValueError, 'replacement refs or tags'):
            delivery.check_private_checkout(self.repo)

    def test_safe_push_cannot_follow_injected_tag_and_preserves_existing_remote_tags(self):
        self.git('tag', '-am', 'Existing fixture tag', 'existing')
        self.git('push', '-q', 'origin', 'refs/tags/existing')
        event = self.store.save(self.request()); original = subprocess.run
        def inject(command, **kwargs):
            if command == ['bash', 'scripts/safe-push.sh']:
                # Inject after the private-ref refusal, directly at the push boundary.
                subprocess.check_call(['git', 'tag', '-am', 'Would follow without override', 'planted'], cwd=kwargs['cwd'])
                subprocess.check_call(['git', 'config', 'push.followTags', 'true'], cwd=kwargs['cwd'])
            return original(command, **kwargs)
        with patch('delivery.subprocess.run', side_effect=inject):
            self.send(event)
        refs = delivery.remote_refs(self.repo)
        self.assertIn('refs/tags/existing', refs)
        self.assertNotIn('refs/tags/planted', refs)

    def test_extra_remote_branch_cannot_report_exact_success(self):
        event = self.store.save(self.request()); original = subprocess.run
        def inject(command, **kwargs):
            result = original(command, **kwargs)
            if command == ['bash', 'scripts/safe-push.sh']:
                subprocess.check_call(['git', 'push', '-q', 'origin', 'HEAD:refs/heads/planted'], cwd=kwargs['cwd'])
            return result
        with patch('delivery.subprocess.run', side_effect=inject):
            with self.assertRaisesRegex(ValueError, 'remote references differ'):
                self.send(event)
        self.assertIn('refs/heads/planted', delivery.remote_refs(self.repo))
        self.assertEqual(delivery.delivery_state(self.repo, event), 'delivered')

    def test_remote_extra_commit_after_push_cannot_report_exact_success(self):
        event = self.store.save(self.request()); original = subprocess.run
        def inject(command, **kwargs):
            result = original(command, **kwargs)
            if command == ['bash', 'scripts/safe-push.sh']:
                root = kwargs['cwd']
                commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
                tree = subprocess.check_output(['git', 'rev-parse', 'HEAD^{tree}'], cwd=root, text=True).strip()
                extra = subprocess.check_output(['git', 'commit-tree', tree, '-p', commit, '-m', 'Extra after verified pair'], cwd=root, text=True).strip()
                subprocess.check_call(['git', 'push', '-q', 'origin', extra + ':master'], cwd=root)
            return result
        with patch('delivery.subprocess.run', side_effect=inject):
            with self.assertRaisesRegex(ValueError, 'remote references differ'):
                self.send(event)

    def test_post_fetch_verification_uses_shared_clone_and_names_existing_riders(self):
        self.put('owner.txt', 'Already committed owner work'); self.commit()
        rider = self.git('rev-parse', '--short', 'HEAD').strip()
        event = self.store.save(self.request()); original = delivery.exact_pair_commit; calls = []
        def observe(work, *args, **kwargs):
            calls.append((work.root, kwargs.get('check_worktree', True)))
            return original(work, *args, **kwargs)
        with patch.object(delivery, 'exact_pair_commit', side_effect=observe):
            result = self.send(event)
        self.assertEqual(calls[-1], (self.root, False))
        self.assertIn(rider, result['receipt'])
        self.assertEqual(len(result['riders']), 1)


if __name__ == '__main__':
    unittest.main()
