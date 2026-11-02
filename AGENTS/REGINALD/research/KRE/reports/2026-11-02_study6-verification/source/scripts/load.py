import json, pandas as pd, numpy as np, os
ROOT=os.environ.get('S6V_ROOT', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D=ROOT+'/data/px'
TK=['WFC','JPM','GS','MS','BAC','FITB','TFC','USB','PNC','COF','C','HBAN','MTB','BNY','NTRS','STT','CFG','RF','KEY','EWBC','PNFP','FHN','ZION','WAL']
def load(t):
    r=json.load(open(f'{D}/{t}.json'))['chart']['result'][0]
    idx=pd.to_datetime(r['timestamp'],unit='s').tz_localize('UTC').tz_convert('America/New_York').normalize().tz_localize(None)
    q=r['indicators']['quote'][0]
    df=pd.DataFrame({'close':q['close'],'adj':r['indicators']['adjclose'][0]['adjclose']},index=idx)
    df=df[~df.index.duplicated(keep='last')]
    div=pd.Series(0.0,index=df.index); spl=pd.Series(1.0,index=df.index)
    ev=r.get('events',{})
    for v in ev.get('dividends',{}).values():
        d=pd.to_datetime(v['date'],unit='s').tz_localize('UTC').tz_convert('America/New_York').normalize().tz_localize(None)
        if d in div.index: div[d]+=v['amount']
    for v in ev.get('splits',{}).values():
        d=pd.to_datetime(v['date'],unit='s').tz_localize('UTC').tz_convert('America/New_York').normalize().tz_localize(None)
        spl[d]=v['numerator']/v['denominator']
    df['div']=div; df['split']=spl
    return df[df.index<=pd.Timestamp('2026-10-30')]
def panel():
    P={t:load(t) for t in TK+['KBWB','KRE','SPY']}
    close=pd.DataFrame({t:P[t]['close'] for t in P}); div=pd.DataFrame({t:P[t]['div'] for t in P}); spl=pd.DataFrame({t:P[t]['split'] for t in P}); adj=pd.DataFrame({t:P[t]['adj'] for t in P})
    return close,div,spl,adj
