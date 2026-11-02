import warnings; warnings.filterwarnings('ignore')
from replicate import *
etf=adj['KBWB'].pct_change(); kre=adj['KRE'].pct_change(); S=pd.Timestamp('2026-07-31')
CM5=['JPM','BAC','GS','MS','C']; REST=[t for t in TK if t not in CM5]
K=port_returns(TK,start=S); X=port_returns(REST,start=S)
win=lambda s,a,b:s.loc[(s.index>a)&(s.index<=b)]
rows=[]
for b in ['2026-10-14','2026-10-21','2026-10-22','2026-10-23','2026-10-26','2026-10-27','2026-10-28','2026-10-29','2026-10-30']:
    b=pd.Timestamp(b); q=cum(win(kre,BASE,b)); e=cum(win(etf,BASE,b)); k=cum(win(K,BASE,b)); x=cum(win(X,BASE,b))
    rows.append(dict(end=b.date(),gap=100*(q-e),CM5_effect=100*(x-k),KRE_minus_exCM5=100*(q-x),share=(x-k)/(q-e)))
D=pd.DataFrame(rows); print(D.round(2).to_string()); D.round(4).to_csv(ROOT+'/out/end_date_sensitivity.csv',index=False)
