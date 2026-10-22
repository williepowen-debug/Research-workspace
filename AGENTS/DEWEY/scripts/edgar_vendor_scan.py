#!/usr/bin/env python3
"""
EDGAR vendor scan — which technology vendors does each bank in a universe name
in its own filings, and when? Built 2026-10-22 (Will-greenlit) from the bank
legacy-technology study (167 KRE banks, ~1,350 documents). Stdlib, plus openpyxl
(in the venv) only for --kre.

Pipeline:
  universe (tickers, or --kre = SSGA's daily KRE holdings) -> CIKs via SEC
  company_tickers.json -> EFTS full-text search per term, restricted to those
  CIKs (chunks of 85) -> fetch each hit document -> split into sentences ->
  tag sentences with vendor / CORE / LEGACY patterns -> TSV of tagged sentences
  + a per-bank summary (latest dated mention per vendor).

Usage:
  .venv/bin/python scripts/edgar_vendor_scan.py --kre --start 2024-01-01 --end 2026-10-22 --out scan.tsv
  python3 scripts/edgar_vendor_scan.py --tickers WAL ZION OZK --terms Fiserv "Jack Henry" --out scan.tsv
  (default terms = the vendor list below; default forms = 10-K,10-Q,8-K,425,S-4)

STATUS RULE used in the 2026-10-22 report (apply by hand from the summary):
  CONFIRMED = a primary document names the core vendor in the window (2024+);
  STALE = named only before it; UNKNOWN = never named. Read the sentence: a vendor
  named for card processing or a merchant alliance is NOT the core vendor.

CAVEATS: most banks never name their vendors (2026-10-22: 108 of 167 KRE banks
UNKNOWN); EFTS caps a query at 1,000 hits; "Hogan" hits were all people's names;
banks that file with the FDIC (e.g. OZK) are invisible here.
"""
import argparse, collections, csv, html, io, json, os, re, sys, time, urllib.parse, urllib.request

UA = "Research DEWEY williepowen@gmail.com"
KRE_URL = "https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-kre.xlsx"
DEFAULT_TERMS = ["Fiserv", "Jack Henry", "Fidelity National Information", "core processing", "core conversion",
                 "core banking", "SilverLake", "Finxact", "TCS BaNCS", "Temenos", "Thought Machine", "nCino",
                 "Q2 Holdings", "Alkami", "Finacle", "Evertec", "Finastra", "legacy systems", "end-of-life"]
PATTERNS = [
    ("Fiserv", r"Fiserv"), ("JackHenry", r"Jack Henry|SilverLake|Banno|Symitar|\bJHA\b"),
    ("FIS", r"\bFIS\b|Fidelity National Information|Systematics|Modern Banking Platform|\bIBS\b|Horizon (core|platform)"),
    ("TCS", r"BaNCS|Tata Consultancy"), ("Temenos", r"Temenos"), ("Finxact", r"Finxact"),
    ("ThoughtMachine", r"Thought Machine"), ("nCino", r"nCino"), ("Q2", r"\bQ2 (Holdings|Software|platform|digital)|Q2,? Inc"),
    ("Alkami", r"Alkami"), ("Infosys", r"Finacle|Infosys"), ("Evertec", r"Evertec|EVERTEC"), ("Finastra", r"Finastra"),
    ("COCC", r"\bCOCC\b"), ("CSI", r"Computer Services, Inc"), ("Candescent", r"Candescent"), ("Backbase", r"Backbase"),
    ("CORE", r"(?i)core (banking|processing|system|platform|processor)"),
    ("LEGACY", r"(?i)legacy (systems?|technolog\w*|platforms?|core)|end[- ]of[- ]life|technology moderni[sz]ation|"
               r"core (replacement|moderni[sz]ation)|core (system |banking |processing )?(conversion|migration)|new core"),
]
VR = [(n, re.compile(p)) for n, p in PATTERNS]


def get(url, tries=6, accept="application/json"):
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read()
        except Exception as e:
            err = e
            if getattr(e, "code", None) == 404:
                break
            time.sleep(2 * (i + 1))
    raise err


def kre_tickers():
    import openpyxl
    req = urllib.request.Request(KRE_URL, headers={"User-Agent": "Mozilla/5.0"})
    wb = openpyxl.load_workbook(io.BytesIO(urllib.request.urlopen(req, timeout=60).read()), read_only=True)
    rows = list(wb.active.iter_rows(values_only=True))
    asof = next((str(c) for r in rows[:5] for c in r if c and "As of" in str(c)), "as-of unknown")
    hdr = next(i for i, r in enumerate(rows) if r and r[0] == "Name")
    tick = [str(r[1]).strip() for r in rows[hdr + 1:] if r and r[1] and str(r[1]).strip() not in ("-", "CASH_USD")]
    print(f"KRE holdings: {len(tick)} tickers ({asof})", file=sys.stderr)
    return tick


def cik_map(tickers):
    ct = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
    m = {v["ticker"]: f"{v['cik_str']:010d}" for v in ct.values()}
    out, missing = {}, []
    for t in tickers:
        c = m.get(t.replace(".", "-"))
        (out.__setitem__(c, t) if c else missing.append(t))
    if missing:
        print(f"no SEC CIK (not scanned): {' '.join(missing)}", file=sys.stderr)
    return out


def search(terms, ciks, forms, start, end):
    hits, cl = [], list(ciks)
    for term in terms:
        for chunk in [cl[i:i + 85] for i in range(0, len(cl), 85)]:
            frm = 0
            while True:
                q = urllib.parse.urlencode({"q": f'"{term}"', "forms": forms, "dateRange": "custom", "startdt": start,
                                            "enddt": end, "ciks": ",".join(chunk), "from": frm})
                try:
                    d = json.loads(get("https://efts.sec.gov/LATEST/search-index?" + q))
                except Exception as e:
                    print(f"  EFTS fail {term}: {e}", file=sys.stderr); break
                hs = d.get("hits", {}).get("hits", [])
                for h in hs:
                    s = h["_source"]; adsh, fn = h["_id"].split(":", 1)
                    tks = sorted({ciks[c] for c in s["ciks"] if c in ciks})
                    hits.append((term, ",".join(tks), s["ciks"][0], s["file_date"], s["form"], adsh, fn))
                total = d["hits"]["total"]["value"]
                frm += 100
                if frm >= total or not hs or frm >= 1000:
                    break
                time.sleep(0.15)
        print(f"  {term}: {len(hits)} hits so far", file=sys.stderr)
    return hits


def sentences(raw):
    t = raw.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?s)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    return re.split(r'(?<=[.!?;])\s+(?=[A-Z•(“"])', t)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--tickers", nargs="*", default=[])
    ap.add_argument("--kre", action="store_true", help="universe = SSGA KRE daily holdings")
    ap.add_argument("--terms", nargs="*", default=DEFAULT_TERMS)
    ap.add_argument("--forms", default="10-K,10-Q,8-K,425,S-4")
    ap.add_argument("--start", default="2024-01-01")
    ap.add_argument("--end", default=time.strftime("%Y-%m-%d"))
    ap.add_argument("--out", required=True, help="TSV of tagged sentences")
    ap.add_argument("--cache", default=None, help="directory to cache fetched documents")
    a = ap.parse_args()
    tickers = (kre_tickers() if a.kre else []) + a.tickers
    if not tickers:
        sys.exit("give --tickers and/or --kre")
    ciks = cik_map(tickers)
    hits = search(a.terms, ciks, a.forms, a.start, a.end)
    docs = {}
    for term, tks, cik, date, form, adsh, fn in hits:
        docs.setdefault((adsh, fn), [tks, cik, date, form])
    print(f"fetching {len(docs)} documents", file=sys.stderr)
    if a.cache:
        os.makedirs(a.cache, exist_ok=True)
    rows, summary = [], collections.defaultdict(dict)
    for i, ((adsh, fn), (tks, cik, date, form)) in enumerate(sorted(docs.items(), key=lambda x: x[1][2])):
        p = os.path.join(a.cache, f"{adsh}__{fn}") if a.cache else None
        try:
            if p and os.path.exists(p):
                raw = open(p, "rb").read()
            else:
                raw = get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{adsh.replace('-', '')}/{fn}", accept="text/html")
                if p:
                    open(p, "wb").write(raw)
        except Exception as e:
            print(f"  fetch fail {adsh} {fn}: {e}", file=sys.stderr); continue
        seen = set()
        for s in sentences(raw):
            tags = [n for n, r in VR if r.search(s)]
            if not tags:
                continue
            s2 = s.strip()[:700]
            if s2 in seen:
                continue
            seen.add(s2)
            rows.append([tks, date, form, adsh, fn, ",".join(tags), s2])
            for tk in tks.split(","):
                for tag in tags:
                    if tag not in ("CORE", "LEGACY") and summary[tk].get(tag, "") < date:
                        summary[tk][tag] = date
        if i % 100 == 0:
            print(f"  parsed {i}/{len(docs)}", file=sys.stderr)
    with open(a.out, "w", newline="") as fo:
        w = csv.writer(fo, delimiter="\t")
        w.writerow(["tickers", "file_date", "form", "accession", "document", "tags", "sentence"])
        w.writerows(rows)
    print(f"\n{len(rows)} tagged sentences -> {a.out}\nlatest dated vendor mention per bank (read the sentence before calling it the CORE vendor):")
    for tk in sorted(set(ciks.values())):
        v = summary.get(tk)
        print(f"  {tk:6s} " + ("; ".join(f"{k} {d}" for k, d in sorted(v.items(), key=lambda x: x[1], reverse=True)) if v else "— none named in window"))


if __name__ == "__main__":
    main()
