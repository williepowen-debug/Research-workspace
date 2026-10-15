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
  .venv/bin/python3 AGENTS/OTTO/scripts/panel_10d.py --backfill      # re-parse every ledger filing + newer
  .venv/bin/python3 AGENTS/OTTO/scripts/panel_10d.py --selftest      # offline merge/seasoning tests
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


# Seasoning positive control (CARL ruling 2026-09-17, acceptance condition 2): >=3 rows per
# shelf, INCLUDING both Exeter double-filing dates (filed 2025-12-01 -> collection 2025-10;
# filed 2026-03-03 -> collection 2026-01). Expected values were read OFF THE EXHIBITS by a
# separate raw-text grep on 2026-10-14 (not by this parser), so the control tests the parser
# against the document. Bridgecrest expectations are hand arithmetic on the exhibit's own
# two dates (agreement "dated as of" = closing date, verified for 2024-1 at its 424B5:
# "on or about January 24, 2024 ... the closing date").
_SA = "https://www.sec.gov/Archives/edgar/data/"
SEASONING_CONTROL = [
    # (deal, issuer, exhibit, expected months_seasoned, expected collection month)
    ("EART 2022-2", "exeter", _SA + "1920761/000092963825004454/eart2022-2_exhibit991.htm", 43, "2025-10"),  # double-filing date
    ("EART 2022-2", "exeter", _SA + "1920761/000092963825004752/eart2022-2_exhibit991.htm", 44, "2025-11"),
    ("EART 2022-2", "exeter", _SA + "1920761/000092963826000840/eart2022-2_exhibit991.htm", 46, "2026-01"),  # double-filing date
    ("EART 2024-1", "exeter", _SA + "2005087/000092963826000850/eart2024-1_exhibit991.htm", 25, "2026-01"),  # double-filing date
    ("SDART 2024-1", "santander", _SA + "1383094/000119312525239308/d67309dex991.htm", 21, "2025-09"),
    ("SDART 2024-1", "santander", _SA + "1383094/000119312526013270/d57557dex991.htm", 24, "2025-12"),
    ("SDART 2024-1", "santander", _SA + "1383094/000119312526106789/d108803dex991.htm", 26, "2026-02"),
    ("BLAST 2024-1", "bridgecrest", _SA + "2006743/000110465925059729/tm2517576d1_ex99-1.htm", 17, "2025-05"),
    ("BLAST 2024-1", "bridgecrest", _SA + "1974820/000110465926062002/tm2613972d2_ex99-1.htm", 28, "2026-04"),
    ("BLAST 2024-1", "bridgecrest", _SA + "1974820/000110465926097635/tm2622707d2_ex99-1.htm", 31, "2026-07"),
    ("BLAST 2023-1", "bridgecrest", _SA + "1974820/000110465926061994/tm2613972d1_ex99-1.htm", 31, "2026-04"),
]


def run_seasoning_control():
    """Re-parse each frozen seasoning-control exhibit. True only if EVERY row reproduces
    both its months_seasoned and its collection month; None if any exhibit is unreachable."""
    ok = True
    for deal, issuer, url, want_ms, want_cp in SEASONING_CONTROL:
        try:
            txt = flatten(fetch(url))
        except Exception as e:
            print(f"\n    (seasoning control exhibit unreachable: {deal} {type(e).__name__})", end="")
            return None
        got_ms, miss = months_seasoned(txt, issuer)
        cp, _ = collection_period(txt)
        if got_ms != want_ms or not cp or cp[:7] != want_cp:
            print(f"\n    ✗ {deal} {want_cp}: months_seasoned {got_ms} (want {want_ms}), "
                  f"collection {cp} (want {want_cp}) {miss or ''}", end="")
            ok = False
    return ok


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

COLUMNS = ["run_ts", "deal", "tier", "issuer", "filing_date", "collection_period",
           "months_seasoned",
           "dq_60plus_pct", "cnl_pct", "anl_pct", "recovery_pct", "ext_rate_pct",
           "status", "parse_misses", "source_url"]

# The 14-column shape that stood until 2026-09-02, kept ONLY so the upsert can read a
# pre-backfill ledger without discarding rows as ragged. Never written.
LEGACY_COLUMNS_14 = [c for c in COLUMNS if c != "collection_period"]

# ── Collection period ────────────────────────────────────────────────────────
# WHY A COLUMN AND NOT A DERIVATION (WQ-107, Will-ruled 2026-09-01):
#   The panel's L1 test is matched-COLLECTION-MONTH YoY. Until 2026-09-02 the collection
#   month was inferred as filing_month minus one. That inference is wrong wherever a
#   filer goes off cadence — Exeter double-filed Dec-2025 and Mar-2026, producing 8
#   collisions and 9 gaps in the inferred series. A leg table registered on an inferred
#   month is the seasonality-mislabel class the 26-of-26 spec exists to kill, so CARL
#   cannot register the V2 downgrade leg until the DISCLOSED period is on the row.
#
# KEYED ON THE ROW LABEL, NEVER ON A TAG NUMBER (CARL 2026-09-01 §3): tag numbering is
# not stable across shelves OR across months on the SAME deal — EART's older template
# runs buckets {97}-{101} with the stated rate at {103}, the same deal a month later
# runs {98}-{102}/{104}, and EART 2026-1 runs {114}-{118}/{120}. A parser keyed on the
# number silently reads the wrong field.
#
# Three disclosed shapes, all label-anchored:
#   exeter/santander : "Collection Period Beginning: MM/DD/YYYY" … "Ending: MM/DD/YYYY"
#   bridgecrest      : "Collection Period: M/D/YYYY Through M/D/YYYY"
# ⚠ 2026-09-02: the date components are separate HTML CELLS on some Bridgecrest
# exhibits, so the flattened text reads "3 /1/2026" — whitespace INSIDE the date. A
# tight \d{1,2}/\d{1,2}/\d{4} missed 2 of 133 rows and reported them as
# label-not-found, i.e. as a missing disclosure rather than a reader defect. The
# separators therefore tolerate surrounding whitespace; the components do not, so this
# cannot bridge two different numbers on the same line.
_D = r"(?P<{}>\d{{1,2}}\s*/\s*\d{{1,2}}\s*/\s*\d{{4}})"
CP_PATTERNS = [
    # bridgecrest single-line form FIRST — its label is a prefix of nothing else,
    # and the two-label form below would not match it.
    re.compile(r"Collection\s+Period\s*:\s*" + _D.format("a")
               + r"\s*(?:Through|through|-|–|—|to)\s*" + _D.format("b")),
    # exeter / santander two-label form. The two labels are NOT adjacent in the
    # flattened text (an "Original" column header sits between them on Exeter), so
    # they are matched independently rather than as one span.
    None,
]
CP_BEGIN = re.compile(r"Collection\s+Period\s+Beginning\s*:\s*" + _D.format("a"))
CP_END   = re.compile(r"Collection\s+Period\s+Ending\s*:\s*" + _D.format("b"))


def _iso(mdy):
    m, d, y = [p.strip() for p in mdy.split("/")]
    return f"{int(y):04d}-{int(m):02d}-{int(d):02d}"


def collection_period(txt):
    """Return ("YYYY-MM-DD/YYYY-MM-DD", None) or (None, reason).

    NEVER falls back to the distribution/filing date. An unreadable period is
    reported as a miss and written EMPTY — the whole point of the column is that the
    period is DISCLOSED, not inferred (root: fail-loud contract above)."""
    m = CP_PATTERNS[0].search(txt)
    if m:
        return f"{_iso(m.group('a'))}/{_iso(m.group('b'))}", None
    b, e = CP_BEGIN.search(txt), CP_END.search(txt)
    if b and e:
        return f"{_iso(b.group('a'))}/{_iso(e.group('b'))}", None
    if b or e:
        return None, "collection_period-half-matched"
    return None, "collection_period-label-not-found"


# ── Months seasoned (CARL ruling 2026-09-17: ISSUER-STATED, distribution-date clock) ──
# Until 2026-10-14 this column was OTTO-COMPUTED as months between the deal's FIRST 10-D
# filing date and this filing date. Read against the exhibits (2026-09-12) that clock was
# -1 on ordinary rows and 0 at the two Exeter double-filing dates (filed 2025-12-01 ->
# collection 2025-10; filed 2026-03-03 -> collection 2026-01), so it was NON-MONOTONE
# inside a deal (43·43, 46·46) and one value mapped to two collection months. The issuer
# keys "Months Seasoned" to the DISTRIBUTION date (one month after the collection
# period). CARL ruled the issuer clock on the grader-checkability test: a grader checking
# the exhibit must find the number in it.
#
#   exeter / santander : the exhibit STATES it ("Months Seasoned: NN"), read label-anchored.
#   bridgecrest        : the exhibit does NOT state it (checked 2026-10-14). It does state
#     the Sale and Servicing Agreement date ("... dated as of January 24, 2024") and the
#     "Distribution Date:", so the value is computed from those TWO EXHIBIT DATES on the
#     convention the other two issuers use (distribution month minus closing month).
#     EXHIBIT-DERIVED, NOT ISSUER-STATED: a grader can check it from the exhibit by
#     arithmetic but will not find it printed. The one place the ruling's letter cannot
#     be met; flagged to CARL.
# Never falls back to filing dates: an unreadable clock is a named miss, written EMPTY.
MS_STATED = re.compile(r"Months\s+Seasoned\s*:\s*(?P<v>\d{1,3})\b")
_MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
BC_AGREEMENT = re.compile(r"dated\s+as\s+of\s+(?P<v>(?:" + _MONTHS + r")\s+\d{1,2}\s*,\s*\d{4})")
BC_DISTRIBUTION = re.compile(r"Distribution\s+Date\s*:\s*" + _D.format("v"))


def months_seasoned(txt, issuer):
    """Return (int, None) or (None, reason). See the block comment above."""
    if issuer in ("exeter", "santander"):
        m = MS_STATED.search(txt)
        return (int(m.group("v")), None) if m else (None, "months_seasoned-label-not-found")
    if issuer == "bridgecrest":
        a, d = BC_AGREEMENT.search(txt), BC_DISTRIBUTION.search(txt)
        if not (a and d):
            return None, "months_seasoned-dates-not-found"
        ad = datetime.strptime(re.sub(r"\s*,\s*", ", ", re.sub(r"\s+", " ", a.group("v"))), "%B %d, %Y")
        dd = datetime.strptime(_iso(d.group("v")), "%Y-%m-%d")
        return (dd.year - ad.year) * 12 + (dd.month - ad.month), None
    return None, "months_seasoned-no-rule-for-issuer"


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


def deal_filings(phrase, want, since=None):
    """Return [(filing_date, cik, accession)] newest-first for this deal's 10-Ds AND
    10-D/As (an amendment restates a servicer report; the (deal, collection_period)
    upsert key lets it supersede the original — see merge()). `since` (YYYY-MM-DD)
    keeps every filing on/after that date instead of the newest `want`."""
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
           for i in range(len(rec["form"])) if rec["form"][i] in ("10-D", "10-D/A")]
    out.sort(reverse=True)
    if since:
        return [f for f in out if f[0] >= since], (out[-1][0] if out else None)
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


# ── Ledger I/O, merge and the seasoning check (2026-10-14 repair) ────────────
def ledger_key(rec):
    """(deal, collection_period); a row with no disclosed period keys on its filing date
    so that two period-less rows can never collapse onto one key."""
    cp = rec.get("collection_period", "")
    return (rec.get("deal", ""), cp if cp else "filed:" + rec.get("filing_date", ""))


def read_ledger(path=None):
    path = path or LEDGER
    existing, order = {}, []
    if not path.exists():
        return order, existing
    with path.open() as fh:
        lines = [ln.rstrip("\n") for ln in fh if ln.strip()]
    if lines and lines[0].split("\t")[0] == COLUMNS[0]:
        lines = lines[1:]
    for ln in lines:
        parts = ln.split("\t")
        if len(parts) == len(LEGACY_COLUMNS_14):
            # Pre-2026-09-02 shape: migrate in memory with an EMPTY collection_period,
            # never a guessed one (a skipped ragged row would drop real history).
            print(f"  ⚠ legacy 14-col row migrated (collection_period left EMPTY): {parts[1]} {parts[4]}")
            rec = dict(zip(LEGACY_COLUMNS_14, parts)); rec["collection_period"] = ""
        elif len(parts) != len(COLUMNS):
            print(f"  ⚠ RAGGED ROW skipped ({len(parts)} of {len(COLUMNS)} fields): {ln[:60]}…")
            continue
        else:
            rec = dict(zip(COLUMNS, parts))
        k = ledger_key(rec)
        if k in existing:
            # A duplicate key already on disk is a pre-repair artefact; keep the newer filing.
            if rec.get("filing_date", "") >= existing[k].get("filing_date", ""):
                existing[k] = rec
            continue
        order.append(k); existing[k] = rec
    return order, existing


def merge(order, existing, rows):
    """Upsert `rows` into (order, existing) on ledger_key. SUPERSEDE RULE: a row replaces
    the one on file only if its filing_date is the SAME OR LATER (a re-parse of the same
    report after a parser fix, or a 10-D/A amending it) AND it is not INVALID while the
    row on file is good. An older filing never overwrites its own amendment, whatever
    order the run fetched them in (runs fetch newest-first, so without this the ORIGINAL
    10-D would be written last and win)."""
    order, existing = list(order), dict(existing)
    stats = {"added": 0, "replaced": 0, "kept": 0}
    for r in rows:
        new = {c: str(r.get(c, "")) for c in COLUMNS}
        k = ledger_key(new)
        old = existing.get(k)
        if old is None:
            order.append(k); existing[k] = new; stats["added"] += 1
            continue
        older = new["filing_date"] < old.get("filing_date", "")
        degrades = new["status"] == "INVALID" and old.get("status", "").startswith("OK")
        if older or degrades:
            stats["kept"] += 1
            continue
        existing[k] = new; stats["replaced"] += 1
    return order, existing, stats


def _ym(cp):
    y, m = int(cp[:4]), int(cp[5:7])
    return y * 12 + m


def check_seasoning(existing):
    """Acceptance condition 3, FAIL-CLOSED: within each deal, ordered by collection month,
    months_seasoned must rise by EXACTLY the number of collection months elapsed — no
    repeat (the old 43·43), no skip (41 -> 43 across one month). Also fails on any OK row
    with an empty months_seasoned or an empty collection_period (condition 1: on EVERY
    row). Returns a list of defects; empty = pass. A coverage gap (a missing month) is
    NOT a defect in the clock and passes if the clock moves by the same number of months."""
    bad, by = [], {}
    for rec in existing.values():
        if not rec.get("status", "").startswith("OK"):
            continue
        if not rec.get("collection_period") or rec.get("months_seasoned", "") == "":
            bad.append(f"{rec.get('deal')} filed {rec.get('filing_date')}: empty "
                       f"collection_period or months_seasoned")
            continue
        by.setdefault(rec["deal"], []).append(rec)
    for deal, recs in by.items():
        recs.sort(key=lambda r: r["collection_period"])
        for a, b in zip(recs, recs[1:]):
            dm = _ym(b["collection_period"]) - _ym(a["collection_period"])
            ds = int(b["months_seasoned"]) - int(a["months_seasoned"])
            if dm == 0:
                bad.append(f"{deal}: collection month {a['collection_period'][:7]} appears twice")
            elif ds != dm:
                bad.append(f"{deal}: {a['collection_period'][:7]}->{b['collection_period'][:7]} "
                           f"is {dm} month(s) but seasoning moves {a['months_seasoned']}->"
                           f"{b['months_seasoned']} ({ds:+d})")
    return bad


def write_ledger(order, existing):
    tmp = LEDGER.with_suffix(".tsv.tmp")
    with tmp.open("w") as fh:
        fh.write("\t".join(COLUMNS) + "\n")
        for k in order:
            fh.write("\t".join(existing[k].get(c, "") for c in COLUMNS) + "\n")
    os.replace(tmp, LEDGER)                       # atomic; never a half-written ledger


def selftest():
    """Offline tests of merge() and check_seasoning(). No network, nothing written.
    Acceptance condition 4's OVERLAP test lives here: a 10-D/A amending a row that sits
    on an Exeter double-filing date."""
    def row(deal, fd, cp, ms, dq, status="OK"):
        return {c: "" for c in COLUMNS} | {"deal": deal, "filing_date": fd,
                "collection_period": cp, "months_seasoned": str(ms), "dq_60plus_pct": str(dq),
                "status": status}
    results = []
    def t(name, cond):
        results.append(cond); print(f"  {'PASS' if cond else 'FAIL'}  {name}")

    # Double-filing date: Exeter filed TWO reports in Dec-2025 (12-01 -> Oct, 12-23 -> Nov).
    base = [row("EART 2022-2", "2025-11-17", "2025-09-01/2025-09-30", 42, 14.00),
            row("EART 2022-2", "2025-12-01", "2025-10-01/2025-10-31", 43, 14.50),
            row("EART 2022-2", "2025-12-23", "2025-11-01/2025-11-30", 44, 15.00)]
    o, e, s = merge([], {}, base)
    t("double-filing date: two December filings stay TWO rows (distinct periods)", len(o) == 3 and s["added"] == 3)
    t("issuer-clock series passes the seasoning check", check_seasoning(e) == [])

    amend = row("EART 2022-2", "2026-01-20", "2025-10-01/2025-10-31", 43, 14.75)   # 10-D/A
    o2, e2, s2 = merge(o, e, [amend])
    k = ("EART 2022-2", "2025-10-01/2025-10-31")
    t("10-D/A on the double-filing row SUPERSEDES it (no extra row)", len(o2) == 3 and s2["replaced"] == 1)
    t("amended values carried", e2[k]["dq_60plus_pct"] == "14.75" and e2[k]["filing_date"] == "2026-01-20")
    t("the other December row is untouched", e2[("EART 2022-2", "2025-11-01/2025-11-30")]["dq_60plus_pct"] == "15.0")

    # A newest-first run fetches the amendment AND the original; the original must not win.
    o3, e3, s3 = merge(o2, e2, [amend, base[1]])
    t("original 10-D re-read after its amendment does NOT overwrite it", e3[k]["dq_60plus_pct"] == "14.75" and s3["kept"] == 1)
    o4, e4, s4 = merge(o, e, [base[1] | {"status": "INVALID", "dq_60plus_pct": ""}])
    t("an INVALID re-parse never overwrites a good row", e4[k]["dq_60plus_pct"] == "14.5" and s4["kept"] == 1)
    o5, e5, s5 = merge(o, e, [row("EART 2022-2", "2025-05-28", "", "", "")])
    t("a period-less row keys on its filing date, never collides", len(o5) == 4)

    # The OLD clock: 41·43·43·44 (filed-date based) must FAIL closed.
    old = [row("EART 2022-2", "2025-10-28", "2025-09-01/2025-09-30", 41, 1),
           row("EART 2022-2", "2025-12-01", "2025-10-01/2025-10-31", 43, 1),
           row("EART 2022-2", "2025-12-23", "2025-11-01/2025-11-30", 43, 1),
           row("EART 2022-2", "2026-01-28", "2025-12-01/2025-12-31", 44, 1)]
    bad = check_seasoning(merge([], {}, old)[1])
    t("old non-monotone clock (41·43·43·44) FAILS closed", len(bad) == 2)
    gap = [row("SDART 2024-1", "2025-12-15", "2025-11-01/2025-11-30", 23, 1),
           row("SDART 2024-1", "2026-02-17", "2026-01-01/2026-01-31", 25, 1)]
    t("coverage gap with a consistent clock passes", check_seasoning(merge([], {}, gap)[1]) == [])
    skip = [gap[0], row("SDART 2024-1", "2026-01-15", "2025-12-01/2025-12-31", 25, 1)]
    t("a seasoning skip across one month FAILS", len(check_seasoning(merge([], {}, skip)[1])) == 1)
    t("an OK row with empty months_seasoned FAILS", len(check_seasoning(merge([], {}, [row("X", "2026-01-15", "2025-12-01/2025-12-31", "", 1)])[1])) == 1)
    n_fail = results.count(False)
    print(f"\n  selftest: {len(results) - n_fail}/{len(results)} PASS")
    return 0 if n_fail == 0 else 1


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
    if "--selftest" in sys.argv:
        return selftest()
    # --backfill → re-parse EVERY filing already on the ledger for each deal (back to that
    # deal's earliest ledger filing_date) plus anything newer. Added 2026-10-14 for the
    # seasoning-clock repair: the ruling requires ONE parser change + a FULL backfill,
    # never hand edits, and check_seasoning() validates the whole ledger, so a partial
    # re-parse would leave old-clock rows beside new-clock rows and fail closed.
    backfill_since = {}
    if "--backfill" in sys.argv:
        for rec in read_ledger()[1].values():
            if rec.get("filing_date"):
                d0 = backfill_since.get(rec["deal"])
                backfill_since[rec["deal"]] = min(d0, rec["filing_date"]) if d0 else rec["filing_date"]
    run_ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    print(f"\n{'='*104}\n  OTTO 10-D Performance Panel — {run_ts}   ({want} filing(s)/deal)")
    print(f"  FIXED PANEL of named deals — NOT an index. Tiers stay separate by design.\n{'='*104}")

    rows, control_ok = [], None
    for deal, phrase, tier, issuer in PANEL:
        if only and only not in deal.lower():
            continue
        if issuer not in SPECS:
            rows.append(dict(run_ts=run_ts, deal=deal, tier=tier, issuer=issuer, status="UNSUPPORTED",
                             parse_misses="no field spec for issuer", filing_date="", collection_period="",
                             months_seasoned="",
                             dq_60plus_pct="", cnl_pct="", anl_pct="", recovery_pct="", ext_rate_pct="", source_url=""))
            print(f"  {deal:14s} UNSUPPORTED — no field spec"); continue
        try:
            filings, first_date = deal_filings(phrase, want, since=backfill_since.get(deal))
        except Exception as e:
            print(f"  {deal:14s} ERROR resolving filings: {type(e).__name__}"); continue
        if not filings:
            rows.append(dict(run_ts=run_ts, deal=deal, tier=tier, issuer=issuer, status="INVALID",
                             parse_misses="deal phrase matched no 10-D — check the name stem",
                             filing_date="", collection_period="", months_seasoned="",
                             dq_60plus_pct="", cnl_pct="",
                             anl_pct="", recovery_pct="", ext_rate_pct="", source_url=""))
            print(f"  {deal:14s} INVALID — phrase matched no 10-D (name stem wrong?)"); continue

        for fdate, cik, acc in filings:
            try:
                txt, url = exhibit_text(cik, acc)
            except Exception as e:
                print(f"  {deal:14s} {fdate}  ERROR fetching exhibit: {type(e).__name__}"); continue
            v, misses = parse(txt, issuer)
            d = derive(v, issuer)
            cper, cmiss = collection_period(txt)
            if cmiss:
                misses.append(cmiss)
            mseas, mmiss = months_seasoned(txt, issuer)
            if mmiss:
                misses.append(mmiss)
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
                             collection_period=cper or "",
                             months_seasoned="" if mseas is None else mseas,
                             status=status, parse_misses=";".join(misses), source_url=url,
                             **{k: ("" if d[k] is None else d[k]) for k in
                                ("dq_60plus_pct","cnl_pct","anl_pct","recovery_pct","ext_rate_pct")}))
            f = lambda k: f"{d[k]:6.2f}" if d[k] is not None else "   n/d"
            print(f"  {deal:14s} {tier:5s} {fdate}  CP {cper or 'NOT-DISCLOSED':>21s}  MS {mseas if mseas is not None else 'n/d':>3}  60+DQ {f('dq_60plus_pct')}  CNL {f('cnl_pct')}"
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

    print(f"  SEASONING CONTROL — {len(SEASONING_CONTROL)} frozen exhibits, >=3 per shelf, both "
          f"Exeter double-filing dates: ", end="")
    s_ok = run_seasoning_control()
    if s_ok is None:
        print("\n    NOT EVALUATED (exhibit unreachable) → run marked INVALID")
        for r in rows: r["status"] = "INVALID"
    elif s_ok:
        print("PASS ✓")
    else:
        print("\n    **FAIL** → the seasoning parser does not reproduce the exhibits; run marked INVALID")
        for r in rows: r["status"] = "INVALID"

    if dry:
        print("\n  [--dry-run] nothing written\n"); return 0

    # ── UPSERT on (deal, collection_period), atomic write ────────────────────
    # History: a blind append until 2026-08-14 (duplicates inflated n), then an upsert on
    # (deal, filing_date). LIQUID registered the vintage hole in that key 2026-09-02: a
    # 10-D/A filed under a NEW date would land as an ADDITIONAL row, and because the
    # headline test is a matched-collection-month YoY DELTA (two endpoints), one amendment
    # could corrupt every YoY pair touching that deal-month. Fixed 2026-10-14 (CARL ruling
    # 2026-09-17, acceptance condition 4): key on the DISCLOSED collection period, which is
    # the stable identity of a servicer report. See merge() for the supersede rule.
    order, existing = read_ledger()
    order, existing, stats = merge(order, existing, rows)
    bad = check_seasoning(existing)
    if bad:
        print("\n  ⛔ SEASONING CHECK FAILED — ledger NOT written (fails closed):")
        for b in bad:
            print(f"       {b}")
        return 2
    write_ledger(order, existing)
    print(f"\n  {LEDGER.name}: {stats['added']} new row(s), {stats['replaced']} replaced, "
          f"{stats['kept']} kept (an older or INVALID read never overwrites a newer good row), "
          f"{len(order)} total (upsert on deal+collection_period); seasoning check PASS\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
