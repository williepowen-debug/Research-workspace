"""Read saved originals only; preserve bank equity and scope reconciliations."""
from pathlib import Path
from decimal import Decimal as D
import json,csv,io
HERE=Path(__file__).resolve().parent
receipts=json.loads((HERE/'retrieval.json').read_text()); d={}; selected=[]
for r in receipts:
 rows=list(csv.reader(io.StringIO(Path(r['raw_path']).read_text()),delimiter=';'))[1:]
 d[(r['bank'],r['report_date'])]={x[2]:x for x in rows if len(x)>=8}
fields=['RIAD4340','RIAD4356','RIAD4415','RIAD4460','RIAD4470','RIADB509','RIADB510','RIADB511']
def value(rows,k):return D(rows[k][3].replace('%',''))
summary=[]
for bank in dict.fromkeys(r['bank'] for r in receipts):
 b,c=d[(bank,'20260630')],d[(bank,'20260930')]
 changes={k:value(c,k)-value(b,k) for k in fields}
 net=sum(v*(-1 if k in ['RIAD4460','RIAD4470'] else 1) for k,v in changes.items())
 actual=value(c,'RIAD3210')-value(b,'RIAD3210');assert net==actual,(bank,net,actual)
 summary.append({'bank':bank,'q3_RIA_changes_k':changes,'equity_change_k':actual,'bridge_residual_k':actual-net})
 for date,rows in [('20260630',b),('20260930',c)]:
  codes=fields+['RIAD3210']+[k for k in rows if k.endswith(('K043','K044','C226','C227','C228','K036','K037','K038','K039','K040','K041','K042','2746','J454'))]
  for code in dict.fromkeys(codes):
   if code in rows:selected.append([bank,date]+rows[code])
(HERE/'equity-bridges.json').write_text(json.dumps(summary,default=str,indent=2)+'\n')
with (HERE/'bridge-primary-rows.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['bank','period','Call Date','Bank RSSD','MDRM','Value','Last Update','Short Definition','Schedule','Line']);w.writerows(selected)
print('All 14 equity bridges reconcile exactly to $000.')
for z in summary:
 if z['bank'] in ['FLG','WAL','OZK','AMTB','SBCF']:print(z['bank'],json.dumps(z,default=str))
