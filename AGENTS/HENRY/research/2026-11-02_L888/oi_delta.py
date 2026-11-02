# Compare Monday-morning Cboe put OI with the 10/30 post-close ladder file (10/29-trade OI).
import json,re,sys
ladder,chaindir=sys.argv[1],sys.argv[2]
for u in ("QQQ","SPX"):
    # both PUT OI sections live in the QQQ ladder file
    txt=open(ladder).read()
    sec=txt.split(f"{u} PUT OI (open interest | today's volume) by expiry:")[1]
    hdr=sec.splitlines()[0]; exps=[e.strip() for e in hdr.split("·")]
    old={}
    for line in sec.splitlines()[1:]:
        m=re.match(r"\s+(\d+):\s+(.*)",line)
        if not m: break
        for e,cell in zip(exps,m.group(2).split("|")):
            old[(e,int(m.group(1)))]=int(cell.split("/")[0].replace(",",""))
    d=json.load(open(f"{chaindir}/{u}.json"))["data"]; new={}
    for o in d["options"]:
        m=re.match(r"[A-Z]+(\d{2})(\d{2})(\d{2})P(\d{8})",o["option"])
        if m:
            k=(f"20{m.group(1)}-{m.group(2)}-{m.group(3)}",int(m.group(4))//1000)
            new[k]=new.get(k,0)+int(o.get("open_interest") or 0)
    print(f"{u} put OI: 10/29-trade -> 10/30-trade (Monday Cboe)")
    for k in sorted(old,key=lambda k:(k[0],-k[1])):
        if k[0]=="2026-10-30": continue
        if k in new: print(f"  {k[0]} {k[1]:>5}: {old[k]:>7,} -> {new[k]:>7,}  ({new[k]-old[k]:+,})")
