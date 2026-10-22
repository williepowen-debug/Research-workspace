#!/usr/bin/env python3
"""Reproduce the December-crack path odds in REPORT.md from daily-vendor.json (vendor daily closes, EST).
Research only; not a forecast, threshold or grade."""
import json,math,statistics as st
from pathlib import Path
d=json.load(open(Path(__file__).resolve().parent/'daily-vendor.json'))
days=sorted(x for x in set(d['HOZ26.NYM'])&set(d['CLZ26.NYM']) if x<'2026-10-21')
cr=[d['HOZ26.NYM'][x][0]*42-d['CLZ26.NYM'][x][0] for x in days]
H=21; D=95.04790847983-90.16
emp=[(min(cr[i+1:i+H+1])-cr[i])<=-D for i in range(len(cr)-H)]
ch=[cr[i]-cr[i-1] for i in range(1,len(cr))]
phi=lambda z:0.5*(1+math.erf(z/math.sqrt(2)))
print('empirical',sum(emp),'/',len(emp))
for n in (len(ch),60,20):
    s=st.pstdev(ch[-n:]); print(n,'sd',round(s,3),'next',round(phi(-D/s),3),'by 11/19',round(2*phi(-D/(s*math.sqrt(H))),3))
print('days below 90.16:',sum(v<90.16 for v in cr),'of',len(cr))
