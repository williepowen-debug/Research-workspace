"""BOND 11/6: official-curve read once Treasury posts. Re-pulls issuer CSVs, then prints daily change, two-day net against 11/4,
real/nominal split, payroll-session comparison (release dates verified at LABOR's USDL records), and the HYG/IEF proxy."""
import urllib.request,io,sys,pandas as pd,yfinance as yf
U='https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=%s&_format=csv'
H={'User-Agent':'Mozilla/5.0 BOND research'}
def g(t,f):
    b=urllib.request.urlopen(urllib.request.Request(U%t,headers=H),timeout=35).read(); open('raw/'+f,'wb').write(b)
    d=pd.read_csv(io.BytesIO(b)); d['Date']=pd.to_datetime(d['Date']); return d.set_index('Date').sort_index()
n=g('daily_treasury_yield_curve','nominal.csv'); r=g('daily_treasury_real_yield_curve','real.csv')
print('frontier',n.index[-1].date(),r.index[-1].date())
c=['3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']
t=n[c].tail(4).T; print(t.to_string())
last=n.index[-1]; prev=n.index[-2]; pp=n.index[-3]
print('daily bp',((n.loc[last,c]-n.loc[prev,c])*100).round(0).to_dict())
print('vs 11/4 bp',((n.loc[last,c]-n.loc['2026-11-04',c])*100).round(0).to_dict())
for a,b in [('2 Yr','10 Yr'),('2 Yr','30 Yr'),('5 Yr','30 Yr')]:
    s=(n[b]-n[a])*100; print(a,b,s.tail(4).round(0).to_dict().values())
print('real'); rc=['5 YR','7 YR','10 YR','20 YR','30 YR']; print(r[rc].tail(4).T.to_string()); print('real daily bp',((r.loc[r.index[-1],rc]-r.loc[r.index[-2],rc])*100).round(0).to_dict())
for k,m in [('10 Yr','10 YR'),('30 Yr','30 YR'),('5 Yr','5 YR')]:
    if r.index[-1]==last:
        dn=(n.loc[last,k]-n.loc[prev,k])*100; dr=(r.loc[last,m]-r.loc[prev,m])*100
        print(k,'nominal',round(dn),'= real',round(dr),'+ residual',round(dn-dr),' nom-real',round(n.loc[last,k]-r.loc[last,m],2))
print('run 30Y>=5:',int((n['30 Yr'][::-1]>=5).cumprod().sum()),'of',len(n),'days',int((n['30 Yr']>=5).sum()))
print('run real10>=2.5:',int((r['10 YR'][::-1]>=2.5).cumprod().sum()))
print('payroll sessions: date, d2Y, d10Y, d30Y, d2s30s')
for x in ['2026-06-05','2026-07-02','2026-08-07','2026-09-04','2026-10-02',str(last.date())]:
    i=n.index.get_loc(pd.Timestamp(x)); a=n.iloc[i]; b=n.iloc[i-1]
    print(x,*(round((a[k]-b[k])*100) for k in ['2 Yr','10 Yr','30 Yr']),round(((a['30 Yr']-a['2 Yr'])-(b['30 Yr']-b['2 Yr']))*100))
d2=(n['2 Yr'].diff()*100).dropna(); print('|d2Y| 2026 pctile of today',round((d2.abs()<abs(d2.iloc[-1])).mean(),2),'median |d2Y|',d2.abs().median())
e=yf.download(['HYG','IEF'],period='3mo',progress=False,auto_adjust=False)['Close']; p=(e['HYG']/e['IEF']).dropna()
print('proxy',round(p.iloc[-1],4),p.index[-1].date(),'z20',round((p.iloc[-1]-p.tail(20).mean())/p.tail(20).std(),2),'pct3m',round((p<p.iloc[-1]).mean(),2))
