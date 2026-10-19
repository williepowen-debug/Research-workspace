"""Descriptive sector-matched quality membership screen, NOT a refinancing test."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import csv, json, subprocess, hashlib, statistics, io, re, sys
import openpyxl

D = Path(__file__).resolve().parent
OLD = D.parent/'2026-10-19_breadth'

def get(item):
    name, url = item
    p = subprocess.run(['curl','-sS','-L','--max-time','15',url],capture_output=True)
    (D/'raw'/name).write_bytes(p.stdout)
    return {'name':name,'url':url,'rc':p.returncode,'bytes':len(p.stdout),
            'sha256':hashlib.sha256(p.stdout).hexdigest(),'retrieved':datetime.now(timezone.utc).isoformat()}

syms = ['XLK','XLC','XLY','XLF','XLV','XLI','XLP','XLE','XLU','XLRE','XLB']
items = [(s+'.xlsx','https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-'+s.lower()+'.xlsx') for s in syms]
items += [('QUAL.csv','https://www.ishares.com/us/products/256101/ishares-msci-usa-quality-factor-etf/latest-holdings.csv')]
if '--reuse' not in sys.argv:
    with ThreadPoolExecutor(max_workers=4) as pool:
        receipt=list(pool.map(get,items))
    (D/'quality-source-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
sector = {};asofs={};conflicts=[]
for s in syms:
    rows=list(openpyxl.load_workbook(D/'raw'/(s+'.xlsx'),read_only=True,data_only=True).active.values)
    asofs[s]=str(rows[2][1])
    assert '16-Oct-2026' in asofs[s], (s,asofs[s])
    header=next(i for i,r in enumerate(rows) if r[0]=='Name' and r[1]=='Ticker')
    for r in rows[header+1:]:
        if isinstance(r[1],str) and isinstance(r[4],(int,float)) and re.fullmatch(r'[A-Z]{1,5}(?:[.][A-Z])?',r[1]):
            sym=r[1].replace('.','-')
            if sym in sector and sector[sym]!=s:
                conflicts.append(sym)
            sector[sym]=s
text=(D/'raw'/'QUAL.csv').read_text(encoding='utf-8-sig')
assert 'Oct 16, 2026' in text[:500]
lines=text.splitlines();head=next(i for i,x in enumerate(lines) if x.startswith('Ticker,'))
quality={r['Ticker'].replace('.','-') for r in csv.DictReader(lines[head:]) if r.get('Asset Class')=='Equity'}
snap=json.loads((OLD/'constituent-snapshot.json').read_text())
analysis=json.loads((D/'analysis.json').read_text())
results=[];stocks=[]
for w in analysis['recent']:
    n=w['sessions']
    if n not in [5,20,60]:continue
    start,end=w['start'],w['end'];groups={}
    for sym,x in snap.items():
        p=x['bars']
        if sym not in sector or start not in p or end not in p:continue
        ret=100*(p[end]/p[start]-1)
        sec=sector[sym];flag=sym in quality
        groups.setdefault(sec,{True:[],False:[]})[flag].append(ret)
        stocks.append({'sessions':n,'symbol':sym,'sector':sec,'qual_member':flag,'raw_price_return_pct':ret})
    rows=[]
    for sec,g in sorted(groups.items()):
        if not g[True] or not g[False]:continue
        rows.append({'sector':sec,'qual_n':len(g[True]),'other_n':len(g[False]),
                     'qual_mean_pct':statistics.mean(g[True]),'other_mean_pct':statistics.mean(g[False]),
                     'qual_median_pct':statistics.median(g[True]),'other_median_pct':statistics.median(g[False]),
                     'qual_minus_other_mean_pp':statistics.mean(g[True])-statistics.mean(g[False])})
    nonfinancial=[r for r in rows if r['sector'] not in ['XLF','XLRE']]
    results.append({'sessions':n,'start':start,'end':end,'sectors':rows,
                    'equal_sector_mean_gap_pp':statistics.mean(r['qual_minus_other_mean_pp'] for r in rows),
                    'nonfinancial_nonREIT_sector_mean_gap_pp':statistics.mean(r['qual_minus_other_mean_pp'] for r in nonfinancial),
                    'nonfinancial_positive_sectors':sum(r['qual_minus_other_mean_pp']>0 for r in nonfinancial),
                    'nonfinancial_sector_count':len(nonfinancial)})
out={'asof':datetime.now(timezone.utc).isoformat(),'sector_asofs':asofs,'sector_conflicts':conflicts,
     'qual_equity_lines':len(quality),'sp500_qual_intersection':len(set(snap)&quality),
     'sp500_sector_coverage':len(set(snap)&set(sector)), 'results':results,
     'limits':['Current QUAL membership applied retrospectively; no point-in-time historical quality classification.',
               'QUAL selects profitability and earnings stability as well as low debt; absence is not high debt.',
               'Sectors matched, not industries/size/valuation/earnings events; no causal or refinancing attribution.',
               'Raw stock price returns exclude distributions and may contain corporate-action artifacts.',
               'This is a descriptive screening comparison only; full maturity/funding test remains separate.']}
assert not conflicts
(D/'quality-screen.json').write_text(json.dumps(out,indent=2)+'\n')
with (D/'quality-screen-stocks.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(stocks[0]));w.writeheader();w.writerows(stocks)
print(json.dumps(out,indent=2))
