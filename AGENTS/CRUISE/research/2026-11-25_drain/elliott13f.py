"""Bounded primary check of WALTER SIG-W-20261117-006 item 10 ('Elliott raised its Norwegian Cruise stake', 13F)."""
import json, re, sys, urllib.request
sys.path.insert(0, "scripts")
from sec_contact import sec_ua
H = {"User-Agent": sec_ua(), "Accept-Encoding": "identity"}
get = lambda u: urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=30).read().decode("utf-8", "replace")
atom = get("https://www.sec.gov/cgi-bin/browse-edgar?company=elliott+investment+management&type=13F-HR&dateb=&owner=include&count=10&action=getcompany&output=atom")
ciks = sorted(set(re.findall(r"CIK=(\d{10})", atom)))
print("ciks", ciks)
for c in ciks[:2]:
    j = json.loads(get(f"https://data.sec.gov/submissions/CIK{c}.json"))
    f = j["filings"]["recent"]; print(j["name"])
    rows = [(f["filingDate"][i], f["form"][i], f["accessionNumber"][i], f["reportDate"][i]) for i in range(len(f["form"])) if f["form"][i].startswith("13F")][:3]
    for r in rows: print("  ", r)
    for d, form, acc, rep in rows[:2]:
        idx = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc.replace('-','')}/index.json"))
        for it in idx["directory"]["item"]:
            if it["name"].endswith(".xml") and "primary" not in it["name"]:
                x = get(f"https://www.sec.gov/Archives/edgar/data/{int(c)}/{acc.replace('-','')}/{it['name']}")
                for blk in re.findall(r"<(?:\w+:)?infoTable>(.*?)</(?:\w+:)?infoTable>", x, re.S):
                    if "NORWEGIAN" in blk.upper():
                        g = lambda t: (re.search(rf"<(?:\w+:)?{t}>(.*?)</", blk, re.S) or [None, None])[1]
                        print("     ", rep, form, g("titleOfClass"), "value", g("value"), "shares", g("sshPrnamt"), g("putCall"))
