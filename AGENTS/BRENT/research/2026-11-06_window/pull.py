import json, yfinance as yf
D='2026-11-06'
import sys
OUT='AGENTS/BRENT/research/2026-11-06_window/'
TAG=sys.argv[1] if len(sys.argv)>1 else 'c1'
syms=['BZF27.NYM','BZG27.NYM','BZH27.NYM','CLZ26.NYM','HOF27.NYM','RBF27.NYM','HOZ26.NYM','RBZ26.NYM']
res={}
for s in syms:
    try:
        h=yf.Ticker(s).history(period='5d',interval='1m',prepost=True)
        rows=[dict(label=i.tz_convert('America/New_York').isoformat(),close=float(r.Close),volume=int(r.Volume)) for i,r in h.iterrows()]
    except Exception as e:
        print(s,'ERR',e); rows=[]
    json.dump(rows,open(OUT+f'raw/{TAG}_{s}.json','w'))
    b=[r for r in rows if r['label'][:10]==D and r['label'][11:16] in('14:28','14:29')]
    p=[r for r in b if r['volume']>0]
    v=sum(r['volume'] for r in p)
    vwap=round(sum(r['close']*r['volume'] for r in p)/v,4) if v>0 else None
    res[s]=dict(vwap=vwap,bars=len(b),pos_bars=len(p),vol=v,last=rows[-1]['label'] if rows else None,last_close=rows[-1]['close'] if rows else None)
    print(s,res[s])
def diff(a,b):
    return round(res[a]['vwap']-res[b]['vwap'],4) if res[a]['vwap'] is not None and res[b]['vwap'] is not None else None
print('BRT-33 M1-M3',diff('BZF27.NYM','BZH27.NYM'))
print('M1-M2',diff('BZF27.NYM','BZG27.NYM'))
g=lambda s:res[s]['vwap']
if all(g(s) is not None for s in('RBF27.NYM','HOF27.NYM','BZF27.NYM')):
    print('Jan 3:2:1',round((2*g('RBF27.NYM')+g('HOF27.NYM'))*42/3-g('BZF27.NYM'),4))
if all(g(s) is not None for s in('HOZ26.NYM','CLZ26.NYM')):
    print('Dec crack HO-CL',round(g('HOZ26.NYM')*42-g('CLZ26.NYM'),4))
json.dump(res,open(OUT+f'window_{TAG}.json','w'),indent=1)
