import warnings; warnings.filterwarnings('ignore')
from replicate import *; from attribution import run
import json
OUT=ROOT+'/out'
etf=adj['KBWB'].pct_change(); kre=adj['KRE'].pct_change()
S=pd.Timestamp('2026-07-31')
win=lambda s,a=BASE,b=END:s.loc[(s.index>a)&(s.index<=b)]
CM5=['JPM','BAC','GS','MS','C']; REST=[t for t in TK if t not in CM5]
K=port_returns(TK,start=S); X=port_returns(REST,start=S); CMb=port_returns(CM5,start=S)
# 1. start-date sensitivity
rows=[]
for a in ['2026-07-31','2026-08-03','2026-08-14','2026-08-31','2026-09-11','2026-09-14','2026-09-30','2026-10-14']:
    a=pd.Timestamp(a); kr=cum(win(kre,a)); e=cum(win(etf,a)); k=cum(win(K,a)); x=cum(win(X,a))
    rows.append(dict(base_close=a.date(),sessions=len(win(kre,a)),KRE=100*kr,KBWB_ETF=100*e,KBWB_rep=100*k,KBWB_exCM5=100*x,gap_KRE_minus_ETF=100*(kr-e),CM5_effect=100*(x-k),KRE_minus_exCM5=100*(kr-x),tracking=100*(k-e)))
SD=pd.DataFrame(rows); SD.round(3).to_csv(f'{OUT}/start_date_sensitivity.csv',index=False); print(SD.round(2).to_string())
# 2. arithmetic daily vs compounded
d=win(X)-win(K); res=run()
print('\nArithmetic sum of daily (X-K):',100*d.sum(),' compounded:',100*(cum(win(X))-cum(win(K))))
print('Arithmetic sum daily per stock c_i:',(100*res['c'].sum()).round(3).to_dict(),' linked:',(100*res['linked']).round(3).to_dict())
g=win(kre)-win(etf); print('Arithmetic sum of daily KRE-ETF gaps:',100*g.sum(),' compounded gap',100*(cum(win(kre))-cum(win(etf))))
print('9/14 day: KRE',100*kre['2026-09-14'],'ETF',100*etf['2026-09-14'],'rep',100*K['2026-09-14'],'X',100*X['2026-09-14'],'CM5 basket',100*CMb['2026-09-14'],'BAC',100*stock_tr().loc['2026-09-14','BAC'])
# 3. correlation in window
C=pd.DataFrame({'KRE':win(kre),'KBWB_ETF':win(etf),'KBWB_rep':win(K),'KBWB_exCM5':win(X),'CM5_basket':win(CMb),'SPY':win(adj['SPY'].pct_change())})
for t in ['BAC','JPM','GS','MS','C','WFC']: C[t]=win(stock_tr()[t])
print('\nwindow corr with KRE:',C.corr()['KRE'].round(3).to_dict())
gap_full=C.KRE-C.KBWB_rep; gap_ex=C.KRE-C.KBWB_exCM5
print('var share: var(KRE-exCM5)/var(KRE-rep)=',gap_ex.var()/gap_full.var(),' sd daily gap full',gap_full.std()*100,' ex',gap_ex.std()*100)
C.to_csv(f'{OUT}/window_daily_returns.csv')
