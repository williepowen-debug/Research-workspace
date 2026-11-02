import json,urllib.request,re,sys
out=sys.argv[1]
for u,sym in [("QQQ","QQQ"),("SPX","_SPX")]:
    req=urllib.request.Request(f"https://cdn.cboe.com/api/global/delayed_quotes/options/{sym}.json",headers={"User-Agent":"Mozilla/5.0 (research)"})
    raw=urllib.request.urlopen(req,timeout=90).read(); open(f"{out}/{u}.json","wb").write(raw)
    j=json.loads(raw); d=j["data"]
    print(u,"timestamp",j.get("timestamp"),"price",d.get("current_price"),"close",d.get("close"),"prev",d.get("prev_day_close"))
    want={"QQQ":[("261120","P",680),("261120","P",690),("261120","P",670),("261120","P",700),("261106","P",690),("261106","P",680),("261102","P",715),("261102","P",690)],
          "SPX":[("261120","P",7600),("261120","P",7700),("261106","P",7550),("261106","P",7600)]}[u]
    idx={}
    for o in d["options"]:
        m=re.match(r"([A-Z]+)(\d{6})([CP])(\d{8})",o["option"])
        if m: idx.setdefault((m.group(2),m.group(3),int(m.group(4))/1000),[]).append((m.group(1),o.get("open_interest"),o.get("volume")))
    for k in want: print("  ",k,idx.get(k))
