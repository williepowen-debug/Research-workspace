import subprocess, sys, re, collections
sys.path.insert(0,"/home/willi/Research-workspace/PROME/tools")
import spawn_list as S
R="/home/willi/Research-workspace"
raw=subprocess.run(["git","-C",R,"log","--since=2026-09-01","--format=%x1e%h\t%cs\t%s","--name-only"],capture_output=True,text=True).stdout
recs=[(h.split("\t",2),p) for h,p in S.parse_log_records(raw)]
import os
desks=sorted(d for d in os.listdir(R+"/AGENTS") if os.path.isdir(R+"/AGENTS/"+d) and re.fullmatch(r"[A-Z][A-Z0-9-]+",d))+["PROME"]
print("commits",len(recs),"desks",len(desks))
quoted=[(h[0],p) for h,ps in recs for p in ps if p.startswith('"')]
print("quoted paths since 9/1:",len(quoted), quoted[:5])
inbox_only=[];unhomed=[];nopaths=[]
for (sha,d8,subj),ps in recs:
    for d in desks:
        if S.STRONG(d).match(subj) or not S.subject_pattern(d).match(subj): continue
        if not S.attributed(d,subj,ps): continue
        home="PROME/" if d=="PROME" else f"AGENTS/{d}/"
        hp=[p for p in ps if p.startswith(home)]
        if d!="PROME" and hp and all(p.startswith(home+"inbox/") for p in hp):
            inbox_only.append((sha,d8,d,subj[:90],hp[:3],[p for p in ps if not p.startswith(home)][:3]))
        elif not hp and ps and not all(S._PACKET.match(p) or p.startswith("memory/auto/") or p in S._SHARED_LOGS for p in ps):
            unhomed.append((sha,d8,d,subj[:90],ps[:4]))
        elif not ps:
            nopaths.append((sha,d8,d,subj[:90]))
print("\nLOOSE-FORM attributed where the desk's ONLY home paths are under its own inbox/ :",len(inbox_only))
for x in inbox_only: print("  ",x)
print("\nLOOSE-FORM attributed with NO home path, via un-homed (non-packet, non-memory/auto) paths:",len(unhomed))
for x in unhomed: print("  ",x)
print("\nLOOSE-FORM attributed with NO paths (empty/merge):",len(nopaths))
for x in nopaths: print("  ",x)
