# BRT-33 windows 11/23 and 11/24 [14:28,14:30) ET plus evening capture; one capture for all legs.
import json, sys, yfinance as yf
OUT='AGENTS/BRENT/research/2026-11-24_red-sea/'
TAG=sys.argv[1] if len(sys.argv)>1 else 'c1'
syms=['BZF27.NYM','BZG27.NYM','BZH27.NYM','CLF27.NYM','CLG27.NYM','CLH27.NYM','HOF27.NYM','RBF27.NYM']
rows_by={}
for s in syms:
    try:
        h=yf.Ticker(s).history(period='5d',interval='1m',prepost=True)
        rows=[dict(label=i.tz_convert('America/New_York').isoformat(),close=float(r.Close),volume=int(r.Volume)) for i,r in h.iterrows()]
    except Exception as e:
        print(s,'ERR',e); rows=[]
    json.dump(rows,open(OUT+f'raw/{TAG}_{s}.json','w'))
    rows_by[s]=rows
out={}
for D in ['2026-11-19','2026-11-20','2026-11-23','2026-11-24']:
    res={}
    for s in syms:
        b=[r for r in rows_by[s] if r['label'][:10]==D and r['label'][11:16] in('14:28','14:29')]
        p=[r for r in b if r['volume']>0]; v=sum(r['volume'] for r in p)
        res[s]=dict(vwap=round(sum(r['close']*r['volume'] for r in p)/v,4) if v>0 else None,bars=len(b),pos_bars=len(p),vol=v)
    g=lambda s:res[s]['vwap']
    d=lambda a,b:(round(g(a)-g(b),4) if g(a) is not None and g(b) is not None else None)
    res['_M1M3']=d('BZF27.NYM','BZH27.NYM'); res['_M1M2']=d('BZF27.NYM','BZG27.NYM'); res['_WTI_M1M3']=d('CLF27.NYM','CLH27.NYM')
    if all(g(s) is not None for s in('HOF27.NYM','CLF27.NYM')): res['_HO_CL_Jan']=round(g('HOF27.NYM')*42-g('CLF27.NYM'),4)
    if all(g(s) is not None for s in('RBF27.NYM','HOF27.NYM','CLF27.NYM')): res['_321_Jan_vsCL']=round((2*g('RBF27.NYM')+g('HOF27.NYM'))*42/3-g('CLF27.NYM'),4)
    out[D]=res
    print(D,'M1-M3',res['_M1M3'],'M1-M2',res['_M1M2'],'WTI M1-M3',res['_WTI_M1M3'],'HO-CL',res.get('_HO_CL_Jan'),'321',res.get('_321_Jan_vsCL'),{s:(res[s]['vwap'],res[s]['pos_bars'],res[s]['vol']) for s in syms})
for s in syms:
    print('LAST',s,rows_by[s][-1] if rows_by[s] else None)
json.dump(out,open(OUT+f'window_{TAG}.json','w'),indent=1)
