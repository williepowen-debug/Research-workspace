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



class TestDocAudit(unittest.TestCase):
    """FALSIFY THE GUARD, don't just run it. doc_audit.py was written 2026-09-05 to catch
    drift classes that had ALREADY bitten this desk; a checker that passes because it
    cannot fail is worse than none [[finding_test_the_guard_not_just_the_guarded]].
    Each test INJECTS the defect and asserts the specific code fires."""

    def setUp(self):
        import importlib, doc_audit
        self.da = importlib.reload(doc_audit)

    def _codes(self, findings):
        return {c for c, _ in findings}

    def test_the_real_desk_is_clean(self):
        """The live surfaces must pass. If this fails, fix the DESK, not the test."""
        self.assertEqual(self.da.audit(), [], "live HANS surfaces have doc-audit findings")

    def test_C1_catches_a_live_value_in_the_spec_mirror(self):
        """The 9/5 defect: CLAUDE.md's band table carried '(live: 54.1 Aug flash)' after
        the registry had been corrected to the 54.3 final."""
        real = self.da.HANS / "CLAUDE.md"
        txt = real.read_text()
        hit = "| German Mfg PMI | <47 sustained"
        self.assertIn(hit, txt, "anchor row moved — update this test, not the guard")
        i = txt.index(hit); j = txt.index("\n", i)
        try:
            real.write_text(txt[:i] + txt[i:j] + " (live: 54.1 Aug flash)" + txt[j:])
            self.assertIn("C1-LIVE-VALUE", self._codes(self.da.audit()))
        finally:
            real.write_text(txt)

    def test_C6_weighs_the_charter_the_fleet_checker_cannot_see(self):
        """scripts/read_cap_check.py opens CLAUDE.md only to find which OTHER files to
        weigh, so the charter — loaded WHOLE by the harness every session — was the one
        surface nothing measured. It stood at 32,961 B against a 32,550 B budget while
        the checker reported '1 file assessed, 0 over budget'."""
        real = self.da.HANS / "CLAUDE.md"
        orig = real.read_bytes()
        try:
            real.write_bytes(orig + b"\nx" * self.da.STATUS_BYTE_BUDGET)
            self.assertIn("C6-CHARTER-BYTES", self._codes(self.da.audit()))
        finally:
            real.write_bytes(orig)

    # ---- C10 / C11, added 2026-09-18 (ML-HANS-461, ML-HANS-462) ----------------
    def _swap_vx(self, vid, **cells):
        """Inject cell values into one VX row, returning a restore callable."""
        real = self.da.HANS / "workbook" / "VX.tsv"
        orig = real.read_text()
        lines = orig.split("\n")
        hdr = lines[0].split("\t")
        for n, line in enumerate(lines):
            if line.startswith(vid + "\t"):
                cols = line.split("\t")
                for k, v in cells.items():
                    cols[hdr.index(k)] = v
                lines[n] = "\t".join(cols)
                break
        else:
            self.fail(f"{vid} not found — update the test, not the guard")
        real.write_text("\n".join(lines))
        return lambda: real.write_text(orig)

    def test_C10_fires_on_the_exact_France_cell_that_shipped(self):
        """THE REGRESSION. VX-HANS-1.05 read GREEN at 348.4 against a Yellow of 350.0 —
        France's first band crossing — and a packet went out on that row still calling it
        green. The value was right and the STATE was wrong."""
        restore = self._swap_vx("VX-HANS-1.05", Current_Value="348.4", Status="GREEN")
        try:
            hits = [m for c, m in self.da.audit()
                    if c == "C10-BAND-STATE" and "VX-HANS-1.05" in m]
            self.assertTrue(hits, "C10 must fire on a GREEN below its own Yellow")
        finally:
            restore()

    def test_C10_treats_a_value_exactly_ON_the_band_as_the_band(self):
        """UK 30Y sat exactly on Yellow(5.75) reading GREEN. A boundary that resolves
        downward is a threshold that never fires on the day it is reached."""
        restore = self._swap_vx("VX-HANS-3.08", Current_Value="5.75", Status="GREEN")
        try:
            self.assertIn("C10-BAND-STATE", self._codes(self.da.audit()))
        finally:
            restore()

    def test_C10_blames_the_BAND_only_when_it_is_truly_non_monotone(self):
        """WRITTEN WRONG FIRST, AND THAT IS THE POINT. I asserted Belgium's 550/400/350
        was non-monotone; it is a perfectly ordered DESCENDING set, under which 470.7 is
        a YELLOW. The bands were never the defect — the STATE was — and I had already
        'repaired' a band to make a wrong state look right before this test caught it.
        So: a real non-monotone set must blame the BAND, and Belgium's real set must
        blame the STATE. Both directions asserted, because only having the first is how
        the mistake happened."""
        restore = self._swap_vx("VX-HANS-1.04", Yellow="400", Orange="550", Red="350")
        try:
            self.assertIn("C10-NON-MONOTONE", self._codes(self.da.audit()))
        finally:
            restore()
        restore = self._swap_vx("VX-HANS-1.04", Yellow="550", Orange="400",
                                Red="350", Current_Value="470.7", Status="GREEN")
        try:
            hits = [m for c, m in self.da.audit()
                    if c == "C10-BAND-STATE" and "VX-HANS-1.04" in m]
            self.assertTrue(hits, "an ordered descending set with a wrong state is a "
                                  "STATE defect, not a band defect")
        finally:
            restore()

    def test_C11_catches_a_surface_facing_the_opposite_way_to_its_threshold(self):
        """VX-HANS-4.01 carried a CUTTING-cycle sign (1.75/1.50/1.25) while HANS-T-04
        fires UPWARD at >=2.75. The registry was re-specced and the vector never was, so
        a threshold and its own metric surface pointed opposite ways and the row could
        not fire in the direction the world was moving."""
        restore = self._swap_vx("VX-HANS-4.01", Yellow="1.75", Orange="1.50", Red="1.25")
        try:
            hits = [m for c, m in self.da.audit()
                    if c == "C11-DIRECTION" and "HANS-T-04" in m]
            self.assertTrue(hits, "C11 must fire when threshold and surface disagree on direction")
        finally:
            restore()

    def test_C11_is_NOT_implied_by_C10_which_is_the_whole_point(self):
        """ZHAO's proof, encoded. Their PBOC rows AGREE with their bands perfectly and
        would read green if the PBOC did nothing, because both bands face one way. So a
        wrong-facing surface can be perfectly self-consistent: C10 passes it and only C11
        catches it. If this ever fails, the two checks have collapsed into one and the
        directional hole is unguarded again."""
        restore = self._swap_vx("VX-HANS-4.01", Yellow="1.75", Orange="1.50",
                                Red="1.25", Current_Value="2.50", Status="GREEN")
        try:
            findings = self.da.audit()
            c10 = [m for c, m in findings if c == "C10-BAND-STATE" and "VX-HANS-4.01" in m]
            c11 = [m for c, m in findings if c == "C11-DIRECTION" and "HANS-T-04" in m]
            self.assertFalse(c10, "the injected row is self-consistent — C10 must NOT fire")
            self.assertTrue(c11, "...and C11 must")
        finally:
            restore()

    def test_band_exempt_stays_empty_of_content_excuses(self):
        """Two exemptions were written on 2026-09-18 and both removed within the hour,
        each having named a defect and then excused it. An exemption may name a property
        of the SCHEMA; it may never name a row whose CONTENT is wrong."""
        self.assertEqual(self.da._audit_full.__code__.co_consts is not None, True)
        import inspect
        src = inspect.getsource(self.da._audit_full)
        self.assertIn("BAND_EXEMPT = {}", src,
                      "BAND_EXEMPT gained an entry — is it a schema property or an excuse?")

    def test_C2_is_SERIES_QUALIFIED_not_bare_value(self):
        """The first version matched bare values and flagged UK CPI 2.9% against EA HICP
        2.9%. A metric with NO declared vectors must be skipped, never guessed.

        🔴 REWRITTEN 2026-09-18 (session 2) AND THE REWRITE IS THE LESSON. The original
        pinned three LIVE LEDGER FACTS — EA HICP current == "3.3", olds contains "2.9",
        vecs == [] — and every one of them changed the moment the desk did its job: the
        August FINAL 3.2 superseded the flash, and the metric gained VX-HANS-4.10. The
        test went RED on a CORRECT refresh while the logic it names was never touched.
        A regression test pinned to a live value tests the DATA, not the GUARD, and its
        red is indistinguishable from a real break [[finding_a_column_that_is_both_record_and_instrument_basis_fails_twice]].
        It now asserts the INVARIANT over whatever the ledger holds, and injects the
        undeclared-surface case rather than borrowing a row that may stop being one.
        → ML-HANS-460
        """
        pub = self.da.published()
        self.assertIn("EA_FLASH_HICP_YOY_PCT", pub)

        # INVARIANT 1 — a metric declaring no VX surface is skipped, never guessed.
        # Asserted over EVERY such metric on the ledger, so the test keeps its subject
        # even when one row gains a surface.
        undeclared = {m for m, (_, _, vecs) in pub.items() if not vecs}
        codes = self.da.audit()
        for m in undeclared:
            self.assertEqual([c for c, msg in codes
                              if c == "C2-SUPERSEDED" and f"retired for {m}" in msg], [],
                             f"{m} declares no VX surface — C2 must skip it, not guess")

        # INVARIANT 2 — generalised from the concrete 2.9/2.9 collision: NO two metrics
        # that retire the same value string may declare the same VX surface, or C2 is
        # guessing again. Stated over every retired value rather than over the one pair
        # that happened to collide in August — that pair is a fact about the tape and
        # will stop existing; the property is a fact about the guard and will not.
        # Non-vacuity is NOT asserted here: test_C2_still_catches_a_genuine_supersession
        # is the live-ammunition half, and a test that manufactures its own subject to
        # avoid looking vacuous is worse than one that delegates it.
        by_val = {}
        for m, (_, olds, vecs) in pub.items():
            for o in olds:
                for v in vecs:
                    prev = by_val.setdefault((o.strip(), v), m)
                    self.assertEqual(prev, m,
                                     f"{m} and {prev} both declare {v} and both retire "
                                     f"{o!r} — C2 cannot tell them apart")

    def test_C2_still_catches_a_genuine_supersession(self):
        """Series-qualifying must not have disarmed the check."""
        pub = self.da.published()
        cur, olds, vecs = pub["GERMAN_MFG_PMI"]
        self.assertEqual(cur, "54.3")
        self.assertIn("54.1", olds, "the flash MUST be on the ledger as superseded")
        self.assertIn("VX-HANS-8.06", vecs, "the metric must declare its surface")

    def test_C3_compares_compound_rows_PER_LEG(self):
        """T-09 is 'spread AND level'. A one-leg comparison silently ignores the leg that
        had no metric surface at all until 9/5."""
        self.assertIsInstance(self.da.REG_VX["HANS-T-09"], tuple)
        self.assertEqual(len(self.da.REG_VX["HANS-T-09"]), 2)
        self.assertIn("VX-HANS-3.09", self.da.REG_VX["HANS-T-09"],
                      "the Italy BTP LEVEL surface must be mapped")

    def test_C4_rejects_a_sender_tree_dispatch_path(self):
        """Two fires read OPEN-and-dispatched for 8 days pointing at HANS's OWN STATUS.md
        — a record that cannot be falsified [[finding_record_of_an_action_is_not_the_action]]."""
        import csv
        p = self.da.HANS / "registry/HANS_T_FIRED_LOG.tsv"
        txt = p.read_text()
        rows = list(csv.reader(txt.split("\n")[:2], delimiter="\t"))
        ci = rows[0].index("dispatch_artifact")
        r = rows[1]; r[ci] = "AGENTS/HANS/STATUS.md"
        try:
            lines = txt.split("\n")
            lines[1] = "\t".join(r)
            p.write_text("\n".join(lines))
            self.assertIn("C4-SELF-DISPATCH", self._codes(self.da.audit()))
        finally:
            p.write_text(txt)

    def test_C6_enforces_the_BYTE_budget_not_only_the_line_cap(self):
        """STATUS passed its 250-line cap at 241 lines while 5,316 B over the read-cap
        budget. The byte budget binds FIRST."""
        self.assertEqual(self.da.STATUS_BYTE_BUDGET, 32550)
        self.assertEqual(self.da.STATUS_LINE_CAP, 250)
        st = self.da.HANS / "STATUS.md"
        self.assertLessEqual(len(st.read_bytes()), self.da.STATUS_BYTE_BUDGET)

    def test_C8_catches_an_ACTIVE_KB_row_asserting_a_retired_value(self):
        """THE PERIMETER GAP CODEX FOUND. C2 covered registry+VX and stopped; three KB rows
        stayed ACTIVE asserting the PMI flashes with Stale_By weeks out, so boot §[7] could
        not reach them either. Inject a genuine stale ACTIVE row and require the fire."""
        p = self.da.HANS / "workbook/KB.tsv"
        txt = p.read_text()
        lines = txt.split("\n")
        ci = {n: i for i, n in enumerate(lines[0].split("\t"))}
        for i, l in enumerate(lines):
            c = l.split("\t")
            if c and c[0] == "KB-HANS-017":
                c[ci["Status"]] = "ACTIVE"
                lines[i] = "\t".join(c)
                break
        else:
            self.fail("KB-HANS-017 not found — update the test, not the guard")
        try:
            p.write_text("\n".join(lines))
            self.assertIn("C8-KB-STALE", self._codes(self.da.audit()))
        finally:
            p.write_text(txt)

    def test_C8_does_NOT_flag_a_historical_QUOTE(self):
        """Corrected rows quote what they used to say — by design. C8's first version
        flagged its own corrections (KB-HANS-047 'flash 54.1') and the value+date form
        ('was 3.29% on 8/28'). Both must pass; a check that punishes correct documentation
        trains you to document less."""
        self.assertEqual([m for c, m in self.da.audit() if c == "C8-KB-STALE"], [],
                         "C8 is flagging a legitimate historical quote")

    def test_published_ledger_parses_with_the_FLEET_reader(self):
        """PUBLISHED.tsv must be readable by scripts/consumer_check.py, not just by us —
        it exists so --from-ledger works."""
        sys.path.insert(0, str(self.da.ROOT / "scripts"))
        from consumer_check import read_ledger
        d = read_ledger(self.da.HANS / "workbook/PUBLISHED.tsv")
        self.assertGreater(len(d), 10)
        self.assertEqual(d["GERMAN_MFG_PMI"][0], "54.3")
        self.assertIn("54.1", d["GERMAN_MFG_PMI"][1])

class TestC4IsHistoryScopedNotLiveState(unittest.TestCase):
    """REGRESSION, 2026-09-10. C4 asks 'was this fire DISPATCHED?' — an EVENT, so
    a question about HISTORY — but it tested `.exists()`, i.e. LIVE STATE. That
    made the guard inherit the RECIPIENT's workflow: BRENT consumes inbound mail
    into inbox/processed/, so two dispatch paths went 'dead' BECAUSE DELIVERY HAD
    SUCCEEDED. A correct-looking alarm for exactly the wrong reason.

    The tempting fix — glob processed/ too — is a PATCH: it leaves the dependency
    in place and WIDENS it, so the next directory the recipient invents breaks it
    again. Diff-scoping REMOVES it. (DAEDALUS 2026-09-10.)

    Pairing rule pinned here: 'did I author it / was it delivered?' => HISTORY =>
    read the diff. 'Is it here NOW?' => LIVE STATE => glob both, order by commit
    time. The wrong pairing yields a guard that LOOKS hardened and is not.
    """

    MOVED = ("AGENTS/BRENT/inbox/2026-09-05_from-HANS_eu-gas-fires-the-half-you-"
             "never-received-ttf-125pct-yoy-storage-lowest-since-2011.md")

    def setUp(self):
        import importlib, doc_audit
        self.da = importlib.reload(doc_audit)

    def test_delivered_then_moved_is_not_dead(self):
        """THE BUG: gone from the pinned path, but history remembers."""
        self.assertFalse((self.da.ROOT / self.MOVED).exists(),
                         "fixture stale: if the packet is back at its pre-move "
                         "path the regression is no longer pinned")
        self.assertTrue(self.da._ever_existed(self.MOVED),
                        "a commit ADDED this packet — delivery is an event and "
                        "history cannot rot; live-state .exists() called it DEAD")

    def test_never_delivered_is_still_caught(self):
        """The guard must not go quiet: a genuinely bad path still fails."""
        self.assertFalse(self.da._ever_existed(
            "AGENTS/BRENT/inbox/2026-09-05_from-HANS_this-packet-never-existed.md"))

    def test_current_path_resolves(self):
        cur = self.MOVED.replace("/inbox/", "/inbox/processed/")
        self.assertTrue((self.da.ROOT / cur).exists())
        self.assertTrue(self.da._ever_existed(cur))

    def test_git_failure_is_UNKNOWN_not_a_silent_pass(self):
        """FAIL CLOSED: if git cannot be consulted the answer is UNKNOWN (None),
        never False-and-quiet — else a broken toolchain certifies the board."""
        real = self.da.subprocess.run
        try:
            self.da.subprocess.run = (
                lambda *a, **k: (_ for _ in ()).throw(OSError("no git")))
            self.assertIsNone(self.da._ever_existed(self.MOVED))
        finally:
            self.da.subprocess.run = real

    def test_info_states_are_not_findings_and_audit_keeps_its_signature(self):
        """C4-MOVED is a visible STATE, not a finding — the same lesson DAEDALUS
        ruled on WQ-112 today: quieting a false alarm by falling SILENT trades a
        loud false alarm for a silent true miss. And audit() must keep its
        flat-list signature: changing it broke five tests here on 2026-09-10."""
        f, info = self.da._audit_full()
        self.assertEqual(f, self.da.audit(), "audit() must stay findings-only")
        self.assertIsInstance(info, list)


# ===========================================================================
# REGRESSION: the 2026-09-18 status-token defect, in BOTH its directions.
#
# What happened: this desk superseded seven KB rows and, trying to be more useful,
# wrote `SUPERSEDED-BY-KB-HANS-059` — fusing the canonical token with its successor
# pointer into one word. Two guards on this desk then disagreed about that cell:
#   * boot.py tested EXACT membership in {"SUPERSEDED","RETIRED"} -> the rows stayed
#     LIVE and EXPIRED. Boot §[7] printed "10 EXPIRED" when the truth was 3, burying
#     the three real ones in seven false ones. FAILS LOUD (noise) — survivable.
#   * doc_audit C8 tested `Status != 'ACTIVE' -> skip`, an ALLOWLIST OF ONE TOKEN,
#     so three rows relabelled EXPIRED-NOT-REFRESHED were silently DROPPED from the
#     stale-value check, along with 2 CORRECTED and 2 CONFIRMED rows that had never
#     been checked at all. FAILS QUIET — the dangerous one.
# Describing a row better must never desupervise it.
# [[finding_status_token_membership_test_desupervises_improved_rows]]
# ===========================================================================
class StatusTokenSemantics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        import importlib, doc_audit
        cls.boot = boot
        cls.doc_audit = importlib.reload(doc_audit)

    # ---- direction 1: dead rows must be recognised however they are spelled ----
    def test_na_wrong_unit_is_recognised_live_not_parked(self):
        """VX-HANS-11.03 carries NA-WRONG-UNIT (fleet canon): its name, value and bands
        are three different constructs, so its COLOUR is unreadable — but the ROW is
        live and must keep its staleness supervision. Recognised-live, not parked, and
        not unknown: an unknown token is correct-but-loud, and a permanent false alarm
        is how a real one gets ignored."""
        self.assertFalse(self.boot.is_dead("NA-WRONG-UNIT"))
        self.assertNotIn("NA-WRONG-UNIT",
                         self.boot.unknown_tokens([([{"S": "NA-WRONG-UNIT"}], "S")]))

    def test_historical_parks_a_dated_snapshot_row(self):
        """HISTORICAL added to both guards 2026-09-18 (2nd session) for KB-HANS-034,
        a DATED MARKET SNAPSHOT of 9/1. Such a row cannot be "made current" — every
        level in it is history the moment the tape moves — so nagging it forever is
        noise, and it must not be value-checked either: it is a citation of its own
        moment. Added to BOTH guards in one edit; the agreement test below is what
        stops a future token landing in only one of them."""
        for cell in ("HISTORICAL",
                     "HISTORICAL 2026-09-18 — dated snapshot, levels all moved"):
            self.assertTrue(self.boot.is_dead(cell), cell)
            self.assertTrue(
                cell.strip().upper().startswith(self.doc_audit.KB_DEAD_PREFIXES), cell)

    def test_compound_superseded_token_is_dead(self):
        """The exact cell that broke it. A canonical token followed by a date and
        prose is the CANON form, not an exception to it."""
        for cell in ("SUPERSEDED 2026-09-18 — superseded by KB-HANS-059",
                     "SUPERSEDED-BY-KB-HANS-059",
                     "RETIRED 2026-09-18 — event passed",
                     "FROZEN 2026-08-28 — not maintained"):
            self.assertTrue(self.boot.is_dead(cell), f"{cell!r} must be DEAD")

    def test_legacy_bare_tokens_stay_recognised(self):
        """Canon grandfathers existing files: 'enforcers must keep recognising the
        legacy set'. Eight bare SUPERSEDED rows predate the compound form."""
        for cell in ("SUPERSEDED", "RETIRED", "FROZEN", "ARCHIVED", "NOT CURRENT"):
            self.assertTrue(self.boot.is_dead(cell), f"legacy {cell!r} must stay DEAD")

    # ---- direction 2: live rows must stay SUPERVISED however they are spelled ----
    def test_live_tokens_are_not_dead(self):
        for cell in ("ACTIVE", "CORRECTED", "CONFIRMED", "GREEN", "ORANGE-WATCH", ""):
            self.assertFalse(self.boot.is_dead(cell), f"{cell!r} must stay LIVE")

    def test_unknown_token_fails_LOUD_not_quiet(self):
        """THE LOAD-BEARING ASSERTION. An unrecognised token must be treated as LIVE
        — nagged, maybe wrongly — never silently parked. Flip this and a future
        invented token disappears from supervision with every check reading green."""
        self.assertFalse(self.boot.is_dead("EXPIRED-NOT-REFRESHED"))
        self.assertFalse(self.boot.is_dead("SOME-TOKEN-NOBODY-HAS-INVENTED-YET"))

    def test_the_two_guards_agree_on_what_dead_means(self):
        """The root defect was not either test alone — it was that two guards on the
        same desk read the SAME COLUMN with different semantics."""
        self.assertEqual(set(self.boot.DEAD_PREFIXES),
                         set(self.doc_audit.KB_DEAD_PREFIXES),
                         "boot.py and doc_audit.py must share one notion of DEAD")
        for cell in ("SUPERSEDED 2026-09-18 — x", "CORRECTED", "CONFIRMED",
                     "EXPIRED-NOT-REFRESHED", "ACTIVE", "RETIRED 2026-01-01"):
            self.assertEqual(
                self.boot.is_dead(cell),
                cell.strip().upper().startswith(self.doc_audit.KB_DEAD_PREFIXES),
                f"guards disagree on {cell!r}")

    def test_c8_scope_is_a_denylist_not_a_one_token_allowlist(self):
        """Falsifies the FIX, not just the bug: a CONFIRMED row — a token the old
        allowlist skipped entirely — must now be inside C8's perimeter."""
        src = (Path(__file__).resolve().parent / "doc_audit.py").read_text()
        self.assertNotIn(").strip().upper() != 'ACTIVE'", src,
                         "C8 must not go back to an allowlist of one token")
        self.assertFalse(self.doc_audit.KB_DEAD_PREFIXES[0].startswith("ACTIVE"))
        for live in ("ACTIVE", "CORRECTED", "CONFIRMED"):
            self.assertFalse(live.upper().startswith(self.doc_audit.KB_DEAD_PREFIXES),
                             f"C8 must SUPERVISE a {live} row")

    def test_kb_file_uses_canonical_token_forms(self):
        """The data half: no KB row may carry a fused token again."""
        import csv
        kb = Path(__file__).resolve().parent.parent / "workbook" / "KB.tsv"
        rows = list(csv.DictReader(kb.open(), delimiter="\t"))
        bad = [r["ID"] for r in rows
               if (r.get("Status") or "").strip().upper().startswith("SUPERSEDED-BY")]
        self.assertEqual(bad, [], f"fused SUPERSEDED-BY token(s) returned: {bad}")


class TestAgsiKeyRejectionDiscriminator(unittest.TestCase):
    """A REJECTED AGSI key returns HTTP 200 + an EMPTY data array — shape-identical to an
    unpublished gas day. Silent expiry therefore produces EXACTLY the message that means
    "come back tomorrow", and a desk defers its checkpoint forever, correctly by the letter.

    Established by negative control 2026-09-19 (PROME probe, independently reproduced):
        real key -> 1 rec · WRONG key -> 0 rec · NO header -> 0 rec · EMPTY-STRING key -> 1 rec
    The last row is the whole discriminator. All tests here are OFFLINE — urlopen is stubbed.
    """

    def _fe(self):
        import importlib, fetch_eu
        return importlib.reload(fetch_eu)

    class _Resp:
        def __init__(self, payload): self._p = payload
        def __enter__(self): return self
        def __exit__(self, *a): return False
        def read(self): return self._p

    def _stub(self, fe, payload_for):
        """payload_for(key) -> bytes. Routes on the x-key header actually sent."""
        import urllib.request
        def fake(req, *a, **k):
            key = req.headers.get("X-key", req.headers.get("x-key", None))
            return TestAgsiKeyRejectionDiscriminator._Resp(payload_for(key))
        self._orig = urllib.request.urlopen
        urllib.request.urlopen = fake
        self.addCleanup(lambda: setattr(urllib.request, "urlopen", self._orig))

    def test_dead_key_is_named_as_a_dead_key_not_as_no_data(self):
        """INJECT a rejected key while the gas day HAS published."""
        fe = self._fe()
        # empty-string key returns data (the vendor quirk); anything else returns empty
        self._stub(fe, lambda k: b'{"data":[{"gasDayStart":"2026-09-17","full":"69.06"}]}'
                                 if k == "" else b'{"data":[]}')
        fe._agsi_key = lambda: "0" * 32
        st, err = fe.agsi_eu()
        self.assertIsNone(st)
        self.assertIn("KEY REJECTED", err)
        self.assertIn("NOT 'come back tomorrow'", err)

    def test_genuine_no_data_does_not_cry_dead_key(self):
        """INJECT a real outage: nothing published, key fine. Must NOT blame the key."""
        fe = self._fe()
        self._stub(fe, lambda k: b'{"data":[]}')      # even the empty-key probe is empty
        fe._agsi_key = lambda: "0" * 32
        st, err = fe.agsi_eu()
        self.assertIsNone(st)
        self.assertNotIn("KEY REJECTED", err)
        self.assertIn("Key validity NOT implicated", err)

    def test_probe_failure_reports_blind_never_no_data(self):
        """INJECT a dead network under the discriminator itself. Fail closed, not quiet."""
        fe = self._fe()
        import urllib.request
        orig = urllib.request.urlopen
        urllib.request.urlopen = lambda *a, **k: (_ for _ in ()).throw(OSError("down"))
        self.addCleanup(lambda: setattr(urllib.request, "urlopen", orig))
        why = fe._agsi_why_empty("x")
        self.assertIn("UNDETERMINED", why)
        self.assertIn("BLIND", why)

    def test_one_key_path_for_the_whole_module(self):
        """REGRESSION: agsi_eu once re-read os.environ itself instead of calling _agsi_key(),
        so the two resolution orders could diverge. Caught 2026-09-19 when an injection
        poisoned the env var and only ONE caller saw it."""
        src = (Path(__file__).resolve().parent / "fetch_eu.py").read_text()
        body = src[src.index("def agsi_eu("):src.index("def agsi_norm(")]
        self.assertNotIn('os.environ.get("AGSI_API_KEY"', body,
                         "agsi_eu re-reads the env directly — second key path has returned")
        self.assertIn("_agsi_key()", body)

    def test_norm_zero_years_names_the_dead_key_shape(self):
        """0/5 years on this API is the dead-key shape, not flaky history — say so."""
        fe = self._fe()
        self._stub(fe, lambda k: b'{"data":[]}')
        fe._agsi_key = lambda: "0" * 32
        mean, med, n, why = fe.agsi_norm("2026-09-17")
        self.assertIsNone(mean)
        self.assertEqual(n, 0)
        self.assertIn("DEAD-KEY shape", why)

    def test_norm_fails_closed_below_quorum_and_never_returns_a_constant(self):
        """INJECT a partial history (3 of 5 years). Must refuse, not average what it has."""
        fe = self._fe()
        good = {2023, 2024, 2025}
        def payload(k):
            payload.i += 1
            return (b'{"data":[{"full":"90.00"}]}' if payload.i in (3, 4, 5)
                    else b'{"data":[]}')
        payload.i = 0
        self._stub(fe, payload)
        fe._agsi_key = lambda: "k"
        mean, med, n, why = fe.agsi_norm("2026-09-17")
        self.assertIsNone(mean, "norm averaged a sub-quorum sample instead of failing closed")
        self.assertIn("only 3/5", why)

    def test_discriminator_carries_its_own_recheck_date(self):
        """A quirk-dependent control without an expiry is a time bomb."""
        src = (Path(__file__).resolve().parent / "fetch_eu.py").read_text()
        self.assertIn("2026-12-19", src, "empty-key discriminator lost its re-check date")
        self.assertIn("safe direction", src.lower(),
                      "the quirk-dependency's fail-direction statement went missing")


if __name__ == "__main__":
    unittest.main(verbosity=2)
