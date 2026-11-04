import pathlib,json,sys,importlib.util,subprocess,csv
from decimal import Decimal
p=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('new','AGENTS/LIQUID/scripts/gate069_legs.py'); new=importlib.util.module_from_spec(s);s.loader.exec_module(new)
old={ '__name__':'old_grade' }; exec(compile(subprocess.check_output(['git','show','0ef2c3def:AGENTS/LIQUID/scripts/gate069_legs.py'],text=True),'old','exec'),old)
def data(k,m=100):
 r=json.loads((p/(k+'.json')).read_text()); assert not r.get('error') and not r['short'] and not r['missing'],r
 ds=[x['date'] for x in r['rows']];assert len(ds)==len(set(ds))
 return {x['date']:int(Decimal(x['value'])*m) for x in r['rows']}
hy=data('BAMLH0A0HYM2');ig=data('BAMLC0A0CM');bb=data('BAMLH0A1HYBB');ccc=data('BAMLH0A3HYC');b=data('BAMLH0A2HYB')
raw=json.loads((p/'raw_closes.json').read_text());eq={t:{d:round(v,2) for d,v in raw[t].items()} for t in new.TICK}
(p/'published_cent_closes.json').write_text(json.dumps(eq,indent=2)+'\n')
changes=[];audit=[];synthetic_misses=0
for n in range(1,2992):
 a=round(n*.20,2);z=round(n*.17,2)
 prices={t:{'2026-10-29':a,'2026-10-30':z} for t in new.TICK};h={'2026-10-29':326,'2026-10-30':331}
 r0=old['grade_l4'](h,prices);r1=new.grade_l4(h,prices)
 assert r1['state']=='FIRED',(n,r1)
 synthetic_misses+=r0['state']!='FIRED'
for d in sorted(hy):
 if d<'2026-09-04':continue
 h={k:v for k,v in hy.items() if k<=d};r0=old['grade_l4'](h,eq);r1=new.grade_l4(h,eq)
 if r1['state']=='INSTRUMENT-FAULT': audit.append({'date':d,'old':r0['state'],'new':r1['state'],'faults':r1['faults']});continue
 prev=r1['hprev']
 # Oracle is integer cents, independently of the patched Decimal comparison and displayed float.
 oracle=any(round(eq[t][d]*100)*100<=round(eq[t][prev]*100)*85 for t in new.TICK) and hy[d]-hy[prev]>=5
 assert (r1['state']=='FIRED')==oracle,(d,r1)
 row={'date':d,'old':r0['state'],'new':r1['state'],'hy_change':r1['hy_chg'],'worst':r1['worst'],'equity_hit':r1['eq_hit']}
 audit.append(row)
 if r0['state']!=r1['state']:changes.append(row)
(p/'boundary_impact.json').write_text(json.dumps({'historical_comparison_from':'2026-09-04','last':max(hy),'sessions':len(audit),'changed_actual_results':changes,'synthetic_misses_of_2991':synthetic_misses,'limit':'Retrieved vendor raw historical closes normalized to published cents. Not immutable original seen-price census. Any pre-adoption or missing coverage excluded.','rows':audit},indent=2)+'\n')
print('Historical audited',len(audit),'changed',len(changes),'synthetic misses',synthetic_misses,'of 2991')
rows=[]
for d in sorted(hy):
 if d<'2026-10-29':continue
 h={k:v for k,v in hy.items() if k<=d}; c={k:v for k,v in ccc.items() if k<=d};q={k:v for k,v in bb.items() if k<=d}
 l1=new.grade_l1(q,c);l4=new.grade_l4(h,eq)
 run=0
 for day in sorted(h,reverse=True):
  if h[day]>320:run+=1
  else:break
 row={'date':d,'HY':hy[d],'IG':ig[d],'BB':bb[d],'B':b[d],'CCC':ccc[d],'HY_IG':hy[d]-ig[d],'HY_over320_count':run,'HY_kill_below260':hy[d]<260,'L1':l1,'L4_author_tested_only':l4,'072_price_fire':ig[d]>94 or hy[d]-ig[d]<180}
 rows.append(row)
 print(d,'HY/IG/BB/B/CCC',hy[d],ig[d],bb[d],b[d],ccc[d],'>320 run',run,'L1',l1['state'],'CCC5',l1.get('ccc_chg'),'L4',l4['state'],l4.get('worst'),'HYdd',l4.get('hy_chg'),'072',row['072_price_fire'])
(p/'credit_grades.json').write_text(json.dumps(rows,indent=2)+'\n')
# No rounding of source percentages before subtraction; compare whole basis points per letter.
fund={k:{x['date']:Decimal(x['value']) for x in json.loads((p/(k+'.json')).read_text())['rows']} for k in ['SOFR','SOFR1','SOFR99','SOFR75','IORB','EFFR','EFFR75','RPONTTLD']}
excluded={line.split('\t')[0] for line in pathlib.Path('AGENTS/LIQUID/workbook/GATE079_CALENDAR_EXCLUDED.tsv').read_text().splitlines()[1:]}
for d in sorted(fund['SOFR99']):
 if d<'2026-10-28':continue
 ib=fund['IORB'][d];tail=round((fund['SOFR99'][d]-ib)*100)
 print('FUNDING',d,'SOFR99-IORB',tail,'excluded',d in excluded,'SOFR-IORB',round((fund['SOFR'][d]-ib)*100),'99-1',round((fund['SOFR99'][d]-fund['SOFR1'][d])*100),'EFFR-IORB',round((fund['EFFR'][d]-ib)*100),'SRF',fund['RPONTTLD'].get(d))
