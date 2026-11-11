"""SAM: SoftBank LTV, FULL revaluation across USD/JPY (written 2026-11-11 on PROME prome-2b's question).

Unlike ltv_lookup.py (whose --fx converts only the post-9/30 Arm move and October tranche and holds
the 9/30 base at 157.35 -- it gives the WRONG SIGN across rates), this revalues the whole 9/30 base.
Inputs, all SoftBank Q2 FY2026 finance deck (investor-finance_q2fy2026_01_en.pdf), as of 2026-09-30, $1=JPY157.35:
  p.41  adjusted net debt JPY11.30T / holdings JPY71.14T = 15.9%
  p.45  holdings (net of asset-backed finance) USD 95% / JPY 5%; interest-bearing debt JPY22.5T USD 55 / JPY 38 / EUR 7;
        cash JPY5.4T about 90% foreign
  p.46  Q2 FX effect: LTV +0.2pt, NAV -JPY2.0T (yen ~3.3% stronger Jun->Sep; 6/30 162.605 own ledger)
fD = foreign share of the ratio's NET debt: NOT disclosed. Central 0.62 (gross-debt split), bracketed by
calibration to p.46 (LTV leg 0.46-0.66, NAV leg 0.55-0.81); 0.50 and 0.70 shown.
Settlement: SB7 $0.9B (JPY140.2B) treated as foreign. ABB: +$5.4B value, +$3.6B / +$5.4B debt (RED S62b convention).
"""
ND,V,R930=11.30,71.14,157.35
fV=0.95; ARM_SH,ARM930=923e6,289.66
def calc(fx,fD,arm=181.49,settle=False,abb_debt=0.0,abb_val=0.0):
    r=fx/R930
    v=V*(1-fV)+V*fV*r+(ARM_SH*(arm-ARM930)+10e9)*fx/1e12+abb_val*fx/1e3
    nd=ND*(1-fD)+ND*fD*r+10e9*fx/1e12+(0.9*fx/1e3 if settle else 0)+abb_debt*fx/1e3
    return nd,v
def arm_for(target,fx,fD,**k):
    lo,hi=1.0,400.0
    for _ in range(100):
        m=(lo+hi)/2; nd,v=calc(fx,fD,arm=m,**k)
        if nd/v>target: lo=m
        else: hi=m
    return m
cases=[("own basis",{}),("+SB7 settlement",{"settle":True}),("ABB low (+$3.6B debt)",{"settle":True,"abb_debt":3.6,"abb_val":5.4}),("ABB high (+$5.4B debt)",{"settle":True,"abb_debt":5.4,"abb_val":5.4})]
fxs=[158.81,160,155,150,145]
for fD in (0.62,0.50,0.70):
    print(f"\nforeign share of net debt fD={fD:.2f}")
    print(f"{'case':24s}"+"".join(f"{x:>9.2f}" for x in fxs)+"   Arm@25% at 158.81 / 145")
    for n,k in cases:
        row="".join(f"{(lambda a:a[0]/a[1]*100)(calc(x,fD,**k)):9.2f}" for x in fxs)
        print(f"{n:24s}{row}   ${arm_for(.25,158.81,fD,**k):.0f} / ${arm_for(.25,145,fD,**k):.0f}")
