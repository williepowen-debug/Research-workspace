import sys,os;sys.path.insert(0,os.path.dirname(__file__))
from lib import *
import statistics as st
# medians from the n=10 rule table, values typed from c_analog output are recomputed there; here: cash premium history
ho=load('EER_EPD2F_PE1_Y35NY_DPGd');sp=load('EER_EPD2DXL0_PF4_Y35NY_DPGd');gc=load('EER_EPD2DXL0_PF4_RGC_DPGd')
c={k:sp[k]-ho[k] for k in sp if k in ho}
v=sorted(c.values());import bisect
print('NYH spot minus HO1, n',len(v),'median',round(st.median(v),3),'rank of 0.29',round(bisect.bisect_left(v,.2924)/len(v)*100,1),'max',max(c.items(),key=lambda x:x[1]))
o=[c[k] for k in c if k.year==2022 and k.month==10];print('Oct 2022 mean',round(st.mean(o),3),'max',round(max(o),3))
n=[sp[k]-gc[k] for k in gc if k in sp];v=sorted(n);print('NYH-USGC n',len(v),'median',round(st.median(v),3),'rank .298',round(bisect.bisect_left(v,.298)/len(v)*100,1))
o=[sp[k]-gc[k] for k in gc if k in sp and k.year==2022 and k.month==10];print('Oct 2022 NYH-USGC mean',round(st.mean(o),3))
