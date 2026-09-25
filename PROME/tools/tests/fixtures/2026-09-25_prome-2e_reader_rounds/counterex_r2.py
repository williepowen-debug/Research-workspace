import sys, pathlib, tempfile, os
sys.path.insert(0, "PROME/tools")
import prome_gate as G
def row(gate, state, cond="crude MM shorts > x", surf="AGENTS/X/KB.md"):
    r = [""]*12; r[0], r[3], r[5], r[10] = gate, cond, state, surf; return r
tmp = tempfile.TemporaryDirectory(dir=sys.argv[1]); root = pathlib.Path(tmp.name)
for d in ("AGENTS/X", "AGENTS/Y/workbook", "FORUM/review", "memory/auto", "PROME"): (root/d).mkdir(parents=True)
(root/"AGENTS/X/CLEAN.md").write_text("letter clean\n")
(root/"AGENTS/X/UNVER.md").write_text("production UNVERIFIED — q\n")
(root/"AGENTS/X/STATUS.md").write_text("## 3\nattested\n## 7\nproduction UNVERIFIED — other letter\n")
(root/"AGENTS/Y/workbook/KB.tsv").write_text("KB-Y-1\tletter clean, attested 9/20\nKB-Y-2\tother letter: realisation UNKNOWN — needs pull\n")
(root/"AGENTS/Y/workbook/KB-Y-9.tsv").write_text("x\n")
(root/"FORUM/review/letter.txt").write_text("production UNVERIFIED — q\n")
(root/"memory/auto/x.md").write_text("realisation UNKNOWN\n")
(root/"PROME/GATES_README.md").write_text("production UNVERIFIED realisation UNKNOWN\n")
cases = {
 "R2-1 FORUM/ directory pointer (outside AGENTS|PROME|FORGE|KERNEL), LIVE —": [row("G-F", "LIVE — x", surf="FORUM/review (letter)")],
 "R2-2 lower-case root dir pointer memory/auto": [row("G-M", "LIVE — x", surf="memory/auto (slug x)")],
 "R2-3 real summary file + directory pointer to the actual letter": [row("G-B", "LIVE — ARMED", surf="AGENTS/X/CLEAN.md (summary) + letter at AGENTS/Y/workbook (KB-Y-2)")],
 "R2-4 one good file + one missing file (read/unread overlap)": [row("G-O", "LIVE — x", surf="AGENTS/X/CLEAN.md + AGENTS/X/MISSING.md")],
 "R2-5 dup gate_id: row1 NOT ARMED cites UNVER, row2 LIVE — cites CLEAN only": [row("G-D", "LIVE / NOT ARMED — p", surf="AGENTS/X/UNVER.md"), row("G-D", "LIVE — x", surf="AGENTS/X/CLEAN.md")],
 "R2-6 README-only surface": [row("G-R", "LIVE — x", surf="PROME/GATES_README.md")],
 "R2-7 NONE | prose (M-09 successor)": [row("G-N", "LIVE — x", surf="NONE | consumer is a thesis leg (M-09 successor)")],
 "R2-8 see AGENTS/X/STATUS.md §3 (token only in §7)": [row("G-S", "LIVE — x", surf="see AGENTS/X/STATUS.md §3")],
 "R2-9 .tsv row pointer KB-Y-1 clean, token in KB-Y-2 of same file": [row("G-T", "LIVE — x", surf="AGENTS/Y/workbook/KB.tsv (KB-Y-1)")],
 "R2-10 prose mentions a dir after a real file: 'AGENTS/X/CLEAN.md; owner AGENTS/X/ desk'": [row("G-P", "LIVE — x", surf="AGENTS/X/CLEAN.md; owner AGENTS/X/ desk")],
 "R2-11 prose-only cell mentioning an agent dir: 'owner-side, see AGENTS/FLG/ register'": [row("G-Q", "LIVE — x", surf="owner-side, see AGENTS/X/ register")],
 "R2-12 token-bearing .txt letter under FORUM/": [row("G-TXT", "LIVE — x", surf="FORUM/review/letter.txt")],
}
for k, rows in cases.items():
    o = G.scan_gate_citability(rows, root)
    print(f"{k}\n   viol={o['violations']} unreach={o['unreachable']} read={o['read']}/{o['live']} unread={o['unread']}\n   detail: {G.citability_detail(o)}")
tmp.cleanup()
