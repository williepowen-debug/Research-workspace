import json, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
from replicate import *
tso=json.load(open(ROOT+'/data/tso.json'))
def tso_asof(t, filed_before):
    v=[x for x in tso.get(t,[]) if x['filed']<=filed_before]
    return float(v[-1]['val']) if v else np.nan
def cap_weights(mcap, top_cap=0.08, n_top=5, rest_cap=0.04):
    w=mcap/mcap.sum(); w=w.copy()
    order=mcap.sort_values(ascending=False).index; top=list(order[:n_top]); rest=list(order[n_top:])
    # stage 1: cap all at 8% iteratively
    for _ in range(50):
        over=w>top_cap+1e-12
        if not over.any(): break
        ex=(w[over]-top_cap).sum(); w[over]=top_cap; free=~over & (w<top_cap)
        w[free]+=ex*w[free]/w[free].sum()
    # stage 2: non-top capped at 4%, excess to uncapped non-top... (methodology: redistribute across remaining securities)
    for _ in range(50):
        over=pd.Series(False,index=w.index); over[rest]=w[rest]>rest_cap+1e-12
        if not over.any(): break
        ex=(w[over]-rest_cap).sum(); w[over]=rest_cap
        recv=[t for t in w.index if (t in top and w[t]<top_cap-1e-12) or (t in rest and w[t]<rest_cap-1e-12)]
        w[recv]+=ex*w[recv]/w[recv].sum()
        # re-cap top at 8
        o2=w>top_cap+1e-12
        if o2.any():
            ex2=(w[o2]-top_cap).sum(); w[o2]=top_cap
            recv=[t for t in rest if w[t]<rest_cap-1e-12]; w[recv]+=ex2*w[recv]/w[recv].sum()
    return w
if __name__=='__main__':
    u8,_,_=nport(); u10,_,_=invesco()
    for ref,filed,u in [('2026-05-29','2026-05-29',u8),('2026-08-31','2026-08-31',u10)]:
        T=pd.Series({t:tso_asof(t,filed) for t in TK})
        ratio=(u/T); unc=['NTRS','MTB','HBAN','CFG','RF','KEY','EWBC','PNFP','FHN','ZION','WAL']
        print(ref,'uncapped u/TSO ratio rel. to median:',(ratio[unc]/ratio[unc].median()).round(4).to_dict())
        # full 24-name rule check (C TSO may be stale; only matters for its capped weight)
        mc=T*close.loc[ref,TK]; w=cap_weights(mc.dropna())
        act=u*close.loc[ref,TK]; act=act/act.sum()
        print(' rule vs actual weights max abs diff (pp):', (100*(w-act[w.index]).abs()).max().round(3), (100*(w-act[w.index])).round(2).loc[lambda s:s.abs()>0.05].to_dict())
