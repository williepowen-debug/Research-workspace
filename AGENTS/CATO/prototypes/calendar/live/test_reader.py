import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace

import reader

TODAY = date(2026, 10, 31)
SOURCES = json.loads((reader.HERE / 'fixtures.json').read_text())['sources']


class CalendarTests(unittest.TestCase):
    def test_dates_preserve_windows_unknown_and_estimates(self):
        self.assertEqual(reader.timing('2026-11-02 → 2026-11-06', TODAY), ('2026-11-02', '2026-11-06', 'window'))
        self.assertEqual(reader.timing('~2026-11-02', TODAY)[2], 'uncertain')
        self.assertEqual(reader.timing('2026-02-30', TODAY)[2], 'uncertain')
        self.assertEqual(reader.timing('after the owner returns', TODAY)[2], 'undated')
        self.assertEqual(reader.timing('2026-10-29', TODAY)[2], 'overdue')

    def test_real_economic_window_and_time_semantics(self):
        events, _ = reader.economic(SOURCES[reader.ECON], TODAY)
        fomc = next(e for e in events if e['title'].startswith('FOMC'))
        self.assertEqual((fomc['date'], fomc['end']), ('2026-10-27', '2026-10-28'))
        jobs = next(e for e in events if 'NFP' in e['title'])
        self.assertEqual((jobs['date'], jobs['time']), ('2026-11-06', '08:30'))
        multiple = next(e for e in events if 'Durable goods; new' in e['title'])
        self.assertEqual(multiple['time'], '')
        beyond = next(e for e in events if 'Thanksgiving' in e['title'])
        self.assertEqual(beyond['lane'], 'uncertain')
        self.assertEqual(beyond['date'], '')

    def test_stale_source_is_not_refreshed_by_reading(self):
        _, notes = reader.economic(SOURCES[reader.ECON], date(2026, 11, 20))
        self.assertTrue(any(n.startswith('STALE:') for n in notes))
        with self.assertRaises(ValueError):
            reader.economic(SOURCES[reader.ECON].replace('Window verified:', 'Missing:'), TODAY)

    def test_real_catalyst_schemas_keep_full_rows(self):
        for path, text in SOURCES.items():
            if not path.endswith('CATALYSTS.tsv'):
                continue
            rows, errors = reader.catalysts(path, text, path.split('/')[1], TODAY)
            self.assertFalse(errors)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]['sources'][0]['excerpt'], text.splitlines()[1])
            self.assertEqual(rows[0]['sources'][0]['sha256'], reader.digest(text))

    def test_malformed_rows_are_reported_without_losing_good_rows(self):
        path = 'AGENTS/LABOR/docket/CATALYSTS.tsv'
        rows, errors = reader.catalysts(path, SOURCES[path] + 'broken\trow\n', 'LABOR', TODAY)
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(errors), 1)

    def test_moved_source_date_and_inline_date_class_are_preserved(self):
        path = 'AGENTS/VIOLET/workbook/CATALYSTS.tsv'
        old, _ = reader.catalysts(path, SOURCES[path], 'VIOLET', TODAY)
        new, _ = reader.catalysts(path, SOURCES[path].replace('2026-11-06\t', '2026-11-09\t'), 'VIOLET', TODAY)
        self.assertEqual(old[1]['confidence'], 'SECONDARY')
        self.assertEqual((old[1]['date'], new[1]['date']), ('2026-11-06', '2026-11-09'))
        self.assertEqual(old[1]['note'], new[1]['note'])

    def test_terminal_gate_annotation_not_treated_as_live(self):
        text = 'gate_id\tstate\treview_by\towner\tcondition\nG1\tRESOLVED(TERMINAL — test)\t2026-11-02\tTEST\tx\nG2\tLIVE / NOT ARMED — test\t2026-11-03 (set 2026-10-01)\tTEST\ty\n'
        rows, errors = reader.gates(text, TODAY)
        self.assertFalse(errors)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['date'], '2026-11-03')
        self.assertIn('not a forecast', rows[0]['note'])

    def test_registry_is_parsed_without_execution(self):
        value = reader.registry("raise RuntimeError('must not run')\nSUMMONS_LEDGERS={'LABOR':'AGENTS/LABOR/docket/CATALYSTS.tsv'}")
        self.assertIn('LABOR', value)
        with self.assertRaises(ValueError):
            reader.registry("SUMMONS_LEDGERS = dict(LABOR='anything')")

    def test_export_hash_race_refuses_instead_of_showing_mismatched_rows(self):
        payload = {'schema': 'spawn_list.open', 'version': 1, 'as_of': TODAY.isoformat(), 'source_sha256': '0' * 64, 'rows': [], 'count': 0}
        with patch.object(reader.subprocess, 'run', return_value=SimpleNamespace(returncode=0, stdout=json.dumps(payload))):
            with self.assertRaisesRegex(ValueError, 'changed during read'):
                reader.docket(reader.ROOT, 'new source bytes', TODAY)

    def test_missing_sources_are_visible_not_a_successful_empty_calendar(self):
        with tempfile.TemporaryDirectory() as folder:
            result = reader.snapshot(Path(folder), TODAY)
            self.assertEqual(result['events'], [])
            self.assertTrue(all(s['status'] == 'unavailable' for s in result['coverage']))

    def test_changed_reviewed_context_is_not_reused(self):
        preview = json.loads((reader.HERE.parent / 'week-sketch/snapshot.json').read_text())
        saved = preview['events'][0]
        texts = {s['path']: s['excerpt'] for s in saved['sources']}
        source = saved['sources'][0]
        base = reader.event(source['path'], texts[source['path']], 1, source['excerpt'], 'Source title', 'TEST', saved['date'], 'unclassified', TODAY)
        joined, _ = reader.enrich([base], texts, TODAY)
        self.assertEqual(joined[0]['id'], saved['id'])
        texts[saved['sources'][-1]['path']] += ' changed'
        texts[saved['sources'][-1]['path']] = 'replaced row'
        changed, notes = reader.enrich([base], texts, TODAY)
        self.assertEqual(changed, [base])
        self.assertTrue(notes)

    def test_path_escape_is_refused(self):
        with self.assertRaises(ValueError):
            reader.read(reader.ROOT, '../.ssh/config')


if __name__ == '__main__':
    unittest.main()
