import json,sys,urllib.request,numpy as np,eccodes
date,hh='20261106','00'
base=f"https://data.ecmwf.int/forecasts/{date}/{hh}z/ifs/0p25/oper/{date}{hh}0000-"
def row(b):
    g=eccodes.codes_new_from_message(b); ni,nj=eccodes.codes_get(g,'Ni'),eccodes.codes_get(g,'Nj')
    v=eccodes.codes_get_values(g).reshape(nj,ni)
    la=np.linspace(eccodes.codes_get(g,'latitudeOfFirstGridPointInDegrees'),eccodes.codes_get(g,'latitudeOfLastGridPointInDegrees'),nj)
    j=int(np.argmin(abs(la-60))); m=v[j].mean(); eccodes.codes_release(g); return m
for s in (0,24,48,72,96,120,144,168,192,216,240):
    u=f"{base}{s}h-oper-fc"
    recs=[json.loads(l) for l in urllib.request.urlopen(u+".index",timeout=60).read().decode().splitlines()]
    o={}
    for r in recs:
        if r.get('param')=='u' and r.get('levelist') in('10','30','50','100'):
            q=urllib.request.Request(u+".grib2",headers={"Range":f"bytes={r['_offset']}-{r['_offset']+r['_length']-1}"})
            o[int(r['levelist'])]=row(urllib.request.urlopen(q,timeout=60).read())
    print(f"+{s}h",' '.join(f"{k}:{o[k]:+.2f}" for k in sorted(o)))
