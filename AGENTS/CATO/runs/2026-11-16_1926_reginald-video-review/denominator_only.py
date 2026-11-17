import gzip, os, sys, csv, statistics as st
sdf_dir, rows_tsv = sys.argv[1], sys.argv[2]
meta = {}
for r in csv.DictReader(open(rows_tsv), delimiter="\t"):
    meta[r["RSSD"]] = r
want = ["2170","F158","F159","1460","F160","F161","2746","3792","8274","3123","LE74"]
out=[]; miss=0
for fn in os.listdir(sdf_dir):
    rssd = fn.split(".")[0]
    if rssd not in meta: miss+=1; continue
    if meta[rssd]["BKCLASS"] in ("OI","NC"): continue
    v={}
    with gzip.open(os.path.join(sdf_dir,fn),"rt",errors="replace") as f:
        next(f)
        for line in f:
            p=line.split(";")
            if len(p)<4: continue
            m=p[2]; code=m[4:]
            if code in want and p[3].strip()!="":
                pref=m[:4]
                # prefer RCFD/RCFA (consolidated) over RCON/RCOA for capital and assets
                key=code
                rank = 0 if pref in ("RCFD","RCFA") else 1
                if key not in v or rank < v[key][1]:
                    try: v[key]=(float(p[3]),rank)
                    except ValueError: pass
    g=lambda k: v[k][0] if k in v else None
    a=g("2170")
    if not a: continue
    cd=(g("F158") or 0)+(g("F159") or 0)
    noo=cd+(g("1460") or 0)+(g("F161") or 0)+(g("2746") or 0)
    allcre=noo+(g("F160") or 0)
    cblr = g("LE74")==1
    if False:  # CATO sensitivity: apply SR 20-8 to every bank
        cap=g("3792"); basis="TRBC"
    elif g("8274") is not None:
        cap=g("8274")+(g("3123") or 0); basis="T1+ACL"
    else: continue
    if cap<=0: continue
    out.append(dict(rssd=rssd,asset=a,cd=cd,noo=noo,allcre=allcre,cap=cap,acl=g("3123") or 0,basis=basis))
print("banks", len(out), "unmatched files", miss)
def rep(lbl, xs):
    if not xs: return
    n=len(xs)
    r_noo=[x["noo"]/x["cap"] for x in xs]; r_all=[x["allcre"]/x["cap"] for x in xs]; r_cd=[x["cd"]/x["cap"] for x in xs]
    acl=[x["allcre"]/x["acl"] for x in xs if x["acl"]>0]
    agg_noo=sum(x["noo"] for x in xs)/sum(x["cap"] for x in xs); agg_all=sum(x["allcre"] for x in xs)/sum(x["cap"] for x in xs)
    print(f"{lbl}: n={n} | CRE ex owner-occ / capital: median {100*st.median(r_noo):.0f}%, agg {100*agg_noo:.0f}%, >=300%: {sum(r>=3 for r in r_noo)} ({100*sum(r>=3 for r in r_noo)/n:.1f}%) | all CRE incl owner-occ: median {100*st.median(r_all):.0f}%, agg {100*agg_all:.0f}%, >=300%: {100*sum(r>=3 for r in r_all)/n:.1f}% | construction >=100%: {100*sum(r>=1 for r in r_cd)/n:.1f}% | all CRE / loss allowance median {st.median(acl):.1f}x | basis T1+ACL (CBLR) {sum(x['basis']=='T1+ACL' for x in xs)}")
rep("ALL", out)
rep("<$1B", [x for x in out if x["asset"]<1e6])
rep("$1-10B", [x for x in out if 1e6<=x["asset"]<1e7])
rep("$10-100B", [x for x in out if 1e7<=x["asset"]<1e8])
rep(">=$100B", [x for x in out if x["asset"]>=1e8])
