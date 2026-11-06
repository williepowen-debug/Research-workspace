import json,sys,urllib.request,concurrent.futures as cf,numpy as np,eccodes,io,hashlib
SP=sys.argv[1]; date=sys.argv[2]; hh=sys.argv[3]
base=f"https://data.ecmwf.int/forecasts/{date}/{hh}z/ifs/0p25/enfo/{date}{hh}0000-"
def row(b):
    g=eccodes.codes_new_from_message(b); ni,nj=eccodes.codes_get(g,'Ni'),eccodes.codes_get(g,'Nj')
    v=eccodes.codes_get_values(g).reshape(nj,ni)
    la=np.linspace(eccodes.codes_get(g,'latitudeOfFirstGridPointInDegrees'),eccodes.codes_get(g,'latitudeOfLastGridPointInDegrees'),nj)
    j=int(np.argmin(abs(la-60))); assert abs(la[j]-60)<1e-6
    m=v[j].mean(); eccodes.codes_release(g); return m
def step(s):
    u=f"{base}{s}h-enfo-ef"
    idx=urllib.request.urlopen(u+".index",timeout=120).read().decode()
    recs=[json.loads(l) for l in idx.splitlines()]
    recs=[r for r in recs if r.get('param')=='u' and r.get('levelist')=='10' and r.get('type') in('pf','cf')]
    vals=[]
    for r in recs:
        q=urllib.request.Request(u+".grib2",headers={"Range":f"bytes={r['_offset']}-{r['_offset']+r['_length']-1}"})
        vals.append((r['type'],row(urllib.request.urlopen(q,timeout=120).read())))
    return s,vals
steps=[int(x) for x in sys.argv[4].split(',')]
with cf.ThreadPoolExecutor(6) as ex:
    res=dict(ex.map(step,steps))
for s in steps:
    pf=np.array([v for t,v in res[s] if t=='pf'])
    print(f"+{s:3d}h n={len(pf)} mean {pf.mean():+.2f} min {pf.min():+.2f} max {pf.max():+.2f} below0 {(pf<0).sum()}/{len(pf)}")
