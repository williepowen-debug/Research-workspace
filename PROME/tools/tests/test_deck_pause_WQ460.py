"""WQ-460: paused Deck checks do no I/O; unrelated closeout checks stay active.

Acceptance and read history: proposals/2026-10-19_wq460-decision-deck-paused-RULED.md.
All mutable inputs are disposable fixtures; never run a live boot or closeout.
"""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import prome_gate as G


class DeckPause(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        for name, value in [('ROOT', self.root), ('results', [])]:
            p = patch.object(G, name, value)
            p.start()
            self.addCleanup(p.stop)

    def test_default_pause_does_not_read_even_missing_or_broken_inputs(self):
        self.assertTrue(G.DECISION_DECK_PAUSED)
        with patch.object(Path, 'read_text', side_effect=AssertionError('paused input read')):
            G.check_publication_prereqs()
            G.check_deck_republish()
        self.assertEqual(len(G.results), 2)
        for severity, name, ok, detail, owner in G.results:
            self.assertEqual(severity, G.ADVISE)
            self.assertTrue(ok)
            self.assertTrue(detail.startswith('PAUSED BY WILL (WQ-460)'))
            self.assertNotIn('NO-OP', detail)
            self.assertNotIn('PUBLISHED', detail)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_active_missing_inputs_still_report_unknown(self):
        with patch.object(G, 'DECISION_DECK_PAUSED', False):
            G.check_publication_prereqs()
            G.check_deck_republish()
        self.assertEqual(len(G.results), 2)
        for _, _, ok, detail, _ in G.results:
            self.assertFalse(ok)
            self.assertTrue(detail.startswith('UNKNOWN'))

    def test_pause_cannot_mask_other_blocking_or_unknown_results(self):
        G.check_publication_prereqs()
        G.check_deck_republish()
        paused = list(G.results)
        self.assertEqual(G.aggregate_rc(paused, []), 0)
        self.assertEqual(G.aggregate_rc(paused + [(G.BLOCK, 'position', False, '', '')], []), 1)
        self.assertEqual(G.aggregate_rc(paused + [(G.ERROR, 'unknown', False, '', '')], []), 2)

    def test_closeout_dispatch_preserves_queue_position_and_review_controls(self):
        invoked = []
        scripts = []
        def guard(check, *args, **kwargs):
            invoked.append(check.__name__)
            if check in (G.check_publication_prereqs, G.check_deck_republish):
                check()
        def run_script(severity, name, cmd, *args, **kwargs):
            scripts.append((severity, cmd))
        with patch.object(G, 'guard', side_effect=guard), \
             patch.object(G, 'run_script', side_effect=run_script), \
             patch.object(G, 'check_orch_closeout'):
            G.mode_closeout('standard', [], [])
        for name in ['check_publication_prereqs', 'check_deck_republish',
                     'check_review_manifest', 'check_gates_tsv', 'check_will_queue',
                     'check_orch_log_observed', 'check_memory_declared', 'check_consumer_declared']:
            self.assertIn(name, invoked)
        for tool in ['scripts/position_agreement_check.py', 'scripts/orch_log.py',
                     'PROME/tools/table_check.py', 'PROME/tools/done_rows_check.py']:
            self.assertTrue(any(sev == G.BLOCK and tool in cmd for sev, cmd in scripts), tool)
        self.assertEqual(len(G.results), 2)
        self.assertTrue(all('PAUSED BY WILL' in row[3] for row in G.results))


if __name__ == '__main__':
    unittest.main()
