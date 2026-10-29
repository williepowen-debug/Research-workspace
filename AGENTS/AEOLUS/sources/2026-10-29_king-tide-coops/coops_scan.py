import json, sys, urllib.request, collections
S = {"8724580":"Key West FL","8723214":"Virginia Key FL","8722670":"Lake Worth Pier FL","8721604":"Trident Pier FL","8720218":"Mayport FL","8720030":"Fernandina Bch FL","8726520":"St Petersburg FL","8725520":"Fort Myers FL","8729108":"Panama City FL","8670870":"Fort Pulaski GA","8665530":"Charleston SC","8658120":"Wilmington NC","8638610":"Sewells Pt VA","8575512":"Annapolis MD","8518750":"The Battery NY","8443970":"Boston MA","9414290":"San Francisco CA"}
B, E = sys.argv[1], sys.argv[2]
base="https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?station={s}&begin_date={b}&end_date={e}&datum=STND&units=english&time_zone=lst_ldt&format=json&application=AEOLUS&product={p}"
def get(u):
    try: return json.load(urllib.request.urlopen(u, timeout=60))
    except Exception as x: return {"error":str(x)}
for s,name in S.items():
    fl = get(f"https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/{s}/floodlevels.json")
    obs = get(base.format(s=s,b=B,e=E,p="water_level"))
    pre = get(base.format(s=s,b=B,e=E,p="predictions")+"&interval=6")
    json.dump({"fl":fl,"obs":obs,"pre":pre}, open(f"coops/{s}.json","w"))
    if "data" not in obs: print(name, s, "OBS FAIL", str(obs)[:120]); continue
    pm = {p["t"]:float(p["v"]) for p in pre.get("predictions",[])}
    day = collections.defaultdict(lambda:(-99,None,None))
    for r in obs["data"]:
        if not r["v"]: continue
        v=float(r["v"]); d=r["t"][:10]
        if v>day[d][0]: day[d]=(v,r["t"][11:],pm.get(r["t"]))
    mn, mo, mj = fl.get("nws_minor") or fl.get("nos_minor"), fl.get("nws_moderate") or fl.get("nos_moderate"), fl.get("nws_major") or fl.get("nos_major")
    src = "NWS" if fl.get("nws_minor") else "NOS"
    out=[]
    for d,(v,t,p) in sorted(day.items()):
        lvl = "MAJ" if mj and v>=mj else "MOD" if mo and v>=mo else "MIN" if mn and v>=mn else ""
        res = f"{v-p:+.2f}" if p is not None else "na"
        out.append(f"{d[5:]} {v:.2f}@{t} r{res} {lvl}")
    print(f"## {name} {s} thr[{src}] minor {mn} mod {mo} maj {mj}")
    print("   " + " | ".join(out))
