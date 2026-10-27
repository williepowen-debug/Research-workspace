"""Reproduce the October26 frozen data build. No network or recurring collector.
Run with repository .venv/bin/python3. Source IDs resolve in data/SOURCES.tsv.
"""
from pathlib import Path
import csv,json
import pandas as pd
import numpy as np
H=Path(__file__).resolve().parents[2]
R=H.parents[1]
D=Path(__file__).resolve().parent
S=D/'sources'
OLD=H/'research/2026-10-26_first-session/sources'
DATA=H/'data'
VINTAGE='CURRENT-2026-10-26'

def month(x):
    return pd.to_datetime(x).to_period('M').to_timestamp()

def date_short(x):
    # Avoid %y's 1969/2068 cutoff misplacing Philadelphia's 1968 observations in the future.
    a,b=str(x).split('-'); y=int(b); y += 2000 if y <= 26 else 1900
    return pd.to_datetime(f'{a}-{y}',format='%b-%Y')

def writer(name,frame,notes):
    p=DATA/name
    with p.open('w') as f:
        f.write('# FROZEN 2026-10-26 — historical current-vintage panel; live release truth is workbook/PRINTS.tsv.\n')
        for n in notes:f.write('# '+n+'\n')
        frame.to_csv(f,sep='\t',index=False,na_rep='UNKNOWN',float_format='%.9g',lineterminator='\n')

# Regions: one row per region/reference month; ONLY current seasonally adjusted diffusion indexes.
frames=[]
mapping={
 'NY':{'Headline':'GACDISA','New_Orders':'NOCDISA','Shipments':'SHCDISA','Employment':'NECDISA','Prices_Paid':'PPCDISA','Prices_Received':'PRCDISA'},
 'PHILLY':{'Headline':'GAC','New_Orders':'NOC','Shipments':'SHC','Employment':'NEC','Prices_Paid':'PPC','Prices_Received':'PRC'},
 'DALLAS':{'Headline':'bact','New_Orders':'vnwo','Shipments':'vshp','Employment':'nemp','Prices_Paid':'prm','Prices_Received':'pfg'},
 'RICHMOND':{'Headline':'sa_mfg_composite','New_Orders':'sa_mfg_new_orders_c','Shipments':'sa_mfg_ship_c','Employment':'sa_mfg_emp_c'},
}
for region in mapping:
    if region=='NY':
        f=pd.read_csv(S/'ny_history.csv',na_values=['ND']);dates=pd.to_datetime(f.surveyDate).dt.to_period('M').dt.to_timestamp()
    elif region=='PHILLY':
        f=pd.read_csv(S/'philly_history.csv');dates=f.DATE.map(date_short)
    elif region=='DALLAS':
        f=pd.read_excel(S/'dallas_history.xls');dates=f.date.map(date_short)
    else:
        f=pd.read_excel(OLD/'richmond_history.xlsx');dates=pd.to_datetime(f.date)
    out=pd.DataFrame({'Region':region,'Ref_Period':dates})
    for key,col in mapping[region].items():out[key]=pd.to_numeric(f[col],errors='coerce')
    out['Source_ID']='REG-'+region
    frames.append(out)
f=pd.read_excel(S/'kc_history.xlsx',header=None)
# Row2 has source month labels with arbitrary days, including Oct26; these are not publication dates.
cols=[c for c in range(1,len(f.columns)) if isinstance(f.iloc[2,c],pd.Timestamp) or hasattr(f.iloc[2,c],'year')]
# pandas returns Python datetime objects on this workbook, so preserve the separate generic date branch.
if not cols:cols=[c for c in range(1,len(f.columns)) if not pd.isna(f.iloc[2,c])]
out=pd.DataFrame({'Region':'KC','Ref_Period':[month(f.iloc[2,c]) for c in cols]})
for key,row in {'Headline':5,'Production':6,'Shipments':7,'New_Orders':8,'Employment':10,'Prices_Received':12,'Prices_Paid':13}.items():
    out[key]=pd.to_numeric(pd.Series([f.iloc[row,c] for c in cols]),errors='coerce')
out['Source_ID']='REG-KC';frames.append(out)
regions=pd.concat(frames,ignore_index=True).sort_values(['Ref_Period','Region'])
regions['Vintage']=VINTAGE;regions['SA']='SA';regions['Unit']='diffusion index points';regions['Basis']='PRIMARY-VERIFIED'
regions=regions[regions.Ref_Period<='2026-10-01']
assert not regions.duplicated(['Region','Ref_Period']).any()
latest=regions.groupby('Region').tail(1).set_index('Region')
for region,expected in {'NY':23.2,'PHILLY':4.3,'DALLAS':9.3,'KC':3,'RICHMOND':-6}.items():
    assert abs(float(latest.loc[region,'New_Orders'])-expected)<1e-8,(region,latest.loc[region,'New_Orders'])
writer('REGIONAL_MONTHLY.tsv',regions.assign(Ref_Period=regions.Ref_Period.dt.strftime('%Y-%m')),['All columns are current activity, never expectations. Richmond price columns UNKNOWN: issuer measures price growth differently, not a comparable diffusion index.','Dallas vnwo means volume of NEW orders; gro means growth RATE of orders and is excluded. KC current SA row8 is used, not NSA/year-ago/future rows.'])

wide=regions.pivot(index='Ref_Period',columns='Region',values='New_Orders').reindex(columns=['NY','PHILLY','RICHMOND','KC','DALLAS'])
breadth=wide.copy();breadth['Regions_Observed']=wide.notna().sum(axis=1)
# Partial panels retain all five source cells. Counts withheld unless all five exist.
breadth['Negative_Regions']=(wide<0).sum(axis=1).where(breadth.Regions_Observed==5)
breadth['Coverage']=np.where(breadth.Regions_Observed==5,'COMPLETE','PARTIAL')
breadth['Ref_Period']=breadth.index.strftime('%Y-%m')
writer('REGIONAL_BREADTH.tsv',breadth.reset_index(drop=True)[['Ref_Period','NY','PHILLY','RICHMOND','KC','DALLAS','Regions_Observed','Negative_Regions','Coverage']],['Same-month sign count of new-order diffusion indexes; no equal-weight national output average. Zero is measured, UNKNOWN is missing.','Current-vintage revisions; no historical first-release simulation; complete coverage starts with Dallas in June2004. October2026 is PARTIAL (4/5), never zero-negative-of-five.'])

# Existing frozen hard-data downloads become one reusable wide panel; source IDs map unit/basis separately.
series={}
for sid in ['INDPRO','IPMAN','TCU','DGORDER','NEWORDER','ANXAVS','AMTMNO','FRGSHPUSM649NCIS','RAILFRTCARLOADSD11','RAILFRTINTERMODALD11','IPG3341S','IPG3342S','IPG3344S','IPG3353S']:
    f=pd.read_csv(OLD/(sid+'.csv'),index_col=0,parse_dates=True)
    series[sid]=pd.to_numeric(f.iloc[:,0],errors='coerce')
hard=pd.DataFrame(series).sort_index()
hard['Ref_Period']=hard.index.strftime('%Y-%m')
writer('HARD_DATA_MONTHLY.tsv',hard.reset_index(drop=True)[['Ref_Period']+list(series)],['Source/units/SA/endpoints in SOURCES.tsv; each column is one source series, not additive across columns.','FRED MIRROR of issuer data, October26 current vintage. Missing histories are UNKNOWN; source-era and vintage differences remain.'])

# BEA quarter panel: use exact nonresidential rows, not residential Equipment with the same label.
bea={}
for sheet in ['T50301-Q','T50306-Q']:
    f=pd.read_excel(S/'bea_section5.xlsx',sheet_name=sheet,header=None)
    qcols=[c for c in range(3,len(f.columns)) if str(f.iloc[7,c]).startswith(('19','20'))]
    for label,line in [('NONRES-EQUIPMENT',9),('INFORMATION-PROCESSING',10),('COMPUTERS',11),('INDUSTRIAL-EQUIPMENT',13)]:
        matches=f.index[pd.to_numeric(f.iloc[:,0],errors='coerce').eq(line)].tolist()
        if not matches:continue
        row=matches[0]
        bea[label+('_QOQ_SAAR' if sheet=='T50301-Q' else '_REAL_LEVEL')]=pd.Series({str(f.iloc[7,c]):pd.to_numeric(f.iloc[row,c],errors='coerce') for c in qcols})
quarter=pd.DataFrame(bea).sort_index();quarter.insert(0,'Ref_Period',quarter.index)
assert len(quarter)>0 and '2026Q2' in quarter.index, 'BEA quarter/line extraction failed'
assert float(quarter.loc['2026Q2','NONRES-EQUIPMENT_QOQ_SAAR'])==13.4
assert float(quarter.loc['2026Q2','INFORMATION-PROCESSING_QOQ_SAAR'])==7.6
writer('EQUIPMENT_QUARTERLY.tsv',quarter.reset_index(drop=True),['BEA primary Section5All workbook; publishedSeptember30,2026. Table5.3.1 lines9/10/11/13 growth percent q/q SAAR.','Table5.3.6 same lines: millions chained2017USD SAAR. Chained components not additive. Full quarter latest2026Q2; cannot stand for2026Q3.'])

# Two consecutive eligible observations, refusing a join over a missing/calendar gap.
def consecutive_two(condition):
    prior=condition.shift(1)
    periods=condition.index.to_period('M').astype('int64')
    adjacent=pd.Series(np.r_[False,np.diff(periods)==1],index=condition.index)
    valid=condition.notna() & prior.notna() & adjacent
    return (condition.eq(True) & prior.eq(True)).where(valid)

def summary(condition):
    flag=consecutive_two(condition)
    q=flag.dropna().astype(bool)
    adjacent=pd.Series(np.r_[False,np.diff(q.index.to_period('M').astype('int64'))==1],index=q.index)
    starts=q & (~q.shift(1,fill_value=False) | ~adjacent)
    return {'eligible_pairs':len(q),'qualifying_pairs':int(q.sum()),'pair_frequency_pct':100*float(q.mean()) if len(q) else None,'episode_starts':int(starts.sum())}
# Meaningful failure/clean controls: missing panel/gapped calendar must not be scored calm or bridged.
control=pd.Series([True,np.nan,True,True],index=pd.date_range('2020-01-01',periods=4,freq='MS'))
assert consecutive_two(control).isna().iloc[:3].all() and bool(consecutive_two(control).iloc[3])
control=pd.Series([True,True],index=pd.to_datetime(['2020-01-01','2020-03-01']))
assert consecutive_two(control).isna().all()
assert pd.isna(breadth.loc['2026-10-01','Negative_Regions'])

samples={'FULL':None,'RECENT10Y':pd.Timestamp('2016-10-01'),'EX-PANDEMIC':None}
cal=[]
for metric,vals in [('CORE-CAPEX-YOY',series['NEWORDER'].pct_change(12,fill_method=None)*100),('CASS-SHIP-YOY',series['FRGSHPUSM649NCIS'].pct_change(12,fill_method=None)*100),('RAIL-CARLOADS-MONTHLY-YOY',series['RAILFRTCARLOADSD11'].pct_change(12,fill_method=None)*100)]:
    vals=vals.dropna()
    for sample,start in samples.items():
        v=vals[vals.index>=start] if start is not None else vals.copy()
        if sample=='EX-PANDEMIC':v=v[~v.index.to_series().between('2020-03-01','2021-06-01')]
        for bar in [0,-5]:
            condition=v.lt(bar);res=summary(condition)
            cal.append({'Metric':metric,'Sample':sample,'Start':str(v.index.min().date()),'End':str(v.index.max().date()),'Rule':f'y/y < {bar}% for 2 monthly observations','Months':len(v),'Monthly_Hits':int(condition.sum()),**res,'Basis':'current vintage, descriptive; not first-publication event probability'})
complete=breadth[breadth.Coverage=='COMPLETE'].Negative_Regions
for sample,start in samples.items():
    v=complete[complete.index>=start] if start is not None else complete.copy()
    if sample=='EX-PANDEMIC':v=v[~v.index.to_series().between('2020-03-01','2021-06-01')]
    for bar in [3,4]:
        condition=v.ge(bar);res=summary(condition)
        cal.append({'Metric':'REGIONAL-NEW-ORDER-BREADTH','Sample':sample,'Start':str(v.index.min().date()),'End':str(v.index.max().date()),'Rule':f'>= {bar}/5 negative regions for 2 complete monthly panels','Months':len(v),'Monthly_Hits':int(condition.sum()),**res,'Basis':'primary current-vintage five-region panel; no national growth/probability mapping'})
cal=pd.DataFrame(cal);writer('CALIBRATION.tsv',cal,['Research candidate counts only; no new threshold registered. FULL/RECENT10Y/EX-PANDEMIC use the same variable and revision basis.','Persistence unit is monthly observations, not agent sessions. EX-PANDEMIC removesMarch2020-June2021 and does not join across the gap. Episode starts may be left-censored at sample start.'])
report={'region_rows':len(regions),'regional_complete_months':len(complete),'first_complete_month':str(complete.index.min().date()),'last_complete_month':str(complete.index.max().date()),'regional_latest':breadth.tail(2).reset_index(drop=True).astype(object).where(breadth.tail(2).reset_index(drop=True).notna(),'UNKNOWN').to_dict('records'),'hard_months':len(hard),'hard_series':len(series),'equipment_quarters':len(quarter),'BEA_latest':quarter.tail(1).to_dict('records'),'calibration_rows':len(cal),'controls':'missing-region panel and calendar-gap refusal controls PASS; five latest regional new-order source checks PASS','partial_october_withheld':True}
(D/'BUILD_RESULT.json').write_text(json.dumps(report,indent=2,default=str,allow_nan=False));print(json.dumps(report,indent=2,default=str,allow_nan=False))
