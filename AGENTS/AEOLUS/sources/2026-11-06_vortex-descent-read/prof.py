import sys, glob, numpy as np, eccodes
d=sys.argv[1]
for p in sorted(glob.glob(d+'/*.grib2')):
    out={}
    with open(p,'rb') as f:
        while True:
            g=eccodes.codes_grib_new_from_file(f)
            if g is None: break
            ni,nj=eccodes.codes_get(g,'Ni'),eccodes.codes_get(g,'Nj')
            v=eccodes.codes_get_values(g).reshape(nj,ni)
            out[eccodes.codes_get(g,'level')]=v[0].mean() if nj==1 else None
            eccodes.codes_release(g)
    print(p.split('/')[-1].replace('.grib2',''),' '.join(f"{k}:{out[k]:+.2f}" for k in sorted(out)))
