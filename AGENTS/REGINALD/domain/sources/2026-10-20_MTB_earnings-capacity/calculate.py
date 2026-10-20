"""Research arithmetic, not a forecast. Dollars millions unless stated."""
import json, hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
# Q3 release earnings highlights, average liabilities, capital discussion.
x=dict(nii=1793,fees=743,expense=1393,provision=135,tax=233,pretax=1008,
       net_income=775,ib_deposits=123069,common_dividends=217,
       preferred_dividends=42,buybacks=323,loan_provision=130,nco=127,
       beginning_allowance=2176,ending_allowance=2179)
# Cross-check scenario inputs against the retained primary table extraction.
tables={z['table']:z['rows'] for z in json.loads((p/'Q3-release-tables.json').read_text())}
def first_value(table,label,index=0):
 row=next(z for z in tables[table] if z.split('|')[0].strip()==label)
 cells=[c.strip().replace(',','') for c in row.split('|')[1:]]
 nums=[]
 for cell in cells:
  try: nums.append(float(cell))
  except ValueError: pass
 return nums[index]
for key,table,label in [('nii',1,'Net interest income'),('fees',1,'Noninterest income'),
 ('expense',1,'Noninterest expense'),('provision',1,'Provision for credit losses'),
 ('net_income',1,'Net income'),('tax',40,'Income taxes'),
 ('ib_deposits',14,'Total interest-bearing deposits'),
 ('loan_provision',16,'Provision for loan losses'),('nco',16,'Net charge-offs'),
 ('ending_allowance',16,'Allowance for loan losses')]:
 assert x[key]==first_value(table,label),(key,x[key])
assert x['beginning_allowance']==first_value(16,'Allowance for loan losses',1)
release=(p/'Q3-release.txt').read_text()
for passage in ['$217 million and $42 million','$323 million']:
 assert passage in release,passage
ppnr=x['nii']+x['fees']-x['expense'];tax=x['tax']/x['pretax']
payout=x['common_dividends']+x['preferred_dividends']+x['buybacks']
assert ppnr-x['provision']==x['pretax']
assert x['pretax']-x['tax']==x['net_income']
assert x['beginning_allowance']+x['loan_provision']-x['nco']==x['ending_allowance']
# Static 92/365-day quarter. Every additional bp hits all IB deposits immediately;
# no asset repricing, hedge offset, mix/volume or tax-rate response is modeled.
scenarios=[]
for label,provision,bps,expense_pct in [
 ('Q3 actual arithmetic',135,0,0),('Higher credit expense only',400,0,0),
 ('Provisions250 plus deposit cost25bp',250,25,0),
 ('Provisions400 plus deposit cost25bp',400,25,0),
 ('Provisions600 plus deposit cost50bp and expense5pct',600,50,.05)]:
 funding=x['ib_deposits']*bps/10000*92/365;extra_exp=x['expense']*expense_pct
 pre=ppnr-funding-extra_exp-provision;net=pre*(1-tax)
 scenarios.append(dict(label=label,total_provision=provision,extra_deposit_cost_bp=bps,
   extra_funding_expense=funding,extra_operating_expense=extra_exp,pretax=pre,
   net_income=net,retained_after_unchanged_distributions=net-payout))
quote=json.loads((p/'MTB-Yahoo-vendor-snapshot.json').read_text())['quote_info']
results=dict(inputs=x,ppnr=ppnr,provision_share_of_ppnr=x['provision']/ppnr,
 ppnr_provision_multiple=ppnr/x['provision'],effective_tax_rate=tax,
 distributions=payout,retained_before_oci=x['net_income']-payout,
 provision_ceiling_to_cover_all_Q3_distributions=ppnr-payout/(1-tax),
 provision_ceiling_for_net_income_zero=ppnr,
 q4_guidance_te_ppnr_low=1830+710-1410,q4_guidance_te_ppnr_high=1850+730-1390,
 price=quote['regularMarketPrice'],quote_epoch=quote['regularMarketTime'],
 price_to_q3_tbv=quote['regularMarketPrice']/115.88,
 vendor_forward_pe=quote['regularMarketPrice']/quote['forwardEps'],scenarios=scenarios)
# Verify downloaded bytes against successful request receipts; failed 403 stays a failure.
verified=[]
for receipt in json.loads((p/'retrieval.json').read_text()):
 if receipt.get('status')==200:
  ext='json' if receipt['id']=='MTB-submissions' else 'html'
  f=p/(receipt['id']+'.'+ext)
  assert hashlib.sha256(f.read_bytes()).hexdigest()==receipt['sha256'],f
  verified.append(f.name)
for receipt in json.loads((p/'slide-retrieval.json').read_text()):
 f=p/receipt['path'];assert receipt['status']==200
 assert hashlib.sha256(f.read_bytes()).hexdigest()==receipt['sha256'],f
 verified.append(f.name)
results['verified_primary_downloads']=verified
(p/'calculations.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
