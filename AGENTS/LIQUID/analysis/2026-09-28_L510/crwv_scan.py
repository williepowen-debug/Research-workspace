# usage: python crwv_scan.py DTCC_ZIP_DIR  (every live CoreWeave print, 2025-12-01..2026-09-25 scanned for L510 sign-continuity)
import zipfile,csv,io,sys,glob,os,datetime as dt
from collections import defaultdict
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/LIQUID/scripts')
import crwv_cds_grade as g
rows=[]
for f in sorted(glob.glob(sys.argv[1]+'/sec_*.zip')):
    try:
        z=zipfile.ZipFile(f); rs=list(csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]),encoding='utf-8',errors='replace')))
    except Exception as e:
        continue
    for i,x in g.crwv_rows(rs):
        try:
            n=float(x['Notional amount-Leg 1'].replace(',','').replace('+','')); c=float(x['Fixed rate-Leg 1']); U=float(x['Other payment amount'])/n
        except: continue
        fl=[]
        if '+' in x['Notional amount-Leg 1']: fl.append('CAP')
        if x['Non-standardized term indicator']!='FALSE': fl.append('NS')
        rows.append((x['Execution Timestamp'][:16],x['Expiration Date'],c,U,x['Notional amount-Leg 1'],','.join(fl),i))
seen=set();out=[]
for r in sorted(rows):
    if r[6] in seen: continue
    seen.add(r[6]); out.append(r)
for r in out: print(f"{r[0]} {r[1]} cpn{int(r[2]*1e4)} U={r[3]*100:6.2f}pt {r[4]:>11} {r[5]}")
print(len(out),"prints")
