import json, pandas as pd, numpy as np
d=json.load(open('h8_fred.json'))
def s(k): r=d[k]['rows']; x=pd.Series([v for _,v in r],index=pd.to_datetime([a for a,_ in r])); return x
b=s('bor_sm')/1000; bn=s('bor_sm_nsa')/1000; bl=s('bor_lg')/1000
dep,cash,ta,loans,ltd=s('dep_sm'),s('cash_sm'),s('ta_sm'),s('loans_sm'),s('ltd_sm'); pc=s('pc_wed')/1000
df=pd.DataFrame({'b':b,'bn':bn,'bl':bl,'dep':dep,'cash':cash,'ta':ta,'loans':loans,'ltd':ltd}).dropna(subset=['b'])
df['ratio']=df.b/df.ta*100
last=df.index[-1]; print('LAST',last.date())
print('\n== A. LEVEL: borrowings $B and % of small-bank assets')
for dt in ['2019-12-25','2022-03-02','2023-03-08','2023-03-15','2023-05-03','2024-03-06','2024-12-25','2025-06-25','2025-12-31']:
    i=df.index.get_indexer([pd.Timestamp(dt)],method='nearest')[0]; r=df.iloc[i]; print(f"  {df.index[i].date()}  bor {r.b:7.1f}  ratio {r.ratio:5.2f}%")
r=df.iloc[-1]; print(f"  {last.date()}  bor {r.b:7.1f}  ratio {r.ratio:5.2f}%")
for since in ['1985','2010']:
    x=df.loc[since:,'ratio']; print(f"  ratio pctile since {since}: {(x<x.iloc[-1]).mean()*100:.0f}th; max {x.max():.2f}% ({x.idxmax().date()}); median {x.median():.2f}%")
y26=df.loc['2026']; t=y26.b.idxmin(); print(f"  2026 trough {t.date()} {y26.b.min():.1f}; 2025 peak-to-2026-trough: 2024 peak {df.loc['2024'].b.max():.1f} ({df.loc['2024'].b.idxmax().date()})")
print('\n== B. RECENT PATH (SA $B)')
for dt,row in df.loc['2026-07-29':].iterrows(): print(f"  {dt.date()} bor {row.b:6.1f}  nsa {row.bn:6.1f}  dep {row.dep:7.1f}  cash {row.cash:6.1f}  loans {row.loans:7.1f}  large-bank bor {row.bl:7.1f}")
print('\n== C. SIZE OF THE RUN vs HISTORY (pct change, SA)')
for w in [1,3,6,13]:
    ch=df.b.pct_change(w)*100; cur=ch.iloc[-1]
    for since in ['1985','2010']:
        x=ch.loc[since:].dropna(); xs=x.drop(x.loc['2023-03-08':'2023-04-05'].index,errors='ignore')
        print(f"  {w:2d}w: now {cur:+5.1f}%  since {since}: pctile {(x<cur).mean()*100:5.1f}  rank {int((x>cur).sum())+1}/{len(x)}  | ex-SVB-weeks rank {int((xs>cur).sum())+1}")
    ch_d=df.b.diff(w); print(f"       $ change now {ch_d.iloc[-1]:+.1f}B")
# since trough
t0=df.loc['2026-07-01':].b.idxmin(); print('\n== D. WHAT FUNDED WHAT, trough',t0.date(),'->',last.date())
a,z=df.loc[t0],df.iloc[-1]
for k in ['b','dep','ltd','cash','loans','ta','bl']: print(f"  {k:6s} {a[k]:9.1f} -> {z[k]:9.1f}  d {z[k]-a[k]:+7.1f}  ({(z[k]/a[k]-1)*100:+5.1f}%)")
print('\n== F. DISCOUNT WINDOW primary credit Wed level $B')
print('  last', pc.index[-1].date(), round(pc.iloc[-1],3))
for since,ex in [('2010',None),('2010','ex')]:
    x=pc.loc[since:]
    if ex: x=x.drop(x.loc['2020-03-11':'2020-12-31'].index).drop(x.loc['2023-03-08':'2023-12-31'].index)
    print(f"  pctile since {since} {'ex-COVID/ex-2023' if ex else ''}: {(x<pc.iloc[-1]).mean()*100:.1f}th; max {x.max():.1f} ({x.idxmax().date()})")
print('  recent:', [(i.date().isoformat(),round(v,2)) for i,v in pc.loc['2026-09-01':].items()])
json.dump({'last':str(last.date())},open('meta.json','w'))
df.to_pickle('df.pkl'); pc.to_pickle('pc.pkl')
