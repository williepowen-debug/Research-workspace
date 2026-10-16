"""Tests for active_decisions_digest.py — ACCEPTANCE_active_decisions_digest_2026-10-16.md A1–A6
plus the independent reader's counterexamples CE1–CE5 (read 1, HOLD → fixed)."""
import datetime as dt
import io
import subprocess
import sys
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import active_decisions_digest as adg  # noqa: E402

TODAY = dt.date(2026, 10, 16)
RULES = "- Include decisions in non-terminal states: `DRAFT`, `PROPOSED`, `WILL_APPROVED`, `BROKER_PENDING`, `ORDER_PLACED`, `FILLED`, `POSITION_UPDATED`, `LOGGED`, `DEFERRED`.\n"
HEAD = "# ACTIVE_DECISIONS.md\n**Updated:** x\n## Rules\n" + RULES + "| not | the | index |\n|---|---|---|\n| a | b | c |\n\n## Live Decision Index\n\n| Decision | State | Owner | Next | Backstop | Source |\n|---|---|---|---|---|---|\n"
TAIL = "\n## Next Maintenance Step\n| another | table | after | the | index | ignored |\n|---|---|---|---|---|---|\n| z | DRAFT | z | z | z | z |\n"
R1 = "| **Plain approved (WQ-1)** | `WILL_APPROVED` 2026-10-14; `BROKER_PENDING` — no fill on file | Will | consume the fills | L1 | ruling |"
R2 = "| **Closed with guards** | CLOSED 2026-09-30 — NO LIVE POSITION. Later: WQ-360 LAPSED; **WILL_APPROVED** sub-state far beyond the first 72 characters of this cell | TERRY | standing guards; expiry 10/19 | — | card |"
R3 = "| Monitor only | `MONITOR_ONLY` — ⛔ ARM RETIRED; FIRED ×2 later in text | PROME | consume grades | HY | HEARTBEAT |"
FIX = HEAD + "\n".join([R1, R2, R3]) + TAIL


def run(text):
    return adg.parse(text, TODAY)


def test_a1_ordinary_rows_and_classes():
    rows, errs = run(FIX)
    assert errs == []
    assert [r["cls"] for r in rows] == ["ACTIONABLE", "GUARD", "GUARD"]
    assert rows[0]["bytes"] == len(rows[0]["raw"].encode())


def test_a1_row_whole_byte_exact(tmp_path):
    p = tmp_path / "ad.md"; p.write_text(FIX, encoding="utf-8")
    out = subprocess.run([sys.executable, str(HERE.parent / "active_decisions_digest.py"), str(p), "--row", "2"],
                         capture_output=True, text=True)
    assert out.returncode == 0 and out.stdout == R2 + "\n"


def test_a2_overlap_window_decides_and_is_shown():
    rows, _ = run(FIX)
    assert rows[1]["cls"] == "GUARD" and rows[1]["state"].startswith("CLOSED 2026-09-30")
    assert rows[2]["cls"] == "GUARD"
    assert rows[0]["cls"] == "ACTIONABLE"                       # "no fill on file" does not demote it
    assert rows[1]["dated"] == ["10/19"]                          # CE4 cue: a dated item inside a GUARD row


def test_a3_wrong_owner_only_the_index_table():
    rows, _ = run(FIX)
    assert [r["title"] for r in rows] == ["Plain approved (WQ-1)", "Closed with guards", "Monitor only"]


def test_a4_missing_information_is_loud():
    rows, errs = run(FIX.replace("`MONITOR_ONLY` — ⛔ ARM RETIRED; FIRED ×2 later in text", ""))
    assert len(rows) == 2 and any("EMPTY State" in e for e in errs)
    rows, errs = run(FIX.replace("| HY | HEARTBEAT |", "|"))
    assert len(rows) == 2 and any("cells" in e for e in errs)
    rows, errs = run(FIX.replace("## Live Decision Index", "## Something else"))
    assert rows == [] and any("no heading" in e for e in errs)


def test_ce1_unusual_leading_tokens_never_default_silently():
    forms = ["will_approved", "⛔ WILL_APPROVED", "2026-10-20 WILL_APPROVED", "LIVE / BROKER_PENDING", "WILL_APPROVED;",
             "WILL_APPROVED→BROKER_PENDING", "_WILL_APPROVED_", "DEFERRED-reconcile", "`WILL_APPROVED`:"]
    body = "\n".join(f"| D{i} | {f} x | o | n | b | s |" for i, f in enumerate(forms))
    rows, errs = run(HEAD + body + TAIL)
    assert all(r["cls"] == "ACTIONABLE" for r in rows), [(r["title"], r["cls"]) for r in rows]
    rows, errs = run(HEAD + "| D | SOMETHING_NEW 2026-10-01 — not terminal | o | n | b | s |" + TAIL)
    assert rows[0]["cls"] == "UNCLASSIFIED" and any("UNCLASSIFIED" in e for e in errs)


def test_ce2_rows_after_comment_blank_or_indent_are_kept():
    body = R1 + "\n<!-- comment -->\n" + R2 + "\n\n   " + R3
    rows, errs = run(HEAD + body + TAIL)
    assert errs == [] and len(rows) == 3


def test_ce3_escaped_pipe_and_extra_cells():
    rows, errs = run(HEAD + "| E | WILL_APPROVED | o \\| p | n | b | s |" + TAIL)
    assert errs == [] and rows[0]["next"] == "n"
    rows, errs = run(HEAD + "| E | WILL_APPROVED | o | p | n | b | s |" + TAIL)
    assert any("7 cells" in e for e in errs)


def test_read2_prose_lead_words_are_not_guard_tokens():
    body = "\n".join(["| P1 | Live order at broker, fill owed | o | n | b | s |",
                      "| P2 | Closed for new entries; sell order working | o | n | b | s |",
                      "| P3 | CLOSED — fill owed by 10/14 | o | sell before Oct-19 print | b | s |"])
    rows, errs = run(HEAD + body + TAIL)
    assert [r["cls"] for r in rows] == ["UNCLASSIFIED", "UNCLASSIFIED", "GUARD"]
    assert sum("UNCLASSIFIED" in e for e in errs) == 2
    assert rows[2]["dated"] == ["10/14", "10/19"]          # overdue M/D and Mon-DD both cued


def test_ce5_rules_list_cross_checked():
    rows, errs = run(FIX.replace("`DEFERRED`", "`DEFERRED`, `PARKED`"))
    assert any("Rules bullet lists" in e for e in errs)


def test_check_mode_rc(tmp_path):
    p = tmp_path / "ad.md"; p.write_text(FIX.replace("| HY | HEARTBEAT |", "|"), encoding="utf-8")
    assert adg.main([str(p), "--check", "--today", "2026-10-16"]) == 1
    p.write_text(FIX, encoding="utf-8")
    assert adg.main([str(p), "--check", "--today", "2026-10-16"]) == 0
    assert adg.main([str(p), "--row", "9"]) == 1


def test_a6_live_file_clean_and_under_3500_bytes():
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = adg.main([str(adg.DEFAULT)])
    assert rc == 0, buf.getvalue()
    assert len(buf.getvalue().encode()) < 3500, len(buf.getvalue().encode())
