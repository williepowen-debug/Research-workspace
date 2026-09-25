import subprocess, sys, re, os
sys.path.insert(0,"/home/willi/Research-workspace/PROME/tools")
import spawn_list as S
R="/home/willi/Research-workspace"
desks=sorted(d for d in os.listdir(R+"/AGENTS") if os.path.isdir(R+"/AGENTS/"+d) and re.fullmatch(r"[A-Z][A-Z0-9-]+",d))+["PROME"]
allc=subprocess.run(["git","-C",R,"log","--since=2026-09-01","--format=%h\t%s"],capture_output=True,text=True).stdout.splitlines()
miss=0; maxrank={}
for d in desks:
    pyset={l.split("\t",1)[0] for l in allc if S.subject_pattern(d).match(l.split("\t",1)[1])}
    g=subprocess.run(["git","-C",R,"log","--since=2026-09-01","--format=%h","--extended-regexp",f"--grep={S.grep_pattern(d)}"],capture_output=True,text=True).stdout.split()
    lost=pyset-set(g); miss+=len(lost)
    if lost: print("PREFILTER DROPS",d,sorted(lost)[:5])
    # rank of first attributed hit in the live n=40 window
    raw=subprocess.run(["git","-C",R,"log","-n","40","--format=%x1e%cs\t%h\t%s","--name-only","--extended-regexp",f"--grep={S.grep_pattern(d)}"],capture_output=True,text=True).stdout
    for i,(h,p) in enumerate(S.parse_log_records(raw)):
        f=h.split("\t",2)
        if S.attributed(d,f[2],p): maxrank[d]=i; break
    else: maxrank[d]=None
print("prefilter drops total:",miss)
print("rank of newest attributed commit within the 40-window (0=first):",sorted(maxrank.items(),key=lambda x:-(x[1] or 0))[:6])
