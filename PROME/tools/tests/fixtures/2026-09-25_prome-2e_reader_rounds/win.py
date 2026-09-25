import subprocess, sys, re, os
sys.path.insert(0,"/home/willi/Research-workspace/PROME/tools")
import spawn_list as S
R="/home/willi/Research-workspace"
desks=sorted(d for d in os.listdir(R+"/AGENTS") if os.path.isdir(R+"/AGENTS/"+d) and re.fullmatch(r"[A-Z][A-Z0-9-]+",d))+["PROME"]
print("hyphenated desks:",[d for d in desks if "-" in d])
def run(desk,n,until,grep):
    cmd=["git","-C",R,"log","--no-merges","--format=%x1e%cs\t%h\t%s","--name-only","--extended-regexp",f"--grep={grep}"]
    if n: cmd[4:4]=["-n",str(n)]
    if until: cmd.append(f"--until={until}")
    return list(S.parse_log_records(subprocess.run(cmd,capture_output=True,text=True).stdout))
def new(desk,n,until):
    recs=run(desk,n,until,S.grep_pattern(desk))
    for h,p in recs:
        f=h.split("\t",2)
        if len(f)==3 and S.attributed(desk,f[2],p): return (f[0],f[1]),len(recs)
    return None,len(recs)
def old(desk,until):
    pat=re.compile(rf"^{re.escape(desk)}( ->|:)")
    for h,p in run(desk,40,until,f"^{re.escape(desk)}( ->|:)"):
        f=h.split("\t",2)
        if len(f)==3 and pat.match(f[2]): return (f[0],f[1])
    return None
bad=0
for until in [None,"2026-09-20","2026-09-10","2026-09-01"]:
    for d in desks:
        n40,_=new(d,40,until); nall,_=new(d,0,until); o=old(d,until)
        flag=[]
        if n40!=nall: flag.append("WINDOW-TRUNCATION n40=%s unlimited=%s"%(n40,nall))
        if o and (n40 is None or n40[0]<o[0]): flag.append("REGRESSION vs old: old=%s new=%s"%(o,n40))
        if flag: bad+=1; print(until,d,flag)
print("flags:",bad)
