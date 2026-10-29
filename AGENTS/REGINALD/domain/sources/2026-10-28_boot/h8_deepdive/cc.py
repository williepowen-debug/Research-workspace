import sys
sys.path.insert(0,'/home/willi/Research-workspace/FORGE/tools/market-data')
import fetch
for sid in ['CCLSCBW027SBOG','CCLSCBW027NBOG','CCLLCBW027SBOG']:
    r=sorted((x['date'],float(x['value'])) for x in fetch.fred_fetch(sid,limit=12) if 'date' in x)
    print(sid, ' '.join(f"{a[5:]}:{v:.1f}" for a,v in r))
