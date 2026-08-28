#!/usr/bin/env python3
"""
SEC EDGAR document reader + XBRL facts — the "actually READ the 10-Q" companion
to edgar_fetch.py (which only lists filings). Closes the BACKLOG.md "EDGAR 403s
on WebFetch" blocker: SEC.gov blocks generic WebFetch UAs, but a declared
User-Agent over urllib works fine. Stdlib only.

Usage:
  # 1) Full-text search across EDGAR (EFTS) — find the filing + snippet
  python3 edgar_doc.py search "geographic concentration" --cik 0001212545 --forms 10-Q
  python3 edgar_doc.py search "Florida" --forms 10-Q --startdt 2026-01-01 --enddt 2026-06-30

  # 2) Read a filing's primary document as TEXT (HTML stripped) — grep optional
  python3 edgar_doc.py doc --cik 0001212545 --accession 0001212545-26-000045
  python3 edgar_doc.py doc --cik 0001212545 --accession 0001212545-26-000045 --grep "Florida"

  # 3) Pull a structured XBRL fact (companyconcept) — bank credit metrics etc.
  python3 edgar_doc.py facts --cik 0001212545 --concept Assets
  python3 edgar_doc.py facts --cik 0001212545 --concept FinancingReceivableAllowanceForCreditLosses

Useful us-gaap concepts for bank credit work:
  Assets, Deposits, FinancingReceivableAllowanceForCreditLosses,
  ProvisionForLoanLeaseAndOtherLosses, FinancingReceivableExcludingAccruedInterestBeforeAllowanceForCreditLoss,
  AllowanceForDoubtfulAccountsReceivable
  (Names drift across filers — use `search` to confirm a tag exists, or pull
   the full set via the companyfacts endpoint, see xbrl_facts(all=True).)

CIK cheatsheet + ticker->CIK authority: see edgar_fetch.py header /
https://www.sec.gov/files/company_tickers.json  (always verify before citing).
"""

import json, sys, argparse, urllib.request, urllib.parse, urllib.error, re
from html.parser import HTMLParser

# SEC requires a declared User-Agent (with contact). This is the whole 403 fix.
UA = "Research DEWEY williepowen@gmail.com"
HJSON = {"User-Agent": UA, "Accept": "application/json"}
HHTML = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"}

EFTS = "https://efts.sec.gov/LATEST/search-index?{}"
ARCH = "https://www.sec.gov/Archives/edgar/data/{cik}/{acc}"
CONCEPT = "https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{concept}.json"
FACTS = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"


class EdgarError(Exception):
    """A reportable EDGAR failure — never a traceback.

    A transport error is a RESULT (404 = no such CIK/accession, 403 = UA wall),
    and a traceback reads to the caller as "the tool is broken" rather than
    "that document does not exist". Class fixed in fetch_url.py 2026-08-02 and
    edgar_fetch.py 2026-08-27; swept here the same day per the BACKLOG row's
    own instruction to fix the CLASS, not the instance.
    """


def _get(url, headers, timeout=30):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        hint = ""
        if e.code == 404:
            hint = "\n  not found — verify the CIK/accession/concept exists"
        elif e.code in (403, 401):
            hint = ("\n  sec.gov wants a DECLARED-CONTACT User-Agent "
                    "('Research NAME email'); a browser UA is 403'd here")
        elif e.code == 429:
            hint = "\n  SEC rate limit — slow down and retry"
        raise EdgarError(f"HTTP {e.code} for {url}{hint}") from e
    except urllib.error.URLError as e:
        raise EdgarError(f"transport error for {url}: "
                         f"{type(e.reason).__name__}: {e.reason}") from e


def _cik10(cik):
    return cik.lstrip("0").zfill(10)


class _Text(HTMLParser):
    """Strip HTML to readable text; drop script/style; keep block breaks."""
    def __init__(self):
        super().__init__()
        self.out = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "br", "div", "tr", "li", "h1", "h2", "h3", "table"):
            self.out.append("\n")
    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            t = data.strip()
            if t:
                self.out.append(t + " ")
    def text(self):
        s = "".join(self.out)
        s = re.sub(r"[ \t]+", " ", s)
        s = re.sub(r"\n\s*\n\s*\n+", "\n\n", s)
        return s.strip()


def search(query, cik=None, forms=None, startdt=None, enddt=None, limit=10):
    params = {"q": query}
    if cik:
        params["ciks"] = _cik10(cik)
    if forms:
        params["forms"] = forms
    if startdt and enddt:
        params["dateRange"] = "custom"
        params["startdt"] = startdt
        params["enddt"] = enddt
    data = json.loads(_get(EFTS.format(urllib.parse.urlencode(params)), HJSON))
    hits = data.get("hits", {}).get("hits", [])
    out = []
    for h in hits[:limit]:
        src = h.get("_source", {})
        _id = h.get("_id", "")  # "accession:document"
        acc = _id.split(":")[0] if ":" in _id else ""
        doc = _id.split(":")[1] if ":" in _id else ""
        out.append({
            "accession": acc,
            "doc": doc,
            "form": src.get("file_type") or (src.get("root_forms") or [""])[0],
            "date": src.get("file_date", ""),
            "display_names": src.get("display_names", []),
        })
    return data.get("hits", {}).get("total", {}).get("value", 0), out


def _int(v):
    """size fields come back as '' on some accessions — int('') is a ValueError."""
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0


def list_documents(cik, accession):
    """Every document filename in an accession, best-effort.

    ⚠️ `index.json` CANNOT BE TRUSTED ALONE — on some accessions it returns
    HTTP 200 with a `directory.item` list containing ONLY the wrapper files
    (`-index.html`, `-index-headers.html`, `.txt`, `-xbrl.zip`) and OMITS every
    real document and exhibit. Verified 2026-08-27 on CRMT 8-K
    0001171843-26-004311, where index.json hid exh_101/102/103 — and exh_101
    was the conformed credit agreement carrying that run's entire answer.
    The failure is a FALSE NEGATIVE with a clean 200, so an exhibit-discovery
    negative taken from index.json is not evidence of absence.

    So: read index.json, then ALSO parse `-index.html` for /Archives/ hrefs and
    merge. The HTML index is the authoritative listing.
    """
    base = ARCH.format(cik=cik.lstrip("0"), acc=accession.replace("-", ""))
    names = {}
    try:
        idx = json.loads(_get(base + "/index.json", HJSON))
        for i in idx.get("directory", {}).get("item", []):
            n = i.get("name", "")
            if n:
                names[n] = _int(i.get("size"))
    except (EdgarError, ValueError):
        pass                                   # HTML index below is the fallback
    try:
        html = _get(f"{base}/{accession}-index.html", HHTML).decode("utf-8", "replace")
        # ⚠️ TWO href shapes. Inline-XBRL PRIMARY documents are linked through the
        # viewer as `/ix?doc=/Archives/...`, NOT as a bare /Archives/ href — so a
        # regex matching only the bare form finds every exhibit but MISSES the
        # primary document, and _primary_doc then falls back to a wrapper file.
        for href in re.findall(r'href="(?:/ix\?doc=)?(/Archives/[^"?]+)"', html):
            n = href.rsplit("/", 1)[-1]
            names.setdefault(n, 0)
    except EdgarError:
        pass
    if not names:
        raise EdgarError(f"no documents listed for {accession} (cik {cik}) — "
                         "verify the accession exists")
    return names


def _primary_doc(cik, accession):
    names = list_documents(cik, accession)
    # prefer the largest .htm that isn't the index / R-exhibit / cover
    cands = [n for n in names if n.lower().endswith((".htm", ".html"))]
    filtered = [n for n in cands if not re.match(r"(R\d|.*index|.*\bex)", n, re.I)]
    cands = filtered or cands
    cands.sort(key=lambda n: names[n], reverse=True)
    return cands[0] if cands else None


# --- XBRL context-header strip -------------------------------------------
# Every modern 10-K/10-Q text extract opens with thousands of XBRL context
# tokens (CIKs, ISO dates, `us-gaap:CommonStockMember`, `xbrli:shares`, …)
# BEFORE any narrative. A --grep for a common term ("guarantee", "Revenue",
# "debt") matches inside that block and buries the real footnote hits — and a
# grep drowned in header noise looks identical to one that legitimately found
# nothing. Cost 2 wasted calls on the 2026-08-02 DR-1 run; stripped by default
# since nobody greps a filing wanting the context block.
_XBRL_TOKEN = re.compile(
    r"^("
    r"\d{7,}"                        # bare CIK
    r"|\d{4}-\d{2}-\d{2}"            # ISO date
    r"|[A-Za-z][\w.\-]*:[\w.\-]+"     # namespaced: us-gaap:X, xbrli:shares, iso4217:USD
    r"|https?://\S*fasb\.org\S*"      # taxonomy URIs
    r"|P\d+[YMD]"                    # ISO durations (P1Y, P3Y)
    r"|[\d,.]+"                      # bare numerics
    r"|true|false"
    r")$"
)


# A line must carry at least one DISTINCTIVELY-XBRL token to be strippable.
# Without this guard a 4-cell all-numeric row ("46,751 39,721 37,608 12,443")
# scores 100% density and a financial table row gets eaten — the failure that
# would matter most, since those rows are exactly what a filing run is after.
# In practice EDGAR's HTML→text emits one cell per line so they fall under
# min_tokens anyway, but belt-and-braces: numbers alone can never strip a line.
_XBRL_DISTINCTIVE = re.compile(
    r"^([A-Za-z][\w.\-]*:[\w.\-]+|https?://\S*fasb\.org\S*|P\d+[YMD])$")


def _is_xbrl_noise(line, min_tokens=4, density=0.6):
    toks = line.split()
    if len(toks) < min_tokens:
        return False
    if not any(_XBRL_DISTINCTIVE.match(t) for t in toks):
        return False
    hits = sum(1 for t in toks if _XBRL_TOKEN.match(t))
    return hits / len(toks) >= density


def strip_xbrl(text):
    """Drop XBRL context lines. Returns (clean_text, lines_dropped)."""
    kept, dropped = [], 0
    for line in text.split("\n"):
        if _is_xbrl_noise(line):
            dropped += 1
        else:
            kept.append(line)
    return "\n".join(kept), dropped


def doc_text(cik, accession, doc=None):
    acc_nodash = accession.replace("-", "")
    if not doc:
        doc = _primary_doc(cik, accession)
        if not doc:
            return None, "no primary .htm found in filing index"
    url = ARCH.format(cik=cik.lstrip("0"), acc=acc_nodash) + "/" + doc
    raw = _get(url, HHTML).decode("utf-8", "replace")
    p = _Text()
    p.feed(raw)
    return doc, p.text()


def xbrl_concept(cik, concept):
    url = CONCEPT.format(cik=_cik10(cik), concept=concept)
    data = json.loads(_get(url, HJSON))
    units = data.get("units", {})
    rows = []
    for unit, vals in units.items():
        for v in vals:
            rows.append({"unit": unit, "end": v.get("end"), "val": v.get("val"),
                         "fy": v.get("fy"), "fp": v.get("fp"), "form": v.get("form"),
                         "filed": v.get("filed")})
    rows.sort(key=lambda r: (r.get("end") or "", r.get("filed") or ""))
    return data.get("entityName", ""), data.get("label", concept), rows


def main():
    ap = argparse.ArgumentParser(description="EDGAR document reader + XBRL facts")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--cik"); s.add_argument("--forms")
    s.add_argument("--startdt"); s.add_argument("--enddt")
    s.add_argument("--limit", type=int, default=10)

    d = sub.add_parser("doc")
    d.add_argument("--cik", required=True); d.add_argument("--accession", required=True)
    d.add_argument("--doc"); d.add_argument("--grep"); d.add_argument("--context", type=int, default=2)
    d.add_argument("--max", type=int, default=0, help="truncate output to N chars (0=full)")
    d.add_argument("--keep-xbrl", action="store_true",
                   help="do NOT strip the XBRL context header (stripped by default — it buries every grep)")

    f = sub.add_parser("facts")
    f.add_argument("--cik", required=True); f.add_argument("--concept", required=True)
    f.add_argument("--last", type=int, default=8)

    a = ap.parse_args()

    if a.cmd == "search":
        total, hits = search(a.query, a.cik, a.forms, a.startdt, a.enddt, a.limit)
        print(f"\n=== EFTS '{a.query}' — {total} total, showing {len(hits)} ===\n")
        for h in hits:
            who = "; ".join(h["display_names"])[:70]
            print(f"  {h['date']}  {h['form']:<8} {h['accession']}  {who}")
            print(f"           doc: {h['doc']}")

    elif a.cmd == "doc":
        name, text = doc_text(a.cik, a.accession, a.doc)
        if text is None:
            print("ERROR:", name); return
        note = ""
        if not a.keep_xbrl:
            text, dropped = strip_xbrl(text)
            if dropped:
                note = f"  [XBRL context: {dropped:,} lines stripped — --keep-xbrl to retain]"
        print(f"\n=== {name}  ({len(text):,} chars ){note}===\n")
        if a.grep:
            lines = text.split("\n")
            pat = re.compile(a.grep, re.I)
            n = 0
            for i, ln in enumerate(lines):
                if pat.search(ln):
                    n += 1
                    lo, hi = max(0, i - a.context), min(len(lines), i + a.context + 1)
                    print("\n".join(lines[lo:hi]))
                    print("  ---")
            if n == 0:
                # An explicit negative is the product. A silent empty result is
                # indistinguishable from a failed read — say so, and exit 1.
                sys.stderr.write(
                    f"NO MATCH for /{a.grep}/ in {name} "
                    f"({len(text):,} chars searched, {len(lines):,} lines)\n")
                sys.exit(1)
        else:
            print(text[:a.max] if a.max else text)

    elif a.cmd == "facts":
        ent, label, rows = xbrl_concept(a.cik, a.concept)
        print(f"\n=== {ent} — {label} ({a.concept}) ===\n")
        for r in rows[-a.last:]:
            print(f"  {r['end']}  {r['fp']} {r['fy']}  {r['form']:<6}  {r['unit']:>4}  {r['val']:,}")


if __name__ == "__main__":
    try:
        sys.exit(main() or 0)
    except EdgarError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)
