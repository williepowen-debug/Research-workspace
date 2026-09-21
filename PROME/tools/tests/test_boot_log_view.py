"""Phase 3: conserve log evidence, fail safely, and bind paged views to source.

Mutable inputs are disposable fixtures. No boot gate or live ledger is executed.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, TOOLS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


reader = load('log_view_reader', 'boot_read.py')
orch = load('log_view_orch', 'orch_closeout.py')
HEADER = ('ORCH_LOG closeout evidence — 2026-09-21 + unresolved prior touches; '
          'attributed records, not native receipt authentication\n')
REASON = 'missing or duplicate structured closeout evidence'
GROUP = f'UNKNOWN (each entry): {REASON}\n'
VIEW = 'orch-compact-v1'


def identity(index, day='2026-09-01', desk='ALPHA', touch='1-SPAWN'):
    key = hashlib.sha256(str(index).encode()).hexdigest()
    return f'{day} {desk} touch {touch} [{key}]'


def gap(index, **kwargs):
    return f'UNKNOWN: {identity(index, **kwargs)}: {REASON}\n'


class LogView(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='boot-log-view-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.path = self.root / 'check.txt'

    def put(self, content):
        self.path.write_bytes(content.encode('utf-8'))

    def read_all(self, view=VIEW):
        offset, digest, texts, pages = 0, None, [], []
        while True:
            page = reader.page(self.path, offset, digest, view)
            texts.append(page['text'])
            pages.append(page)
            encoded = json.dumps(page['text'], ensure_ascii=False)[1:-1].encode('utf-8')
            self.assertLessEqual(len(encoded), reader.PAGE_TEXT_BYTES)
            if page['eof']:
                self.assertIsNone(page['next_offset'])
                return ''.join(texts), pages
            self.assertGreater(page['next_offset'], offset)
            offset, digest = page['next_offset'], page['sha256']

    def test_group_retains_every_identity_order_reason_and_unknown_state(self):
        source = HEADER + gap(1) + gap(2, day='2026-09-21', desk='OTHER', touch='2a')
        self.put(source)
        text, pages = self.read_all()
        self.assertEqual(text, HEADER + GROUP + '  ' + identity(1) + '\n  ' +
                         identity(2, day='2026-09-21', desk='OTHER', touch='2a') + '\n')
        self.assertEqual(pages[0]['compacted_groups'], 1)
        self.assertEqual(self.path.read_text(), source)

    def test_old_pending_asks_novel_failure_and_inventory_gap_survive_overlap(self):
        pending = ('ASKED → still working: 1\n  2020-01-01 OLD touch 1 [full-key]: '
                   'ask: outstanding | pending; no completion receipt established\n')
        new = '❌ BLOCKING: a new failure in a previously quiet check — owner BETA\n'
        unknown = 'UNKNOWN: spawn inventory coverage UNKNOWN; ledger absence cannot prove no spawns\n'
        source = HEADER + pending + gap(1) + gap(2) + new + gap(3) + gap(4) + unknown
        self.put(source)
        text, _ = self.read_all()
        self.assertIn(pending, text)
        self.assertIn(new, text)
        self.assertTrue(text.endswith(unknown))
        for i in range(1, 5):
            self.assertIn(identity(i), text)
        self.assertEqual(text.count(GROUP), 2)

    def test_unfamiliar_and_malformed_rows_stay_verbatim(self):
        novel = f'UNKNOWN: {identity(5)}: receipt contradicts owner; action still owed\n'
        malformed = gap(6).replace('touch 1-SPAWN', 'touch ?')
        unusual = gap(7, desk='TWO WORDS')
        source = HEADER + gap(1) + gap(2) + novel + malformed + unusual
        self.put(source)
        text, _ = self.read_all()
        self.assertTrue(text.endswith(novel + malformed + unusual))

    def test_wrong_header_other_check_and_singleton_fall_back_to_full(self):
        for source in ('other check\n' + gap(1) + gap(2),
                       HEADER.replace('attributed records', 'new format') + gap(1) + gap(2),
                       HEADER + gap(1), '', '❌ missing evidence\n',
                       HEADER + gap(1) + gap(2).rstrip('\n')):
            with self.subTest(source=source[:40]):
                self.put(source)
                text, pages = self.read_all()
                self.assertEqual(text, source)
                self.assertEqual(pages[0]['representation'], 'full-fallback')

    def test_pagination_conserves_unicode_and_escaped_text(self):
        tail = ('⚠️ novel \\path\t"quoted" 🧭' * 400) + '\n'
        source = HEADER + ''.join(gap(i) for i in range(180)) + tail
        self.put(source)
        expected = HEADER + GROUP + ''.join('  ' + identity(i) + '\n' for i in range(180)) + tail
        text, pages = self.read_all()
        self.assertEqual(text, expected)
        self.assertGreater(len(pages), 1)
        full, _ = self.read_all('full')
        self.assertEqual(full, source)

    def test_full_mode_keeps_raw_digest_and_result_interface(self):
        source = HEADER + gap(1) + gap(2)
        self.put(source)
        page = reader.page(self.path)
        self.assertEqual(page['sha256'], hashlib.sha256(source.encode()).hexdigest())
        self.assertEqual(page['text'], source)
        self.assertNotIn('view', page)

    def test_changed_source_refuses_even_when_group_shape_is_unchanged(self):
        self.put(HEADER + ''.join(gap(i) for i in range(100)))
        first = reader.page(self.path, view=VIEW)
        self.put(self.path.read_text().replace('ALPHA', 'BETA', 1))
        with self.assertRaisesRegex(ValueError, 'Source or view changed'):
            reader.page(self.path, first['next_offset'], first['sha256'], VIEW)

    def test_switching_representation_refuses_in_both_directions(self):
        self.put(HEADER + ''.join(gap(i) for i in range(100)))
        for old, new in [('full', VIEW), (VIEW, 'full')]:
            first = reader.page(self.path, view=old)
            with self.assertRaisesRegex(ValueError, 'Source or view changed'):
                reader.page(self.path, first['next_offset'], first['sha256'], new)

    def test_bad_offsets_or_missing_digest_refuse(self):
        self.put(HEADER + gap(1) + gap(2))
        first = reader.page(self.path, view=VIEW)
        for offset, digest in [(-1, None), (1, None), (99999, first['sha256'])]:
            with self.subTest(offset=offset), self.assertRaises(ValueError):
                reader.page(self.path, offset, digest, VIEW)

    def test_missing_unreadable_or_invalid_utf8_never_says_eof(self):
        script = self.root / 'boot_read.py'
        shutil.copyfile(TOOLS / 'boot_read.py', script)
        self.path.write_bytes(b'\xff')
        for target in (self.root / 'absent.txt', self.root, self.path):
            result = subprocess.run([sys.executable, '-B', str(script), str(target),
                                     '--view', VIEW], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            report = json.loads(result.stdout)
            self.assertFalse(report['eof'])
            self.assertIn('error', report)

    def test_public_cli_pages_and_binds_view(self):
        self.put(HEADER + ''.join(gap(i) for i in range(100)))
        script = self.root / 'boot_read.py'
        shutil.copyfile(TOOLS / 'boot_read.py', script)
        command = [sys.executable, '-B', str(script), str(self.path)]
        first = subprocess.run(command + ['--view', VIEW], capture_output=True, text=True)
        self.assertEqual(first.returncode, 0)
        report = json.loads(first.stdout)
        args = ['--offset', str(report['next_offset']), '--sha256', report['sha256']]
        wrong = subprocess.run(command + args, capture_output=True, text=True)
        self.assertEqual(wrong.returncode, 2)
        right = subprocess.run(command + args + ['--view', VIEW], capture_output=True, text=True)
        self.assertEqual(right.returncode, 0)
        self.assertEqual(json.loads(right.stdout)['offset'], report['next_offset'])

    def test_real_producer_fixture_retains_prior_unresolved_and_coverage(self):
        ledger = self.root / 'orch.tsv'
        rows = []
        for i in range(3):
            rows.append(['2020-01-01', f'DESK{i}', 'T1', '1', 'fixture',
                         'N/A', 'N/A', 'YES', '', 'N/A', 'N/A', 'N/A', '0'])
        evidence = {'owner':'PROME', 'session_id':'test', 'touch_at':'2020-01-01T12:00:00-05:00',
                    'observed_at':'2020-01-01T13:00:00-05:00', 'state':'ASKED_WORKING', 'ask':'still owed'}
        rows.append(['2020-01-01', 'OLD', 'T1', '1', 'fixture', 'N/A', 'N/A', 'YES',
                     'closeout_v1=' + json.dumps(evidence), 'N/A', 'N/A', 'N/A', '0'])
        ledger.write_text('\t'.join(orch.HEADER) + '\n' +
                          ''.join('\t'.join(row) + '\n' for row in rows))
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            rc = orch.main(['--ledger', str(ledger), '--date', '2026-09-21'])
        self.assertEqual(rc, 1)
        self.put(stdout.getvalue())
        text, _ = self.read_all()
        for row in rows:
            self.assertIn(orch.touch_key(row), text)
            self.assertIn(row[1], text)
        self.assertIn('ASKED → still working: 1', text)
        self.assertIn('ask: still owed | pending; no completion receipt established', text)
        self.assertIn('spawn inventory coverage UNKNOWN', text)
        self.assertIn(GROUP, text)


if __name__ == '__main__':
    unittest.main()
