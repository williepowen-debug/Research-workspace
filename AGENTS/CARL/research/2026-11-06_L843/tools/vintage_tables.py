#!/usr/bin/env python3
"""Consumer-automotive delinquency by origination year, matched by age, from the Q3 and year-end filings. Run from sources/."""
import re
def rows(fn):
    L=open(fn+'.htm.txt').read().split('\n')
    i=next(k for k,l in enumerate(L) if 'amortized cost basis of our consumer finance receivables and loans by credit quality' in l)
    hdr=None;out={}
    for k in range(i,i+16):
        l=L[k]
        m=re.match(r'\t?(20\d\d)\t(20\d\d)\t(20\d\d)\t(20\d\d)\t(20\d\d)',l)
        if m and hdr is None: hdr=[int(x) for x in m.groups()]
        for lab,key in [('Current','cur'),('30–59','d30'),('60–89','d60'),('90 or more','d90'),('Total consumer automotive','tot')]:
            if l.startswith(lab) and key not in out:
                nums=[int(x.replace(',','')) for x in re.findall(r'\d[\d,]*',l.split('\t',1)[1]) ]
                out[key]=nums
    return hdr,out
D={}
for fn,date in [('ally-20230930','2023-09-30'),('ally-20231231','2023-12-31'),('ally-20240930','2024-09-30'),('ally-20241231','2024-12-31'),('ally-20250930','2025-09-30'),('ally-20251231','2025-12-31'),('ally-20260930','2026-09-30')]:
    h,o=rows(fn)
    for j,y in enumerate(h):
        D[(y,date)]={k:o[k][j] for k in o}
    print(date,h,'tot',o['tot'][:5],'d60',o['d60'][:5],'d90',o['d90'][:5])
print('\nvintage\tdate\tage_label\tbal\t30+%\t60+%\t90+%')
for v in (2022,2023,2024,2025,2026):
    for d in sorted({k[1] for k in D}):
        if (v,d) in D:
            r=D[(v,d)]; y=int(d[:4]); lab=f"{'Sep' if d[5:7]=='09' else 'Dec'} Y+{y-v}"
            print(v,d,lab,r['tot'],round(100*(r['d30']+r['d60']+r['d90'])/r['tot'],2),round(100*(r['d60']+r['d90'])/r['tot'],2),round(100*r['d90']/r['tot'],2),sep='\t')
