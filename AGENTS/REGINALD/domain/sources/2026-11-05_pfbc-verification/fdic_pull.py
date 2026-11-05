import json,urllib.request,urllib.parse,csv,sys,time
out=sys.argv[1]
F="CERT,NAMEFULL,REPDTE,ASSET,LNREMULT,P3REMULT,NAREMULT,NTREMULT,LNLSGR,P3ASSET,NAASSET,NTLNLS,STNAME"
def q(flt):
    u="https://api.fdic.gov/banks/financials?"+urllib.parse.urlencode(dict(filters=flt,fields=F,limit=10000,format="json",sort_by="REPDTE",sort_order="ASC"))
    for k in range(3):
        try:
            d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=90).read()); return [x['data'] for x in d['data']]
        except Exception as e: time.sleep(2); err=e
    raise err
pf=q("CERT:33539 AND REPDTE:[20141231 TO 20260630]")
json.dump(pf,open(out+'/pf.json','w'))
A=[]
for y in range(2010,2027):
    for d in ('0331','0630','0930','1231'):
        r=f"{y}{d}"
        if r>'20260630': break
        A+=q(f"REPDTE:{r} AND ASSET:[5000000 TO 15000000]")
json.dump(A,open(out+'/peers.json','w')); print(len(pf),len(A))
