import urllib.request,struct,json,hashlib,datetime
from pathlib import Path
import numpy as np
out=Path('research/2026-11-04_catchup')
def signed(b):
 n=int.from_bytes(b,'big'); bits=len(b)*8;return -(n&((1<<(bits-1))-1)) if n>>(bits-1) else n
def decode(b):
 assert b[:4]==b'GRIB' and b[7]==2 and int.from_bytes(b[8:16],'big')==len(b) and b[-4:]==b'7777'
 sec={};p=16
 while p<len(b)-4:
  n=int.from_bytes(b[p:p+4],'big');sec[b[p+4]]=b[p:p+n];p+=n
 s=sec[3];ni=int.from_bytes(s[30:34],'big');nj=int.from_bytes(s[34:38],'big');assert int.from_bytes(s[12:14],'big')==0 and ni==1440 and nj==1
 assert signed(s[46:50])==60000000 and signed(s[55:59])==60000000 and int.from_bytes(s[50:54],'big')==0 and int.from_bytes(s[59:63],'big')==359750000
 s=sec[4];assert int.from_bytes(s[7:9],'big')==0 and s[9:11]==bytes([2,2]) and int.from_bytes(s[18:22],'big')==0 and s[22]==100 and int.from_bytes(s[24:28],'big')*10**(-signed(s[23:24]))==1000
 s=sec[5];assert int.from_bytes(s[9:11],'big')==0 and int.from_bytes(s[5:9],'big')==1440 and sec[6][5]==255
 r=struct.unpack('>f',s[11:15])[0];e=signed(s[15:17]);d=signed(s[17:19]);bits=s[19];payload=sec[7][5:];big=int.from_bytes(payload,'big');total=len(payload)*8
 vals=[(r+((big>>(total-(i+1)*bits))&((1<<bits)-1))*2**e)*10**(-d) for i in range(1440)]
 unpack=np.unpackbits(np.frombuffer(payload,dtype=np.uint8))[:1440*bits].reshape(1440,bits).dot(2**np.arange(bits-1,-1,-1));vals2=(r+unpack*2**e)*10**(-d);assert np.allclose(vals,vals2,rtol=0,atol=1e-12)
 s=sec[1];ts=datetime.datetime(int.from_bytes(s[12:14],'big'),*s[14:19],tzinfo=datetime.timezone.utc)
 return dict(reference_time=ts.isoformat(),forecast_hours=0,parameter='UGRD',pressure_pa=1000,latitude=60,longitude_count=1440,zonal_mean_u_m_s=sum(vals)/1440,raw_sha256=hashlib.sha256(b).hexdigest(),basis='GFS analyzed field f000, not direct measurement or forecast; owner acceptance pending',decoder_crosscheck='integer extraction and numpy unpackbits agree')
control=decode(Path('research/2026-11-02_UNG-refresh/gfs-20261102-06z-f000-u10-60n.grib2').read_bytes());assert abs(control['zonal_mean_u_m_s']-5.531545627170138)<1e-9
rows=[]
for day,hour in [('20261103','00'),('20261104','00'),('20261104','12')]:
 url=f'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?dir=%2Fgfs.{day}%2F{hour}%2Fatmos&file=gfs.t{hour}z.pgrb2.0p25.f000&var_UGRD=on&lev_10_mb=on&subregion=&leftlon=0&rightlon=359.75&toplat=60&bottomlat=60'
 try:
  b=urllib.request.urlopen(url,timeout=30).read();r=decode(b);r['source']=url;(out/f'gfs-{day}-{hour}z.grib2').write_bytes(b);rows.append(r)
 except Exception as e:rows.append(dict(source=url,error=str(e)))
(out/'vortex-observations.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows))
