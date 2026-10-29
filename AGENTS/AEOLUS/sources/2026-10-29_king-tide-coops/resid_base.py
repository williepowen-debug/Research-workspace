import json, urllib.request, statistics, sys
S={"8724580":"Key West","8723214":"Virginia Key","8722670":"Lake Worth","8721604":"Trident Pier","8665530":"Charleston","8638610":"Sewells Pt","9414290":"San Francisco","8726520":"St Petersburg"}
base="https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?station={s}&begin_date={b}&end_date={e}&datum=STND&units=english&time_zone=gmt&format=json&application=AEOLUS&product={p}&interval=h"
def get(u): return json.load(urllib.request.urlopen(u,timeout=60))
for s,n in S.items():
    row=[]
    for b,e in [("20260801","20260831"),("20260901","20260930"),("20261001","20261019"),("20261020","20261028")]:
        try:
            o={r["t"]:float(r["v"]) for r in get(base.format(s=s,b=b,e=e,p="hourly_height").replace("&interval=h",""))["data"] if r["v"]}
        except Exception:
            o={r["t"]:float(r["v"]) for r in get(base.format(s=s,b=b,e=e,p="water_level").replace("&interval=h",""))["data"] if r["v"] and r["t"].endswith(":00")}
        p={r["t"]:float(r["v"]) for r in get(base.format(s=s,b=b,e=e,p="predictions"))["predictions"]}
        d=[o[t]-p[t] for t in o if t in p]
        row.append(f"{b[4:6]}/{b[6:]}-{e[4:6]}/{e[6:]} {statistics.mean(d):+.2f} (n={len(d)})")
    print(f"{n:14s}", " | ".join(row))
