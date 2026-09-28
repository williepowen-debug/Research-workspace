# usage: python isda_neg.py FRED_JSON_DIR   (negative-sign counterfactual for the 7/06 anchor; needs QuantLib)
import sys, os; sys.argv=[sys.argv[0], sys.argv[1]]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'isda_bench.py')).read().split("D = dt.date")[0])
import datetime as dt
D=dt.date
for name,tr,mat,U,iso in [("7/06 Jun-31 CORR 750k",D(2026,7,6),D(2031,6,20),0.0369,'2026-07-06'),
                          ("7/06 Jun-31 2M",D(2026,7,6),D(2031,6,20),0.0287,'2026-07-06'),
                          ("7/07 Dec-30 500k",D(2026,7,7),D(2030,12,20),0.0178,'2026-07-07')]:
    today=qd(tr); disc=curve(today,iso); _,_,acc=par_and_upfront(tr,mat,0.08,disc)
    pos,_=solve(tr,mat,U+acc,disc); neg,_=solve(tr,mat,acc-U,disc)
    print(f"{name:24s} |U| {U*100:.2f}pt  ISDA cash-reading: POSITIVE sign {pos*1e4:6.1f}bp | NEGATIVE sign {neg*1e4:6.1f}bp")
