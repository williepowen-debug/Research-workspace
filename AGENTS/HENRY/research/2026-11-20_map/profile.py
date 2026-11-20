import sys, datetime as dt
from collections import defaultdict
sys.path.insert(0, "/home/willi/Research-workspace/AGENTS/HENRY/scripts")
import gamma_flip as g
today = dt.date(2026,11,20)
for und in ("SPX","QQQ"):
    spot, opts, err = g._fetch_yfinance(today, 35, 0.25, und)
    if err: print(und, err); continue
    q = g.UNDERLYINGS[und]["q"]
    def net(S, sel=lambda o: True):
        s=0.0
        for K,T,iv,oi,typ in opts:
            if not sel((K,T,iv,oi,typ)): continue
            v=g.bsm_gamma(S,K,T,iv,q)*oi*100*S*S*0.01
            s+= v if typ=="C" else -v
        return s/1e9
    print(f"== {und} spot {spot:.2f} contracts {len(opts)} totOI {sum(o[3] for o in opts):,.0f}")
    step = 50 if und=="SPX" else 5
    base = round(spot/step)*step
    for S in [base+i*step for i in range(-4,10)]:
        print(f"  S={S:>8.1f} net {net(S):7.1f}")
    byT=defaultdict(float)
    for o in opts:
        K,T,iv,oi,typ=o
        v=g.bsm_gamma(spot,K,T,iv,q)*oi*100*spot*spot*0.01/1e9
        byT[round(T*365)] += v if typ=="C" else -v
    print("  by days-to-expiry:", {k:round(v,1) for k,v in sorted(byT.items())[:8]})
    # biggest OI strikes nearest expiry
    nearest=min(o[1] for o in opts)
    top=defaultdict(lambda:[0,0])
    for K,T,iv,oi,typ in opts:
        if T==nearest: top[K][0 if typ=="C" else 1]+=oi
    print("  nearest-expiry (days",round(nearest*365),") top OI:", sorted(top.items(), key=lambda x:-(x[1][0]+x[1][1]))[:6])
