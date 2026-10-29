"""Guards for mof_flows.py's one-week selling bar (>¥1.5T LT-debt net selling).

Written 2026-10-29, owed since the 2026-10-01 incident: MOF published week
2026.9.13~9.19 (LT debt -¥1.905T first print, THROUGH the bar) in the same release
as 2026.9.20~9.26 (-¥684.5B). The WEEKLY ALERT read only rows[-1], so the run
printed "inside the ¥1.5T bar" and the one tripped week was never evaluated.
Recurred benignly 2026-10-29 (two new weeks, both inside the bar).

Tests drive main() end to end with a fake fetch and a temp ledger, so they
exercise the printed alert, not a helper the old code never had.

Run: python3 -m pytest scripts/tests/test_mof_weekly_bar.py -q
 or: python3 scripts/tests/test_mof_weekly_bar.py
"""
import contextlib
import importlib.util
import io
import pathlib
import tempfile

_SPEC = importlib.util.spec_from_file_location(
    "mof_flows", pathlib.Path(__file__).resolve().parents[1] / "mof_flows.py")
mof = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(mof)


def _row(period, lt):
    return {"period": period, "equity_net": 0, "lt_debt_net": lt, "subtotal_net": lt,
            "short_debt_net": 0, "total_net": lt, "in_equity_net": None,
            "in_lt_debt_net": None, "in_subtotal_net": None, "in_short_debt_net": None,
            "in_total_net": None}


# Twelve quiet weeks, then the real 10/01 pair (first-print values from MOF_FLOWS.tsv).
BASE = [_row(f"2026．6．{i}～6．{i}", 1000) for i in range(1, 11)] + [
    _row("2026．8．30～9．5", 1189), _row("2026．9．6～9．12", 10900)]
TRIP = _row("2026．9．13～9．19", -19049)
AFTER = _row("2026．9．20～9．26", -6845)


def _run(rows, ledger_rows):
    tmp = pathlib.Path(tempfile.mkdtemp()) / "MOF_FLOWS.tsv"
    tmp.write_text(mof.TSV_HEADER + "".join(f"{r['period']}\t0\t{r['lt_debt_net']}\n"
                                            for r in ledger_rows))
    saved = (mof.FLOWS_TSV, mof.fetch_mof_csv, mof.parse_mof_csv)
    mof.FLOWS_TSV = tmp
    mof.fetch_mof_csv = lambda: "stub"
    mof.parse_mof_csv = lambda _t: list(rows)
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            mof.main()
    finally:
        mof.FLOWS_TSV, mof.fetch_mof_csv, mof.parse_mof_csv = saved
    return buf.getvalue()


def test_incident_1001_tripped_week_published_with_a_later_week_fires():
    """The headline defect. FAILS on the pre-fix script (it reads rows[-1] only)."""
    out = _run(BASE + [TRIP, AFTER], ledger_rows=BASE)
    assert "WEEKLY SELL BAR TRIPPED" in out, out
    tripped = [l for l in out.splitlines() if "TRIPPED" in l]
    assert any("9．13～9．19" in l for l in tripped), tripped


def test_every_new_week_is_listed_not_just_the_latest():
    out = _run(BASE + [TRIP, AFTER], ledger_rows=BASE)
    alert = out.split("WEEKLY ALERT", 1)[1].split("ROLLING", 1)[0]
    assert "9．13～9．19" in alert and "9．20～9．26" in alert, alert
    assert "2 new week" in alert, alert


def test_rerun_with_nothing_new_does_not_re_announce_old_trip_as_new():
    """Ledger already holds both weeks: evaluate the latest for display only."""
    out = _run(BASE + [TRIP, AFTER], ledger_rows=BASE + [TRIP, AFTER])
    alert = out.split("WEEKLY ALERT", 1)[1].split("ROLLING", 1)[0]
    assert "TRIPPED" not in alert, alert
    assert "no new week" in alert, alert


def test_single_new_week_inside_bar_unchanged_behaviour():
    out = _run(BASE + [AFTER], ledger_rows=BASE)
    alert = out.split("WEEKLY ALERT", 1)[1].split("ROLLING", 1)[0]
    assert "TRIPPED" not in alert and "inside the ¥1.5T bar" in alert, alert


def test_rolling_sums_state_their_vintage():
    """Owed with the fix: the live CSV is revised; the ledger keeps first prints."""
    out = _run(BASE + [TRIP, AFTER], ledger_rows=BASE)
    rolling = out.split("ROLLING", 1)[1].split("ALERT STATUS", 1)[0]
    assert "live CSV" in rolling and "first print" in rolling, rolling


if __name__ == "__main__":
    fails = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            try:
                fn()
                print(f"PASS {name}")
            except AssertionError as e:
                fails += 1
                print(f"FAIL {name}: {str(e)[:300]}")
    raise SystemExit(1 if fails else 0)
