"""One-off reproduction for the accompanying review; pinned source, no production writes."""
import ast
import re
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

REF = "99e66d32cc3b96fb6e5728254d09beb7309950c2"


def functions(path, names, env):
    source = subprocess.check_output(["git", "show", f"{REF}:{path}"], text=True)
    tree = ast.parse(source)
    tree.body = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    exec(compile(tree, path, "exec"), env)
    return env


pages = {
    "list": '<a href="new">公开市场业务交易公告 [2026]第218号</a>'
            '<a href="old">公开市场业务交易公告 [2026]第217号</a>',
    "new": "2026-11-10 09:00 固定利率 隔夜 1.50％",
    "old": "2026-11-09 09:00 固定利率 隔夜 1.25 %",
}
zhao = functions("AGENTS/ZHAO/scripts/boot.py",
                 {"_pboc_omo_latest", "_stored_rate", "_pboc_source_verdict"},
                 {"re": re, "PBOC_OMO_LIST": "list", "_curl": lambda u: pages[u]})
bad = zhao["_pboc_source_verdict"]("1.25 overnight", False)
print("Newest fixed-rate notice unparseable; older matches:", bad)
assert bad[:2] == (True, 0) and "217" in bad[2], "Pinned failure changed"
pages["new"] = "2026-11-10 09:00 固定利率 隔夜 1.50 %"
control = zhao["_pboc_source_verdict"]("1.25 overnight", False)
print("Parsable changed-rate control:", control)
assert control[:2] == (True, 1) and "218" in control[2]

with tempfile.TemporaryDirectory() as td:
    ledger = Path(td) / "ledger.tsv"
    ledger.write_text("date\tvix\tvix9d\tvix3m\tvix6m\tvvix\tbasis\n")
    violet = functions("AGENTS/VIOLET/scripts/thresholds.py", {"append_daily_log"},
                       {"datetime": datetime, "DAILY_LOG": ledger})
    row = dict(date="2026-09-07", vix=15.3, vix9d="", vix3m="", vix6m="", vvix="", basis="SETTLE")
    before = ledger.read_bytes()
    assert violet["append_daily_log"](row) == "skip-orphan-vix"
    assert ledger.read_bytes() == before
    row.update(date="2026-09-08", vix9d=14, vix3m=17, vix6m=18, vvix=90)
    assert violet["append_daily_log"](row) == "appended"
    print("VIOLET orphan nonmutation and normal-session controls: PASS")
print("Reproduction completed; ZHAO failure demonstrated, not fixed.")
