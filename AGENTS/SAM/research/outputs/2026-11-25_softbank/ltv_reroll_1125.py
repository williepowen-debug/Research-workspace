"""SAM 2026-11-25 SoftBank LTV re-roll. Model = research/outputs/2026-11-06_softbank/ltv_fx_sensitivity.py
(full revaluation of the 9/30 base; inputs SoftBank Q2 FY2026, $1=157.35) plus 11/25 re-marks:
 SBKK 9434.T 241.1 (9/30) -> live, applied to its 9/30 equity value 3.42T (yen, no FX).
 Interest carry ~0.125T (PROME reader F1 estimate, 11/16) ; SB7 settlement $0.9B ; ABB brackets.
Everything else held at 9/30 marks (SVF incl. OpenAI unchanged; Intel collar-netted; T-Mobile 0)."""
import sys
ND,V,R930=11.30,71.14,157.35
fV=0.95; ARM_SH,ARM930=923e6,289.66
SBKK_V,SBKK930=3.42,241.1
def calc(fx,fD,arm,sbkk,carry=0.0,settle=False,abb_debt=0.0,abb_val=0.0):
    r=fx/R930
    v=V*(1-fV)+V*fV*r+(ARM_SH*(arm-ARM930)+10e9)*fx/1e12+abb_val*fx/1e3+SBKK_V*(sbkk/SBKK930-1)
    nd=ND*(1-fD)+ND*fD*r+10e9*fx/1e12+(0.9*fx/1e3 if settle else 0)+abb_debt*fx/1e3+carry
    return nd,v
def arm_for(t,fx,fD,sbkk,**k):
    lo,hi=1.0,400.0
    for _ in range(100):
        m=(lo+hi)/2; nd,v=calc(fx,fD,m,sbkk,**k)
        lo,hi=(m,hi) if nd/v>t else (lo,m)
    return m
arm=float(sys.argv[1]); fx=float(sys.argv[2]); sbkk=float(sys.argv[3])
cases=[("own basis, no drift",{}),("+ interest carry",{"carry":0.125}),("+ carry + SB7",{"carry":0.125,"settle":True}),
       ("+ ABB low ($3.6B debt)",{"carry":0.125,"settle":True,"abb_debt":3.6,"abb_val":5.4}),
       ("+ ABB high ($5.4B debt)",{"carry":0.125,"settle":True,"abb_debt":5.4,"abb_val":5.4})]
for fD in (0.62,0.50,0.70):
    print(f"\nfD={fD:.2f}  Arm ${arm}  USD/JPY {fx}  SBKK {sbkk}")
    for n,k in cases:
        nd,v=calc(fx,fD,arm,sbkk,**k)
        print(f"  {n:26s} ND {nd:6.2f}T  V {v:6.2f}T  LTV {nd/v*100:5.2f}%   Arm@25% ${arm_for(.25,fx,fD,sbkk,**k):6.1f}   Arm@35% ${arm_for(.35,fx,fD,sbkk,**k):6.1f}")
