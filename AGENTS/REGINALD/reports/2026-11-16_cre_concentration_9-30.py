import gzip, os, sys, csv, statistics as st
sdf_dir, rows_tsv = sys.argv[1], sys.argv[2]
meta = {}
for r in csv.DictReader(open(rows_tsv), delimiter="\t"):
    meta[r["RSSD"]] = r
# Denominator per SR 20-8 (corrected 2026-11-16 evening; first run mixed TRBC and T1+ACL)
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
    # SR 20-8 (Fed, 3/30/2020, rev. 4/2/2020; joint statement with FDIC and OCC): for ALL banks the
    # supervisory concentration denominator is tier 1 capital + the allowance for credit losses on
    # loans and leases (CECL) or + the entire ALLL (non-CECL). Total risk-based capital is NOT used.
    if g("8274") is None: continue
    cap=g("8274")+(g("3123") or 0); basis="T1+ACL"
    if cap<=0: continue
    trbc = g("3792") if (g("3792") and g("LE74")!=1) else None   # sensitivity only, the pre-2020 basis
    out.append(dict(rssd=rssd,asset=a,cd=cd,noo=noo,allcre=allcre,cap=cap,acl=g("3123") or 0,basis=basis,trbc=trbc))
print("banks", len(out), "unmatched files", miss)
def rep(lbl, xs):
    if not xs: return
    n=len(xs)
    r_noo=[x["noo"]/x["cap"] for x in xs]; r_all=[x["allcre"]/x["cap"] for x in xs]; r_cd=[x["cd"]/x["cap"] for x in xs]
    acl=[x["allcre"]/x["acl"] for x in xs if x["acl"]>0]
    agg_noo=sum(x["noo"] for x in xs)/sum(x["cap"] for x in xs); agg_all=sum(x["allcre"] for x in xs)/sum(x["cap"] for x in xs)
    tr=[x for x in xs if x["trbc"]]
    if tr: print(f"   sensitivity, pre-2020 total-capital basis where reported (n={len(tr)}): median {100*st.median([x['noo']/x['trbc'] for x in tr]):.0f}%, >=300% {sum(x['noo']/x['trbc']>=3 for x in tr)}")
    print(f"{lbl}: n={n} | CRE ex owner-occ / capital: median {100*st.median(r_noo):.0f}%, agg {100*agg_noo:.0f}%, >=300%: {sum(r>=3 for r in r_noo)} ({100*sum(r>=3 for r in r_noo)/n:.1f}%) | all CRE incl owner-occ: median {100*st.median(r_all):.0f}%, agg {100*agg_all:.0f}%, >=300%: {100*sum(r>=3 for r in r_all)/n:.1f}% | construction >=100%: {100*sum(r>=1 for r in r_cd)/n:.1f}% | all CRE / loss allowance median {st.median(acl):.1f}x | basis T1+ACL all {sum(x['basis']=='T1+ACL' for x in xs)}")
rep("ALL", out)
rep("<$1B", [x for x in out if x["asset"]<1e6])
rep("$1-10B", [x for x in out if 1e6<=x["asset"]<1e7])
rep("$10-100B", [x for x in out if 1e7<=x["asset"]<1e8])
rep(">=$100B", [x for x in out if x["asset"]>=1e8])
