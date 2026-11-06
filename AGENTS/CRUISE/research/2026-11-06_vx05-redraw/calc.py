#!/usr/bin/env python3
"""VX-CRU-05 redraw: NCLH net leverage and deposits against capacity, by quarter-end.
Inputs transcribed from NCLH earnings Ex-99.1 and cross-checked by the asserts below. USD millions."""
import json, math, pathlib, sys
RAW=pathlib.Path(sys.argv[1])  # scratch directory holding companyfacts.json from pull.py
ATS={'2022-12':2516.521,'2023-03':3177.026,'2023-06':3345.767,'2023-09':2965.280,'2023-12':3060.666,'2024-03':3629.707,
     '2024-06':3779.119,'2024-09':3144.586,'2024-12':3105.964,'2025-03':3762.256,'2025-06':3833.775,'2025-09':3146.869,
     '2025-12':3200.593,'2026-03':3718.873,'2026-06':3651.201,'2026-09':3141.976}
CAP={'2022-12':5035367,'2023-03':5415547,'2023-06':5513288,'2023-09':5820448,'2023-12':5903305,'2024-03':5841015,
     '2024-06':5736385,'2024-09':6033707,'2024-12':5834290,'2025-03':5700563,'2025-06':6052273,'2025-09':6417724,
     '2025-12':6263064,'2026-03':6392969,'2026-06':6589740,'2026-09':6766454}
# (net debt, trailing 12-month Adj EBITDA, company-printed leverage)
LEV={'2023-12':(13656.510,1860.731,'7.3x'),'2024-03':(13189.703,2090.479,'6.3x'),'2024-06':(12844.463,2163.374,'5.9x'),
     '2024-09':(13072.682,2342.302,'5.58x'),'2024-12':(12909.725,2450.804,'5.27x'),'2025-03':(13809.422,2439.887,'5.66x'),
     '2025-06':(13579.396,2546.265,'5.3x'),'2025-09':(14354.660,2634.523,'5.4x'),'2025-12':(14396.283,2730.226,'5.3x'),
     '2026-03':(14969.825,2810.050,'5.3x'),'2026-06':(14816.685,2781.518,'5.3x'),'2026-09':(14829.995,2699.038,'5.5x')}
# cross-checks: capacity quarters sum to the printed year-to-date totals
assert CAP['2026-03']+CAP['2026-06']+CAP['2026-09']==19749163
assert CAP['2025-03']+CAP['2025-06']+CAP['2025-09']+CAP['2025-12']==24433624
assert CAP['2024-03']+CAP['2024-06']+CAP['2024-09']+CAP['2024-12']==23445397
# cross-check: deposits against XBRL ContractWithCustomerLiabilityCurrent (independent path, same issuer)
f=json.load(open(RAW/'companyfacts.json'))['facts']['us-gaap']['ContractWithCustomerLiabilityCurrent']['units']['USD']
x={v['end'][:7]:v['val']/1e6 for v in f if v.get('form') in('10-Q','10-K')}
for k,v in ATS.items():
    if k in x: assert abs(x[k]-v)<0.6,(k,x[k],v)
def prev(k):
    y,m=k.split('-'); return f"{int(y)-1}-{m}"
def nxt(k):
    y,m=map(int,k.split('-')); m+=3
    if m>12: y+=1;m-=12
    return f"{y}-{m:02d}"
def lev_leg(printed):
    v=round(float(printed.rstrip('x')),1)
    return 1 if v<=4.9 else 2 if v<=5.4 else 3 if v<=5.9 else 4
def dep_leg(g):
    return 1 if g>=0 else 2 if g>=-3 else 3 if g>=-8 else 4
NAME={1:'GREEN',2:'YELLOW',3:'ORANGE',4:'RED'}
row=[]
for k in sorted(ATS):
    if prev(k) not in ATS: continue
    a=(ATS[k]/ATS[prev(k)]-1)*100; c=(CAP[k]/CAP[prev(k)]-1)*100; g=round(a-c,2)
    nx=None
    n=nxt(k)
    if n in CAP and prev(n) in CAP: nx=a-(CAP[n]/CAP[prev(n)]-1)*100
    r=dict(q=k,ats=ATS[k],ats_yoy=round(a,2),cap_yoy=round(c,2),gap=g,gap_next_q_cap=None if nx is None else round(nx,2),dep_leg=dep_leg(g))
    if k in LEV:
        nd,e,p=LEV[k]; r.update(net_debt=nd,ttm_ebitda=e,printed=p,computed=round(nd/e,2),lev_leg=lev_leg(p))
        r['row']=math.ceil((r['lev_leg']+r['dep_leg'])/2); r['row_name']=NAME[r['row']]
    row.append(r)
# forward arithmetic for the next print, 12/31/26. ESTIMATE, not a company figure.
nd=14829.995; fy=2550.0; q4=414.0
ttm=2699.038
nine=fy-q4; q4_25=ttm-nine
capex=1100+100; ocf_flat=2089.7-1706.36
base=nd+capex-ocf_flat
fwd=dict(implied_9m_2026=round(nine,1),implied_q4_2025=round(q4_25,1),unchanged_net_debt_lev=round(nd/fy,2),
         q4_capex=capex,q4_ocf_flat=round(ocf_flat,1),net_debt_est=round(base,1),net_debt_rise=round(base-nd,1),base_lev=round(base/fy,2),
         net_debt_at_6x=fy*5.95,rise_needed_to_print_6_0=round(fy*5.95-nd,1))
# CRU-13 hit level as a deposit-leg reading: capacity for Q4-26 is not disclosed, so show the gap for a range
d=[]
for cap_g in (2,4,6,8):
    for ats in (3100.0,3200.593,3264.6,3350.0):
        a=(ats/3200.593-1)*100; d.append(dict(cap_yoy=cap_g,ats=ats,ats_yoy=round(a,2),gap=round(a-cap_g,2),leg=NAME[dep_leg(a-cap_g)]))
combos={f"{NAME[l]}/{NAME[g]}":NAME[math.ceil((l+g)/2)] for l in NAME for g in NAME}
out=dict(rows=row,forward=fwd,dep_sensitivity=d,combos=combos)
pathlib.Path('calculations.json').write_text(json.dumps(out,indent=1))
for r in row:
    print(r['q'],f"{r['ats']:9.1f} ats {r['ats_yoy']:+6.2f} cap {r['cap_yoy']:+6.2f} gap {r['gap']:+7.2f} nextq {r['gap_next_q_cap']}",r.get('printed'),r.get('computed'),'L',r.get('lev_leg'),'D',r['dep_leg'],r.get('row_name'))
print(fwd); print(combos)
