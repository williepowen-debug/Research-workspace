import sys
sys.path.insert(0, sys.argv[1])
import eccodes, numpy as np
with open(sys.argv[2],'rb') as f:
    g=eccodes.codes_grib_new_from_file(f)
gk=lambda k:eccodes.codes_get(g,k)
print({k:gk(k) for k in ('shortName','typeOfLevel','level','stream','dataType','dataDate','dataTime','step','Ni','Nj','gridType','packingType','latitudeOfFirstGridPointInDegrees','latitudeOfLastGridPointInDegrees','iDirectionIncrementInDegrees','numberOfMissing')})
v=eccodes.codes_get_double_array(g,'values').reshape(gk('Nj'),gk('Ni'))
lat0=gk('latitudeOfFirstGridPointInDegrees'); dj=gk('jDirectionIncrementInDegrees')
lats=lat0-dj*np.arange(gk('Nj'))
for L in (60.5,60.25,60.0,59.75,59.5):
    j=int(np.argmin(abs(lats-L))); r=v[j]
    print(f"lat {lats[j]:.2f} n={r.size} mean {r.mean():+.6f} min {r.min():+.2f} max {r.max():+.2f} frac<0 {(r<0).mean():.3f}")
