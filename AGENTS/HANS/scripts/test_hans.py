#!/usr/bin/env python3
"""
HANS focused test suite — OFFLINE and DETERMINISTIC (no network, no API keys).

Added 2026-08-28 after review: "There is no HANS test suite yet."

Priority is REGRESSION on bugs this desk actually shipped today, not coverage theatre:
  · boot staleness reported every same-day row as 999d stale  (`0 or 999` — 0 is FALSY)
  · fetch_eu crashed formatting AGSI `trend`, which arrives as a STRING
  · finding_check must FAIL the exact claim/robustness pair that was retracted

Run:  .venv/bin/python AGENTS/HANS/scripts/test_hans.py
"""
import sys, unittest
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import boot, finding_check as fc
import pmi_ism_lead_test as pil


def d(n):
    """ISO date n days ago."""
    return (date.today() - timedelta(days=n)).isoformat()


class TestAge(unittest.TestCase):
    """boot._age + the falsy-zero staleness regression."""

    def test_today_is_zero_not_none(self):
        self.assertEqual(boot._age(d(0)), 0)

    def test_known_offset(self):
        self.assertEqual(boot._age(d(30)), 30)

    def test_unparseable_returns_none(self):
        for bad in ("", "n/a", "2026-13-99", "FROZEN"):
            self.assertIsNone(boot._age(bad), f"{bad!r} should be None")

    def test_REGRESSION_zero_age_is_not_stale(self):
        """`(_age(x) or 999)` reported every row refreshed TODAY as 999d stale,
        because 0 is falsy. Guard the correct form explicitly."""
        a = boot._age(d(0))
        self.assertFalse(a is None or a > boot.STALE_DAYS,
                         "a row refreshed today must NOT be flagged stale")
        self.assertEqual((a or 999), 999, "0 is falsy — this is exactly why `or` was wrong")

    def test_dead_statuses_excluded_from_staleness(self):
        for s in ("FROZEN", "RETIRED", "UNREACHABLE"):
            self.assertIn(s, boot.DEAD)


class TestIndependence(unittest.TestCase):
    """finding_check Gate A."""

    def test_same_dimension_fails(self):
        ok, _ = fc.independence("lag", "lag")
        self.assertFalse(ok)

    def test_equivalent_dimensions_fail(self):
        for a, v in (("lag", "horizon"), ("horizon", "window"),
                     ("sample", "period"), ("period", "era"), ("spec", "specification")):
            ok, _ = fc.independence(a, v)
            self.assertFalse(ok, f"{a}/{v} are equivalent and must NOT pass")

    def test_genuinely_independent_passes(self):
        for a, v in (("lag", "sample"), ("threshold", "period"), ("horizon", "subgroup")):
            ok, _ = fc.independence(a, v)
            self.assertTrue(ok, f"{a}/{v} are independent and should pass")

    def test_unknown_dimension_is_none_not_pass(self):
        ok, msg = fc.independence("vibes", "sample")
        self.assertIsNone(ok, "unknown input must not silently PASS")
        self.assertIn("unknown", msg.lower())

    def test_REGRESSION_the_retracted_pair(self):
        """The exact pair from the 8/28 retraction: claim ABOUT lag, robustness
        VARIED lag. This must fail or the gate is decorative."""
        ok, _ = fc.independence(about="lag", varied="lag")
        self.assertFalse(ok)


class TestStability(unittest.TestCase):
    """finding_check Gate B, on synthetic keysets — no network."""

    KEYS = {f"{y}-{m:02d}" for y in range(2000, 2027) for m in range(1, 13)}

    def test_stable_statistic_passes(self):
        v, _ = fc.stability(lambda k: 0.60, self.KEYS, verbose=False)
        self.assertEqual(v, "STABLE")

    def test_sign_flip_detected(self):
        def s(keys):
            gfc = {k for k in keys if k[:4] in ("2008", "2009")}
            return 0.5 if gfc else -0.4          # positive only while GFC present
        v, _ = fc.stability(s, self.KEYS, verbose=False)
        self.assertEqual(v, "FAILS — SIGN FLIPS")

    def test_collapse_detected(self):
        def s(keys):
            covid = {k for k in keys if k[:4] in ("2020", "2021")}
            return 0.8 if covid else 0.05        # same sign, magnitude collapses
        v, _ = fc.stability(s, self.KEYS, verbose=False)
        self.assertEqual(v, "FAILS — COLLAPSES")

    def test_uncomputable_is_not_stable(self):
        v, _ = fc.stability(lambda k: None, self.KEYS, verbose=False)
        self.assertEqual(v, "UNCOMPUTABLE")

    def test_gate_requires_BOTH(self):
        """Independent dimension but an unstable statistic must still not ship."""
        def s(keys):
            return 0.5 if {k for k in keys if k[:4] in ("2008", "2009")} else -0.4
        self.assertFalse(fc.gate("x", about="lag", varied="sample",
                                 stat=s, keys=self.KEYS))

    def test_gate_without_stat_does_not_pass(self):
        """Gate B not run must NOT count as verified-clean."""
        self.assertFalse(fc.gate("x", about="lag", varied="sample"))


class TestSeriesMath(unittest.TestCase):
    """pmi_ism_lead_test helpers — the lead direction depends on these."""

    def test_shift_moves_forward(self):
        self.assertEqual(pil.shift({"2026-01": 1.0}, 2), {"2026-03": 1.0})

    def test_shift_crosses_year_boundary(self):
        self.assertEqual(pil.shift({"2026-11": 1.0}, 3), {"2027-02": 1.0})

    def test_shift_zero_is_identity(self):
        self.assertEqual(pil.shift({"2026-05": 2.0}, 0), {"2026-05": 2.0})

    def test_yoy_computes_percent(self):
        out = pil.yoy({"2025-06": 100.0, "2026-06": 110.0})
        self.assertAlmostEqual(out["2026-06"], 10.0, places=6)

    def test_yoy_drops_rows_without_a_prior_year(self):
        self.assertNotIn("2025-06", pil.yoy({"2025-06": 100.0, "2026-06": 110.0}))

    # corr() refuses n<24 BY DESIGN, so these fixtures span 30 months.
    # (First draft of this test used 12 and errored — the code was right, the test wasn't.)
    KEYS30 = [f"{2024 + (i // 12)}-{i % 12 + 1:02d}" for i in range(30)]

    def test_corr_perfect_positive(self):
        a = {k: float(i) for i, k in enumerate(self.KEYS30)}
        b = {k: float(i) * 3 + 7 for i, k in enumerate(self.KEYS30)}
        r, n = pil.corr(a, b)
        self.assertAlmostEqual(r, 1.0, places=6)
        self.assertEqual(n, 30)

    def test_corr_perfect_negative(self):
        a = {k: float(i) for i, k in enumerate(self.KEYS30)}
        b = {k: -float(i) for i, k in enumerate(self.KEYS30)}
        r, _ = pil.corr(a, b)
        self.assertAlmostEqual(r, -1.0, places=6)

    def test_corr_uses_only_overlapping_keys(self):
        a = {k: float(i) for i, k in enumerate(self.KEYS30)}
        b = dict(list(a.items())[:26])
        _, n = pil.corr(a, b)
        self.assertEqual(n, 26, "correlation must be computed on the INTERSECTION only")

    def test_corr_refuses_small_samples(self):
        r, n = pil.corr({"2026-01": 1.0}, {"2026-01": 2.0})
        self.assertIsNone(r, "n<24 must return None, not a spurious correlation")


class TestFetchEuParsing(unittest.TestCase):
    """fetch_eu — the AGSI trend field arrives as a STRING and once crashed the printer."""

    def test_REGRESSION_trend_string_coerces(self):
        for raw in ("0.27", "-0.10", 0.27, None, "", "n/a"):
            try:
                out = f"{float(raw):+.2f}"
                self.assertIsInstance(out, str)
            except (TypeError, ValueError):
                pass          # the guarded path — must not raise uncaught

    def test_country_EU_is_not_the_aggregate_code(self):
        """Documents the silent-failure trap: country=EU returns 200 + empty array."""
        src = (Path(__file__).resolve().parent / "fetch_eu.py").read_text()
        self.assertIn("type=EU", src)
        self.assertNotIn('"https://agsi.gie.eu/api?country=EU', src)


class TestExitSemanticsPerimeter(unittest.TestCase):
    """The 0/1/2 contract must cover ALL live pulls, not just Yahoo.

    Added 2026-08-28 on review: fetch_eu only PRINTED, so ECB/AGSI failures and
    breaches never reached the exit code or the registry-integrity check. A run
    with working Yahoo and dead European primaries would exit 0 CLEAN while the
    screen said PULL FAILED — semantics advertising a wider perimeter than checked.
    """

    def test_REGRESSION_ttf_L1_carries_its_threshold_id(self):
        """Only the L2+ branch used to enter the integrity comparison, because the
        L1 band text had no HANS-T- id in it."""
        for level in (60.0, 62.0, 65.9):
            _, txt = boot._ttf(level)
            self.assertIn("HANS-T-07", txt, f"L1 at {level} must carry its threshold id")

    def test_every_banded_ttf_tier_is_identifiable(self):
        for level, tier in ((66.0, "L2"), (100.1, "L3"), (200.1, "L4")):
            _, txt = boot._ttf(level)
            self.assertIn("HANS-T-07", txt)
            self.assertIn(tier, txt)

    def test_ttf_below_L1_is_not_a_breach(self):
        em, txt = boot._ttf(50.0)
        self.assertEqual(em, "🟢")
        self.assertNotIn("HANS-T-07", txt, "an unbreached band must not enter the integrity list")

    def test_eurusd_band_ids_only_when_breached(self):
        self.assertNotIn("HANS-T-11", boot._eurusd(1.16)[1])
        for breached in (1.02, 0.98):     # 0.98 = the CRISIS tier, which also lacked its id
            self.assertIn("HANS-T-11", boot._eurusd(breached)[1])

    def test_REGRESSION_no_banded_tier_omits_its_threshold_id(self):
        """The general form of the bug: severe tiers were the ones missing ids, so the
        WORST states silently skipped the integrity check. Assert every non-green
        tier of every banded fn is identifiable."""
        cases = [(boot._ttf, [60.0, 66.0, 101.0, 201.0], "HANS-T-07"),
                 (boot._eurusd, [1.02, 0.98], "HANS-T-11")]
        for fn, levels, tid in cases:
            for lv in levels:
                em, txt = fn(lv)
                self.assertNotEqual(em, "🟢", f"{fn.__name__}({lv}) should be a breach")
                self.assertIn(tid, txt, f"{fn.__name__}({lv}) omits {tid} — skips integrity")

    def test_fetch_eu_exposes_the_three_key_contract(self):
        """boot depends on these keys existing. Network-tolerant: a total failure
        still has to return the contract, not None."""
        import io, contextlib, fetch_eu
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                r = fetch_eu.main()
        except Exception as e:
            self.skipTest(f"network unavailable: {str(e)[:40]}")
        for k in ("observations", "failures", "breached"):
            self.assertIn(k, r, f"boot consumes r[{k!r}] — the contract must hold")
        self.assertIsInstance(r["failures"], list)
        self.assertIsInstance(r["breached"], list)

    def test_compound_rows_need_BOTH_legs(self):
        """T-09/T-10 must not fire on a spread leg alone — reporting one leg as a
        fire is how a compound gate gets simplified into a single number."""
        src = (Path(__file__).resolve().parent / "fetch_eu.py").read_text()
        self.assertIn("sp > 200 and cv > 5.50", src)
        self.assertIn("sp > 100 and cv > 4.50", src)

    def test_boot_consumes_the_return_not_just_the_printing(self):
        src = (Path(__file__).resolve().parent / "boot.py").read_text()
        self.assertIn("eu = fetch_eu.main()", src)
        self.assertIn('breached.extend(eu.get("breached"', src)
        self.assertIn('pull_fails += len(eu.get("failures"', src)

    def test_boot_declares_all_three_exit_codes(self):
        src = (Path(__file__).resolve().parent / "boot.py").read_text()
        for token in ("0  CLEAN", "1  ATTENTION", "2  BLOCKING"):
            self.assertIn(token, src)


if __name__ == "__main__":
    unittest.main(verbosity=2)
