#!/usr/bin/env python3
"""L394 regression suite: original independent counterexamples plus neighbours.

Run directly or through unittest. FETCH_REVIEW_SOURCE optionally selects an
exported fetch.py revision. Every test loads an isolated copy and fake yfinance;
no assertion uses live cache, credentials, market data, or audit logs.
"""
import contextlib
import datetime
import importlib.util
import io
import json
import os
import pathlib
import sys
import tempfile
import time
import types
import unittest
from unittest.mock import patch

SOURCE = pathlib.Path(os.environ.get("FETCH_REVIEW_SOURCE", str(
    pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/fetch.py"
))).resolve()
FIXED_DATE = time.struct_time((2026, 9, 14, 12, 0, 0, 0, 257, -1))
B = 1_000_000


def metadata(symbol, price, timestamp=B, name="Brent Crude Oil Last Day Financ"):
    return dict(symbol=symbol, regularMarketPrice=price,
                regularMarketTime=timestamp, shortName=name, instrumentType="FUTURE")


class ContractRepairs(unittest.TestCase):
    def setUp(self):
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(patch.dict(os.environ, {
            "MKTDATA_REEXEC": "1", "FRED_API_KEY": "offline-fixture-only"
        }))
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
        self.errors = {"BAD"}
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
                if self.symbol in owner.errors:
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


    def test_complete_cache_hit_does_not_refetch(self):
        first = self.fetch.price_fetch("BZ=F")
        self.quote = 110
        self.assertEqual(self.fetch.price_fetch("BZ=F"), first)
        self.assertEqual(self.calls, ["BZ=F"])

    def test_partial_cache_recovery_refreshes_all_members(self):
        self.fetch.price_fetch(["BZ=F", "BAD"])
        self.quote = 110
        self.errors.clear()
        recovered = self.fetch.price_fetch(["BZ=F", "BAD"])
        self.assertEqual(set(recovered), {"BZ=F", "BAD"})
        self.assertTrue(all(row["price"] == 110 for row in recovered.values()))
        before_calls = list(self.calls)
        self.assertEqual(self.fetch.price_fetch(["BZ=F", "BAD"]), recovered)
        self.assertEqual(self.calls, before_calls)

    def test_legacy_cached_error_is_retried(self):
        self.fetch._cache_path("prices_BZ=F").write_text(json.dumps({
            "ts": time.time(), "val": {"BZ=F": {"error": "legacy failure"}}
        }))
        self.assertEqual(self.fetch.price_fetch("BZ=F")["BZ=F"]["price"], 100)
        self.assertEqual(self.calls, ["BZ=F"])

    def test_repeated_failures_keep_cli_error_exit(self):
        for _ in range(3):
            result = self.fetch.price_fetch(["BZ=F", "BAD"])
            self.assertEqual(set(result), {"BZ=F", "BAD"})
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                self.fetch._exit_on_fetch_errors("fixture", price_results=result)
            self.assertEqual(error.exception.code, 3)

    def test_missing_or_wrong_symbols_on_every_leg(self):
        for leg in self.table:
            original = self.table[leg]["symbol"]
            for value in (None, "", " ", "WRONG", 123, False):
                with self.subTest(leg=leg, value=value):
                    self.table[leg]["symbol"] = value
                    result = self.probe()
                    self.assert_refused(result)
                    if leg != "BZ=F":
                        self.assertIn("metadata-symbol-", result["dropped"][leg])
            self.table[leg]["symbol"] = original

    def test_symbol_normalization_only_case_and_whitespace(self):
        for leg in self.table:
            self.table[leg]["symbol"] = " " + leg.lower() + " "
        self.assertEqual(self.probe()["verdict"], "IDENTIFIED")

    def test_invalid_continuous_and_matched_timestamps_refuse(self):
        for leg in ("BZ=F", "BZU26.NYM"):
            for value in (None, 0, -1, False, "bad", [], float("nan"), float("inf"),
                          B + 0.5, "1000000.00000000001"):
                with self.subTest(leg=leg, value=repr(value)):
                    self.table[leg]["regularMarketTime"] = value
                    self.assert_refused(self.probe())
            self.table[leg]["regularMarketTime"] = B

    def test_unknown_nonmatched_timestamp_is_explicitly_advisory(self):
        self.table["BZV26.NYM"]["regularMarketTime"] = None
        result = self.probe()
        self.assertEqual(result["verdict"], "IDENTIFIED")
        self.assertIsNone(result["candidate_age_s"]["BZV26.NYM"])
        self.assertIn("unknown-candidate-times", result["control"])

    def test_stale_threshold_boundary_is_unchanged(self):
        for age, expected in ((900, "IDENTIFIED"), (901, "REFUSED-match-on-stale-candidate")):
            with self.subTest(age=age):
                self.table["BZU26.NYM"]["regularMarketTime"] = B - age
                self.assertEqual(self.probe()["verdict"], expected)

    def test_invalid_prices_on_every_leg_refuse_without_crashing(self):
        for leg in self.table:
            original = self.table[leg]["regularMarketPrice"]
            for value in (None, "bad", [], {}, True, float("nan"), float("inf"), "-inf"):
                with self.subTest(leg=leg, value=repr(value)):
                    self.table[leg]["regularMarketPrice"] = value
                    self.assert_refused(self.probe())
            self.table[leg]["regularMarketPrice"] = original

    def test_zero_negative_and_numeric_string_prices_are_valid(self):
        for value in (0, -20, "100"):
            with self.subTest(value=value):
                self.table["BZ=F"]["regularMarketPrice"] = value
                self.table["BZU26.NYM"]["regularMarketPrice"] = value
                self.assertEqual(self.probe()["verdict"], "IDENTIFIED")

    def test_invalid_candidate_drops_without_poisoning_valid_control(self):
        self.table["BZX26.NYM"] = metadata("BZX26.NYM", 102)
        for key, value in (("symbol", "WRONG"), ("regularMarketPrice", float("nan"))):
            with self.subTest(key=key):
                self.table["BZV26.NYM"] = metadata("BZV26.NYM", 101)
                self.table["BZV26.NYM"][key] = value
                result = self.fetch.contract_probe("BZ", horizon=3)
                self.assertEqual(result["verdict"], "IDENTIFIED")
                self.assertIn("BZV26.NYM", result["dropped"])
                self.assertNotIn("BZV26.NYM", result["candidates"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
