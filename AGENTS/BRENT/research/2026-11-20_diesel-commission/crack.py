# Vendor daily bars for the December and January ULSD cracks (HO x 42 - CL). [EST vendor daily, not settlements]
import json, yfinance as yf, statistics as st, sys
OUT='AGENTS/BRENT/research/2026-11-20_diesel-commission/'
legs={'Dec':('HOZ26.NYM','CLZ26.NYM'),'Jan':('HOF27.NYM','CLF27.NYM')}
raw={}
for k,(ho,cl) in legs.items():
    for s in (ho,cl):
        h=yf.Ticker(s).history(period='3mo',interval='1d',auto_adjust=False)
        raw[s]={i.strftime('%Y-%m-%d'):[float(r.Close),int(r.Volume)] for i,r in h.iterrows()}
json.dump(raw,open(OUT+'daily-vendor.json','w'))
for k,(ho,cl) in legs.items():
    d=sorted(set(raw[ho])&set(raw[cl]))
    c=[(x,round(raw[ho][x][0]*42-raw[cl][x][0],4)) for x in d]
    print(k,'crack, last 25 rows (date, crack, HO vol, CL vol):')
    for x,v in c[-25:]: print(' ',x,v,raw[ho][x][1],raw[cl][x][1])
    ch=[c[i][1]-c[i-1][1] for i in range(1,len(c))]
    for n in (20,40):
        print(k,f'sd daily change last {n}:',round(st.pstdev(ch[-n:]),3),'mean',round(st.mean(ch[-n:]),3))
    lo=min(c,key=lambda t:t[1]); hi=max(c,key=lambda t:t[1])
    print(k,'min',lo,'max',hi)
