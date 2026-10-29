from pathlib import Path
import csv,json,datetime as dt,sys
import xlrd
H=Path(__file__).parent; R=H/'raw';B=H.parents[1]
sys.path.insert(0,str(B/'monitors'))
from rates_context import parse_fomc_calendar

def iso(s):return dt.datetime.strptime(s,'%m/%d/%Y').date().isoformat()
def curves(fn):return {iso(x['Date']):{k:float(v) for k,v in x.items() if k!='Date' and v} for x in csv.DictReader((R/fn).open())}
n=curves('nominal.csv');r=curves('real.csv');days=sorted(n)
summary={'nominal_frontier':days[-1],'real_frontier':max(r),'curve_rows':[]}
for d in days[-8:]:
 x=n[d];real=r[d];summary['curve_rows'].append({'date':d,'nominal':x,'real':real,'2s10s_bp':round((x['10 Yr']-x['2 Yr'])*100),'5s30s_bp':round((x['30 Yr']-x['5 Yr'])*100),'10y_nominal_minus_real':round(x['10 Yr']-real['10 YR'],2),'30y_nominal_minus_real':round(x['30 Yr']-real['30 YR'],2)})
for key,series,field,bar in [('30y',n,'30 Yr',5.0),('real10',r,'10 YR',2.5)]:
 ds=sorted(series);run=0
 for d in reversed(ds):
  if series[d][field]<bar:break
  run+=1
 summary[key+'_regime']={'basis':'Treasury 2026 file, published sessions >= threshold; missing dates skipped','threshold':bar,'n':len(ds),'days_ge':sum(series[d][field]>=bar for d in ds),'trailing_run':run}
p=json.loads((R/'fr2004.json').read_text())['series'];ds=sorted(set.intersection(*(set(x) for x in p.values())))
summary['dealer_rows']=[{'date':d,**{k:round(v[d],3) for k,v in p.items()},'total_long':round(sum(p[k][d] for k in ['7-11Y','11-21Y','>21Y']),3)} for d in ds[-4:]]
bs=[]
for row in csv.reader((R/'bund10.csv').open(encoding='utf-8-sig')):
 try:dt.date.fromisoformat(row[0]);v=float(row[1])
 except (ValueError,IndexError):continue
 bs.append((row[0],v))
summary['bund_evals']=[{'date':d,'value':v,'prior5':bs[i-5][0],'delta_bp':round((v-bs[i-5][1])*100,6),'met':v>3.25 and (v-bs[i-5][1])*100>17} for i,(d,v) in enumerate(bs) if d>='2026-10-20' and i>=5]
sh=xlrd.open_workbook(str(R/'ACM.xls')).sheet_by_name('ACM Daily');hdr=sh.row_values(0); acm={}
for i in range(1,sh.nrows):
 row=sh.row_values(i)
 try:d=dt.datetime.strptime(row[0],'%d-%b-%Y').date().isoformat()
 except (ValueError,TypeError):continue
 acm[d]={k:row[hdr.index(k)] for k in ['ACMY10','ACMTP10','ACMRNY10']}
summary['acm_frontier']=max(acm);summary['acm_oct16_to_latest']={k:round((acm[max(acm)][k]-acm['2026-10-16'][k])*100,6) for k in ['ACMY10','ACMTP10','ACMRNY10']}
summary['acm_latest']=acm[max(acm)]
meetings=parse_fomc_calendar((R/'fomc_calendar.html').read_text())
print('MEETINGS',meetings)
# Freeze event study definition: FOMC decision-day delta(30Y-2Y), same-day minus prior published session; >0 steepens; <=0 does not.
base=[]
for dd in meetings:
 d=dd.isoformat() if hasattr(dd,'isoformat') else str(dd)
 if not ('2026-01-01'<=d<='2026-10-28') or d not in n:continue
 prior=max(t for t in n if t<d)
 delta=round(((n[d]['30 Yr']-n[d]['2 Yr'])-(n[prior]['30 Yr']-n[prior]['2 Yr']))*100,6)
 base.append({'decision':d,'prior':prior,'delta_2s30s_bp':delta,'steepens':delta>0})
summary['fomc_2026_base_rate']={'definition':'2s30s decision-day close minus prior published session; >0bp = steepens; <=0 = does not; all completed 2026 meetings incl 10-28, Treasury primary','events':base,'n':len(base),'steepens':sum(x['steepens'] for x in base)}
(H/'derived.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
