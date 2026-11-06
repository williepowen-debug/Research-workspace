# BROCK 11/6 close refresh. 39-name discount on the latest XBRL NAV; closes are yfinance vendor bars, not official closes.
import sys,csv,json,time,statistics as st,urllib.request,warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'scripts')
from sec_contact import sec_ua
import yfinance as yf
ua=sec_ua() if callable(sec_ua) else sec_ua
rows=[r for r in csv.reader(open('AGENTS/BROCK/research/2026-10-31_R2-review/NAV_DISCOUNT_39.tsv'),delimiter='\t') if r and not r[0].startswith('#') and r[0]!='ticker']
navs={};fail=[]
for r in rows:
    t,cik=r[0],int(r[1]); best=(r[2],float(r[3]))
    try:
        j=json.load(urllib.request.urlopen(urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyconcept/CIK{cik:010d}/us-gaap/NetAssetValuePerShare.json',headers={'User-Agent':ua}),timeout=20))
        for v in j.get('units',{}).values():
            for f in v:
                if f.get('form') in('10-Q','10-K') and f['end']>best[0]: best=(f['end'],float(f['val']))
    except Exception as e: fail.append((t,str(e)[:40]))
    navs[t]=best; time.sleep(0.12)
tk=[r[0] for r in rows]
c=yf.download(tk,period='5d',interval='1d',auto_adjust=False,progress=False,threads=False)['Close']
print('last bar',c.index[-1].date(),'read',time.strftime('%H:%M:%S'),'missing',[t for t in tk if c[t].iloc[-1]!=c[t].iloc[-1]],'navfail',fail)
out=[]
for t in tk:
    p=float(c[t].iloc[-1]); n=navs[t]
    if p==p: out.append((t,n[0],n[1],round(p,2),round((1-p/n[1])*100,2)))
with open('AGENTS/BROCK/research/2026-11-06_close-refresh/NAV_DISCOUNT_39_close.tsv','w') as f:
    f.write('# 39-name discount, vendor closes session 2026-11-06 (yfinance Close, not official closes), latest XBRL NAV per share; mixed NAV vintages\nticker\tnav_date\tnav\tclose\tdiscount_pct\n')
    for x in out: f.write('\t'.join(map(str,x))+'\n')
d=[x[4] for x in out]
print('n',len(d),'median',round(st.median(d),2),'mean',round(st.mean(d),2),'>35',sum(x>35 for x in d),'<10',sum(x<10 for x in d),'prem',sum(x<0 for x in d))
from collections import Counter
print(Counter(x[1] for x in out))
six=[x[4] for x in out if x[0] in('ARCC','FSK','OBDC','BXSL','MAIN','GSBD')]
print('six',len(six),round(st.mean(six),2),round(st.median(six),2))
for x in out:
    if x[0] in('ARCC','BXSL','FSK','GBDC','HTGC','OBDC','MFIC'): print(x)
