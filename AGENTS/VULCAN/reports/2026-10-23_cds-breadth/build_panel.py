import csv,io,zipfile,statistics as st,re,json
days=["2026_09_30","2026_10_09","2026_10_13","2026_10_16","2026_10_20","2026_10_21","2026_10_22"]
def norm(n):
    n=n.upper().replace(";",",")
    n=re.sub(r"[.,]","",n); n=re.sub(r"\b(INC|CORPORATION|CORP|COMPANY|LLC|LTD|PLC|HOLDINGS|GROUP|CO|THE)\b","",n)
    return re.sub(r"\s+"," ",n).strip()
lv={}; cnt={}
for d in days:
    z=zipfile.ZipFile(f"sec_{d}.zip")
    for r in csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]),encoding="utf-8",errors="replace")):
        n=r["Underlying Asset Name"]
        if r["Action type"]!="NEWT" or not n or r["Expiration Date"]!="2031-12-20" or not r["Spread-Leg 1"]: continue
        try: s=float(r["Spread-Leg 1"])*1e4
        except: continue
        if 0<s<5000:
            k=norm(n); lv.setdefault(k,{}).setdefault(d,[]).append(s)
med={n:{d:st.median(v) for d,v in dd.items()} for n,dd in lv.items()}
json.dump({n:{d:[round(x,1) for x in v] for d,v in dd.items()} for n,dd in lv.items()},open("../cds_spread_only.json","w"))
print("names with any disseminated 5Y spread:",len(med))
for n in sorted(med):
    m=med[n]
    if len(m)>=2:
        print(f"{n[:34]:34s} "+"  ".join(f"{d[5:]}:{m[d]:5.0f}" for d in days if d in m))
