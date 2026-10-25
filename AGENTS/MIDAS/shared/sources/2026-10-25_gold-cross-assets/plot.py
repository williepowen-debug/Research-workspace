"""Cross-asset charts; temporary matplotlib only, no project installation."""
from pathlib import Path
import sys,os
sys.path.insert(0,'/tmp/midas-gold-plot-deps')
os.environ.setdefault('MPLCONFIGDIR','/tmp/midas-cross-assets-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd

P=Path(__file__).resolve().parent
d=pd.read_csv(P/'all_asset_common_panel.csv',index_col=0,parse_dates=True)
funds=pd.read_csv(P/'funds_common_panel.csv',index_col=0,parse_dates=True)
episodes=pd.read_csv(P/'gold_drawdown_cross_asset_returns.csv')
colors={'GLD':'#ad7c14','SPY':'#386b96','IEF':'#629684','TLT':'#8a6ba3','WTI':'#b34c41'}
labels={'GLD':'Gold (GLD)','SPY':'US stocks (SPY)','IEF':'7–10y Treasury (IEF)',
        'TLT':'20+y Treasury (TLT)','WTI':'WTI spot price · not investment return'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,
 'axes.spines.right':False,'axes.titleweight':'bold','figure.facecolor':'#faf9f5','axes.facecolor':'#faf9f5',
 'text.color':'#17252d','axes.labelcolor':'#17252d'})
fig=plt.figure(figsize=(13.5,11.3),layout='constrained');gs=fig.add_gridspec(3,2,height_ratios=[1.1,1,1])
ax=fig.add_subplot(gs[0,:]);q=d.loc['2026-01-29':];idx=100*q/q.iloc[0]
for t in idx:ax.plot(idx.index,idx[t],label=labels[t],color=colors[t],lw=2.6 if t=='GLD' else 1.7)
ax.axhline(100,color='#777',lw=.8,linestyle='--');ax.set_ylabel('January 29, 2026 = 100')
ax.set_title('Since gold’s January peak: stocks and oil higher, gold and Treasuries lower',loc='left',pad=12)
ax.legend(frameon=False,fontsize=9,ncol=3,loc='upper left');ax.grid(axis='y',alpha=.18)
ax.annotate('All series end Oct 20\nWTI source publication lag',xy=(idx.index[-1],idx.WTI.iloc[-1]),
 xytext=(-155,-10),textcoords='offset points',fontsize=9)
heat=fig.add_subplot(gs[1,:]);arr=episodes[['GLD','SPY','IEF','TLT','WTI']].to_numpy()
heat.imshow(arr,cmap='RdYlGn',vmin=-100,vmax=100,aspect='auto')
heat.set_xticks(range(5),['Gold','US stocks','7–10y Treasuries','20+y Treasuries','WTI spot price'])
heat.set_yticks(range(5),['2006 gold decline','2008 gold decline','2011–2015 gold decline',
 '2020–2022 gold decline','2026 · ongoing to Oct 20'])
for i in range(len(arr)):
 for j in range(5):heat.text(j,i,f'{arr[i,j]:+.1f}%',ha='center',va='center',fontsize=11,fontweight='bold',color='#17252d')
heat.set_title('Same dates across assets during each major gold decline',loc='left',pad=12)
heat.tick_params(length=0);heat.spines[['left','bottom']].set_visible(False)

for k,(asset,title) in enumerate([('SPY','Gold has become more correlated with stocks'),('WTI','Gold’s relationship with oil also changes sign')]):
 ax=fig.add_subplot(gs[2,k])
 pair=(funds[['GLD','SPY']] if asset=='SPY' else d[['GLD','WTI']]).copy()
 r=pair.pct_change(fill_method=None)
 if asset=='WTI':r=r.loc[(pair.WTI>0)&(pair.WTI.shift(1)>0)]
 r=r.dropna();rolling=r.GLD.rolling(120).corr(r[asset]);latest=rolling.dropna().iloc[-1]
 ax.plot(rolling.index,rolling,color=colors[asset],lw=1.3)
 ax.axhline(0,color='#666',lw=.7);ax.set_ylim(-.8,.85);ax.set_title(title,loc='left',fontsize=11,pad=10)
 ax.set_ylabel('120-observation return correlation');ax.grid(axis='y',alpha=.15)
 ax.text(.03,.91,f'Latest: {latest:+.2f}',transform=ax.transAxes,fontweight='bold',color=colors[asset])
fig.suptitle('Gold versus equities, Treasuries and oil',x=.01,ha='left',fontsize=20,fontweight='bold')
fig.supxlabel('Sources: GLD issuer closes with Oct 23 mirror extension; SPY/IEF/TLT dividend-adjusted Yahoo market-return proxies; EIA WTI spot.\nOil is a price change, not an investable return. Historical gold troughs are retrospective; no recovery or causal forecast is implied.',fontsize=9)
for ext in ['png','svg','pdf']:fig.savefig(P/f'gold_cross_assets.{ext}',dpi=180,bbox_inches='tight')
print('Saved PNG/SVG/PDF cross-asset charts.')
