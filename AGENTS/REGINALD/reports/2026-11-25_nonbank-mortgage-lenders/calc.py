ye=dict(UWM=900.0+300.0,RKT=150+700+450+360+150+310+440+265+150,ONIT=1285.2,PFSI_notes=1326.0); q=dict(UWM=1415+875,RKT=0+150+0+250+25+25+340+150,ONIT=1700.6,PFSI_notes=1641.0)
for k in ye: print(k,ye[k],q[k],f"{100*(q[k]/ye[k]-1):.1f}%")
a,b=sum(ye.values()),sum(q.values()); print("sum",a,b,100*(b/a-1)); print("ex RKT",a-ye['RKT'],b-q['RKT'],100*((b-q['RKT'])/(a-ye['RKT'])-1))
print("UWM warehouse",7650963/8912496-1,"RKT funding",12042/13851-1)
print("WAL gap",10768-7029,"ACL bp",6.7/7029*1e4, "MF %T1", None)
exec(open("code/rank.py").read().split('k,o=D')[0])
k,o=D["09302026"]
for r,n,x in [("3138146","WAL",7029),("2354985","CUBI",1400.6),("3938186","BKU",932.3),("485559","FHN",3869),("2618780","TCBI",5441.7)]:
    t=v("09302026",r,"8274")/1e3; L=v("09302026",r,"2122")/1e3; m=v("09302026",r,"PV05")/1e3; tc=v("09302026",r,"3792")
    print(n,"T1",round(t),"M10a",round(m),"10-Q",x,"share of M10a %.1f"%(100*x/m),"%%loans %.1f %%T1 %.1f"%(100*x/L,100*x/t),"gap",round(m-x),"TC",tc and round(tc/1e3), "q0 PV12",(v("12312025",r,"PV12") or 0)/1e3)
for n,f in[("WAL PV11..16",["PV11","PV12","PV13","PV14","PV15","PV16"])]: print(n,[(c,v("09302026","3138146",c)) for c in f])
