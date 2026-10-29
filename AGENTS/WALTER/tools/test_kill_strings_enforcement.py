"""kill_strings enforcement (2026-10-29): FORMAT_SPEC v0.22 made the field mandatory on
corrections from 9/24, but nothing checked it and 53 corrections shipped without it.
gen_board_index refuses a post-cutoff correction without it; walter_doctor counts the
pre-cutoff misses and flags new ones; both accept the quoted `signal_type` form."""
import importlib.util
import os
import pathlib
import tempfile

HERE = pathlib.Path(__file__).resolve().parent


def _load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _card(d, sid, dispatched, stype, kill=None):
    k = f"kill_strings: {kill}\n" if kill is not None else ""
    text = (f'---\nsignal_id: "{sid}"\ndate: "{dispatched[:10]}"\ndispatched: "{dispatched}"\n'
            f"signal_type: {stype}\ncorrects: [\"SIG-W-20261001-001\"]\n{k}"
            f'cluster: "MISC"\nprecedence: "ROUTINE"\n---\n# t\n')
    (pathlib.Path(d) / f"{sid}-t.md").write_text(text)


def _board():
    d = tempfile.mkdtemp()
    _card(d, "SIG-W-20261029-090", "2026-10-29T17:00:00Z", '"correction"')          # new, missing
    _card(d, "SIG-W-20261029-091", "2026-10-29T17:00:00Z", "correction", '["x"]')   # new, ok
    _card(d, "SIG-W-20261029-092", "2026-10-29T17:00:00Z", "'correction'", "[]")    # new, empty
    _card(d, "SIG-W-20261020-093", "2026-10-20T17:00:00Z", '"correction"')          # legacy
    return d


def test_generator_refuses_new_correction_without_kill_strings():
    g = _load("gen_board_index")
    g.BOARD = _board()
    _, errors = g.load_signals()
    hit = sorted(e.split(":")[0] for e in errors if "kill_strings" in e)
    assert hit == ["SIG-W-20261029-090-t.md", "SIG-W-20261029-092-t.md"]


def test_doctor_flags_new_counts_legacy_and_reads_quoted_type():
    wd = _load("walter_doctor")
    wd.BOARD = pathlib.Path(_board())
    out = wd.check_correction_kill_strings()
    meds = [m for lvl, m in out if lvl == wd.MED]
    assert len(meds) == 2 and all(("-090-" in m) or ("-092-" in m) for m in meds)
    info = [m for lvl, m in out if lvl == wd.INFO][0]
    assert "1 correction(s) carry it" in info and "1 pre-enforcement miss" in info
    assert wd._is_correction('signal_type: "correction"')
    assert not wd._is_correction('signal_type: "context"')
