import pandas as pd, numpy as np, io, subprocess, sys
import yfinance as yf
arch=pd.read_csv(sys.argv[1],comment="#"); arch.columns=['date','hy']; arch['date']=pd.to_datetime(arch['date']); arch['hy']=pd.to_numeric(arch['hy'],errors='coerce')
live=pd.read_csv(io.StringIO(subprocess.run(['curl','-s','--max-time','40','https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2'],capture_output=True,text=True).stdout)); live.columns=['date','hy']; live['date']=pd.to_datetime(live['date']); live['hy']=pd.to_numeric(live['hy'],errors='coerce')
m=arch.merge(live,on='date',suffixes=('_a','_l')).dropna()
print('overlap',len(m),'maxdiff',(m.hy_a-m.hy_l).abs().max())
hy=pd.concat([arch[arch.date<live.date.min()],live]).dropna().set_index('date')['hy']*100
spx=yf.download('^GSPC',start='1996-06-01',end='2026-11-26',auto_adjust=False,progress=False)['Close'].squeeze()
df=pd.concat([hy.rename('hy'),spx.rename('spx')],axis=1).dropna()
over=(df.hy>350).astype(int)
run3=over.rolling(3).sum()==3
LB=int(sys.argv[2])
ev=[]
for i in range(len(df)):
    if run3.iloc[i] and (run3.iloc[i-LB:i].sum()==0) and i-LB>=0:
        ev.append(i)
rows=[]
for i in ev:
    d=df.index[i]; s0=df.spx.iloc[i]; h0=df.hy.iloc[i]
    pk=df.spx.iloc[max(0,i-120):i+1].max()
    r={'fire':d.date(),'hy':round(h0),'hy_min60':round(df.hy.iloc[i-60:i].min()),'spx_off_120d_high%':round((s0/pk-1)*100,1),'spx_5d_before%':round((s0/df.spx.iloc[i-5]-1)*100,1)}
    for k in (10,20,40,60):
        r[f'+{k}%']=round((df.spx.iloc[i+k]/s0-1)*100,1) if i+k<len(df) else None
    w=df.spx.iloc[i:i+41]; r['min40%']=round((w.min()/s0-1)*100,1) if i+40<len(df) else None
    hw=df.hy.iloc[i:i+61]; r['hy_peak60']=round(hw.max()) if i+60<len(df) else None
    r['hy_d1']=round(h0-df.hy.iloc[i-1]); r['hy_pk_before']=round(df.hy.iloc[i-5:i+1].max()); r['hy+5']=round(df.hy.iloc[i+5]-h0) if i+5<len(df) else None; r['hy+10']=round(df.hy.iloc[i+10]-h0) if i+10<len(df) else None
    r['hy+20']=round(df.hy.iloc[i+20]-h0) if i+20<len(df) else None
    rows.append(r)
out=pd.DataFrame(rows); pd.set_option('display.width',250); print(out.to_string(index=False))
c=out.dropna()
for k in ('+10%','+20%','+40%','+60%','min40%'):
    print(k,'median',c[k].median(),'neg share',round((c[k]<0).mean(),2),'n',len(c))
