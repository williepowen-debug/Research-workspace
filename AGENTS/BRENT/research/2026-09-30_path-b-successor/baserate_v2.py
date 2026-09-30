"""BRT-31 base rate v2 (BRENT 2026-09-30, after CARL's blind read 13aa2cd46).
Grades each historical window by the LETTER, first-terminal-event-wins, in data-week order:
  - price check per window week: GASREGW on the Monday after the data week vs the obs 364 days earlier;
    the 3rd week with YoY < +20% => NOT-FIRED-PRECONDITION (terminal) at that week;
  - MET at the first consecutive pair <= T (terminal) at the pair's second week;
  - same week: NOT-FIRED wins (refusal wins ties);
  - window end with neither: NOT MET if every print > NV, else NO-VERDICT.
Reuses baserate.py's data/helpers. Rows = (week, 4wk YoY, min 12wk price YoY)."""
import os, sys, datetime as dt, io, contextlib
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
with contextlib.redirect_stdout(io.StringIO()): import baserate as b
def pyoy(w):
    a=b.near(w+dt.timedelta(days=3)); c=b.near(w+dt.timedelta(days=3-364)); return (a/c-1)*100
def grade(i,T,NV,L=8,K=2,pre=True):
    win=b.rows[i+1:i+1+L]
    if len(win)<L or (win[-1][0]-b.rows[i][0]).days>7*L+3: return None
    low=0
    for k,(w,y,_) in enumerate(win):
        if pre and pyoy(w)<20:
            low+=1
            if low>=3: return "NOT_FIRED"
        if k>=1 and y<=T and win[k-1][1]<=T: return "MET"
    return "NOT_MET" if all(x[1]>NV for x in win) else "NO_VERDICT"
def table(filt,T,pre,excl=lambda w:False,cluster=False):
    out=[]; 
    for i,(w,y,py) in enumerate(b.rows):
        if filt(y,py) and not excl(w):
            g=grade(i,T,-1.0,pre=pre)
            if g: out.append((w,g))
    n=len(out); fired=[g for _,g in out if g!="NOT_FIRED"]
    pct=lambda xs,s: round(100*sum(x==s for x in xs)/len(xs)) if xs else None
    res=dict(n=n,not_fired=pct([g for _,g in out],"NOT_FIRED"),fired_n=len(fired),MET=pct(fired,"MET"),NOT_MET=pct(fired,"NOT_MET"),NV=pct(fired,"NO_VERDICT"))
    if cluster:  # equal weight per cluster (split on >9-week gap), fired windows only
        cl=[]; prev=None
        for w,g in out:
            if prev is None or (w-prev).days>63: cl.append([])
            cl[-1].append(g); prev=w
        fcl=[[g for g in c if g!="NOT_FIRED"] for c in cl]; fcl=[c for c in fcl if c]
        res["clusters"]=len(cl); res["cw_MET"]=round(100*sum(sum(g=="MET" for g in c)/len(c) for c in fcl)/len(fcl))
        res["cw_NOT_MET"]=round(100*sum(sum(g=="NOT_MET" for g in c)/len(c) for c in fcl)/len(fcl))
    return res
HP=lambda y,py: py>=20 and y>=-0.5
ORD=lambda y,py: py<20 and y>=-0.5
for T in (-1.5,-2.0):
    print(f"T<={T}  HIGH-PRICE, letter as written (in-window precondition):", table(HP,T,True,cluster=True))
    print(f"T<={T}  HIGH-PRICE, ex-2022 (COVID-era base):             ", table(HP,T,True,excl=lambda w:w.year==2022,cluster=True))
    print(f"T<={T}  ORDINARY (min 12wk price YoY <20), no precondition:", table(ORD,T,False))
