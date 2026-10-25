"""Standalone charts; matplotlib installed only in /tmp for this analysis."""
from pathlib import Path
import sys,os,json
sys.path.insert(0,'/tmp/midas-gold-plot-deps')
os.environ.setdefault('MPLCONFIGDIR','/tmp/midas-gold-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

HERE=Path(__file__).resolve().parent
d=pd.read_csv(HERE/'drawdown_series.csv',index_col=0,parse_dates=True)
e=pd.read_csv(HERE/'major_drawdowns.csv')
s=json.loads((HERE/'summary.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,
                    'axes.spines.right':False,'axes.titleweight':'bold','figure.facecolor':'#faf9f5',
                    'axes.facecolor':'#faf9f5','text.color':'#17252d','axes.labelcolor':'#17252d'})
fig=plt.figure(figsize=(13,9.2),layout='constrained')
gs=fig.add_gridspec(2,2,height_ratios=[1.1,1])
ax=fig.add_subplot(gs[0,:]);ax.plot(d.index,d.close,color='#9d7517',lw=2)
ax.set_yscale('log');ax.set_ylim(35,650);ax.set_yticks([50,100,200,400]);ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
ax.yaxis.set_minor_formatter(mtick.NullFormatter())
ax.set_title('Gold’s long rise and current retreat',loc='left',fontsize=15,pad=12)
ax.set_ylabel('GLD dollars/share · logarithmic scale');ax.grid(axis='y',alpha=.18)
ax.scatter(pd.Timestamp(s['peak']),s['peak_price'],color='#b94a43',s=32,zorder=4)
ax.annotate('Jan 29 peak $495.90',xy=(pd.Timestamp(s['peak']),s['peak_price']),
            xytext=(-155,18),textcoords='offset points',arrowprops={'arrowstyle':'-','color':'#777'})
ax.scatter(d.index[-1],d.close.iloc[-1],color='#17252d',s=35,zorder=4)
ax.annotate('Oct 23 $366.61\n26.1% below peak',xy=(d.index[-1],d.close.iloc[-1]),
            xytext=(-135,-48),textcoords='offset points',arrowprops={'arrowstyle':'-','color':'#777'},fontweight='bold')
ax2=fig.add_subplot(gs[1,0]);ax2.fill_between(d.index,d.drawdown_pct,0,color='#c3aa6a',alpha=.65)
ax2.plot(d.index,d.drawdown_pct,color='#8e6a1b',lw=.8)
ax2.axhline(-20,color='#888',linestyle='--',lw=.8);ax2.set_ylim(-52,3)
ax2.yaxis.set_major_formatter(mtick.PercentFormatter());ax2.set_title('Decline from the previous record close',loc='left',pad=10)
ax2.set_ylabel('Nominal closing-price drawdown');ax2.grid(axis='y',alpha=.18)
ax2.annotate('2011–2015: −45.6%',xy=(pd.Timestamp('2015-12-17'),-45.56),
             xytext=(-75,-19),textcoords='offset points',fontsize=9)
ax3=fig.add_subplot(gs[1,1]);colors=['#9099a1','#49758c','#9a66a2','#639b8f','#bf453b']
for (_,r),color in zip(e.iterrows(),colors):
 peak=pd.Timestamp(r.peak);recovery=pd.Timestamp(r.recovery) if pd.notna(r.recovery) else d.index[-1]
 q=d.loc[peak:min(recovery,peak+pd.Timedelta(days=1000)),'close']
 days=(q.index-peak).days;val=100*(q/r.peak_price-1)
 label=f'{peak.year}'+(' · ongoing' if peak.year==2026 else '')
 ax3.plot(days,val,label=label,color=color,lw=2.8 if peak.year==2026 else 1.5)
 if peak.year==2026:ax3.scatter(days[-1],val.iloc[-1],color=color,s=30,zorder=4)
ax3.axhline(0,color='#888',lw=.7);ax3.set_ylim(-52,5);ax3.set_xlim(0,1000)
ax3.yaxis.set_major_formatter(mtick.PercentFormatter());ax3.set_xlabel('Calendar days after each record peak')
ax3.set_title('Major drawdowns · first 1,000 days',loc='left',pad=10)
ax3.legend(frameon=False,ncol=2,loc='lower left',fontsize=9);ax3.grid(axis='y',alpha=.18)
fig.suptitle('GLD history through October 23, 2026',x=.01,ha='left',fontsize=19,fontweight='bold')
fig.supxlabel('Source: SPDR issuer closes Nov 2004–Oct 22, 2026; Oct 23 Yahoo mirror. USD nominal prices, after fund expenses.\nHistorical paths are retrospective; the ongoing 2026 trough and recovery are unknown.',fontsize=9)
for ext in ['png','svg','pdf']:fig.savefig(HERE/f'gold_historical_comparison.{ext}',dpi=180,bbox_inches='tight')
print('Saved PNG, SVG and PDF historical comparison charts.')
