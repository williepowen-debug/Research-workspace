#!/usr/bin/env python3
"""
HY ETF holdings: pull, save dated, and compare two dates by bucket.
Built 2026-10-23 (Will-greenlit "yes go ahead with the tool") after the third run that
needed holdings history and found none (REQ-002, REQ-003; BACKLOG 2026-07-02 and
2026-10-23 rows). Stdlib only (the JNK XLSX is read with zipfile).

Funds:
  HYG  iShares `latest-holdings.csv` (CUSIP, sector, price, YTW). The URL ignores
       asOfDate, so ONLY TODAY'S FILE EXISTS; history is whatever someone saved.
       Older saved downloads (XML-spreadsheet .xls, e.g. LIQUID's) import too.
  JNK  SSGA `holdings-daily-us-en-jnk.xlsx` (name, ISIN, weight, coupon, par,
       market value, maturity). No sector, price or yield column: price is
       derived as market value / par x 100.

Usage:
  python3 etf_holdings.py pull                       # both funds -> research/etf_holdings/
  python3 etf_holdings.py import FILE --fund HYG     # register an older download by its as-of date
  python3 etf_holdings.py list
  python3 etf_holdings.py compare HYG:2026-10-13 HYG:2026-10-22 --min-ytw 12
  python3 etf_holdings.py compare JNK:2026-10-22 JNK:2026-10-30 --max-price 80 --tsv out.tsv
      (a side may also be a file path; --bucket NAME=REGEX replaces the default buckets,
       repeatable, first match wins, unmatched -> "other")

compare prints, per bucket: line count, weight, weight share, average change in
yield-to-worst and price, and each bucket's share of the sleeve's total yield change
and price loss (weight x change). Then the top names by price contribution.

CAVEATS (state them in any report that uses the output):
  - Vendor evaluated prices, not trades; iShares says a price "may not necessarily be
    as of the date shown".
  - Neither fund publishes ratings. A YTW or price threshold is a PROXY for a rating tier.
  - Price change includes the rate move. For whole-fund windows where Treasuries moved,
    bucket shares of price change are rate-contaminated (small or sign-flipping
    denominator); use a high-yield sleeve or convert to spread terms.
  - Bucket regexes are a name classification, not an index sector; ICE "Technology" != AI.
  - JNK market value may include accrued interest, so derived price runs high by that amount.
    JNK lists exited positions with par 0; they are dropped (39 of 1,159 rows on 2026-10-22).
  - Matching key = (name, maturity, float(coupon)); " Prvt" is mapped to " 144A". Lines
    present in only one file are reported as unmatched, never silently dropped.
"""
import argparse, csv, gzip, hashlib, html, io, re, sys, time, urllib.request, zipfile
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
STORE = HERE.parent / "research" / "etf_holdings"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
URLS = {
    "HYG": "https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf/latest-holdings.csv",
    "JNK": "https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-jnk.xlsx",
}
# Default buckets, as used in REQ-003 (2026-10-23). First match wins.
BUCKETS = [
    ("ai_builder", r"^(COREWEAVE|SOFTBANK|WULF COMPUTE|GALAXY HELIOS|FLASH COMPUTE|EDGED COMPUTE|CORE SCIENTIFIC|"
                   r"CIPHER COMPUTE|BLACK PEARL COMPUTE|APLD COMPUTECO)"),
    ("software", r"CLOUD SOFTWARE|NEPTUNE BIDCO|ION PLATFORM|ATHENAHEALTH|SS&C|^UKG |CORELOGIC|GEN DIGITAL|CLARIVATE|"
                 r"ROCKET SOFTWARE|MCAFEE|OPEN TEXT|^SABRE|GO DADDY|NCR VOYIX|TWILIO|FAIR ISAAC|CDK STEERCO|"
                 r"DUN & BRADSTREET|ZOOMINFO|GOTO GROUP|RACKSPACE|ELLUCIAN|COTIVITI|CITRIX|PROOFPOINT|INFORMATICA|"
                 r"DAYFORCE|BLACKBAUD|CONDOR|BOOST NEWCO|POLARIS NEWCO|VERSCEND|CAMELOT"),
]


def num(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    s = str(x).replace(",", "").replace("%", "").strip()
    if s in ("", "-", "--", "N/A"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def fetch(url, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:  # SSL drops and resets happen on single calls
            last = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"fetch failed after {tries} tries: {url}: {last}")


def _date(s, fmts):
    s = s.strip().replace("As of ", "")
    for f in fmts:
        try:
            return datetime.strptime(s, f).date().isoformat()
        except ValueError:
            pass
    raise ValueError(f"unparsed as-of date: {s!r}")


def _row(name, sector, weight, price, ytw, maturity, coupon, par, mv, ident):
    return dict(name=name.strip(), sector=sector, weight=num(weight), price=num(price), ytw=num(ytw),
                maturity=maturity, coupon=num(coupon), par=num(par), mv=num(mv), id=ident)


def parse_hyg_csv(raw):
    lines = raw.decode("utf-8-sig", errors="replace").splitlines()
    if not lines or "Fund Holdings as of" not in lines[1]:
        raise ValueError("not an iShares holdings CSV (the endpoint sometimes serves HTML)")
    asof = _date(lines[1].split(",", 1)[1].strip('"'), ["%b %d, %Y"])
    hi = next(i for i, l in enumerate(lines) if l.startswith("Name,"))
    rows = []
    for r in csv.DictReader(io.StringIO("\n".join(lines[hi:]))):
        if r.get("Asset Class") != "Fixed Income":
            continue
        rows.append(_row(r["Name"], r["Sector"], r["Weight (%)"], r["Price"], r["Yield to Worst (%)"],
                         r["Maturity"], r["Coupon (%)"], r["Par Value"], r["Market Value"], r.get("CUSIP")))
    return asof, rows


def parse_hyg_xls(raw):
    t = raw.decode("utf-8", errors="replace")
    m = re.search(r'<ss:Worksheet ss:Name="Holdings">(.*?)</ss:Worksheet>', t, re.S)
    if not m:
        raise ValueError("no Holdings worksheet in XML spreadsheet")
    cells = [[html.unescape(c) for c in re.findall(r"<ss:Data[^>]*>([^<]*)</ss:Data>", r)]
             for r in re.findall(r"<ss:Row[^>]*>(.*?)</ss:Row>", m.group(1), re.S)]
    asof = next(_date(r[r.index("Fund Holdings as of") + 1], ["%b %d, %Y"])
                for r in cells[:8] if "Fund Holdings as of" in r)
    hi = next(i for i, r in enumerate(cells) if r and r[0] == "Name")
    hdr = cells[hi]
    rows = []
    for c in cells[hi + 1:]:
        if len(c) != len(hdr):
            continue
        r = dict(zip(hdr, c))
        if r.get("Asset Class") != "Fixed Income":
            continue
        rows.append(_row(r["Name"], r["Sector"], r["Weight (%)"], r["Price"], r["Yield to Worst (%)"],
                         r["Maturity"], r["Coupon (%)"], r["Par Value"], r["Market Value"], r.get("CUSIP")))
    return asof, rows


def _xlsx_rows(raw):
    z = zipfile.ZipFile(io.BytesIO(raw))
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", ns):
            shared.append("".join(x.text or "" for x in si.iter("{%s}t" % ns["m"])))
    sheet = sorted(n for n in z.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml", n))[0]
    out = []
    for row in ET.fromstring(z.read(sheet)).iter("{%s}row" % ns["m"]):
        vals = {}
        for c in row.findall("m:c", ns):
            col = re.match(r"[A-Z]+", c.get("r")).group(0)
            v = c.find("m:v", ns)
            if c.get("t") == "s" and v is not None:
                vals[col] = shared[int(v.text)]
            elif c.get("t") == "inlineStr":
                vals[col] = "".join(x.text or "" for x in c.iter("{%s}t" % ns["m"]))
            else:
                vals[col] = v.text if v is not None else None
        cols = sorted(vals, key=lambda k: (len(k), k))
        out.append([vals[k] for k in cols] if cols else [])
    return out


def parse_jnk_xlsx(raw):
    rows = _xlsx_rows(raw)
    asof = next(_date(r[1], ["%d-%b-%Y"]) for r in rows[:6] if r and r[0] == "Holdings:")
    hi = next(i for i, r in enumerate(rows) if r and r[0] == "Name")
    hdr = rows[hi]
    out = []
    for r in rows[hi + 1:]:
        if not r or not r[0]:
            continue
        d = dict(zip(hdr, r))
        par, mv = num(d.get("Par Value")), num(d.get("Market Value"))
        if num(d.get("Weight")) is None or not par:
            continue
        mat = d.get("Maturity") or ""
        try:
            mat = datetime.strptime(mat, "%m/%d/%Y").strftime("%b %d, %Y")
        except ValueError:
            pass
        out.append(_row(d["Name"], None, d["Weight"], mv / par * 100 if mv else None, None,
                        mat, d.get("Coupon"), par, mv, d.get("Identifier")))
    return asof, out


def sniff(raw):
    if raw[:2] == b"PK":
        return "xlsx"
    head = raw[:4096].decode("utf-8", errors="replace")
    if "<ss:Workbook" in head or "urn:schemas-microsoft-com:office:spreadsheet" in head:
        return "xls"
    if "Fund Holdings as of" in head:
        return "csv"
    raise ValueError("unrecognised holdings file (HTML error page?)")


def parse(raw):
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    kind = sniff(raw)
    return {"xlsx": parse_jnk_xlsx, "xls": parse_hyg_xls, "csv": parse_hyg_csv}[kind](raw)


def save(fund, raw, store=STORE):
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    kind = sniff(raw)
    asof, rows = parse(raw)
    if not rows:
        raise ValueError(f"{fund}: parsed 0 bond rows; not saving")
    d = Path(store) / fund
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{fund}_{asof}.{kind}.gz"
    if p.exists():
        same = hashlib.sha256(gzip.decompress(p.read_bytes())).digest() == hashlib.sha256(raw).digest()
        return p, asof, len(rows), ("already saved, identical" if same else "already saved, CONTENT DIFFERS (kept existing)")
    p.write_bytes(gzip.compress(raw, mtime=0))
    return p, asof, len(rows), "saved"


def resolve(spec, store=STORE):
    m = re.fullmatch(r"(HYG|JNK):(\d{4}-\d{2}-\d{2})", spec)
    if not m:
        return Path(spec)
    hits = sorted((Path(store) / m.group(1)).glob(f"{m.group(1)}_{m.group(2)}.*.gz"))
    if not hits:
        raise SystemExit(f"no saved file for {spec} under {store}")
    return hits[0]


def key(r):
    return (re.sub(r"\s+", " ", r["name"].replace(" Prvt", " 144A")).upper(), r["maturity"], r["coupon"])


def bucket_of(name, buckets):
    for b, rx in buckets:
        if rx.search(name.upper()):
            return b
    return "other"


def compare(base_rows, end_rows, buckets, min_ytw=None, max_price=None):
    a, b = {}, {}
    for r in base_rows:
        a.setdefault(key(r), r)
    for r in end_rows:
        b.setdefault(key(r), r)

    def in_sleeve(r):
        if min_ytw is not None and (r["ytw"] is None or r["ytw"] < min_ytw):
            return False
        if max_price is not None and (r["price"] is None or r["price"] >= max_price):
            return False
        return True

    sleeve = [k for k, r in a.items() if in_sleeve(r)]
    agg, names, skipped = {}, {}, []
    for k in sleeve:
        x, y = a[k], b.get(k)
        if not y or not x["price"] or not y["price"] or x["weight"] is None:
            skipped.append((x["name"], "unmatched" if not y else "no price/weight"))
            continue
        w = x["weight"]
        dp = (y["price"] / x["price"] - 1) * 100
        dy = (y["ytw"] - x["ytw"]) * 100 if (x["ytw"] is not None and y["ytw"] is not None) else None
        bk = bucket_of(x["name"], buckets)
        g = agg.setdefault(bk, dict(n=0, w=0.0, wdp=0.0, wdy=0.0, wy=0.0))
        g["n"] += 1; g["w"] += w; g["wdp"] += w * dp
        if dy is not None:
            g["wdy"] += w * dy; g["wy"] += w
        nm = re.sub(r" 144A$", "", x["name"])
        h = names.setdefault(nm, dict(bucket=bk, sector=x["sector"], w=0.0, wdp=0.0))
        h["w"] += w; h["wdp"] += w * dp
    return dict(sleeve=len(sleeve), sleeve_w=sum(a[k]["weight"] or 0 for k in sleeve),
                agg=agg, names=names, skipped=skipped,
                unmatched_total=len(set(a) - set(b)))


def report(res, base_label, end_label, top=20, tsv=None):
    agg = res["agg"]
    tw = sum(g["w"] for g in agg.values()) or 1
    tp = sum(g["wdp"] for g in agg.values()) or float("nan")
    ty = sum(g["wdy"] for g in agg.values()) or float("nan")
    print(f"{base_label} -> {end_label}: sleeve {res['sleeve']} lines, {res['sleeve_w']:.2f}% of fund; "
          f"computed {sum(g['n'] for g in agg.values())}; skipped {len(res['skipped'])}; "
          f"base lines absent from end file (whole fund) {res['unmatched_total']}")
    for nm, why in res["skipped"]:
        print(f"  SKIPPED {nm} ({why})")
    hdr = ["bucket", "n", "weight_pct", "weight_share", "avg_dytw_bp", "dytw_share", "avg_dpx_pct", "dpx_share"]
    out = []
    for bk in sorted(agg):
        g = agg[bk]
        out.append([bk, g["n"], round(g["w"], 3), round(g["w"] / tw * 100, 1),
                    round(g["wdy"] / g["wy"], 0) if g["wy"] else "", round(g["wdy"] / ty * 100, 1) if g["wy"] else "",
                    round(g["wdp"] / g["w"], 2), round(g["wdp"] / tp * 100, 1)])
    print("\t".join(hdr))
    for r in out:
        print("\t".join(str(v) for v in r))
    print(f"TOTAL avg dPx {tp / tw:.2f}%")
    print(f"--- top {top} names by price contribution (weight x dPx); share = of sleeve total")
    for nm, h in sorted(res["names"].items(), key=lambda z: z[1]["wdp"])[:top]:
        print(f"  {nm[:42]:42s} {h['bucket']:11s} {str(h['sector'] or '')[:22]:22s} w={h['w']:.2f} "
              f"dPx={h['wdp'] / h['w']:7.2f}% share={h['wdp'] / tp * 100:5.1f}%")
    if tsv:
        with open(tsv, "w", newline="") as f:
            wr = csv.writer(f, delimiter="\t", lineterminator="\n")
            wr.writerow(hdr); wr.writerows(out)
        print(f"wrote {tsv}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=str(STORE), help="store directory (default research/etf_holdings)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pull"); p.add_argument("--fund", nargs="+", default=["HYG", "JNK"], choices=list(URLS))
    p = sub.add_parser("import"); p.add_argument("file"); p.add_argument("--fund", required=True, choices=list(URLS))
    sub.add_parser("list")
    p = sub.add_parser("compare"); p.add_argument("base"); p.add_argument("end")
    p.add_argument("--min-ytw", type=float); p.add_argument("--max-price", type=float)
    p.add_argument("--bucket", action="append", default=[], metavar="NAME=REGEX")
    p.add_argument("--top", type=int, default=20); p.add_argument("--tsv")
    a = ap.parse_args(argv)

    if a.cmd == "pull":
        rc = 0
        for fund in a.fund:
            try:
                path, asof, n, status = save(fund, fetch(URLS[fund]), a.dir)
                print(f"{fund}\tas of {asof}\t{n} bonds\t{status}\t{path}")
            except Exception as e:
                print(f"{fund}\tFAILED\t{e}", file=sys.stderr); rc = 1
        return rc
    if a.cmd == "import":
        path, asof, n, status = save(a.fund, Path(a.file).read_bytes(), a.dir)
        print(f"{a.fund}\tas of {asof}\t{n} bonds\t{status}\t{path}")
        return 0
    if a.cmd == "list":
        for p in sorted(Path(a.dir).glob("*/*.gz")):
            print(p.name)
        return 0
    if a.cmd == "compare":
        buckets = [(b, re.compile(rx)) for b, rx in BUCKETS]
        if a.bucket:
            buckets = [(s.split("=", 1)[0], re.compile(s.split("=", 1)[1])) for s in a.bucket]
        if a.min_ytw is not None and any("JNK" in str(s) for s in (a.base, a.end)):
            print("note: JNK has no YTW column; --min-ytw selects nothing there (use --max-price)", file=sys.stderr)
        pb, pe = resolve(a.base, a.dir), resolve(a.end, a.dir)
        (ab, rb), (ae, re_) = parse(pb.read_bytes()), parse(pe.read_bytes())
        report(compare(rb, re_, buckets, a.min_ytw, a.max_price), f"{pb.name} (as of {ab})", f"{pe.name} (as of {ae})",
               a.top, a.tsv)
        return 0


if __name__ == "__main__":
    sys.exit(main())
