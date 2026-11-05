import sys, json, subprocess, itertools, datetime as dt
import yfinance as yf
fee=1.30
def screen(tk, exp, kind, wmin, wmax, n=8, cap=4.90, band=(0.90,1.08)):
    t=yf.Ticker(tk); 
    spot=t.fast_info['last_price']
    ch=t.option_chain(exp); df=(ch.calls if kind=='C' else ch.puts)
    df=df[(df.bid>0)&(df.ask>0)&(df.ask>=df.bid)]
    df=df[(df.strike>=spot*band[0])&(df.strike<=spot*band[1])]
    rows=[]
    recs=df.to_dict('records')
    for a,b in itertools.permutations(recs,2):
        if kind=='C' and not a['strike']<b['strike']: continue
        if kind=='P' and not a['strike']>b['strike']: continue
        w=abs(a['strike']-b['strike'])
        if w<wmin or w>wmax: continue
        outer=a['ask']-b['bid']; mid=(a['bid']+a['ask'])/2-(b['bid']+b['ask'])/2
        if outer<=0 or outer>cap: continue
        be=a['strike']+outer if kind=='C' else a['strike']-outer
        rows.append(dict(long=a['strike'],short=b['strike'],lba=f"{a['bid']:.2f}/{a['ask']:.2f}",sba=f"{b['bid']:.2f}/{b['ask']:.2f}",outer=round(outer,2),mid=round(mid,2),pct_w=round(outer/w*100,1),be=round(be,2),be_pct=round((be/spot-1)*100,2),rr=round((w-outer)/outer,2),oiL=int(a.get('openInterest') or 0),oiS=int(b.get('openInterest') or 0),ivL=round(a['impliedVolatility']*100,1),ivS=round(b['impliedVolatility']*100,1)))
    rows.sort(key=lambda r:(r['pct_w']))
    print(f"\n== {tk} {exp} {kind} spot {spot:.2f}  ({len(rows)} spreads ≤{cap})")
    for r in rows[:n]: print(r)
for spec in sys.argv[1:]:
    tk,exp,kind,wmin,wmax=spec.split(':')
    screen(tk,exp,kind,float(wmin),float(wmax))
