"""BOND 11/9 closeout: official Treasury nominal/real cells for 11/9 (issuer CSVs), daily change, curve, runs."""
import urllib.request,io,pandas as pd
U='https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=%s&_format=csv'
H={'User-Agent':'Mozilla/5.0 BOND research'}
def g(t,f):
    b=urllib.request.urlopen(urllib.request.Request(U%t,headers=H),timeout=35).read(); open('raw/'+f,'wb').write(b)
    d=pd.read_csv(io.BytesIO(b)); d['Date']=pd.to_datetime(d['Date']); return d.set_index('Date').sort_index()
n=g('daily_treasury_yield_curve','nominal.csv'); r=g('daily_treasury_real_yield_curve','real.csv')
print('frontier',n.index[-1].date(),r.index[-1].date())
c=['2 Yr','3 Yr','5 Yr','10 Yr','20 Yr','30 Yr']; print(n[c].tail(3).T.to_string())
print('daily bp',((n[c].iloc[-1]-n[c].iloc[-2])*100).round(0).to_dict())
a=n.iloc[-1]; print('2s10s',round((a['10 Yr']-a['2 Yr'])*100),'5s30s',round((a['30 Yr']-a['5 Yr'])*100),'2s30s',round((a['30 Yr']-a['2 Yr'])*100),'20-30',round((a['20 Yr']-a['30 Yr'])*100))
rc=['5 YR','10 YR','30 YR']; print(r[rc].tail(3).T.to_string()); print('real daily bp',((r[rc].iloc[-1]-r[rc].iloc[-2])*100).round(0).to_dict())
print('run 30Y>=5:',int((n['30 Yr'][::-1]>=5).cumprod().sum()),'days',int((n['30 Yr']>=5).sum()),'of',len(n))
print('run real10>=2.5:',int((r['10 YR'][::-1]>=2.5).cumprod().sum()))
