"""Float-tie guards for rate_differential.py (SAM-41 bars) and jgb_auctions.py
(tail / BTC status bars). DAEDALUS L546 class, owed since 2026-10-08.

Same class fixed in cpi_japan.py on 2026-09-19: published values have fixed
decimals (yields 3dp), but float subtraction leaves residue, so a TRUE value
exactly on a strict bar classifies differently depending on its absolute level.
Measured 2026-10-29: a true 5Y gap of exactly 2.250 computes BELOW the bar for
267 of 1,200 3dp pairs; a true tail of exactly 5.0bp computes ABOVE 5 for 1,607
of 3,000 pairs. Neither is live (real gaps sit 30+bp from the bars; SAM-41 is
RESOLVED and its 2026-08-28 boundary dates were checked 9/19), so this is latent.

Run: python3 scripts/tests/test_float_ties.py
"""
import contextlib
import importlib.util
import io
import pathlib
import tempfile

_DIR = pathlib.Path(__file__).resolve().parents[1]


def _load(name):
    spec = importlib.util.spec_from_file_location(name, _DIR / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rd = _load("rate_differential")
ja = _load("jgb_auctions")


def _run_rd(pairs):
    """pairs: list of ((us5, us10), (jp5, jp10)) on consecutive dates."""
    dates = [f"2026-10-{i:02d}" for i in range(1, len(pairs) + 1)]
    ust = {d: p[0] for d, p in zip(dates, pairs)}
    jgb = {d: p[1] for d, p in zip(dates, pairs)}
    saved = (rd.load_jgb, rd.fetch_ust, rd.OUT_TSV)
    rd.load_jgb = lambda: jgb
    rd.fetch_ust = lambda _y: ust
    rd.OUT_TSV = pathlib.Path(tempfile.mkdtemp()) / "RATE_DIFFERENTIAL.tsv"
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rd.main()
    finally:
        rd.load_jgb, rd.fetch_ust, rd.OUT_TSV = saved
    return buf.getvalue()


def test_5y_gap_exactly_on_bar_does_not_fire():
    # (4.004 - 1.754) == 2.250 exactly; float gives 2.2499999999999996.
    out = _run_rd([((4.004, 5.0), (1.754, 2.0))] * 5)
    assert "5Y 0/5" in out, out
    assert "CONDITION MET" not in out, out


def test_10y_gap_exactly_on_bar_does_not_fire():
    # (3.001 - 1.201) == 1.800 exactly; float gives 1.7999999999999998.
    out = _run_rd([((5.0, 3.001), (2.0, 1.201))] * 5)
    assert "10Y 0/5" in out, out
    assert "CONDITION MET" not in out, out


def test_gap_one_thousandth_through_bar_still_fires():
    out = _run_rd([((4.004, 5.0), (1.755, 2.0))] * 5)  # 2.249
    assert "5Y 5/5" in out and "CONDITION MET" in out, out


def test_tail_is_exact_to_published_precision():
    assert ja.tail_bp_of(1.912, 1.905) == 0.7
    assert ja.tail_bp_of(1.050, 1.000) == 5.0


def test_tail_exactly_5bp_is_not_a_quality_problem():
    assert ja.classify_status(3.5, ja.tail_bp_of(1.050, 1.000)) == "✅ Orderly"
    assert ja.classify_status(3.5, ja.tail_bp_of(1.051, 1.000)) == "🟠 Quality problem"


# BTC is NOT in this class: a search of 30,000 0.1-unit bid/accept pairs exactly on the
# 2.0x and 2.8x bars found zero float misses (division is correctly rounded), so it was
# deliberately left unchanged on 2026-10-29.


if __name__ == "__main__":
    fails = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            try:
                fn()
                print(f"PASS {name}")
            except Exception as e:  # AttributeError on old code counts as failure
                fails += 1
                print(f"FAIL {name}: {type(e).__name__} {str(e)[:200]}")
    raise SystemExit(1 if fails else 0)
