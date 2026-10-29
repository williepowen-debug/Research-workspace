#!/usr/bin/env python3
"""BRT-31 data week 2026-10-23 (release 2026-10-28) from release-day saved EIA bytes.
Research only; no live feeds, state writes, threshold or trade authority.
"""
import datetime as dt,hashlib,json
from pathlib import Path
from decimal import Decimal,getcontext
import xlrd
getcontext().prec=40
D=Path(__file__).resolve().parent
P=D.parent/'2026-10-21_eia-oct21'

def series(path,key):
    book=xlrd.open_workbook(path)
    for sh in book.sheets():
        if sh.nrows<3 or key not in sh.row_values(1):continue
        c=sh.row_values(1).index(key);out={}
        for r in range(3,sh.nrows):
            x=sh.cell_value(r,0);v=sh.cell_value(r,c)
            if isinstance(x,(int,float)) and v!='':out[xlrd.xldate_as_datetime(x,book.datemode).date().isoformat()]=Decimal(str(v))
        return {'file':path.name,'sheet':sh.name,'column':c,'series':key,'title':sh.cell_value(2,c)},out
    raise ValueError('Missing exact series '+key)

basis,g=series(D/'psw01.xls','WGFUPUS2')
_,gprev=series(P/'psw01.xls','WGFUPUS2')
w=dt.date(2026,10,23)
cur=[(w-dt.timedelta(days=7*k)).isoformat() for k in range(4)]
base=[(dt.date.fromisoformat(x)-dt.timedelta(days=364)).isoformat() for x in cur]
cs=sum(g[k] for k in cur);bs=sum(g[k] for k in base);yoy=(cs/bs-1)*100
# revisions vs the 10/21-captured workbook (recorded, never re-grade)
rev={k:{'prior_capture':str(gprev[k]),'this_capture':str(g[k])} for k in cur[1:]+base if k in gprev and gprev[k]!=g[k]}
pb,p=series(D/'eia-retail.xls','EMM_EPMR_PTE_NUS_DPG')
pc='2026-10-26';pbd=(dt.date.fromisoformat(pc)-dt.timedelta(days=364)).isoformat()
py=(p[pc]/p[pbd]-1)*100 if pc in p and pbd in p else None
sha={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(D.iterdir()) if f.suffix in ('.xls','.csv','.txt')}
res={'data_week':w.isoformat(),'release':'2026-10-28','capture':'release-day ir.eia.gov current files, 2026-10-28T23:48-04:00',
 'gasoline_basis':basis,'current_rows':{k:str(g[k]) for k in cur},'base_rows':{k:str(g[k]) for k in base},
 'current_avg':str(cs/4),'base_avg':str(bs/4),'yoy_pct':str(yoy),'qualifying_volume_week':yoy<=Decimal('-1.5'),
 'revisions_vs_prior_capture':rev,
 'price_basis':pb,'price_current':{pc:str(p.get(pc))},'price_base':{pbd:str(p.get(pbd))},'price_yoy_pct':None if py is None else str(py),
 'price_below_20':None if py is None else bool(py<20),'latest_retail_date':max(p),'sha256':sha}
print(json.dumps(res,indent=1))
json.dump(res,open(D/'evaluation.json','w'),indent=1)
