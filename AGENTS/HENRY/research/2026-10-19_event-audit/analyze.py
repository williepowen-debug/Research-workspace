"""Reproduce frozen-window event sensitivities; run from this script's directory or elsewhere."""
from pathlib import Path
import csv,json,math,hashlib,datetime as dt,gzip,tarfile
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parent
INPUT=P.parent/'2026-10-19_repeat-losers/daily-audit.csv.gz'
SYMS=['MOS','HII','ADM','CPRT']
def read_raw(name):
 path=P/name
 if path.exists():return path.read_text()
 with tarfile.open(P/'sources.tar.gz') as ar:return ar.extractfile(name).read().decode()
rows=[]
for r in csv.DictReader(gzip.open(INPUT,'rt')):
 if r['symbol'] not in SYMS:continue
 for k in ['window']:r[k]=int(r[k])
 for k in ['stock_return','index_return','sector_return']:r[k]=float(r[k])
 for k in ['index_up','sector_up','both_up','stock_loss','index_lag','sector_lag']:r[k]=r[k]=='True'
 rows.append(r)
D=sorted({r['date'] for r in rows});events=[]
def event(sym,date,mode,title,source,kind='operating',note=''):
 events.append(dict(symbol=sym,date=date,clock=mode,title=title,source=source,kind=kind,note=note))
receipts=json.load(open(P/'filing-receipts.json'))
def sec(sym,part):
 return next(x['url'] for x in receipts if x['symbol']==sym and part in x['url'])
# Unknown release clocks retain both dated and following sessions; no inference from late filings.
event('MOS','2026-08-04','unknown','Q2 results, phosphate production constraints and outlook',sec('MOS','000109'),'earnings','SEC accepted16:26ET; actual issuer release clock unverified, conservative dated+next union')
event('MOS','2026-08-10','same','Tender offer announcement and new-note underwriting',sec('MOS','341391'),'capital','Accepted08:50ET; public no later than before open')
event('MOS','2026-08-14','unknown','Tender pricing',sec('MOS','352365'),'capital','Release datedAug14; late SEC acceptance does not establish first public clock')
event('MOS','2026-08-17','same','Final tender results',sec('MOS','353193'),'capital','Accepted06:38ET')
event('MOS','2026-08-17','unknown','Completed $2B new notes',sec('MOS','354095'),'capital','Completed, not denied financing; filing16:18ET is latest known public time')
event('MOS','2026-08-28','unknown','Redemption notice for2027/2028notes',sec('MOS','000122'),'capital','Notice of scheduledSept28redemption, not evidence execution occurred')
event('MOS','2026-10-14','unknown','South Fort Meade199 layoffs, state notification received', 'https://reactwarn.floridajobs.org/WarnList/Records?year=2026','operating','Primary record state notification10/14, layoff12/8; underlying letter download403; NOT October5 public event')
event('ADM','2026-08-04','same','Q2 results and raised adjustedEPSguidance',sec('ADM','000040'),'earnings','SEC public10:03ET; issuer call08:30ET; public no later than intraday')
event('ADM','2026-08-10','unknown','New-note underwriting agreement disclosed with closing',sec('ADM','342579'),'capital','AgreementAug5; first captured public disclosureAug10with closing. No exclusion backdated to private agreement')
event('ADM','2026-08-10','unknown','Completed $1Bnotes',sec('ADM','342579'),'capital','Completed4.829%2031and5.269%2036; filingafterclose')
# HII issuer-distributed wire gives actual ET times, including after-hours dates that differ from URL dates.
seen=set()
for i in [0,2,3]:
 s=BeautifulSoup(read_raw(f'raw/HII-wire-{i}.html'),'html.parser')
 for x in s.select('.newsLink'):
  a=x.select_one('.mainLink a');clock=x.select_one('.date-source span')
  if not a or not clock:continue
  title=a.get_text(' ',strip=True);url='https://www.globenewswire.com'+a['href']
  if url in seen:continue
  seen.add(url);stamp=dt.datetime.strptime(clock.text.strip(),'%B %d, %Y %H:%M ET');date=stamp.date().isoformat()
  if date<'2026-07-24':continue
  admin=any(t in title for t in ['Hiring Event','Hosts National Commission','Conference Call','Promotes Greg','1,000 Trainees','Media Advisory','Workforce Development','Names Chris','Declares Quarterly','Hosts Australian','Names Michael'])
  kind='admin' if admin else ('earnings' if 'Results' in title else 'operating')
  event('HII',date,'next' if stamp.hour>=16 else 'same',title,url,kind,'Wire timestamp '+clock.text.strip())
event('HII','2026-10-19','unknown','Autonomous launcher demonstration','https://www.hii.com/newsroom','operating','Issuer newsroom captured; clock unknown; modest operating milestone, broad event sensitivity only')
event('CPRT','2026-09-10','next','Q4 results',sec('CPRT','387902'),'earnings','IssuerSep1 scheduledreleaseafter16ET; actual8Kaccepted20:16ET. Plannedclock corroborates, exactactualrelease timestamp unavailable')
event('CPRT','2026-09-10','unknown','ACV merger agreement announcement',sec('CPRT','388064'),'capital','Actual release clock unresolved: preserveSep10and11, do not assume earnings clock applies to deal')
fups=json.load(open(P/'followup-receipts.json'))
for i,date,title in [(5,'2026-09-17','ACV tender commencement'),(4,'2026-09-29','HSR withdrawal/refiling and lawsuits disclosed'),(3,'2026-10-01','ACV first tender extension'),(2,'2026-10-08','ACV second tender extension'),(1,'2026-10-14','HSR clearance condition satisfied')]:
 event('CPRT',date,'unknown',title,fups[i]['url'],'capital','Public dated release/filing; clock unresolved. Sep28underlyingHSRevent first capturedSep29: removeSep29+30, not privateSep28date')
event('CPRT','2026-10-16','same','ACV acquisition completed',sec('CPRT','423478'),'capital','Accepted13:59ET; consummation completedOct16')
event('CPRT','2026-10-16','unknown','20MCEOoptionaward, grantedOct14',sec('CPRT','424052'),'capital','Material award subject shareholderapproval. First captured publicfilingOct16afterclose; no proof prior disclosure. UnknownunionOct16+19; NOT backdated toOct14grant')
# Map unknown date to conservative union, never include sessions before dated information except labelled halo.
def mapped(e):
 future=[d for d in D if d>=e['date']]
 if not future:return []
 if e['clock']=='next' and future[0]==e['date']:future=future[1:]
 return future[:2] if e['clock']=='unknown' and future and future[0]==e['date'] else future[:1]
for e in events:e['removed_sessions']=mapped(e) if e['kind']!='admin' else []
(P/'events.json').write_text(json.dumps(events,indent=2)+'\n')
(P/'input-receipt.json').write_text(json.dumps({'input':str(INPUT.relative_to(P.parent.parent.parent.parent)),'compressed_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),'decompressed_sha256':hashlib.sha256(gzip.decompress(INPUT.read_bytes())).hexdigest(),'frozen_cohort_sha256':hashlib.sha256((P.parent/'2026-10-19_catchup/COHORT.md').read_bytes()).hexdigest(),'frozen_repeat_result_sha256':hashlib.sha256((P.parent/'2026-10-19_repeat-losers/RESULT.md').read_bytes()).hexdigest()},indent=2)+'\n')
def comp(r,key):return math.prod(1+x[key] for x in r)-1
out=[];worst=[]
for sym in SYMS:
 allset={d for e in events if e['symbol']==sym for d in e['removed_sessions']}
 earnset={d for e in events if e['symbol']==sym and e['kind']=='earnings' for d in e['removed_sessions']}
 halo={D[j] for d in allset for j in range(max(0,D.index(d)-1),min(len(D),D.index(d)+2))}
 for w in [5,20,60]:
  sample=sorted([r for r in rows if r['symbol']==sym and r['window']==w],key=lambda x:x['date']);assert len(sample)==w
  low=min(sample,key=lambda x:(x['stock_return'],x['date']));worst.append(dict(symbol=sym,window=w,**{k:low[k] for k in ['date','stock_return','index_up','sector_up','both_up']}))
  for scenario,excluded in [('baseline',set()),('earnings',earnset),('events',allset),('worst',{low['date']}),('events+worst',allset|{low['date']}),('halo',halo)]:
   kept=[r for r in sample if r['date'] not in excluded]
   base=dict(symbol=sym,window=w,scenario=scenario,retained=len(kept),removed=';'.join(r['date'] for r in sample if r['date'] in excluded),stock_retained_return=comp(kept,'stock_return'),index_retained_return=comp(kept,'index_return'),sector_retained_return=comp(kept,'sector_return'))
   for condition in ['index_up','sector_up','both_up']:
    eligible=[r for r in kept if r[condition]];n=len(eligible);loss=sum(r['stock_loss'] for r in eligible)
    out.append(dict(**base,condition=condition,eligible=n,losses=loss,index_lags=sum(r['index_lag'] for r in eligible),sector_lags=sum(r['sector_lag'] for r in eligible),loss_fraction=loss/n if n else '',majority=loss>n/2 if n else False))
with (P/'sensitivities.csv').open('w') as f:
 wr=csv.DictWriter(f,fieldnames=list(out[0]));wr.writeheader();wr.writerows(out)
(P/'worst-days.json').write_text(json.dumps(worst,indent=2)+'\n')
# Independent checks: arithmetic products vs log-sum; counts from numeric return signs rather than saved flags.
for r in rows:
 assert r['stock_loss']==(r['stock_return']<0)
 assert r['index_up']==(r['index_return']>0)
 assert r['sector_up']==(r['sector_return']>0)
 assert r['both_up']==(r['index_return']>0 and r['sector_return']>0)
for o in out:
 kept=[r for r in rows if r['symbol']==o['symbol'] and r['window']==o['window'] and r['date'] not in o['removed'].split(';')]
 for key in ['stock','index','sector']:
  assert abs(math.expm1(math.fsum(math.log1p(r[key+'_return']) for r in kept))-o[key+'_retained_return'])<1e-12
 assert o['eligible']==sum(r[o['condition']] for r in kept)
 assert o['losses']==sum(r[o['condition']] and r['stock_return']<0 for r in kept)
assert hashlib.sha256((P.parent/'2026-10-19_catchup/COHORT.md').read_bytes()).hexdigest()=='278210becafd4ad78bf8e9d5b8125b35837884b4da6b9347341cf029e4340dcc'
assert hashlib.sha256((P.parent/'2026-10-19_repeat-losers/RESULT.md').read_bytes()).hexdigest()=='7667de05aafc30edf6276b597454e5fd2cc191fd1ecc7bedf32a4af2ee960984'
print('PASS',len(rows),'source rows,',len(out),'sensitivity rows,',len(events),'events/admin entries; original studies immutable')
for sym in SYMS:
 for scenario in ['baseline','earnings','events','worst','events+worst','halo']:
  a=[o for o in out if o['symbol']==sym and o['scenario']==scenario and o['condition']=='both_up']
  print(sym,scenario,[(o['window'],round(o['stock_retained_return']*100,3),f"{o['losses']}/{o['eligible']}") for o in a])
