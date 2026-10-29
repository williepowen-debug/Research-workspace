"""WQ-545 leg 4: AMZN/AAPL implied earnings move (nearest-expiry ATM straddle / spot, yfinance chain,
intraday 10/29) vs median absolute post-earnings 1-day move over the last 8 reports, and the realized
FOMC 10/28 SPX/QQQ move. Run from repo root with .venv python -I."""
import yfinance as yf, pandas as pd, numpy as np, datetime as dt
for tk in ('AMZN','AAPL'):
    t=yf.Ticker(tk); spot=t.fast_info['lastPrice']
    exps=[e for e in t.options if e>='2026-10-30'][:2]
    for e in exps:
        ch=t.option_chain(e); c,p=ch.calls,ch.puts
        k=c.iloc[(c.strike-spot).abs().argsort()[:1]].strike.values[0]
        cm=c[c.strike==k].iloc[0]; pm=p[p.strike==k].iloc[0]
        mid=lambda r:(r.bid+r.ask)/2 if r.bid>0 and r.ask>0 else r.lastPrice
        st=mid(cm)+mid(pm)
        print(f"{tk} spot {spot:.2f} exp {e} K {k} straddle {st:.2f} = {st/spot*100:.2f}% | call IV {cm.impliedVolatility:.3f} put IV {pm.impliedVolatility:.3f} | bid/ask c {cm.bid}/{cm.ask} p {pm.bid}/{pm.ask}")
    try:
        ed=t.get_earnings_dates(limit=16)
        ed=ed[ed.index<pd.Timestamp('2026-10-29',tz=ed.index.tz)].head(8)
        h=t.history(period='3y',auto_adjust=False)['Close']; h.index=h.index.tz_localize(None).normalize()
        mv=[]
        for d in ed.index:
            d0=d.tz_localize(None); day=d0.normalize()
            pre=day if d0.hour>=16 else h.index[h.index<day][-1]   # after-close report: move = next session vs report day
            i=h.index.get_indexer([pre])[0]
            if i<0 or i+1>=len(h): continue
            mv.append((pre.date(),round((h.iloc[i+1]/h.iloc[i]-1)*100,2)))
        a=[abs(x) for _,x in mv]
        print(f"{tk} last {len(mv)} post-earnings 1-day moves: {mv}\n   median |move| {np.median(a):.2f}% mean {np.mean(a):.2f}%")
    except Exception as ex: print(tk,'earnings history unavailable:',ex)
for tk in ('^GSPC','QQQ'):
    h=yf.Ticker(tk).history(start='2026-10-26',end='2026-10-30',auto_adjust=False)['Close']
    print(tk,'closes',{str(k.date()):round(v,2) for k,v in h.items()})
