# SAM re-mark of SoftBank LTV. Inputs: SBG Q1 FY26 finance deck (6/30/2026, $1=Y162.39); marks 11/6.
fx0,fx=162.39,158.5; k=fx/fx0
L0=10.81
arm_sh=923e6; arm_ml_usd=3.2210e12/fx0   # margin loan Y3,221.0B
sbkk_sh=19149e6; sbkk_ml=1.197
def V(arm_px,openai_up=0.0,tr=20e9,svf_loan=True,arm_extra=0.0,dbridge=False,sbkk_px=235.4):
    arm=arm_sh*arm_px*fx/1e12-(arm_ml_usd+arm_extra)*fx/1e12
    sb=sbkk_sh*sbkk_px/1e12-sbkk_ml
    v=arm+sb+3.60*k+19.29*k+1.00*k+6.51
    v+=tr*fx/1e12
    if svf_loan: v-=10e9*fx/1e12
    if dbridge: v+=3.1e9*fx/1e12
    return v+openai_up
def L(tr=20e9,svf_loan=True,arm_extra=0.0,dbridge=False,check=0.0):
    l=L0-0.2                       # about half of Y14T debt in USD, ~2.4% FX
    l+=tr*fx/1e12
    if svf_loan: l-=10e9*fx/1e12
    l-=arm_extra*fx/1e12
    if dbridge: l+=3.1e9*fx/1e12
    return l+check
up=(110e9*0.4671)*fx/1e12
print('OpenAI carrying check: 110B/0.13=%.0fB; up-mark to 1.25T on 852B: +%.1fT'%(110/.13,up))
cases={'A reported basis: SVF2 loan outside ratio, DigitalBridge paid':dict(svf_loan=True,dbridge=True),
       'B A + Arm loan +$5B drawn':dict(svf_loan=True,arm_extra=5e9,dbridge=True),
       'C recourse view: guaranteed SVF2 loan counted, DigitalBridge paid':dict(svf_loan=False,dbridge=True),
       'D C + Arm loan +$5B drawn':dict(svf_loan=False,arm_extra=5e9,dbridge=True)}
for n,c in cases.items():
    for px,lab,tr in ((172.34,'11/6',20e9),(289.66,'9/30 (Oct tranche not yet paid)',10e9)):
        l=L(tr=tr,**c); v=V(px,tr=tr,**c); print(f'{n:64s} Arm {px:7.2f} {lab}: L {l:5.2f} V {v:5.2f} LTV {l/v*100:4.1f}%')
    l=L(**c); nonarm=V(0,**c)
    need=l/0.25-nonarm
    print(f"   Arm price for 25%: ${need*1e12/fx/arm_sh:6.1f}   with OpenAI at 1.25T: LTV {l/(V(172.34,**c)+up)*100:4.1f}%")
c=dict(svf_loan=True,dbridge=True)
base=L(**c)/V(172.34,**c)*100
for usd in (0.3e9,0.5e9,0.9e9):
    a=usd*fx/1e12; print(f'check ${usd/1e9:.1f}B = Y{a*1000:.0f}B: LTV change {((L(**c)+a)/(V(172.34,**c)+a)*100-base):+.2f}ppt')
print('valuation effect ppt', round(L(**c)/(V(172.34,**c)+up)*100-base,2))
# independent route from 3/31 base
L33=8.2;V33=L33/0.17
arm331=arm_sh*151.28*159.0/1e12; armnow=arm_sh*172.34*fx/1e12
l=L33+2.7-0.5+20e9*fx/1e12-10e9*fx/1e12+3.1e9*fx/1e12; v=V33+2.7+(armnow-arm331)+0.1+1.3+20e9*fx/1e12-10e9*fx/1e12+3.1e9*fx/1e12
print('route2 from 3/31: L %.2f V %.2f LTV %.1f%%'%(l,v,l/v*100))
h=[385,600,550,550,350,500];print('Hawks senior 6/30 ex-matured',sum(h),'+1000 =',sum(h)+1000,' share of 10T %.0f%%, of 2386T %.2f%%'%((sum(h)+1000)/100,(sum(h)+1000)/2386000*100))

# sensitivities on case A
c=dict(svf_loan=True,dbridge=True); l,v=L(**c),V(172.34,**c)
x=11.87e9*fx/1e12; print('if $11.87B also sits outside the ratio: %.1f%%'%((l-x)/(v-x)*100))
y=(5.4e9-1.75e9)*fx/1e12; print('if ABB closes in full, SBG equity $3.65B: %.1f%%'%((l+y)/(v+y)*100))
print('Arm pledged 769M/923M = %.0f%%; value at $172.34 $%.1fB; cover on $25B %.1fx, on $20B %.1fx'%(769/923*100,769e6*172.34/1e9,769e6*172.34/25e9,769e6*172.34/20e9))
