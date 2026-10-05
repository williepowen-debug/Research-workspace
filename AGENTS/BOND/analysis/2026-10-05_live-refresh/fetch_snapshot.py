from pathlib import Path
import sys, json, csv, io, datetime as dt, urllib.request, concurrent.futures
from zoneinfo import ZoneInfo
BASE=Path('/home/willi/Research-workspace/AGENTS/BOND')
OUT=BASE/'analysis/2026-10-05_live-refresh/raw'
OUT.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(BASE/'monitors'))
sys.path.insert(0,str(BASE.parents[1]/'FORGE/tools/market-data'))
import fetch, fr2004_fetch as fr, buyback_f2 as f2
def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,default=str)+'\n')
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 BOND research'}),timeout=40) as r:
        return r.read().decode()
def treasury(kind):
    url='https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type='+kind+'&_format=csv'
    body=get(url)
    (OUT/(kind+'.csv')).write_text(body)
    rows=list(csv.DictReader(io.StringIO(body)))
    if not rows or not any('Date' in r for r in rows): raise ValueError('not Treasury CSV')
    rows.sort(key=lambda r:dt.datetime.strptime(r['Date'],'%m/%d/%Y'))
    return {'source':url,'recent':rows[-8:]}
def credit():
    ids=['BAMLH0A0HYM2','BAMLH0A3HYC','BAMLC0A0CM','BAMLC0A4CBBB','BAMLH0A1HYBB','BAMLH0A2HYB','SOFR','IORB','EFFR']
    answer={}
    for sid in ids:
        cache=fetch._cache_path('fred_'+sid+'_10')
        if cache.exists(): cache.unlink()
        rows=fetch.fred_fetch(sid,limit=10)
        if not rows or 'error' in rows[0]: answer[sid]={'gap':'fetch failed'}
        else: answer[sid]=rows
    save('fred_latest_vintage.json',answer)
    return {k:v[:3] if isinstance(v,list) else v for k,v in answer.items()}
def dealer():
    sb=fr.current_seriesbreak(dt.date.today())
    keys=fr.BUCKETS+[('PDPOSGSC-G3L6','3-6Y'),('PDPOSGSC-G6L7','6-7Y')]
    series={label:fr.fetch(key,sb) for key,label in keys}
    save('fr2004.json',{'break':sb,'series':series})
    dates=sorted(set.intersection(*(set(v) for v in series.values())))
    return {'break':sb,'recent':[{d:{k:round(v[d],3) for k,v in series.items()}} for d in dates[-3:]]}
def buyback():
    ops,details=f2.fetch_live()
    save('buyback_operations.json',ops)
    rows=[r for r in details if r['operation_date']=='2026-10-01']
    op=[o for o in ops if o['operation_date']=='2026-10-01']
    if len(op)!=1: raise ValueError('op ambiguous')
    save('buyback_20261001_details.json',rows)
    ok,reason=f2.complete(op[0],rows)
    if not ok: raise ValueError(reason)
    vintages=f2.resolve_vintages([r['cusip_nbr'] for r in rows])
    m=f2.metrics(op[0],rows,vintages)
    save('buyback_20261001_metrics.json',m)
    return {'operation':op[0],'metrics':m}
def prices():
    symbols=['TLT','TBT']
    cache=fetch._cache_path('prices_'+'_'.join(sorted(symbols)))
    if cache.exists(): cache.unlink()
    quotes=fetch.price_fetch(symbols)
    save('quotes.json',{'captured_et':dt.datetime.now(ZoneInfo('America/New_York')).isoformat(),'vendor':'yfinance','quotes':quotes})
    return quotes
def upcoming():
    url='https://www.treasurydirect.gov/TA_WS/securities/upcoming?format=json'
    data=json.loads(get(url));save('treasurydirect_upcoming.json',data)
    return [r for r in data if r.get('securityType') in ('Note','Bond') and str(r.get('auctionDate',''))[:10]>='2026-10-05']
def tga():
    url='https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance?filter=record_date:gte:2026-09-30&sort=-record_date&page[size]=100'
    data=json.loads(get(url));save('dts_operating_cash_balance.json',data)
    return data['data']
def extra():
    import yfinance as yf, xlrd
    import rates_context as rc
    strip=yf.download(['ZQV26.CBT','ZQX26.CBT','ZQZ26.CBT','ZQF27.CBT'],period='1mo',progress=False,auto_adjust=False)['Close']
    frame={str(d.date()):{k:round(100-float(v),6) for k,v in row.items() if str(v)!='nan'} for d,row in strip.iterrows()}
    save('fed_funds_four_contracts.json',frame)
    d=get(rc.ACM_URL) if False else urllib.request.urlopen(urllib.request.Request(rc.ACM_URL,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read()
    (OUT/'ACM.xls').write_bytes(d)
    sh=xlrd.open_workbook(file_contents=d).sheet_by_name('ACM Daily')
    ci={str(x):i for i,x in enumerate(sh.row_values(0))}
    acm=[{'date':dt.datetime.strptime(sh.cell_value(i,0),'%d-%b-%Y').date().isoformat(),'ACMTP10':sh.cell_value(i,ci['ACMTP10'])} for i in range(max(1,sh.nrows-30),sh.nrows)]
    save('acm_last30.json',acm)
    kw=fetch.fred_fetch('THREEFYTP10',30);save('kw_last30.json',kw)
    first={s:fetch.fred_fetch_vintage(s,limit=5,basis='first-published',observation_start='2026-09-24') for s in ['BAMLH0A0HYM2','BAMLH0A3HYC','BAMLC0A0CM']}
    save('credit_first_published.json',first)
    daily={s:fetch.fred_fetch(s,20000) for s in ['DGS30','DFII10','T5YIFR','T10YIE']}
    save('fred_derived_histories.json',daily)
    sources={
      'auction_schedule.pdf':'https://home.treasury.gov/system/files/221/TentativeAuctionScheduleQ32026.pdf',
      'nbim_bond_letter.html':'https://www.nbim.no/en/news-and-insights/submissions-to-ministry/2026/the-government-pension-fund-global--analyses-and-assessments-of-the-investment-strategy-for-bonds/',
      'jefferson.html':'https://www.federalreserve.gov/newsevents/speech/jefferson20261001a.htm',
      'paramount_pricing.pdf':'https://ir.paramount.com/node/73371/pdf',
      'october_fed_calendar.html':'https://www.federalreserve.gov/newsevents/2026-october.htm'}
    for name,url in sources.items():
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as resp:
            (OUT/name).write_bytes(resp.read())
    return {'latest_futures':dict(list(frame.items())[-2:]),'acm':acm[-2:],'kw':kw[:1], 'first_published':{k:v['rows'][:2] for k,v in first.items()},'extra_sources':list(sources)}
jobs={'nominal':lambda:treasury('daily_treasury_yield_curve'),'real':lambda:treasury('daily_treasury_real_yield_curve'),'credit':credit,'dealer':dealer,'buyback':buyback,'prices':prices,'auctions':upcoming,'tga':tga,'extra':extra}
summary={'captured_start_et':dt.datetime.now(ZoneInfo('America/New_York')).isoformat(),'fred_basis':'latest-vintage, not first-published','results':{}}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    fs={pool.submit(fn):name for name,fn in jobs.items()}
    for future in concurrent.futures.as_completed(fs):
        name=fs[future]
        try: summary['results'][name]=future.result()
        except Exception as e: summary['results'][name]={'gap':type(e).__name__}
summary['captured_end_et']=dt.datetime.now(ZoneInfo('America/New_York')).isoformat()
save('summary.json',summary)
print(json.dumps({'captured_start_et':summary['captured_start_et'],'captured_end_et':summary['captured_end_et'],'gaps':{k:v for k,v in summary['results'].items() if isinstance(v,dict) and 'gap' in v},'extra':summary['results'].get('extra'),'prices':summary['results'].get('prices'),'buyback_metrics':summary['results'].get('buyback',{}).get('metrics')},indent=2,default=str))
