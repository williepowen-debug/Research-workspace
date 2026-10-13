# October12 diagnostic band update

Reuse saved raw history throughOctober9, append later explicit-unadjusted completedETFbars. Verify all overlapping Close values; preserve original inputs. No actual score or frozen prediction changes. S is the adopted d200 upside leg; r63 is diagnostic only. C carries existing decayed1 with no new crossing. CPER is price context only, with no standalone crash/upside grid.

```python
from pathlib import Path
import json,hashlib
import pandas as pd
p=Path('sources/2026-10-12_news-sweep');raw=json.loads((p/'ETF_raw_history.json').read_text());out={}
for t in ['SLV','PPLT','PALL','CPER']:
 file=Path('sources/2026-10-12_review')/f'{t}.csv'
 df=pd.read_csv(file,index_col=0);df.index=pd.to_datetime(df.index);prior=df.loc[:'2026-10-09','Close'].dropna()
 updates=pd.Series({r['date']:r['close'] for r in raw[t]['history']},dtype=float);updates.index=pd.to_datetime(updates.index)
 common=prior.index.intersection(updates.index);err=max(abs(prior.loc[common]-updates.loc[common]))
 assert err<.0001,(t,err)
 series=pd.concat([prior,updates.loc[updates.index>prior.index[-1]]]);assert series.index.is_unique and len(series)>=252
 before=100*(prior.iloc[-1]/prior.tail(200).mean()-1);d200=100*(series.iloc[-1]/series.tail(200).mean()-1);ddbefore=100*(prior.iloc[-1]/prior.tail(252).max()-1);dd=100*(series.iloc[-1]/series.tail(252).max()-1)
 r63=100*(series.iloc[-1]/series.iloc[-64]-1)
 thresholds={'SLV':[-5,-12,-20],'PPLT':[-10,-15,-20],'PALL':[-12,-20,-25]}.get(t,[-5,-12,-20]);level=1
 for i,threshold in enumerate(thresholds,2):
  if d200<=threshold:level=i
 S=3 if d200>=40 else (2 if d200>=30 else 1)
 crossedT=[line for line in thresholds if before>line and d200<=line]
 crossedC=[line for line in [-20,-30,-40] if ddbefore>line and dd<=line]
 crossedS=[line for line in [30,40] if before<line and d200>=line]
 out[t]={'date':series.index[-1].date().isoformat(),'close':float(series.iloc[-1]),'d200':float(d200),'dd252':float(dd),'r63_diagnostic_only':float(r63),'T_level':level,'C_level':1,'C_basis':'prior approved crash decay=1; no fresh deeper crossing on10/12','S_level':S,'S_metric':'d200 upside, not r63','new_crossings_on_oct12':{'T':crossedT,'C':crossedC,'S':crossedS},'old_to_new_common_raw_close_max_error':float(err),'prior_source_sha256':hashlib.sha256(file.read_bytes()).hexdigest()}
 if t=='CPER':
  for key in ['T_level','C_level','C_basis','S_level','S_metric','new_crossings_on_oct12']:out[t].pop(key,None)
  out[t]['role']='Copper price-history context only; no standalone crash/upside grid adopted'
 series.to_csv(p/f'{t}_paired_ending_20261012.csv',header=['Close'])
(p/'bands.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
```
