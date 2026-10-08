import json
from datetime import datetime, timezone
import yfinance as yf
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)) or ".")
res={'retrieved_utc':datetime.now(timezone.utc).isoformat()}
for sym in ['HOX26.NYM','CLX26.NYM','HOZ26.NYM','CLZ26.NYM']:
    try:
        t=yf.Ticker(sym)
        fr=t.history(period='5d',interval='1m',auto_adjust=False)
        fr.to_csv(f'{sym}_1m.csv')
        fr=fr.tz_convert('America/New_York')
        d=fr[fr.index.date==datetime(2026,10,8).date()]
        w=d.between_time('14:28','14:30')
        v=w.Volume.sum()
        r={'n_day_bars':len(d),'bars':[(i.strftime('%H:%M'),float(x.High),float(x.Low),float(x.Close),int(x.Volume)) for i,x in w.iterrows()],
           'vol':int(v),
           'typ_vwap':float((((w.High+w.Low+w.Close)/3)*w.Volume).sum()/v) if v else None,
           'close_vwap':float((w.Close*w.Volume).sum()/v) if v else None,
           'last_bar':str(d.index[-1]) if len(d) else None}
        dd=t.history(period='10d',interval='1d',auto_adjust=False)
        dd.to_csv(f'{sym}_1d.csv')
        r['daily_tail']=[(str(i.date()),float(x.Open),float(x.High),float(x.Low),float(x.Close),int(x.Volume)) for i,x in dd.tail(3).iterrows()]
        res[sym]=r
    except Exception as e:
        res[sym]={'error':repr(e)}
json.dump(res,open('evidence.json','w'),indent=1,default=str)
print(json.dumps(res,indent=1,default=str))
