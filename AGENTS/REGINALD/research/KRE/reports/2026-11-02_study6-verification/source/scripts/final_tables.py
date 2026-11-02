import warnings; warnings.filterwarnings('ignore')
from replicate import *; from attribution import run
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
OUT=ROOT+'/out'
etf=adj['KBWB'].pct_change(); kre=adj['KRE'].pct_change()
S=pd.Timestamp('2026-07-31'); A=pd.Timestamp('2026-10-14')
win=lambda s,a=BASE,b=END:s.loc[(s.index>a)&(s.index<=b)]
CM5=['JPM','BAC','GS','MS','C']; REST=[t for t in TK if t not in CM5]
K=win(port_returns(TK,start=S)); X=win(port_returns(REST,start=S)); E=win(etf); Q=win(kre)
fee=0.0035/252
# cumulative tracking path
cK=(1+K).cumprod(); cE=(1+E).cumprod(); cKn=(1+K-fee).cumprod()
dev=100*(cE-cK); devn=100*(cE-cKn)
print('cum tracking ETF-rep (pp): end',dev.iloc[-1].round(3),' max',dev.max().round(3),dev.idxmax().date(),' min',dev.min().round(3),dev.idxmin().date())
print('cum tracking ETF-rep_net (pp): end',devn.iloc[-1].round(3),' max',devn.max().round(3),' min',devn.min().round(3))
for a,b in [(BASE,pd.Timestamp('2026-08-31')),(pd.Timestamp('2026-08-31'),pd.Timestamp('2026-09-18')),(pd.Timestamp('2026-09-18'),END)]:
    print(f' segment {a.date()}->{b.date()}: ETF {100*cum(win(etf,a,b)):.3f} rep {100*cum(win(port_returns(TK,start=S),a,b)):.3f} rep_net {100*cum(win(port_returns(TK,start=S),a,b)-fee):.3f}')
# per-stock linked attribution by period
rows=[]
for lab,(a,b) in {'63d 8/3-10/30':(BASE,END),'selloff 8/3-10/14':(BASE,A),'rally 10/14-10/30':(A,END)}.items():
    r=run(a,b); L=100*r['linked']
    rows.append(dict(period=lab,KBWB_rep=100*r['K'],KBWB_exCM5=100*r['X'],BAC=L['BAC'],GS=L['GS'],MS=L['MS'],JPM=L['JPM'],C=L['C'],GS_MS=L['GS']+L['MS'],JPM_C=L['JPM']+L['C'],CM5_total=L.sum(),
                     KRE=100*cum(win(kre,a,b)),KBWB_ETF=100*cum(win(etf,a,b))))
T=pd.DataFrame(rows).set_index('period'); T['KRE_minus_exCM5']=T.KRE-T.KBWB_exCM5; T['tracking_rep_minus_ETF']=T.KBWB_rep-T.KBWB_ETF; T['gap_KRE_minus_ETF']=T.KRE-T.KBWB_ETF
T['check']=T.KRE_minus_exCM5+T.CM5_total+T.tracking_rep_minus_ETF-T.gap_KRE_minus_ETF
print(T.round(3).T.to_string()); T.round(4).to_csv(f'{OUT}/corrected_attribution_linked.csv')
# daily series out
r=run(); W=win(weights_prev(TK,start=S))
daily=pd.DataFrame({'KRE_TR':Q,'KBWB_ETF_TR':E,'KBWB_rep':K,'KBWB_exCM5':X})
for t in CM5: daily['c_'+t]=r['c'][t]; daily['w_'+t]=W[t]
daily['link_factor']=r['A']; daily.to_csv(f'{OUT}/daily_reconstruction.csv')
# figure
fig,ax=plt.subplots(1,2,figsize=(13,4.8))
for s,l,st in [(Q,'KRE (actual, TR)','-'),(E,'KBWB (actual, TR)','-'),(K,'KBWB reconstructed','--'),(X,'KBWB ex-JPM/BAC/GS/MS/C','-')]:
    ax[0].plot(100*((1+s).cumprod()-1),st,label=l)
ax[0].axvline(pd.Timestamp('2026-09-14'),color='grey',lw=.7); ax[0].axvline(A,color='grey',lw=.7); ax[0].set_title('Cumulative total return from 8/3 close (%)'); ax[0].legend(fontsize=8); ax[0].grid(alpha=.3)
cq=100*((1+Q).cumprod()-1); ce=100*((1+E).cumprod()-1); cx=100*((1+X).cumprod()-1); ck=100*((1+K).cumprod()-1)
ax[1].plot(cq-ce,'C0',lw=2,label='KRE minus KBWB (actual): the gap to explain')
ax[1].plot(cx-ck,'C3',label='KBWB ex-five minus KBWB (reconstructed): five-bank effect')
ax[1].plot(cq-cx,'C2',label='KRE minus KBWB ex-five: what remains')
for d in ['2026-09-14','2026-10-14']: ax[1].axvline(pd.Timestamp(d),color='grey',lw=.7)
ax[1].set_title('Running cumulative return differences from 8/3 (pp)'); ax[1].legend(fontsize=8); ax[1].grid(alpha=.3); ax[1].axhline(0,color='k',lw=.5)
plt.tight_layout(); plt.savefig(f'{OUT}/fig_verification.png',dpi=130)
