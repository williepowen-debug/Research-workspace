import sys,csv,io,zipfile,urllib.request,datetime as dt,os,time,gc
OUT=sys.argv[1]; start,end=sys.argv[2],sys.argv[3]
URL="https://pddata.dtcc.com/ppd/api/report/cumulative/sec/SEC_CUMULATIVE_CREDITS_%s.zip"
KEEP=['Dissemination Identifier','Original Dissemination Identifier','Action type','Event type','Event timestamp','Cleared','Execution Timestamp','Effective Date','Expiration Date','Platform identifier','Prime brokerage transaction indicator','Block trade election indicator','Notional amount-Leg 1','Notional currency-Leg 1','Fixed rate-Leg 1','Spread-Leg 1','Other payment amount','Other payment type','Package indicator','Underlier ID-Leg 1','Underlying Asset Name','UPI FISN','UPI Underlier Name','Non-standardized term indicator']
NAMES=('ORACLE','ORACLE COP','SOFTBANK','MICROSOFT','COREWEAVE','META PLATFORMS','AMAZON','ALPHABET')
done=set()
if os.path.exists(OUT):
    done={l.split('\t',1)[0] for l in open(OUT,encoding='utf-8')}
d=dt.date.fromisoformat(start); e=dt.date.fromisoformat(end)
t0=time.time(); w=open(OUT,'a',encoding='utf-8',newline='')
while d<=e:
    if d.weekday()<5 and d.isoformat() not in done:
        ds=d.isoformat()
        try:
            b=urllib.request.urlopen(urllib.request.Request(URL%ds.replace('-','_'),headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
            z=zipfile.ZipFile(io.BytesIO(b)); n=0; tot=0
            with z.open(z.namelist()[0]) as f:
                for r in csv.DictReader(io.TextIOWrapper(f,encoding='utf-8',errors='replace')):
                    tot+=1
                    u=(r.get('Underlying Asset Name') or '').upper()
                    if any(x in u for x in NAMES) or r.get('Underlier ID-Leg 1')=='6EC42L':
                        w.write('\t'.join([ds]+[(r.get(k) or '').replace('\t',' ') for k in KEEP])+'\n'); n+=1
            w.write('\t'.join([ds,'__DAY__',str(tot),str(n)])+'\n'); w.flush()
            print(ds,tot,n,flush=True); del b,z; gc.collect()
        except Exception as ex:
            print(ds,'UNAVAILABLE',str(ex)[:70],flush=True)
    d+=dt.timedelta(days=1)
    if time.time()-t0>240: print('STOP budget, rerun to resume',flush=True); break
w.close()
