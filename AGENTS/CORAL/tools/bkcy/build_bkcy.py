#!/usr/bin/env python3
"""CORAL bankruptcy per-capita instrument (AOUSC Table F-2 + Census V2025).
Inputs in cwd: bf_f2_MMDD.YYYY.xlsx (12-month), q3m/bf_f2.3_MMDD.YYYY.xlsx (3-month),
co-est2025-alldata.csv, NST-EST2025-ALLDATA.csv.  Output: stdout tables + bkcy_extract.json"""
import csv, glob, re, openpyxl, json, os
ND="Alachua,Bay,Calhoun,Dixie,Escambia,Franklin,Gadsden,Gilchrist,Gulf,Holmes,Jackson,Jefferson,Lafayette,Leon,Levy,Liberty,Madison,Okaloosa,Santa Rosa,Taylor,Wakulla,Walton,Washington".split(",")
MD="Baker,Bradford,Brevard,Charlotte,Citrus,Clay,Collier,Columbia,DeSoto,Duval,Flagler,Glades,Hamilton,Hardee,Hendry,Hernando,Hillsborough,Lake,Lee,Manatee,Marion,Nassau,Orange,Osceola,Pasco,Pinellas,Polk,Putnam,St. Johns,Sarasota,Seminole,Sumter,Suwannee,Union,Volusia".split(",")
SD="Broward,Miami-Dade,Highlands,Indian River,Martin,Monroe,Okeechobee,Palm Beach,St. Lucie".split(",")
DIST={"FL,N":ND,"FL,M":MD,"FL,S":SD}
YRS=(2023,2024,2025)
cty={}; fl={}
for r in csv.DictReader(open("co-est2025-alldata.csv",encoding="latin-1")):
    if r["STATE"]=="12" and r["SUMLEV"]=="050": cty[r["CTYNAME"].replace(" County","")]={y:int(r[f"POPESTIMATE{y}"]) for y in YRS}
    if r["STATE"]=="12" and r["SUMLEV"]=="040": fl={y:int(r[f"POPESTIMATE{y}"]) for y in YRS}
assert set(cty)==set(ND+MD+SD) and len(cty)==67
pop={}
for y in YRS:
    for d,l in DIST.items(): pop[(d,y)]=sum(cty[c][y] for c in l)
    pop[("FL M+S",y)]=pop[("FL,M",y)]+pop[("FL,S",y)]; pop[("FL all",y)]=fl[y]
    assert fl[y]==sum(pop[(d,y)] for d in DIST)
nst={r["NAME"]:r for r in csv.DictReader(open("NST-EST2025-ALLDATA.csv",encoding="latin-1"))}
for y in YRS:
    pop[("US 50+DC",y)]=int(nst["United States"][f"POPESTIMATE{y}"])
    pop[("US+PR",y)]=pop[("US 50+DC",y)]+int(nst["Puerto Rico"][f"POPESTIMATE{y}"])
def num(x): return 0 if x in (None,"0","-","–") else int(x)
TERR=("PR","VI","GU","NMI")
MON={"03":"March","06":"June","09":"September","12":"December"}
def load(pattern, tag):
    out={}
    for f in sorted(glob.glob(pattern)):
        m=re.search(r"_(\d\d)(\d\d)\.(\d{4})\.xlsx",f); per=f"{m[3]}-{m[1]}-{m[2]}"
        ws=openpyxl.load_workbook(f,data_only=True).worksheets[0]
        title=" ".join(str(c) for r in ws.iter_rows(max_row=3,values_only=True) for c in r if c)
        assert f"{MON[m[1]]} {int(m[2])}, {m[3]}" in title and tag in title, (f,title)
        rows={}; allrows=[]
        for r in ws.iter_rows(values_only=True):
            if isinstance(r[0],str) and (isinstance(r[1],(int,float)) or r[1]=="0"):
                k=r[0].strip()
                rec=dict(total=num(r[1]),ch7=num(r[2]),ch11=num(r[3]),ch13=num(r[4]),bus=num(r[6]),nb=num(r[11]),nb7=num(r[12]),nb13=num(r[14]))
                rows[k]=rec
                if not r[0].startswith(" ") and k not in ("Total",): allrows.append((k,rec["total"]))
        rows["FL M+S"]={k:rows["FL,M"][k]+rows["FL,S"][k] for k in rows["FL,M"]}
        rows["FL all"]={k:rows["FL M+S"][k]+rows["FL,N"][k] for k in rows["FL,M"]}
        rows["US 50+DC"]={k:rows["Total"][k]-sum(rows[t][k] for t in TERR) for k in rows["Total"]}
        rows["US+PR"]={k:rows["Total"][k]-sum(rows[t][k] for t in TERR if t!="PR") for k in rows["Total"]}
        rank=sorted(allrows,key=lambda x:-x[1]); rows["_rank"]={k:i+1 for i,(k,_) in enumerate(rank)}
        rows["_top8"]=rank[:8]
        out[per]=rows
    return out
D12=load("bf_f2_*.xlsx","12-Month"); D3=load("q3m/bf_f2.3_*.xlsx","Three-Month")
json.dump({"F2_12mo":D12,"F2_3mo":D3,"pop":{f"{a}|{b}":v for (a,b),v in pop.items()}},open("bkcy_extract.json","w"),indent=1)
G=["FL,N","FL,M","FL,S","FL M+S","FL all","US 50+DC","US+PR"]
def yo(per): return f"{int(per[:4])-1}{per[4:]}"
print("POP (Census V2025, July 1):"); [print(f"  {g:9s} "+"  ".join(f"{y}:{pop[(g,y)]:,}" for y in YRS)) for g in G]
for name,D,ann in (("12-MONTH ROLLING (F-2)",D12,1),("3-MONTH QUARTER (F-2 Quarterly), annualized x4",D3,4)):
    print(f"\n=== {name}: per-100k on FIXED V2025 denominator; YoY = raw filings ===")
    for key,lab in (("total","ALL CHAPTERS"),("nb","NONBUSINESS"),("ch7","CH7"),("nb7","NONBUS CH7")):
        print(f"-- {lab}")
        print("period      "+"".join(f"{g:>19s}" for g in G))
        for per in sorted(D):
            cells=[]
            for g in G:
                v=D[per][g][key]; rate=ann*v/pop[(g,2025)]*1e5
                y=f"{100*(v/D[yo(per)][g][key]-1):+5.1f}%" if yo(per) in D else "   n/a"
                cells.append(f"{v:>7,} {rate:5.1f} {y}")
            print(per+" "+"".join(f"{c:>19s}" for c in cells))
print("\n=== Matched-vintage check (12-mo, all ch & nonbus): rate using July-1 pop of the year the window ends mostly in ===")
for per in sorted(D12):
    y=min(2025,int(per[:4])-1 if per[5:7] in ("03",) else int(per[:4])) ; y=max(y,2023)
    print(per,f"popyr={y}"," ".join(f"{g}:{D12[per][g]['total']/pop[(g,y)]*1e5:.1f}/{D12[per][g]['nb']/pop[(g,y)]*1e5:.1f}" for g in ("FL M+S","FL all","US 50+DC","US+PR")))
print("\n=== District rank by total filings (12-mo; 94 districts + territorial) ===")
for per in sorted(D12):
    r=D12[per]["_rank"]; print(per, "FL,M #%d  FL,S #%d  FL,N #%d | top8:"%(r["FL,M"],r["FL,S"],r["FL,N"]), D12[per]["_top8"])
