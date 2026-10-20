from pathlib import Path
import sys,json,datetime,importlib.util
import yfinance as yf,pandas as pd
R=Path(__file__).resolve().parents[4];D=R/'AGENTS/VULCAN';out=D/'reports/2026-10-20_catchup'
spec=importlib.util.spec_from_file_location('vulcan_mag7',D/'tools/mag7.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
# Falsify benchmark selection with opposing return paths, then a missing-benchmark refusal.
orig=yf.download
idx=pd.bdate_range(end='2026-10-19',periods=80)
p0=pd.DataFrame({'NVDA':[100*(0.999**n) for n in range(80)],'QQQ':[100*(0.999**n) for n in range(80)],'SPY':[100*(1.001**n) for n in range(80)]},index=idx)
yf.download=lambda *a,**kw:{'Close':p0}
a,_=m.layer_contributions({'NVDA':(100,100)},'19-Oct-2026',benchmark='QQQ');b,_=m.layer_contributions({'NVDA':(100,100)},'19-Oct-2026')
assert all(float(x['index_ret_pp'])<0 and abs(float(x['recon_err_pp']))<0.0002 for x in a)
assert all(float(x['index_ret_pp'])>0 for x in b)
yf.download=lambda *a,**kw:{'Close':p0.drop(columns='QQQ')}
assert m.layer_contributions({'NVDA':(100,100)},'19-Oct-2026',benchmark='QQQ')==([], 'ERR:no-price-frame')
yf.download=orig
j=json.loads((out/'sources/qqq-holdings-response.json').read_text());hs=j['holdings'];assert len(hs)==j['totalNumberOfHoldings'];assert abs(sum(float(x['percentageOfTotalNetAssets'] or 0) for x in hs)-100)<0.00001
h={x['ticker']:(float(x['percentageOfTotalNetAssets']),float(x['units'])) for x in hs if x['securityTypeCode'] in ['COM','DRNY','ADR']}
assert len(h)==len([x for x in hs if x['securityTypeCode'] in ['COM','DRNY','ADR']])
def capture(*a,**kw):
 
 if '--offline' in sys.argv:
  px=pd.read_csv(out/'sources/qqq-adjusted-closes.csv',index_col=0,parse_dates=True);return {'Close':px}
 f=orig(*a,**kw);f['Close'].to_csv(out/'sources/qqq-adjusted-closes.csv');return f
yf.download=capture
rows,note=m.layer_contributions(h,datetime.date.fromisoformat(j['effectiveDate']).strftime('%d-%b-%Y'),benchmark='QQQ')
yf.download=orig
assert len(rows)==4,(rows,note)
res={'asof':j['effectiveDate'],'issuer_api':'https://dng-api.invesco.com/cache/v1/accounts/en_US/shareclasses/46090E103/holdings/fund?idType=cusip&productType=ETF','holding_rows':len(hs),'equity_rows':len(h),'CRWV_weight_pct':h['CRWV'][0],'rows':rows,'note':note,'guards':'3 passed: QQQ selects negative benchmark; SPY default selects positive; missing QQQ refuses','basis':'One-time QQQ variant, current-share/current-membership daily reconstruction, equity-only normalized weights; cash/future/collateral rows excluded. Tiers reused unchanged. Report pp first, ratio only above existing 1pp floor. SPY floor base-rate does NOT transfer to QQQ; no new threshold or cadence.'}
(out/'qqq-contribution.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
