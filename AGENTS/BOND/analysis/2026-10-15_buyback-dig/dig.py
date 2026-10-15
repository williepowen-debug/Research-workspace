"""BOND 2026-10-15 buyback dig: per-op accepted CUSIPs, yield paid (street convention, clean price),
spread vs Treasury par curve interpolated at the same maturity on the PRIOR official close,
cumulative retirement vs MSPD issued. Inputs in raw/ (FiscalData + Treasury CSVs)."""
import json,csv,datetime as dt,sys
from pathlib import Path
H=Path(__file__).parent; R=H/'raw'
ops={o['operation_date']+o['maturity_bucket']:o for o in json.load(open(R/'ops_all.json'))['data']}
det=json.load(open(R/'secdet_all.json'))['data']
D=lambda s:dt.date.fromisoformat(s)
def addm(d,m):
    y,mo=divmod(d.month-1+m,12); return dt.date(d.year+y,mo+1,min(d.day,28) if d.day>28 else d.day)
def ytm(clean,cpn,settle,mat):
    # coupon dates back from maturity
    cds=[mat]
    while cds[-1]>settle: cds.append(addm(cds[-1],-6))
    prev=cds[-1]; nxt=cds[-2]; future=sorted(c for c in cds if c>settle)
    w=(nxt-settle).days/(nxt-prev).days; ai=cpn/2*(settle-prev).days/(nxt-prev).days
    dirty=clean+ai; c=cpn/2
    def pv(y):
        return sum(c/(1+y/2)**(w+i) for i in range(len(future)))+100/(1+y/2)**(w+len(future)-1)
    lo,hi=0.0,0.2
    for _ in range(100):
        m=(lo+hi)/2
        if pv(m)>dirty: lo=m
        else: hi=m
    return m*100
# Treasury par curves 2025+2026
curve={}
for f in ['nominal.csv','nominal_2025.csv']:
    p=Path('/home/willi/Research-workspace/AGENTS/BOND/analysis/2026-10-15_post-PPI/raw')/f if f=='nominal.csv' else R/f
    if not p.exists(): continue
    for r in csv.DictReader(open(p)):
        m,d,y=r['Date'].split('/'); curve[dt.date(int(y),int(m),int(d))]=r
def par(day,years):
    ds=sorted(k for k in curve if k<day)  # PRIOR official close (op runs 13:40-14:00, before the close)
    r=curve[ds[-1]]
    pts=[(10,'10 Yr'),(20,'20 Yr'),(30,'30 Yr')]
    for (a,ka),(b,kb) in zip(pts,pts[1:]):
        if a<=years<=b:
            ya,yb=float(r[ka]),float(r[kb]); return ds[-1],ya+(yb-ya)*(years-a)/(b-a)
    return ds[-1],None
out=[]
want=sys.argv[1:] or ['2026-07-01','2026-09-10','2026-10-01','2026-10-15','2026-09-24','2026-10-08']
for od in want:
    rows=[r for r in det if r['operation_date']==od and float(r['par_amt_accepted'])>0]
    o=[v for k,v in ops.items() if k.startswith(od)][0]
    settle=D(o['settlement_date']); tot=float(o['total_par_amt_accepted'])
    print(f"\n== {od} {o['maturity_bucket']} accepted {tot/1e9:.3f}B of offered {float(o['total_par_amt_offered'])/1e9:.2f}B, {len(rows)}/{o['nbr_issues_eligible']} issues")
    for r in sorted(rows,key=lambda r:-float(r['par_amt_accepted'])):
        px=float(r['weighted_avg_accepted_price']); cpn=float(r['coupon_rate_pct']); mat=D(r['maturity_date'])
        y=ytm(px,cpn,settle,mat); yrs=(mat-settle).days/365.25; cd,pc=par(D(od),yrs)
        sp=(y-pc)*100 if pc else None
        a=float(r['par_amt_accepted'])
        line=f"   {r['cusip_nbr']} {cpn:5.3f} {r['maturity_date']} {a/1e6:7.0f}M ({a/tot*100:5.1f}%) px {px:7.3f} ytm {y:5.3f}  par@{yrs:4.1f}y {pc if pc is None else round(pc,3)} [{cd}]  spread {'' if sp is None else f'{sp:+5.1f}bp'}"
        print(line); out.append(dict(op=od,cusip=r['cusip_nbr'],cpn=cpn,mat=r['maturity_date'],par=a,px=px,ytm=round(y,4),par_interp=pc,spread_bp=sp))
json.dump(out,open(H/'derived.json','w'),indent=1)

# ---- timing-corrected summary: three curve bases per op (prior close, vendor-adjusted op window, same-day close)
vw=json.load(open(R/'vendor_opwindow.json'))
def par_on(day,years,same=False):
    ds=sorted(k for k in curve if (k<=day if same else k<day))
    if same and ds[-1]!=day: return None
    r=curve[ds[-1]]; pts=[(10,'10 Yr'),(20,'20 Yr'),(30,'30 Yr')]
    for (a,ka),(b,kb) in zip(pts,pts[1:]):
        if a<=years<=b: ya,yb=float(r[ka]),float(r[kb]); return ya+(yb-ya)*(years-a)/(b-a)
print("\n== TIMING-CORRECTED par-weighted spread of yield paid over the interpolated par curve (bp)")
print("   op          bucket       prior-close  vendor-move  op-window-adj  same-day-close")
summary=[]
for od in want:
    o=[v for k,v in ops.items() if k.startswith(od)][0]; rows=[x for x in out if x['op']==od]
    tot=sum(x['par'] for x in rows)
    tnx=vw[f'^TNX {od}']['move_bp']; tyx=vw[f'^TYX {od}']['move_bp']
    mv=(tnx+tyx)/2 if o['maturity_bucket']=='10Y to 20Y' else tyx
    sp_prior=sum(x['spread_bp']*x['par'] for x in rows)/tot
    sd=[]
    for x in rows:
        yrs=(D(x['mat'])-D(o['settlement_date'])).days/365.25; p=par_on(D(od),yrs,same=True)
        sd.append(None if p is None else (x['ytm']-p)*100)
    sp_same=None if None in sd else sum(s*x['par'] for s,x in zip(sd,rows))/tot
    print(f"   {od}  {o['maturity_bucket']:11}  {sp_prior:+6.1f}      {mv:+6.1f}        {sp_prior-mv:+6.1f}        {'n/a (tonight)' if sp_same is None else f'{sp_same:+6.1f}'}")
    summary.append(dict(op=od,bucket=o['maturity_bucket'],spread_prior_close=round(sp_prior,1),vendor_move=mv,spread_opwindow_adj=round(sp_prior-mv,1),spread_same_day_close=None if sp_same is None else round(sp_same,1)))
json.dump(dict(rows=out,summary=summary),open(H/'derived.json','w'),indent=1)

# ---- duration offset: DV01 retired by buybacks since 9/10 vs DV01 issued at 20Y/30Y auctions since 9/10
def dv01(clean,cpn,settle,mat):
    y=ytm(clean,cpn,settle,mat)/100
    def px(yy):
        cds=[mat]
        while cds[-1]>settle: cds.append(addm(cds[-1],-6))
        prev=cds[-1]; nxt=cds[-2]; fut=sorted(c for c in cds if c>settle); w=(nxt-settle).days/(nxt-prev).days
        return sum(cpn/2/(1+yy/2)**(w+i) for i in range(len(fut)))+100/(1+yy/2)**(w+len(fut)-1)
    return (px(y-0.0001)-px(y+0.0001))/2   # per 100 par, per 1bp
ret=0; mv=0
for x in out:
    if x['op']<'2026-09-10': continue
    o=[v for k,v in ops.items() if k.startswith(x['op'])][0]
    d=dv01(x['px'],x['cpn'],D(o['settlement_date']),D(x['mat'])); ret+=d*x['par']/100; mv+=x['px']*x['par']/100
iss=0
for amt,mat,cpn,settle,px in [(22e9,'2056-08-15',5.125,'2026-09-15',97.262274),(13e9,'2046-08-15',5.125,'2026-09-18',96.423840),(22e9,'2056-08-15',5.125,'2026-10-15',92.889131)]:
    iss+=dv01(px,cpn,D(settle),D(mat))*amt/100   # TreasuryDirect auction price, coupon, maturity
print(f"\n== DURATION OFFSET since 9/10: buybacks retired par ${sum(x['par'] for x in out if x['op']>='2026-09-10')/1e9:.2f}B, market value ${mv/1e9:.2f}B, DV01 ${ret/1e6:.2f}M/bp")
print(f"   20Y/30Y auctions issued par $57B, DV01 ${iss/1e6:.2f}M/bp (TreasuryDirect auction prices)  => buybacks offset {ret/iss*100:.0f}% of issued DV01")
