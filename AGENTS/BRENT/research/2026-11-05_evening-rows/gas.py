import sys,json,datetime as dt,urllib.request
sys.path.insert(0,'/home/willi/Research-workspace/FORGE/tools/market-data')
import fetch as F
u='https://api.eia.gov/v2/seriesid/PET.EMM_EPMR_PTE_NUS_DPG.W?api_key=%s&length=1800'%F.EIA_API_KEY
r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'research-client/1.0'}),timeout=40))
rows=sorted((dt.date.fromisoformat(d['period']),float(d['value'])) for d in r['response']['data'] if d['value'] is not None)
print(r['response']['data'][0].get('series-description'),rows[-4:]);G=dict(rows)
a=dt.date(2026,11,2);b=a-dt.timedelta(days=364);print('yoy',G[a],G[b],(G[a]/G[b]-1)*100)
last=rows[-1][1];need=4.0/last-1
out=[]
for y in range(1995,2026):
    s=[k for k in G if k.year==y and k.month==11 and k.day<=7]
    if not s: continue
    k=s[0];p=[G.get(k+dt.timedelta(days=7*i)) for i in range(1,8)]
    if None in p: continue
    out.append((y,G[k],round(min(p)/G[k]-1,4)))
print(out);print('need',round(need,4),sum(o[2]<=need for o in out),len(out))
