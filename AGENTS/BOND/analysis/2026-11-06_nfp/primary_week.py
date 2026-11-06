"""Friday HY primary count, week of 11/2, and pulled-deal candidates 11/2-11/6. Same queries as 2026-11-05_catchup/primary_edgar_count.py."""
import sys,json,time,urllib.parse,urllib.request
sys.path.insert(0,'scripts')
import sec_contact as sc
HD={"User-Agent":sc.sec_ua("BOND-research/1.0 {}")}
def q(p,a,b):
    u="https://efts.sec.gov/LATEST/search-index?"+urllib.parse.urlencode({"q":p,"dateRange":"custom","startdt":a,"enddt":b,"forms":"8-K"})
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=HD),timeout=30))["hits"]
a,b="2026-11-02","2026-11-06"
h1=q('"pricing of" "senior notes"',a,b); time.sleep(.3); h2=q('"pricing of" "senior secured notes"',a,b); time.sleep(.3)
ents={}
for x in h1["hits"]+h2["hits"]:
    s=x["_source"]; ents[s["ciks"][0]]=(s["display_names"][0][:40],s["file_date"])
print('week',a,'notes',h1["total"]["value"],'secured',h2["total"]["value"],'filers',len(ents))
for k,v in sorted(ents.items(),key=lambda z:z[1][1]): print(' ',v)
for p in ('"not to proceed" "senior notes"','"postponed" "notes offering"','"decided not to proceed" notes offering'):
    r=q(p,a,b); time.sleep(.3)
    print(p,r["total"]["value"],[ (x["_source"]["display_names"][0][:34],x["_source"]["file_date"]) for x in r["hits"][:6]])
