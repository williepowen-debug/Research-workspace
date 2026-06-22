#!/usr/bin/env python3
"""SHADE 80/20 NPORT-P crawl: registered-fund FLOOR on Athene Global Funding (AGF) FABN maturities.
Enumerates NPORT-P filings reporting period 2026-03-31 that hold AGF notes, restricts to the
top-N registrant trusts (the 80/20), fetches each primary_doc.xml, regex-extracts AGF holdings
(par + maturity + coupon), dedups by (cik, seriesId, cusip), sums PAR per CUSIP, buckets by year.
"""
import json, re, time, sys, urllib.request, collections

UA = "SHADE Research williepowen@gmail.com"
# Full registered-fund floor: each fund's MOST RECENT public NPORT-P. Funds file public NPORT-P at
# each fiscal-quarter-end (~3mo apart, filed within 60d), so a ~3-month FILING window captures each
# fund's latest filing ~once; dedup by (cik, seriesId) keeping latest period_ending resolves any dup.
FTS = "https://efts.sec.gov/LATEST/search-index?q=%22Athene+Global+Funding%22&forms=NPORT-P&startdt=2026-03-20&enddt=2026-06-22&from={}"

def get(url, raw=False, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    import gzip; data = gzip.decompress(data)
                return data if raw else data.decode("utf-8", "replace")
        except Exception as e:
            if i == tries - 1:
                return None
            time.sleep(0.6 * (i + 1))

# ---- 1. enumerate the 3/31 AGF NPORT-P universe ----
filings = {}  # accession -> (cik, name, file_date)
frm = 0
while True:
    js = get(FTS.format(frm))
    if not js:
        break
    try:
        d = json.loads(js)
    except Exception:
        break
    hits = d.get("hits", {}).get("hits", [])
    if not hits:
        break
    for h in hits:
        s = h["_source"]
        accn = h["_id"].split(":")[0]
        cik = s["ciks"][0]
        name = (s.get("display_names") or ["?"])[0]
        filings[accn] = (cik, name, s.get("file_date"), s.get("period_ending"))
    frm += 100
    if frm > 8000:
        break
    time.sleep(0.12)

print(f"[enum] AGF NPORT-P filings found (latest-window): {len(filings)}")

# ---- 2. FULL crawl: all trusts ----
by_trust = collections.Counter()
for accn, (cik, name, fd, pe) in filings.items():
    by_trust[(cik, name)] += 1
selected = dict(filings)
print(f"[scope] FULL crawl — {len(by_trust)} registrant trusts, {len(selected)} filings")
print("[top trusts] " + "; ".join(f"{name.split('(')[0].strip()}={n}" for (cik, name), n in by_trust.most_common(12)))

# ---- 3. fetch + parse each selected filing ----
BLK = re.compile(r"<invstOrSec>.*?</invstOrSec>", re.S)
def tag(b, t):
    m = re.search(rf"<{t}[^>]*>(.*?)</{t}>", b, re.S)
    return m.group(1).strip() if m else ""
def tagattr(b, t, a):
    m = re.search(rf"<{t}[^>]*\b{a}=\"([^\"]*)\"", b, re.S)
    return m.group(1).strip() if m else ""

rows = []  # (cik, seriesId, ident, par, valusd, maturity, rt, kind, title, fund, period)
fail = 0
for i, (accn, (cik, name, fd, pe)) in enumerate(sorted(selected.items())):
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn.replace('-','')}/primary_doc.xml"
    xml = get(url)
    if not xml:
        fail += 1
        continue
    sid = tag(xml, "seriesId") or accn
    for b in BLK.findall(xml):
        if ("ATHENE GLOBAL FUNDING" not in b.upper()) and not re.search(r"<cusip[^>]*>0468[56][A-Z0-9]", b):
            continue
        cusip = tag(b, "cusip")
        isin = tagattr(b, "isin", "value")
        ident = cusip if cusip and cusip not in ("N/A","000000000") else isin
        par = tag(b, "balance"); valusd = tag(b, "valUSD")
        mat = tag(b, "maturityDt"); rt = tag(b, "annualizedRt"); kind = tag(b, "couponKind")
        title = tag(b, "title")[:60]
        try: parf = float(par)
        except: parf = 0.0
        try: valf = float(valusd)
        except: valf = 0.0
        rows.append((cik, sid, ident, parf, valf, mat, rt, kind, title, name.split("(")[0].strip(), pe or ""))
    if i % 100 == 0:
        print(f"[fetch] {i}/{len(selected)} (fails={fail})", flush=True)
    time.sleep(0.08)

print(f"[fetch] done: {len(selected)} filings, {fail} fails, {len(rows)} raw AGF holding-lines")

# ---- 4. dedup by (cik, seriesId, ident): keep LATEST period_ending, then max par (amended dups) ----
ded = {}
for cik, sid, ident, parf, valf, mat, rt, kind, title, fund, pe in rows:
    key = (cik, sid, ident)
    if key not in ded or (pe, parf) > (ded[key][8], ded[key][0]):
        ded[key] = (parf, valf, mat, rt, kind, title, ident, fund, pe)

per_cusip = {}  # ident -> {par,val,mat,rt,kind,title,holders}
for (cik, sid, ident), (parf, valf, mat, rt, kind, title, idd, fund, pe) in ded.items():
    e = per_cusip.setdefault(ident, {"par":0.0,"val":0.0,"mat":mat,"rt":rt,"kind":kind,"title":title,"holders":0})
    e["par"] += parf; e["val"] += valf; e["holders"] += 1
    if mat: e["mat"] = mat

def yr(m):
    return m[:4] if m and len(m) >= 4 else "?"
buck = collections.defaultdict(lambda: {"par":0.0,"val":0.0,"cusips":0})
for ident, e in per_cusip.items():
    y = yr(e["mat"]); buck[y]["par"] += e["par"]; buck[y]["val"] += e["val"]; buck[y]["cusips"] += 1

# ---- 5. output ----
out = {"scope": "FULL latest-public-filing-per-fund (all fiscal periods)", "trusts_total": len(by_trust),
       "filings_fetched": len(selected), "fetch_fails": fail, "unique_fund_series_lines": len(ded),
       "unique_cusips": len(per_cusip),
       "by_year": {y: {"par_usd_mn": round(v["par"]/1e6,1), "val_usd_mn": round(v["val"]/1e6,1), "cusips": v["cusips"]}
                   for y, v in sorted(buck.items())},
       "cusips_2026_2027": sorted(
           [{"cusip": ident, "par_usd_mn": round(e["par"]/1e6,1), "val_usd_mn": round(e["val"]/1e6,1),
             "maturity": e["mat"], "rate": e["rt"], "kind": e["kind"], "holders": e["holders"], "title": e["title"]}
            for ident, e in per_cusip.items() if yr(e["mat"]) in ("2026","2027")],
           key=lambda x: x["maturity"] or "")}
with open("/tmp/agf_floor.json","w") as f:
    json.dump(out, f, indent=1)

tot2627 = sum(buck[y]["par"] for y in ("2026","2027"))/1e9
totall = sum(v["par"] for v in buck.values())/1e9
print("\n===== AGF REGISTERED-FUND FLOOR (par, latest-per-fund, FULL crawl) =====")
for y in sorted(buck):
    print(f"  {y}: ${buck[y]['par']/1e9:6.2f}B par  ({buck[y]['cusips']} CUSIPs)")
print(f"  ---- 2026+2027 wall floor: ${tot2627:.2f}B par ;  all-years total: ${totall:.2f}B par ;  unique CUSIPs: {len(per_cusip)}")
print("[out] /tmp/agf_floor.json")
