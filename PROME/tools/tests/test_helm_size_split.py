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
            with patch.object(da, 'render_docket_page', lambda root, page_href: ('', ['boom'])):
                self.assertIsNone(wh.write_docket(out))
            self.assertFalse((Path(td) / wh.DOCKET_FILE).exists())
            with patch.object(da, 'render_docket_page', lambda root, page_href: ('<!doctype html>ok', [])):
                self.assertEqual(wh.write_docket(out), wh.DOCKET_FILE)
            self.assertEqual((Path(td) / wh.DOCKET_FILE).read_text(), '<!doctype html>ok')

    def test_wrong_owner_rows_filtered_identically_in_both_renders(self):
        rows = da.pending_work(FIX)
        self.assertTrue(all(re.search(r'\bPROME\b', r['owner']) for r in rows))
        page, _ = da.render(FIX, docket_href='docket.html')
        doc, _ = da.render_docket_page(FIX)
        self.assertEqual(len(re.findall(r"href='docket\.html#L\d+'", page)), len(rows))
        self.assertEqual(len(re.findall(r"<details id='L\d+'>", doc)), len(rows))


if __name__ == '__main__':
    unittest.main()
