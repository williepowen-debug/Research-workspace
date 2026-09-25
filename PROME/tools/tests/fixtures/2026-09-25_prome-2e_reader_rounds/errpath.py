import sys, pathlib, tempfile, os
sys.path.insert(0, "PROME/tools")
import prome_gate as G
def row(gate, state, surf):
    r = [""]*12; r[0], r[5], r[10] = gate, state, surf; return r
with tempfile.TemporaryDirectory(dir=sys.argv[1]) as t:
    root = pathlib.Path(t); (root/"A").mkdir()
    G.results.clear(); G.record_gate_citability([row("G-F","LIVE — x","A/MISSING.md")], root)
    print("unreachable →", [(r[0], r[1], r[2]) for r in G.results], "rc", G.aggregate_rc(G.results, []))
    (root/"A/locked.md").write_text("x"); os.chmod(root/"A/locked.md", 0)
    G.results.clear(); G.guard(G.record_gate_citability, [row("G-L","LIVE — x","A/locked.md")], root)
    print("unreadable →", [(r[0], r[1], r[3][:90]) for r in G.results], "rc", G.aggregate_rc(G.results, []))
    os.chmod(root/"A/locked.md", 0o600)
    (root/"A/dir.md").mkdir()
    G.results.clear(); G.record_gate_citability([row("G-D","LIVE — x","A/dir.md")], root)
    print("dir named .md →", [(r[0], r[1]) for r in G.results])
G.results.clear()
