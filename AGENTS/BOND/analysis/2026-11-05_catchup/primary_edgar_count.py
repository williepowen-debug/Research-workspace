import sys,json,time,re,urllib.parse,urllib.request,datetime as dt
sys.path.insert(0,'scripts')
import sec_contact as sc
HD={"User-Agent":sc.sec_ua("BOND-research/1.0 {}")}
def q(p,a,b):
    u="https://efts.sec.gov/LATEST/search-index?"+urllib.parse.urlencode({"q":p,"dateRange":"custom","startdt":a,"enddt":b,"forms":"8-K"})
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=HD),timeout=30))["hits"]
d=dt.date(2026,8,31)
print("week_mon  notes  secured  entities")
while d<=dt.date(2026,11,2):
    e=d+dt.timedelta(days=4); a,b=d.isoformat(),e.isoformat()
    h1=q('"pricing of" "senior notes"',a,b); time.sleep(.25); h2=q('"pricing of" "senior secured notes"',a,b); time.sleep(.25)
    ents={x["_source"]["ciks"][0] for x in h1["hits"]+h2["hits"]}
    print(a,h1["total"]["value"],h2["total"]["value"],len(ents)); d+=dt.timedelta(days=7)
print("---pulled candidates")
seen=set()
for p in ('"not to proceed" "senior notes"','"postponed" "notes offering"','"decided not to proceed" notes offering'):
    for x in q(p,"2026-10-01","2026-11-05")["hits"]:
        s=x["_source"]; acc=x["_id"].split(":")[0]; f=x["_id"].split(":")[1]
        if (acc,f) in seen: continue
        seen.add((acc,f))
        cik=s["ciks"][0].lstrip("0"); u=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{f}"
        try:
            t=urllib.request.urlopen(urllib.request.Request(u,headers=HD),timeout=30).read().decode("utf8","ignore")
            t=re.sub(r"<[^>]+>"," ",t); t=re.sub(r"\s+"," ",t)
            m=[t[max(0,i.start()-110):i.end()+110] for i in re.finditer(r"(?i)not to proceed|postponed",t)][:1]
            print(s["display_names"][0][:30],s["file_date"],'::',m[0] if m else None)
        except Exception as e: print(s["display_names"][0][:30],"ERR",str(e)[:50])
        time.sleep(.2)
