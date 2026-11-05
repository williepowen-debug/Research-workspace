"""US registered-fund holdings of Ueno Bank 6.70% 2031 (CUSIP 903934AB3) from SEC N-PORT. One-time.
Match is on the CUSIP or the exact issuer word, never a substring: 'ueno' alone also hits Buenos Aires and TrueNoord.
Latest report per series. Reports lag: nothing here is dated after the failure.
Usage (repo root): .venv/bin/python3 AGENTS/REGINALD/domain/sources/2026-11-05_ueno/nport_ueno.py OUTDIR"""
import subprocess,sys,json,re,time,collections
sys.path.insert(0,'scripts'); import sec_contact
ua=sec_contact.sec_ua("REGINALD {}")
def get(u):
    for i in range(4):
        time.sleep(0.2+i)
        o=subprocess.run(['curl','-s','-m','40','-H','User-Agent: '+ua,u],capture_output=True,text=True).stdout
        if o and not o.lstrip().startswith('<html') : return o
    return o
hits={}
W=[('2026-03-01','2026-06-20'),('2026-06-21','2026-07-31'),('2026-08-01','2026-09-10'),('2026-09-11','2026-09-30'),('2026-10-01','2026-11-05')]
for a,b in W:
    frm=0
    while True:
        d=json.loads(get('https://efts.sec.gov/LATEST/search-index?q=%22Ueno%20Bank%22%20OR%20UENOPY%20OR%20903934AB3&forms=NPORT-P&dateRange=custom&startdt='+a+'&enddt='+b+'&from='+str(frm)))
        H=d.get('hits',{}).get('hits',[])
        for x in H:
            z=x['_source']; hits[z['adsh']]=(z['file_date'],(z.get('display_names') or [''])[0],z['ciks'][0] if z.get('ciks') else None)
        print(a,b,d.get('hits',{}).get('total',{}).get('value'),'page',frm,len(H))
        frm+=len(H)
        if len(H)<100: break
print('filings',len(hits))
rows=[];fail=[]
for adsh,(fd,nm,cik) in hits.items():
    x=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{adsh.replace("-","")}/primary_doc.xml')
    if '<invstOrSec>' not in x: fail.append(adsh); continue
    g=lambda p,t=x:(re.search(p,t,re.S) or [None,''])[1].strip()
    ser=g(r'<seriesName>(.*?)</seriesName>'); rp=g(r'<repPdDate>(.*?)</repPdDate>'); net=g(r'<netAssets>(.*?)</netAssets>')
    for b in re.findall(r'<invstOrSec>(.*?)</invstOrSec>',x,re.S):
        n,t2,cu=g(r'<name>(.*?)</name>',b),g(r'<title>(.*?)</title>',b),g(r'<cusip>(.*?)</cusip>',b)
        if cu=='903934AB3' or re.search(r'\bUENO\s+BANK\b|\bUENOPY\b',n+' '+t2,re.I):
            rows.append(dict(fund=nm,series=ser,rep=rp,filed=fd,net=float(net or 0),name=n,title=t2,cusip=cu,mat=g(r'<maturityDt>(.*?)</maturityDt>',b),bal=float(g(r'<balance>(.*?)</balance>',b) or 0),val=float(g(r'<valUSD>(.*?)</valUSD>',b) or 0),pct=float(g(r'<pctVal>(.*?)</pctVal>',b) or 0),adsh=adsh))
json.dump(rows,open(sys.argv[1]+'/nport_rows.json','w'),indent=0)
print('rows',len(rows),'fail',len(fail),fail[:5])
print('distinct cusips',collections.Counter((r['cusip'],r['mat']) for r in rows))
lat={}
for r in rows:
    k=r['series']+'|'+r['cusip']
    if k not in lat or r['rep']>lat[k]['rep']: lat[k]=r
L=sorted(lat.values(),key=lambda r:-r['bal'])
print('series',len(L),'face $M',round(sum(r['bal'] for r in L)/1e6,2),'value $M',round(sum(r['val'] for r in L)/1e6,2),'share of $350M %.1f%%'%(sum(r['bal'] for r in L)/3.5e6))
print('latest report months',sorted(collections.Counter(r['rep'][:7] for r in L).items()))
print('max pct of fund',max(r['pct'] for r in L))
by=collections.Counter()
for r in L: by[re.sub(r'\s*\(.*','',r['fund'])[:36]]+=r['bal']
for k,v in by.most_common(16): print(f'{v/1e6:6.2f} {k}')
for r in L[:14]: print(f"{r['bal']/1e6:5.2f} {r['pct']:.2f}% {r['rep']} {r['series'][:50]} px {r['val']/r['bal']*100:.1f}")
m=collections.defaultdict(list)
for r in rows:
    if r['bal']: m[r['rep'][:7]].append(r['val']/r['bal']*100)
print('price by month',{k:round(sum(v)/len(v),1) for k,v in sorted(m.items())})
