"""Exact additive attribution of the ex-CM5 counterfactual effect, KBWB contribution-to-return, gap reconciliation."""
import warnings; warnings.filterwarnings('ignore')
from replicate import *
OUT=ROOT+'/out'; import os; os.makedirs(OUT,exist_ok=True)
etf=adj['KBWB'].pct_change(); kre=adj['KRE'].pct_change()
win=lambda s,a=BASE,b=END:s.loc[(s.index>a)&(s.index<=b)]
S=pd.Timestamp('2026-07-31')
CM5=['JPM','BAC','GS','MS','C']; REST=[t for t in TK if t not in CM5]
def run(a=BASE,b=END,switch=SW):
    K=win(port_returns(TK,start=S,switch=switch),a,b); X=win(port_returns(REST,start=S,switch=switch),a,b)
    W=win(weights_prev(TK,start=S,switch=switch),a,b); r=win(stock_tr()[TK],a,b)
    # daily identity: X_t - K_t = sum_i in CM5 w_i,t-1 (X_t - r_i,t)
    c=W[CM5].mul(X,axis=0)-W[CM5]*r[CM5]
    assert np.allclose(c.sum(1),X-K,atol=1e-12)
    gK=(1+K).cumprod(); gX=(1+X).cumprod()
    pre=gK.shift(1).fillna(1.0)                        # prod_{s<t}(1+K_s)
    post=(gX.iloc[-1]/gX)                              # prod_{s>t}(1+X_s)
    A=pre*post
    linked=c.mul(A,axis=0).sum()                       # exact: sums to cumX-cumK
    cumK=gK.iloc[-1]-1; cumX=gX.iloc[-1]-1
    assert abs(linked.sum()-(cumX-cumK))<1e-12
    # contribution to KBWB return (per $1 at base): sum_t w_i,t-1 r_i,t * prod_{s<t}(1+K_s)
    contrib=(W*r).mul(pre,axis=0).sum()
    assert abs(contrib.sum()-cumK)<1e-12
    # stock cumulative TR (dividends reinvested in stock)
    stock_cum=(1+r).prod()-1
    avgw=W.mean()
    return dict(K=cumK,X=cumX,linked=linked,contrib=contrib,stock_cum=stock_cum,avgw=avgw,W0=W.iloc[0],c=c,A=A,Kd=K,Xd=X)
if __name__=='__main__':
    res=run(); e=cum(win(etf)); k=cum(win(kre))
    L=res['linked']
    print('cumK',res['K'],'cumX',res['X'],'X-K',res['X']-res['K'])
    print('linked per stock (pp):',(100*L).round(3).to_dict())
    grp={'BAC':['BAC'],'GS+MS':['GS','MS'],'JPM+C':['JPM','C']}
    print({g:round(100*L[v].sum(),3) for g,v in grp.items()})
    tab=pd.DataFrame({'w_start_8/3':100*res['W0'],'avg_w':100*res['avgw'],'stock_TR_63d':100*res['stock_cum'],'contrib_to_KBWB_pp':100*res['contrib']}).sort_values('contrib_to_KBWB_pp')
    tab.loc['TOTAL']=[tab['w_start_8/3'].sum(),tab['avg_w'].sum(),np.nan,tab['contrib_to_KBWB_pp'].sum()]
    print(tab.round(3).to_string()); tab.round(4).to_csv(f'{OUT}/kbwb_contrib_63d.csv')
    # rally
    r2=run(pd.Timestamp('2026-10-14'),END)
    print('RALLY K',r2['K'],'X',r2['X'],{g:round(100*r2['linked'][v].sum(),3) for g,v in grp.items()})
    r3=run(BASE,pd.Timestamp('2026-10-14'))
    print('SELLOFF K',r3['K'],'X',r3['X'],{g:round(100*r3['linked'][v].sum(),3) for g,v in grp.items()}, 'KRE',cum(win(kre,BASE,pd.Timestamp('2026-10-14'))),'ETF',cum(win(etf,BASE,pd.Timestamp('2026-10-14'))))
