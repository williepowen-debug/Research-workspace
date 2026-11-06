# NCEP/NCAR R1 daily mean u at 60N, zonal mean of 144 longitudes, Nov 1 to Dec 31, 10 and 30 hPa.
# Serial and paced: the server returned 429 to four parallel workers. Resumable by year.
import urllib.request, urllib.error, re, datetime as dt, time, os
B='https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis/Dailies/pressure/uwnd.%d.nc'
UA={'User-Agent':'Mozilla/5.0 (research-client)'}
OUT='data/ncep_u60.tsv'
def get(u):
    for a in range(12):
        try:
            return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read().decode()
        except urllib.error.HTTPError as e:
            if e.code not in (429,500,502,503,504): raise
            w=int(e.headers.get("Retry-After") or 120+60*a); print('429, wait',w,flush=True); time.sleep(w)
        except Exception as e:
            print('retry',repr(e)[:80],flush=True); time.sleep(10*(a+1))
    raise SystemExit('gave up')
done=set()
if os.path.exists(OUT):
    done={l[:4] for l in open(OUT) if l[:2] in('19','20')}
else:
    open(OUT,'w').write('date\thpa\tu_zonal_60N\n')
HP={0:30,1:10}
for y in range(2026,1949,-1):
    if str(y) in done: continue
    s=dt.date(y,11,1).timetuple().tm_yday-1; e=s+60
    if y==2026:
        n=int(re.search(r'time = (\d+)',get(B%y+'.dds')).group(1)); e=min(e,n-1)
        time.sleep(3)
        if e<s: continue
    t=get(B%y+f'.ascii?uwnd%5B{s}:{e}%5D%5B14:2:16%5D%5B12%5D%5B0:143%5D')
    rows=re.findall(r'^\[(\d+)\]\[(\d+)\]\[0\], (.*)$',t,re.M)
    assert len(rows)==2*(e-s+1),(y,len(rows))
    with open(OUT,'a') as f:
        for r,l,vals in rows:
            v=[float(x) for x in vals.split(',')]; assert len(v)==144
            d=dt.date(y,11,1)+dt.timedelta(days=int(r))
            f.write('%s\t%d\t%.3f\n'%(d.isoformat(),HP[int(l)],sum(v)/144))
    print(y,flush=True); time.sleep(50)
print('DONE',flush=True)
