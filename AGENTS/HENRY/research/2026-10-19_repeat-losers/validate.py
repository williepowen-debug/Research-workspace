import json,csv,pathlib,math,hashlib,datetime,collections
from zoneinfo import ZoneInfo
P=pathlib.Path(__file__).resolve().parent
m=json.loads((P/'metrics.json').read_text());summary=json.loads((P/'summary.json').read_text());matches=json.loads((P/'stronger-matches.json').read_text());rows=list(csv.DictReader((P/'daily-audit.csv').open()));groups=collections.defaultdict(list)
for r in rows:groups[(r['symbol'],r['window'])].append(r)
assert summary['universe']==503 and summary['covered']==501 and len(summary['excluded'])==2
assert len(groups)==len(m)*3
for (symbol,n),rr in groups.items():
 w=m[symbol]['windows'][n];assert len(rr)==int(n) and len({r['date'] for r in rr})==int(n)
 stock=math.prod(1+float(r['stock_return']) for r in rr)-1;assert abs(stock*100-w['return_pct'])<1e-8
 for cond in ['index_up','sector_up','both_up']:
  f=[r for r in rr if (float(r['index_return'])>0 if cond=='index_up' else float(r['sector_return'])>0 if cond=='sector_up' else float(r['index_return'])>0 and float(r['sector_return'])>0)]
  assert len(f)==w[cond]['eligible'];assert sum(float(r['stock_return'])<0 for r in f)==w[cond]['losses']
  if f:assert abs((math.prod(1+float(r['stock_return']) for r in f)-1)*100-w[cond]['stock_conditional_pct'])<1e-8
for symbol,r in matches.items():
 c=r['control']
 if c:
  assert r['size_ratio']<=2
  for n in ['20','60']:assert m[c]['windows'][n]['return_pct']>m[symbol]['windows'][n]['return_pct']
  assert m[c]['windows']['20']['both_up']['loss_fraction']<m[symbol]['windows']['20']['both_up']['loss_fraction']
assert hashlib.sha256((P.parent/'2026-10-19_catchup/COHORT.md').read_bytes()).hexdigest()=='278210becafd4ad78bf8e9d5b8125b35837884b4da6b9347341cf029e4340dcc'
# Literal cash-index sign sensitivity, distinct from adjustedSPY proxy used by primary plan.
d=json.loads((P/'raw/chart-GSPC.json').read_text())['chart']['result'][0];q=d['indicators']['quote'][0]['close'];index={datetime.datetime.fromtimestamp(t,ZoneInfo('America/New_York')).date().isoformat():c for t,c in zip(d['timestamp'],q) if c};cal=sorted(day for day in index if day<=summary['endpoint']);sens={}
for symbol in summary['shortlist']:
 sens[symbol]={}
 for n in ['20','60']:
  grid=cal[-int(n)-1:];ir={day:index[day]/index[prev]-1 for prev,day in zip(grid,grid[1:])};rr=groups[(symbol,n)];up=[r for r in rr if ir[r['date']]>0];both=[r for r in up if float(r['sector_return'])>0]
  sens[symbol][n]=dict(cash_index_up_losses=sum(float(r['stock_return'])<0 for r in up),cash_index_up_days=len(up),cash_both_losses=sum(float(r['stock_return'])<0 for r in both),cash_both_days=len(both),spy_sign_disagreement_dates=[r['date'] for r in rr if (ir[r['date']]>0)!=(float(r['index_return'])>0)])
(P/'cash-index-sensitivity.json').write_text(json.dumps(sens,indent=2)+'\n')
print('PASS:503=501complete+2excluded;all5/20/60dailycountandconditionalreturnreconciliations;strongerpeer+sizeconstraints;originalcohortshaunchanged.')
print('Cash SPX vs adjustedSPY sign disagreements:',{s:{n:v['spy_sign_disagreement_dates'] for n,v in d.items()} for s,d in sens.items()})
print('PASS refers to retained sample arithmetic and source chronology,notcausalidentification/completeglobalpeeruniverse.')
