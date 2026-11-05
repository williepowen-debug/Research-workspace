"""WQ-596 base rates for BND-34..37, computed 2026-11-05 before any resolving print. Run from AGENTS/BOND/monitors."""
import sys,re,io,csv,datetime as dt,requests,warnings,os
sys.path.insert(0,os.getcwd())
import pandas as pd,numpy as np
warnings.filterwarnings('ignore')
import fr2004_fetch as fr
key=None
for l in open('../../../FORGE/tools/market-data/.env'):
    m=re.match(r'\s*FRED_API_KEY\s*=\s*"?([^"\s]+)',l)
    if m:key=m.group(1)
def fred(s,start='1962-01-01'):
    j=requests.get('https://api.stlouisfed.org/fred/series/observations',params=dict(series_id=s,api_key=key,file_type='json',observation_start=start),timeout=30).json()
    d=pd.DataFrame(j['observations']);d=d[d.value!='.']
    return pd.Series(d.value.astype(float).values,index=pd.to_datetime(d.date))
# A HY
hy=(fred('BAMLH0A0HYM2','2023-01-01')*100).round()
N=38  # sessions 11/5..12/31 inclusive, roughly
fmax=hy[::-1].rolling(N,min_periods=N).max()[::-1].shift(-1)
d=pd.DataFrame({'hy':hy,'fmax':fmax}).dropna()
for lo,hi in [(320,345),(335,355)]:
    s=d[(d.hy>=lo)&(d.hy<=hi)]
    print(f'HY start {lo}-{hi}: n={len(s)} max>=351 {100*(s.fmax>=351).mean():.0f}%  (nonoverlap approx n/{N}={len(s)/N:.1f})')
print('HY window',hy.index[0].date(),hy.index[-1].date(),'n',len(hy),'share of days >=351',round(100*(hy>=351).mean(),1))
# B 10Y
y=fred('DGS10')
for st in ['1962-01-01','2022-01-01']:
    c=(y.shift(-38)-y)[st:].dropna()*100
    print(f'10Y 38-session change from {st}: n={len(c)} mean {c.mean():+.1f} sd {c.std():.1f} P(>=+8) {100*(c>=8).mean():.0f}%  P(>=+7){100*(c>=7).mean():.0f}%')
ch5=(y-y.shift(5))*100
c=(y.shift(-38)-y)
m=(ch5<=-10)
cc=c[m]['2022-01-01':].dropna()*100
print(f'  after 5-session fall>=10bp since 2022: n={len(cc)} P(>=+8) {100*(cc>=8).mean():.0f}%')
# C FR2004: LONG-END = 7-11Y + 11-21Y + >21Y, weekly
sb=fr.current_seriesbreak(dt.date.today())
ser={l:pd.Series(fr.fetch(k,sb)) for k,l in fr.BUCKETS}
df=pd.DataFrame(ser).astype(float).sort_index()
print('labels',list(df.columns),'n',len(df),df.index[0],df.index[-1])
long_cols=[c for c in df.columns if any(t in c for t in ('7-11','7–11','11-21','11–21','21'))]
long_cols=list(dict.fromkeys(long_cols))
print('long cols',long_cols)
L=df[long_cols].sum(axis=1)
print('last',L.tail(4).round(3).to_dict())
for w in (8,):
    c=(L.shift(-w)-L).dropna()
    print(f'{w}-week change n={len(c)} mean {c.mean():+.1f} sd {c.std():.1f} P(>=+5) {100*(c>=5).mean():.0f}% P(>0) {100*(c>0).mean():.0f}%')
    c2=c.tail(52); print(f'  last 52 windows mean {c2.mean():+.1f} P(>=+5) {100*(c2>=5).mean():.0f}%')
# D PMMS
t=requests.get('https://www.freddiemac.com/pmms/docs/PMMS_history.csv',timeout=30,headers={'User-Agent':'BOND-research'}).text
rows=list(csv.reader(io.StringIO(t)));h=rows[0];print(h[:3],rows[-1][:3])
p=pd.Series({pd.to_datetime(r[0]):float(r[1]) for r in rows[1:] if r[1]}).sort_index()
for st in ('1971-01-01','2022-01-01'):
    q=p[st:]
    fm=q[::-1].rolling(8,min_periods=8).min()[::-1].shift(-1)
    x=(fm-q).dropna()
    print(f'PMMS from {st}: n={len(x)} P(min next 8 weekly <= -0.19) {100*(x<=-0.19).mean():.0f}%')
s=(p-y.reindex(p.index,method='ffill')).dropna()*100
print('PMMS-10Y spread last 12',s.tail(12).round(0).tolist(),'median 26',round(s.tail(26).median(),0))
