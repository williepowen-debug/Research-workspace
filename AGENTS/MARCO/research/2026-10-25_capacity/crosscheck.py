#!/usr/bin/env python3
"""Bounded old-summary endpoint cross-check; no canonical baseline writes."""
import csv,json,sys
from pathlib import Path
D=Path(__file__).resolve().parent
sys.path.insert(0,str(D.parents[1]/'tools'))
from bts_airport_pull import pull
import requests
s=requests.Session();rows=[];meta=[]
for carrier,airports in [('All',['MCO','FLL','MIA']),('NK',['MCO','FLL','MIA'])]:
 for ap in airports:
  values=pull(ap,carrier,s);latest=max(values)
  meta.append({'airport':ap,'carrier':carrier,'endpoint':'https://transtats.bts.gov/Data_Elements.aspx?Data=1','latest_actual':f'{latest[0]}-{latest[1]:02d}','parsed_rows':len(values)})
  for (y,m),v in sorted(values.items()):
   if y>=2024:rows.append({'airport':ap,'carrier':carrier,'year':y,'month':m,'domestic':v[0],'international':v[1],'total':v[2]})
  print(meta[-1],flush=True)
with (D/'summary_endpoint_crosscheck.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['airport','carrier','year','month','domestic','international','total'],lineterminator='\n');w.writeheader();w.writerows(rows)
(D/'summary_endpoint_coverage.json').write_text(json.dumps(meta,indent=2)+'\n')
