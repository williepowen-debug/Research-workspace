import csv, io, sys, zipfile, datetime as dt
sys.path.insert(0, sys.argv[1]); import crwv_cds_grade as g
D = dt.date
allr = []
for day in sys.argv[3:]:
    z = zipfile.ZipFile(f"{sys.argv[2]}/sec_{day}.zip")
    for x in csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]), encoding="utf-8", errors="replace")):
        x["_f"] = day; allr.append(x)
nm = lambda x: "|".join([x.get("Underlying Asset Name") or "", x.get("UPI Underlier Name") or ""]).upper()
sb = [x for x in allr if "SOFTBANK" in nm(x)]
ids = {x["Dissemination Identifier"] for x in sb}
dead = {x["Original Dissemination Identifier"] for x in allr if x["Action type"] in ("CANC","ERRO","EROR","TERM")}
for x in sorted(sb, key=lambda x: x["Execution Timestamp"]):
    if x["Execution Timestamp"][:10] < "2026-11-24": continue
    try:
        n = float(x["Notional amount-Leg 1"].replace(",","").replace("+","")); c = float(x["Fixed rate-Leg 1"]); U = float(x["Other payment amount"])/n
        tr = D.fromisoformat(x["Execution Timestamp"][:10]); m = D.fromisoformat(x["Expiration Date"])
        s = round(g.conv_spread(U,c,tr,m)*1e4); sd = round(g.conv_spread(U,c,tr,m,dirty=True)*1e4)
    except Exception: s = sd = "-"
    print(x["_f"][5:], x["Action type"], x["Dissemination Identifier"], x["Execution Timestamp"][5:16], x["Expiration Date"], x["Notional amount-Leg 1"], x["Notional currency-Leg 1"], x["Fixed rate-Leg 1"], x["Other payment amount"], s, sd, "DEAD" if x["Dissemination Identifier"] in dead else "", nm(x)[:40])
