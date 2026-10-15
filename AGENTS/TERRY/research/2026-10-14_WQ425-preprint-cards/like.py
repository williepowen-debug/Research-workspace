import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scen import put, pbelow, iv
for nm,S,K,BE,T,mid,bid,yiv in (("OZK 40P Nov20",44.93,40,39.19,37/365,0.40,0.30,0.3916),("WAL 65P Dec18",72.22,65,63.29,65/365,1.975,1.70,0.4392)):
    im=iv(mid,S,K,T); ib=iv(bid,S,K,T)
    print(nm, "IV(mid)=%.1f%% IV(bid)=%.1f%% vendorIV=%.1f%%"%(im*100,ib*100,yiv*100))
    for lab,s in (("mid",im),("vendor",yiv)):
        print("   %s: P(<strike %.2f)=%.1f%%  P(<breakeven %.2f)=%.1f%%"%(lab,K,pbelow(S,K,T,s)*100,BE,pbelow(S,BE,T,s)*100))
