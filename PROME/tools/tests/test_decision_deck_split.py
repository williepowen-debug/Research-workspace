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

    # ---- Change A (DOCKET L660): selectable options — ACCEPTANCE_deck_options_2026-10-09.md ----
    CARD = ('# Card\n## 2. Context\n| a | b |\n|---|---|\n| x | y |\n'
            '## 3. The choices\n| # | choice | what you get |\n|---|---|---|\n'
            '| **A** | **Sell it now** (§4) | ≈ $100 |\n| B | Hold to 10/14 | nothing |\n| **No re-rule** | letter stands | — |\n'
            '## 4. After\ntext\n')
    HCARD = '# H\n## 3. Re-rule\n| option | effect |\n|---|---|\n| **R-A: permit a sale** | $90 |\n| **R-B: ride, close 10/16** | spirit |\n'

    def _expl10(self, options='', source=''):
        D.EXPL.write_text('wq\tname\twhat\twhy_yours\tif_yes\tif_no\tif_nothing\trec_reason\toptions\toptions_source\n'
                          f'1\tExplained name\tFull what\tFull why\tFull yes\tFull no\tFull nothing\tFull recommendation\t{options}\t{source}\n')
        (self.root / 'cards').mkdir(exist_ok=True)
        (self.root / 'cards' / 'x.md').write_text(self.CARD)
        (self.root / 'cards' / 'h.md').write_text(self.HCARD)

    @staticmethod
    def _article(html_text, wq):
        m = re.search(rf'<article class="card[^"]*" id="wq-{wq}".*?</article>', html_text, re.S)
        return m.group(0)

    PARENT = 'efd67fbf0^'   # the last pre-Change-A generator (read 1, ❌1: compare against the PARENT render, never new-vs-new)

    def _parent_articles(self, wqs):
        """Render the same fixture with the pre-Change-A generator (git show) and return its plain articles."""
        import importlib.util
        repo = Path(__file__).resolve().parents[3]
        src = subprocess.run(['git', '-C', str(repo), 'show', f'{self.PARENT}:PROME/tools/decision_deck.py'], capture_output=True, text=True)
        if src.returncode != 0:
            self.skipTest('parent generator not available from git history')
        mod_path = self.root / 'parent_decision_deck.py'; mod_path.write_text(src.stdout)
        spec = importlib.util.spec_from_file_location('parent_decision_deck', mod_path)
        P = importlib.util.module_from_spec(spec); spec.loader.exec_module(P)
        for k in ('ROOT', 'Q', 'AD', 'DOCKET', 'EXPL', 'LEDGER'):
            setattr(P, k, getattr(D, k))
        P.ARCH = []; P.days_dark = lambda desk: None
        out = self.root / 'parent' / 'owed.html'
        P.build(self.today, out)
        text = out.read_text()
        return {wq: self._article(text, wq) for wq in wqs}

    def test_ac1_plain_card_byte_identical_to_the_parent_render(self):
        self._expl10()                                   # 10-column sidecar, options empty
        r, owed10, _ = self.build()
        parent = self._parent_articles(['1', '2'])
        for wq in ('1', '2'):
            self.assertEqual(parent[wq], self._article(owed10, wq), f'plain card wq-{wq} differs from the pre-Change-A render')
        self.assertEqual(r['options_rows'], [])
        self.assertIn('<div class="tap" data-wq="1">', owed10)

    def test_ac2_options_render_verbatim_with_consequences_and_no_approve(self):
        self._expl10('A = Sell it now :: ≈ $100 || B = Hold to 10/14 :: nothing', 'cards/x.md#3')
        r, owed, reference = self.build()
        self.assertEqual(r['options_rows'], ['1']); self.assertEqual(r['options_warnings'], [])
        for frag in ('id="ch-1-A"', 'id="ch-1-B"', 'data-did="1"', 'class="otext">Sell it now<', '<span class="ocons">≈ $100<',
                     'id="lt-1"', 'id="note-1"', 'Full nothing', 'Full recommendation', 'cards/x.md</code> §3'):
            self.assertIn(frag, owed)
        for frag in ('id="ap-1"', 'id="dc-1"', 'Full yes', 'Full no<'):
            self.assertNotIn(frag, owed)
        self.assertNotIn('data-v=', reference)

    def test_ac6_two_decision_units_on_one_row(self):
        self._expl10('TLT: A = Sell it now :: ≈ $100 || B = Hold to 10/14 :: nothing ;; HBAN: R-A = permit a sale :: $90 || R-B = ride, close 10/16 :: spirit',
                     'TLT=cards/x.md#3 ;; HBAN=cards/h.md#3')
        r, owed, _ = self.build()
        self.assertEqual(r['options_warnings'], [])
        self.assertEqual(owed.count('id="wq-1"'), 1)
        for frag in ('id="tap-1.TLT" data-wq="1" data-did="1.TLT"', 'id="tap-1.HBAN" data-wq="1" data-did="1.HBAN"',
                     'id="ch-1.HBAN-R-A"', 'id="note-1.TLT"', 'id="note-1.HBAN"', '<span class="did">1.HBAN</span>'):
            self.assertIn(frag, owed)

    def test_ac4_mismatch_fails_the_build_and_writes_nothing(self):
        for options in ('A = Sell it now :: ≈ $100 || B = Hold to 10/14 :: nothing || C = Invented :: x',   # deck-but-not-offered
                        'A = Sell it now :: ≈ $100',                                                      # offered-but-missing
                        'A = Sell it later :: ≈ $100 || B = Hold to 10/14 :: nothing'):                  # text not a prefix
            with self.subTest(options=options):
                self._expl10(options, 'cards/x.md#3')
                with self.assertRaises(SystemExit) as cm:
                    self.build()
                self.assertIn('WQ-1', str(cm.exception))
                self.assertFalse(self.out.exists())

    def test_ac5_unreadable_source_falls_back_to_the_plain_card_with_a_warning(self):
        for source in ('cards/x.md#9', 'cards/missing.md#3', 'cards/x.md#2', ''):
            with self.subTest(source=source):
                self._expl10('A = Sell it now || B = Hold to 10/14', source)
                r, owed, _ = self.build()
                self.assertIn('id="ap-1"', owed); self.assertNotIn('id="ch-1-A"', owed)
                self.assertIn('<div class="tap" data-wq="1">', owed)       # the whole-row plain card, parent markup
                self.assertEqual(len(r['options_warnings']), 1); self.assertIn('WQ-1', r['options_warnings'][0])

    def test_ac4_ac6_partial_drop_in_a_two_unit_row_keeps_both_decision_ids(self):
        # read 1 ❌4: one unit's source unreadable ⇒ that unit renders PLAIN controls under ITS OWN id; the other keeps its options
        self._expl10('TLT: A = Sell it now :: ≈ $100 || B = Hold to 10/14 :: nothing ;; HBAN: R-A = permit a sale :: $90 || R-B = ride, close 10/16 :: spirit',
                     'TLT=cards/moved.md#3 ;; HBAN=cards/h.md#3')
        r, owed, _ = self.build()
        self.assertEqual(len(r['options_warnings']), 1); self.assertIn('WQ-1.TLT', r['options_warnings'][0])
        for frag in ('id="tap-1.TLT" data-wq="1" data-did="1.TLT"', 'id="ap-1.TLT"', 'id="dc-1.TLT"', 'id="lt-1.TLT"', 'id="note-1.TLT"',
                     'id="tap-1.HBAN" data-wq="1" data-did="1.HBAN"', 'id="ch-1.HBAN-R-A"', '<span class="did">1.TLT</span>'):
            self.assertIn(frag, owed)
        self.assertNotIn('id="ch-1.TLT-A"', owed); self.assertNotIn('id="ap-1"', owed); self.assertNotIn('data-did="1"', owed)

    def test_declared_plain_unit_renders_plain_controls_under_its_own_id(self):
        self._expl10('TLT: PLAIN :: owner card re-cut owed :: APPROVE=sell it (card A) :: DECLINE=hold it (card C) ;; HBAN: R-A = permit a sale :: $90 || R-B = ride, close 10/16 :: spirit', 'HBAN=cards/h.md#3')
        r, owed, _ = self.build()
        self.assertEqual(r['options_warnings'], [])
        for frag in ('id="ap-1.TLT"', 'owner card re-cut owed', 'id="ch-1.HBAN-R-B"',
                     '<span class="otext" data-for="APPROVE">sell it (card A)</span>', '<span class="otext" data-for="DECLINE">hold it (card C)</span>'):
            self.assertIn(frag, owed)
        # read 2 ❌X2: a PLAIN unit on a multi-decision row must state both meanings
        self._expl10('TLT: PLAIN :: owner card re-cut owed ;; HBAN: R-A = permit a sale :: $90 || R-B = ride, close 10/16 :: spirit', 'HBAN=cards/h.md#3')
        with self.assertRaises(ValueError):
            self.build()
        # read 2 ⚠️W6 (the ❌4 class): options_source naming a unit the options cell lacks refuses the build
        self._expl10('HBAN: R-A = permit a sale :: $90 || R-B = ride, close 10/16 :: spirit', 'TLT=cards/x.md#3 ;; HBAN=cards/h.md#3')
        with self.assertRaises(SystemExit) as cm:
            self.build()
        self.assertIn('unit-for-unit', str(cm.exception))
        # a single declared PLAIN unit is simply today's plain card
        self._expl10('PLAIN :: held', '')
        r, owed, _ = self.build()
        self.assertIn('<div class="tap" data-wq="1">', owed); self.assertNotIn('class="tap unit"', owed)

    def test_ac2_consequence_must_be_verbatim_from_the_card_cells(self):
        # read 1 ❌2: a paraphrased consequence refuses the build; verbatim cells (+ a [PROME: …] bracket) pass
        self._expl10('A = Sell it now :: ≈ $100 [PROME: 9/26 marks] || B = Hold to 10/14 :: nothing', 'cards/x.md#3')
        r, owed, _ = self.build()
        self.assertIn('≈ $100 [PROME: 9/26 marks]', owed)
        # read 2 ❌X1: a paraphrase, a PARTIAL copy, a bracket-only, an empty and a one-character consequence all refuse
        for bad in ('about one hundred dollars', '$100', '[PROME: only a note]', '', '$'):
            with self.subTest(consequence=bad):
                self._expl10(f'A = Sell it now :: {bad} || B = Hold to 10/14 :: nothing', 'cards/x.md#3')
                if self.out.exists():
                    self.out.unlink()                     # a passing build above wrote it; the refusal must not
                with self.assertRaises(SystemExit) as cm:
                    self.build()
                self.assertIn('consequence', str(cm.exception)); self.assertFalse(self.out.exists())

    def test_malformed_options_cell_is_promes_defect_and_raises(self):
        for options in ('A Sell it now', 'a = lower label', 'A = x || A = y', 'A = x ;; B = y'):
            with self.subTest(options=options):
                self._expl10(options, 'cards/x.md#3')
                with self.assertRaises(ValueError):
                    self.build()

    def test_offered_options_reads_only_label_shaped_rows_of_the_numbered_section(self):
        self._expl10()
        self.assertEqual(D.offered_options('cards/x.md', '3'), [{'label': 'A', 'text': 'Sell it now (§4)', 'cells': '≈ $100'}, {'label': 'B', 'text': 'Hold to 10/14', 'cells': 'nothing'}])
        self.assertEqual(D.offered_options('cards/h.md', '3'), [{'label': 'R-A', 'text': 'permit a sale', 'cells': '$90'}, {'label': 'R-B', 'text': 'ride, close 10/16', 'cells': 'spirit'}])
        self.assertIsNone(D.offered_options('cards/x.md', '2'))
        self.assertIsNone(D.offered_options('cards/x.md', '4'))


if __name__ == '__main__':
    unittest.main()
