"""Gold war/conflict descriptive windows. Fixed event list in METHOD.md."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import pandas as pd

P=Path(__file__).resolve().parent;DESK=P.parents[2]
gold_path=DESK/'gold/sources/2026-10-25_historical-comparison/gold_close_series.csv'
g=pd.read_csv(gold_path,index_col=0,parse_dates=True).close
assert g.index.is_unique and g.index.is_monotonic_increasing and (g>0).all()
events=[
 ('Georgia conflict escalation','2008-08-08','https://press.un.org/en/2008/sc9418.doc.htm','Night of August7-8; escalating conflict, not a clean isolated surprise.'),
 ('Crimea armed seizure','2014-02-27','https://www.ohchr.org/Documents/Countries/UA/Crimea2014_2017_EN.pdf','Chosen armed-seizure date, not March18 annexation; wider crisis predates date.'),
 ('Full-scale Ukraine invasion','2022-02-24','https://www.un.org/sites/un2.un.org/files/sg_annual_report_2023_en_0.pdf','February24 calendar date; substantial prior military buildup.'),
 ('Hamas attacks / Israel-Hamas conflict','2023-10-07','https://www.ochaopt.org/content/escalation-gaza-strip-and-israel-flash-update-1','Saturday event; first fund close MondayOctober9.'),
 ('Iran direct attack on Israel','2024-04-13','https://commonslibrary.parliament.uk/research-briefings/cbp-10002/','Saturday attack; first close MondayApril15; escalation, not a new independent war.'),
 ('Israel-Iran war','2025-06-13','https://dppa.dfs.un.org/en/israel-iran-crisis-un-chief-urges-calm-after-overnight-strikes','Local overnight June13; UN NewYork statement June12; first US session June13.'),
 ('US-Israeli strikes on Iran','2026-02-28','https://digitallibrary.un.org/record/4103823','Saturday start; first fund close MondayMarch2; ongoing current war.'),
]
rows=[];paths=[]
for name,date,url,notes in events:
 event=pd.Timestamp(date);i=g.index.searchsorted(event);base_i=i-1
 assert base_i>=21
 r={'event':name,'event_calendar_date':date,'baseline_date':str(g.index[base_i].date()),
    'baseline_GLD':float(g.iloc[base_i]),'first_session':str(g.index[i].date()),
    'pre21_start':str(g.index[base_i-21].date()),
    'pre21_return_pct':float(100*(g.iloc[base_i]/g.iloc[base_i-21]-1)),
    'chronology_primary':url,'notes':notes}
 for n in [1,5,21,63,126,252]:
  target=base_i+n
  if target<len(g):
   r[f'session{n}_date']=str(g.index[target].date())
   r[f'session{n}_return_pct']=float(100*(g.iloc[target]/g.iloc[base_i]-1))
  else:
   r[f'session{n}_date']='NOT_YET_OBSERVED';r[f'session{n}_return_pct']=None
 r['latest_date']=str(g.index[-1].date())
 r['latest_vs_baseline_pct']=float(100*(g.iloc[-1]/g.iloc[base_i]-1))
 for step in range(-21,min(252,len(g)-base_i-1)+1):
  ix=base_i+step
  paths.append({'event':name,'event_calendar_date':date,'relative_session':step,
                'date':str(g.index[ix].date()),'return_from_baseline_pct':float(100*(g.iloc[ix]/g.iloc[base_i]-1))})
 rows.append(r)
pd.DataFrame(rows).to_csv(P/'daily_conflict_event_returns.csv',index=False)
pd.DataFrame(paths).to_csv(P/'daily_event_paths.csv',index=False)

wb=P/'worldbank_monthly.xlsx'
raw=pd.read_excel(wb,sheet_name='Monthly Prices',header=4)
dates=raw.iloc[:,0].astype(str);mask=dates.str.fullmatch(r'\d{4}M\d{2}')
gold=pd.Series(pd.to_numeric(raw.loc[mask,'Gold'],errors='raise').to_numpy(),
               index=pd.PeriodIndex(dates.loc[mask].str.replace('M','-'),freq='M'),name='gold_usd_troy_oz').sort_index()
assert gold.index.is_unique and (gold>0).all()
gold.to_csv(P/'worldbank_monthly_gold.csv')
old=[('Arab-Israeli war','1973-10'),('Soviet invasion of Afghanistan','1979-12'),
     ('Iraq invasion of Kuwait','1990-08'),('Coalition Gulf War campaign','1991-01'),('Iraq invasion','2003-03')]
older=[]
for name,date in old:
 event=pd.Period(date,freq='M');base=event-1;bp=float(gold.loc[base])
 r={'event':name,'event_month':date,'baseline_month':str(base),'baseline_average_usd_oz':bp}
 for n in [0,3,6,12]:
  target=event+n;r[f'plus{n}_month']=str(target)
  r[f'plus{n}_average_usd_oz']=float(gold.loc[target])
  r[f'plus{n}_return_pct']=float(100*(gold.loc[target]/bp-1))
 older.append(r)
pd.DataFrame(older).to_csv(P/'older_conflict_monthly_average_comparisons.csv',index=False)
desc=pd.read_excel(wb,sheet_name='Description',header=None)
definition=[str(x) for x in desc.to_numpy().flatten() if str(x).startswith('Gold,')]
assert len(definition)==1,definition
mis=pd.read_excel(wb,sheet_name='Mismatch Details',header=3)
gold_mis=mis.loc[mis.astype(str).apply(lambda col:col.str.contains('Gold',case=False)).any(axis=1)]
gold_mis.to_csv(P/'publisher_mismatch_sheet_gold_entries.csv',index=False)

manifest={
 'created_at':datetime.now(timezone.utc).isoformat(),
 'gold_daily_input':str(gold_path.relative_to(DESK)),
 'gold_daily_sha256':hashlib.sha256(gold_path.read_bytes()).hexdigest(),
 'daily_endpoint':str(g.index[-1].date()),'modern_event_count':len(events),'older_monthly_case_count':len(old),
 'worldbank_update':'October02,2026 as workbook header; data through September2026',
 'worldbank_gold_definition':definition[0],
 'publisher_mismatch_sheet_gold_entry_count':len(gold_mis),
 'older_monthly_gold_definition_applies':'Pre-June2025 London afternoon fixing, average of daily rates; nominal USD/troy ounce',
 'urls':{
  'worldbank_landing':'https://www.worldbank.org/en/research/commodity-markets',
  'worldbank_monthly':'https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Historical-Data-Monthly.xlsx',
  'wgc':'https://www.gold.org/goldhub/gold-focus/2026/03/weekly-markets-monitor-crisis-hedge',
  'wgc_pdf':'https://www.gold.org/download/file/20583/WMM_2_March_Crisis_Hedge.pdf',
  'bis':'https://www.bis.org/publications/working-paper-1380-chasing-el-dorado-gold-under-shifting-geopolitical-and-financial-condition',
  'bis_pdf':'https://www.bis.org/publications/working-paper-1380-chasing-el-dorado-gold-under-shifting-geopolitical-and-financial-condition.pdf',
  'lbma':'https://www.lbma.org.uk/alchemist/issue-30/not-just-another-war-story',
  'gold_convertibility':'https://www.federalreservehistory.org/essays/gold-convertibility-ends',
  'war1973':'https://history.state.gov/milestones/1969-1976/arab-israeli-war-1973',
  'war1979':'https://history.state.gov/milestones/1977-1980/soviet-invasion-afghanistan',
  'gulf1990_1991':'https://history.state.gov/milestones/1989-1992/gulf-war'},
 'captures':{fn:hashlib.sha256((P/fn).read_bytes()).hexdigest() for fn in [
  'worldbank_monthly.xlsx','worldbank_commodity_landing.html','BIS_wp1380.pdf','WGC_20260302.pdf','LBMA_gulf_wars.html']},
 'limits':['selected examples, not war census','later returns reflect all shocks; no war-only causal attribution',
           'monthly average ratios are not daily close-to-close returns','2026 252-session result right-censored',
           '1990/1991 stages and recent MiddleEast events overlap; no independent event odds'],
}
(P/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('DAILY');print(pd.DataFrame(rows)[['event','pre21_return_pct']+[f'session{n}_return_pct' for n in [1,5,21,63,126,252]]].round(3).to_string(index=False))
print('MONTHLY AVERAGES');print(pd.DataFrame(older)[['event','baseline_month']+[f'plus{n}_return_pct' for n in [0,3,6,12]]].round(3).to_string(index=False))
print('DATA LIMITS',json.dumps(manifest,indent=2))
