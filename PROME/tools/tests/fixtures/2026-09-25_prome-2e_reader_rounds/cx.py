import os, pathlib, subprocess, sys, tempfile
sys.path.insert(0, "/home/willi/Research-workspace/PROME/tools")
import spawn_list as S, desk_activity as DA
def g(repo,*a): return subprocess.run(["git","-C",str(repo),*a],capture_output=True,text=True,check=True).stdout
def commit(repo, subj, paths, mv=None):
    if mv:
        src,dst=mv; (repo/dst).parent.mkdir(parents=True,exist_ok=True); g(repo,"mv",src,dst)
    for p in paths:
        f=repo/p; f.parent.mkdir(parents=True,exist_ok=True); f.write_text(subj+os.urandom(4).hex()); g(repo,"add","--",p)
    g(repo,"commit","-q","--allow-empty" if not paths and not mv else "-q","-m",subj)
    return g(repo,"rev-parse","--short","HEAD").strip()
def fresh(name):
    d=pathlib.Path(sys.argv[1])/name
    subprocess.run(["rm","-rf",str(d)]); d.mkdir(parents=True)
    g(d,"init","-q","-b","master"); g(d,"config","user.email","t@t"); g(d,"config","user.name","t")
    return d
def show(repo, desk):
    S.ROOT=repo
    a=S.Liveness(None).last_self_commit(desk); b=DA.last_commit(repo,desk)
    print(f"  last_self_commit({desk}) = {a}   desk_activity = {b and (b['sha'][:9], b['subject'])}")
# CX1: another desk delivers a packet INTO the named desk's inbox under a loose subject naming the recipient
r=fresh("cx1"); print("CX1 recipient-named loose subject + packet into recipient's inbox (carve-out 1, authored by MIDAS)")
commit(r,"HAWK: baseline own commit",["AGENTS/HAWK/STATUS.md"])
g(r,"commit","-q","--allow-empty","--date=2026-09-01T00:00:00","-m","noop") if False else None
sha=commit(r,"HAWK L433 re-grade request from MIDAS (carve-out 1)",["AGENTS/HAWK/inbox/2026-09-25_from-MIDAS_regrade.md","AGENTS/MIDAS/STATUS.md"])
print("  cx commit",sha); show(r,"HAWK")
sha2=commit(r,"HAWK packet delivered by PROME",["AGENTS/HAWK/inbox/2026-09-25_from-PROME_task.md"])
print("  cx commit (PROME packet only)",sha2); show(r,"HAWK")
# CX2: PROME consume-move of a desk packet within the desk's own inbox (rename -> only NEW path printed)
r=fresh("cx2"); print("CX2 PROME moves AGENTS/BOND/inbox/x.md -> AGENTS/BOND/inbox/processed/x.md, loose subject")
commit(r,"BOND: old own",["AGENTS/BOND/STATUS.md"])
commit(r,"PROME -> BOND: task",["AGENTS/BOND/inbox/2026-09-20_from-PROME_t.md"])
sha=commit(r,"BOND packet -> processed (PROME L0 drain)",[],mv=("AGENTS/BOND/inbox/2026-09-20_from-PROME_t.md","AGENTS/BOND/inbox/processed/2026-09-20_from-PROME_t.md"))
print("  cx commit",sha, "paths:", g(r,"show","--name-only","--format=",sha).split()); show(r,"BOND")
# CX3: quotePath — another desk's home path with non-ASCII char, loose subject naming a different desk
r=fresh("cx3"); print("CX3 MIDAS commit, loose subject 'ZHAO refuted …', MIDAS path contains non-ASCII (quoted by core.quotePath)")
sha=commit(r,"ZHAO refuted my amendment rule",["AGENTS/MIDAS/notes/zhao_réfutation.md"])
print("  cx commit",sha,"raw name-only:",repr(g(r,"log","-1","--name-only","--format=%x1e%s")))
show(r,"ZHAO")
# CX4: PROME commit, loose subject naming a desk, touching only un-homed PROME-adjacent paths (docs/, memory daily, .claude/)
r=fresh("cx4"); print("CX4 PROME commit 'YURI registered …' touching docs/ + memory/<date>.md + .claude/ only")
sha=commit(r,"YURI onboarding recorded in provenance",["docs/CANON_PROVENANCE.md","memory/2026-09-25.md",".claude/skills/boot/SKILL.md"])
print("  cx commit",sha); show(r,"YURI")
# CX5: merge commit with loose subject (no paths shown by --name-only)
r=fresh("cx5"); print("CX5 merge commit whose subject names a desk")
commit(r,"PROME: base",["PROME/a.md"]); g(r,"checkout","-q","-b","side"); commit(r,"PROME: side",["PROME/b.md"]); g(r,"checkout","-q","master"); commit(r,"PROME: main",["PROME/c.md"])
g(r,"merge","-q","--no-ff","side","-m","TERRY sweep merged by PROME")
print("  merge paths:",repr(g(r,"log","-1","--name-only","--format=%x1e%s"))); show(r,"TERRY")
# CX6: lane depth two / lane packet with processed lane
r=fresh("cx6"); print("CX6 own loose commit whose only paths are a 2-level lane packet in another desk (carve-out 1 into a nested lane)")
sha=commit(r,"OTTO s023 packet to WAL",["AGENTS/WAL/inbox/WALTER/urgent/SIG-9.md"]); show(r,"OTTO")
