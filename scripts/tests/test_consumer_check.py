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
"""
import sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import consumer_check as cc  # noqa: E402

FAILS = []
def check(name, cond, detail=""):
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

print(f"\n{'PASS' if not FAILS else 'FAIL'}: {9 - len(FAILS)}/9 — {', '.join(FAILS) or 'all cases held'}")
sys.exit(1 if FAILS else 0)
