import sys, pathlib, tempfile
sys.path.insert(0, "PROME/tools")
import prome_gate as G
real = (G.ROOT/"PROME/GATES.tsv").read_text(encoding="utf-8").split("\n")
hi = next(i for i, l in enumerate(real) if l.startswith("gate_id\t"))
def run(label, hdr_line, extra_rows=()):
    with tempfile.TemporaryDirectory(dir=sys.argv[1]) as t:
        root = pathlib.Path(t); (root/"PROME").mkdir()
        lines = real[:]; lines[hi] = hdr_line
        lines += list(extra_rows)
        (root/"PROME/GATES.tsv").write_text("\n".join(lines), encoding="utf-8")
        saved = G.ROOT; G.ROOT = root; G.results.clear()
        try: G.guard(G.check_gates_tsv)
        finally: G.ROOT = saved
        print(label); [print("   ", r[0], "|", r[1], "|", r[2], "|", str(r[3])[:110]) for r in G.results]
        print("    rc", G.aggregate_rc(G.results, [])); G.results.clear()
h = real[hi].split("\t"); print("live header:", h)
# drift only in definition_surface name; plus a FIRED-UNEXECUTED row to show it goes unevaluated
fired = "GATE-ZZ\t2026-09-25\tX\tcond\tc\tFIRED-UNEXECUTED 9/25\t\t\tNONE\tJUDGEMENT\tAGENTS/X/a.md\t2026-09-30"
h2 = h[:]; h2[10] = "definition_home"
run("A) col-10 renamed + a FIRED-UNEXECUTED row", "\t".join(h2), [fired])
h3 = h[:]; h3[0] = "gate"
run("B) header first cell renamed (assertion skipped?)", "\t".join(h3))
