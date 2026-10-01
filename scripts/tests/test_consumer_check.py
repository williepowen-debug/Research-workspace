#!/usr/bin/env python3
"""Committed regression fixtures for scripts/consumer_check.py (RAV review 2026-08-28: the
8/28 fixes were verified only by one-off recorded fixture runs; a shared script needs its
cases on disk). Run:  python3 scripts/tests/test_consumer_check.py   (rc 0 pass / 1 fail).

Covers, by name:
  read_ledger      — '#' banner ABOVE the header must not manufacture a phantom metric (BROCK)
                     · clean ledger unchanged · '#' lines mid-file skipped
  line-class       — threshold operator beside the value ⇒ 🟠            (DOCKET kill line)
                     · tail word within THRESH_WINDOW of the value ⇒ 🟠
                     · tail word FAR from the value ⇒ stays 🔴            (false-negative shape)
                     · dated .tsv row ⇒ 🟠                                 (time-series capture)
                     · plain live copy ⇒ stays 🔴                          (the positive control)
  prose banner     — line-1 FROZEN/ARCHIVED <date> clears · mention / struck-through / no-date /
                     no-marker do not · overlap: _line_class dated-row rule unchanged (DOCKET L457)
"""
import sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import consumer_check as cc  # noqa: E402

FAILS = []
TOTAL = [0]
def check(name, cond, detail=""):
    TOTAL[0] += 1
    print(("  ✅ " if cond else "  ❌ ") + name + (f"  [{detail}]" if detail and not cond else ""))
    if not cond:
        FAILS.append(name)

def w(p: Path, text: str):
    p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text)

with tempfile.TemporaryDirectory() as td:
    ws = Path(td)
    # ── read_ledger ──
    w(ws / "led_commented.tsv", "# banner\n# second\nmetric\tvalue\tasof\tnote\nm\t5.9312\t2026-07-27\t\nm\t6.7391\t2026-08-28\t\n")
    w(ws / "led_clean.tsv", "metric\tvalue\tasof\tnote\nm\t5.9312\t2026-07-27\t\nm\t6.7391\t2026-08-28\t\n")
    w(ws / "led_midcomment.tsv", "metric\tvalue\tasof\tnote\nm\t5.9312\t2026-07-27\t\n# note between rows\nm\t6.7391\t2026-08-28\t\n")
    exp = {"m": ("6.7391", ["5.9312"])}
    print("read_ledger")
    check("comment above header → no phantom metric", cc.read_ledger(ws / "led_commented.tsv") == exp, str(cc.read_ledger(ws / "led_commented.tsv")))
    check("clean ledger unchanged", cc.read_ledger(ws / "led_clean.tsv") == exp)
    check("comment mid-file skipped", cc.read_ledger(ws / "led_midcomment.tsv") == exp)

    # ── line-class demotion (5-sig-digit needle so the sig-digit floor does not pre-empt;
    #    TWO scans of ≤COLLISION_FILE_CAP files each, because a context-less needle in >4 files
    #    is demoted as noise by the pre-existing collision pass — the first run of this suite
    #    tripped exactly that and every case went 🟠, positive control included) ──
    def scan_case(files):
        with tempfile.TemporaryDirectory() as td2:
            ws2 = Path(td2); own2 = ws2 / "AGENTS" / "X"; own2.mkdir(parents=True)
            for rel, text in files.items():
                w(ws2 / rel, text)
            st, cd, _m, _h = cc.scan(ws2, ["5.9312"], own2, current="6.7391")
            return {r[0] for r in st}, {r[0]: r[4] for r in cd}
    live = {"AGENTS/Y/STATUS.md": "Current CCC/BB ratio sits at 5.9312, per BROCK.\n"}
    print("line-class demotion — scan A (threshold forms)")
    S, C = scan_case({**live,
        "PROME/DOCKET.md": "W3 kill: CCC/BB ≤5.9312 ×2 obs — FROZEN falsifier\n",
        "AGENTS/Y/GATES.md": "trigger fires above 5.9312 consecutive prints\n"})
    check("plain live copy stays 🔴 (positive control)", "AGENTS/Y/STATUS.md" in S, f"stale={S} cand={C}")
    check("threshold operator ⇒ 🟠", "threshold operator" in C.get("PROME/DOCKET.md", ""), str(C))
    check("tail word NEAR value ⇒ 🟠", "within" in C.get("AGENTS/Y/GATES.md", ""), str(C))
    print("line-class demotion — scan B (false-negative shape + dated row)")
    S, C = scan_case({**live,
        "AGENTS/Y/FAR.md": "the level is 5.9312 today; " + ("x" * 60) + " consecutive sessions elsewhere\n",
        "AGENTS/Y/MARKET_DATA.tsv": "date\tseries\tvalue\n2026-07-27\tCCC-BB\t5.9312\n"})
    check("positive control again 🔴", "AGENTS/Y/STATUS.md" in S, f"stale={S}")
    check("tail word FAR from value stays 🔴", "AGENTS/Y/FAR.md" in S, f"stale={S} cand={set(C)}")
    check("dated .tsv row ⇒ 🟠", "HISTORY-ROW" in C.get("AGENTS/Y/MARKET_DATA.tsv", ""), str(C))

    # ── prose file-level dead banner (DOCKET L457, HAWK 9/28: ISO_DATE_RE was bound twice and
    #    the anchored L723 form shadowed the loose form file_is_dead() needs ⇒ no prose banner
    #    could ever clear). Conditions in AGENTS/DAEDALUS/runs/2026-10-01_L457_*.md ──
    print("prose dead banner (file_is_dead, rowish=False)")
    def dead(text, name="P.md"):
        f = ws / "banner" / name; w(f, text); return cc.file_is_dead(f, rowish=False)
    check("canon line-1 'FROZEN <date> — …' clears", dead("FROZEN 2026-09-22 — not maintained; STATUS is canonical\nbody 5.9312\n"))
    check("blockquote+emphasis+emoji prefix clears", dead("> ⚠️ **FROZEN 2026-07-12 — per-bank research** body\n"))
    check("heading-form banner clears", dead("# FROZEN 2026-09-22 — heartbeat plan record\n"))
    check("blank lines before the banner still read line 1", dead("\n\n> 🗄️ **ARCHIVED 2026-08-01** (WAL session)\n"))
    check("marker MENTIONED mid-line does not clear", not dead("# Notes on superseded values 2026-09-22\n"))
    check("marker in paragraph 2, not line 1, does not clear", not dead("# Live notes 2026-09-22\n\nFROZEN 2026-09-22 — quoted example\n"))
    check("struck-through (revoked) banner does not clear", not dead("> **🧊 ~~FROZEN 2026-07-04~~ — ⚖️ FREEZE LIFTED 2026-08-23** live book\n"))
    check("marker with no date does not clear", not dead("# FROZEN — verbatim rotation out of STATUS\n"))
    check("date with no marker does not clear", not dead("2026-09-22 — notes\n"))
    # independent read 2026-10-01 (❌ on condition 3): title-shaped first lines and a revoked banner
    check("title: '# Superseded-values ledger (<date>)' does not clear", not dead("# Superseded-values ledger (2026-09-01)\n"))
    check("title: '# ARCHIVED items index <date>' does not clear", not dead("# ARCHIVED items index 2026-09-01\n"))
    check("title: '> **Retired agents (<date>)**' does not clear", not dead("> **Retired agents (2026-09-01)**\n"))
    check("title: '# Frozen thresholds <date>' does not clear", not dead("# Frozen thresholds 2026-09-01\n"))
    check("revoked banner without strike-through does not clear", not dead("> ❌ FROZEN 2026-07-04 — FREEZE LIFTED 2026-08-23, live book\n"))
    check("LIVE pending pre-registration ('FROZEN GRADING CARD … <event date>') does not clear",
          not dead("# 🔒 FROZEN GRADING CARD — NFP SEPTEMBER · Fri 2026-10-02, 08:30 ET\n"))
    check("table first line '| FROZEN | <date> |' does not clear", not dead("| FROZEN | 2026-09-01 |\n"))
    check("'FROZEN until <date>' does not clear", not dead("FROZEN until 2026-12-01 pending review\n"))
    check("canon with colon form 'SUPERSEDED 2026-07-08:' clears", dead("> **SUPERSEDED 2026-07-08:** this remark was folded into STATUS\n"))
    # overlap: the anchored constant's own caller (_line_class) — the dated-row rule must still
    # need a BARE date in cell 1; a date-plus-text first cell is not a time-series capture
    check("overlap: bare-date first cell ⇒ HISTORY-ROW", "HISTORY-ROW" in (cc._line_class("2026-07-27\tCCC-BB\t5.9312", ["5.9312"], "x.tsv") or ""))
    check("overlap: date-plus-text first cell ⇒ not a history row", cc._line_class("2026-07-27 note\tCCC-BB\t5.9312", ["5.9312"], "x.tsv") is None)

print(f"\n{'PASS' if not FAILS else 'FAIL'}: {TOTAL[0] - len(FAILS)}/{TOTAL[0]} — {', '.join(FAILS) or 'all cases held'}")
sys.exit(1 if FAILS else 0)
