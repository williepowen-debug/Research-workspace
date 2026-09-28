# usage: python accrued_test2.py DTCC_ZIP_DIR  (sec_YYYY_MM_DD.zip files; L510 accrued-treatment test: does DTCC UFRO jump by the accrued at a coupon date?)
import zipfile,csv,io,sys,statistics as st,datetime as dt
from collections import defaultdict
D=dt.date
def imm_prev(d):
    c=[]
    for y in (d.year-1,d.year):
        for m in (3,6,9,12):
            x=D(y,m,20)
            while x.weekday()>=5: x+=dt.timedelta(1)
            c.append(x)
    return max(x for x in c if x<=d)
def load(day):
    z=zipfile.ZipFile(f"{sys.argv[1]}/sec_{day}.zip")
    return list(csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]),encoding='utf-8',errors='replace')))
def prints(day):
    out=defaultdict(list)
    for x in load(day):
        if x['Action type']!='NEWT' or x['Other payment type']!='UFRO': continue
        if x['Non-standardized term indicator']!='FALSE' or x['Package indicator'] not in ('FALSE','false',''): continue
        if x['Notional currency-Leg 1']!='USD': continue
        uid=(x['Underlier ID-Leg 1'] or '')+'|'+(x['Underlying Asset Name'] or '')
        if uid=='|': continue
        try:
            n=float(x['Notional amount-Leg 1'].replace(',','').replace('+','')); c=float(x['Fixed rate-Leg 1'])
            U=float(x['Other payment amount'])/n
        except: continue
        if c not in (0.01,0.05) or not x['Expiration Date'].endswith('-20'): continue
        tr=D.fromisoformat(x['Execution Timestamp'][:10])
        if tr.isoformat().replace('-','_')!=day: continue   # same-day executions only
        a=c*((tr+dt.timedelta(1))-imm_prev(tr)).days/360
        out[(uid,x['Expiration Date'],c)].append((U,a))
    return out
def cmp(label,d1,d2):
    A=prints(d1);B=prints(d2)
    for c in (0.01,0.05):
        ks=[k for k in A if k in B and k[2]==c]
        # exclude near-zero upfronts where |.| folds
        ks=[k for k in ks if min(st.median(u for u,_ in A[k]),st.median(u for u,_ in B[k]))>2.5*c*90/360]
        if not ks: continue
        dU=[abs(st.median(u for u,_ in B[k])-st.median(u for u,_ in A[k])) for k in ks]
        da=[abs(st.median(a for _,a in B[k])-st.median(a for _,a in A[k])) for k in ks]
        print(f"{label:34s} cpn {int(c*1e4)}: n={len(ks):3d} | median |dU| {st.median(dU)*100:.3f}pt | accrued reset |da| {st.median(da)*100:.3f}pt | "
              f"share |dU| within +-35% of |da|: {sum(abs(x-y)<=0.35*y for x,y in zip(dU,da))/len(ks) if st.median(da)>0 else float('nan'):.2f}")
cmp("PLACEBO 9/16 vs 9/18 (no coupon)","2026_09_16","2026_09_18")
cmp("PLACEBO 9/22 vs 9/24 (no coupon)","2026_09_22","2026_09_24")
cmp("COUPON 9/18 vs 9/22","2026_09_18","2026_09_22")
cmp("COUPON 9/17 vs 9/23","2026_09_17","2026_09_23")
cmp("PLACEBO 6/16 vs 6/18","2026_06_16","2026_06_18")
cmp("COUPON 6/18 vs 6/23","2026_06_18","2026_06_23")
cmp("COUPON 6/17 vs 6/24","2026_06_17","2026_06_24")
print("--- SIGNED change of the reported (unsigned) value, cpn 100, |U|>0.6pt both days ---")
def signed(label,d1,d2,c=0.01,lo=0.006):
    A=prints(d1);B=prints(d2)
    ks=[k for k in A if k in B and k[2]==c and min(st.median(u for u,_ in A[k]),st.median(u for u,_ in B[k]))>lo]
    d=sorted((st.median(u for u,_ in B[k])-st.median(u for u,_ in A[k]))*100 for k in ks)
    bins=[-9,-0.5,-0.35,-0.15,-0.05,0.05,0.15,0.35,0.5,9]
    h=[sum(bins[i]<=x<bins[i+1] for x in d) for i in range(len(bins)-1)]
    print(f"{label:30s} n={len(d):3d} median {st.median(d):+.3f}pt mean {st.mean(d):+.3f} | hist {h}  (bins {bins[1:-1]})")
signed("PLACEBO 9/16->9/18","2026_09_16","2026_09_18")
signed("COUPON 9/18->9/22","2026_09_18","2026_09_22")
signed("COUPON 9/17->9/22","2026_09_17","2026_09_22")
signed("PLACEBO 9/22->9/23","2026_09_22","2026_09_23")
signed("COUPON 6/18->6/23","2026_06_18","2026_06_23")
signed("PLACEBO 6/23->6/24","2026_06_23","2026_06_24")
