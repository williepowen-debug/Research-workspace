import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from scen import put
def solve(S0,K,T,s,target):
    lo,hi=-0.5,0.3
    for _ in range(80):
        m=(lo+hi)/2
        if put(S0*(1+m),K,T,s)>target: lo=m
        else: hi=m
    return m*100
for s in (0.32,0.36):
    print("OZK move for post-print mid = now mid 0.40: %.1f%% (postIV %.0f%%); = now bid 0.30: %.1f%%"%(solve(44.93,40,30/365,s,0.40),s*100,solve(44.93,40,30/365,s,0.30)))
for s in (0.36,0.38,0.40):
    print("WAL move for post-print mid = now mid 1.975: %.1f%% (postIV %.0f%%); = now bid 1.70: %.1f%%"%(solve(72.22,65,59/365,s,1.975),s*100,solve(72.22,65,59/365,s,1.70)))
oz=[-4.47,9.70,0.25,0.10,-6.89,0.06,-2.06,-1.26]; wa=[-8.93,-5.14,0.71,-3.98,3.24,1.16,0.69,3.61]
for s in (0.38,):
    v=[put(72.22*(1+m/100),65,59/365,s) for m in wa]; print("WAL E[mid] postIV 38%%: $%.3f -> $%.0f x4"%(sum(v)/8,sum(v)/8*400))
    print(" per-print:", [(m, round(x,2)) for m,x in zip(wa,v)])
v=[put(44.93*(1+m/100),40,30/365,0.34) for m in oz]; print("OZK E[mid] postIV 34%%: $%.3f -> $%.0f x4"%(sum(v)/8,sum(v)/8*400)); print(" per-print:", [(m, round(x,3)) for m,x in zip(oz,v)])
# bad-print payoff vs now
for m in (-8.93,-12,-15):
    print("WAL %.2f%%: mid@38%% $%.2f -> x4 $%.0f (vs $790 mid now: %+.0f)"%(m, put(72.22*(1+m/100),65,59/365,0.38), put(72.22*(1+m/100),65,59/365,0.38)*400, put(72.22*(1+m/100),65,59/365,0.38)*400-790))
for m in (-6.89,-10,-15):
    print("OZK %.2f%%: mid@34%% $%.2f -> x4 $%.0f (vs $160 mid now: %+.0f)"%(m, put(44.93*(1+m/100),40,30/365,0.34), put(44.93*(1+m/100),40,30/365,0.34)*400, put(44.93*(1+m/100),40,30/365,0.34)*400-160))
