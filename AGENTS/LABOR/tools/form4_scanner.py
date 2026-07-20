#!/usr/bin/env python3
"""
form4_scanner — SEC EDGAR Form 4 (insider transaction) pull + LABOR's 14x sell/buy framework.

WHAT THIS DOES (and honestly does NOT do):
  - RESOLVES a ticker -> CIK via SEC's official company_tickers.json (free, no key).
  - PULLS the last N days of Form 4 filings for that CIK from data.sec.gov/submissions
    (free, UA-headed — gov sites 403 without a declared User-Agent; see auto-memory
    finding_edgar_403_user_agent_header). This WORKS live.
  - PARSES each filing's primary XML (Table I non-derivative transactions): reporting
    owner, relationship, transaction code, shares, price, acquired/disposed.
  - SCORES per LABOR's 14x framework: open-market sell $ / open-market buy $ (codes P=buy,
    S=sell only — awards/grants/exercises/gifts/tax-withholding are NOT counted as market
    conviction, they're compensation mechanics). >2.5x = peer-elevated, >=14x = LABOR's
    historical layoff-lead threshold (3-6mo lead per Feb-28 framework note).
  - If a filing's XML fails to fetch/parse, it is reported as UNPARSED with the accession
    number — NOT silently dropped and NOT estimated. Cluster/anomaly read is built only from
    what actually parsed. No fabricated interpretation layer.

WHAT THIS DOES NOT DO:
  - No historical/backtested peer 2.5x baseline computation (that needs a sector universe
    pull, out of scope for tonight's build) — the 2.5x/14x thresholds are cited from LABOR's
    existing framework (STATUS.md / CLAUDE.md Research Toolkit), not re-derived here.
  - No price/market-cap normalization across issuers — $ sold is nominal per-filing.

Usage:
  python3 form4_scanner.py scan WAL --days 90            # ticker -> CIK -> Form 4 pull + score
  python3 form4_scanner.py scan OZK --days 90 --json
  python3 form4_scanner.py cik WAL                        # just resolve ticker -> CIK

Run with the repo-root venv:
  /home/willi/Research-workspace/.venv/bin/python3 AGENTS/LABOR/tools/form4_scanner.py scan WAL --days 90
"""

import argparse, gzip, json, sys, time, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, date

UA = "LABOR-research williepowen@gmail.com"
DATA_BASE = "https://data.sec.gov"
WWW_BASE = "https://www.sec.gov"
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"

# LABOR framework thresholds (STATUS.md / CLAUDE.md Research Toolkit — not re-derived here)
PEER_RATIO = 2.5
LEAD_RATIO = 14.0

# Transaction codes counted as genuine open-market conviction (Table I, Section 16 form)
BUY_CODES = {"P"}   # open-market purchase
SELL_CODES = {"S"}  # open-market sale
# Excluded from ratio (compensation mechanics, not conviction): A (award/grant), M (option
# exercise), F (tax withholding), G (gift), C (conversion), X (option exercise-related).


def _get(url, retries=3, backoff=1.5, timeout=25):
    """UA-headed GET with SSL/transient retry (per DEWEY trace_bond.py reference shape)."""
    headers = {"User-Agent": UA, "Accept-Encoding": "gzip, deflate"}
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                if resp.info().get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
                return raw
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            last = e
            if attempt < retries - 1:
                time.sleep(backoff * (attempt + 1))
    raise last


_TICKER_CACHE = None


def resolve_cik(ticker):
    """SEC company_tickers.json: ticker -> (10-digit zero-padded CIK, company title)."""
    global _TICKER_CACHE
    if _TICKER_CACHE is None:
        raw = _get(TICKERS_URL)
        _TICKER_CACHE = json.loads(raw)
    ticker_u = ticker.upper()
    for row in _TICKER_CACHE.values():
        if row.get("ticker", "").upper() == ticker_u:
            return str(row["cik_str"]).zfill(10), row.get("title")
    return None, None


def get_form4_filings(cik, days=90):
    """Recent Form 4 filings for a CIK from data.sec.gov/submissions, filtered to `days` back.
    Returns (filings, meta) where meta carries the submissions record's own
    `insiderTransactionForIssuerExists` flag + entityType + name — SEC's own signal for
    whether this CIK is a genuine Form-4 issuer at all. A CIK with the flag false will
    always return 0 filings; that is NOT the same as "0 insider activity" (see scan()) —
    verified live 2026-07-09: OZK's ticker->CIK resolution (company_tickers.json, confirmed
    independently via the legacy ticker.txt file AND browse-edgar's own CIK-by-ticker lookup)
    lands on a CIK that is a trust/investment-manager filer (13F-HR/SC 13G only) for Bank OZK,
    NOT the bank's Form-4 issuer identity — that flag is 0 there. The bank's actual former
    SEC issuer CIK (0001038205, "BANK OF THE OZARKS INC") stopped filing entirely in Feb 2022
    (its own 10-K/Form-4 stream ends then, alongside 425/S-4 merger-communication forms in the
    same window) — consistent with Bank OZK (FDIC Cert #110, FDIC-confirmed active, $41.66B
    assets per FDIC BankFind, live-checked 2026-07-09) moving to FDIC substituted-compliance
    reporting under Exchange Act §12(i) rather than direct SEC/EDGAR reporting. Net: OZK's
    current insider transactions are NOT retrievable via SEC EDGAR by this tool — a real
    coverage gap, not a bug, and not something to paper over with a silent zero.

    UPDATE 2026-07-20: the FDIC backend closes this gap. OZK files Form 3/4/5 with the FDIC
    (cert #110) at securitiesfilings.fdicconnect.fdic.gov/api/instdiscl/cert/110 (browser UA
    required, same trick as EDGAR) — live-proven this session (469 records; newest 6/15/2026).
    The OZK agent's curated tracker `AGENTS/OZK/INSIDERS/SELLING.md` is the interpretation
    layer. Per PROME's 7/10 spec this FDIC path should become a code fallback here (fall back
    by cert# when insiderTransactionForIssuerExists=False); as of 7/20 that INTEGRATION IS
    STILL OWED — the fallback was run manually, this tool still emits only the fail-loud
    warning below for OZK-class FDIC-supervised issuers."""
    url = f"{DATA_BASE}/submissions/CIK{cik}.json"
    data = json.loads(_get(url))
    meta = {
        "name": data.get("name"),
        "entityType": data.get("entityType"),
        "insiderTransactionForIssuerExists": bool(data.get("insiderTransactionForIssuerExists")),
    }
    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accessions = recent.get("accessionNumber", [])
    primary_docs = recent.get("primaryDocument", [])
    cutoff = date.today() - timedelta(days=days)
    out = []
    for i, form in enumerate(forms):
        if form != "4":
            continue
        try:
            fdate = datetime.strptime(dates[i], "%Y-%m-%d").date()
        except (ValueError, IndexError):
            continue
        if fdate < cutoff:
            continue
        out.append({
            "accession": accessions[i],
            "date": dates[i],
            "primary_doc": primary_docs[i] if i < len(primary_docs) else None,
        })
    # NOTE: EDGAR "recent" only holds the newest ~1000 filings company-wide; for the tickers
    # this scanner targets (WAL/OZK/ZION Form-4 volume), 90 days is well within that window.
    return out, meta


def fetch_filing(cik_int, accession, primary_doc):
    """Fetch the RAW Form 4 XML for a filing.

    submissions.json's `primaryDocument` field (e.g. "xslF345X06/wk-form4_....xml") points
    at SEC's XSLT-RENDERED HTML view, not the raw XML — same filename, but under an
    `xslF345X##/` subpath the EDGAR server special-cases to serve rendered HTML. Verified live
    2026-07-09 (WAL CIK 1212545, accession 0001628280-26-044008): fetching that path returned
    a `<!DOCTYPE html>` document, which then broke ElementTree parsing ("mismatched tag") on
    every filing — a silent-failure bug caught only by testing on live data, not by unit logic.
    The actual raw XML lives at the SAME basename one directory up (no xslF345X##/ prefix) —
    confirmed via the filing's EDGAR index page. Try that first; {accession}.xml is a fallback
    for older filing conventions. Returns (xml_bytes, url) or (None, url)."""
    acc_nodash = accession.replace("-", "")
    base = f"{WWW_BASE}/Archives/edgar/data/{cik_int}/{acc_nodash}"
    candidates = []
    if primary_doc:
        candidates.append(f"{base}/{primary_doc.rsplit('/', 1)[-1]}")  # strip xslF345X##/ prefix
    candidates.append(f"{base}/{accession}.xml")
    last_url = candidates[0]
    for url in candidates:
        last_url = url
        try:
            return _get(url), url
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
            continue
    return None, last_url


def _text(el, path, default=None):
    node = el.find(path)
    if node is None:
        return default
    val = node.find("value")
    if val is not None and val.text is not None:
        return val.text.strip()
    if node.text is not None:
        return node.text.strip()
    return default


def parse_form4(xml_bytes):
    """Parse ownershipDocument XML -> dict of owner info + non-derivative transaction rows.
    Raises on malformed XML — caller records as UNPARSED, does not guess."""
    root = ET.fromstring(xml_bytes)
    owner_name = _text(root, ".//reportingOwner/reportingOwnerId/rptOwnerName", "UNKNOWN")
    rel = root.find(".//reportingOwner/reportingOwnerRelationship")
    is_officer = _text(rel, "isOfficer") == "1" if rel is not None else False
    is_director = _text(rel, "isDirector") == "1" if rel is not None else False
    is_ten_pct = _text(rel, "isTenPercentOwner") == "1" if rel is not None else False
    officer_title = _text(rel, "officerTitle", "") if rel is not None else ""
    roles = []
    if is_director:
        roles.append("Director")
    if is_officer:
        roles.append(officer_title or "Officer")
    if is_ten_pct:
        roles.append("10%+ Owner")

    txns = []
    for t in root.findall(".//nonDerivativeTable/nonDerivativeTransaction"):
        code = _text(t, "transactionCoding/transactionCode")
        tdate = _text(t, "transactionDate")
        shares_s = _text(t, "transactionAmounts/transactionShares")
        price_s = _text(t, "transactionAmounts/transactionPricePerShare")
        ad_code = _text(t, "transactionAmounts/transactionAcquiredDisposedCode")
        shares_after_s = _text(t, "postTransactionAmounts/sharesOwnedFollowingTransaction")
        try:
            shares = float(shares_s) if shares_s else None
        except ValueError:
            shares = None
        try:
            price = float(price_s) if price_s else None
        except ValueError:
            price = None
        try:
            shares_after = float(shares_after_s) if shares_after_s else None
        except ValueError:
            shares_after = None
        txns.append({
            "code": code, "date": tdate, "shares": shares, "price": price,
            "acquired_disposed": ad_code, "shares_after": shares_after,
        })
    return {"owner": owner_name, "roles": roles, "transactions": txns}


def scan(ticker, days=90):
    cik, title = resolve_cik(ticker)
    if not cik:
        return {"ticker": ticker, "error": "CIK not resolved via company_tickers.json"}
    cik_int = int(cik)
    filings, cik_meta = get_form4_filings(cik, days=days)
    cik_warning = None
    if not filings and not cik_meta["insiderTransactionForIssuerExists"]:
        cik_warning = (
            f"SEC's own submissions record for CIK {cik} ('{cik_meta['name']}', "
            f"entityType={cik_meta['entityType'] or 'BLANK'}) reports "
            f"insiderTransactionForIssuerExists=False — this CIK has NEVER been a Form-4 "
            f"issuer. The company_tickers.json ticker->CIK resolution for '{ticker}' likely "
            f"landed on the wrong entity (e.g. a trust/investment-manager filer sharing the "
            f"company name), or this issuer reports insider transactions outside SEC EDGAR "
            f"(e.g. FDIC substituted compliance, Exchange Act §12(i)). DO NOT read '0 "
            f"filings' below as '0 insider activity' — it means this ticker's Form-4s (if any "
            f"exist) are not retrievable via this tool's SEC EDGAR pull."
        )

    parsed_filings = []
    unparsed = []
    for f in filings:
        xml_bytes, url = fetch_filing(cik_int, f["accession"], f["primary_doc"])
        if xml_bytes is None:
            unparsed.append({"accession": f["accession"], "date": f["date"],
                              "reason": "fetch failed (all candidate URLs)", "url": url})
            continue
        try:
            parsed = parse_form4(xml_bytes)
        except ET.ParseError as e:
            unparsed.append({"accession": f["accession"], "date": f["date"],
                              "reason": f"XML parse error: {e}", "url": url})
            continue
        parsed["accession"] = f["accession"]
        parsed["filing_date"] = f["date"]
        parsed["url"] = url
        parsed_filings.append(parsed)

    buy_shares = buy_value = sell_shares = sell_value = 0.0
    buy_events, sell_events = [], []
    insiders_buying, insiders_selling = set(), set()
    other_code_counts = {}

    for pf in parsed_filings:
        for t in pf["transactions"]:
            code = t["code"]
            if code in BUY_CODES and t["shares"] and t["price"]:
                buy_shares += t["shares"]
                buy_value += t["shares"] * t["price"]
                insiders_buying.add(pf["owner"])
                buy_events.append({"owner": pf["owner"], "roles": pf["roles"], "date": t["date"],
                                    "shares": t["shares"], "price": t["price"],
                                    "value": t["shares"] * t["price"], "accession": pf["accession"]})
            elif code in SELL_CODES and t["shares"] and t["price"]:
                sell_shares += t["shares"]
                sell_value += t["shares"] * t["price"]
                insiders_selling.add(pf["owner"])
                sell_events.append({"owner": pf["owner"], "roles": pf["roles"], "date": t["date"],
                                     "shares": t["shares"], "price": t["price"],
                                     "value": t["shares"] * t["price"], "accession": pf["accession"]})
            elif code:
                other_code_counts[code] = other_code_counts.get(code, 0) + 1

    ratio = (sell_value / buy_value) if buy_value > 0 else (float("inf") if sell_value > 0 else None)

    # Cluster read: 3+ distinct insiders selling within any rolling 14-day window
    cluster_flag = False
    cluster_detail = None
    sell_dates = sorted({e["date"] for e in sell_events if e["date"]})
    for d in sell_dates:
        try:
            d0 = datetime.strptime(d, "%Y-%m-%d").date()
        except ValueError:
            continue
        window_owners = {e["owner"] for e in sell_events if e["date"] and
                          0 <= (d0 - datetime.strptime(e["date"], "%Y-%m-%d").date()).days <= 14}
        if len(window_owners) >= 3:
            cluster_flag = True
            cluster_detail = f"{len(window_owners)} distinct insiders sold within 14d of {d}"
            break

    return {
        "ticker": ticker, "cik": cik, "company": title, "days_window": days,
        "cik_warning": cik_warning,
        "filings_found": len(filings), "filings_parsed": len(parsed_filings),
        "filings_unparsed": unparsed,
        "buy_shares": buy_shares, "buy_value": buy_value, "buy_events": len(buy_events),
        "sell_shares": sell_shares, "sell_value": sell_value, "sell_events": len(sell_events),
        "insiders_buying": sorted(insiders_buying), "insiders_selling": sorted(insiders_selling),
        "sell_buy_ratio": ratio,
        "peer_elevated": (ratio is not None and ratio not in (float("inf"),) and ratio >= PEER_RATIO)
                          or ratio == float("inf"),
        "lead_threshold_fired": (ratio is not None and ratio not in (float("inf"),) and ratio >= LEAD_RATIO)
                                 or (ratio == float("inf") and sell_value > 0),
        "cluster_flag": cluster_flag, "cluster_detail": cluster_detail,
        "other_code_counts": other_code_counts,
        "buy_events_detail": buy_events, "sell_events_detail": sell_events,
    }


def _fmt_money(v):
    return f"${v:,.0f}"


def _fmt_report(r):
    if "error" in r:
        return f"=== {r['ticker']} === ERROR: {r['error']}"
    lines = []
    lines.append(f"=== {r['ticker']} ({r['company']}, CIK {r['cik']}) — Form 4, last {r['days_window']}d ===")
    if r.get("cik_warning"):
        lines.append(f"⚠️  DATA-QUALITY WARNING: {r['cik_warning']}")
    lines.append(f"Filings found: {r['filings_found']} | parsed: {r['filings_parsed']} | unparsed: {len(r['filings_unparsed'])}")
    if r["filings_unparsed"]:
        for u in r["filings_unparsed"]:
            lines.append(f"  UNPARSED accession={u['accession']} date={u['date']} reason={u['reason']}")
    lines.append(f"Open-market BUYS  (code P): {r['buy_events']} txns, {r['buy_shares']:,.0f} sh, {_fmt_money(r['buy_value'])} | insiders: {', '.join(r['insiders_buying']) or '(none)'}")
    lines.append(f"Open-market SELLS (code S): {r['sell_events']} txns, {r['sell_shares']:,.0f} sh, {_fmt_money(r['sell_value'])} | insiders: {', '.join(r['insiders_selling']) or '(none)'}")
    ratio = r["sell_buy_ratio"]
    if ratio is None:
        ratio_s = "n/a (no buys, no sells)"
    elif ratio == float("inf"):
        ratio_s = "INF (sells with zero open-market buys)"
    else:
        ratio_s = f"{ratio:.1f}x"
    lines.append(f"Sell/Buy $ ratio: {ratio_s}  [peer threshold {PEER_RATIO}x | LABOR lead threshold {LEAD_RATIO}x]")
    lines.append(f"  Peer-elevated (>= {PEER_RATIO}x): {'YES' if r['peer_elevated'] else 'no'}")
    lines.append(f"  Lead-threshold fired (>= {LEAD_RATIO}x): {'YES' if r['lead_threshold_fired'] else 'no'}")
    lines.append(f"Cluster (3+ distinct insiders selling within 14d): {'YES — ' + r['cluster_detail'] if r['cluster_flag'] else 'no'}")
    if r["other_code_counts"]:
        lines.append(f"Other txn codes seen (excluded from ratio, comp mechanics): {r['other_code_counts']}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="SEC Form 4 insider-transaction scanner + LABOR 14x framework")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("cik", help="ticker -> CIK")
    c.add_argument("ticker")

    s = sub.add_parser("scan", help="ticker -> Form 4 pull + 14x score")
    s.add_argument("ticker")
    s.add_argument("--days", type=int, default=90)
    s.add_argument("--json", action="store_true")

    a = ap.parse_args()
    try:
        if a.cmd == "cik":
            cik, title = resolve_cik(a.ticker)
            print(json.dumps({"ticker": a.ticker, "cik": cik, "company": title}, indent=2))
        elif a.cmd == "scan":
            r = scan(a.ticker, days=a.days)
            print(json.dumps(r, indent=2) if a.json else _fmt_report(r))
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
