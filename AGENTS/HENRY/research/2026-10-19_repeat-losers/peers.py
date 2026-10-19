import json,pathlib,math
P=pathlib.Path(__file__).resolve().parent
m=json.loads((P/'metrics.json').read_text());summary=json.loads((P/'summary.json').read_text());prior=json.loads((P.parent/'2026-10-19_catchup/shares.json').read_text());shares={k:prior[k] for k in ['MOS','CF','MGM','WYNN','LVS']}
rows=[('HII',39404203,'2026-06-30','2026-07-30','1501585/000150158526000047/hii-20260630.htm','us-gaap:CommonStockSharesOutstanding contextc-14,notJuly24cover'),('ADM',482000000,'2026-06-30','2026-08-04','7084/000000708426000042/adm-20260630.htm','CommonStockSharesOutstanding c-19 scale6,already net treasury;rounded'),('MCD',707641531,'2026-06-30','2026-08-07','63908/000006390826000073/mcd-20260630.htm','dei:EntityCommonStockSharesOutstanding contextc-2 is June30 periodend,notJulycover;matches roundedissued1660.6M minus953.0Mtreasury'),('SBUX',1139800000,'2026-06-28','2026-07-29','829224/000082922426000130/sbux-20260628.htm','CommonStockSharesOutstanding c-57 scale6;notJuly23cover1140.0M'),('PCAR',526360000,'2026-06-30','2026-07-29','75362/000119312526323642/pcar-20260630.htm','Roundedissued526.4M less0.04Mtreasury=526.36M;notJuly24cover'),('CPRT',925811482,'2026-04-30','2026-05-29','900075/000119312526245578/cprt-20260430.htm','April30outstanding925811482;September10Q4releasecontainsEPSaverages,noteligibleJuly31outstandingcount;July31annual10KfiledSeptember29AFTERformationexcluded'),('INGR',63100000,'2026-06-30','2026-08-07','1046257/000162828026054722/ingr-20260630.htm','Roundedissued77.8M less14.7Mtreasury=63.1M;notAugust5cover')]
for s,n,d,a,url,b in rows:shares[s]=dict(shares=n,period_end=d,available_by=a,source='https://www.sec.gov/Archives/edgar/data/'+url,basis=b)
formation=summary['starts']['20'];caps={s:m[s]['formation_raw_close']*r['shares']/1e9 for s,r in shares.items()};assert all(r['available_by']<formation for r in shares.values())
pools={'MOS':['CF','NTR'],'HII':['GD','BWXT'],'ADM':['BG','INGR'],'MGM':['WYNN','LVS'],'MCD':['YUM','SBUX','QSR','DPZ','CMG'],'PCAR':['CMI'],'CPRT':['RBA']}
audit=[];matches={}
for s,cs in pools.items():
 eligible=[]
 for c in cs:
  a,b=m[s]['windows'],m[c]['windows'];stronger=b['20']['return_pct']>a['20']['return_pct'] and b['60']['return_pct']>a['60']['return_pct'] and b['20']['both_up']['loss_fraction']<a['20']['both_up']['loss_fraction']
  ratio=max(caps[s],caps[c])/min(caps[s],caps[c]) if c in caps else None
  row=dict(weak=s,candidate=c,stronger_20_and_60_and_lower_20_both_loss=stronger,weak_cap_bn=caps[s],candidate_cap_bn=caps.get(c),size_ratio=ratio,weak_20_pct=a['20']['return_pct'],candidate_20_pct=b['20']['return_pct'],weak_60_pct=a['60']['return_pct'],candidate_60_pct=b['60']['return_pct'])
  if not stronger:row['disposition']='REJECTED_STRENGTH'
  elif c=='YUM':
   bound=m[c]['formation_raw_close']*273000000/1e9;row.update(candidate_cap_upper_bound_bn=bound,source='https://www.sec.gov/Archives/edgar/data/1041061/000104106126000160/yum-20260630.htm',bound_basis='273M issued shares bound outstanding from above;NOT an outstanding-share marketcap');assert bound<caps[s]/2;row['disposition']='REJECTED_SIZE_UPPER_BOUND'
  elif ratio is None:row['disposition']='UNRESOLVED_PERIODEND_SIZE_OR_CLASSES'
  elif ratio>2:row['disposition']='REJECTED_SIZE'
  else:row['disposition']='ELIGIBLE';eligible.append(row)
  audit.append(row)
 if eligible:
  best=min(eligible,key=lambda r:(abs(math.log(r['candidate_cap_bn']/r['weak_cap_bn'])),r['candidate']));c=best['candidate'];matches[s]=dict(control=c,size_ratio=best['size_ratio'],weak_cap_bn=caps[s],control_cap_bn=caps[c],difference_pp={n:m[s]['windows'][n]['return_pct']-m[c]['windows'][n]['return_pct'] for n in ['5','20','60']})
 else:matches[s]=dict(control=None,weak_cap_bn=caps[s],reason='No verified stronger peer within2x in boundedindustrypool;seeaudit,notwholemarketcensus')
robust=[s for s in summary['shortlist'] if all(m[s]['windows'][n][c]['loss_fraction']>.5 for n in ['20','60'] for c in ['index_up','sector_up','both_up'])]
sensitivity={}
for minimum in [(5,15),(4,12),(0,0)]:
 names=[]
 for s in [r['ticker'] for r in json.loads((P/'universe.json').read_text())['rows']]:
  if s not in m:continue
  a,b=m[s]['windows']['20'],m[s]['windows']['60'];ca,cb=a['both_up'],b['both_up']
  if ca['eligible']>=minimum[0] and cb['eligible']>=minimum[1] and a['return_pct']<0 and b['return_pct']<0 and ca['loss_fraction'] is not None and cb['loss_fraction'] is not None and ca['loss_fraction']>.5 and cb['loss_fraction']>.5:names.append(s)
 sensitivity[str(minimum)]=names
assert set(sensitivity['(5, 15)'])==set(sensitivity['(0, 0)']);assert robust==['MOS','HII','ADM','CPRT']
for name,d in [('shares.json',shares),('formation-caps.json',caps),('peer-audit.json',audit),('stronger-matches.json',matches),('robustness.json',dict(separate_condition_robust=robust,min_eligible_sensitivity=sensitivity))]: (P/name).write_text(json.dumps(d,indent=2)+'\n')
print('Separate index/sector/BOTH-up robust in20and60:',robust)
for s,r in matches.items():print(s,r)
print('PASS strongerpeerconstraints,2xsize,preformationavailability,denominatorsensitivity,noforcedmatch')
