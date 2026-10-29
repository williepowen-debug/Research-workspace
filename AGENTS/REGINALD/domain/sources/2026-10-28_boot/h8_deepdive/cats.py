import sys, urllib.parse, json
sys.path.insert(0,'/home/willi/Research-workspace/FORGE/tools/market-data')
import fetch
want=["Commercial and Industrial Loans, Small Domestically Chartered","Commercial Real Estate Loans, Small Domestically Chartered","Residential Real Estate Loans, Small Domestically Chartered","Consumer Loans, Small Domestically Chartered","Loans to Nondepository Financial Institutions, Small Domestically Chartered","Securities in Bank Credit, Small Domestically Chartered","All Other Loans and Leases, Small Domestically Chartered","Other Loans and Leases, Small Domestically Chartered"]
ids={}
for q in want:
    url="https://api.stlouisfed.org/fred/series/search?"+urllib.parse.urlencode({"search_text":q,"api_key":fetch.FRED_API_KEY,"file_type":"json","limit":10})
    for s in fetch._retry_request(url).get("seriess",[]):
        if s['frequency_short']=='W' and s['seasonal_adjustment_short']=='SA' and 'Small' in s['title'] and s['id'] not in ids.values():
            ids[s['title'][:80]]=s['id']
out={}
for t,sid in ids.items():
    r=sorted((x['date'],float(x['value'])) for x in fetch.fred_fetch(sid,limit=60) if 'date' in x)
    dd=dict(r)
    a=dd.get('2026-07-15'); b=dd.get('2026-09-02'); z=dd.get('2026-10-14')
    if a and b and z: print(f"{sid:18s} {t[:62]:62s} 7/15 {a:8.1f}  9/02 {b:8.1f}  10/14 {z:8.1f}  d6w {z-b:+6.1f}  dQ {z-a:+6.1f}")
