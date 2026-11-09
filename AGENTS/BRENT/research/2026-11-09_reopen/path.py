# Reopen path read: BZF27 / BZH27 / CLZ26 1-minute bars from the Sunday 18:00 ET open to now.
import json, sys, yfinance as yf
OUT='AGENTS/BRENT/research/2026-11-09_reopen/'
TAG=sys.argv[1] if len(sys.argv)>1 else 'p1'
for s in ['BZF27.NYM','BZH27.NYM','CLZ26.NYM']:
    h=yf.Ticker(s).history(period='5d',interval='1m',prepost=True)
    rows=[dict(t=i.tz_convert('America/New_York').isoformat(),c=float(r.Close),h=float(r.High),l=float(r.Low),v=int(r.Volume)) for i,r in h.iterrows()]
    json.dump(rows,open(OUT+f'raw/{TAG}_{s}.json','w'))
    ses=[r for r in rows if r['t']>='2026-11-08T18:00']
    if not ses: print(s,'no bars since Sunday open'); continue
    def seg(a,b):
        x=[r for r in ses if a<=r['t'][:16]<b]
        return (min(r['l'] for r in x),max(r['h'] for r in x),x[0]['c'],x[-1]['c'],sum(r['v'] for r in x),len(x)) if x else None
    print(s,'first',ses[0]['t'],ses[0]['c'],'| last',ses[-1]['t'],ses[-1]['c'])
    print('  session hi/lo',max(r['h'] for r in ses),min(r['l'] for r in ses))
    print('  Sun eve 18:00-24:00 lo,hi,open,close,vol,bars',seg('2026-11-08T18:00','2026-11-09T00:00'))
    print('  Asia 00:00-03:00',seg('2026-11-09T00:00','2026-11-09T03:00'))
    print('  London morning 03:00-08:00',seg('2026-11-09T03:00','2026-11-09T08:00'))
    print('  US 08:00-now',seg('2026-11-09T08:00','2026-11-09T23:59'))
