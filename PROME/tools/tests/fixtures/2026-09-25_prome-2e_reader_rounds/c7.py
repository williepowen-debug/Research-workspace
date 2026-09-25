import subprocess, sys, re, os
sys.path.insert(0,"/home/willi/Research-workspace/PROME/tools")
import spawn_list as S
R="/home/willi/Research-workspace"
raw=subprocess.run(["git","-C",R,"log","--since=2026-09-01","--format=%x1e%h\t%cs\t%s","--name-only"],capture_output=True,text=True).stdout
recs=list(S.parse_log_records(raw))
desks=sorted(d for d in os.listdir(R+"/AGENTS") if os.path.isdir(R+"/AGENTS/"+d) and re.fullmatch(r"[A-Z][A-Z0-9-]+",d))+["PROME"]
lost=gained=0; rej=[]
for h,ps in recs:
    sha,_,subj=h.split("\t",2)
    for d in desks:
        o=bool(S.STRONG(d).match(subj)); n=S.attributed(d,subj,ps)
        lost+= o and not n; gained+= n and not o
        if S.subject_pattern(d).match(subj) and not o and not n: rej.append((sha,d,subj[:70]))
print("commits",len(recs),"LOST",lost,"GAINED",gained,"REJECTED",len(rej)); [print("  ",r) for r in rej]
