import sys,csv,json,time,statistics as st,warnings
warnings.filterwarnings('ignore')
S='/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-BROCK/242d91ef-fe7f-40c2-ac6e-a78d689f8e12/scratchpad'
sys.path.insert(0,S)
from edgar import *
import yfinance as yf
rows=[r for r in csv.reader(open('AGENTS/BROCK/research/2026-10-31_R2-review/NAV_DISCOUNT_39.tsv'),delimiter='\t') if r and not r[0].startswith('#') and r[0]!='ticker']
print(len(rows))
navs={}
for r in rows:
    t,cik=r[0],int(r[1])
    c,b=get(f'https://data.sec.gov/api/xbrl/companyconcept/CIK{cik:010d}/us-gaap/NetAssetValuePerShare.json')
    best=(r[2],float(r[3]),r[4],r[5])
    if c==200:
        u=json.loads(b).get('units',{})
        for k,v in u.items():
            for f in v:
                if f.get('form') in('10-Q','10-K') and f['end']>best[0]:
                    best=(f['end'],float(f['val']),f['form'],f.get('filed'))
    navs[t]=best
tk=[r[0] for r in rows]
px=yf.download(tk,period='3d',interval='1d',auto_adjust=False,progress=False)['Close'].iloc[-1]
print('px time',time.strftime('%H:%M:%S'))
out=[]
for t in tk:
    p=float(px[t]); n=navs[t]
    out.append((t,n[0],n[1],round(p,2),round((1-p/n[1])*100,2)))
d=sorted(x[4] for x in out if x[4]==x[4])
print('n',len(d),'median',round(st.median(d),2),'>35',sum(x>35 for x in d),'<10',sum(x<10 for x in d),'prem',sum(x<0 for x in d))
print('NAV vintage count',{k:sum(1 for x in out if x[1]==k) for k in set(x[1] for x in out)})
for x in out:
    if x[0] in('ARCC','BXSL','FSK','GBDC','HTGC','OBDC','MAIN','OTF','TCPC','MFIC','PSEC'): print(x)
six=[x[4] for x in out if x[0] in('ARCC','BXSL','FSK','GBDC','HTGC','OBDC')]
print('six',round(st.median(six),2), round(sum(six)/len(six),2),six)
json.dump(out,open(S+'/nav39_live.json','w'))
