import sys; sys.path.insert(0,"code")
from uni import *
C={"2170","2122","J454","PV05","PV06","PV07","PV08","PV09","PV11","PV12","PV23","PV24","PV25","8274","P859","3792","3210","A222","J451","5369","1403"}
F=("RCFD","RCON"); D={}
for q in("12312025","06302026","09302026"): D[q]=load("bulk/"+q,C)
def v(q,r,c,pref=F):
    e=D[q][1].get(r,{}); 
    for p in pref+("RCFA","RCOA"):
        if p+c in e: return float(e[p+c])
k,o=D["09302026"]
R=[]
for r in o:
    a=v("09302026",r,"PV05")
    R.append((r,k[r][0],v("09302026",r,"2170") or 0,a))
big=[x for x in R if x[2]>=1e7]
print("filers",len(R),"assets>=10B",len(big),"PV05 present",sum(x[3] is not None for x in R),"present >=10B",sum(x[3] is not None for x in big),"present <10B",sum(x[3] is not None for x in R if x[2]<1e7))
print(">=10B missing PV05:",[x[1] for x in big if x[3] is None])
tot=lambda q:(sum(v(q,r,"PV05") or 0 for r in D[q][1]),sum(v(q,r,"J454") or 0 for r in D[q][1]),sum((v(q,r,"PV05") is not None) for r in D[q][1]))
for q in D: print(q,"sum PV05 $M, 9.a $M, n",[round(x/1e3) for x in tot(q)[:2]],tot(q)[2], "9.a at non-splitters $M",round(sum((v(q,r,"J454") or 0) for r in D[q][1] if v(q,r,"PV05") is None)/1e3))
rows=[]
for r,n,A,a in R:
    if not a: continue
    q="09302026"; L=v(q,r,"2122"); t1=v(q,r,"8274"); 
    if t1 is None: t1=v(q,r,"3210")
    rows.append(dict(r=r,n=n,A=A/1e3,a=a/1e3,L=100*a/L if L else 0,t=100*a/t1 if t1 else 0,u=(v(q,r,"PV12") or 0)/1e3,uk=v(q,r,"PV12") is not None,a2=(v("06302026",r,"PV05") or 0)/1e3,ye=(v("12312025",r,"PV05") or 0)/1e3,pd=(v(q,r,"PV23") or 0)/1e3,p90=(v(q,r,"PV24") or 0)/1e3,na=(v(q,r,"PV25") or 0)/1e3,nd=(v(q,r,"J454") or 0)/1e3,don=(v(q,r,"PV05",("RCON",)) or 0)/1e3,t1=t1/1e3,tc=(v(q,r,"3792") or 0)/1e3))
h=f"{'RSSD':8}{'bank':34}{'assets':>9}{'M10a':>8}{'YE25':>8}{'Q2':>8}{'%loan':>7}{'%T1':>7}{'unused':>8}{'%T1+u':>7}{'NA ndfi':>8}{'30-89':>7}{'domst':>8}"
def pr(x): print(f"{x['r']:8}{x['n'][:33]:34}{x['A']:9.0f}{x['a']:8.0f}{x['ye']:8.0f}{x['a2']:8.0f}{x['L']:7.2f}{x['t']:7.1f}{x['u']:8.0f}{100*(x['a']+x['u'])/x['t1']:7.1f}{x['na']:8.1f}{x['pd']:7.1f}{x['don']:8.0f}")
print("\nTOP 30 by %T1, M10a>=100M"); print(h)
for x in sorted([x for x in rows if x['a']>=100],key=lambda x:-x['t'])[:30]: pr(x)
print("\nTOP 20 by $"); 
for x in sorted(rows,key=lambda x:-x['a'])[:20]: pr(x)
print("\nMINE"); M="107244 3138146 2652092 276579 1929247 3303298 3938186 34537 83638 694904 501105 12311 229801 2354985".split()
by={x['r']:x for x in rows}
for r in sorted(M,key=lambda r:-(by[r]['t'] if r in by else -1)):
    if r in by: pr(by[r])
    else: print(r,k[r][0],"PV05=",v("09302026",r,"PV05"),"9.a $M",(v("09302026",r,"J454") or 0)/1e3,"unused PV12",v("09302026",r,"PV12"))
top=sorted([x['a'] for x in rows],reverse=True); s=sum(top); print("top4/10 share",sum(top[:4])/s,sum(top[:10])/s, "n>0",len(top), "n %T1>=50",sum(x['t']>=50 for x in rows),">=25",sum(x['t']>=25 for x in rows))
print("median %T1 of >=10B filers",sorted((by[x[0]]['t'] if x[0] in by else 0) for x in big)[len(big)//2])
print("\nnon-splitters <10B: top 9.a % of T1 (NOT decomposed)")
ns=[(100*(v("09302026",r,"J454") or 0)/(v("09302026",r,"8274") or v("09302026",r,"3210") or 1e12),n,A/1e3,(v("09302026",r,"J454") or 0)/1e3) for r,n,A,a in R if a is None and (v("09302026",r,"J454") or 0)>=1e5]
for x in sorted(ns,reverse=True)[:12]: print([round(x[0],1),x[1],round(x[2]),round(x[3])])
