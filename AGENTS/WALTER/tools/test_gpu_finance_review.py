"""Acceptance cases for GPU_FINANCE_REVIEW (Will 2026-11-11): label-matched rows surface,
identical titles fold, other labels and pre-baseline days stay out, a disposition consumes
exactly one open key, a closed or unknown key is refused, an unreadable state is UNKNOWN."""
import json, tempfile, unittest
from pathlib import Path
from unittest import mock
import intake_scan as s


def row(title, label='gpu-obsolescence-1'):
    return dict(title=title, label=label, link='https://example.test/' + title[:5], source='X', date='Wed, 11 Nov 2026 12:00:00 GMT')


class GpuQueue(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.lane = Path(self.tmp.name) / 'lane'
        self.state = Path(self.tmp.name) / 'gpu_state.json'
        for day, items in {
            '2026-11-10': [row('Before baseline')],
            '2026-11-11': [row('Ares wary of GPU loans'), row('Unrelated', label='bank-earnings'), row('Same story')],
            '2026-11-12': [row('Same story', label='gpu-obsolescence-3')],
        }.items():
            (self.lane / 'data' / day).mkdir(parents=True)
            (self.lane / 'data' / day / 'news.json').write_text(json.dumps({'items': items}))
        self.p = [mock.patch.object(s, 'LANE', self.lane), mock.patch.object(s, 'GPU_STATE', self.state)]
        for x in self.p: x.start()

    def tearDown(self):
        for x in self.p: x.stop()
        self.tmp.cleanup()

    def test_surface_fold_and_exclusions(self):
        q, err = s.gpu_finance_queue()
        self.assertEqual(err, [])
        titles = sorted(c['title'] for c in q)
        self.assertEqual(titles, ['Ares wary of GPU loans', 'Same story'])
        same = [c for c in q if c['title'] == 'Same story'][0]
        self.assertEqual(len(same['rows']), 2)

    def test_disposition_consumes_one_and_refuses_repeat(self):
        q, _ = s.gpu_finance_queue()
        k = [c for c in q if c['title'] == 'Same story'][0]['key']
        self.assertEqual(s.gpu_disposition(k, 'DUP', 'SIG-W-20261111-020'), 0)
        self.assertEqual(len(s.gpu_finance_queue()[0]), 1)
        self.assertEqual(s.gpu_disposition(k, 'DUP', 'again'), 2)
        self.assertEqual(s.gpu_disposition('gpu:000000000000', 'KILL', 'x'), 2)
        self.assertEqual(s.gpu_disposition(q[0]['key'], 'BOGUS', 'x'), 2)
        self.assertEqual(s.gpu_disposition(q[0]['key'], 'KILL', '  '), 2)

    def test_unreadable_state_is_unknown_not_empty(self):
        self.state.write_text('{not json')
        q, err = s.gpu_finance_queue()
        self.assertEqual(q, [])
        self.assertTrue(err and 'UNKNOWN' in err[0])


if __name__ == '__main__':
    unittest.main()
