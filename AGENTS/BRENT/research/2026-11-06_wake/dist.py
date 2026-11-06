#!/usr/bin/env python3
"""Distillate stock, cover and flow arithmetic from EIA weekly history files. Days = stock / 4-week average product supplied (my arithmetic, EIA's method)."""
import xlrd,datetime as dt,sys
from pathlib import Path
H=Path(__file__).resolve().parent
def load(n):
    b=xlrd.open_workbook(H/f'{n}w.xls');s=b.sheet_by_index(1)
    return {xlrd.xldate.xldate_as_datetime(s.cell_value(r,0),b.datemode).date():s.cell_value(r,1) for r in range(3,s.nrows) if s.cell_value(r,1)!=''}
st=load('WDISTUS1');ps=load('WDIUPUS2');ex=load('WDIEXUS2');pr=load('WDIRPUS2');im=load('WDIIMUS2')
print('latest',max(st),st[max(st)],'ps',max(ps),ps[max(ps)],'ex',max(ex),ex[max(ex)],'prod',max(pr),pr[max(pr)],'imp',max(im),im[max(im)])
d=sorted(ps);days={}
for i in range(3,len(d)):
    k=d[i]
    if k in st: days[k]=st[k]/(sum(ps[x] for x in d[i-3:i+1])/4)
l=max(days);print('days latest',l,round(days[l],2),'4wk',sum(ps[x] for x in d[-4:])/4)
prior=[(k,v) for k,v in sorted(days.items()) if k<l and v<=days[l]]
print('last at/below',prior[-1] if prior else None,'n',len(prior))
print('lowest 5',[(str(k),round(v,1)) for k,v in sorted(days.items(),key=lambda x:x[1])[:5]])
y=[(k.year,round(v,1)) for k,v in days.items() if k.month==10 and 25<=k.day<=31]
print('late Oct days, lowest',sorted(y,key=lambda z:z[1])[:6])
print('2003 low days',[(str(k),round(v,1)) for k,v in days.items() if k.year==2003][10:20])
print('last 8 wks: stock chg, prod, imp, exp, ps')
for k in sorted(st)[-8:]:
    p=[x for x in sorted(st) if x<k][-1]
    print(k,round(st[k]-st[p]),pr.get(k),im.get(k),ex.get(k),ps.get(k))
print('exports yoy',ex.get(dt.date(2026,10,30)),ex.get(dt.date(2025,10,31)))
e4=[ex[x] for x in sorted(ex)[-4:]];print('exports 4wk',sum(e4)/4,'yr ago',sum(ex[x] for x in sorted(ex) if dt.date(2025,10,10)<=x<=dt.date(2025,10,31))/4)
