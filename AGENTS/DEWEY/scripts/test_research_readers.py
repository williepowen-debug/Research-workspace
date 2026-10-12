"""Offline regressions for scoped evidence reads and gas-window integrity.

Run: .venv/bin/python3 AGENTS/DEWEY/scripts/test_research_readers.py
No source calls; the GIE fixture is the frozen October12 primary archive.
"""

import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch


HERE = Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


edgar = load("edgar_doc")
gie = load("gie_pull")
pdf = load("pdf2text")
with patch.dict(os.environ, {"FRED_API_KEY": "synthetic-sweep-key"}):
    fred = load("fred_pull")


class ReaderRegression(unittest.TestCase):
    def test_multiexhibit_cannot_certify_absence_from_first_document(self):
        names = {"q2fy27pr.htm": 100000, "q2fy27cfocommentary.htm": 2000}
        with patch.object(edgar, "list_documents", return_value=names):
            with self.assertRaisesRegex(edgar.EdgarError, "q2fy27cfocommentary"):
                edgar.doc_text("1045810", "0001045810-26-000073")

    def test_json_omission_is_recovered_from_html_including_inline_viewer(self):
        wrapper = json.dumps({"directory": {"item": [
            {"name": "0001045810-26-000073-index.html", "size": "100"},
            {"name": "R1.htm", "size": "200"}]}}).encode()
        html = (b'<a href="/Archives/edgar/data/1045810/acc/q2fy27pr.htm">PR</a>'
                b'<a href="/ix?doc=/Archives/edgar/data/1045810/acc/q2fy27cfocommentary.htm">CFO</a>')
        with patch.object(edgar, "_get", side_effect=[wrapper, html]):
            names = edgar.list_documents("1045810", "0001045810-26-000073")
        self.assertIn("q2fy27pr.htm", names)
        self.assertIn("q2fy27cfocommentary.htm", names)

    def test_unread_html_index_is_not_complete_json_listing(self):
        wrapper = b'{"directory":{"item":[{"name":"R1.htm"}]}}'
        with patch.object(edgar, "_get", side_effect=[wrapper, edgar.EdgarError("unavailable")]):
            with self.assertRaisesRegex(edgar.EdgarError, "JSON index alone"):
                edgar.list_documents("1045810", "0001045810-26-000073")

    def test_single_document_ignores_generated_wrappers(self):
        names = {"abc-index.html": 9000, "R1.htm": 60000, "report.htm": 4000}
        with patch.object(edgar, "list_documents", return_value=names):
            self.assertEqual(edgar._primary_doc("1", "abc"), "report.htm")

    def test_scoped_miss_and_positive_secondary_exhibit_are_distinct(self):
        for name, text, expected in [("q2fy27pr.htm", "Earnings press release", 1),
                                     ("q2fy27cfocommentary.htm", "primarily related to the procurement of memory", None)]:
            out, err = io.StringIO(), io.StringIO()
            argv = ["edgar_doc.py", "doc", "--cik", "1045810", "--accession", "acc", "--doc", name, "--grep", "memory"]
            with patch.object(edgar.sys, "argv", argv), patch.object(edgar, "doc_text", return_value=(name, text)), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                try:
                    rc = edgar.main()
                except SystemExit as error:
                    rc = error.code
            self.assertEqual(rc, expected)
            self.assertIn("this document only", out.getvalue())
            if expected == 1:
                self.assertIn(name, err.getvalue())

    def test_context_strip_preserves_narrative(self):
        clean, dropped = edgar.strip_xbrl("0001045810 2026-01-25 us-gaap:CommonStockMember xbrli:shares\n46,751 39,721 37,608 12,443\nRevenue includes memory purchases")
        self.assertEqual(dropped, 1)
        self.assertIn("memory purchases", clean)
        self.assertIn("46,751 39,721 37,608 12,443", clean)

    def gas_rows(self):
        path = HERE.parent / "research/2026-10-12_dr4/agsi-2026.json"
        data = json.loads(path.read_text())
        return sorted(data, key=lambda r: r["gasDayStart"], reverse=True)[:15]

    def refill(self, rows):
        args = SimpleNamespace(country=None, key=None, window=14, target=80.0, peak="2026-11-01")
        out = io.StringIO()
        with patch.object(gie, "_rows", return_value=rows), contextlib.redirect_stdout(out):
            gie.cmd_refill(args)
        return out.getvalue()

    def test_frozen_gie_series_reproduces_report_from_unsorted_rows(self):
        text = self.refill(list(reversed(self.gas_rows())))
        self.assertIn("2.131 TWh/d", text)
        self.assertIn("77.8%", text)
        self.assertIn("not a verified peak", text)
        self.assertNotIn("achievable", text)

    def test_missing_or_duplicate_gas_dates_do_not_certify_pace(self):
        rows = self.gas_rows()
        for bad in [rows[:-1], rows[:5] + rows[6:], rows[:-1] + [rows[-2]]]:
            with self.subTest(days=len(bad)), self.assertRaisesRegex(gie.GieError, "consecutive gas days"):
                self.refill(bad)

    def test_missing_stock_cannot_be_used_in_projection(self):
        rows = [dict(r) for r in self.gas_rows()]
        rows[-1]["gasInStorage"] = "-"
        with self.assertRaisesRegex(gie.GieError, "finite"):
            self.refill(rows)

    def test_empty_or_malformed_gas_records_are_source_failures(self):
        rows = [dict(r) for r in self.gas_rows()]
        rows[0]["gasDayStart"] = "not-a-date"
        for bad in [[], rows]:
            with self.subTest(records=len(bad)), self.assertRaises(gie.GieError):
                self.refill(bad)

    def test_zero_window_rejected_before_source_call(self):
        argv = ["gie_pull.py", "refill", "--window", "0"]
        with patch.object(gie.sys, "argv", argv), patch.object(gie, "_rows") as source, contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                gie.main()
        self.assertEqual(error.exception.code, 2)
        source.assert_not_called()

    def test_pdf_text_miss_warns_that_images_were_not_searched(self):
        for text in ["", "Slide title only"]:
            err = io.StringIO()
            with patch.object(pdf.sys, "argv", ["pdf2text.py", "fixture.pdf", "--grep", "delinquency"]), patch.object(pdf, "extract", return_value=text), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
                self.assertEqual(pdf.main(), 1)
            self.assertIn("images/charts have not been searched", err.getvalue())

    def test_documented_pdf_literal_statistic_does_not_crash(self):
        with patch.object(pdf.sys, "argv", ["pdf2text.py", "fixture.pdf", "--grep", "+18.8"]), patch.object(pdf, "extract", return_value="uncapped +18.8%"), contextlib.redirect_stdout(io.StringIO()):
            self.assertIsNone(pdf.main())

    def test_zero_overlap_fred_splice_does_not_claim_validation(self):
        with patch.object(fred, "archive_fetch", return_value=([{"date": "2020-01-01", "value": "1"}], {})), patch.object(fred, "fetch", return_value=[{"date": "2023-01-01", "value": "2"}]):
            _, _, note = fred.splice_fetch("SYNTHETIC")
        self.assertIn("NOT validated", note)
        self.assertNotIn("ALL MATCH", note)


if __name__ == "__main__":
    unittest.main(verbosity=2)
