import re,sys,json,collections
from rows import rows
SOFT={"ARCC":r"Software and Services","BXSL":r"Software","FSK":r"Software & Services","GBDC":r"Software","HTGC":r"(Application|System) Software","OBDC":r"Internet software and services"}
STOP={"Interest"}
def norm(h):
    h=re.sub(r'\s*\(continued\)\s*$','',h,flags=re.I)
    h=re.sub(r'\(\d+\)$','',h).strip()
    return h
def load_xbrl(path,instant):
    s=open(path,encoding='utf-8',errors='replace').read()
    ctx={}
    for cid,body in re.findall(r'<context id="([^"]+)">(.*?)</context>',s,re.S):
        m=re.search(r'dimension="us-gaap:InvestmentIdentifierAxis">\s*<[^>]+>(.*?)</',body,re.S)
        p=re.search(r'<instant>([^<]+)</instant>',body)
        if m and p and p.group(1)==instant:
            dims=re.findall(r'dimension="([^"]+)"',body)
            ctx[cid]=(re.sub(r'\s+',' ',m.group(1)).strip(),dims)
    facts=collections.defaultdict(dict)
    for name in ["InvestmentOwnedAtFairValue","InvestmentOwnedAtCost","InvestmentOwnedBalancePrincipalAmount","InvestmentCompanyFinancialCommitmentToInvesteeFutureAmount","InvestmentInterestRatePaidInKind","InvestmentOwnedBalanceShares"]:
        for m in re.finditer(r'<us-gaap:%s\b([^>]*)>([^<]*)</us-gaap:%s>'%(name,name),s):
            a=m.group(1); c=re.search(r'contextRef="([^"]+)"',a).group(1)
            if c in ctx:
                try: facts[c][name]=float(m.group(2))
                except: pass
                u=re.search(r'unitRef="([^"]+)"',a)
                if name=="InvestmentOwnedBalancePrincipalAmount" and u: facts[c]["par_unit"]=u.group(1)
    return ctx,facts
def industry_map(htmlpath,tk):
    cur=None; mp={}; order={}; k=0
    softpat=re.compile(SOFT[tk])
    for t,f in rows(htmlpath):
        if not f:
            if len(t)==1 and len(t[0])<70 and not t[0].endswith(':') and not t[0].startswith('Total'):
                h=norm(t[0])
                if h not in STOP: cur=h
            continue
        ind=cur
        for x in t:
            if softpat.fullmatch(x): ind=x
        if tk=="FSK":
            ind=t[2] if len(t)>2 else cur
        k+=1
        for name,c in f:
            mp.setdefault(c,ind); order.setdefault(c,(k,t[0] if t else ''))
    return mp,order
if __name__=="__main__":
    tk,html_,xml_,instant=sys.argv[1:5]
    ctx,facts=load_xbrl(xml_,instant)
    mp,order=industry_map(html_,tk)
    softpat=re.compile(SOFT[tk])
    recs=[]
    for c,(ident,dims) in ctx.items():
        fv=facts[c].get("InvestmentOwnedAtFairValue")
        if fv is None and "InvestmentCompanyFinancialCommitmentToInvesteeFutureAmount" not in facts[c]: continue
        ind=mp.get(c)
        recs.append(dict(ctx=c,id=ident,ind=ind,ord=order.get(c,(10**9,''))[0],soft=bool(ind and softpat.fullmatch(ind)),**facts[c]))
    json.dump(recs,open(f"{sys.argv[5]}/{tk}_recs.json","w"))
    tot=sum(r.get("InvestmentOwnedAtFairValue",0) for r in recs)
    st=sum(r.get("InvestmentOwnedAtFairValue",0) for r in recs if r["soft"])
    unm=sum(r.get("InvestmentOwnedAtFairValue",0) for r in recs if r["ind"] is None)
    print(tk,"positions",len(recs),"totalFV %.1fM"%(tot/1e6),"softFV %.1fM"%(st/1e6),"share %.1f%%"%(100*st/tot),"unmappedFV %.1fM"%(unm/1e6))
    c=collections.Counter()
    for r in recs: c[r["ind"]]+=r.get("InvestmentOwnedAtFairValue",0)
    print("  top inds:",[(k,round(v/1e6)) for k,v in c.most_common(6)])
