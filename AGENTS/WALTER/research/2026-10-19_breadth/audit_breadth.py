from pathlib import Path
from datetime import datetime,timezone,timedelta
from zoneinfo import ZoneInfo
import json,statistics,html
D=Path(__file__).resolve().parent;NY=ZoneInfo('America/New_York');snap=json.loads((D/'constituent-snapshot.json').read_text());j=json.loads((D/'chart-SPY.json').read_text())['chart']['result'][0];sessions=sorted({datetime.fromtimestamp(t,NY).date().isoformat() for t in j['timestamp'] if datetime.fromtimestamp(t,NY).date().isoformat()<='2026-10-16'});hist=[]
for i,day in enumerate(sessions[-21:]):
 prev=sessions[sessions.index(day)-1];rr=[]
 for x in snap.values():
  if day in x['bars'] and prev in x['bars']:rr.append(x['bars'][day]/x['bars'][prev]-1)
 hist.append({'date':day,'prior_session':prev,'covered':len(rr),'up':sum(v>0 for v in rr),'down':sum(v<0 for v in rr),'flat':sum(v==0 for v in rr),'expected':503})
ma={}
for n in [20,50,200]:
 prior=sessions[-(n-1):];vals=[];excluded=[]
 for s,x in snap.items():
  if len(prior)==n-1 and all(d in x['bars'] for d in prior):vals.append(x['price']>(sum(x['bars'][d] for d in prior)+x['price'])/n)
  else:excluded.append(s)
 ma[str(n)]={'required_sessions':n,'coverage':len(vals),'above':sum(vals),'pct_above':100*sum(vals)/len(vals) if vals else None,'excluded':excluded,'basis':'currentquote+precedingn-1SPYsessions,rawvendorprices;currentholdingsproxy;notclosegrade'}
week=[]
for s in ['SPY','RSP']:
 z=json.loads((D/f'chart-{s}.json').read_text())['chart']['result'][0];ds=[datetime.fromtimestamp(t,NY).date().isoformat() for t in z['timestamp']];q=z['indicators']['quote'][0]['close'];a=z['indicators']['adjclose'][0]['adjclose'];px={d:(p,v) for d,p,v in zip(ds,q,a)}
 for start,end in [('2026-10-02','2026-10-09'),('2026-10-09','2026-10-16')]:week.append({'symbol':s,'start':start,'end':end,'price_return_pct':100*(px[end][0]/px[start][0]-1),'adj_return_pct':100*(px[end][1]/px[start][1]-1)})
out={'reviewed_at':datetime.now(timezone.utc).isoformat(),'history':hist,'moving_averages':ma,'weekly':week,'limits':'historicalcurrentbasket,survivorship/indexmembershiplimitations;priorstocknullbarsnotfilled,skipnotallowed;nohistoricalbreadthclaimwithoutdatecoverage'}
(D/'session-audit.json').write_text(json.dumps(out,indent=2)+'\n');print('MA',json.dumps(ma));print('Weeks',json.dumps(week));print('Last10counts',hist[-10:])
# Small self-contained vector export, no plottingpackageorinstall.
series={}
for s in ['SPY','RSP']:
 z=json.loads((D/f'chart-{s}.json').read_text())['chart']['result'][0];series[s]={datetime.fromtimestamp(t,NY).date().isoformat():v for t,v in zip(z['timestamp'],z['indicators']['adjclose'][0]['adjclose']) if v is not None}
ds=sorted(d for d in set(series['SPY'])&set(series['RSP']) if d<='2026-10-16')[-64:];vals={s:[100*series[s][d]/series[s][ds[0]] for d in ds] for s in series};lo=min(min(v) for v in vals.values())-1;hi=max(max(v) for v in vals.values())+1
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="520" viewBox="0 0 1120 520">','<rect width="1120" height="520" fill="#fff"/>','<style>text{font-family:Arial,sans-serif;fill:#1f2937}.small{font-size:13px}.title{font-size:24px;font-weight:bold}.label{font-size:16px}</style>','<text x="35" y="38" class="title">A rising index can mask weak participation</text>','<text x="35" y="67" class="label">Recent equal-weight recovery coexists with a narrow rebound today</text>']
X=lambda i:75+570*i/(len(ds)-1);Y=lambda v:365-240*(v-lo)/(hi-lo)
for k in range(5):
 v=lo+(hi-lo)*k/4;y=Y(v);svg+= [f'<line x1="75" y1="{y}" x2="645" y2="{y}" stroke="#e5e7eb"/>',f'<text x="32" y="{y+5}" class="small">{v:.0f}</text>']
for s,color in [('SPY','#2563eb'),('RSP','#c2410c')]:
 pts=' '.join(f'{X(i):.1f},{Y(v):.1f}' for i,v in enumerate(vals[s]));svg.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3"/>');svg.append(f'<text x="650" y="{Y(vals[s][-1])+5}" class="label" style="fill:{color}">{s}</text>')
for i in [0,21,42,63]:svg.append(f'<text x="{X(i)-25}" y="395" class="small">{ds[i][5:]}</text>')
svg += ['<text x="75" y="103" class="label">63-session adjusted-price wealth proxy</text>','<text x="75" y="422" class="small">SPY: size weighted   RSP: equal weight   Start = 100; through Oct 16</text>','<text x="760" y="103" class="label">Oct 19, about 2:57 p.m. ET</text>']
b=json.loads((D/'breadth-summary.json').read_text())
for i,(label,key,color) in enumerate([('Up','up','#15803d'),('Down','down','#b91c1c'),('Flat','unchanged','#6b7280')]):
 v=b[key];x=770+i*95;h=v/350*220;svg += [f'<rect x="{x}" y="{365-h}" width="58" height="{h}" fill="{color}"/>',f'<text x="{x+29}" y="{355-h}" text-anchor="middle" class="label">{v}</text>',f'<text x="{x+29}" y="395" text-anchor="middle" class="label">{label}</text>']
svg+=['<text x="760" y="422" class="small">503 tradable equity lines in SPY holdings</text>','<text x="35" y="466" class="small">Sources: SSGA holdings dated Oct 16 / Yahoo daily bars and quotes. Quote times 14:50–14:57 ET; intraday, not a closing grade.</text>','<text x="35" y="490" class="small">Current-holdings proxy, not an official index count. Counts include multiple share classes. SPY and RSP are ETF proxies.</text>','</svg>'];(D/'breadth.svg').write_text('\n'.join(svg)+'\n')
