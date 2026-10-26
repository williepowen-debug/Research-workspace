#!/usr/bin/env python3
"""Recalculate the bounded study from exact retained BTS segments; no network.
Source definitions: class F scheduled service; domestic ORIGIN departures;
Canada-LAS both directions. No missing-filing imputation in observed tables.
"""
import csv,json,math
from collections import defaultdict
from pathlib import Path
D=Path(__file__).resolve().parent
FIELDS=['seats','passengers','departures_performed','departures_scheduled','asm','rpm','records']
def read(name):
 with (D/name).open() as f:return list(csv.DictReader(f))
def save(name,rows):
 if not rows:raise ValueError('empty '+name)
 with (D/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def val(x,k):return float(x[k] or 0)
def aggregate(rows,keyfn):
 a=defaultdict(lambda:{k:0. for k in FIELDS})
 for x in rows:
  if x['CLASS']!='F':continue
  k=keyfn(x);t=a[k]
  for f in FIELDS[:4]:t[f]+=val(x,f.upper())
  t['asm']+=val(x,'SEATS')*val(x,'DISTANCE');t['rpm']+=val(x,'PASSENGERS')*val(x,'DISTANCE');t['records']+=1
 return a
def n(v):return int(v) if v==int(v) else v
def metrics(a):
 return {**{k:n(v) for k,v in a.items()},'passengers_per_seat_pct':round(a['passengers']/a['seats']*100,6) if a['seats'] else '', 'distance_weighted_load_factor_pct':round(a['rpm']/a['asm']*100,6) if a['asm'] else ''}
def pct(a,b):return (a/b-1)*100 if b else None
def family(x):
 c=x['UNIQUE_CARRIER']
 return {'AC':'Air Canada family','QK':'Air Canada family','RV':'Air Canada family','WS':'WestJet','WR':'WestJet','PD':'Porter family','P3':'Porter family','F8':'Flair','07Q':'Flair','TS':'Air Transat','Y9':'Lynx'}.get(c,x['UNIQUE_CARRIER_NAME'])
def canada(x):return x['CARRIER_GROUP']=='0'
def empty():return {k:0. for k in FIELDS}
def sum_cells(cells):
 o=empty()
 for v in cells:
  for k in FIELDS:o[k]+=v[k]
 return o
# Domestic carrier-month rows and airport total/Spirit/other groups.
dom=[x for y in [2025,2026] for x in read(f'GEE_{y}_segments.csv')]
a=aggregate(dom,lambda x:(x['ORIGIN'],int(float(x['YEAR'])),int(float(x['MONTH'])),x['UNIQUE_CARRIER'],x['UNIQUE_CARRIER_NAME']))
save('domestic_carrier_month.csv',[dict(zip(['airport','year','month','carrier','carrier_name'],k),**metrics(v)) for k,v in sorted(a.items())])
groups={};out=[]
for ap in ['FLL','MCO','MIA']:
 for y in [2025,2026]:
  for m in range(1,13 if y==2025 else 8):
   for group in ['Spirit','Other carriers','Total']:
    cells=[v for k,v in a.items() if k[:3]==(ap,y,m) and (group=='Total' or (k[3]=='NK')==(group=='Spirit'))]
    v=sum_cells(cells);groups[ap,y,m,group]=v
    out.append({'airport':ap,'year':y,'month':m,'group':group,**metrics(v)})
save('domestic_airport_month_groups.csv',out)
replacement=[]
for ap in ['FLL','MCO','MIA']:
 for m in range(1,8):
  n25=groups[ap,2025,m,'Spirit'];n26=groups[ap,2026,m,'Spirit'];o25=groups[ap,2025,m,'Other carriers'];o26=groups[ap,2026,m,'Other carriers'];t25=groups[ap,2025,m,'Total'];t26=groups[ap,2026,m,'Total']
  sl=n25['seats']-n26['seats'];pl=n25['passengers']-n26['passengers'];sd=o26['seats']-o25['seats'];pd=o26['passengers']-o25['passengers']
  replacement.append({'airport':ap,'month':m,'spirit_seats_2025':n(n25['seats']),'spirit_seats_2026':n(n26['seats']),'other_seats_2025':n(o25['seats']),'other_seats_2026':n(o26['seats']),'total_seats_2025':n(t25['seats']),'total_seats_2026':n(t26['seats']),'spirit_seat_loss':n(sl),'other_seat_net_change':n(sd),'seat_replacement_pct':round(sd/sl*100,6) if sl>0 else '', 'spirit_passenger_loss':n(pl),'other_passenger_net_change':n(pd),'passenger_replacement_pct':round(pd/pl*100,6) if pl>0 else '', 'total_seats_yoy_pct':round(pct(t26['seats'],t25['seats']),6),'total_passengers_yoy_pct':round(pct(t26['passengers'],t25['passengers']),6),'lf_2025_pct':metrics(t25)['distance_weighted_load_factor_pct'],'lf_2026_pct':metrics(t26)['distance_weighted_load_factor_pct'],'utilization_2025_pct':metrics(t25)['passengers_per_seat_pct'],'utilization_2026_pct':metrics(t26)['passengers_per_seat_pct'],'residual_seat_shortfall':n(t25['seats']-t26['seats'])})
save('domestic_replacement.csv',replacement)
# International LAS<->Canada: both directions, all carrier nationalities; nationality separately shown.
intl=[x for y in [2024,2025,2026] for x in read(f'FJE_{y}_segments.csv')]
b=aggregate(intl,lambda x:(int(float(x['YEAR'])),int(float(x['MONTH'])),x['UNIQUE_CARRIER'],x['UNIQUE_CARRIER_NAME'],family(x),'Canadian/foreign carrier' if canada(x) else 'US carrier','LAS->CA' if x['ORIGIN']=='LAS' else 'CA->LAS'))
save('las_carrier_month_direction.csv',[dict(zip(['year','month','carrier','carrier_name','family','nationality','direction'],k),**metrics(v)) for k,v in sorted(b.items())])
las=[]
for y in [2024,2025,2026]:
 for m in range(1,13 if y<2026 else 8):
  for group in ['All carriers','Canadian/foreign carriers','US carriers']:
   cells=[v for k,v in b.items() if k[:2]==(y,m) and (group=='All carriers' or (k[5]=='US carrier')==(group=='US carriers'))]
   las.append({'year':y,'month':m,'group':group,**metrics(sum_cells(cells))})
save('las_month_groups_observed.csv',las)
# Coverage scan: carrier-month holes on full source geography, and LAS/domestic airport subsets.
# A zero cell is absence of an observed row, not an assertion of zero actual service.
holes=[]
def scan(series,scope,table):
 timeline=sorted({(y,m) for (carrier,y,m) in series});cs=sorted({c for (c,y,m) in series})
 for c in cs:
  for i,(y,m) in enumerate(timeline):
   here=series.get((c,y,m),0);prev=series.get((c,*timeline[i-1]),0) if i else 0;after=series.get((c,*timeline[i+1]),0) if i+1<len(timeline) else 0
   if here==0 and prev>5000 and (after>5000 or i==len(timeline)-1):
    holes.append({'table':table,'scope':scope,'carrier':c,'year':y,'month':m,'previous_seats':n(prev),'next_seats':n(after),'candidate_type':'trailing' if i==len(timeline)-1 else 'interior','verdict':'UNRESOLVED candidate; do not silently treat missing as zero'})
for ap in ['FLL','MCO','MIA']:
 s=defaultdict(float)
 for k,v in a.items():
  if k[0]==ap:s[k[3],k[1],k[2]]+=v['seats']
 scan(s,ap,'GEE')
for table,years in [('GEE',[2025,2026]),('FJE',[2024,2025,2026])]:
 s=defaultdict(float)
 for y in years:
  for x in read(f'{table}_{y}_geography_carrier_month.csv'):s[x['carrier'],int(x['year']),int(x['month'])]+=float(x['seats'])
 scan(s,'full selected geography',table)
s=defaultdict(float)
for k,v in b.items():s[k[2],k[0],k[1]]+=v['seats']
scan(s,'LAS<->CA','FJE')
save('hole_candidates.csv',holes)
# Findings printed as an inspection aid; source tables retain all inputs.
print('DOMESTIC MAY-JULY')
for x in replacement:
 if x['month']>=5:print(json.dumps(x))
print('HOLE CANDIDATES')
for x in holes:print(json.dumps(x))
print('LAS OBSERVED MAY-JULY')
for x in las:
 if x['year']==2026 and x['month']>=5:print(json.dumps(x))
print('LAS FAMILIES')
fams=sorted({k[4] for k in b})
for f in fams:
 by={}
 for y in [2024,2025,2026]:
  by[y]=sum(v['seats'] for k,v in b.items() if k[0]==y and k[1]<=7 and k[4]==f)
 print(f,by)
# Arithmetic and perimeter checks, not tests mirroring implementation.
assert all(x['ORIGIN'] in {'MCO','FLL','MIA'} for x in dom)
assert all((x['ORIGIN']=='LAS' and x['DEST_COUNTRY']=='CA') or (x['DEST']=='LAS' and x['ORIGIN_COUNTRY']=='CA') for x in intl)
assert all(v['passengers']<=v['seats'] for v in a.values())
assert all(v['passengers']<=v['seats'] for v in b.values())
for x in replacement:assert x['spirit_seat_loss']-x['other_seat_net_change']==x['residual_seat_shortfall']
print('CHECKS: geographic perimeter, passenger<=seat, exact seat-loss identity PASS')
# LAS observed comparisons. Complete winter window is unaffected by the known Jun/Jul holes.
monthly={(x['year'],x['month'],x['group']):x for x in las}
compare=[]
for m in range(1,8):
 x=monthly[2026,m,'All carriers'];p=monthly[2025,m,'All carriers'];p2=monthly[2024,m,'All carriers']
 compare.append({'month':m,'seats_2024_observed':p2['seats'],'seats_2025_observed':p['seats'],'seats_2026_observed':x['seats'],'observed_yoy_pct':round(pct(x['seats'],p['seats']),6),'observed_vs2024_pct':round(pct(x['seats'],p2['seats']),6),'coverage':'INCOMPLETE - Air Canada June filing missing' if m==6 else 'INCOMPLETE - Porter July filing missing' if m==7 else 'No known whole-carrier-month hole detected','passengers_2025_observed':p['passengers'],'passengers_2026_observed':x['passengers'],'observed_passenger_yoy_pct':round(pct(x['passengers'],p['passengers']),6)})
save('las_comparison_observed.csv',compare)
# Explicit sensitivity estimates, not observations or grades. AC June national hole
# propagates to LAS even though one adjacent LAS month is <5,000 seats.
carrier=defaultdict(float)
for k,v in b.items():carrier[k[2],k[0],k[1]]+=v['seats']
sensitivity=[]
for m,c,fill,method in [(6,'AC',(carrier['AC',2026,5]+carrier['AC',2026,7])/2,'mean of LAS May and July; not national allocation'),(7,'PD',carrier['PD',2026,6],'carry LAS June forward')]:
 observed=monthly[2026,m,'All carriers']['seats'];base=monthly[2025,m,'All carriers']['seats']
 sensitivity.append({'month':m,'missing_carrier':c,'observed_route_seats':observed,'estimated_missing_seats':fill,'estimate_method':method,'estimated_total_seats':observed+fill,'estimated_yoy_pct':round(pct(observed+fill,base),6),'estimate_not_observation':'YES - never grade this estimate'})
save('las_sensitivity_estimates.csv',sensitivity)
period=[]
for window in ['Winter Nov-Mar','Jan-May','Jan-Jul observed']:
 for fam in ['ALL']+fams:
  sums={}
  for end_year in [2025,2026]:
   vals=[v for k,v in b.items() if (fam=='ALL' or k[4]==fam) and (((k[0]==end_year-1 and k[1]>=11) or (k[0]==end_year and k[1]<=3)) if window=='Winter Nov-Mar' else (k[0]==end_year and k[1]<=(5 if window=='Jan-May' else 7)))]
   sums[end_year]=sum_cells(vals)
  if sums[2025]['seats'] or sums[2026]['seats']:
   period.append({'window':window,'family':fam,'seats_2025_window':n(sums[2025]['seats']),'seats_2026_window':n(sums[2026]['seats']),'yoy_pct':round(pct(sums[2026]['seats'],sums[2025]['seats']),6) if sums[2025]['seats'] else '', 'coverage':'INCOMPLETE Jun/Jul - do not grade' if window=='Jan-Jul observed' else 'No known whole-carrier-month hole detected'})
save('las_period_family.csv',period)
print('LAS MONTH COMPARISON')
for x in compare:print(json.dumps(x))
print('LAS SENSITIVITY - NOT OBSERVED')
for x in sensitivity:print(json.dumps(x))
print('LAS WINTER AND JAN-MAY')
for x in period:
 if x['window']!='Jan-Jul observed':print(json.dumps(x))

# Canadian airline families only, excluding rare third-country/US tag segments.
canadian_codes={'AC','QK','RV','WS','WR','PD','P3','F8','07Q','TS','Y9'}
canadian_windows=[]
for window in ['Winter Nov-Mar','Jan-May']:
 for fam in ['ALL CANADIAN']+sorted({k[4] for k in b if k[2] in canadian_codes}):
  vals={}
  for end_year in [2025,2026]:
   vals[end_year]=sum(v['seats'] for k,v in b.items() if k[2] in canadian_codes and (fam=='ALL CANADIAN' or k[4]==fam) and (((k[0]==end_year-1 and k[1]>=11) or (k[0]==end_year and k[1]<=3)) if window=='Winter Nov-Mar' else (k[0]==end_year and k[1]<=5)))
  if any(vals.values()):canadian_windows.append({'window':window,'family':fam,'seats_2025_window':n(vals[2025]),'seats_2026_window':n(vals[2026]),'yoy_pct':round(pct(vals[2026],vals[2025]),6) if vals[2025] else ''})
save('las_canadian_family_windows.csv',canadian_windows)
print('CANADIAN-AIRLINE-ONLY WINDOWS')
for x in canadian_windows:print(json.dumps(x))
