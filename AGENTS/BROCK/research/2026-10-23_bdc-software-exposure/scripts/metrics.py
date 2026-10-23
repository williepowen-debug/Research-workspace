import json,re,collections,sys
SP="/tmp/claude-1000/-home-willi-Research-workspace-PROME/8901ab4a-e7a6-4f42-afa6-5f001a17e8a4/scratchpad"
CUT={"ARCC":1930,"BXSL":901,"FSK":753,"GBDC":2075,"HTGC":10**8,"OBDC":791}
def name(t,i):
    i=i.replace("&amp;","&")
    if t=="HTGC" and i.count(",")>=2 and (i.startswith("Debt") or i.startswith("Equity") or i.startswith("Warrant")):
        i=i.split(",",2)[2]
    n=i.split(" | ")[0]
    n=re.sub(r"\(.*?\)","",n)
    n=re.sub(r"\s+\d+$","",n)
    if t=="FSK": n=n.split(",")[0]
    w=re.sub(r"[^a-z0-9 ]","",n.lower()).split()
    w=[x for x in w if x not in ("inc","llc","lp","corp","the","ltd","co","holdings","holding","holdco","parent","buyer","bidco","topco","midco","intermediate")]
    return " ".join(w[:2])
out={}
for t in CUT:
    R=json.load(open(f"{SP}/{t}_recs.json"))
    allU=[r for r in R if "InvestmentCompanyFinancialCommitmentToInvesteeFutureAmount" in r]
    P=[r for r in R if r["ord"]<=CUT[t] and "InvestmentOwnedAtFairValue" in r and not re.search(r"\bTotal\b",r["id"])]
    if t=="FSK": P=[r for r in P if " | " in r["id"]]
    if t=="BXSL": P=[r for r in P if r["ind"]!="Cash and Cash Equivalents" and "Money Market" not in r["id"]]
    def stats(S):
        fv=sum(r["InvestmentOwnedAtFairValue"] for r in S); cost=sum(r.get("InvestmentOwnedAtCost",0) for r in S)
        debt=[]; eq=[]
        for r in S:
            f=r["InvestmentOwnedAtFairValue"]; c=r.get("InvestmentOwnedAtCost",0); p=r.get("InvestmentOwnedBalancePrincipalAmount",0)
            if p and p>0:
                if r.get("par_unit")=="usd": parusd=p
                else: parusd=None
                if parusd: m=f/parusd if parusd else None
                else: m=f/c if c>0 else None; parusd=c
                if m is not None and parusd>0: debt.append((m,parusd,f,r))
            else: eq.append(r)
        par=sum(d[1] for d in debt); dfv=sum(d[2] for d in debt)
        b90=sum(d[1] for d in debt if d[0]<0.90); b80=sum(d[1] for d in debt if d[0]<0.80)
        f90=sum(d[2] for d in debt if d[0]<0.90); f80=sum(d[2] for d in debt if d[0]<0.80)
        iss=collections.defaultdict(lambda:[0,0]); 
        for m,pp,f,r in debt: k=name(t,r["id"]); iss[k][0]+=pp; iss[k][1]+=f
        n80=sum(1 for k,(pp,f) in iss.items() if pp>0 and f/pp<0.80); n90=sum(1 for k,(pp,f) in iss.items() if pp>0 and f/pp<0.90)
        eqfv=sum(r["InvestmentOwnedAtFairValue"] for r in eq); eqc=sum(r.get("InvestmentOwnedAtCost",0) for r in eq)
        worst=sorted(((f/pp,k,pp,f) for k,(pp,f) in iss.items() if pp>1e6),key=lambda x:x[0])[:8]
        return dict(fv=fv/1e6,cost=cost/1e6,fvc=fv/cost if cost else None,debtpar=par/1e6,debtfv=dfv/1e6,mark=dfv/par if par else None,
                    par_b90=b90/par if par else None,par_b80=b80/par if par else None,fv_b90=f90/fv,fv_b80=f80/fv,n_iss=len(iss),n90=n90,n80=n80,
                    eqfv=eqfv/1e6,eqc=eqc/1e6,worst=[(round(a,3),k,round(pp/1e6,1),round(f/1e6,1)) for a,k,pp,f in worst])
    S=[r for r in P if r["soft"]]; N=[r for r in P if not r["soft"]]
    s=stats(S); n=stats(N)
    softnames={name(t,r["id"]) for r in S}
    U=sum(r["InvestmentCompanyFinancialCommitmentToInvesteeFutureAmount"] for r in allU)/1e6
    US=sum(r["InvestmentCompanyFinancialCommitmentToInvesteeFutureAmount"] for r in allU if name(t,r["id"]) in softnames)/1e6
    out[t]=dict(soft=s,rest=n,totfv=sum(r["InvestmentOwnedAtFairValue"] for r in P)/1e6,unf_tagged=U,unf_soft=US)
    print(f"{t}: SOI FV {out[t]['totfv']:.0f}M | SOFT FV {s['fv']:.0f} cost {s['cost']:.0f} FV/cost {s['fvc']:.3f} | debt par {s['debtpar']:.0f} mark(FV/par) {s['mark']:.3f} | par<90 {100*s['par_b90']:.1f}% par<80 {100*s['par_b80']:.1f}% | FV<90 {100*s['fv_b90']:.1f}% FV<80 {100*s['fv_b80']:.1f}% | issuers {s['n_iss']} <90:{s['n90']} <80:{s['n80']} | equity FV {s['eqfv']:.0f}/cost {s['eqc']:.0f}")
    print(f"     REST: FV/cost {n['fvc']:.3f} mark {n['mark']:.3f} par<90 {100*n['par_b90']:.1f}% par<80 {100*n['par_b80']:.1f}% | unfunded tagged {U:.0f}M, to software names {US:.0f}M")
    print("     worst soft:",s["worst"])
json.dump(out,open(f"{SP}/metrics.json","w"),indent=1)
