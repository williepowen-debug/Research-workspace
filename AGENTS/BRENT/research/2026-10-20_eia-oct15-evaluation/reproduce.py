#!/usr/bin/env python3
"""Reproduce the dated October15 WPSR/BRT31 evaluation from saved primary bytes.
Research only; no live feeds, state writes, monitor, threshold or trade authority.
"""
import csv,datetime as dt,hashlib,io,json,re
from pathlib import Path
from decimal import Decimal,getcontext
import xlrd
getcontext().prec=40
D=Path(__file__).resolve().parent

def series(filename,key):
    book=xlrd.open_workbook(D/filename)
    for sh in book.sheets():
        if sh.nrows<3 or key not in sh.row_values(1):continue
        c=sh.row_values(1).index(key);out={}
        for r in range(3,sh.nrows):
            x=sh.cell_value(r,0);v=sh.cell_value(r,c)
            if isinstance(x,(int,float)) and v!='':out[xlrd.xldate_as_datetime(x,book.datemode).date().isoformat()]=Decimal(str(v))
        return {'file':filename,'sheet':sh.name,'column':c,'series':key,'title':sh.cell_value(2,c)},out
    raise ValueError('Missing exact series '+key)

def archived_gasoline(filename):
    rows=list(csv.reader(io.StringIO((D/filename).read_text(errors='replace'))))
    hits=[r for r in rows if r[:2]==['Product Supplied ','Finished Motor Gasoline']]
    assert len(hits)==1,(filename,len(hits))
    head=rows[0];row=hits[0]
    return {dt.datetime.strptime(head[i],'%m/%d/%y').date().isoformat():Decimal(row[i].replace(',','')) for i in [2,4]}

basis,g=series('psw01.xls','WGFUPUS2');w=dt.date(2026,10,9)
cur=[(w-dt.timedelta(days=7*k)).isoformat() for k in range(4)]
base=[(dt.date.fromisoformat(x)-dt.timedelta(days=364)).isoformat() for x in cur]
arch={}
for f in ['archive-table9.csv','archive-oct07-table9.csv','archive-sep30-table9.csv','archive-sep23-table9.csv']:arch.update(archived_gasoline(f))
assert set(cur+base)==set(arch)
assert all(g[k]==arch[k] for k in cur+base),'Do not accept a revised/current workbook as original'
cs=sum(g[k] for k in cur);bs=sum(g[k] for k in base);yoy=(cs/bs-1)*100
pb,p=series('eia-retail.xls','EMM_EPMR_PTE_NUS_DPG');price_current='2026-10-12';price_base=(dt.date.fromisoformat(price_current)-dt.timedelta(days=364)).isoformat();assert price_base=='2025-10-13'
py=(p[price_current]/p[price_base]-1)*100
# Independent source-format retrieval, same EIA measurement lineage, not a second survey.
text=(D/'eia-retail.html').read_text()
assert '2025-Oct' in text and '2026-Oct' in text
assert '3.061' in text and '4.331' in text
# Keep the closed policy test distinct from general diesel relief.
html=(D/'seds-gasoline.html').read_text()
shares={}
for name in ['North Carolina','United States','Indiana','Georgia','Ohio']:
    match=re.search(r'<th[^>]*>\s*'+re.escape(name)+r'\s*</th>(.*?)</tr>',html,re.S)
    assert match,name
    vals=re.findall(r'<td[^>]*>(.*?)</td>',match.group(1),re.S)
    nums=[re.sub('<[^>]*>','',v).strip().replace(',','') for v in vals]
    shares[name]=Decimal(nums[3])
ncshare=shares['North Carolina']/shares['United States']*100
assert ncshare<10
assert 'October 10, 2026' in (D/'nc-tax.html').read_text()
# Crude/product facts: exact WEEKLY series, never the duplicate 4-week-average key.
keys=['WCRRIUS2','WCRRIP32','WPULEUS3','W_NA_YUP_R30_PER','WDISTUS1','WDISTP11','WDISTP31','WDIEXUS2','WDIIMUS2','WDIRPUS2','WDIRPP32','WD0TP_NUS_2','WD0TP_R30_2','WDIUPUS2']
regional={}
book=xlrd.open_workbook(D/'psw09.xls')
for key in keys:
    for sh in book.sheets():
        if sh.nrows<3 or key not in sh.row_values(1):continue
        title=sh.cell_value(2,sh.row_values(1).index(key))
        if not title.startswith('Weekly '):continue
        j=sh.row_values(1).index(key);vals={}
        for i in range(3,sh.nrows):
            x=sh.cell_value(i,0)
            if not isinstance(x,(int,float)):continue
            date=xlrd.xldate_as_datetime(x,book.datemode).date().isoformat()
            if date in ['2026-10-02','2026-10-09']:vals[date]=Decimal(str(sh.cell_value(i,j)))
        regional[key]={'sheet':sh.name,'column':j,'title':title,'current':str(vals['2026-10-09']),'previous':str(vals['2026-10-02']),'change':str(vals['2026-10-09']-vals['2026-10-02'])};break
    assert key in regional,key
# Current release tables are byte-identical to the dated October15 issue.
assert (D/'current-table1.csv').read_bytes()==(D/'archive-table1.csv').read_bytes()
assert (D/'current-table9.csv').read_bytes()==(D/'archive-table9.csv').read_bytes()
# Recompute the weekly distillate identity change in kb/d; no rounded prose arithmetic.
rr=regional
balance_delta=sum(Decimal(rr[k]['change'])*sign for k,sign in [('WDIRPUS2',1),('WDIIMUS2',1),('WDIEXUS2',-1),('WDIUPUS2',-1)])
assert balance_delta==Decimal('-356.0')

# These are facts for the registered first week, not a final MET/NOT MET grade.
result={'week':'2026-10-09','release':'2026-10-15','publication_validation':'Current psw01 exact 8 weekly values match primary dated archived weekly-release rows; not a release-day local XLS capture. No matching gasoline erratum identified; inspected errata is dated2023. All are one EIA lineage.','gasoline_basis':basis,'current_rows':{x:str(g[x]) for x in cur},'base_rows':{x:str(g[x]) for x in base},'current_sum':str(cs),'base_sum':str(bs),'current_average':str(cs/4),'base_average':str(bs/4),'yoy_pct':str(yoy),'rounded_pair_yoy_pct':str((Decimal(8678)/Decimal(8713)-1)*100),'price_basis':pb,'price_current':{price_current:str(p[price_current])},'price_base':{price_base:str(p[price_base])},'price_yoy_pct':str(py),'below_20_price_count':int(py<20),'qualifying_volume_week':yoy<=Decimal('-1.5'),'qualifying_volume_streak':0,'result':'OPEN; first week NON-QUALIFYING; no terminal event','confidence':'40% unchanged','north_carolina_share_basis':'EIA SEDS2024F TableF15 total motor gasoline thousand barrels','seds_totals':{x:str(v) for x,v in shares.items()},'north_carolina_share_pct':str(ncshare),'contamination':'NC gasoline excise suspension effective10/10 is within window, but NC alone below10%. GA9/29, OH10/4 and INcontinuing8/7 suspension predate10/9; not silently counted as new in-window actions. No >=10% in-window state coverage or federal gasoline-excise cut established in bounded search. Exhaustive50state absence NOT certified; recheck before terminal NOT MET. Diesel-only relief is not gasoline-excise contamination.','regional_weekly':regional,'distillate_balance_change_kbd':str(balance_delta),'invariants':{'archived_weekly_rows_match_psw01':True,'exact_364_day_price_map':True,'no_rounded_average_substitution':True,'no_pre_window_volume_week_imported':True,'no_terminal_grade_after_one_week':True,'no_trade_action':True}}
print(json.dumps(result,indent=2))
