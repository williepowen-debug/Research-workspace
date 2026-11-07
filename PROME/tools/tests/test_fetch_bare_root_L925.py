#!/usr/bin/env python3
"""L925 acceptance: bare futures roots refuse at the CLI. No network, no yfinance call."""
import contextlib
import importlib.util
import io
import pathlib
import sys
import types
import unittest
from unittest.mock import patch

PATH = pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/fetch.py"


def load():
    sys.modules.setdefault("yfinance", types.ModuleType("yfinance"))
    spec = importlib.util.spec_from_file_location("fetch_l925", PATH)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class BareRoots(unittest.TestCase):
    def setUp(self):
        self.f = load()

    def run_cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        calls = []
        with patch.object(sys, "argv", ["fetch.py", *argv]), \
             patch.object(self.f, "cmd_price", lambda a, fl: calls.append(a)), \
             contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                self.f.main()
                rc = 0
            except SystemExit as e:
                rc = e.code
        return rc, out.getvalue(), err.getvalue(), calls

    def test_every_registered_root_refuses(self):
        for root, form in self.f.FUTURES_ROOTS.items():
            rc, out, err, calls = self.run_cli("price", root)
            self.assertEqual((rc, out, calls), (2, "", []), root)
            self.assertIn(form, err)

    def test_any_case_and_mixed_list_refuse_whole(self):
        rc, out, err, calls = self.run_cli("price", "SPY", "cl")
        self.assertEqual((rc, calls), (2, []))
        self.assertIn("CL=F", err)

    def test_equity_flag_serves_as_typed(self):
        rc, _, _, calls = self.run_cli("price", "CL", "--equity")
        self.assertEqual((rc, calls), (0, [["CL"]]))

    def test_futures_forms_and_tickers_pass(self):
        for t in ("CL=F", "CLX26", "CLX26.NYM", "GCZ26.CMX", "SPY", "KRE", "VLO", "HO=F"):
            rc, _, _, calls = self.run_cli("price", t)
            self.assertEqual((rc, calls), (0, [[t]]), t)

    def test_fallback_path_refuses(self):
        rc, out, err, calls = self.run_cli("CL")
        self.assertEqual((rc, out, calls), (2, "", []))
        self.assertIn("CL=F", err)

    def test_fleet_root_pl_refuses(self):
        rc, _, err, calls = self.run_cli("price", "PL")
        self.assertEqual((rc, calls), (2, []))
        self.assertIn("PL=F", err)

    def test_decimals(self):
        d = self.f._price_decimals
        self.assertEqual(d("HO=F", 4.3359), 4)
        self.assertEqual(d("RBX26.NYM", 2.1), 4)
        self.assertEqual(d("CL=F", 95.51), 2)
        self.assertEqual(d("AAPL", 4.3359), 2)

    def test_futures_note_only_with_a_future_row(self):
        row = {"price": 4.3359, "prev": 4.3, "change_pct": 0.8, "name": "HO", "volume": 1}
        for rows, want in (({"HO=F": row}, True), ({"SPY": dict(row, price=500.0)}, False),
                           ({"HO=F": {"error": "x"}}, False)):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.f.display_prices(rows)
            self.assertEqual("10 minutes behind" in out.getvalue(), want)
            if "HO=F" in rows and "error" not in rows["HO=F"]:
                self.assertIn("4.3359", out.getvalue())


if __name__ == "__main__":
    unittest.main()
