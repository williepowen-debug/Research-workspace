"""Gold conflict-window charts with separate daily and monthly bases."""
from pathlib import Path
import os,sys
sys.path.insert(0,'/tmp/midas-gold-plot-deps');os.environ.setdefault('MPLCONFIGDIR','/tmp/midas-war-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

P=Path(__file__).resolve().parent
daily=pd.read_csv(P/'daily_conflict_event_returns.csv')
paths=pd.read_csv(P/'daily_event_paths.csv')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,
 'axes.spines.right':False,'axes.titleweight':'bold','figure.facecolor':'#faf9f5','axes.facecolor':'#faf9f5',
 'text.color':'#17252d','axes.labelcolor':'#17252d'})
fig=plt.figure(figsize=(13.5,10),layout='constrained');gs=fig.add_gridspec(2,1,height_ratios=[1,1.15])
ax=fig.add_subplot(gs[0]);cols=['pre21_return_pct']+[f'session{n}_return_pct' for n in [1,5,21,63,126]]
arr=daily[cols].to_numpy();ax.imshow(arr,cmap='RdYlGn',vmin=-30,vmax=30,aspect='auto')
labels=['Georgia 2008','Crimea 2014','Ukraine invasion 2022','Hamas attacks 2023',
        'Iran attack 2024','Israel–Iran war 2025','US/Israel–Iran war 2026']
ax.set_yticks(range(7),labels)
ax.set_xticks(range(6),['Prior 21 sessions','First session','5 sessions','21 sessions','63 sessions','126 sessions'])
for i in range(len(arr)):
 for j in range(len(cols)):ax.text(j,i,f'{arr[i,j]:+.1f}%',ha='center',va='center',fontweight='bold')
ax.tick_params(length=0);ax.spines[['left','bottom']].set_visible(False)
ax.set_title('Same pre-event closing-price baseline · GLD nominal USD returns',loc='left',pad=12)
ax=fig.add_subplot(gs[1]);selected={'Full-scale Ukraine invasion':('#427293','Ukraine 2022'),
 'Hamas attacks / Israel-Hamas conflict':('#719a79','Israel–Hamas 2023'),
 'Israel-Iran war':('#8a6b9d','Israel–Iran 2025'),
 'US-Israeli strikes on Iran':('#b4473f','US/Israel–Iran 2026')}
for event,(color,label) in selected.items():
 q=paths.loc[(paths.event==event)&(paths.relative_session<=126)]
 ax.plot(q.relative_session,q.return_from_baseline_pct,label=label,color=color,lw=2.3)
ax.axvline(0,color='#777',ls='--',lw=1);ax.axhline(0,color='#777',lw=.8)
ax.set_xlabel('Trading sessions relative to last close before the event');ax.set_ylabel('Return from pre-event GLD close')
ax.yaxis.set_major_formatter(mtick.PercentFormatter());ax.grid(axis='y',alpha=.18)
ax.set_title('An initial reaction does not determine the following months',loc='left',pad=10)
ax.legend(frameon=False,ncol=2,loc='upper left')
fig.suptitle('Gold during conflict: the horizon changes the answer',x=.01,ha='left',fontsize=20,fontweight='bold')
fig.supxlabel('Source: SPDR issuer GLD closes; fixed selected event dates verified at primary chronology sources.\nPre-event column is the run-up ending at the baseline; other columns start at that baseline. Later returns include all concurrent shocks.\nSelected examples, not all wars or a causal trading backtest. Approximately 21 / 126 sessions correspond to one / six months.',fontsize=9)
for ext in ['png','svg','pdf']:fig.savefig(P/f'gold_conflict_windows.{ext}',dpi=180,bbox_inches='tight')
print('Saved conflict-window PNG, SVG and PDF.')
