import json, sys, yfinance as yf
OUT='AGENTS/BRENT/research/2026-11-18_gulf-eia/'
TAG=sys.argv[1] if len(sys.argv)>1 else 'c1'
syms=['BZF27.NYM','BZG27.NYM','BZH27.NYM','CLZ26.NYM','CLF27.NYM','HOZ26.NYM','HOF27.NYM','RBZ26.NYM','RBF27.NYM','BZ=F','CL=F']
res={}
for s in syms:
    try:
        h=yf.Ticker(s).history(period='5d',interval='1m',prepost=True)
        rows=[dict(label=i.tz_convert('America/New_York').isoformat(),close=float(r.Close),volume=int(r.Volume)) for i,r in h.iterrows()]
        d=yf.Ticker(s).history(period='10d',interval='1d')
        daily=[dict(date=str(i.date()),close=float(r.Close),volume=int(r.Volume)) for i,r in d.iterrows()]
    except Exception as e:
        print(s,'ERR',e); rows=[]; daily=[]
    json.dump(dict(m1=rows,daily=daily),open(OUT+f'raw/{TAG}_{s}.json','w'))
    # 11/17 14:28-14:30 window vwap for comparability, and today's high/low/last
    def win(day):
        b=[r for r in rows if r['label'][:10]==day and r['label'][11:16] in('14:28','14:29') and r['volume']>0]
        v=sum(r['volume'] for r in b); return round(sum(r['close']*r['volume'] for r in b)/v,4) if v else None
    today=[r for r in rows if r['label'][:10]=='2026-11-18']
    res[s]=dict(win1117=win('2026-11-17'),last=today[-1] if today else None,
        hi=max((r['close'] for r in today),default=None),lo=min((r['close'] for r in today),default=None),
        vol_today=sum(r['volume'] for r in today),daily=daily[-4:])
    print(s,json.dumps(res[s]))
json.dump(res,open(OUT+f'summary_{TAG}.json','w'),indent=1)
