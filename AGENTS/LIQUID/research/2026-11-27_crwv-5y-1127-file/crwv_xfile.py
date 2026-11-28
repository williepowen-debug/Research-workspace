import csv, io, sys, zipfile, datetime as dt
sys.path.insert(0, sys.argv[1])
import crwv_cds_grade as g
D = dt.date
files = sys.argv[3:]
cache = sys.argv[2]
allrows = []
for day in files:
    z = zipfile.ZipFile(f"{cache}/sec_{day}.zip")
    for x in csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]), encoding="utf-8", errors="replace")):
        x["_file"] = day; allrows.append(x)
def is_cw(x):
    s = "|".join([x.get("Underlying Asset Name") or "", x.get("UPI Underlier Name") or "", x.get("Underlier ID-Leg 1") or ""]).upper()
    return "COREWEAVE" in s or "239FAV" in s or "US21873S" in s
cw = [x for x in allrows if is_cw(x)]
ids = {x["Dissemination Identifier"] for x in cw}
# pull in any row whose original id links to a CoreWeave id (cancels w/o names)
linked = [x for x in allrows if x["Original Dissemination Identifier"] in ids and not is_cw(x)]
rows = cw + linked
rows.sort(key=lambda x: (x["Event timestamp"], x["Dissemination Identifier"]))
dead = {}
for x in allrows:
    if x["Action type"] in ("CANC","ERRO","EROR","TERM") and x["Original Dissemination Identifier"]:
        dead.setdefault(x["Original Dissemination Identifier"], []).append((x["Action type"], x["Dissemination Identifier"], x["Event timestamp"], x["_file"]))
corr = {}
for x in allrows:
    if x["Action type"] in ("CORR","MODI") and x["Original Dissemination Identifier"]:
        corr.setdefault(x["Original Dissemination Identifier"], []).append(x)
def spreads(x):
    try:
        n = x["Notional amount-Leg 1"]; notl = float(n.replace(",","").replace("+",""))
        c = float(x["Fixed rate-Leg 1"]); U = float(x["Other payment amount"]) / notl
        trade = D.fromisoformat(x["Execution Timestamp"][:10]); mat = D.fromisoformat(x["Expiration Date"])
        return round(g.conv_spread(U,c,trade,mat)*1e4), round(g.conv_spread(U,c,trade,mat,dirty=True)*1e4), U*100
    except Exception as e:
        return None
print("file|act|diss_id|orig_id|event_ts|exec_ts|mat|notional|nonstd|name|und_id|upfront_pt|clean|dirty|killed_by|corrected_by")
for x in rows:
    if x["Execution Timestamp"][:10] < "2026-11-19" and x["Expiration Date"] < "2027-01-01": continue
    s = spreads(x)
    k = dead.get(x["Dissemination Identifier"], [])
    c = [(y["Action type"], y["Dissemination Identifier"], y["_file"]) for y in corr.get(x["Dissemination Identifier"], [])]
    print("|".join(map(str,[x["_file"][5:], x["Action type"], x["Dissemination Identifier"], x["Original Dissemination Identifier"], x["Event timestamp"][5:16], x["Execution Timestamp"][5:16], x["Expiration Date"], x["Notional amount-Leg 1"], x["Non-standardized term indicator"], (x.get("Underlying Asset Name") or "")[:16], x.get("Underlier ID-Leg 1"), f"{s[2]:.2f}" if s else "-", s[0] if s else "-", s[1] if s else "-", k, c])))
