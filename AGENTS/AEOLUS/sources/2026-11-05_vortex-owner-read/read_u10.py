#!/usr/bin/env python3
"""AEOLUS owner read: 10 hPa 60N zonal-mean zonal wind from a GRIB2 message.
Usage: read_u10.py <file.grib2> [...]   (needs eccodes; not in .venv: pip install --target <scratch> eccodes)
GFS: NOMADS filter_gfs_0p25.pl, file=gfs.tHHz.pgrb2.0p25.anl (scout basis) or .f000, var_UGRD, lev_10_mb, leftlon=0 rightlon=359.75 toplat=60 bottomlat=60.
ECMWF: data.ecmwf.int open data <YYYYMMDD>/<HH>z/ifs/0p25/oper/, param u levelist 10, range-GET from the .index; take the 60.0N row.
Zonal mean = unweighted mean over all longitudes of the exact-60N row. Prints one line per file."""
import sys, hashlib, numpy as np, eccodes
for p in sys.argv[1:]:
    b = open(p, 'rb').read(); g = eccodes.codes_new_from_message(b)
    ni, nj = eccodes.codes_get(g, 'Ni'), eccodes.codes_get(g, 'Nj')
    v = eccodes.codes_get_values(g).reshape(nj, ni)
    la = np.linspace(eccodes.codes_get(g, 'latitudeOfFirstGridPointInDegrees'), eccodes.codes_get(g, 'latitudeOfLastGridPointInDegrees'), nj)
    j = int(np.argmin(abs(la - 60))); assert abs(la[j] - 60) < 1e-6
    print(p, eccodes.codes_get(g, 'dataDate'), eccodes.codes_get(g, 'dataTime'), 'step', eccodes.codes_get(g, 'step'), eccodes.codes_get(g, 'level'), 'n', ni, 'zonal_mean %.6f' % v[j].mean(), hashlib.sha256(b).hexdigest())
