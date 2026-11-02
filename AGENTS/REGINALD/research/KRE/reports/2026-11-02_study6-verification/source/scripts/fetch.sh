#!/usr/bin/env bash
# Re-download all raw inputs into ../data (set UA to your contact per SEC fair-access policy).
set -e
cd "$(dirname "$0")/../data"; UA="${UA:-Research contact@example.com}"
# 1. KBWB N-PORT-P, period 2026-08-31 (Invesco Exchange-Traded Fund Trust II, CIK 1378872, series S000034530), filed 2026-10-30
curl -s -A "$UA" -o nport_0831.xml "https://www.sec.gov/Archives/edgar/data/1378872/000137887226001970/primary_doc.xml"
# 2. Invesco KBWB holdings (current only; effectiveBusinessDate must read 2026-10-30 to reproduce)
curl -s -A "Mozilla/5.0" -o kbwb_hold_now.json "https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/46138E628/holdings/fund?idType=cusip&productType=ETF"
# 3. KBWB summary prospectus (fees)
curl -s -A "$UA" -o kbwb_497k.htm "https://www.sec.gov/Archives/edgar/data/1378872/000119312525325636/d54028d497k.htm"
# 4. SSGA KRE NAV history
curl -s -A "Mozilla/5.0" -o kre_nav.xlsx "https://www.ssga.com/library-content/products/fund-data/etfs/us/navhist-us-en-kre.xlsx"
# 5. Yahoo daily prices + dividends (2026 window, and 2014+ for correlation history)
mkdir -p px pxlong
for t in WFC JPM GS MS BAC FITB TFC USB PNC COF C HBAN MTB BNY NTRS STT CFG RF KEY EWBC PNFP FHN ZION WAL KBWB KRE SPY; do
 curl -s -A "Mozilla/5.0" -o px/$t.json "https://query1.finance.yahoo.com/v8/finance/chart/$t?period1=1767225600&period2=1800000000&interval=1d&events=div%7Csplit&includeAdjustedClose=true"
 curl -s -A "Mozilla/5.0" -o pxlong/$t.json "https://query1.finance.yahoo.com/v8/finance/chart/$t?period1=1388534400&period2=1800000000&interval=1d&events=div%7Csplit&includeAdjustedClose=true"
done
# 6. SEC XBRL cover-page shares outstanding (dei:EntityCommonStockSharesOutstanding) -> tso.json
curl -s -A "$UA" -o tickers.json https://www.sec.gov/files/company_tickers.json
python3 - << 'PY'
import json,subprocess,time
m={v['ticker']:v['cik_str'] for v in json.load(open('tickers.json')).values()}
out={}
for t in ['WFC','JPM','GS','MS','BAC','FITB','TFC','USB','PNC','COF','C','HBAN','MTB','BNY','NTRS','STT','CFG','RF','KEY','EWBC','PNFP','FHN','ZION','WAL']:
    u=f'https://data.sec.gov/api/xbrl/companyconcept/CIK{m[t]:010d}/dei/EntityCommonStockSharesOutstanding.json'
    r=subprocess.run(['curl','-s','-A','Research contact@example.com',u],capture_output=True,text=True).stdout
    try: out[t]=[x for x in json.loads(r)['units']['shares'] if x['end']>='2026-01-01']
    except Exception: pass
    time.sleep(0.15)
json.dump(out,open('tso.json','w'))
PY
