import pandas as pd, numpy as np
S=pd.read_csv('/tmp/s6/out/prereg_state_series.csv',index_col=0,parse_dates=True)
N=63; F=S.shift(-N).add_suffix('_f'); J=pd.concat([S,F],axis=1).dropna()
def c1(r): return np.where(r.corr_f<=0.863,'persist',np.where(r.vol_f<0.20,'calm_norm','stress_norm'))
def c3(r): return np.where(r.brate_f< -0.03,'neg',np.where(r.brate_f>0.03,'pos','zero'))
J['C1']=c1(J); J['C3']=c3(J); J['C2']=np.where(J.beta_f>=0.8,'beta>=.8','beta<.8')
def eps(mask,gap=63):
    idx=J.index[mask];
    if len(idx)==0: return []
    s=pd.Series(idx); g=(s.diff()>pd.Timedelta(days=int(gap*1.5))).cumsum()
    return [(grp.iloc[0].date(),grp.iloc[-1].date(),len(grp)) for _,grp in s.groupby(g)]
sets={'all':J.index==J.index,'corr<.863':J['corr']<.863,'corr<.80':J['corr']<.80,'corr<.863 & vol<.20':(J['corr']<.863)&(J.vol<.20),
      'beta<.5':J.beta<.5,'beta<.6':J.beta<.6,'brate<-.03':J.brate<-.03,'brate<-.03 & since2012':(J.brate<-.03)&(J.index>='2012-01-01'),
      'corr<.863 & beta<.6':(J['corr']<.863)&(J.beta<.6),'vol<.20':J.vol<.20}
for nm,m in sets.items():
    s=J[m]; print(f'\n## {nm}: days={len(s)} episodes={len(eps(m))}')
    print('  C1',s.C1.value_counts(normalize=True).round(2).to_dict(),'| C2',s.C2.value_counts(normalize=True).round(2).to_dict(),'| C3',s.C3.value_counts(normalize=True).round(2).to_dict())
    # episode-level (each episode weighted equally)
    E=[]
    for a,b,n in eps(m):
        e=J.loc[str(a):str(b)][m.loc[str(a):str(b)] if hasattr(m,'loc') else slice(None)]
        E.append({'start':a,'end':b,'days':n,'corr>.863':(e.corr_f>.863).mean(),'calm_norm':(e.C1=='calm_norm').mean(),'beta>=.8':(e.beta_f>=.8).mean(),'brate_neg':(e.C3=='neg').mean()})
    if nm!='all' and nm!='vol<.20':
        E=pd.DataFrame(E); print(E.round(2).to_string(index=False)); print('  episode-weighted:',E[['corr>.863','calm_norm','beta>=.8','brate_neg']].mean().round(2).to_dict())
# persistence of vol<.20
print('\nP(vol_f<.20 | vol<.20)=%.2f ; P(vol_f<.20) all=%.2f'%((J[J.vol<.2].vol_f<.2).mean(),(J.vol_f<.2).mean()))
print('share of days since 2006 with vol<.20: %.2f'%((S.vol<.2).mean()))
print('se of 63d corr near 0.72 (Fisher): %.3f'%((1-0.72**2)/np.sqrt(60)))
