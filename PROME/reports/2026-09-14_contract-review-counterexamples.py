#!/usr/bin/env python3
"""L394 independent offline review. Pass an exported fetch.py, never the live file.

Assertions express required behavior; failures are the retained review evidence.
No network, live cache, credentials, or production audit log is used.
See the sibling contract-identification-review.md for the pinned export command.
"""
import contextlib
import datetime
import importlib.util
import os
import pathlib
import sys
import tempfile
import time
import types
import unittest
from unittest.mock import patch

SOURCE = pathlib.Path(sys.argv.pop(1)).resolve()
os.environ["MKTDATA_REEXEC"] = "1"
FIXED_DATE = time.struct_time((2026, 9, 14, 12, 0, 0, 0, 257, -1))
B = 1_000_000


def metadata(symbol, price, timestamp=B, name="Brent Crude Oil Last Day Financ"):
    return dict(symbol=symbol, regularMarketPrice=price,
                regularMarketTime=timestamp, shortName=name, instrumentType="FUTURE")


class Review(unittest.TestCase):
    def setUp(self):
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        temp = pathlib.Path(self.stack.enter_context(tempfile.TemporaryDirectory()))
        # Load a copy in an isolated tree: _load_dotenv must never read live .env.
        module_path = temp / "FORGE/tools/market-data/fetch.py"
        module_path.parent.mkdir(parents=True)
        module_path.write_bytes(SOURCE.read_bytes())
        spec = importlib.util.spec_from_file_location("review_fetch", module_path)
        self.fetch = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.fetch)
        self.stack.enter_context(patch.object(self.fetch, "_audit_log"))
        self.stack.enter_context(patch.object(self.fetch.time, "localtime", return_value=FIXED_DATE))
        self.table = {
            "BZ=F": metadata("BZ=F", 100),
            "BZU26.NYM": metadata("BZU26.NYM", 100),
            "BZV26.NYM": metadata("BZV26.NYM", 101),
        }
        self.calls = []
        self.quote = 100
        owner = self

        class History:
            empty = False
            index = [datetime.datetime(2026, 9, 11), datetime.datetime(2026, 9, 14)]

            def __len__(self):
                return len(self.index)

        class Ticker:
            def __init__(self, symbol):
                self.symbol = symbol
                owner.calls.append(symbol)

            @property
            def history_metadata(self):
                return owner.table[self.symbol]

            @property
            def fast_info(self):
                if self.symbol == "BAD":
                    raise RuntimeError("fixture vendor outage")
                return dict(lastPrice=owner.quote, previousClose=99, lastVolume=10)

            def history(self, **kwargs):
                return History()

        yf = types.ModuleType("yfinance")
        yf.Ticker = Ticker
        self.stack.enter_context(patch.dict(sys.modules, {"yfinance": yf}))

    def probe(self):
        return self.fetch.contract_probe("BZ", horizon=2)

    def assert_refused(self, result):
        self.assertTrue(result["verdict"].startswith("REFUSED-"), result)

    def test_valid_distinct_control(self):
        self.assertEqual(self.probe()["verdict"], "IDENTIFIED")

    def test_known_stale_match_is_refused(self):
        self.table["BZU26.NYM"]["regularMarketTime"] = B - 10_000
        self.assertEqual(self.probe()["verdict"], "REFUSED-match-on-stale-candidate")

    def test_name_price_agreement(self):
        self.table["BZ=F"]["shortName"] = "Brent Sep 26"
        self.assertEqual(self.probe()["cross_check"], "agrees-with-vendor-name:BZU26")

    def test_name_price_disagreement(self):
        self.table["BZ=F"]["shortName"] = "Brent Oct 26"
        self.assertEqual(self.probe()["verdict"], "REFUSED-disagrees-with-vendor-name")

    def test_missing_matched_timestamp_cannot_establish_compatible_times(self):
        self.table["BZU26.NYM"].pop("regularMarketTime")
        self.assert_refused(self.probe())

    def test_missing_continuous_timestamp_cannot_establish_compatible_times(self):
        self.table["BZ=F"].pop("regularMarketTime")
        self.assert_refused(self.probe())

    def test_wrong_matched_symbol_cannot_identify_requested_contract(self):
        self.table["BZU26.NYM"]["symbol"] = "CLV26.NYM"
        self.assert_refused(self.probe())

    def test_wrong_continuous_symbol_cannot_identify_requested_root(self):
        self.table["BZ=F"]["symbol"] = "CL=F"
        self.assert_refused(self.probe())

    def test_nonfinite_quote_is_not_a_second_control_price(self):
        for invalid in (float("nan"), float("inf")):
            with self.subTest(price=repr(invalid)):
                self.table["BZV26.NYM"]["regularMarketPrice"] = invalid
                self.assert_refused(self.probe())

    def test_partial_cache_retries_do_not_renew_old_successful_quote(self):
        clock = [10_000]
        self.stack.enter_context(patch.object(self.fetch.time, "time", side_effect=lambda: clock[0]))
        ttl = self.fetch._cache_ttl("prices_BAD_BZ=F")
        first = self.fetch.price_fetch(["BZ=F", "BAD"])
        self.assertEqual(first["BZ=F"]["price"], 100)
        self.assertIn("error", first["BAD"])
        self.quote = 110
        clock[0] += ttl - 1
        self.fetch.price_fetch(["BZ=F", "BAD"])
        clock[0] += ttl - 1
        result = self.fetch.price_fetch(["BZ=F", "BAD"])
        self.assertIn("error", result["BAD"])
        self.assertEqual(result["BZ=F"]["price"], 110,
                         f"quote exceeds its original TTL; calls={self.calls}; result={result}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
