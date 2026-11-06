"""Pulled-deal candidates 11/2-11/6: read the 8-K text, do not count the hit. EDGAR search returns 500s intermittently; retry, and name any query that never answered."""
import sys,json,time,re,urllib.parse,urllib.request
sys.path.insert(0,'scripts')
import sec_contact as sc
HD={"User-Agent":sc.sec_ua("BOND-research/1.0 {}")}
def q(p,a,b):
    u="https://efts.sec.gov/LATEST/search-index?"+urllib.parse.urlencode({"q":p,"dateRange":"custom","startdt":a,"enddt":b,"forms":"8-K"})
    for i in range(4):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=HD),timeout=30))["hits"]
        except Exception as e: err=e; time.sleep(2+i)
    print('NO ANSWER',p,err); return None
a,b="2026-11-02","2026-11-06"
h1=q('"pricing of" "senior notes"',a,b); h2=q('"pricing of" "senior secured notes"',a,b)
ents={x["_source"]["ciks"][0] for x in (h1 or {"hits":[]})["hits"]+(h2 or {"hits":[]})["hits"]}
print('filers',len(ents), 'totals', h1 and h1["total"]["value"], h2 and h2["total"]["value"])
seen=set()
for p in ('"not to proceed" "senior notes"','"postponed" "notes offering"','"decided not to proceed" notes offering'):
    r=q(p,a,b)
    if not r: continue
    print(p,'hits',r["total"]["value"])
    for x in r["hits"][:6]:
        s=x["_source"]; acc,f=x["_id"].split(":")
        if (acc,f) in seen: continue
        seen.add((acc,f)); cik=s["ciks"][0].lstrip("0")
        u=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{f}"
        try:
            t=urllib.request.urlopen(urllib.request.Request(u,headers=HD),timeout=30).read().decode("utf8","ignore")
            t=re.sub(r"<[^>]+>"," ",t); t=re.sub(r"\s+"," ",t)
            m=[t[max(0,i.start()-160):i.end()+160] for i in re.finditer(r"(?i)not to proceed|postponed",t)][:2]
            print(' ',s["display_names"][0][:34],s["file_date"],m)
        except Exception as e: print(' ',s["display_names"][0][:34],'ERR',str(e)[:50])
        time.sleep(.3)
