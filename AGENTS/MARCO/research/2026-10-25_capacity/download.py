#!/usr/bin/env python3
"""One-off reproducible BTS source extraction for the commissioned Oct25 study.
No scheduled collector or canonical-baseline writes. Full archives in /tmp;
exact relevant segment rows and source metadata beside this script.
"""
import csv,hashlib,io,json,re,zipfile
from pathlib import Path
from datetime import datetime,timezone
import requests
from bs4 import BeautifulSoup
OUT=Path(__file__).resolve().parent
CACHE=Path('/tmp/marco_capacity_20261025');CACHE.mkdir(exist_ok=True)
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
COMMON=['DEPARTURES_SCHEDULED','DEPARTURES_PERFORMED','SEATS','PASSENGERS','DISTANCE','UNIQUE_CARRIER','AIRLINE_ID','UNIQUE_CARRIER_NAME','UNIQUE_CARRIER_ENTITY','REGION','CARRIER_GROUP','CARRIER_GROUP_NEW','ORIGIN','ORIGIN_CITY_NAME','DEST','DEST_CITY_NAME','AIRCRAFT_TYPE','AIRCRAFT_CONFIG','YEAR','MONTH','CLASS']
JOBS=[('GEE','Florida',2025),('GEE','Florida',2026),('FJE','Canada',2024),('FJE','Canada',2025),('FJE','Canada',2026)]
def save_csv(path,header,rows):
 with path.open('w',newline='') as f:
  w=csv.writer(f,lineterminator='\n');w.writerow(header);w.writerows(rows)
def run(table,geo,year):
 s=requests.Session();s.headers['User-Agent']=UA
 url=f'https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ={table}&QO_fu146_anzr=Nv4%20Pn44vr45'
 g=s.get(url,timeout=35);g.raise_for_status();soup=BeautifulSoup(g.text,'html.parser')
 text=soup.get_text(' ',strip=True);m=re.search(r'Latest Available Data:\s*([A-Za-z]+\s+\d{4})',text)
 fields=COMMON+(['ORIGIN_STATE_ABR','DEST_STATE_ABR'] if table=='GEE' else ['ORIGIN_COUNTRY','DEST_COUNTRY'])
 names={x.get('name') for x in soup.select('input[type=checkbox]')}
 assert set(fields)<=names,(table,set(fields)-names)
 payload={i.get('name'):i.get('value','') for i in soup.select('input[type=hidden]') if i.get('name')}
 payload.update({'__EVENTTARGET':'','__EVENTARGUMENT':'','__LASTFOCUS':'','cboGeography':geo,'cboYear':str(year),'cboPeriod':'All','btnDownload':'Download'})
 payload.update({x:'on' for x in fields})
 r=s.post(url,data=payload,timeout=50);r.raise_for_status()
 if r.content[:2]!=b'PK':
  (CACHE/f'{table}_{year}_error.html').write_bytes(r.content)
  raise ValueError(f'{table}/{year}: not ZIP, {r.headers.get("Content-Type")}')
 arc=CACHE/f'{table}_{geo}_{year}.zip';arc.write_bytes(r.content)
 z=zipfile.ZipFile(io.BytesIO(r.content));members=[n for n in z.namelist() if n.lower().endswith('.csv')];assert len(members)==1,members
 raw=z.read(members[0]);reader=csv.DictReader(io.StringIO(raw.decode('utf-8-sig')))
 rows=[{k.strip().upper():v for k,v in row.items() if k and k.strip()} for row in reader]
 assert rows
 header=list(rows[0]);months=sorted({int(float(x['MONTH'])) for x in rows});years={int(float(x['YEAR'])) for x in rows};assert years=={year},years
 if table=='GEE':selected=[x for x in rows if x['ORIGIN'] in {'MCO','FLL','MIA'}]
 else:selected=[x for x in rows if (x['ORIGIN']=='LAS' and x['DEST_COUNTRY']=='CA') or (x['DEST']=='LAS' and x['ORIGIN_COUNTRY']=='CA')]
 assert selected,(table,year,'no selected rows')
 save_csv(OUT/f'{table}_{year}_segments.csv',header,([x[k] for k in header] for x in selected))
 # Full-geography carrier-month coverage diagnostic, not an imputation.
 from collections import defaultdict
 agg=defaultdict(lambda:[0.,0.,0.,0.])
 for x in rows:
  if x['CLASS']!='F':continue
  a=agg[(year,int(float(x['MONTH'])),x['UNIQUE_CARRIER'],x['UNIQUE_CARRIER_NAME'])]
  for i,k in enumerate(['SEATS','PASSENGERS','DEPARTURES_PERFORMED','DEPARTURES_SCHEDULED']):a[i]+=float(x[k] or 0)
 save_csv(OUT/f'{table}_{year}_geography_carrier_month.csv',['year','month','carrier','name','seats','passengers','departures_performed','departures_scheduled'],([*k,*v] for k,v in sorted(agg.items())))
 rec={'table':table,'geography':geo,'year':year,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'url':url,'latest_label':m.group(1) if m else None,'actual_months':months,'archive_bytes':len(r.content),'archive_sha256':hashlib.sha256(r.content).hexdigest(),'csv_sha256':hashlib.sha256(raw).hexdigest(),'csv_member':members[0],'full_rows':len(rows),'retained_rows':len(selected),'retained_rule':'ORIGIN in MCO/FLL/MIA' if table=='GEE' else 'LAS<->CA either direction','class_filter_in_saved_segments':'none; analysis selects F','fields':header}
 print(json.dumps(rec),flush=True);return rec
if __name__=='__main__':
 manifest=[]
 for job in JOBS:
  manifest.append(run(*job));(OUT/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
