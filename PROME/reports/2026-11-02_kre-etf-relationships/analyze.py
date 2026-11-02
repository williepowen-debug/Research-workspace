"""Reproducible descriptive study. No owner grades or trading rules are changed."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

P = Path(__file__).resolve().parent
symbols = ['KRE','KBWB','XLF','IWM','SPY','RSP','QQQ','HYG','LQD','IEF','TLT','VNQ','SHY']
frames = {}
checks = {}
for s in symbols:
    f = pd.read_csv(P / f'{s}_daily.csv')
    f.index = pd.to_datetime(f['Date'].str[:10])
    assert f.index.is_unique and f.index.is_monotonic_increasing, s
    assert (f[['Close','Adj Close']] > 0).all().all(), s
    checks[s] = {'missing_adjusted': int(f['Adj Close'].isna().sum()),
                 'first': str(f.index.min().date()), 'last': str(f.index.max().date()),
                 'max_abs_daily_return_pct': float(f['Adj Close'].pct_change(fill_method=None).abs().max()*100)}
    frames[s] = f
allpx = pd.concat({s:f['Adj Close'] for s,f in frames.items()}, axis=1)
assert not allpx.isna().any().any(), 'Missing dates: do not forward fill'
px = allpx.loc[:'2026-10-30'].copy()
assert str(px.index[-1].date()) == '2026-10-30'
ret = px.pct_change(fill_method=None).dropna()
px.to_csv(P/'aligned_adjusted_closes.csv', index_label='date')

summary = pd.DataFrame(index=symbols)
for n in [1,5,20,63,126,252]:
    summary[f'{n}d_pct'] = (px.iloc[-1]/px.iloc[-n-1]-1)*100
summary['YTD_pct'] = (px.iloc[-1]/px.loc[:'2025-12-31'].iloc[-1]-1)*100
summary['since_Oct14_pct'] = (px.iloc[-1]/px.loc['2026-10-14']-1)*100
summary['since_Aug3_pct'] = (px.iloc[-1]/px.loc['2026-08-03']-1)*100
summary['drawdown_126d_pct'] = (px.iloc[-1]/px.tail(126).max()-1)*100
summary.to_csv(P/'performance.csv', index_label='ETF')
intraday = pd.DataFrame(index=symbols)
for s in symbols:
    f = frames[s]
    intraday.loc[s,'last_unadjusted'] = f.loc['2026-11-02','Close']
    intraday.loc[s,'day_pct'] = (f.loc['2026-11-02','Close']/f.loc['2026-10-30','Close']-1)*100
intraday.to_csv(P/'intraday_snapshot.csv',index_label='ETF')

corr = pd.DataFrame(index=symbols)
for label, data in [('full_2012_2026',ret),('252d',ret.tail(252)),('63d',ret.tail(63)),('20d',ret.tail(20))]:
    corr[label] = data.corr()['KRE']
corr.to_csv(P/'daily_return_correlations.csv',index_label='ETF')

# Conditional linear comparison: estimate coefficients only on the 252 days
# BEFORE the last 20-day evaluation interval. Daily simple returns, intercept.
models = {}
train,test = ret.iloc[-272:-20],ret.iloc[-20:]
for label, cols in [('market',['SPY']),('size_and_market',['SPY','IWM']),
                    ('banks_size_rates',['KBWB','IWM','IEF'])]:
    x = np.column_stack([np.ones(len(train)),train[cols].values])
    y = train.KRE.values
    b = np.linalg.lstsq(x,y,rcond=None)[0]
    pred = np.column_stack([np.ones(len(test)),test[cols].values])@b
    resid = test.KRE.values-pred
    models[label] = {'training_start':str(train.index[0].date()),'training_end':str(train.index[-1].date()),
                    'evaluation_start':str(test.index[0].date()),'evaluation_end':str(test.index[-1].date()),
                    'intercept':float(b[0]),'betas':dict(zip(cols,b[1:].tolist())),
                    'train_R2':float(1-np.sum((y-x@b)**2)/np.sum((y-y.mean())**2)),
                    'actual_compound_pct':float((np.prod(1+test.KRE.values)-1)*100),
                    'predicted_compound_pct':float((np.prod(1+pred)-1)*100),
                    'residual_daily_sum_pp':float(resid.sum()*100)}
(P/'conditional_models.json').write_text(json.dumps(models,indent=2)+'\n')

# Explicit calendar comparisons: chosen for contrasting episodes, not optimized
# to fit current returns. Window returns start at the stated prior close.
episodes = [('2016 Nov-Dec','2016-10-31','2016-12-30'),
            ('2020 Nov-Dec','2020-10-30','2020-12-31'),
            ('2023 Mar-May','2023-02-28','2023-05-31'),
            ('2023 Nov-Dec','2023-10-31','2023-12-29'),
            ('2024 July','2024-06-28','2024-07-31'),
            ('2026 Aug-Oct','2026-08-03','2026-10-14'),
            ('2026 Oct rebound','2026-10-14','2026-10-30')]
ep = pd.DataFrame({name:(px.loc[end]/px.loc[start]-1)*100 for name,start,end in episodes}).T
ep.to_csv(P/'historical_windows.csv', index_label='window')

# Exploratory nearest historical states: 6 pre-specified dimensions. All
# candidate dates <=2025-12-31, with outcomes observed before current cutoff.
# Standardization uses candidates only; features overlap, no causal inference.
r20=px.pct_change(20,fill_method=None)
r63=px.pct_change(63,fill_method=None)
features=pd.DataFrame({'KRE20':r20.KRE,'KRE63':r63.KRE,
    'KRE_minus_IWM20':r20.KRE-r20.IWM,'KRE_minus_KBWB20':r20.KRE-r20.KBWB,
    'RSP_minus_QQQ20':r20.RSP-r20.QQQ,'IEF20':r20.IEF}).dropna()
candidates=features.loc[:'2025-12-31']
sd=candidates.std(ddof=1)
dist=np.sqrt((((candidates-features.iloc[-1])/sd)**2).mean(axis=1)).sort_values()
positions={d:i for i,d in enumerate(px.index)}
selected=[]
for d,v in dist.items():
    if all(abs(positions[d]-positions[e])>126 for e in selected):
        selected.append(d)
    if len(selected)==8: break
analog=[]
for d in selected:
    i=positions[d]
    row={'date':str(d.date()),'distance':float(dist.loc[d])}
    for n in [21,63]:
        row[f'KRE_forward_{n}d_pct']=float((px.KRE.iloc[i+n]/px.KRE.iloc[i]-1)*100)
        row[f'KRE_minus_SPY_forward_{n}d_pp']=float(((px.KRE.iloc[i+n]/px.KRE.iloc[i]-1)-(px.SPY.iloc[i+n]/px.SPY.iloc[i]-1))*100)
        row[f'worst_close_vs_entry_{n}d_pct']=float((px.KRE.iloc[i+1:i+n+1].min()/px.KRE.iloc[i]-1)*100)
    row.update({k:float(v*100) for k,v in features.loc[d].items()})
    analog.append(row)
pd.DataFrame(analog).to_csv(P/'exploratory_analogs.csv',index=False)
features.tail(1).mul(100).to_csv(P/'current_analog_features_pct.csv',index_label='date')
baseline={str(n):{'mean_pct':float((px.KRE.shift(-n)/px.KRE-1).dropna().mean()*100),
                 'median_pct':float((px.KRE.shift(-n)/px.KRE-1).dropna().median()*100)} for n in [21,63]}
(P/'checks_and_baseline.json').write_text(json.dumps({'checks':checks,'rows_completed':len(px),
    'return_observations':len(ret),'baseline_overlapping_all_days':baseline},indent=2)+'\n')

plt.rcParams.update({'figure.facecolor':'#f7f9fc','axes.facecolor':'white',
    'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,
    'grid.alpha':.18,'font.size':10,'savefig.facecolor':'#f7f9fc'})
colors={'KRE':'#d35400','KBWB':'#305f9a','IWM':'#008578','SPY':'#555b66',
        'RSP':'#8a59a5','QQQ':'#bd407a','HYG':'#58923b','IEF':'#5199aa'}
fig,axs=plt.subplots(2,2,figsize=(15,10),layout='constrained')
base=px.loc[:'2025-12-31'].iloc[-1]
for s in ['KRE','KBWB','IWM','SPY','QQQ']:
    axs[0,0].plot(px.loc['2026':].index,(px.loc['2026':,s]/base[s]-1)*100,label=s,color=colors[s],lw=2 if s=='KRE' else 1.4)
axs[0,0].set_title('2026 total-return proxies: the broader picture',loc='left',weight='bold')
axs[0,0].set_ylabel('Return since Dec 31, 2025 (%)');axs[0,0].legend(ncol=3)
for s in ['KBWB','IWM','SPY','QQQ']:
    ratio=px.KRE/px[s]
    rb=ratio.loc[:'2025-12-31'].iloc[-1]
    axs[0,1].plot(ratio.loc['2026':].index,100*(ratio.loc['2026':]/rb-1),label=f'KRE / {s}',color=colors[s])
axs[0,1].axhline(0,color='gray',lw=.8)
axs[0,1].set_title('Relative strength: rising = KRE outperforming',loc='left',weight='bold')
axs[0,1].set_ylabel('Change in adjusted-price ratio (%)');axs[0,1].legend(ncol=2)
for s in ['KRE','KBWB','IWM','RSP','QQQ','HYG','IEF']:
    seg=px.loc['2026-10-14':,s]
    axs[1,0].plot(seg.index,(seg/seg.iloc[0]-1)*100,label=s,color=colors[s])
axs[1,0].set_title('October rebound: Oct 14 close = 0%',loc='left',weight='bold')
axs[1,0].set_ylabel('Adjusted return (%)');axs[1,0].legend(ncol=4)
for s in ['KBWB','IWM','QQQ','IEF']:
    rc=ret.KRE.rolling(63).corr(ret[s])
    axs[1,1].plot(rc.loc['2022':].index,rc.loc['2022':],label=s,color=colors[s])
axs[1,1].axhline(0,color='gray',lw=.8);axs[1,1].set_ylim(-1,1)
axs[1,1].set_title('63-session correlations change with the regime',loc='left',weight='bold')
axs[1,1].set_ylabel('Daily-return correlation with KRE');axs[1,1].legend(ncol=4)
for ax in axs.flat: ax.tick_params(axis='x',rotation=25)
fig.suptitle('KRE relationships | completed sessions through October 30, 2026\nYahoo adjusted closes; distributions/splits adjusted; November 2 intraday excluded',fontsize=15,weight='bold')
fig.savefig(P/'kre_relationships.png',dpi=160);plt.close(fig)

fig,ax=plt.subplots(figsize=(12,6),layout='constrained')
cols=['KRE','KBWB','IWM','SPY','QQQ','HYG','IEF','VNQ']
arr=ep[cols].values
im=ax.imshow(arr,cmap='RdYlGn',vmin=-35,vmax=35,aspect='auto')
ax.set_xticks(range(len(cols)),cols);ax.set_yticks(range(len(ep)),ep.index)
for i in range(len(ep)):
    for j in range(len(cols)):
        ax.text(j,i,f'{arr[i,j]:+.1f}%',ha='center',va='center',fontsize=11,color='black')
ax.grid(False)
ax.set_title('Different paths to bank rallies—and a bank selloff\nSelected calendar windows; unequal lengths; adjusted returns, not causal attribution',loc='left',fontsize=14,weight='bold')
fig.colorbar(im,ax=ax,label='Window return (%)',shrink=.8)
fig.savefig(P/'historical_comparisons.png',dpi=160);plt.close(fig)
print('PERFORMANCE\n',summary.round(2).to_string())
print('\nCORRELATIONS\n',corr.round(3).to_string())
print('\nEPISODES\n',ep[cols].round(2).to_string())
print('\nMODELS\n',json.dumps(models,indent=2))
print('\nANALOGS\n',pd.DataFrame(analog).round(3).to_string(index=False))
print('\nINTRADAY\n',intraday.round(3).to_string())
