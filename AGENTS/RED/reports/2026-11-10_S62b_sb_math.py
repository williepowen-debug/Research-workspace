import math
fx=158.69; arm=181.49; ARM_SH=923e6; ARM930=289.66
nd,v=11.30,71.14              # reported 9/30, yen T (ds p.17)
oct_t=10e9*fx/1e12            # October OpenAI tranche, into debt and value
L=nd+oct_t; V=v+oct_t+ARM_SH*(arm-ARM930)*fx/1e12
def r(l,vv): return 100*l/vv
def arm_for(t,l,vv): return arm+(l/t-vv)*1e12/(ARM_SH*fx)
print(f"A  SoftBank basis rolled           {r(L,V):.2f}%  L={L:.3f} V={V:.3f}  Arm25 ${arm_for(.25,L,V):.0f}")
st=0.1402; abb=5.4e9*fx/1e12
print(f"B  + settlement                    {r(L+st,V):.2f}%  Arm25 ${arm_for(.25,L+st,V):.0f}")
print(f"C  + settlement + ABB at cost      {r(L+st+abb,V+abb):.2f}%  Arm25 ${arm_for(.25,L+st+abb,V+abb):.0f}  drop {100*(1-arm_for(.25,L+st+abb,V+abb)/arm):.1f}%")
ab=6.49; hy=0.76
print(f"D  gross: asset-backed added back  {r(L+ab,V+ab):.2f}%   +hybrid 50% back {r(L+ab+hy,V+ab):.2f}%")
print(f"   9/30 gross                       {r(nd+ab,v+ab):.2f}%  +hybrid {r(nd+ab+hy,v+ab):.2f}%")
oai=110e9*fx/1e12; armnet=ARM_SH*arm*fx/1e12-3.90
print(f"   OpenAI {oai:.2f}T = {100*oai/V:.1f}% of V; Arm net {armnet:.2f}T = {100*armnet/V:.1f}%")
for d in (0.15,0.20,0.30):
    print(f"E  OpenAI mark -{int(d*100)}% (on C)        {r(L+st+abb,V+abb-d*oai):.2f}%")
for a_d,o_d in ((0.10,0.10),(0.10,0.15),(0.05,0.10)):
    dv=ARM_SH*arm*a_d*fx/1e12+o_d*oai
    print(f"F  Arm -{int(a_d*100)}% & OpenAI -{int(o_d*100)}% on A {r(L,V-dv):.2f}%  on C {r(L+st+abb,V+abb-dv):.2f}%")
for s in (347,497,513):
    lam=s/1e4/0.6; print(f"G  CDS {s}bp R40 -> hazard {100*lam:.1f}%/yr, 5y cum PD {100*(1-math.exp(-5*lam)):.0f}% (risk-neutral)")
print(f"H  new $10B debt-funded check on C: {r(L+st+abb+10e9*fx/1e12,V+abb+10e9*fx/1e12):.2f}%")
