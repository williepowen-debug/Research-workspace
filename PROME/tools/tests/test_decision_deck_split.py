"""L393: fixture-only split, navigation and ruling-store regressions."""
import datetime as dt
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import decision_deck as D


class DeckSplit(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        paths = {k: self.root / k for k in ('Q', 'AD', 'DOCKET', 'EXPL', 'LEDGER')}
        self.addCleanup(patch.stopall)
        patch.multiple(D, ROOT=self.root, ARCH=[], **paths).start()
        D.Q.write_text('''## OPEN
| # | Item | Type | Needed by | Open since | PROME rec | Notes |
|---|---|---|---|---|---|---|
| 1 | Ordinary source <unsafe> | RULE | 2026-09-16 | 9/15 | Recommend one | original note |
| 2 | APPROVED hands | ACTION | 2026-09-17 | 9/15 | Complete hands | already answered |
| 3 | Blocked request | RULE | | 9/15 | Wait | ⛔ waits: OTHER |
## RECENTLY DONE
| 4 Historical title | 2026-09-14 | Entire ruling retained |
''')
        D.AD.write_text('''## Live Decision Index
| Decision | State | Owner | Next | Backstop | Source |
|---|---|---|---|---|---|
| Flight fixture | In progress | DESK | Next step | Full backstop | Full source |
''')
        D.DOCKET.write_text('2026-09-16\tWill catalyst\tWill\tPENDING\tartifact\n2026-09-16\tOther owner catalyst\tOTHER\tPENDING\tartifact\n')
        D.EXPL.write_text('wq\tname\twhat\twhy_yours\tif_yes\tif_no\tif_nothing\trec_reason\n1\tExplained name\tFull what\tFull why\tFull yes\tFull no\tFull nothing\tFull recommendation\n')
        self.out = self.root / 'output' / 'owed deck.html'
        self.today = dt.date(2026, 9, 15)
        patch.object(D, 'days_dark', return_value=None).start()

    def build(self, **kwargs):
        result = D.build(self.today, self.out, **kwargs)
        return result, self.out.read_text(), Path(result['reference_out']).read_text()

    def test_partition_retains_full_content_and_actions(self):
        r, owed, reference = self.build()
        self.assertEqual(r['explainers_missing'], ['2', '3'])
        for content in ('Full what', 'Full why', 'Full yes', 'Full no', 'Full nothing', 'Full recommendation', 'original note', 'Explainer owed'):
            self.assertIn(content, owed)
        self.assertIn('&lt;unsafe&gt;', owed)
        for ident in ('wq-1', 'wq-2', 'wq-3'):
            self.assertIn(f'id="{ident}"', owed)
            self.assertNotIn(f'id="{ident}"', reference)
        for content in ('Entire ruling retained', 'Full backstop', 'Full source', 'Will catalyst'):
            self.assertIn(content, reference)
            self.assertNotIn(content, owed)
        self.assertNotIn('Other owner catalyst', reference)
        self.assertIn('id="ap-1"', owed)
        self.assertIn('id="dn-2"', owed)
        self.assertNotIn('id="ap-2"', owed)
        self.assertNotIn('<div class="tap" data-wq="3">', owed)
        self.assertNotIn('window.claude', reference)
        self.assertNotIn('data-v=', reference)
        self.assertIn("db.collection('rulings')", owed)
        self.assertEqual(re.search('data-build="([^"]+)"', owed)[1], re.search('data-build="([^"]+)"', reference)[1])

    def test_local_links_encode_paths_and_work_across_directories(self):
        r, owed, reference = self.build(reference_out=self.root / 'other folder' / 'reference.html')
        self.assertEqual(r['link_mode'], 'local')
        self.assertIn('href="../other%20folder/reference.html"', owed)
        self.assertIn('href="../output/owed%20deck.html"', reference)

    def test_hosted_pair_preserves_original_store_location(self):
        url = 'https://claude.ai/code/artifact/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'
        r, owed, reference = self.build(owed_url=D.OWED_ARTIFACT_URL, reference_url=url)
        self.assertEqual(r['link_mode'], 'hosted')
        self.assertIn(f'href="{url}"', owed)
        self.assertIn(f'href="{D.OWED_ARTIFACT_URL}"', reference)

    def test_invalid_hosted_targets_fail_before_writes(self):
        original = D.OWED_ARTIFACT_URL
        for kwargs in (
            {'owed_url': original},
            {'reference_url': original},
            {'owed_url': original, 'reference_url': 'javascript:alert(1)'},
            {'owed_url': original, 'reference_url': original},
            {'owed_url': original, 'reference_url': original[:-36] + original[-36:].upper() + '/'},
            {'owed_url': 'https://claude.ai/code/artifact/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 'reference_url': original},
        ):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                self.build(**kwargs)
            self.assertFalse(self.out.exists())

    def test_same_output_and_symlink_are_rejected_without_overwrite(self):
        self.out.parent.mkdir()
        self.out.write_text('preserve')
        link = self.root / 'alias.html'
        link.symlink_to(self.out)
        for ref in (self.out, link):
            with self.assertRaises(ValueError):
                self.build(reference_out=ref)
            self.assertEqual(self.out.read_text(), 'preserve')

    def test_hosted_reference_note_present_missing_malformed(self):
        # WQ-382 (a) (2026-10-08): AC1 present -> built + version; AC2 missing/malformed -> UNKNOWN, no crash.
        import json as _json, tempfile as _tf
        from pathlib import Path as _P
        with _tf.TemporaryDirectory() as d:
            ok = _P(d) / "ok.json"; ok.write_text(_json.dumps({"built": "2026-09-26 16:03", "version": "v12"}), encoding="utf-8")
            self.assertEqual(D._hosted_reference_note(ok), "hosted build 2026-09-26 16:03 (v12); refreshes on Will's word or at a spine audit")
            self.assertIn("hosted build UNKNOWN", D._hosted_reference_note(_P(d) / "absent.json"))
            bad = _P(d) / "bad.json"; bad.write_text("{not json", encoding="utf-8")
            self.assertIn("hosted build UNKNOWN", D._hosted_reference_note(bad))
            empty = _P(d) / "empty.json"; empty.write_text(_json.dumps({"built": "", "version": "v1"}), encoding="utf-8")
            self.assertIn("hosted build UNKNOWN", D._hosted_reference_note(empty))

    def test_history_growth_stays_out_of_owed(self):
        history = 'HISTORY_ONLY_' * 10000
        D.Q.write_text(D.Q.read_text() + f'| 5 More history | 2026-09-14 | {history} |\n')
        _, owed, reference = self.build()
        self.assertNotIn('HISTORY_ONLY_', owed)
        self.assertIn(history, reference)

    def test_ui_and_rulings_with_stub_runtime(self):
        self.assertIsNotNone(shutil.which('node'), 'Node is required to exercise production JavaScript')
        result = subprocess.run(['node', str(Path(__file__).with_name('decision_deck_runtime.cjs'))],
                                input=json.dumps({'ui': D.UI_JS, 'rulings': D.RULING_JS}),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
