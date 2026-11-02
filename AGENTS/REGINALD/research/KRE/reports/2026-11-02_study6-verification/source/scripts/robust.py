import warnings; warnings.filterwarnings('ignore')
from replicate import *; from reindex import *
OUT=ROOT+'/out'
etf=adj['KBWB'].pct_change(); kre=adj['KRE'].pct_change()
S=pd.Timestamp('2026-07-31'); A=pd.Timestamp('2026-10-14')
win=lambda s,a=BASE,b=END:s.loc[(s.index>a)&(s.index<=b)]
u8,_,_=nport(); u10,_,_=invesco()
SETS={'BAC':['BAC'],'GS+MS':['GS','MS'],'JPM+C':['JPM','C'],'CM5':['JPM','BAC','GS','MS','C'],'BAC+GS+MS':['BAC','GS','MS']}
r_st=stock_tr()
def reindexed_units(names):
    res=[]
    for ref in ['2026-05-29','2026-08-31']:
        T=pd.Series({t:tso_asof(t,ref) for t in names}); mc=T*close.loc[ref,names]
        w=cap_weights(mc); res.append(w/close.loc[ref,names])   # index shares per $1
    return res
def fixed_weight(names, w0):
    w=w0[names]/w0[names].sum(); return (r_st[names]*w).sum(1)
def ew(names): return r_st[names].mean(1)
rows=[]
def add(construction, full, ex_dict):
    k63=cum(win(full)); ka=cum(win(full,A)); ks=cum(win(full,BASE,A))
    for g,x in ex_dict.items():
        rows.append(dict(construction=construction,removed=g,full_63=100*k63,ex_63=100*cum(win(x)),effect_63=100*(cum(win(x))-k63),
                         full_rally=100*ka,ex_rally=100*cum(win(x,A)),effect_rally=100*(cum(win(x,A))-ka),
                         full_selloff=100*ks,ex_selloff=100*cum(win(x,BASE,A)),effect_selloff=100*(cum(win(x,BASE,A))-ks)))
# 1 baseline
for lab,sw,pre,post in [('A. Holdings, switch after 9/18 (baseline)',SW,None,None),('B. Holdings, switch after 8/31',pd.Timestamp('2026-08-31'),None,None),
                        ('C. Holdings, switch after 9/21',pd.Timestamp('2026-09-21'),None,None),('D. June units (8/31 N-PORT) throughout',END,u8,u8),('E. Sept units (10/30) throughout',pd.Timestamp('2026-01-01'),u10,u10)]:
    full=port_returns(TK,switch=sw,start=S,pre=pre,post=post)
    add(lab,full,{g:port_returns([t for t in TK if t not in ex],switch=sw,start=S,pre=pre,post=post) for g,ex in SETS.items()})
# F re-indexed by KBW rule
full=port_returns(TK,start=S)
d={}
for g,ex in SETS.items():
    nm=[t for t in TK if t not in ex]; a,b=reindexed_units(nm)
    d[g]=port_returns(nm,start=S,pre=a,post=b)
add('F. Re-indexed: KBW cap rule re-applied to remaining names',full,d)
# G fixed weights at 8/3, daily rebalanced
W0=weights_prev(TK,start=S).loc[BASE+pd.Timedelta(days=1):].iloc[0]
add('G. Fixed 8/3 weights, rebalanced daily',fixed_weight(TK,W0),{g:fixed_weight([t for t in TK if t not in ex],W0) for g,ex in SETS.items()})
# H equal weight (different construction)
add('H. Equal-weight, daily rebalanced (DIFFERENT construction)',ew(TK),{g:ew([t for t in TK if t not in ex]) for g,ex in SETS.items()})
# I price-only baseline
rp=P.pct_change()
def port_price(names):
    W=weights_prev(names,start=S); return (W*rp.loc[W.index,names]).sum(1)
add('I. Holdings baseline, PRICE-ONLY (no dividends)',port_price(TK),{g:port_price([t for t in TK if t not in ex]) for g,ex in SETS.items()})
R=pd.DataFrame(rows)
R.round(3).to_csv(f'{OUT}/robustness_grid.csv',index=False)
pd.set_option('display.width',250)
print(R.round(3).to_string())
print('KRE 63',100*cum(win(kre)),' rally',100*cum(win(kre,A)),' selloff',100*cum(win(kre,BASE,A)),' ETF',100*cum(win(etf)),100*cum(win(etf,A)),100*cum(win(etf,BASE,A)))
print('KRE price-only 63', 100*cum(win(close['KRE'].pct_change())),' ETF price-only',100*cum(win(close['KBWB'].pct_change())))
