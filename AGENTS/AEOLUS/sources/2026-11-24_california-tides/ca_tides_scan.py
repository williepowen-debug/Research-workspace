# AEOLUS 2026-11-24: CA CO-OPS observed 11/24 highs vs predictions, datum-page max, and monthly-highest record scan. Datum MLLW, feet, LST.
import json, sys, urllib.request, collections, os
S = {"9419750":"Crescent City","9418767":"North Spit (Humboldt Bay)","9416841":"Arena Cove","9415020":"Point Reyes","9414290":"San Francisco","9414750":"Alameda","9414863":"Richmond","9414523":"Redwood City","9415144":"Port Chicago","9415102":"Martinez-Amorco","9413450":"Monterey","9412110":"Port San Luis","9411340":"Santa Barbara","9410840":"Santa Monica","9410660":"Los Angeles","9410230":"La Jolla","9410170":"San Diego"}
os.makedirs("coops", exist_ok=True)
API="https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?station={s}&begin_date={b}&end_date={e}&datum=MLLW&units=english&time_zone=lst&format=json&application=research-client&product={p}"
def get(u):
    try: return json.load(urllib.request.urlopen(u, timeout=90))
    except Exception as x: return {"error":str(x)}
for s,name in S.items():
    obs = get(API.format(s=s,b="20261122",e="20261125",p="water_level"))
    pre = get(API.format(s=s,b="20261122",e="20261125",p="predictions")+"&interval=6")
    dat = get(f"https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/{s}/datums.json?units=english")
    fl  = get(f"https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/{s}/floodlevels.json?units=english")
    mon = []
    for y0 in range(1850, 2027, 10):
        r = get(API.format(s=s,b=f"{y0}0101",e=f"{min(y0+9,2026)}1231",p="monthly_mean"))
        mon += r.get("data", [])
    json.dump({"obs":obs,"pre":pre,"dat":dat,"fl":fl,"mon":mon}, open(f"coops/{s}.json","w"))
    mllw = next((d["value"] for d in dat.get("datums",[]) if d["name"]=="MLLW"), None)
    mx = dat.get("max"); mxd = dat.get("maxdate")
    dpmax = round(mx-mllw,3) if (mx is not None and mllw is not None) else None
    pm = {p["t"]:float(p["v"]) for p in pre.get("predictions",[])}
    day = collections.defaultdict(lambda:(-99,None,None,None))
    for r in obs.get("data",[]):
        if not r["v"]: continue
        v=float(r["v"]); d=r["t"][:10]
        if v>day[d][0]: day[d]=(v,r["t"][11:],pm.get(r["t"]),r["q"])
    hi = sorted([(float(m["highest"]),m["year"],m["month"]) for m in mon if m.get("highest") not in (None,"")], reverse=True)[:5]
    first = min((int(m["year"]) for m in mon), default=None)
    print(f"## {name} {s} | datum-page max {dpmax} MLLW on {mxd} | monthly-highest record since {first}: " + ", ".join(f"{v:.3f} ({y}-{int(mo):02d})" for v,y,mo in hi))
    print("   flood thr (STND):", {k:v for k,v in fl.items() if v and k!='self'}, "| MLLW-on-STND", mllw)
    for d,(v,t,p,q) in sorted(day.items()):
        print(f"   {d} max {v:.3f}@{t} pred {p} resid {v-p:+.2f} q={q}" if p is not None else f"   {d} max {v:.3f}@{t} q={q}")
    if "error" in obs: print("   OBS ERR", obs["error"][:100])
