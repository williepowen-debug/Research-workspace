"""Offline regression tests for continuation, review/mark binding and receipts."""
import io
import atexit
import json
import os
from pathlib import Path
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

_ISOLATED = tempfile.TemporaryDirectory(prefix='xbm_workflow_import_')
atexit.register(_ISOLATED.cleanup)
if 'x_bookmarks_scan' not in sys.modules:
    os.environ['WALTER_X_ENV'] = str(Path(_ISOLATED.name) / '.env')
    os.environ['WALTER_X_SEEN'] = str(Path(_ISOLATED.name) / 'seen.json')
sys.path.insert(0, str(Path(__file__).resolve().parent))
import x_bookmarks_scan as x
w = x.workflow


class HTTPError(Exception):
    def __init__(self, status):
        self.response = types.SimpleNamespace(status_code=status)


class Workflow(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix='xbm_workflow_')
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for name, value in [('SEEN', self.root/'seen.json'), ('ENV_PATH', self.root/'.env')]:
            mock = patch.object(x, name, value)
            mock.start()
            self.addCleanup(mock.stop)
        request_mock = patch.object(x, '_require_requests', return_value=types.SimpleNamespace(HTTPError=HTTPError))
        request_mock.start()
        self.addCleanup(request_mock.stop)
        self.provider = patch.object(x, 'api_get_bookmarks', side_effect=self.page)
        self.provider.start()
        self.addCleanup(self.provider.stop)
        x.ENV_PATH.write_text('X_BOOKMARK_ACCESS_TOKEN=FAKE\nX_USER_ID=fixture\nX_CLIENT_ID=fixture\nX_BOOKMARK_REFRESH_TOKEN=FAKE_REFRESH\n')
        self.items, self.calls = [], []
        self.make_items(1)

    def make_items(self, count):
        self.items = [{'id': str(i), 'author_id': 'fixture', 'text': 'SYNTHETIC_BODY_ONLY_STDOUT'}
                      for i in range(count)]

    def page(self, user, token, cursor=None):
        offset = int(cursor or 0)
        self.calls.append(offset)
        stop = offset + x.PAGE_SIZE
        return self.items[offset:stop], {'fixture': 'fixture'}, {}, (
            {'next_token': str(stop)} if stop < len(self.items) else {})

    def main(self, *args):
        output = io.StringIO()
        with redirect_stdout(output):
            result = x.main(list(args))
        return result, output.getvalue()

    def review(self, read_state='fully_read', disposition='DISPATCH', **updates):
        staged = w.read_json(x._pending_path())
        path = self.root / f'review-{len(list(self.root.glob("review-*.json")))}.json'
        self.main('--review-template', str(path))
        value = json.loads(path.read_text())
        for item in value['items']:
            item.update(disposition=disposition, read_state=read_state, **updates)
        path.write_text(json.dumps(value))
        self.assertEqual(value['staged_at'], staged['staged_at'])
        return path

    def mark(self, **updates):
        return self.main('--mark', '--review', str(self.review(**updates)))

    def test_501_resumes_after_actual_review_mark(self):
        self.make_items(501)
        self.main()
        self.assertEqual(len(x.load_pending()), 500)
        self.assertFalse(w.path_for(x.SEEN, 'scan_token').exists())
        self.mark()
        self.assertFalse(x.load_seen()['scan_complete'])
        before = len(self.calls)
        self.main()
        self.assertEqual(self.calls[before:], [500])
        self.assertEqual(x.load_pending(), ['500'])
        self.mark()
        self.assertEqual(len(x.load_seen()['consumed']), 501)
        receipt = w.read_json(w.path_for(x.SEEN, 'receipt'))
        self.assertFalse(receipt['scan']['head_checked_this_run'])
        self.assertFalse(receipt['scan']['incomplete'])
        _, output = self.main('--receipt')
        self.assertIn('newer bookmarks were not checked', output)

    def test_damaged_501_stage_cannot_skip_unreviewed_id(self):
        self.make_items(501)
        self.main()
        staged = w.read_json(x._pending_path())
        staged['ids'].remove('499')
        w.atomic_json(x._pending_path(), staged)
        # A fresh, otherwise valid review must not authorize the original cursor.
        path = self.review()
        before = {p: p.read_bytes() for p in self.root.glob('*.json')}
        with self.assertRaisesRegex(SystemExit, 'binding'):
            self.main('--mark', '--review', str(path))
        self.assertEqual({p: p.read_bytes() for p in before}, before)
        self.assertEqual(x.load_seen()['consumed'], [])
        self.assertFalse(w.path_for(x.SEEN, 'scan_token').exists())
        # A safe fresh scan recovers the missing ID and then the 501st item.
        self.main()
        self.assertIn('499', x.load_pending())
        self.mark()
        self.main()
        self.mark()
        self.assertEqual(set(x.load_seen()['consumed']), {str(i) for i in range(501)})

    def test_new_stage_missing_binding_fields_refuses_before_writes(self):
        self.main()
        original = w.read_json(x._pending_path())
        path = self.review()
        for field in ['checkpoint_hash', 'stage_id', 'stage_schema', 'review_required']:
            with self.subTest(field=field):
                damaged = dict(original)
                damaged.pop(field, None)
                w.atomic_json(x._pending_path(), damaged)
                with self.assertRaisesRegex(SystemExit, 'binding'):
                    self.main('--mark', '--review', str(path))
                self.assertEqual(x.load_seen()['consumed'], [])
                self.assertFalse(w.path_for(x.SEEN, 'scan_token').exists())

    def test_stage_identity_survives_timestamp_collision(self):
        with patch('time.time', return_value=__import__('time').time()):
            self.main()
            path = self.review()
            self.main()  # identical IDs AND timestamp, but a different scan
            with self.assertRaisesRegex(SystemExit, 'does not match'):
                self.main('--mark', '--review', str(path))
        self.assertEqual(x.load_seen()['consumed'], [])

    def test_old_unbound_continuation_requires_rescan(self):
        self.main()
        staged = w.read_json(x._pending_path())
        checkpoint = w.proposed_checkpoint(x.SEEN, staged)
        proposal = w.path_for(x.SEEN, 'next_token')
        w.atomic_json(proposal, checkpoint)  # October19's unbound format
        old = {'ids': staged['ids'], 'staged_at': staged['staged_at'],
               'review_required': True, 'scan': staged['scan'],
               'checkpoint_hash': __import__('hashlib').sha256(proposal.read_bytes()).hexdigest()}
        w.atomic_json(x._pending_path(), old)
        with self.assertRaisesRegex(SystemExit, 'binding'):
            self.main('--mark')
        self.assertEqual(x.load_seen()['consumed'], [])

    def test_timestamped_legacy_stage_without_continuation_still_marks(self):
        x.save_pending(['old'])
        self.main('--mark')
        self.assertEqual(x.load_seen()['consumed'], ['old'])
        self.assertFalse(w.path_for(x.SEEN, 'scan_token').exists())

    def test_all_modern_metadata_lost_cannot_downgrade_to_legacy(self):
        self.make_items(501)
        self.main()
        staged = w.read_json(x._pending_path())
        w.atomic_json(x._pending_path(), {key: staged[key] for key in ('ids', 'staged_at')})
        before = {p: p.read_bytes() for p in self.root.glob('*.json')}
        with self.assertRaisesRegex(SystemExit, 'binding'):
            self.main('--mark')
        self.assertEqual({p: p.read_bytes() for p in before}, before)
        self.assertEqual(x.load_seen()['consumed'], [])

    def test_legacy_shape_with_active_cursor_and_lost_proposal_refuses(self):
        self.make_items(1001)
        self.main()
        self.mark()
        self.main()
        staged = w.read_json(x._pending_path())
        w.atomic_json(x._pending_path(), {key: staged[key] for key in ('ids', 'staged_at')})
        w.path_for(x.SEEN, 'next_token').unlink()
        with self.assertRaisesRegex(SystemExit, 'binding'):
            self.main('--mark')
        self.assertEqual(len(x.load_seen()['consumed']), 500)

    def test_empty_damaged_stage_refuses_instead_of_claiming_no_work(self):
        self.main()
        staged = w.read_json(x._pending_path())
        w.atomic_json(x._pending_path(), dict(staged, ids=[]))
        with self.assertRaisesRegex(SystemExit, 'binding'):
            self.main('--mark')
        self.assertEqual(x.load_seen()['consumed'], [])

    def test_proposal_from_another_stage_cannot_be_rebound_by_hash(self):
        self.main()
        old_proposal = w.path_for(x.SEEN, 'next_token').read_bytes()
        self.main()  # same IDs but a different stage identity
        staged = w.read_json(x._pending_path())
        proposal = w.path_for(x.SEEN, 'next_token')
        proposal.write_bytes(old_proposal)
        staged['checkpoint_hash'] = __import__('hashlib').sha256(old_proposal).hexdigest()
        w.atomic_json(x._pending_path(), staged)
        with self.assertRaisesRegex(SystemExit, 'binding'):
            self.main('--mark', '--review', str(self.review()))
        self.assertEqual(x.load_seen()['consumed'], [])

    def test_mark_retry_after_cursor_write_and_receipt_failure(self):
        self.make_items(501)
        self.main()
        path = self.review()
        with patch.object(w, 'mark_receipt', side_effect=OSError('simulated receipt failure')):
            with self.assertRaises(OSError):
                self.main('--mark', '--review', str(path))
        self.assertEqual(len(x.load_seen()['consumed']), 500)
        self.assertEqual(w.read_json(w.path_for(x.SEEN, 'scan_token'))['next_token'], '500')
        self.main('--mark', '--review', str(path))
        self.main()
        self.assertEqual(x.load_pending(), ['500'])

    def test_1001_three_scans_never_exceed_request_budget(self):
        self.make_items(1001)
        for expected in [500, 500, 1]:
            before = len(self.calls)
            self.main()
            self.assertEqual(len(x.load_pending()), expected)
            self.assertLessEqual(len(self.calls)-before, 10)
            self.mark()
        self.assertEqual(len(x.load_seen()['consumed']), 1001)

    def test_normal_no_cap_and_seen_fast_path(self):
        self.make_items(51)
        self.main()
        self.mark()
        before = len(self.calls)
        _, output = self.main()
        self.assertEqual(self.calls[before:], [0])
        self.assertIn('No new items', output)
        self.assertTrue(x.load_seen()['scan_complete'])

    def test_legacy_seen_prefix_gets_full_audit(self):
        self.make_items(501)
        x.save_seen({'consumed': [str(i) for i in range(500)], 'pilot_start_id': None})
        self.main()  # first 500 all seen; still must continue to the unseen tail
        self.assertFalse(x.load_seen()['scan_complete'])
        self.assertEqual(x.load_pending(), [])
        self.main()
        self.assertEqual(x.load_pending(), ['500'])

    def test_lost_local_cursor_restarts_without_hiding_tail(self):
        self.make_items(501)
        self.main()
        self.mark()
        cursor = w.path_for(x.SEEN, 'scan_token')
        cursor.rename(self.root/'lost-cursor.json')
        self.main()
        self.assertEqual(x.load_pending(), [])
        self.assertFalse(x.load_seen()['scan_complete'])
        self.main()
        self.assertEqual(x.load_pending(), ['500'])

    def test_rejected_cursor_fails_loud_then_recovers(self):
        self.make_items(501)
        self.main()
        self.mark()
        with patch.object(x, 'api_get_bookmarks', side_effect=HTTPError(400)):
            with self.assertRaisesRegex(SystemExit, 'INCOMPLETE'):
                self.main()
        self.assertEqual(len(x.load_seen()['consumed']), 500)
        self.assertIsNone(w.read_json(w.path_for(x.SEEN, 'scan_token'))['next_token'])
        self.main()  # full restart cannot stop at newly marked prefix
        self.main()
        self.assertEqual(x.load_pending(), ['500'])

    def test_new_head_item_is_checked_after_resumed_tail(self):
        self.make_items(501)
        self.main()
        self.mark()
        self.items.insert(0, {'id': 'new-head', 'author_id': 'fixture', 'text': 'new'})
        self.main()
        self.mark()
        self.main()
        self.assertEqual(x.load_pending(), ['new-head'])
        self.mark()
        self.assertIn('new-head', x.load_seen()['consumed'])
        self.assertIn('500', x.load_seen()['consumed'])

    def test_unmarked_scan_repeats_instead_of_advancing_cursor(self):
        self.make_items(501)
        self.main()
        first = x.load_pending()
        self.main()  # no mark/commit in between
        self.assertEqual(x.load_pending(), first)
        self.assertEqual(x.load_seen()['consumed'], [])

    def test_mark_interruption_after_seen_write_is_recoverable(self):
        self.make_items(501)
        self.main()
        path = self.review()
        with patch.object(w, 'commit_checkpoint', side_effect=OSError('simulated crash')):
            with self.assertRaises(OSError):
                self.main('--mark', '--review', str(path))
        self.assertEqual(len(x.load_seen()['consumed']), 500)
        self.main('--mark', '--review', str(path))  # idempotent retry advances safely
        self.main()
        self.assertEqual(x.load_pending(), ['500'])

    def test_missing_proposal_fails_before_marking(self):
        self.main()
        path = self.review()
        w.path_for(x.SEEN, 'next_token').rename(self.root/'lost-next.json')
        with self.assertRaisesRegex(SystemExit, 'missing/changed'):
            self.main('--mark', '--review', str(path))
        self.assertEqual(x.load_seen()['consumed'], [])

    def test_mark_requires_review_and_exact_stage(self):
        self.main()
        result, output = self.main('--mark')
        self.assertEqual(result, 1)
        self.assertIn('REFUSING', output)
        path = self.review()
        value = json.loads(path.read_text())
        value['items'][0]['id'] = 'different'
        path.write_text(json.dumps(value))
        with self.assertRaisesRegex(SystemExit, 'exactly match'):
            self.main('--mark', '--review', str(path))
        self.assertEqual(x.load_seen()['consumed'], [])

    def test_review_binding_rejects_new_scan_same_ids(self):
        self.main()
        path = self.review()
        self.main()
        with self.assertRaisesRegex(SystemExit, 'does not match'):
            self.main('--mark', '--review', str(path))

    def test_partial_material_requires_followup_or_selective_request(self):
        self.main()
        path = self.review(read_state='partly_read')
        with self.assertRaisesRegex(SystemExit, 'follow-up'):
            self.main('--mark', '--review', str(path))
        self.assertEqual(x.load_seen()['consumed'], [])
        path = self.review(read_state='partly_read', ask_user='Please share table 2; it contains the debt maturity needed for this credit lead.')
        self.main('--mark', '--review', str(path))
        _, output = self.main('--receipt')
        self.assertIn('partly read 1', output)
        self.assertIn('table 2', output)
        self.assertNotIn('Fully read 1', output)

    def test_incomplete_review_template_cannot_mark(self):
        self.main()
        path = self.root/'unfilled.json'
        self.main('--review-template', str(path))
        with self.assertRaisesRegex(SystemExit, 'incomplete/duplicate'):
            self.main('--mark', '--review', str(path))

    def test_state_and_stage_never_store_fetched_body_or_credential(self):
        self.main()
        for file in self.root.glob('*.json'):
            raw = file.read_text()
            self.assertNotIn('SYNTHETIC_BODY', raw)
            self.assertNotIn('FAKE_REFRESH', raw)
            self.assertNotIn('FAKE', raw)

    def test_receipt_and_template_do_not_fetch_or_read_env(self):
        self.main()
        with patch.object(x, 'load_env', side_effect=AssertionError('no credential read')):
            before = len(self.calls)
            self.main('--receipt')
            self.main('--review-template', str(self.root/'template.json'))
            self.assertEqual(len(self.calls), before)

    def test_429_and_network_failure_do_not_mark_or_advance(self):
        for error in [HTTPError(429), OSError('network')]:
            with patch.object(x, 'api_get_bookmarks', side_effect=error):
                with self.assertRaises(SystemExit):
                    self.main()
            self.assertEqual(x.load_seen()['consumed'], [])
            self.assertFalse(w.path_for(x.SEEN, 'scan_token').exists())

    def test_401_retry_keeps_cursor_and_request_budget(self):
        self.make_items(501)
        original = self.page
        count = 0
        def once(user, token, cursor=None):
            nonlocal count
            count += 1
            if count == 1:
                raise HTTPError(401)
            return original(user, token, cursor)
        with patch.object(x, 'api_get_bookmarks', side_effect=once), patch.object(x, 'refresh_access_token', return_value=('FAKE_NEW', 'FAKE_REFRESH_NEW')):
            self.main()
        self.assertEqual(count, 10)
        self.assertEqual(len(x.load_pending()), 450)
        staged = w.read_json(x._pending_path())
        self.assertEqual(w.proposed_checkpoint(x.SEEN, staged)['next_token'], '450')
        self.mark()
        self.main()
        self.assertEqual(len(x.load_pending()), 51)

    def test_corrupt_cursor_state_refuses(self):
        w.path_for(x.SEEN, 'scan_token').write_text('{bad')
        with self.assertRaisesRegex(SystemExit, 'REFUSING'):
            self.main()
        self.assertEqual(self.calls, [])

    def test_duplicate_page_ids_preserve_first_seen_order(self):
        self.items = [{'id': key, 'author_id': 'fixture', 'text': 'fixture'} for key in ['A', 'B', 'A', 'C']]
        self.main()
        self.assertEqual(x.load_pending(), ['A', 'B', 'C'])

    def test_corrupt_or_future_stage_cannot_mark(self):
        self.main()
        original = w.read_json(x._pending_path())
        for value in [float('nan'), float('inf'), __import__('time').time()+3600]:
            damaged = dict(original, staged_at=value)
            x._pending_path().write_text(json.dumps(damaged))
            self.main('--mark')
            self.assertEqual(x.load_seen()['consumed'], [])
        x._pending_path().write_text(json.dumps(dict(original, ids=[{'text': 'MUST_NOT_PERSIST'}])))
        with self.assertRaisesRegex(SystemExit, 'plain IDs'):
            self.main('--mark')
        self.assertEqual(x.load_seen()['consumed'], [])

    def test_incomplete_proposal_tampering_prevents_seen_write(self):
        self.main()
        path = self.review()
        proposal = w.path_for(x.SEEN, 'next_token')
        proposal.write_text('{}')
        with self.assertRaisesRegex(SystemExit, 'missing/changed'):
            self.main('--mark', '--review', str(path))
        self.assertEqual(x.load_seen()['consumed'], [])

    def test_zero_items_at_head_makes_no_review_claim(self):
        self.make_items(0)
        _, output = self.main()
        self.assertIn('No new items', output)
        self.assertNotIn('M dispatched', output)
        self.assertNotIn('Reviewed/marked', output)

    def test_existing_followup_ref_retains_unread_gap(self):
        self.main()
        followup = self.root/'followup.md'
        followup.write_text('Fixture follow-up only')
        path = self.review(read_state='unread', follow_up='followup.md')
        with patch.object(w, 'ROOT', self.root):
            self.main('--mark', '--review', str(path))
        receipt = w.read_json(w.path_for(x.SEEN, 'receipt'))
        self.assertEqual(receipt['read_counts'], {'unread': 1})
        self.assertEqual(receipt['follow_ups'][0]['ref'], 'followup.md')


    def test_unread_is_not_rejected_or_fully_read(self):
        self.main()
        path = self.review(read_state='unread', disposition='KILL')
        with self.assertRaisesRegex(SystemExit, 'unread is not rejected'):
            self.main('--mark', '--review', str(path))
        path = self.review(ask_user='Need the article body to assess the claim.')
        with self.assertRaisesRegex(SystemExit, 'conflicts with fully_read'):
            self.main('--mark', '--review', str(path))
        self.assertEqual(x.load_seen()['consumed'], [])



if __name__ == '__main__':
    unittest.main(verbosity=2)
