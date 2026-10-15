from math import log, sqrt, exp, erf
def N(x): return 0.5*(1+erf(x/sqrt(2)))
def put(S,K,T,s,r=0.04):
    if T<=0: return max(K-S,0)
    d1=(log(S/K)+(r+0.5*s*s)*T)/(s*sqrt(T)); d2=d1-s*sqrt(T)
    return K*exp(-r*T)*N(-d2)-S*N(-d1)
def pbelow(S,K,T,s,r=0.0):
    d2=(log(S/K)+(r-0.5*s*s)*T)/(s*sqrt(T)); return N(-d2)
def iv(price,S,K,T,r=0.04):
    lo,hi=0.01,3.0
    for _ in range(100):
        m=(lo+hi)/2
        if put(S,K,T,m,r)>price: hi=m
        else: lo=m
    return m
def event(sn,tn,sf,tf):
    sb2=(sf*sf*tf-sn*sn*tn)/(tf-tn); e2=sn*sn*tn-sb2*tn
    return sqrt(max(sb2,0)), (sqrt(e2) if e2>0 else float('nan'))
print("== event-implied one-day print move (term structure, ATM puts, vendor mids) ==")
print("OZK Nov20/Jan15 45P:", ["%.3f"%x for x in event(0.3267,37/365,0.3113,93/365)])
print("WAL Nov20/Dec18 72.5P:", ["%.3f"%x for x in event(0.4419,37/365,0.3994,65/365)])
print("WAL Nov20/Mar19 72.5P:", ["%.3f"%x for x in event(0.4419,37/365,0.3698,156/365)])
print("WAL Dec18/Jan15 72.5P:", ["%.3f"%x for x in event(0.3994,65/365,0.3753,93/365)])
import statistics as st
oz=[-4.47,9.70,0.25,0.10,-6.89,0.06,-2.06,-1.26]; wa=[-8.93,-5.14,0.71,-3.98,3.24,1.16,0.69,3.61]
for nm,m in (("OZK",oz),("WAL",wa)):
    print(nm,"realized RMS %.2f%% mean|m| %.2f%%"%(sqrt(sum(x*x for x in m)/len(m)), sum(abs(x) for x in m)/len(m)))
print()
print("== pre-print implied P(below strike at expiry), vendor mid IV ==")
print("OZK 40P Nov20 IV39.16:", "%.3f"%pbelow(44.93,40,37/365,0.3916), " IV from mid0.40:", "%.3f"%iv(0.40,44.93,40,37/365), "bid0.30:", "%.3f"%iv(0.30,44.93,40,37/365))
print("WAL 65P Dec18 IV43.92:", "%.3f"%pbelow(72.22,65,65/365,0.4392))
print()
print("== OZK 40P Nov20 x4: value after the 10/20 AMC print (10/21 close, 30 cal days left), model MID per contract ==")
S0=44.93
for s_post in (0.32,0.36):
    row=[]
    for mv in (-20,-15,-12,-10,-8.93,-6.89,-4.47,-3,-2.06,-1.26,0,0.06,0.1,0.25,3,9.7):
        S=S0*(1+mv/100); row.append((mv, round(put(S,40,30/365,s_post),3)))
    print(" postIV %.0f%%:"%(s_post*100), row)
# expectation over empirical 8
for s_post in (0.32,0.36):
    vals=[put(S0*(1+m/100),40,30/365,s_post) for m in oz]
    print(" E[mid] over OZK's 8 prints, postIV %.0f%%: $%.3f/contract = $%.0f x4"%(s_post*100, sum(vals)/8, sum(vals)/8*400))
print(" pre-print now: bid 0.30 / mid 0.40 => $120 / $160 x4")
print()
print("== WAL 65P Dec18 x4: value after the 10/19 AMC print (10/20 close, 59 cal days left), model MID per contract ==")
S0=72.22
for s_post in (0.36,0.40):
    row=[]
    for mv in (-20,-15,-12,-10,-8.93,-5.14,-3.98,0,0.69,0.71,1.16,3.24,3.61,5):
        S=S0*(1+mv/100); row.append((mv, round(put(S,65,59/365,s_post),3)))
    print(" postIV %.0f%%:"%(s_post*100), row)
for s_post in (0.36,0.40):
    vals=[put(S0*(1+m/100),65,59/365,s_post) for m in wa]
    print(" E[mid] over WAL's 8 prints, postIV %.0f%%: $%.3f/contract = $%.0f x4"%(s_post*100, sum(vals)/8, sum(vals)/8*400))
print(" pre-print now: bid 1.70 / mid 1.98 => $680 / $790 x4")
# no-move theta check: value at 10/20 close with pre-print IV (event still pending) vs now
print()
print("== no-move carry to the print (event premium intact, IV unchanged) ==")
print(" OZK 40P now(37d,39.16%%) %.3f -> 10/20 close (31d, same IV) %.3f"%(put(44.93,40,37/365,0.3916), put(44.93,40,31/365,0.3916)))
print(" WAL 65P now(65d,43.92%%) %.3f -> 10/19 close (60d, same IV) %.3f"%(put(72.22,65,65/365,0.4392), put(72.22,65,60/365,0.4392)))
# roll candidates
print()
print("== roll arithmetic (natural = sell at bid, buy at ask; mid = mid-mid), x4, before fees ==")
for nm,sb,sm,ba,bm in (("OZK Nov20 40P -> Jan15 40P",0.30,0.40,0.90,0.825),("WAL Dec18 65P -> Jan15 65P",1.70,1.975,2.75,2.45),("WAL Dec18 65P -> Mar19 65P",1.70,1.975,4.00,3.75)):
    print(" %s: natural debit $%.0f, mid debit $%.0f"%(nm,(ba-sb)*400,(bm-sm)*400))
