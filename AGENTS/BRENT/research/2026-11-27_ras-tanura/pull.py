# 11/27 evening capture for the Ras Tanura / SOMO conditional read (session brent-desk-2026-11-27b).
# Same vendor method as research/2026-11-27_brt33/pull.py: yfinance one-minute (5d) + daily (15d) bars, raw saved per symbol.
import json, sys, yfinance as yf
OUT='AGENTS/BRENT/research/2026-11-27_ras-tanura/'
TAG=sys.argv[1] if len(sys.argv)>1 else 'h1'
syms=['BZF27.NYM','BZG27.NYM','BZH27.NYM','BZJ27.NYM','CLF27.NYM','CLG27.NYM','CLH27.NYM','HOF27.NYM','HOG27.NYM','RBF27.NYM','BZ=F','CL=F','USO']
for s in syms:
    try:
        t=yf.Ticker(s)
        h=t.history(period='5d',interval='1m',prepost=True)
        rows=[dict(label=i.tz_convert('America/New_York').isoformat(),close=float(r.Close),volume=int(r.Volume)) for i,r in h.iterrows()]
        d=t.history(period='15d',interval='1d')
        daily=[dict(date=str(i.date()),close=float(r.Close),volume=int(r.Volume)) for i,r in d.iterrows()]
    except Exception as e:
        print(s,'ERR',e); rows=[]; daily=[]
    json.dump(dict(m1=rows,daily=daily),open(OUT+f'raw/{TAG}_{s}.json','w'))
    lastv=[r for r in rows if r['volume']>0]
    print('LAST',s,lastv[-1] if lastv else None,'DAILY',[(x['date'],round(x['close'],2)) for x in daily[-6:]])
