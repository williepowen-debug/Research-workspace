"""KB-LIQ-136 Q3 verdict and KB-LIQ-144 month-turn re-check, plus upcoming coupon auctions. One-off."""
import json,sys,pathlib
sys.path.insert(0,'FORGE/tools/market-data')
from fetch import fred_fetch
P=pathlib.Path(__file__).parent
d=json.load(open(P/'treasury_upcoming.json'))
print(list(d[0].keys())[:12])
for x in sorted(d,key=lambda r:r.get('auctionDate') or r.get('AuctionDate','')):
    g=lambda k:x.get(k) or x.get(k[0].upper()+k[1:])
    print(str(g('auctionDate'))[:10],g('securityType'),g('securityTerm'),'issue',str(g('issueDate'))[:10],g('offeringAmount'))
def s(sid,n):
    return {r['date']:float(r['value']) for r in fred_fetch(sid,limit=n) if r.get('value') not in ('.','',None)}
so,s99,io,srf=s('SOFR',60),s('SOFR99',60),s('IORB',60),s('RPONTTLD',60)
print('--136 Q3')
for dt in ['2026-10-01','2026-10-02','2026-10-05','2026-10-07']:
    print(dt,'SOFR-IORB',round((so[dt]-io[dt])*100),'SOFR99-IORB',round((s99[dt]-io[dt])*100),'SRF',srf.get(dt))
w=s('WRESBAL',8); print('WRESBAL min since 10/1',min(v for k,v in w.items() if k>='2026-10-01'))
b=s('BAMLH0A2HYB',800); c=s('BAMLH0A3HYC',800)
ds=sorted(set(b)&set(c)); gap={k:round((c[k]-b[k])*100) for k in ds}
turns=[]
for i in range(1,len(ds)):
    if ds[i][:7]!=ds[i-1][:7]: turns.append((ds[i],gap[ds[i]]-gap[ds[i-1]]))
others=[gap[ds[i]]-gap[ds[i-1]] for i in range(1,len(ds)) if ds[i][:7]==ds[i-1][:7]]
up=sum(1 for _,v in turns if v>0)
print('--144 n',len(turns),'first',turns[0],'rise share',round(up/len(turns)*100,1),'mean',round(sum(v for _,v in turns)/len(turns),1),'others mean',round(sum(others)/len(others),2))
print('last 4',turns[-4:],'rank of 11/02',sorted(v for _,v in turns).index(turns[-1][1])+1)
