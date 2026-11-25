import json,urllib.request,sys
B="https://api.tidesandcurrents.noaa.gov"
def g(u):
    try: return json.load(urllib.request.urlopen(u,timeout=30))
    except Exception as e: return {"err":str(e)}
st=g(B+"/mdapi/prod/webapi/stations.json?type=waterlevels")["stations"]
out=[]
for s in st:
    if s["state"] not in("CA","OR","WA"): continue
    i=s["id"]
    d=g(f"{B}/api/prod/datagetter?product=water_level&begin_date=20261124&end_date=20261125&datum=MLLW&station={i}&time_zone=lst&units=english&format=json&application=research")
    rows=[(float(r["v"]),r["t"],r["f"]) for r in d.get("data",[]) if r["v"]]
    if not rows: out.append((s["name"],i,"NO DATA",d.get("error") or d.get("err"))); continue
    td=[r for r in rows if r[1].startswith("2026-11-25")]; yd=[r for r in rows if r[1].startswith("2026-11-24")]
    t=g(f"{B}/dpapi/prod/webapi/product.json?name=toptenwaterlevels&station={i}&units=english&datum=MLLW").get("topTenWaterLevels",[])
    top=max(t,key=lambda x:x["height"]) if t else None
    m=max(td) if td else None; y=max(yd) if yd else None
    fl="" 
    if m and top and m[0]>top["height"]: fl="NEW TODAY OVER LIST"
    if y and top and y[0]>top["height"]: fl+=" 11/24 OVER LIST"
    out.append((s["name"],i,"today",m,"11/24",y,"last",td[-1] if td else None,"list#1",(top["height"],top["peakDate"]) if top else None,fl))
for o in out: print(*o)
