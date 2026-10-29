"""Tests for prome_gate.check_heartbeat_chain / heartbeat_chain_counts —
ACCEPTANCE_heartbeat_chain_format_L852_2026-10-28.md A1–A6, A8 (A7 N/A: one reader, one file)."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import prome_gate as pg  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]

NEW_STYLE = """# HEARTBEAT.md
**Base:** Monday night, 2026-10-26, THIRTY-FIFTH base, PROME. Market pull: 20:29 ET. **Amendment chain: 2.** Prior base: archive.

**Amendment 1 — October27 closeout, NEXUS e9a2fd411:** Vulnerabilities are present; amendment 1 text mentions amendment 3 mid-line.

**Amendment 2 — October28 night closeout, PROME prome-92:** The FOMC HELD.

**1. Energy —** text.
"""

OLD_STYLE = """# HEARTBEAT.md
**Base:** 2026-10-23 Friday, THIRTY-FOURTH base, PROME.
**Amendments append below this line; the ~5 rule holds. Chain: 2.**

> **AMENDMENT #1 — Fri 2026-10-23 16:5x ET, CORRECTION to § 3.** text.

> ## AMENDMENT #2 — Sat 2026-10-24 15:55 ET, CORRECTION.
"""

MIXED = """**Base:** x. **Amendment chain: 2.**

> **AMENDMENT #1 — old block retained.** text

**Amendment 2 — new block appended:** text
"""

NO_DECLARATION = """**Base:** Monday night, 2026-10-26, THIRTY-FIFTH base, PROME. Chain of custody: fine.

**Amendment 1 — October27:** text
"""

DECLARED_BUT_NO_BLOCKS = """**Base:** x. **Amendment chain: 1.**

Amendment chain: 1 is also mentioned here in prose. The amendments append below.
"""


def run_check(tmp_path, text):
    f = tmp_path / "HB.md"
    f.write_text(text, encoding="utf-8")
    got = []
    pg.record = lambda sev, name, ok, detail, owner: got.append((sev, name, ok, detail, owner))
    pg.check_heartbeat_chain(f)
    assert len(got) == 1
    return got[0]


def test_a1_current_style_counts_two_and_agrees(tmp_path):
    assert pg.heartbeat_chain_counts(NEW_STYLE) == (2, 2)
    sev, name, ok, detail, _ = run_check(tmp_path, NEW_STYLE)
    assert ok is True and detail.startswith("chain at 2 amendment(s) (header-declared count agrees)")


def test_a1_live_file_is_readable_by_the_check():
    text = (ROOT / "HEARTBEAT.md").read_text(encoding="utf-8")
    counted, declared = pg.heartbeat_chain_counts(text)
    assert declared is not None, "the live HEARTBEAT header must carry an accepted declaration form"
    assert counted == declared


def test_a2_prior_style_both_block_forms_and_old_declaration():
    assert pg.heartbeat_chain_counts(OLD_STYLE) == (2, 2)


def test_a2_34th_base_archive_counts_four_and_warns(tmp_path):
    snap = ROOT / "PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-10-26.md"
    if not snap.exists():
        pytest.skip("archive snapshot absent on this clone")
    text = snap.read_text(encoding="utf-8")
    counted, declared = pg.heartbeat_chain_counts(text)
    assert (counted, declared) == (4, 4)
    sev, name, ok, detail, _ = run_check(tmp_path, text)
    assert ok is False and "re-base rule trips at ~5" in detail


def test_a3_missing_declaration_fails_loud_and_names_the_forms(tmp_path):
    assert pg.heartbeat_chain_counts(NO_DECLARATION) == (1, None)
    sev, name, ok, detail, _ = run_check(tmp_path, NO_DECLARATION)
    assert ok is False and detail.startswith("UNVERIFIABLE")
    assert "NOT a verdict" in detail
    for form in ("`> ## AMENDMENT #N`", "`> **AMENDMENT #N`", "`**Amendment N —`",
                 "`**Amendments append … Chain: N`", "`**Amendment chain: N.**`"):
        assert form in detail                           # A8 self-describing


def test_a3_declared_over_zero_blocks_is_unverifiable_not_zero(tmp_path):
    assert pg.heartbeat_chain_counts(DECLARED_BUT_NO_BLOCKS) == (0, 1)
    sev, name, ok, detail, _ = run_check(tmp_path, DECLARED_BUT_NO_BLOCKS)
    assert ok is False and detail.startswith("UNVERIFIABLE") and "counted 0" in detail


def test_a4_disagreement_trips_on_max(tmp_path):
    text = NEW_STYLE.replace("**Amendment chain: 2.**", "**Amendment chain: 5.**")
    sev, name, ok, detail, _ = run_check(tmp_path, text)
    assert ok is False and "larger (5)" in detail


def test_a5_overlap_both_styles_in_one_file_sum():
    assert pg.heartbeat_chain_counts(MIXED) == (2, 2)


def test_a6_false_positives_are_not_blocks():
    assert pg.heartbeat_chain_counts("**Amendment chain: 2.**\n")[0] == 0
    assert pg.heartbeat_chain_counts("**Amendments append below. Chain: 0.**\n")[0] == 0
    assert pg.heartbeat_chain_counts("prose says amendment 1 was fine\n")[0] == 0
    assert pg.heartbeat_chain_counts("Amendment chain: 3 at line start\n")[0] == 0
    # the lowercase body form still needs the number right after the word
    assert pg.heartbeat_chain_counts("**Amendment one — spelled out:** text\n")[0] == 0


QUOTED_IN_BODY = """**Base:** Monday night, THIRTY-FIFTH base, PROME. No chain figure here.

**Amendment 1 — October27:** text quoting the old header verbatim: **Amendment chain: 2.** as prose.

**Amendment 2 — October28:** text.
"""


def test_a3_declaration_quoted_in_a_body_block_is_not_the_header(tmp_path):
    # Independent read P-14 (2026-10-28): whole-file search returned (2, 2) and a confident PASS here.
    assert pg.heartbeat_chain_counts(QUOTED_IN_BODY) == (2, None)
    sev, name, ok, detail, _ = run_check(tmp_path, QUOTED_IN_BODY)
    assert ok is False and detail.startswith("UNVERIFIABLE")
