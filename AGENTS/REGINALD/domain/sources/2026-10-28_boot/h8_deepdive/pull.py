import sys, json, datetime
sys.path.insert(0,'/home/willi/Research-workspace/FORGE/tools/market-data')
import fetch
S={'bor_sm':'H8B3094NSMA','bor_sm_nsa':'H8B3094NSMD','bor_lg':'H8B3094NLGA','dep_sm':'DPSSCBW027SBOG','cash_sm':'CASSCBW027SBOG','ta_sm':'TLASCBW027SBOG','loans_sm':'LLBSCBW027SBOG','ltd_sm':'LTDSCBW027SBOG','pc_wed':'WLCFLPCL'}
out={}
for k,sid in S.items():
    r=fetch.fred_fetch(sid, limit=100000)
    if r and 'error' in r[0]: print(k,sid,'ERROR',r[0]['error']); continue
    rows=sorted((x['date'],float(x['value'])) for x in r)
    out[k]={'id':sid,'rows':rows}
    print(k,sid,len(rows),rows[0],rows[-1])
out['_retrieved']=datetime.datetime.now().astimezone().isoformat()
json.dump(out,open('h8_fred.json','w'))
import yfinance as yf
k=yf.download('KRE',start='2006-06-01',progress=False,auto_adjust=True)
c=k['Close']; c=c.iloc[:,0] if hasattr(c,'columns') else c
c=c.dropna(); c=c[c.index.date<datetime.date(2026,10,28)]
json.dump({'rows':[(d.strftime('%Y-%m-%d'),float(v)) for d,v in c.items()],'basis':'yfinance auto_adjust total-return-ish closes, today excluded'},open('kre.json','w'))
print('KRE',len(c),c.index[0].date(),c.index[-1].date())
