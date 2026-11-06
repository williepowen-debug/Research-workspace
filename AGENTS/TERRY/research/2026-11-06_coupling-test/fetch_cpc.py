# CPC 8-14 day temperature outlook shapefiles, issues Nov 7 to Dec 3, 2012-2025, plus the latest. Paced.
import re, urllib.request, time, os, sys
ua={'User-Agent':'Mozilla/5.0 (research-client)'}
B='https://ftp.cpc.ncep.noaa.gov/GIS/us_tempprcpfcst/'
s=urllib.request.urlopen(urllib.request.Request(B,headers=ua),timeout=60).read().decode()
d=sorted(set(re.findall(r'814temp_(\d{8})\.zip',s)))
d=[x for x in d if '1107'<=x[4:]<='1203' or x=='20261105']
os.makedirs('data/cpc',exist_ok=True)
for i,x in enumerate(d):
    p=f'data/cpc/814temp_{x}.zip'
    if os.path.exists(p): continue
    try:
        b=urllib.request.urlopen(urllib.request.Request(B+f'814temp_{x}.zip',headers=ua),timeout=60).read()
        open(p,'wb').write(b)
    except Exception as e:
        print('fail',x,repr(e)[:80],flush=True); time.sleep(5)
    time.sleep(1.0)
print('DONE',len(d),flush=True)
