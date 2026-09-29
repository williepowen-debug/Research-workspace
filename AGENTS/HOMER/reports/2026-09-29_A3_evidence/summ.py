import pandas as pd
z=pd.read_csv('zori_neg_series.csv').round(4); a=pd.read_csv('al_top100city_neg_series.csv').round(4)
reg=[('pre-2020 normal','2016-01','2020-02'),('COVID dip','2020-03','2021-06'),('boom','2021-07','2022-12'),('2023-26 soft patch','2023-01','2026-12'),('ALL','2000-01','2099-12')]
def s(df,col,lab):
    out=[]
    for n,lo,hi in reg:
        x=df[(df.month>=lo)&(df.month<=hi)]
        if len(x)==0: continue
        i=x[col].idxmax(); j=x[col].idxmin()
        out.append(f"| {lab} | {n} | {x.month.min()}..{x.month.max()} | {len(x)} | {x[col].min():.1f} ({df.month[j]}) | {x[col].median():.1f} | {x[col].mean():.1f} | {x[col].max():.1f} ({df.month[i]}) |")
    print('\n'.join(out))
s(z,'pct_top','Zillow top-100 (b)'); s(z,'pct_all','Zillow all (a)'); s(a,'pct','AptList top-100 cities')
print('Zillow (a) n range', z.n_all.min(), z.n_all.max())
def rung(df,col,levels,lab):
    last=df.tail(13)
    print(lab,'window',last.month.iloc[0],'..',last.month.iloc[-1],'values',last[col].round(1).tolist())
    for L in levels:
        k=(last[col]>L).sum(); print(f'  >{L}: crossed {k}/13', 'PINNED' if k==13 else ('never crossed' if k==0 else 'discriminates'),
              '| full-history months crossed:',(df[col]>L).sum(),'/',len(df))
rung(z,'pct_top',[4.1,10.1,15.0],'Zillow(b)')

rung(a,'pct',[20,40,55],'AptList old bands')
# lag: turning points
