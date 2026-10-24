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

  # 2) Enumerate documents, then choose the actual HTML document to read.
  python3 edgar_doc.py exhibits --cik 0001212545 --accession 0001212545-26-000045
  # Bare doc is accepted only when one narrative candidate is verified.
  python3 edgar_doc.py doc --cik 0001212545 --accession 0001212545-26-000045
  # Add --doc FILENAME_FROM_INDEX --grep "Florida" for a document-scoped read.

  # 3) Pull a structured XBRL fact (companyconcept) — bank credit metrics etc.
  python3 edgar_doc.py facts --cik 0001212545 --concept Assets
  python3 edgar_doc.py facts --cik 0001212545 --concept FinancingReceivableAllowanceForCreditLosses
  # facts prints start, filed and accession after the original columns, so a
  # three-month and a nine-month row with the same end date and fp are distinct.

  # 4) Evidence-preserving comparison of ONE standard us-gaap duration fact across
  #    two EXACT periods (DOCKET L834; integrated from CATO's prototype, see below).
  python3 edgar_doc.py compare --cik 0001326801 \
      --concept NetCashProvidedByUsedInOperatingActivities --unit USD \
      --prior 2025-07-01 2025-09-30 --current 2026-07-01 2026-09-30 \
      --as-of 2026-10-24 --format markdown --save
  # Replay a saved response instead of fetching (timestamp is the operator's word):
  python3 edgar_doc.py compare --snapshot RESPONSE.json --retrieved-at 2026-10-24T21:43:10+00:00 ...

compare — what it does and does not do:
  Selection: exact start/end and unit; the latest filing on or before --as-of
  (so a prior-year comparative may come from the current filing, visibly);
  conflicting latest records FAIL; period lengths must be within 7 days (a
  disclosed heuristic that catches quarter-vs-year-to-date, not an accounting
  comparability test); prior must end before current starts. No quarter
  subtraction, currency conversion or substitute tag — a tag the issuer does
  not use fails explicitly. Output is a JSON record; Markdown is rendered from
  it. --save keeps the raw SEC response (content-addressed by sha256), the
  JSON and the Markdown under research/edgar_xbrl/<ET date>_<cik>_<concept>_<unit>/.
  Not covered: instant (balance-sheet) metrics, custom tags, segment facts and
  accounting changes need further source work; an operator-supplied retrieval
  timestamp is not independently verified evidence; no claim of measured time
  savings. Limits carried in every record: see COMPARE_LIMITS.

Useful us-gaap concepts for bank credit work:
  Assets, Deposits, FinancingReceivableAllowanceForCreditLosses,
  ProvisionForLoanLeaseAndOtherLosses, FinancingReceivableExcludingAccruedInterestBeforeAllowanceForCreditLoss,
  AllowanceForDoubtfulAccountsReceivable
  (Names drift across filers — use `search` to confirm a tag exists, or pull
   the full set via the SEC companyfacts endpoint. No xbrl_facts helper is exposed.)

CIK cheatsheet + ticker->CIK authority: see edgar_fetch.py header /
https://www.sec.gov/files/company_tickers.json  (always verify before citing).
"""

import json, sys, argparse, urllib.request, urllib.parse, urllib.error, re
import hashlib, math
from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
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
    except EdgarError as e:
        raise EdgarError(
            f"cannot verify the HTML accession index for {accession}: {e}. "
            "The JSON index alone cannot certify the document list; "
            "use an independently verified explicit --doc for a scoped read.") from e
    if not names:
        raise EdgarError(f"no documents listed for {accession} (cik {cik}) — "
                         "verify the accession exists")
    return names


def _primary_doc(cik, accession):
    names = list_documents(cik, accession)
    cands = sorted(n for n in names
                   if n.lower().endswith((".htm", ".html", ".pdf"))
                   and not n.lower().endswith(("-index.html", "-index-headers.html"))
                   and not re.fullmatch(r"R\d+\.html?", n, re.I))
    if len(cands) != 1:
        listing = ", ".join(cands) or "none"
        raise EdgarError(
            f"{accession}: {len(cands)} narrative document candidates ({listing}). "
            "Refusing to select one as the whole filing. Enumerate with exhibits "
            "and read each relevant file with --doc; a scoped miss is not filing-level absence.")
    if cands[0].lower().endswith(".pdf"):
        raise EdgarError(f"{cands[0]} is a PDF; use pdf2text.py for this scoped read")
    return cands[0]


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
            # start/accn/frame kept (L834): without them a three-month and a
            # nine-month row of one 10-Q (same end, same fp) are indistinguishable.
            rows.append({"unit": unit, "end": v.get("end"), "val": v.get("val"),
                         "fy": v.get("fy"), "fp": v.get("fp"), "form": v.get("form"),
                         "filed": v.get("filed"), "start": v.get("start"),
                         "accn": v.get("accn"), "frame": v.get("frame")})
    rows.sort(key=lambda r: (r.get("end") or "", r.get("filed") or ""))
    return data.get("entityName", ""), data.get("label", concept), rows


# --- Evidence-preserving duration compare (DOCKET L834, 2026-10-24) ---------
# Integrated from CATO's isolated prototype
# AGENTS/CATO/runs/2026-10-24_sec-comparison/prepare.py (commit 38e1c2304), with
# its selection policy and explicit failures carried UNCHANGED. Additions here:
# PROME's fifth limit, a retrieval_basis/notes provenance pair, a named cause when
# the requested end holds only an instant fact, and --save (the prototype only
# printed). Transport is this module's _get()/HJSON — same declared-contact UA.

COMPARE_SELECTION = ('Exact periods/unit; latest filed on or before cutoff; '
                     'conflicting latest records rejected')
COMPARE_LIMITS = [
    'Filing cutoff is not a historical API snapshot.',
    'Same concept/unit and similar duration do not establish accounting comparability.',
    'Standard entity-level US-GAAP facts only; custom tags and segment facts need document work.',
    'Filing links identify sources; the source statements have not been independently reconciled.',
    'A fact appears in the SEC API only after the XBRL filing is processed; a press-release number is not in it.',
]
COMPARE_NOTE_INSTANT = ('Instant (balance-sheet) metrics, custom tags, segment facts and accounting '
                        'changes need further source work; this record covers one duration fact.')
RETRIEVAL_NOTES = {
    'live-fetch': 'Retrieved live by edgar_doc.py compare; retrieved_at is the tool clock (UTC) when the response arrived.',
    'operator-snapshot': 'Replayed from a saved response; retrieved_at was supplied by the operator and is not independently verified evidence.',
}
SAVE_ROOT = Path(__file__).resolve().parent.parent / 'research' / 'edgar_xbrl'
_ET = ZoneInfo('America/New_York')


def _iso_day(value):
    return date.fromisoformat(value)


def compare_build(raw, *, cik, concept, unit, prior, current, as_of, retrieved_at,
                  retrieval_basis='operator-snapshot'):
    """CATO's build(), unchanged in policy. Raises ValueError naming the cause."""
    data = json.loads(raw)
    if str(data.get('cik')).lstrip('0') != cik.lstrip('0'):
        raise ValueError('Response issuer does not match requested CIK')
    if data.get('taxonomy') != 'us-gaap' or data.get('tag') != concept:
        raise ValueError('Response taxonomy/concept does not match request')
    stamp = datetime.fromisoformat(retrieved_at.replace('Z', '+00:00'))
    if stamp.tzinfo is None:
        raise ValueError('Retrieval timestamp must include timezone')
    cutoff = _iso_day(as_of)
    if cutoff > stamp.date():
        raise ValueError('Filing cutoff cannot be later than retrieval date')
    durations = [(_iso_day(b) - _iso_day(a)).days + 1 for a, b in (prior, current)]
    if min(durations) <= 0 or abs(durations[0] - durations[1]) > 7:
        raise ValueError('Periods have invalid or mismatched durations; comparison withheld')
    if _iso_day(prior[1]) >= _iso_day(current[0]):
        raise ValueError('Prior and current periods must be ordered and nonoverlapping')
    if retrieval_basis not in RETRIEVAL_NOTES:
        raise ValueError(f'Unknown retrieval basis {retrieval_basis!r}')
    url = CONCEPT.format(cik=f'{int(cik):010d}', concept=concept)
    units = data.get('units', {})

    def select(period):
        matches = [v for v in units.get(unit, [])
                   if (v.get('start'), v.get('end')) == tuple(period)]
        if not matches:
            msg = f'Missing period {period} in unit {unit}; no proxy substituted'
            if any(v.get('start') is None and v.get('end') == period[1] for v in units.get(unit, [])):
                msg += '; only an instant (balance-sheet) fact exists at that end date, duration comparison does not apply'
            if unit not in units:
                msg += f"; units present: {', '.join(sorted(units)) or 'none'}"
            raise ValueError(msg)
        for v in matches:
            if not v.get('filed'):
                raise ValueError('Matching record lacks filing date')
            _iso_day(v['filed'])
        eligible = [v for v in matches if _iso_day(v['filed']) <= cutoff]
        if not eligible:
            raise ValueError(f'No filing on or before cutoff for {period}')
        newest = max(v['filed'] for v in eligible)
        latest = [v for v in eligible if v['filed'] == newest]
        identities = set()
        for v in latest:
            if not re.fullmatch(r'\d{10}-\d{2}-\d{6}', v.get('accn', '')) or not v.get('form'):
                raise ValueError('Selected record lacks valid filing identity/form')
            if isinstance(v.get('val'), bool) or not isinstance(v.get('val'), (int, float)) or not math.isfinite(v['val']):
                raise ValueError('Selected record lacks a finite numeric value')
            identities.add((v['accn'], v['val'], v['form']))
        if len(identities) != 1:
            raise ValueError('Ambiguous latest filing/value; explicit source selection needed')
        v = latest[0]
        return {**{k: v.get(k) for k in ('start', 'end', 'val', 'accn', 'form', 'filed', 'fy', 'fp', 'frame')},
                'unit': unit, 'kind': 'reported',
                'filing_url': f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{v['accn'].replace('-', '')}/{v['accn']}-index.html"}

    old, new = select(prior), select(current)
    delta = new['val'] - old['val']
    pct = delta / old['val'] * 100 if old['val'] > 0 else None
    return {'entity': data.get('entityName'), 'cik': cik, 'concept': concept, 'unit': unit,
            'source_url': url, 'retrieved_at': retrieved_at,
            'response_sha256': hashlib.sha256(raw).hexdigest(), 'filing_cutoff': as_of,
            'selection': COMPARE_SELECTION,
            'prior': old, 'current': new,
            'calculation': {'kind': 'derived', 'difference': delta, 'unit': unit,
                            'formula': 'current.val - prior.val', 'percent_change': pct,
                            'percent_formula': '(current.val - prior.val) / prior.val * 100; omitted when prior <= 0'},
            'limits': list(COMPARE_LIMITS),
            'retrieval_basis': retrieval_basis,
            'notes': [RETRIEVAL_NOTES[retrieval_basis], COMPARE_NOTE_INSTANT]}


def compare_markdown(packet):
    """Render Markdown FROM the JSON record only — never assembled separately."""
    p, c, calc = packet['prior'], packet['current'], packet['calculation']
    lines = [f"# {packet['entity']} — {packet['concept']}", '',
             '| Record | Reporting period | Reported value | Filed | Source |',
             '|---|---|---:|---|---|']
    for label, r in (('Prior', p), ('Current', c)):
        lines.append(f"| {label} | {r['start']} to {r['end']} | {r['val']:,} {r['unit']} | {r['filed']} | [{r['accn']}]({r['filing_url']}) |")
    pct = 'not calculated (prior value is nonpositive)' if calc['percent_change'] is None else f"{calc['percent_change']:+.2f}%"
    lines += ['', f"Calculated change: **{calc['difference']:+,} {calc['unit']}**; {pct}.",
              'Formula: current reported value − prior reported value.', '',
              f"Filing cutoff: {packet['filing_cutoff']}. Retrieved: {packet['retrieved_at']}.",
              f"[SEC data response]({packet['source_url']}); SHA-256 `{packet['response_sha256']}`.", '',
              *[f'- {limit}' for limit in packet['limits']], '']
    if packet.get('notes'):
        lines += ['Notes:', *[f'- {n}' for n in packet['notes']], '']
    return '\n'.join(lines)


def _safe_part(text):
    return re.sub(r'[^A-Za-z0-9_-]', '-', text.replace('/', '_per_'))


def compare_save(raw, packet, md, root=None):
    """Write raw response + JSON + Markdown; never overwrite. Returns [(path, state)]."""
    if hashlib.sha256(raw).hexdigest() != packet['response_sha256']:
        raise ValueError('Raw response does not hash to the record sha256; nothing saved')
    root = Path(root) if root is not None else SAVE_ROOT
    stamp = datetime.fromisoformat(packet['retrieved_at'].replace('Z', '+00:00'))
    day = stamp.astimezone(_ET).date().isoformat()
    folder = root / f"{day}_{int(packet['cik']):010d}_{_safe_part(packet['concept'])}_{_safe_part(packet['unit'])}"
    sha12 = packet['response_sha256'][:12]
    p, c = packet['prior'], packet['current']
    base = f"{p['start']}_{p['end']}_vs_{c['start']}_{c['end']}_cutoff-{packet['filing_cutoff']}_{sha12}"
    targets = [(folder / f'sec-response_{sha12}.json', raw),
               (folder / f'{base}.json', (json.dumps(packet, indent=2) + '\n').encode()),
               (folder / f'{base}.md', md.encode())]
    folder.mkdir(parents=True, exist_ok=True)
    out = []
    for path, blob in targets:
        try:
            with open(path, 'xb') as fh:
                fh.write(blob)
            out.append((path, 'written'))
        except FileExistsError:
            same = path.read_bytes() == blob
            out.append((path, 'already saved, identical' if same else
                        'already saved, earlier record KEPT (differs from this run; not overwritten)'))
    return out


def _cmd_compare(a, save_root=None):
    try:
        if not re.fullmatch(r'\d{1,10}', a.cik) or int(a.cik) <= 0:
            raise ValueError('CIK must be 1–10 digits and positive')
        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9]*', a.concept):
            raise ValueError('Invalid US-GAAP concept name')
        if a.snapshot:
            if not a.retrieved_at:
                raise ValueError('--snapshot requires --retrieved-at; file modification time is not provenance')
            raw, retrieved, basis = Path(a.snapshot).read_bytes(), a.retrieved_at, 'operator-snapshot'
        else:
            if a.retrieved_at:
                raise ValueError('--retrieved-at is only for saved snapshots')
            try:
                raw = _get(CONCEPT.format(cik=f'{int(a.cik):010d}', concept=a.concept), HJSON)
            except EdgarError as exc:
                raise ValueError(str(exc)) from exc
            retrieved, basis = datetime.now(timezone.utc).isoformat(), 'live-fetch'
        packet = compare_build(raw, cik=a.cik, concept=a.concept, unit=a.unit,
                               prior=a.prior, current=a.current, as_of=a.as_of,
                               retrieved_at=retrieved, retrieval_basis=basis)
        md = compare_markdown(packet)
        print(md if a.format == 'markdown' else json.dumps(packet, indent=2))
        if a.save:
            for path, state in compare_save(raw, packet, md, save_root):
                sys.stderr.write(f'SAVED [{state}]: {path}\n')
        return 0
    except (ValueError, TypeError, KeyError, OSError) as exc:
        sys.stderr.write(f'Comparison unavailable: {exc}\n')
        return 2


def main():
    ap = argparse.ArgumentParser(description="EDGAR document reader + XBRL facts")
    sub = ap.add_subparsers(dest="cmd", required=True)

    e = sub.add_parser("exhibits", help="list all accession documents from JSON + HTML index")
    e.add_argument("--cik", required=True)
    e.add_argument("--accession", required=True)

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

    c = sub.add_parser("compare", help="evidence-preserving compare of one us-gaap duration fact across two exact periods")
    c.add_argument("--cik", required=True)
    c.add_argument("--concept", required=True, help="Standard us-gaap concept (no substitution on a miss)")
    c.add_argument("--unit", required=True)
    c.add_argument("--prior", nargs=2, required=True, metavar=("START", "END"))
    c.add_argument("--current", nargs=2, required=True, metavar=("START", "END"))
    c.add_argument("--as-of", required=True, help="Filing-date cutoff, YYYY-MM-DD")
    c.add_argument("--snapshot", help="Saved raw SEC companyconcept JSON; otherwise fetch once")
    c.add_argument("--retrieved-at", help="Required with --snapshot: actual retrieval timestamp including timezone")
    c.add_argument("--format", choices=("json", "markdown"), default="json")
    c.add_argument("--save", action="store_true",
                   help="keep raw response + JSON + Markdown under research/edgar_xbrl/ (never overwrites)")

    a = ap.parse_args()

    if a.cmd == "exhibits":
        names = list_documents(a.cik, a.accession)
        print(f"=== {a.accession} — {len(names)} indexed documents ===")
        for name, size in sorted(names.items()):
            print(f"  {name}  ({size} bytes in JSON index; 0 = size unavailable)")

    elif a.cmd == "search":
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
        print("SCOPE: this document only; this read does not establish whole-filing absence.\n")
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
            # Original columns first, unchanged; start/filed/accn appended (L834).
            print(f"  {r['end']}  {r['fp']} {r['fy']}  {r['form']:<6}  {r['unit']:>4}  {r['val']:,}"
                  f"  start {r['start'] or '- (instant)'}  filed {r['filed']}  {r['accn']}")

    elif a.cmd == "compare":
        return _cmd_compare(a)


if __name__ == "__main__":
    try:
        sys.exit(main() or 0)
    except EdgarError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)
