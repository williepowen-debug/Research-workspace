# 11/25 evening capture (Jazan session, brent-desk-agent-2026-11-25-b): same method as research/2026-11-25_eia-gulf/pull.py; vendor yfinance one-minute + daily bars.
# the EIA reaction, and any BRT-33 window present in the capture. Raw saved per symbol.
import json, sys, yfinance as yf
OUT='AGENTS/BRENT/research/2026-11-25_jazan/'
TAG=sys.argv[1] if len(sys.argv)>1 else 'c1'
syms=['BZF27.NYM','BZG27.NYM','BZH27.NYM','CLF27.NYM','CLG27.NYM','CLH27.NYM','HOF27.NYM','RBF27.NYM','BZ=F','CL=F']
rows_by={}
for s in syms:
    try:
        t=yf.Ticker(s)
        h=t.history(period='5d',interval='1m',prepost=True)
        rows=[dict(label=i.tz_convert('America/New_York').isoformat(),close=float(r.Close),volume=int(r.Volume)) for i,r in h.iterrows()]
        d=t.history(period='10d',interval='1d')
        daily=[dict(date=str(i.date()),close=float(r.Close),volume=int(r.Volume)) for i,r in d.iterrows()]
    except Exception as e:
        print(s,'ERR',e); rows=[]; daily=[]
    json.dump(dict(m1=rows,daily=daily),open(OUT+f'raw/{TAG}_{s}.json','w'))
    rows_by[s]=rows
    last=rows[-1] if rows else None
    print('LAST',s,last,'DAILY',daily[-3:])
out={}
for D in ['2026-11-23','2026-11-24','2026-11-25']:
    res={}
    for s in syms:
        b=[r for r in rows_by[s] if r['label'][:10]==D and r['label'][11:16] in('14:28','14:29')]
        p=[r for r in b if r['volume']>0]; v=sum(r['volume'] for r in p)
        res[s]=dict(vwap=round(sum(r['close']*r['volume'] for r in p)/v,4) if v>0 else None,bars=len(b),pos_bars=len(p),vol=v)
    g=lambda s:res[s]['vwap']
    d=lambda a,b:(round(g(a)-g(b),4) if g(a) is not None and g(b) is not None else None)
    res['_M1M3']=d('BZF27.NYM','BZH27.NYM'); res['_M1M2']=d('BZF27.NYM','BZG27.NYM')
    if all(g(s) is not None for s in('HOF27.NYM','CLF27.NYM')): res['_HO_CL_Jan']=round(g('HOF27.NYM')*42-g('CLF27.NYM'),4)
    out[D]=res
    print('WINDOW',D,'M1-M3',res['_M1M3'],'M1-M2',res['_M1M2'],'HO-CL',res.get('_HO_CL_Jan'),{s:(res[s]['vwap'],res[s]['pos_bars'],res[s]['vol']) for s in syms[:3]})
json.dump(out,open(OUT+f'window_{TAG}.json','w'),indent=1)
