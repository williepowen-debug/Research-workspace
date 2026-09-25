import sys, pathlib, tempfile
sys.path.insert(0, "PROME/tools")
import prome_gate as G
def row(gate, state, cond="crude MM shorts > x", surf="AGENTS/X/KB.md", n=12):
    r = [""] * max(n, 11); r[0], r[3], r[5] = gate, cond, state
    if n > 10: r[10] = surf
    return r[:n]
tmp = tempfile.TemporaryDirectory(dir=sys.argv[1]); root = pathlib.Path(tmp.name)
(root/"AGENTS/X").mkdir(parents=True); (root/"PROME").mkdir()
(root/"AGENTS/X/KB.tsv").write_text("KB-X-1\tletter: SOFR>IORB; production UNVERIFIED — query: run SOFR99\n")
(root/"AGENTS/X/UNVER.md").write_text("letter production UNVERIFIED — query: x\n")
(root/"AGENTS/X/spec.json").write_text('{"letter": "realisation UNKNOWN — needs history pull"}\n')
(root/"AGENTS/X/WRAP.md").write_text("letter: strict >12.00; production\nUNVERIFIED — query: Trepp pull\n")
(root/"AGENTS/X/STATUS.md").write_text("## GATE-A\nattested 9/20.\n## other thesis\nKB-77 production UNVERIFIED — query: y\n")
(root/"PROME/GATES_README.md").write_text("rule prose: production UNVERIFIED and realisation UNKNOWN\n")
outside = pathlib.Path(sys.argv[1])/"outside_root.md"; outside.write_text("production UNVERIFIED — outside root\n")
cases = {
 "CE1 directory pointer (live LIQ-069/072 shape), KB.tsv carries token, LIVE — lead":
    [row("G-DIR", "LIVE — **ARMED 1-of-2", surf="AGENTS/X (KB-X-1)")],
 "CE2 duplicate gate_id: first NOT ARMED, second LIVE — on same file":
    [row("G-DUP", "LIVE / NOT ARMED — attestation pending: x", surf="AGENTS/X/UNVER.md"),
     row("G-DUP", "LIVE — armed", surf="AGENTS/X/UNVER.md")],
 "CE3 non-.md/.tsv surface (.json) with token, LIVE —":
    [row("G-JSON", "LIVE — x", surf="AGENTS/X/spec.json")],
 "CE4 short row (10 cells, no definition_surface) LIVE — with token in CONDITION cell":
    [row("G-SHORT", "LIVE — x", cond="≥30bp — realisation UNKNOWN", n=10)],
 "CE5 FIRED-UNEXECUTED row, letter carries token":
    [row("G-FIRED", "FIRED-UNEXECUTED 9/25", surf="AGENTS/X/UNVER.md")],
 "CE6 token wrapped across a line break, LIVE —":
    [row("G-WRAP", "LIVE — x", surf="AGENTS/X/WRAP.md")],
 "CE7 ./PROME/GATES_README.md spelled with ./ (README guard is exact-string)":
    [row("G-README", "LIVE — x", surf="./PROME/GATES_README.md")],
 "CE8 absolute path outside root":
    [row("G-ABS", "LIVE — x", surf=str(outside))],
 "CE9 section pointer into a shared STATUS.md; token belongs to a different section":
    [row("G-A", "LIVE — x", surf="AGENTS/X/STATUS.md §GATE-A")],
 "CE10 bare .md basename present at root only via subdir":
    [row("G-BASE", "LIVE — x", surf="UNVER.md (see AGENTS/X)")],
}
for k, rows in cases.items():
    try:
        o = G.scan_gate_citability(rows, root)
        print(f"{k}\n   violations={o["violations"]} unreachable={o["unreachable"]} files={o["files"]} read={o.get("read")}/{o.get("live")} unread={o.get("unread")} short={o.get("short")}\n   detail: {G.citability_detail(o)}")
    except Exception as e:
        print(f"{k}\n   RAISED {type(e).__name__}: {e}")
tmp.cleanup(); outside.unlink()
