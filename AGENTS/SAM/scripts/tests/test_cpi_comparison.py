"""Guards for cpi_japan.print_comparison_note's PAIRED branch.

Written 2026-09-19 alongside the fix, because the defect it covers survived 27
days in a boot-wired script: the ruling that retired the interpretation landed in
STATUS_REFERENCE.md and docket/CALENDAR.md, and nothing propagated it into the
code that kept printing it every run.

The three defects under test:
  1. FLOAT BOUNDARY  — `diff > 0.1` on float-subtracted one-decimal values.
  2. RETIRED READ    — "pattern INVERTED, leading-indicator hawkish" (retired
                       2026-08-23, KB-169: the counter-example was a base artifact).
  3. STALE CONSTANT  — "the typical 30-40bp", a 2020-base figure; the 2025-base
                       mean is ~-0.13pp.

Run: python3 -m pytest scripts/tests/test_cpi_comparison.py -q
 or: python3 scripts/tests/test_cpi_comparison.py
"""
import io
import contextlib
import re
import importlib.util
import pathlib
import sys

_SPEC = importlib.util.spec_from_file_location(
    "cpi_japan", pathlib.Path(__file__).resolve().parents[1] / "cpi_japan.py")
cpi = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(cpi)


def _run(pairs):
    """pairs: {month: (tokyo_core_core, national_core_core)} -> captured stdout."""
    nat = {m: {"core_core": n} for m, (_t, n) in pairs.items()}
    tok = {m: {"core_core": t} for m, (t, _n) in pairs.items()}
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        cpi.print_comparison_note(nat, tok)
    return buf.getvalue()


# The 2025-base same-month core-core series measured in KB-169 (remeasure 2026-08-23).
# Tokyo - National, in pp: Feb 0.0 / Mar -0.2 / Apr -0.2 / May -0.3 / Jun 0.0 / Jul -0.1
BASE2025 = {
    "2026-02": (2.4, 2.4), "2026-03": (2.2, 2.4), "2026-04": (1.7, 1.9),
    "2026-05": (1.5, 1.8), "2026-06": (1.7, 1.7), "2026-07": (1.8, 1.9),
}
# August 2026 as actually published (CPI.tsv, 2025 base): Tokyo 2.0 / National 1.9.
AUGUST = dict(BASE2025, **{"2026-08": (2.0, 1.9)})


def test_classification_is_invariant_to_absolute_level_at_a_fixed_gap():
    """THE headline defect, stated as the property that actually falsifies it.

    ⚠️ An earlier version of this test asserted only that (2.0, 1.9) prints
    "+0.1pp ABOVE National". That PASSED AGAINST THE PRE-FIX CODE, because the old
    float branch happened to fire on that one input too — so the test named after
    the defect could not detect the defect. Verified by running it against the
    backed-up original. It tested the output string, not the arithmetic.

    The discriminating property: with one-decimal inputs, the classification must
    depend ONLY on the gap, never on the absolute level. Float subtraction breaks
    that, because the representation error moves with magnitude:
        2.0 - 2.2 == -0.20000000000000018  -> old `< -0.2` TRUE
        1.7 - 1.9 == -0.19999999999999996  -> old `< -0.2` FALSE
    Same true gap, opposite branches. The old code printed "-0.2pp BELOW National
    - expected pattern" for one and "-0.2pp ... narrower than the typical 30-40bp"
    for the other. Likewise at +0.1: (2.0, 1.9) fired the INVERTED branch while
    (0.3, 0.2) did not."""
    # premises, so the test documents why it exists even if the code changes
    assert (2.0 - 2.2) < -0.2 and not ((1.7 - 1.9) < -0.2), "float error moves with magnitude"
    assert (2.0 - 1.9) > 0.1 and not ((0.3 - 0.2) > 0.1)
    assert round(2.0 * 10) - round(2.2 * 10) == round(1.7 * 10) - round(1.9 * 10) == -2

    def verdict(t, n):
        head = _run({"2026-08": (t, n)}).splitlines()[0]
        return head.split("): ", 1)[-1]

    for gap_pairs in ([(2.0, 2.2), (1.7, 1.9), (0.5, 0.7), (1.3, 1.5)],   # all -0.2pp
                      [(2.0, 1.9), (0.3, 0.2), (1.1, 1.0), (1.5, 1.4)]):  # all +0.1pp
        verdicts = {verdict(t, n) for t, n in gap_pairs}
        assert len(verdicts) == 1, (
            "same true gap classified %d different ways: %r" % (len(verdicts), verdicts))


def test_retired_interpretation_is_never_ASSERTED():
    """The retired read must never be emitted as a conclusion.

    ⚠️ This assertion is deliberately NOT `"leading-indicator hawkish" not in out`.
    The fix prints that phrase inside a prohibition ("NOT 'leading-indicator
    hawkish'"), so a bare substring test cannot tell an EMISSION from a BAN and
    fails on correct code — which is exactly what its first version did here.
    Keyed on the phrase alone, the guard read the ban as the breach.
    So: "pattern INVERTED" must be absent outright, and every occurrence of the
    hawkish phrase must be immediately preceded by the negation."""
    for pairs in (BASE2025, AUGUST, {"2026-08": (2.5, 1.5)}):
        out = _run(pairs)
        assert "pattern INVERTED" not in out
        for mm in re.finditer(r"leading-indicator hawkish", out):
            prefix = out[max(0, mm.start() - 6):mm.start()]
            assert prefix.endswith("NOT '"), (
                "hawkish phrase emitted outside the prohibition: ...%s" % out[mm.start() - 40:mm.end()])


def test_stale_2020_base_constant_is_gone():
    """'~30-40bp' is a 2020-base figure. It must not be asserted as the band."""
    for pairs in (BASE2025, AUGUST):
        out = _run(pairs)
        assert "30-40bp" not in out


def test_measured_band_matches_kb169_and_is_not_hardcoded():
    """The band must be computed from the ledger, so it tracks the active base.
    Prior months Feb-Jul (n=6) have mean -0.13pp and range -0.3..0.0."""
    out = _run(AUGUST)
    assert "n=6" in out
    assert "mean -0.13pp" in out
    assert "range -0.3 to +0.0pp" in out
    assert "Tokyo ≤ National in 6 of 6" in out

    # Feed a DIFFERENT history: the band must move, proving it is measured.
    # NOTE the band covers PRIOR months only (the current month is the thing being
    # placed against it), so Jan/Feb (+1.0, +1.0) give n=2 mean +1.00 — NOT the
    # 3-month mean. The first version of this test asserted +0.67 by averaging all
    # three and failed against correct code.
    other = {"2026-01": (2.0, 1.0), "2026-02": (2.0, 1.0), "2026-03": (1.0, 2.0)}
    band = _run(other)
    assert "n=2" in band and "mean +1.00pp" in band


def test_every_2025_base_month_reads_as_within_tendency():
    """On the measured 2025-base data Tokyo <= National in 6 of 6. None of those
    months may be flagged as an exception. The OLD thresholds called 5 of these 6
    'narrower than the typical 30-40bp' — i.e. the normal case, labelled abnormal."""
    for month, (t, n) in BASE2025.items():
        out = _run({month: (t, n)})
        assert "within the measured tendency" in out, month
        assert "ABOVE National" not in out, month


def test_positive_gap_carries_both_caveats():
    """August 2026 is the first positive paired gap on the 2025 base. It must be
    reported as an exception WITH the retirement warning and the quantization
    caveat — the flag is legitimate, the old label was not."""
    out = _run(AUGUST)
    assert "exception 1 of 7 paired months" in out
    assert "RETIRED 2026-08-23" in out and "BASE ARTIFACT" in out
    assert "one-decimal publication floor" in out
    assert "(0.0, 0.2)pp" in out


def test_quantization_caveat_is_scoped_to_the_one_tenth_case():
    """A larger positive gap is not a rounding question — the caveat must not fire
    there, or it becomes noise that trains the reader to skip it."""
    out = _run({"2026-07": (1.8, 1.9), "2026-08": (2.5, 1.9)})
    assert "+0.6pp ABOVE National" in out
    assert "one-decimal publication floor" not in out
    assert "RETIRED 2026-08-23" in out


def test_divergence_note_is_invariant_to_absolute_level():
    """Same defect CLASS as the PAIRED branch, in the function that runs on BOTH
    series on EVERY boot. Found by auditing the first fix, not by a wrong print.

    Old code compared float-subtracted one-decimal values:
        1.9 - 1.7 == 0.19999999999999996  -> `<= 0.2` TRUE  -> "less BOJ cover"
        2.2 - 2.0 == 0.20000000000000018  -> `<= 0.2` FALSE -> label WITHHELD
    Identical +0.2pp gap; the BOJ read-through appeared or vanished on the
    absolute level alone. Exhaustive over 0.0-6.0 at one decimal: 32 of 59
    possible +0.2pp gaps failed the test, plus 4 true +0.5pp gaps failing `>= 0.5`."""
    for gap_tenths, pairs in (
        (2, [(1.9, 1.7), (2.2, 2.0), (2.1, 1.9), (0.8, 0.6), (1.6, 1.4)]),
        (5, [(1.9, 1.4), (2.3, 1.8), (0.7, 0.2), (1.4, 0.9), (4.1, 3.6)]),
    ):
        notes = {cpi.divergence_note(c, cc) for cc, c in pairs}
        assert len(notes) == 1, (
            "+%.1fpp gap classified %d ways: %r" % (gap_tenths / 10, len(notes), notes))


def test_divergence_note_exhaustive_bucket_agreement():
    """No one-decimal pair anywhere in the plausible range may disagree with the
    exact tenths bucket it belongs to."""
    vals = [round(i * 0.1, 1) for i in range(0, 61)]
    for cc in vals:
        for c in vals:
            t = round(cc * 10) - round(c * 10)
            note = cpi.divergence_note(c, cc)
            if t >= 5:
                assert "energy/subsidy-driven" in note, (cc, c, t, note)
            elif t <= 2:
                assert "broad-based softening" in note, (cc, c, t, note)
            else:
                assert "\u2192" not in note and "-&gt;" not in note, (cc, c, t, note)


def test_divergence_note_negative_gap_is_not_printed_as_plus_minus():
    """core-core can fall BELOW core when ENERGY is RISING (core includes energy,
    core-core does not) — the live oil-shock case. The old format string hardcoded
    a '+' and would render that as 'gap +-0.3pp'. No such row exists in CPI.tsv
    yet, so this is a latent defect that would first appear exactly when the desk
    cares most."""
    note = cpi.divergence_note(2.0, 1.7)          # core 2.0, core-core 1.7 => -0.3pp
    assert "+-" not in note, note
    assert "-0.3pp" in note


def test_no_paired_month_is_reported_not_guessed():
    nat = {"2026-08": {"core_core": 1.9}}
    tok = {"2026-07": {"core_core": 1.8}}
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        cpi.print_comparison_note(nat, tok)
    out = buf.getvalue()
    assert "no gap figure this run" in out
    assert "ABOVE" not in out


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("PASS", name)
            except AssertionError as e:
                fails += 1
                print("FAIL", name, "--", e)
    print("\n%d failure(s)" % fails)
    sys.exit(1 if fails else 0)
