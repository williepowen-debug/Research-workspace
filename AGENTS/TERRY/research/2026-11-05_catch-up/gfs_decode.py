"""Decode NOAA GFS f000 UGRD 10 mb 60N from a NOMADS grib filter; GRIB2 simple packing only. TERRY read, not an AEOLUS log."""
import struct,sys,urllib.request,hashlib,json,datetime as dt
def decode(b):
    assert b[:4]==b'GRIB'; p=16; R=E=D=nb=None; n=None; data=None
    while b[p:p+4]!=b'7777':
        l=struct.unpack('>I',b[p:p+4])[0]; s=b[p+4]
        if s==5:
            n=struct.unpack('>I',b[p+5:p+9])[0]; tpl=struct.unpack('>H',b[p+9:p+11])[0]; assert tpl==0,tpl
            R=struct.unpack('>f',b[p+11:p+15])[0]
            def sm(x): return -(x&0x7fff) if x&0x8000 else x
            E=sm(struct.unpack('>H',b[p+15:p+17])[0]); D=sm(struct.unpack('>H',b[p+17:p+19])[0]); nb=b[p+19]
        if s==7: data=b[p+5:p+l]
        p+=l
    v=int.from_bytes(data,'big'); tot=len(data)*8; m=(1<<nb)-1
    return [(R+((v>>(tot-nb*(i+1)))&m)*2.0**E)/10.0**D for i in range(n)]
out=[]
for ymd,hh in [x.split('/') for x in sys.argv[1:]]:
    u=f'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?dir=%2Fgfs.{ymd}%2F{hh}%2Fatmos&file=gfs.t{hh}z.pgrb2.0p25.f000&var_UGRD=on&lev_10_mb=on&subregion=&leftlon=0&rightlon=359.75&toplat=60&bottomlat=60'
    try:
        b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'terry-desk'}),timeout=40).read()
        x=decode(b); r={'ref':f'{ymd} {hh}Z','n':len(x),'zonal_mean_u_m_s':sum(x)/len(x),'sha256':hashlib.sha256(b).hexdigest(),'url':u}
    except Exception as e: r={'ref':f'{ymd} {hh}Z','error':str(e)[:120]}
    print(r if 'error' in r else (r['ref'],r['n'],round(r['zonal_mean_u_m_s'],6),r['sha256'][:12])); out.append(r)
json.dump(out,open(sys.argv[0].replace('gfs_decode.py','gfs_reads.json'),'w'),indent=1)
