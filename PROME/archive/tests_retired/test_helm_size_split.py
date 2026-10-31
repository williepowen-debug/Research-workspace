"""ACCEPTANCE_helm_size_split_2026-10-03 — the Helm page keeps one line per pending PROME
docket row and links each to its full record in a supporting file; nothing lost, no link
dangling, legacy output byte-stable, and a page never links a file that was not written."""
import html
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import desk_attention as da  # noqa: E402
import will_handbook as wh  # noqa: E402

FIX = Path(__file__).resolve().parent / 'fixtures' / 'desk_attention'


class HelmSizeSplitTests(unittest.TestCase):

    def test_p1_no_loss_same_rows_in_page_and_file_with_every_cell_verbatim(self):
        rows = da.pending_work(FIX)
        self.assertTrue(rows, 'fixture must carry pending PROME rows')
        page, errors = da.render(FIX, docket_href='docket.html')
        doc, derrs = da.render_docket_page(FIX, page_href='https://example.invalid/helm')
        self.assertEqual((errors, derrs), ([], []))
        sec = page[page.find("<section id='prome-work'>"):]
        sec = sec[:sec.find('</section>')]
        ids_page = {int(x) for x in re.findall(r"href='docket\.html#L(\d+)'", sec)}
        ids_doc = {int(x) for x in re.findall(r"<details id='L(\d+)'>", doc)}
        self.assertEqual({r['line'] for r in rows}, ids_page)
        self.assertEqual(ids_page, ids_doc)
        for r in rows:
            for cell in ('title', 'state', 'next', 'evidence', 'owner'):
                self.assertIn(html.escape(r[cell]), doc, f"L{r['line']} {cell} not verbatim in docket page")
        # the page itself no longer carries the heavy cells
        self.assertNotIn('Recorded state:', sec)
        self.assertIn(f"{len(rows)} rows", sec)

    def test_p2_every_link_resolves_and_file_is_a_complete_document(self):
        page, _ = da.render(FIX, docket_href='docket.html')
        doc, _ = da.render_docket_page(FIX, page_href='https://example.invalid/helm')
        for frag in re.findall(r"href='docket\.html(#L\d+)?'", page):
            if frag:
                self.assertIn(f"<details id='{frag[1:]}'>", doc, f'dangling {frag}')
        self.assertTrue(doc.startswith('<!doctype html>'))
        for needle in ('<meta charset="utf-8">', 'name="viewport"', '<title>', 'background:var(--ground)',
                       'prefers-color-scheme:dark', ':root[data-theme="dark"]', 'https://example.invalid/helm'):
            self.assertIn(needle, doc)

    def test_p3_lines_stay_readable_in_both_files(self):
        page, _ = da.render(FIX, docket_href='docket.html')
        doc, _ = da.render_docket_page(FIX)
        self.assertLessEqual(max(len(l.encode()) for l in doc.split('\n')), 10_000)
        self.assertLessEqual(max(len(l.encode()) for l in page.split('\n')), 10_000)
        # the heavy cells never share a line in the file: one row per line, one cell per line inside it
        self.assertNotIn('</p><p>', doc)

    def test_p5_legacy_mode_is_byte_stable_in_either_call_order(self):
        a, ea = da.render(FIX)
        b, eb = da.render(FIX, docket_href='docket.html')
        c, ec = da.render(FIX)
        self.assertEqual(a, c)                       # a split render leaves no state behind (overlap)
        self.assertEqual((ea, eb, ec), ([], [], []))
        self.assertIn('Recorded state:', a)          # legacy carries every cell on the page …
        self.assertNotIn('docket.html', a)           # … and links nothing
        rows = da.pending_work(FIX)
        for r in rows:                               # the legacy row string is exactly the old one
            self.assertIn(da._work_row_full(r), a)
        self.assertNotEqual(a, b)

    def test_p6_docket_error_means_no_link_and_no_file(self):
        def boom(root=da.ROOT, today=None):
            raise ValueError('DOCKET L9: unparseable pending date')
        with patch.object(da, 'pending_work', boom):
            page, errors = da.render(FIX, docket_href='docket.html')
            self.assertIn('DOCKET L9: unparseable pending date', errors)
            self.assertNotIn('docket.html', page)
            self.assertNotIn("<section id='prome-work'>", page)
            doc, derrs = da.render_docket_page(FIX)
            self.assertEqual((doc, derrs), ('', ['DOCKET L9: unparseable pending date']))
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / 'handbook.html'
            wh.ALERTS.clear()
            with patch.object(da, 'render_docket_page', lambda root, page_href, work=None: ('', ['boom'])):
                self.assertIsNone(wh.write_docket(out, []))
            self.assertFalse((Path(td) / wh.DOCKET_FILE).exists())
            self.assertTrue(any(label == 'docket' and 'boom' in reason for label, reason in wh.ALERTS), wh.ALERTS)
            wh.ALERTS.clear()
            with patch.object(da, 'render_docket_page', lambda root, page_href, work=None: ('<!doctype html>ok', [])):
                self.assertEqual(wh.write_docket(out, []), wh.DOCKET_FILE)
            self.assertEqual((Path(td) / wh.DOCKET_FILE).read_text(), '<!doctype html>ok')

    def test_wrong_owner_rows_filtered_identically_in_both_renders(self):
        rows = da.pending_work(FIX)
        self.assertTrue(all(re.search(r'\bPROME\b', r['owner']) for r in rows))
        page, _ = da.render(FIX, docket_href='docket.html')
        doc, _ = da.render_docket_page(FIX)
        self.assertEqual(len(re.findall(r"href='docket\.html#L\d+'", page)), len(rows))
        self.assertEqual(len(re.findall(r"<details id='L\d+'>", doc)), len(rows))


class HelmSnapshotTests(unittest.TestCase):
    """Episode 2 (CATO C-1/C-2): one docket snapshot for both renders; a failed snapshot is retained."""

    def setUp(self):
        wh.ALERTS.clear()
        self._real = da.pending_work

    def tearDown(self):
        da.pending_work = self._real
        wh.ALERTS.clear()

    def _run(self, td):
        out = Path(td) / 'handbook.html'
        with patch.object(sys, 'argv', ['will_handbook.py', '-o', str(out), '--no-feed']):
            import io, contextlib
            with contextlib.redirect_stdout(io.StringIO()):
                rc = wh.main()
        page = out.read_text(encoding='utf-8')
        dk = Path(td) / wh.DOCKET_FILE
        return rc, page, (dk.read_text(encoding='utf-8') if dk.exists() else None)

    def test_q1_one_snapshot_so_a_row_appended_between_reads_reaches_neither_output(self):
        real, calls = self._real, []
        def drift(root=da.ROOT, today=None):
            calls.append(1)
            rows = real(root, today)
            if len(calls) >= 2:   # a writer between two reads — the race CATO found
                rows = rows + [dict(line=99999, due='2026-10-03', title='appended between reads', owner='PROME',
                                    state='PENDING', evidence='', next='', timing='TODAY')]
            return rows
        da.pending_work = drift
        with tempfile.TemporaryDirectory() as td:
            rc, page, dk = self._run(td)
        self.assertEqual(len(calls), 1, 'the docket must be read exactly once per render')
        self.assertIsNotNone(dk)
        links = {int(x) for x in re.findall(r"href='docket\.html#L(\d+)'", page)}
        ids = {int(x) for x in re.findall(r"<details id='L(\d+)'>", dk)}
        self.assertEqual(links, ids)
        self.assertNotIn('L99999', page); self.assertNotIn("id='L99999'", dk)

    def test_q2_a_failed_snapshot_is_retained_as_review_even_if_a_later_read_would_succeed(self):
        real, calls = self._real, []
        def flaky(root=da.ROOT, today=None):
            calls.append(1)
            if len(calls) == 1:
                raise ValueError('DOCKET L9: unparseable pending date')
            return real(root, today)
        da.pending_work = flaky
        with tempfile.TemporaryDirectory() as td:
            rc, page, dk = self._run(td)
        self.assertEqual(rc, 1, 'a failed snapshot must return REVIEW')
        self.assertTrue(any(label == 'docket' and 'unparseable pending date' in reason for label, reason in wh.ALERTS), wh.ALERTS)
        self.assertIsNone(dk, 'no supporting file on a failed snapshot')
        self.assertNotIn("href='docket.html", page)
        self.assertNotIn("<section id='prome-work'>", page)
        self.assertIn('unparseable pending date', page, 'the page carries the error')
        self.assertEqual(len(calls), 1, 'no second read may rescue the run')

    def test_q2b_an_error_with_an_empty_message_is_still_a_failure(self):
        for exc in (ValueError(), OSError()):
            real, calls = self._real, []
            def flaky(root=da.ROOT, today=None, exc=exc):
                calls.append(1)
                if len(calls) == 1:
                    raise exc
                return real(root, today)
            da.pending_work = flaky; wh.ALERTS.clear()
            with tempfile.TemporaryDirectory() as td:
                rc, page, dk = self._run(td)
            self.assertEqual(rc, 1, type(exc).__name__)
            self.assertTrue(any(label == 'docket' and type(exc).__name__ in reason for label, reason in wh.ALERTS), wh.ALERTS)
            self.assertIsNone(dk); self.assertNotIn("href='docket.html", page)
            self.assertEqual(len(calls), 1, 'no second read may rescue the run')


if __name__ == '__main__':
    unittest.main()
