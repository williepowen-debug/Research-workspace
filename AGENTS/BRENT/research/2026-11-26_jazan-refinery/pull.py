# 11/26 night capture (Jazan REFINERY session): same method as research/2026-11-25_jazan/pull.py; vendor yfinance one-minute + daily bars.
# Adds HOG27/RBG27 and a per-minute path around the 15:19Z (10:19 ET) Arab News publication. Raw saved per symbol.
import json, sys, yfinance as yf
OUT='AGENTS/BRENT/research/2026-11-26_jazan-refinery/'
TAG=sys.argv[1] if len(sys.argv)>1 else 'f1'
syms=['BZF27.NYM','BZG27.NYM','BZH27.NYM','CLF27.NYM','CLG27.NYM','HOF27.NYM','HOG27.NYM','RBF27.NYM','BZ=F','CL=F','HO=F']
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
    print('LAST',s,rows[-1] if rows else None,'N',len(rows),'DAILY',daily[-3:])
