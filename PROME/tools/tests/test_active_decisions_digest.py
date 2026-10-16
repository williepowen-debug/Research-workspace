"""Tests for active_decisions_digest.py — ACCEPTANCE_active_decisions_digest_2026-10-16.md A1–A4, A6."""
import io
import subprocess
import sys
from contextlib import redirect_stdout
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import active_decisions_digest as adg  # noqa: E402

FIX = """# ACTIVE_DECISIONS.md
**Updated:** x
## Rules
| not | the | index |
|---|---|---|
| a | b | c |

## Live Decision Index

| Decision | State | Owner | Next | Backstop | Source |
|---|---|---|---|---|---|
| **Plain approved (WQ-1)** | `WILL_APPROVED` 2026-10-14; `BROKER_PENDING` — no fill on file | Will | consume the fills | L1 | ruling |
| **Closed with guards** | CLOSED 2026-09-30 — NO LIVE POSITION. Later: WQ-360 LAPSED; **WILL_APPROVED** sub-state inside | TERRY | standing guards | — | card |
| Monitor only | `MONITOR_ONLY` — ⛔ ARM RETIRED; FIRED ×2 later in text | PROME | consume grades | HY | HEARTBEAT |

## Next Maintenance Step
| another | table | after | the | index | ignored |
|---|---|---|---|---|---|
| z | DRAFT | z | z | z | z |
"""


def run(text):
    rows, errs = adg.parse(text)
    return rows, errs


def test_a1_ordinary_rows_and_classes():
    rows, errs = run(FIX)
    assert errs == []
    assert [r["n"] for r in rows] == [1, 2, 3]
    assert [r["cls"] for r in rows] == ["ACTIONABLE", "GUARD", "GUARD"]
    assert rows[0]["token"] == "WILL_APPROVED"
    assert rows[0]["bytes"] == len(rows[0]["raw"].encode())


def test_a1_row_whole_byte_exact(tmp_path):
    p = tmp_path / "ad.md"; p.write_text(FIX, encoding="utf-8")
    out = subprocess.run([sys.executable, str(HERE.parent / "active_decisions_digest.py"), str(p), "--row", "2"],
                         capture_output=True, text=True)
    assert out.returncode == 0
    assert out.stdout == FIX.split("\n")[12] + "\n"


def test_a2_overlap_leading_token_decides_and_is_shown():
    rows, _ = run(FIX)
    closed, mon = rows[1], rows[2]
    assert closed["token"] == "CLOSED" and closed["cls"] == "GUARD"
    assert mon["token"] == "MONITOR_ONLY" and mon["cls"] == "GUARD"
    assert closed["state"].startswith("CLOSED 2026-09-30")       # leading token in context
    assert rows[0]["cls"] == "ACTIONABLE"                          # "no fill on file" does not demote it


def test_a3_wrong_owner_only_the_index_table():
    rows, _ = run(FIX)
    titles = [r["title"] for r in rows]
    assert "a" not in titles and "z" not in titles and len(rows) == 3


def test_a4_missing_information_is_loud():
    rows, errs = run(FIX.replace("`MONITOR_ONLY` — ⛔ ARM RETIRED; FIRED ×2 later in text", ""))
    assert len(rows) == 2 and errs and "EMPTY State" in errs[0]
    rows, errs = run(FIX.replace("| HY | HEARTBEAT |", "|"))
    assert len(rows) == 2 and errs and "cells" in errs[0]
    rows, errs = run(FIX.replace("## Live Decision Index", "## Something else"))
    assert rows == [] and "no heading" in errs[0]


def test_a4_check_mode_rc(tmp_path):
    p = tmp_path / "ad.md"; p.write_text(FIX.replace("| HY | HEARTBEAT |", "|"), encoding="utf-8")
    assert adg.main([str(p), "--check"]) == 1
    p.write_text(FIX, encoding="utf-8")
    assert adg.main([str(p), "--check"]) == 0
    assert adg.main([str(p), "--row", "9"]) == 1


def test_a6_live_file_digest_under_3000_bytes():
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = adg.main([str(adg.DEFAULT)])
    assert rc == 0
    assert len(buf.getvalue().encode()) < 3000, len(buf.getvalue().encode())
