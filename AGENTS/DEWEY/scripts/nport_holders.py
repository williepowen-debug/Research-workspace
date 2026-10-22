#!/usr/bin/env python3
"""
N-PORT holder scanner — which registered funds hold a named set of bonds/deals,
how much, and in which class. Built 2026-10-22 (Will-greenlit) from the REQ-007
v2 leg that answered "do private-credit vehicles hold the weak data-center
tranches?" (1,293 filings, 664 fund series). Stdlib only.

Pipeline (one command):
  1. EDGAR full-text search (EFTS) for each deal-name term, forms NPORT-P, date window
  2. fetch each filing's holdings XML (falls back to primary_doc.xml when the
     indexed document name 404s — ~60% of the first pass on 2026-10-22)
  3. keep <invstOrSec> rows whose name/title matches --match
  4. dedupe to the LATEST position per (registrant, series, CUSIP)
  5. tag the class letter (from the title, else inferred by CUSIP from other
     funds' titles — marked with '*'), print a class summary, write TSV

Usage:
  python3 nport_holders.py --term 'Vantage="Vantage Data Centers Issuer"' \
      --term 'SWCH="SWCH Commercial Mortgage Trust"' \
      --match 'VANTAGE DATA|SWCH' --start 2026-07-15 --end 2026-10-22 --out holders.tsv
  python3 nport_holders.py --terms-file deals.txt --match '...' --start ... --end ... --out ...
      (deals.txt: one NAME=QUERY per line; QUERY is an EFTS phrase, quote it)

CAVEATS (state them in any report that uses the output):
  - N-PORT covers registered funds only: private funds, separate accounts and
    insurer general accounts are NOT here. Insurer-sponsored variable trusts are.
  - EFTS caps each query at 1,000 hits; split long windows if a term saturates.
  - Class letter != rating. Map class -> rating from the presale ladder.
  - Mostly quarter-end positions (N-PORT is filed monthly, public quarterly).
"""
import argparse, csv, collections, json, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

UA = "Research DEWEY williepowen@gmail.com"   # SEC wants a declared contact UA (see edgar_doc.py)
NS = "{http://www.sec.gov/edgar/nport}"
COLS = ["adsh", "file_date", "rep_date", "registrant", "series", "net_assets", "name", "title",
        "cusip", "balance", "valUSD", "pctVal", "assetCat", "restricted", "url"]


def get(url, tries=5):
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            err = e
            if getattr(e, "code", None) == 404:
                break
            time.sleep(2 + 2 * i)
    raise err


def efts(q, start, end, frm=0):
    p = {"q": q, "forms": "NPORT-P", "dateRange": "custom", "startdt": start, "enddt": end, "from": frm}
    return json.loads(get("https://efts.sec.gov/LATEST/search-index?" + urllib.parse.urlencode(p)))


def harvest(terms, start, end):
    filings = {}
    for name, q in terms.items():
        frm = 0
        while True:
            try:
                d = efts(q, start, end, frm)
            except Exception as e:
                print(f"  EFTS error on {name}: {e}", file=sys.stderr)
                break
            hits = d["hits"]["hits"]
            for h in hits:
                s = h["_source"]
                f = filings.setdefault(s["adsh"], {"cik": s["ciks"][0], "fn": h["_id"].split(":", 1)[1],
                                                   "date": s["file_date"], "terms": set()})
                f["terms"].add(name)
            total = d["hits"]["total"]["value"]
            frm += 100
            if frm >= total or not hits or frm >= 1000:
                if total >= 1000:
                    print(f"  WARNING: {name} saturated the 1,000-hit cap — split the date window", file=sys.stderr)
                break
            time.sleep(0.2)
        print(f"  {name}: {len(filings)} filings so far", file=sys.stderr)
    return filings


def parse(xml_bytes, match, adsh, file_date, url):
    root = ET.fromstring(xml_bytes)

    def t(el, tag):
        if el is None:
            return ""
        e = el.find(".//" + NS + tag)
        return e.text if e is not None and e.text else ""
    gen, fi = root.find(".//" + NS + "genInfo"), root.find(".//" + NS + "fundInfo")
    out = []
    for inv in root.iter(NS + "invstOrSec"):
        nm, ti = t(inv, "name"), t(inv, "title")
        if match.search(nm + " " + ti):
            out.append([adsh, file_date, t(gen, "repPdDate"), t(gen, "regName"), t(gen, "seriesName"),
                        t(fi, "netAssets"), nm, ti, t(inv, "cusip"), t(inv, "balance"), t(inv, "valUSD"),
                        t(inv, "pctVal"), t(inv, "assetCat"), t(inv, "isRestrictedSec"), url])
    return out


def fetch_one(item, match):
    adsh, f = item
    base = f"https://www.sec.gov/Archives/edgar/data/{int(f['cik'])}/{adsh.replace('-', '')}/"
    for fn in (f["fn"], "primary_doc.xml"):
        try:
            return parse(get(base + fn), match, adsh, f["date"], base + fn), None
        except Exception as e:
            last = f"{type(e).__name__}: {str(e)[:60]}"
    return [], (adsh, base, last)


def klass(s):
    s = s.upper()
    m = (re.search(r"CLASS\s+([A-Z][A-Z0-9-]*)", s) or re.search(r"\bCL\s+([A-Z][A-Z0-9-]*)", s)
         or re.search(r"20\d\d[- ]?\d?[A-Z]{0,4}\s+([A-HJ-Z][0-9]?|HRR|RR)\b(?! ?\d{4})", s))
    return m.group(1) if m else ""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--term", action="append", default=[], help='NAME="EFTS phrase" (repeatable)')
    ap.add_argument("--terms-file")
    ap.add_argument("--match", required=True, help="regex on holding name+title (case-insensitive)")
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--out", required=True, help="TSV of latest positions")
    ap.add_argument("--raw", help="optional TSV of every matched row before dedupe")
    a = ap.parse_args()
    lines = list(a.term) + ([l.strip() for l in open(a.terms_file) if l.strip() and not l.startswith("#")] if a.terms_file else [])
    terms = dict(l.split("=", 1) for l in lines)
    if not terms:
        sys.exit("need at least one --term or --terms-file")
    match = re.compile(a.match, re.I)

    filings = harvest(terms, a.start, a.end)
    print(f"total filings {len(filings)}", file=sys.stderr)
    rows, errs = [], []
    with ThreadPoolExecutor(4) as ex:
        for i, (r, e) in enumerate(ex.map(lambda it: fetch_one(it, match), filings.items())):
            rows.extend(r)
            if e:
                errs.append(e)
            if i % 200 == 0:
                print(f"  parsed {i}/{len(filings)}, rows {len(rows)}", file=sys.stderr)
    if a.raw:
        with open(a.raw, "w", newline="") as fo:
            w = csv.writer(fo, delimiter="\t"); w.writerow(COLS); w.writerows(rows)

    # class map by CUSIP, then latest per (registrant, series, cusip)
    cmap = collections.defaultdict(collections.Counter)
    for r in rows:
        c = klass(r[7]) or klass(r[6])
        if c and r[8] not in ("", "000000000", "N/A"):
            cmap[r[8]][c] += 1
    latest = {}
    for r in rows:
        k = (r[3], r[4], r[8] if r[8] not in ("", "000000000", "N/A") else r[7])
        if k not in latest or r[2] > latest[k][2]:
            latest[k] = r
    out = []
    for r in latest.values():
        c = klass(r[7]) or klass(r[6])
        if not c and r[8] in cmap:
            c = cmap[r[8]].most_common(1)[0][0] + "*"
        out.append(r + [c])
    out.sort(key=lambda r: -float(r[10] or 0))
    with open(a.out, "w", newline="") as fo:
        w = csv.writer(fo, delimiter="\t"); w.writerow(COLS + ["class"]); w.writerows(out)

    tot = sum(float(r[10] or 0) for r in out)
    print(f"\npositions {len(out)} · fund series {len({(r[3], r[4]) for r in out})} · total ${tot/1e6:,.1f}M · fetch errors {len(errs)}")
    by = collections.defaultdict(lambda: [0, 0.0])
    for r in out:
        c = r[-1].rstrip("*") or "UNK"
        b = "A (senior)" if c.startswith("A") else c
        by[b][0] += 1; by[b][1] += float(r[10] or 0)
    for k, (n, v) in sorted(by.items(), key=lambda x: -x[1][1]):
        print(f"  class {k:12s} {n:5d} positions  ${v/1e6:10,.1f}M  {v/tot*100 if tot else 0:5.1f}%")
    for e in errs[:10]:
        print("  ERR", *e, file=sys.stderr)


if __name__ == "__main__":
    main()
