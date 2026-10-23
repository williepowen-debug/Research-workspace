# L546 edge test (WATT 2026-10-23). Run from repo root: python3 AGENTS/WATT/sources/2026-10-23/test_l546_demand_pct.py
import sys; sys.path.insert(0,"AGENTS/WATT"); import power_watch as pw
def fake(latest,peak):
    rows=[{"date":"L","value":str(latest)}]+[{"date":f"h{i}","value":str(peak if i==0 else max(peak-1000,0))} for i in range(25)]
    pw.fetch.eia_pjm_demand=lambda hours=26: rows
    pct=pw.read_pjm_demand()[4]; return pct, f"{pct:.1f}", pct>=pw.NEAR_PEAK_PCT
cases=[("AC2 exact 95.000",95000,100000,True),("AC3 94.96 prints 95.0",94960,100000,True),
       ("AC4 94.94",94940,100000,False),("97 exact",97000,100000,True),("AC5 peak0",0,0,False)]
fails=0
for k,a,b,exp in cases:
    pct,disp,hint=fake(a,b); ok=(hint==exp) and (disp==f"{pct:.1f}") and pct==float(disp)
    fails+= not ok; print(f"{k}: pct={pct} printed={disp} hint={hint} expect={exp} {'PASS' if ok else 'FAIL'}")
print("fails",fails)
