#!/usr/bin/env python3
"""DOCKET L546 — float-tie class in FORGE market-data classification.

The list comes from PROME/tools/tests/ACCEPTANCE_L546_float_tie_classify_2026-10-08.md,
written before the code, NOT from the reported symptom. Category 3 (wrong owner) is
justified N/A there: this fix touches FORGE's classify only; desk letters keep their own
tie handling.

The PRE-FIX reference implementations are kept inline (``_classify_prefix``,
``_steep_label_prefix``) so AC5's "the old code is seen to fail first" is executable,
not remembered. Modules under test are imported by path (the directory name has a hyphen).
Run: python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_l546_float_tie.py
"""
import datetime as dt
import importlib.util
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
MD = ROOT / "FORGE/tools/market-data"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, MD / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


config = _load("config")
vix = _load("vix_futures")


# ---------------------------------------------------------------- pre-fix references
def _classify_prefix(value, series_def):
    """Verbatim shape of config.classify before L546 (raw float vs edges)."""
    if value is None:
        return "unknown"
    y = series_def["yellow"]
    r = series_def["red"]
    if series_def["direction"] == "higher_worse":
        if value < y[0]:
            return "green"
        elif value < r[0]:
            return "yellow"
        return "red"
    if value > y[1]:
        return "green"
    elif value >= y[0]:
        return "yellow"
    return "red"


def _steep_label_prefix(pct):
    """Verbatim shape of vix_futures' local classify before L546 (unrounded pct)."""
    if pct < 0:
        return "BACKWARDATION"
    if pct < vix.AVG_STEEPNESS:
        return "BELOW_AVG"
    if pct < vix.COMPLACENCY_THRESHOLD:
        return "NORMAL_TO_ELEVATED"
    return "COMPLACENCY_TOP_30PCT"


def _bp_series(edge_y, edge_r, precision=0):
    """Synthetic higher_worse series in bp with a declared precision (FRED pct ×100)."""
    d = {
        "name": f"SYN {edge_y}/{edge_r}",
        "source": "fred",
        "direction": "higher_worse",
        "green": (None, edge_y),
        "yellow": (edge_y, edge_r),
        "red": (edge_r, None),
        "multiply": 100,
    }
    if precision is not None:
        d["precision"] = precision
    return d


# Hundredths whose ×100 lands BELOW the integer in binary (the false-all-clear direction
# under classify's `<`): 1.13, 1.14, 1.15, 1.16, 2.01, 2.03, 2.05, 2.07 (WALTER 10/8).
DOWN_TIES = [(1.13, 113), (2.01, 201)]
# LIQUID's cases land ABOVE the integer (1.10→110.00000000000001, 2.20→220.00000000000003).
UP_TIES = [(1.10, 110), (2.20, 220)]


class TestAC5_OldCodeFailsFirst(unittest.TestCase):
    """CHECK_STANDARD: the defect is induced on the pre-fix reference and seen to fire."""

    def test_prefix_classify_lands_on_the_mild_side_of_a_down_tie(self):
        for pct, edge in DOWN_TIES:
            s = _bp_series(edge - 50, edge)
            self.assertNotEqual(pct * 100, edge, "fixture must be a real binary tie")
            self.assertEqual(_classify_prefix(pct * 100, s), "yellow",
                             f"{pct}*100 should have mis-landed below {edge} on the old code")

    def test_prefix_steepness_label_disagrees_with_published_number(self):
        pct = (13.20 - 12.50) / 12.50 * 100
        self.assertNotEqual(pct, 5.6)
        self.assertEqual(_steep_label_prefix(pct), "BELOW_AVG")
        self.assertEqual(round(pct, 3), 5.6)  # the number the JSON publishes says "at average"


class TestAC1_OnEdgeEqualsTheLetter(unittest.TestCase):
    """A converted value mathematically ON an edge classifies into the edge's zone."""

    def test_down_ties_classify_as_the_edge_zone(self):
        for pct, edge in DOWN_TIES:
            s = _bp_series(edge - 50, edge)
            self.assertEqual(config.classify(pct * 100, s), "red", f"{pct}*100 ON red edge {edge}")

    def test_up_ties_still_classify_as_the_edge_zone(self):
        # Correct side under `<` even before the fix (direction of the binary error); kept as regression.
        for pct, edge in UP_TIES:
            s = _bp_series(edge - 50, edge)
            self.assertEqual(config.classify(pct * 100, s), "red", f"{pct}*100 ON red edge {edge}")

    def test_yellow_edge_tie(self):
        s = _bp_series(113, 300)
        self.assertEqual(config.classify(1.13 * 100, s), "yellow")
        self.assertEqual(config.classify(1.12 * 100, s), "green")


class TestAC2_MissingPrecisionIsLoud(unittest.TestCase):
    """`multiply` without `precision` is a declared defect; nothing is silently rounded."""

    def test_classify_without_precision_compares_raw(self):
        s = _bp_series(63, 113, precision=None)
        self.assertNotIn("precision", s)
        # unchanged (pre-fix) behaviour on the raw float — the hole stays VISIBLE, not papered over
        self.assertEqual(config.classify(1.13 * 100, s), _classify_prefix(1.13 * 100, s))

    def test_every_live_multiply_series_declares_precision(self):
        missing = [s["name"] for s in config.SERIES if "multiply" in s and "precision" not in s]
        self.assertEqual(missing, [], f"multiply without precision: {missing}")

    def test_selftest_helper_names_the_missing_series(self):
        self.assertTrue(hasattr(config, "undeclared_precision"), "config.undeclared_precision() missing")
        fake = [{"name": "A", "multiply": 100}, {"name": "B", "multiply": 100, "precision": 0}, {"name": "C"}]
        self.assertEqual(config.undeclared_precision(fake), ["A"])


class TestAC3_LabelMatchesPublishedNumber(unittest.TestCase):
    """compute_steepness classifies the same 3-dp value it publishes."""

    @staticmethod
    def _contracts(m1, m2, m3=None, as_of=dt.date(2026, 10, 8)):
        out = [
            {"symbol": "M1", "price": m1, "expiration": as_of + dt.timedelta(days=40)},
            {"symbol": "M2", "price": m2, "expiration": as_of + dt.timedelta(days=70)},
        ]
        if m3 is not None:
            out.append({"symbol": "M3", "price": m3, "expiration": as_of + dt.timedelta(days=100)})
        return out, as_of

    def test_exact_average_tie_labels_at_average_not_below(self):
        contracts, as_of = self._contracts(12.50, 13.20)
        r = vix.compute_steepness(contracts, as_of)
        self.assertEqual(r["strict"]["steepness_pct"], 5.6)
        self.assertEqual(r["strict"]["classification"], "NORMAL_TO_ELEVATED")

    def test_adjusted_leg_uses_the_rounded_value_too(self):
        as_of = dt.date(2026, 10, 8)
        contracts = [
            {"symbol": "M1", "price": 12.0, "expiration": as_of + dt.timedelta(days=2)},  # inside roll window
            {"symbol": "M2", "price": 12.50, "expiration": as_of + dt.timedelta(days=30)},
            {"symbol": "M3", "price": 13.20, "expiration": as_of + dt.timedelta(days=60)},
        ]
        r = vix.compute_steepness(contracts, as_of)
        self.assertEqual(r["adjusted"]["steepness_pct"], 5.6)
        self.assertEqual(r["adjusted"]["classification"], "NORMAL_TO_ELEVATED")

    def test_label_and_number_never_straddle_an_edge(self):
        for m1, m2 in [(12.50, 13.20), (18.75, 19.80), (20.0, 21.12), (15.0, 16.3485)]:
            contracts, as_of = self._contracts(m1, m2)
            r = vix.compute_steepness(contracts, as_of)
            n, label = r["strict"]["steepness_pct"], r["strict"]["classification"]
            expect = ("BACKWARDATION" if n < 0 else "BELOW_AVG" if n < vix.AVG_STEEPNESS
                      else "NORMAL_TO_ELEVATED" if n < vix.COMPLACENCY_THRESHOLD else "COMPLACENCY_TOP_30PCT")
            self.assertEqual(label, expect, f"{m1}/{m2}: number {n} vs label {label}")


class TestAC4_NoLiveGradeMoves(unittest.TestCase):
    """At every CURRENT FORGE edge (read dynamically), on/below/above classify as before."""

    def test_current_edges_unchanged(self):
        for s in config.SERIES:
            if "multiply" not in s:
                continue
            mult = s["multiply"]
            edges = [e for pair in (s["green"], s["yellow"], s["red"]) for e in pair if e is not None]
            for edge in sorted(set(edges)):
                for pct in (edge / mult - 0.01, edge / mult, edge / mult + 0.01):
                    v = pct * mult
                    self.assertEqual(config.classify(v, s), _classify_prefix(round(v, s["precision"]), s),
                                     f"{s['name']} pct={pct} v={v}")


class TestNeighbours(unittest.TestCase):
    def test_overlap_rounding_is_idempotent(self):
        for pct, _ in DOWN_TIES + UP_TIES:
            v = pct * 100
            self.assertEqual(round(round(v, 0), 0), round(v, 0))

    def test_ordinary_live_prints(self):
        hy = next(s for s in config.SERIES if s["name"] == "HY OAS")
        self.assertEqual(config.classify(3.09 * 100, hy), "red")
        self.assertEqual(config.classify(2.60 * 100, hy), "green")
        kre = next(s for s in config.SERIES if s["name"] == "KRE")
        self.assertNotIn("multiply", kre)
        self.assertEqual(config.classify(75, kre), "green")

    def test_concurrent_intake_twin_agrees_on_edge_handling(self):
        # WALTER's Research-Intake patch stores round(pct*100) (integer bp). Same convention as precision 0.
        for pct in (1.13, 2.01, 2.70, 3.09):
            self.assertEqual(round(pct * 100), round(pct * 100, 0))
            self.assertEqual(float(str(round(pct * 100))), round(pct * 100, 0))


if __name__ == "__main__":
    unittest.main()
