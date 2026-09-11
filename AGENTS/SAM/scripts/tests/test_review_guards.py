"""Offline regression tests for the September 11 review findings."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1]
def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
memory = load('subagent_memory_roll')
kura = load('kura_proposal_roll')
cftc = load('cftc_jpy')

class ReviewGuards(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def test_protected_sections_keep_closed_children(self):
        for parent in ('## CALIBRATION', '## STANDING MONITORS', '## NEXT RUN HINTS', '## CHANGES SINCE LAST RUN'):
            with self.subTest(parent=parent):
                self.assertEqual(memory.classify('### CLOSED examples', 'CLOSED', parent)[0], 'stay')

    def test_pending_requires_positive_closure(self):
        for heading in ('### Run 20 — NOT CLOSED', '### Run 20 — UNCLOSED', '### Run 20 — CLOSED marker missing'):
            self.assertEqual(memory.classify(heading, 'CLOSED', '## PENDING (escalations)')[0], 'stay')
        self.assertEqual(memory.classify('### ✅ CLOSED by SAM', 'done', '## PENDING (escalations)')[0], 'roll')

    def test_live_pending_named_run_survives_recency(self):
        p = self.root / 'state.md'
        p.write_text('## PENDING (escalations)\n### Run 1 — current work\nAnother item is CLOSED; this one is live.\n')
        self.assertEqual(memory.plan(p, 0)[2], [])

    def kura_plan(self, topic, landed, suffix=''):
        p = self.root / 'KURA.md'
        p.write_text('## PROPOSED ADDS\n### Run 1 — old\nKB-SAM-1\tA\tB\tC\t' + topic + '\n' + suffix)
        with patch.object(kura, 'SPEC', p), patch.object(kura, 'landed_rows', return_value={'KB-SAM-1': landed}):
            return kura.plan(0)

    def test_topic_prefix_collision_stays(self):
        self.assertEqual(self.kura_plan('x'*40+' proposed', 'x'*40+' different')[2], [])

    def test_empty_topic_is_not_landing(self):
        self.assertEqual(self.kura_plan('', 'existing topic')[2], [])

    def test_same_id_with_conflicting_topics_stays(self):
        self.assertEqual(self.kura_plan('same', 'same', 'KB-SAM-1\tA\tB\tC\tdifferent\n')[2], [])

    def test_section_boundary_is_not_archived(self):
        for suffix in ('## OPERATING RULES\nKeep live\n', '### The rule\nKeep live\n'):
            roll = self.kura_plan(' Same — topic ', 'same - topic', suffix)[2]
            self.assertEqual(len(roll), 1)
            self.assertNotIn('Keep live', roll[0]['body'])

    def test_memory_apply_preserves_archived_body_and_protected_rules(self):
        p = self.root / 'state.md'
        body = '## PENDING from Run 1 — ✅ CLOSED\nVerbatim ¥ evidence.\n\n'
        live = '## CALIBRATION\n### CLOSED examples\nKeep this rule.\n'
        p.write_text(body + live)
        with patch.object(memory, 'SAM', self.root), patch('sys.argv', ['roller', str(p), '--apply', '--keep-runs', '0']), contextlib.redirect_stdout(io.StringIO()):
            memory.main()
        self.assertIn(body, (self.root / 'state_ARCHIVE.md').read_text())
        self.assertIn('Keep this rule.', p.read_text())
        self.assertNotIn('Verbatim ¥ evidence.', p.read_text())

    def test_kura_apply_preserves_body_and_trailing_rules(self):
        p, archive = self.root / 'KURA.md', self.root / 'archive.md'
        body = '### Run 1 — old\nKB-SAM-1\tA\tB\tC\tTopic ¥\n\n'
        tail = '### The rule\nAlways keep this instruction.\n'
        p.write_text('## PROPOSED ADDS\n' + body + tail)
        with patch.object(kura, 'SPEC', p), patch.object(kura, 'ARCHIVE', archive), patch.object(kura, 'landed_rows', return_value={'KB-SAM-1': 'Topic ¥'}), patch('sys.argv', ['roller', '--apply', '--keep-runs', '0']), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(kura.main(), 0)
        self.assertIn(body, archive.read_text())
        self.assertIn(tail, p.read_text())
        self.assertNotIn(tail, archive.read_text())

    def drift(self, rows):
        p = self.root / 'CFTC.tsv'
        p.write_text('Date\tChange_Net\n' + ''.join(f'{d}\t{c}\n' for d,c in rows))
        out = io.StringIO()
        with patch.object(cftc, 'CFTC_TSV', p), contextlib.redirect_stdout(out):
            result = cftc.multi_print_drift_check()
        return result, out.getvalue()

    def test_gap_cannot_be_called_consecutive(self):
        result, out = self.drift([('2026-08-11', -10000), ('2026-08-25', -10000)])
        self.assertIs(result, False)
        self.assertIn('NOT EVALUATED', out)
        self.assertNotIn('DRIFT FLAG', out)

    def test_bad_middle_observation_is_not_skipped(self):
        result, out = self.drift([('2026-08-11', -10000), ('2026-08-18', 'bad'), ('2026-08-25', -10000)])
        self.assertIs(result, False)
        self.assertIn('UNKNOWN', out)

    def test_reverse_order_uses_latest_dates(self):
        result, out = self.drift([('2026-08-25', -10000), ('2026-08-18', -10000), ('2026-08-11', 20000)])
        self.assertIs(result, True)
        self.assertIn('DRIFT FLAG', out)

    def test_duplicate_date_is_unknown(self):
        self.assertIs(self.drift([('2026-08-18', -10000), ('2026-08-18', -10000)])[0], False)

    def test_b0_run_stops_at_date_gap(self):
        _, out = self.drift([('2026-08-04', -5000), ('2026-08-18', -5000), ('2026-08-25', -5000)])
        self.assertNotIn('3 consecutive', out)

if __name__ == '__main__':
    unittest.main()
