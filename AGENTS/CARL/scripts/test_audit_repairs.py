"""Offline regression coverage for the October 26 file-audit repairs."""
import csv
import importlib.util
from io import StringIO
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout, redirect_stderr


def module(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + ".py"))
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


brier = module("brier_audit")
boot = module("boot")
revisions = module("revision_ledger")
thresholds = module("thresholds")


class PredictionReaderTests(unittest.TestCase):
    header = "Pred_ID\tDate_Made\tPrediction\tConfidence\tTimeframe\tStatus\tDate_Resolved\tOutcome\tInvalidation\tNotes\tInstrument\n"

    def read(self, content):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "predictions.tsv"
            path.write_text(content)
            return brier.load(path)

    def test_comment_header_and_literal_unbalanced_quote_do_not_merge_rows(self):
        rows = self.read("# Last real data refresh: 2026-10-26\n" + self.header +
                         'CRL-01\t2026-01-01\tA "literal claim\t75%\tQ1\tMISSED\t2026-03-31\tmiss\tbar\tnotes\tseries\n' +
                         'CRL-02\t2026-01-01\tB\t60%\tQ1\tCONFIRMED\t2026-03-31\thit\tbar\tnotes\tseries\n')
        self.assertEqual([r["id"] for r in rows], ["CRL-01", "CRL-02"])
        self.assertEqual([r["f_recorded"] for r in rows], [.75, .60])

    def test_unresolved_and_unscored_states_stay_excluded(self):
        content = self.header
        for i, status in enumerate(["OPEN", "STUCK", "RETIRED", "NO-VERDICT"], 1):
            content += f"CRL-{i:02}\t2026-01-01\tA\t75%\tQ1\t{status}\t\t\tbar\tnotes\tseries\n"
        self.assertEqual(self.read(content), [])

    def test_malformed_or_duplicate_rows_fail_loudly(self):
        with self.assertRaisesRegex(ValueError, "missing Pred_ID"):
            self.read("# only comments\n")
        row = "CRL-01\t2026-01-01\tA\t75%\tQ1\tMISSED\t2026-03-31\tmiss\tbar\tnotes\tseries\n"
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.read(self.header + row + row)
        with self.assertRaisesRegex(ValueError, "invalid prediction row"):
            self.read(self.header + "CRL-01\tshort\n")

    def test_live_ledger_agrees_with_raw_resolved_id_set(self):
        text = brier.DEFAULT_TSV.read_text()
        expected = {r[0] for line in text.splitlines() if not line.startswith("#")
                    and len(r := line.split("\t")) > 5 and r[5] in brier.OUTCOME}
        self.assertEqual({r["id"] for r in brier.load(brier.DEFAULT_TSV)}, expected)

    def test_fractional_outcomes_and_grouping_are_not_binary_uncertainty(self):
        forecasts, outcomes = [.1, .2, .9], [0, 0, .5]
        rel, res, unc, base = brier.decompose(forecasts, outcomes, [(0, .5), (.5, 1.01)])
        self.assertAlmostEqual(unc, sum((o - base) ** 2 for o in outcomes) / 3)
        self.assertAlmostEqual(rel - res + unc, brier.brier([.15, .15, .9], outcomes))
        self.assertNotAlmostEqual(rel - res + unc, brier.brier(forecasts, outcomes))


class RevisionWriterTests(unittest.TestCase):
    def test_quoted_prose_does_not_swallow_subsequent_events(self):
        snapshots = {
            "old": {"CRL-01": {"status": "OPEN", "conf": 75, "timeframe": "Q1", "inval": "bar", "text": 'A "literal claim'}},
            "new": {"CRL-01": {"status": "MISSED", "conf": 75, "timeframe": "Q1", "inval": "bar", "text": 'B "other claim'}},
        }
        output = StringIO()
        with patch.object(revisions, "commits", return_value=iter([("old", "2026-01-01", 'A "subject'), ("new", "2026-02-01", "B")])), \
             patch.object(revisions, "load", side_effect=snapshots.get), \
             patch.object(revisions.sys, "argv", ["revision_ledger.py"]), \
             redirect_stdout(output), redirect_stderr(StringIO()):
            revisions.main()
        rows = list(csv.DictReader(StringIO(output.getvalue()), delimiter="\t"))
        self.assertEqual([r["event"] for r in rows], ["REGISTERED", "STATUS", "TEXT"])
        self.assertEqual(rows[0]["commit_subject"], 'A "subject')
        self.assertEqual(rows[-1]["new"], 'B "other claim')


class BootLedgerTests(unittest.TestCase):
    def test_canonical_reader_is_used_and_findings_preserved(self):
        result = subprocess.CompletedProcess([], 1, "23 stale ledgers; frozen baseline exempt\n", "")
        with patch.object(boot.subprocess, "run", return_value=result) as run:
            self.assertEqual(boot.check_ledger_staleness(), ["23 stale ledgers; frozen baseline exempt"])
        args = run.call_args.args[0]
        self.assertEqual(args[1:], [str(boot.WORKSPACE / "scripts/ledger_staleness.py"), "CARL", "--quiet"])

    def test_empty_failure_and_timeout_are_not_clean(self):
        with patch.object(boot.subprocess, "run", return_value=subprocess.CompletedProcess([], 2, "", "")):
            self.assertIn("CANNOT CERTIFY", boot.check_ledger_staleness()[0])
        with patch.object(boot.subprocess, "run", side_effect=subprocess.TimeoutExpired("check", 60)):
            self.assertIn("CANNOT RUN", boot.check_ledger_staleness()[0])

    def test_filter_keeps_failure_and_attaches_only_own_section(self):
        result = boot.collapse_output("Checking Exeter REGISTERED...\nquiet\nChecking Ally...\nERROR: missing series\n")
        self.assertEqual(result, ["    Checking Ally...", "    ERROR: missing series"])


class ThresholdDisplayTests(unittest.TestCase):
    def test_oas_percentage_point_input_is_displayed_in_basis_points(self):
        self.assertEqual(thresholds.fmt_value(3.31, "BAMLH0A0HYM2"), "331.0")

    def test_missing_inputs_are_not_a_clean_no_breach_result(self):
        output = StringIO()
        with patch.object(thresholds, "get_prices", return_value={}), \
             patch.object(thresholds, "fred_fetch", return_value=[{"error": "offline test"}]), \
             patch.object(thresholds.sys, "argv", ["thresholds.py", "--json"]), redirect_stdout(output):
            rc = thresholds.main()
        import json
        result = json.loads(output.getvalue())
        self.assertEqual(rc, 1)
        self.assertTrue(result["diagnostic_only"])
        self.assertIn("SYF", result["coverage"]["missing_market"])
        self.assertIn("GASREGW", result["coverage"]["missing_fred"])

    def test_previous_close_fallback_has_unknown_quote_time(self):
        from types import SimpleNamespace
        fake = SimpleNamespace(tickers={"TEST": SimpleNamespace(info={"previousClose": 100})})
        with patch.object(thresholds.yf, "Tickers", return_value=fake):
            result = thresholds.get_prices(["TEST"])["TEST"]
        self.assertEqual(result["basis"], "previousClose fallback")
        self.assertIsNone(result["asof_utc"])


if __name__ == "__main__":
    unittest.main()
