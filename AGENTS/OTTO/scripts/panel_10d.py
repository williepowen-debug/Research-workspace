#!/usr/bin/env python3
"""
OTTO — Subprime auto ABS performance panel, built from SEC 10-D trustee reports.

WHY THIS EXISTS
  OTTO's subprime performance read came from the Fitch Auto ABS Index, reached only
  through a free trade-press mirror. That mirror decayed (2026: latest obtainable data
  was MARCH), and the paid alternatives were tested 2026-07-25 and are closed —
  S&P's tracker returns HTTP 403, KBRA's full indices spreadsheet requires an ABS
  Premium subscription. Rather than depend on a republication of someone else's index,
  this builds the series from the same primary documents the agencies use.

  Second reason, and the better one: the Fitch index is a BLEND whose composition is
  dominated by Santander's very large, much cleaner deals. That composition bias is
  what broke OTTO-04 — deep-subprime 2022 collateral was >25% CNL while the blended
  index tracked toward ~24.3%. A self-built panel keeps the tiers SEPARATE by
  construction, which is what the thesis actually asks about.

  Third: 10-Ds disclose an EXTENSION RATE (Exeter and peers) that Fitch never
  published. Extensions are the mechanical lever for making a delinquent loan appear
  current — the conduct the Tricolor superseding indictment describes. That field also
  replaces workbook/EXTENSION_PROXY.tsv, frozen 2026-07-25 as a dead manual stub.

WHAT IT IS NOT
  NOT an index. It is a FIXED PANEL of named deals. Do not average across deals of
  different seasoning and call it a market rate — a basket whose composition drifts
  month to month moves for compositional reasons, which is precisely the error this
  panel exists to avoid. Compare like-vintage to like-vintage, or read deals singly.
  Coverage is ~8 deals, not the ~$100B+ universe Fitch tracks; it is a consistent
  probe, not a market aggregate.

FAIL-LOUD (same contract as scripts/shelf_halt_monitor.py)
  - Every row is RUN-STAMPED. A number without a run stamp is not data.
  - A field that does not parse is written EMPTY with the miss named in `parse_misses`
    — never 0, never carried forward. A missing extension rate means "this issuer does
    not disclose it," not "extensions were zero."
  - POSITIVE CONTROL: a known deal/field/value must reproduce before any run is
    trusted. Control failure marks the whole run INVALID.
  - Unsupported issuers are reported UNSUPPORTED, never silently skipped.
  - Network/parse errors RAISE. They never degrade into a benign-looking number.

Usage:
  .venv/bin/python3 AGENTS/OTTO/scripts/panel_10d.py                 # latest filing per deal
  .venv/bin/python3 AGENTS/OTTO/scripts/panel_10d.py --history 6     # last 6 filings per deal
  .venv/bin/python3 AGENTS/OTTO/scripts/panel_10d.py --dry-run
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

OTTO_DIR = Path(__file__).resolve().parent.parent
LEDGER = OTTO_DIR / "workbook" / "PANEL_10D.tsv"
FTS = "https://efts.sec.gov/LATEST/search-index?"
UA = {"User-Agent": "OTTO Research willi.research@gmail.com"}
DELAY, RETRIES = 0.15, 3

# ── Panel ────────────────────────────────────────────────────────────────────
# tier is the analytical point: keep DEEP and BROAD separate, never blended.
PANEL = [
    ("EART 2022-2", "Exeter Automobile Receivables Trust 2022-2", "DEEP",  "exeter"),
    ("EART 2022-3", "Exeter Automobile Receivables Trust 2022-3", "DEEP",  "exeter"),
    ("EART 2023-1", "Exeter Automobile Receivables Trust 2023-1", "DEEP",  "exeter"),
    ("EART 2024-1", "Exeter Automobile Receivables Trust 2024-1", "DEEP",  "exeter"),
    ("SDART 2022-6", "Santander Drive Auto Receivables Trust 2022-6", "BROAD", "santander"),
    ("SDART 2023-1", "Santander Drive Auto Receivables Trust 2023-1", "BROAD", "santander"),
    ("SDART 2024-1", "Santander Drive Auto Receivables Trust 2024-1", "BROAD", "santander"),
    # Carvana/DriveTime shelf — the Carvana sub-thesis's only primary-source collateral read.
    ("BLAST 2024-1", "Bridgecrest Lending Auto Securitization Trust 2024-1", "CARVANA", "bridgecrest"),
    ("BLAST 2023-1", "Bridgecrest Lending Auto Securitization Trust 2023-1", "CARVANA", "bridgecrest"),
]

# Positive control — must reproduce exactly or the run is INVALID.
#
# ⚠ REBUILT 2026-08-03 (s017). The v1 control was ("EART 2022-3","cnl_pct",27.58)
# compared against whatever the LATEST filing returned. That is a threshold pinned to a
# MOVING quantity: the moment a new 10-D lands — the exact event this instrument exists
# to detect — the control fails and marks a perfectly good run INVALID. It fired on
# 2026-08-03 when Exeter's 07-30 filings posted (2022-3 CNL 27.58 -> 27.86) and
# condemned 9 valid rows. Same failure family as OTTO-04/-07/-30
# (auto-memory `finding_threshold_level_is_a_measurement_not_a_constant`).
#
# v2 pins the control to a FIXED ARCHIVED EXHIBIT. It re-parses that one frozen document
# every run, so it tests the PARSER (which must not drift) and never the WORLD (which must).
CONTROL = {
    "deal":   "EART 2022-3",
    "issuer": "exeter",
    "field":  "cnl_pct",
    "value":  27.58,
    "label":  "10-D filed 2026-06-30 (frozen exhibit)",
    "url":    "https://www.sec.gov/Archives/edgar/data/1931330/"
              "000092963826002447/eart2022-3_exhibit991.htm",
}


def run_control():
    """Re-parse the frozen control exhibit. Returns True/False, or None if unreachable."""
    try:
        txt = flatten(fetch(CONTROL["url"]))
    except Exception as e:
        print(f"  (control exhibit unreachable: {type(e).__name__})")
        return None
    v, _ = parse(txt, CONTROL["issuer"])
    d = derive(v, CONTROL["issuer"])
    got = d.get(CONTROL["field"])
    if got is None:
        return False
    return abs(got - CONTROL["value"]) < 0.01

# ── Pattern primitives ───────────────────────────────────────────────────────
# TWO traps live in these documents, both found by getting them wrong first:
#  1. Footnote markers like `{95}` sit between a label and its value — and they
#     CONTAIN DIGITS, so a naive "skip to the first number" grabs 95. SKIP therefore
#     consumes brace-tokens explicitly.
#  2. A gap written `[^\d]{0,30}` stops dead at that same `{93}` and silently matches
#     the wrong field — which is how the first run reported an ANL of 111,600%.
# Empty cells are EM-DASHES (—), not zeros, so numeric cells cannot be assumed present.
SKIP = r"(?:\{\d+\}|[^\d{])*"                    # footnotes + non-numeric filler
NUMV = r"(?P<v>[\d,]+\.\d{1,4}|[\d,]+)"          # the value we want
PCT  = r"[\s\S]{0,140}?(?P<v>[\d,]+\.\d{1,2})\s*%"   # first N.NN% after a label

# Bridgecrest (Carvana/DriveTime shelf) uses a THIRD schema:
#   - line references are PARENTHESISED `(51 )`, not braced `{51}` — so the brace-aware
#     SKIP does not apply and would capture the reference number as the value;
#   - some labels carry a brace FORMULA containing digits, e.g. `{(42)-(sum of (45)...)}`;
#   - delinquency buckets are dollars only, with NO percentage column — but the filing
#     states a ready-made 60+ figure at line (55), which is what OTTO wants anyway;
#   - CNL must be derived against the Original Pool Balance at line (14).
BSKIP = r"(?:\([^)]*\)|\{[^}]*\}|[^\d({])*"   # paren refs AND letter tags like "(B)"

SPECS = {
    "exeter": {
        "dq_61_90":   r"61-90 days" + PCT,
        "dq_91_120":  r"91-120 days" + PCT,
        "dq_120plus": r"over 120 days" + PCT,
        # Issuer-stated 60+ aggregate {102}, tested against {103} Delinquency Trigger
        # (40.00%). Canonical since 2026-08-27 — see derive().
        "dq_60plus_direct": r"\{\d+\}\s*(?P<v>[\d.]+)\s*%\s*\{\d+\}\s*Delinquency Trigger",
        "cnl_pct":    r"Cumulative\s+net\s+loss\s+ratio" + PCT,
        "ext_rate":   r"Extension Rate" + PCT,
        "net_loss_period": r"Net losses during period" + SKIP + NUMV,
        "beg_balance":     r"Beginning of Period Aggregate Principal Balance" + SKIP + NUMV,
        "liquidated":      r"becoming Liquidated Receivables during period" + SKIP + NUMV,
        "liq_proceeds":    r"Net Liquidation Proceeds collected during period" + SKIP + NUMV,
    },
    "santander": {
        "dq_61_90":   r"61-90 days" + PCT,
        "dq_91_120":  r"91-120 days" + PCT,
        "dq_120plus": r"121 \+ days delinquent" + PCT,
        # Issuer-stated 60+ aggregate {79}, tested against this deal's own {80}
        # Delinquency Trigger (24.00%). Canonical since 2026-08-27 — see derive().
        "dq_60plus_direct": r"Delinquency Percentage as of the End of the Collection Period\s*\{?\d*\}?\s*(?P<v>[\d.]+)\s*%",
        "cum_loss_dollars": r"Cumulative Net losses since Cut-off Date" + SKIP + NUMV,
        "net_loss_period":  r"Net losses during period" + SKIP + NUMV,
        # Initial Purchase row: units, cut-off date, closing date, THEN the balance.
        "initial_pool":     r"Initial Purchase\s+[\d,]+\s+[\d/]+\s+[\d/]+\s+" + NUMV,
        # Pool FACTOR (current balance / original). Needed because Santander does not
        # state a beginning-of-period balance; without it, ANL computed off the INITIAL
        # pool understates a seasoned deal by the amortisation factor — ~6x here.
        "pool_factor":      r"Pool Balance\)" + SKIP + NUMV,
        # ext_rate deliberately ABSENT — Santander does not disclose it. Absence is
        # recorded as not-disclosed, never as zero.
    },
    "bridgecrest": {
        "dq_60plus_direct": r"Receivables greater than 60 days delinquent at end of Collection Period" + PCT,
        "cum_loss_dollars": r"aggregate amount of Net Charged-Off Receivables losses as of the last day of the current Collection Period" + BSKIP + NUMV,
        "original_pool":    r"Original Pool Balance as of Cutoff Date" + BSKIP + NUMV,
        "net_loss_period":  r"Net Charged-Off Receivables losses occurring in current Collection Period" + BSKIP + NUMV,
        # "Pool Balance of the Collection Period (1 ) 14,479 $ 271,583,183.15"
        # -> skip the receivable COUNT, take the dollar balance.
        "pool_balance":     r"Pool Balance of the Collection Period" + BSKIP + r"[\d,]+" + BSKIP + NUMV,
        "ext_balance":      r"Principal Balance of receivables extended in Collection Period" + BSKIP + NUMV,
    },
}

COLUMNS = ["run_ts", "deal", "tier", "issuer", "filing_date", "months_seasoned",
           "dq_60plus_pct", "cnl_pct", "anl_pct", "recovery_pct", "ext_rate_pct",
           "status", "parse_misses", "source_url"]


def _num(s):
    return float(s.replace(",", "")) if s else None


def fetch(url, timeout=45):
    last = None
    for a in range(RETRIES):
        try:
            time.sleep(DELAY)
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception as e:
            last = e
            time.sleep(1.5 * (a + 1))
    raise last


def flatten(raw):
    import html as _h
    return _h.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", raw)))


def resolve_trust_cik(hits, phrase):
    """Resolve the CIK of the TRUST named `phrase` — not the depositor.

    `_source.ciks[0]` is the DEPOSITOR, which is shared across every trust a shelf has
    ever issued (all Santander trusts share CIK 1383094). Taking ciks[0] silently
    returns the same filing list for every deal on a shelf, producing *identical
    metrics for different vintages* — plausible-looking and completely wrong. The
    per-trust CIK is embedded in the matching display_name instead.
    Returns None when no display_name matches, which callers must treat as INVALID.
    """
    for h in hits:
        for n in h["_source"].get("display_names", []):
            if phrase.lower() in n.lower():
                m = re.search(r"CIK\s*(\d{6,10})", n)
                if m:
                    return m.group(1).lstrip("0")
    return None


def deal_filings(phrase, want):
    """Return [(filing_date, cik, accession)] newest-first for this deal's 10-Ds."""
    r = json.loads(fetch(FTS + urllib.parse.urlencode({"q": f'"{phrase}"', "forms": "10-D"}), 30))
    hits = r.get("hits", {}).get("hits", [])
    if not hits:
        return []
    cik = resolve_trust_cik(hits, phrase)
    if not cik:
        raise RuntimeError(f"could not resolve a trust CIK whose display_name matches {phrase!r}")
    sub = json.loads(fetch(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json", 30))
    rec = sub["filings"]["recent"]
    out = [(rec["filingDate"][i], cik, rec["accessionNumber"][i])
           for i in range(len(rec["form"])) if rec["form"][i] == "10-D"]
    out.sort(reverse=True)
    return out[:want], (out[-1][0] if out else None)


def exhibit_text(cik, accession):
    """Resolve the EX-99.1 servicer report for an accession.

    ⚠ 2026-08-27: `index.json` began returning an INCOMPLETE directory listing for
    these filers — only the primary 10-D document plus the index files, with the
    exhibit ABSENT — while the exhibit itself still resolves 200 at its URL and is
    still correctly typed `EX-99.1` in the human `-index.html` document table. The
    old filename-heuristic path therefore matched nothing and fell through to a
    silent "any .htm" fallback, which returns the 10-D WRAPPER (no data table). Every
    field then missed, the row was written `OK-PARTIAL` with blanks, and the upsert
    REPLACED four good rows with empty ones. The positive control passed throughout,
    because it re-parses a FROZEN LOCAL exhibit and so cannot see a resolution fault.

    Resolution order is now: (1) the `-index.html` document table, keyed on the
    declared TYPE (`EX-99.*`) rather than on a filename convention; (2) the
    index.json filename heuristic, kept as a fallback for filers whose index page
    shape differs. There is deliberately NO third fallback: an unresolved exhibit
    RAISES, because substituting a different document silently is what caused the
    data loss."""
    acc = accession.replace("-", "")
    base = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}"

    # (1) authoritative: the declared document TYPE in the filing index table
    try:
        page = fetch(f"{base}/{accession}-index.html", 30)
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", page, re.S | re.I)
        for row in rows:
            href = re.search(r'href="([^"]+\.(?:htm|txt))"', row, re.I)
            if not href:
                continue
            cells = [re.sub(r"<[^>]+>", "", c).strip()
                     for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S | re.I)]
            if any(re.fullmatch(r"EX-99(\.\d+)?", c, re.I) for c in cells):
                url = "https://www.sec.gov" + href.group(1) if href.group(1).startswith("/") \
                      else f"{base}/{href.group(1).rsplit('/', 1)[-1]}"
                return flatten(fetch(url)), url
    except Exception:
        pass  # fall through to the filename heuristic

    # (2) fallback: filename convention in the JSON directory listing
    try:
        idx = json.loads(fetch(f"{base}/index.json", 30))
        names = [i["name"] for i in idx["directory"]["item"]]
    except Exception as e:
        raise RuntimeError(f"could not resolve exhibit: index.html and index.json both failed ({type(e).__name__})")
    cands = [n for n in names if re.search(r"(ex.?99|exhibit.?99)", n, re.I) and n.endswith((".htm", ".txt"))]
    if not cands:
        # NO wrapper fallback — see the docstring. Fail loud rather than parse the wrong document.
        raise RuntimeError(
            "no EX-99 exhibit resolvable (index.html carried no EX-99 type row and "
            f"index.json listed only {names!r}) — refusing to substitute the 10-D wrapper")
    url = f"{base}/{cands[0]}"
    return flatten(fetch(url)), url


def parse(txt, issuer):
    spec = SPECS[issuer]
    vals, misses = {}, []
    for field, pat in spec.items():
        m = re.search(pat, txt, re.I)
        if not m:
            misses.append(field)
            vals[field] = None
            continue
        vals[field] = _num(m.group("v"))
    return vals, misses


def derive(v, issuer):
    """Compute the four comparable metrics. Any input missing -> output None, never 0."""
    out = {}
    # ⚠ 2026-08-27 — DEFINITION RECONCILED WITH CARL, and the panel was internally
    # INCONSISTENT before it. Bridgecrest read the issuer's stated aggregate while
    # Exeter and Santander SUMMED the 61-90 / 91-120 / 121+ buckets — so the deep and
    # broad tiers were measured one way and Carvana another, INSIDE a panel whose whole
    # purpose is cross-tier comparison. All three shelves in fact disclose an
    # issuer-stated 60+ aggregate, each tested against that deal's OWN Delinquency
    # Trigger: SDART {79} (vs {80} 24.00%), EART {102} (vs {103} 40.00%), BLAST (55)
    # (vs (56) 50.00%). That is the contractually operative number and it is now
    # canonical on every shelf; the bucket sum is retained only as a fallback.
    # MEASURED GAP (issuer aggregate MINUS bucket sum): Santander +0.62 to +0.73pp
    # across three deals and three months — the BROAD tier was UNDERSTATED by ~0.7pp,
    # so published deep-vs-broad level bifurcation was overstated by about that much.
    # Exeter +0.01pp (its buckets already ~equal its aggregate).
    # DIRECTION IS UNAFFECTED, which is why CARL's V2 grade stands either way:
    # SDART 2022-6 Jun->Jul reads -0.34pp on buckets and -0.39pp on {79}; 2024-1 reads
    # -0.11pp and -0.13pp. Found by CARL 2026-08-27; adopted here because it also
    # removes a defect internal to this panel.
    if issuer != "bridgecrest":
        direct = v.get("dq_60plus_direct")
        if direct is not None:
            out["dq_60plus_pct"] = direct
        else:
            dq = [v.get("dq_61_90"), v.get("dq_91_120"), v.get("dq_120plus")]
            out["dq_60plus_pct"] = round(sum(dq), 2) if all(x is not None for x in dq) else None

    if issuer == "exeter":
        out["cnl_pct"] = v.get("cnl_pct")
        nl, bb = v.get("net_loss_period"), v.get("beg_balance")
        out["anl_pct"] = round(nl / bb * 12 * 100, 2) if nl and bb else None
        liq, pr = v.get("liquidated"), v.get("liq_proceeds")
        out["recovery_pct"] = round(pr / liq * 100, 2) if liq and pr else None
        out["ext_rate_pct"] = v.get("ext_rate")
    elif issuer == "bridgecrest":
        out["dq_60plus_pct"] = v.get("dq_60plus_direct")   # stated at line (55)
        cl, op = v.get("cum_loss_dollars"), v.get("original_pool")
        out["cnl_pct"] = round(cl / op * 100, 2) if (cl and op) else None
        nl, pb = v.get("net_loss_period"), v.get("pool_balance")
        out["anl_pct"] = round(nl / pb * 12 * 100, 2) if (nl and pb) else None
        out["recovery_pct"] = None      # gross liquidation balance not separably stated
        eb = v.get("ext_balance")
        out["ext_rate_pct"] = round(eb / pb * 100, 2) if (eb and pb) else None
    else:  # santander: cumulative losses are dollars -> derive ratio off initial pool
        cl, ip = v.get("cum_loss_dollars"), v.get("initial_pool")
        out["cnl_pct"] = round(cl / ip * 100, 2) if cl and ip else None
        # ANL must be measured against the CURRENT balance, as Exeter's is. Santander
        # states only the initial balance + a pool factor, so reconstruct:
        #   current balance = initial pool x pool factor
        # NOTE: Santander's own stated definition uses the AVERAGE portfolio balance for
        # the period ((beginning + end)/2); this uses the point-in-time balance, so the
        # figure is a close approximation, not the issuer's own published ratio.
        nl, pf = v.get("net_loss_period"), v.get("pool_factor")
        cur = ip * pf if (ip and pf) else None
        out["anl_pct"] = round(nl / cur * 12 * 100, 2) if (nl and cur) else None
        out["recovery_pct"] = None      # gross liquidation balance not disclosed in this format
        out["ext_rate_pct"] = None      # NOT DISCLOSED by this issuer — not zero
    return out


def months_between(a, b):
    da, db = datetime.strptime(a, "%Y-%m-%d"), datetime.strptime(b, "%Y-%m-%d")
    return (db.year - da.year) * 12 + (db.month - da.month)


def main():
    want = 1
    if "--history" in sys.argv:
        want = int(sys.argv[sys.argv.index("--history") + 1])
    dry = "--dry-run" in sys.argv
    # --only <substr>  → restrict the run to deals whose name contains <substr>
    # (case-insensitive). Added 2026-08-14: a full --history backfill is 9 deals x N
    # filings of rate-limited EDGAR fetches and times out interactive runs. The
    # severity-divergence falsifier reads Exeter ONLY (sole issuer disclosing a
    # recovery rate), so it needs `--only EART` rather than a whole-panel pull.
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1].lower()
    run_ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    print(f"\n{'='*104}\n  OTTO 10-D Performance Panel — {run_ts}   ({want} filing(s)/deal)")
    print(f"  FIXED PANEL of named deals — NOT an index. Tiers stay separate by design.\n{'='*104}")

    rows, control_ok = [], None
    for deal, phrase, tier, issuer in PANEL:
        if only and only not in deal.lower():
            continue
        if issuer not in SPECS:
            rows.append(dict(run_ts=run_ts, deal=deal, tier=tier, issuer=issuer, status="UNSUPPORTED",
                             parse_misses="no field spec for issuer", filing_date="", months_seasoned="",
                             dq_60plus_pct="", cnl_pct="", anl_pct="", recovery_pct="", ext_rate_pct="", source_url=""))
            print(f"  {deal:14s} UNSUPPORTED — no field spec"); continue
        try:
            filings, first_date = deal_filings(phrase, want)
        except Exception as e:
            print(f"  {deal:14s} ERROR resolving filings: {type(e).__name__}"); continue
        if not filings:
            rows.append(dict(run_ts=run_ts, deal=deal, tier=tier, issuer=issuer, status="INVALID",
                             parse_misses="deal phrase matched no 10-D — check the name stem",
                             filing_date="", months_seasoned="", dq_60plus_pct="", cnl_pct="",
                             anl_pct="", recovery_pct="", ext_rate_pct="", source_url=""))
            print(f"  {deal:14s} INVALID — phrase matched no 10-D (name stem wrong?)"); continue

        for fdate, cik, acc in filings:
            try:
                txt, url = exhibit_text(cik, acc)
            except Exception as e:
                print(f"  {deal:14s} {fdate}  ERROR fetching exhibit: {type(e).__name__}"); continue
            v, misses = parse(txt, issuer)
            d = derive(v, issuer)
            # ⚠ 2026-08-27: the ledger upsert is last-write-wins, which silently assumes
            # the newest write is the better one. A FAILED parse also wins. On 8/27 a
            # wrong-document fetch wrote all-blank rows over four good EART rows. A row
            # carrying none of the five headline metrics is a PARSE FAILURE, not a
            # partial read: report it and DROP it, so the good row on disk survives.
            headline = ("dq_60plus_pct", "cnl_pct", "anl_pct", "recovery_pct", "ext_rate_pct")
            if all(d[k] is None for k in headline):
                print(f"  {deal:14s} {tier:5s} {fdate}  ⛔ PARSE FAILURE — zero of "
                      f"{len(headline)} headline metrics resolved; row DROPPED, not upserted "
                      f"(protects any existing row). source={url}")
                continue
            status = "OK" if not misses else "OK-PARTIAL"
            rows.append(dict(run_ts=run_ts, deal=deal, tier=tier, issuer=issuer, filing_date=fdate,
                             months_seasoned=months_between(first_date, fdate) if first_date else "",
                             status=status, parse_misses=";".join(misses), source_url=url,
                             **{k: ("" if d[k] is None else d[k]) for k in
                                ("dq_60plus_pct","cnl_pct","anl_pct","recovery_pct","ext_rate_pct")}))
            f = lambda k: f"{d[k]:6.2f}" if d[k] is not None else "   n/d"
            print(f"  {deal:14s} {tier:5s} {fdate}  60+DQ {f('dq_60plus_pct')}  CNL {f('cnl_pct')}"
                  f"  ANL {f('anl_pct')}  REC {f('recovery_pct')}  EXT {f('ext_rate_pct')}"
                  + (f"   ⚠ missed: {','.join(misses)}" if misses else ""))

    # ── Safety net: identical metric tuples across DIFFERENT deals ──────────────
    # Distinct vintages cannot legitimately produce identical performance. When they
    # do, it means every deal resolved to the same filings — the depositor-CIK bug
    # (fixed 2026-07-25, kept as a detector because the failure LOOKS like valid data).
    seen = {}
    for r in rows:
        if r.get("status", "").startswith("OK") and r.get("cnl_pct") != "":
            key = (r["cnl_pct"], r["dq_60plus_pct"], r["anl_pct"], r["filing_date"])
            seen.setdefault(key, []).append(r["deal"])
    dupes = {k: v for k, v in seen.items() if len(set(v)) > 1}
    if dupes:
        print("\n  ⚠️  DUPLICATE-METRIC DETECTOR TRIPPED — different deals returned identical values:")
        for k, v in dupes.items():
            print(f"       {', '.join(sorted(set(v)))}  ->  cnl={k[0]} dq={k[1]} anl={k[2]}")
        print("       This means deals resolved to the SAME filings. Run marked INVALID.")
        for r in rows:
            if r["deal"] in {d for v in dupes.values() for d in v}:
                r["status"] = "INVALID"
                r["parse_misses"] = (r.get("parse_misses", "") + ";duplicate-metrics-across-deals").strip(";")

    print(f"\n  POSITIVE CONTROL — re-parse frozen exhibit: {CONTROL['deal']} "
          f"{CONTROL['field']} must equal {CONTROL['value']} ({CONTROL['label']}): ", end="")
    control_ok = run_control()
    if control_ok is None:
        print("NOT EVALUATED (control exhibit unreachable) → run marked INVALID")
        for r in rows: r["status"] = "INVALID"
    elif control_ok:
        print("PASS ✓")
    else:
        print("**FAIL** → every value in this run is untrustworthy; run marked INVALID")
        for r in rows: r["status"] = "INVALID"

    if dry:
        print("\n  [--dry-run] nothing written\n"); return 0

    # ── UPSERT on (deal, filing_date), atomic write ──────────────────────────
    # Was a blind append. Re-running against an already-recorded filing wrote a
    # DUPLICATE row — 5 of them existed by 2026-08-14, all the 07-15 SDART/BLAST
    # filings, from the s017 re-run. Harmless to eyeball, NOT harmless to any
    # statistic computed off this ledger: duplicates silently inflate n and
    # double-weight one month. Found while base-rating the severity-divergence
    # falsifier, which reads exactly these columns. Key is (deal, filing_date)
    # because that pair identifies one servicer report; last write wins, so a
    # re-parse after a parser fix supersedes rather than accumulates.
    existing, order = {}, []
    if LEDGER.exists():
        with LEDGER.open() as fh:
            lines = [ln.rstrip("\n") for ln in fh if ln.strip()]
        if lines and lines[0].split("\t")[0] == COLUMNS[0]:
            lines = lines[1:]
        for ln in lines:
            parts = ln.split("\t")
            if len(parts) != len(COLUMNS):        # field-count the WHOLE file
                print(f"  ⚠ RAGGED ROW skipped ({len(parts)} of {len(COLUMNS)} fields): {ln[:60]}…")
                continue
            rec = dict(zip(COLUMNS, parts))
            k = (rec["deal"], rec["filing_date"])
            if k not in existing:
                order.append(k)
            existing[k] = rec

    added = replaced = 0
    for r in rows:
        k = (str(r.get("deal", "")), str(r.get("filing_date", "")))
        if k in existing:
            replaced += 1
        else:
            added += 1
            order.append(k)
        existing[k] = {c: str(r.get(c, "")) for c in COLUMNS}

    tmp = LEDGER.with_suffix(".tsv.tmp")
    with tmp.open("w") as fh:
        fh.write("\t".join(COLUMNS) + "\n")
        for k in order:
            fh.write("\t".join(existing[k].get(c, "") for c in COLUMNS) + "\n")
    os.replace(tmp, LEDGER)                       # atomic; never a half-written ledger
    print(f"\n  {LEDGER.name}: {added} new row(s), {replaced} replaced, "
          f"{len(order)} total (upsert on deal+filing_date)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
