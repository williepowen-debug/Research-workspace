"""Tests for prome_gate.summarize_orch_closeout — ACCEPTANCE_gate_log_summary_2026-10-16.md A1–A4, A6."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import prome_gate as pg  # noqa: E402

TODAY = "2026-10-16"
BODY = """ORCH_LOG closeout evidence — 2026-10-16 + unresolved prior touches
ASKED → receipt: 2
  2026-10-16 CRUISE touch 1-SPAWN [aaa]: ask: … | receipt: …
  2026-10-16 BROCK touch 1-SPAWN [bbb]: ask: … | receipt: …
ASKED → still working: 1
  2026-09-19 ARGUS touch 1-SPAWN [ccc]: ask: … | pending
ALREADY CLOSED OUT: 0
WENT DARK BEFORE THE ASK: 2
  2026-10-15 BROCK touch 1-SPAWN [ddd]: presence: dark
  2026-10-16 PROME-reader touch 1-SPAWN [eee]: presence: helper
UNKNOWN: 2026-09-01 TERRY touch 1 [fff]: missing or duplicate
UNKNOWN: 2026-10-16 ZHAO touch 1 [ggg]: missing
UNKNOWN: spawn inventory coverage UNKNOWN; ledger absence cannot prove no spawns
"""


def test_a1_counts_and_todays_names_on_the_line():
    ok, line = pg.summarize_orch_closeout(BODY, 1, TODAY)
    assert ok is False                                   # rc=1 stays an advisory flag, as before
    assert line.startswith("ASKED→receipt 2 (CRUISE BROCK) · still working 1 · already closed 0 · dark-before-ask 2 (PROME-reader)")
    assert "UNKNOWN rows 2 (today 1: ZHAO · older 1 ≤2026-09-01, the standing WQ-249 backlog — not a boot read)" in line
    assert line.endswith("spawn inventory coverage UNKNOWN; ledger absence cannot prove no spawns")
    assert len(line) <= 700                               # A6 (amended at read 1: the line names today's touches)


def test_a2_overlap_same_desk_in_two_states_counted_in_each():
    ok, line = pg.summarize_orch_closeout(BODY, 1, TODAY)
    assert "ASKED→receipt 2 (CRUISE BROCK)" in line and "dark-before-ask 2" in line   # BROCK in both, never netted


def test_a3_wrong_owner_only_this_log_is_summarised():
    ok, line = pg.summarize_orch_closeout(BODY + "⚠️ AGENTS/WAL/STATUS.md DATE DRIFT\n", 1, TODAY)
    assert "DATE DRIFT" not in line


def test_a4_missing_count_lines_are_unknown_never_zero():
    with pytest.raises(ValueError, match="counts UNKNOWN"):
        pg.summarize_orch_closeout(BODY.replace("ALREADY CLOSED OUT: 0\n", ""), 1, TODAY)
    with pytest.raises(ValueError):
        pg.summarize_orch_closeout("", 0, TODAY)


def test_rc0_is_ok():
    ok, _ = pg.summarize_orch_closeout(BODY.replace("UNKNOWN: spawn inventory coverage UNKNOWN; ledger absence cannot prove no spawns\n", ""), 0, TODAY)
    assert ok is True


def test_live_log_if_present():
    p = Path("/tmp/prome-boot-8fb641db/checks/00-orchestrated-touch-closeout-evidence-wq-249-.txt")
    if not p.exists():
        pytest.skip("no live boot log on this machine")
    ok, line = pg.summarize_orch_closeout(p.read_text(encoding="utf-8"), 1, TODAY)
    assert "ASKED→receipt 4 (CRUISE REGINALD ORACLE BROCK)" in line and len(line) <= 700
    assert "PROME-reader (bootplan-read1)" in line          # read 1 C4: the full desk token
    assert "today 14:" in line and "ARGUS" in line         # read 1 C8: today's UNKNOWN touches named


def test_read1_c4_full_desk_token_and_c8_todays_unknown_names():
    body = BODY.replace("  2026-10-16 PROME-reader touch", "  2026-10-16 PROME-reader (plan-read x) touch")
    ok, line = pg.summarize_orch_closeout(body, 1, TODAY)
    assert "dark-before-ask 2 (PROME-reader (plan-read x))" in line
    assert "today 1: ZHAO" in line


SPAWN = """spawn_list · as-of 2026-10-16 · horizon +0d · 4 row(s): DARK 1 · ACTIVE 2 · lands-ahead 0 · PROME 1 · WILL 0
key\tdue\tΔd\towner\tclass\tbasis
⚠️ D:L405\t2026-10-16\t0\tZHAO\tDARK\tlast self-commit …
D:L548\t2026-10-07\t9\tDAEDALUS\tACTIVE\t…
G:GATE-X\t2026-10-09\t7\tBRENT\tACTIVE\t…
D:L350\t2026-09-19\t27\tPROME\tPROME-OWNED\tdo it
"""


def test_read1_c13_spawn_list_counts_and_ids_on_the_line():
    ok, line = pg.summarize_spawn_list(SPAWN, 1)
    assert ok is False
    assert line.startswith("as-of 2026-10-16 · horizon +0d · 4 row(s): DARK 1 · ACTIVE 2")
    assert "DARK: D:L405 ZHAO" in line and "ACTIVE: D:L548 DAEDALUS, G:GATE-X BRENT" in line
    with pytest.raises(ValueError, match="counts UNKNOWN"):
        pg.summarize_spawn_list("key\tdue\n", 1)
