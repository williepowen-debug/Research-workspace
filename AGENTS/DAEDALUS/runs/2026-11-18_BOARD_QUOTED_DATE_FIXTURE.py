import sys, importlib.util, io, contextlib, datetime as dt, subprocess
from pathlib import Path
R = Path("/home/willi/Research-workspace"); S = Path(sys.argv[1]); FX = S/"fx"; which = sys.argv[2]
desks = ["RED","TERRY","PROME","CARL","HENRY","REGINALD"]
FM = '''---
signal_id: "SIG-W-20261110-{n}"
date: "2026-11-10"
timestamp: "2026-11-10T15:19:18Z"
dispatched: "2026-11-10T15:19:18Z"
action: ["{d}"]
info: ["BROCK"]
precedence: "PRIORITY"
---

# Fixture quoted-date signal for {d}
'''
for i, d in enumerate(desks):
    n = f"9{i:02d}"
    t = FM.format(n=n, d=d)
    (FX/"BOARD"/f"SIG-W-20261110-{n}-fixture-{d.lower()}.md").write_text(t)
    if d in ("HENRY","REGINALD"):
        (FX/"AGENTS"/d/"inbox"/"WALTER"/f"SIG-W-20261110-{n}-fixture-{d.lower()}.md").write_text(t)
(FX/"AGENTS/RED/board_log.tsv").write_text("timestamp_read\tsignal_id\tdisposition\tsource\tnotes\n")
(FX/"AGENTS/TERRY/board_log.tsv").write_text("timestamp_read\tsignal_id\tdisposition\tsource\tnotes\n")
(FX/"AGENTS/HENRY/board_log.tsv").write_text("timestamp_read\tsignal_id\n")
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(Path(path).parent)); spec.loader.exec_module(m); return m
today = dt.date(2026, 11, 18)
out = io.StringIO()
with contextlib.redirect_stdout(out):
    if which == "RED":
        m = load("redboot", R/"AGENTS/RED/scripts/boot.py"); m.REPO = FX; m.RED = FX/"AGENTS/RED"; m.section_board_gap(True)
    elif which in ("TERRY", "TERRY_PREFIX"):
        p = R/"AGENTS/TERRY/scripts/boot.py" if which == "TERRY" else S/"terry_boot_prefix.py"
        sys.path.insert(0, str(R/"AGENTS/TERRY/scripts"))
        m = load("terryboot", p); print("RESULT", m.board_gap(FX/"BOARD", FX/"AGENTS/TERRY", today))
    elif which == "EXEMPT":
        m = load("exempt_gap", R/"PROME/tools/exempt_gap.py"); rows, note, inst = m.scan(FX, today, 0, desks=["RED","TERRY","CARL"])
        print("ROWS", rows); print("INSTR", inst)
    elif which == "BOARDSCAN":
        m = load("board_scan", R/"PROME/tools/board_scan.py")
        f = next((FX/"BOARD").glob("*prome.md")); s = m.inspect_signal(f.name, f.read_text())
        print("SIGNAL", vars(s))
    elif which == "HENRY":
        m = load("henryboot", R/"AGENTS/HENRY/scripts/boot.py"); m.HENRY_DIR = FX/"AGENTS/HENRY"
        print("RESULT", m.walter_lane_backlog(today))
    elif which == "REGINALD":
        m = load("regboot", R/"AGENTS/REGINALD/scripts/boot.py"); m.DESK = FX/"AGENTS/REGINALD"; print("RESULT", m.check_inbox())
    elif which == "CARL":
        m = load("carlgap", R/"AGENTS/CARL/scripts/board_gap.py")
        rows = [r for r in m.index_rows() if r[0] in ("SIG-W-20261118-003", "SIG-W-20261117-001")]
        import re; q = [l for l in (R/"BOARD").glob("SIG-W-202611*.md") if re.search(r'^date: "', l.read_text(), re.M)]
        ids = {re.match(r"SIG-W-\d{8}-\d{3}", l.name).group(0) for l in q}
        allidx = {r[0] for r in m.index_rows()}
        print("quoted-date Nov files", len(ids), "missing from INDEX rows CARL parses:", sorted(ids - allidx))
print(out.getvalue()[-2500:])
