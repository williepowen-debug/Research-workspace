#!/usr/bin/env python3
"""Servicer filing reader: the same six lines from each listed servicer's 10-Q/10-K. DRAFT ONLY.

Built 2026-11-25 on Will's word (22:02 ET, "build script 2 now ... six listed servicers, six lines";
DAEDALUS notes AGENTS/DAEDALUS/runs/2026-11-25_HOMER_SCRIPT2_READ.md). It writes ONE draft
Markdown file under reports/filing_drafts/ and nothing else: never a ledger, a grade, a band,
a reading cell or a servicer-watch alarm. A figure it cannot find is "not found", never zero.
Reading the filing text stays required before any figure is used.

All SEC access goes through DEWEY's reader, called as a command and never edited:
AGENTS/DEWEY/scripts/edgar_doc.py (facts, exhibits, doc). That reader carries the fleet's
SEC contact (WQ-600) and reads STANDARD us-gaap tags only, so:
  - a line with a standard tag (TAGS below, from the 2026-11-25 survey) prints the tagged value
    for the period and the year-earlier period, both from the SAME filing;
  - every line, tagged or not, also prints the matching statement rows from the filing text with
    their location (document, block number, nearest Note heading) and a link, for reading.

Usage (from AGENTS/HOMER/):
  python3 tools/filing_reader.py read --period 2026-09-30 [PFSI RKT ...]   # draft for the period
  python3 tools/filing_reader.py survey                                     # which lines carry standard tags
  python3 tools/filing_reader.py check                                      # must match HOMER's hand readings
  python3 tools/filing_reader.py --selftest                                 # malformed inputs must FAIL; no network
Exit: 0 every requested company read · 1 any company could not be read, or a check failed · 2 usage.
"""
import datetime as dt, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DESK = os.path.normpath(os.path.join(HERE, ".."))
ROOT = os.path.normpath(os.path.join(DESK, "..", ".."))
EDGAR = os.path.join(ROOT, "AGENTS", "DEWEY", "scripts", "edgar_doc.py")
OUTDIR = os.path.join(DESK, "reports", "filing_drafts")

# Panel: the five names in registry/SERVICER_WATCH.md, plus Rithm (see RITHM_REASON). Freedom is
# private and files no 10-Q. Adding a name here adds data only; it never adds a name to the watch.
COMPANIES = [("PFSI", "PennyMac Financial Services", "1745916"), ("RKT", "Rocket Companies", "1805284"),
             ("UWMC", "UWM Holdings", "1783398"), ("LDI", "loanDepot", "1831631"),
             ("ONIT", "Onity Group", "873860"), ("RITM", "Rithm Capital", "1556593")]
RITHM_REASON = ("Rithm is not named in SERVICER_WATCH.md. Included as data only: it was on the 8/23 "
                "non-funding-leverage panel and in the 9/29 sweep (KB-HOMER-033), and it owns Newrez, a "
                "large non-bank servicer. Its inclusion adds no name to the watch (Will-gated).")

# The six lines. `rx` finds statement rows in the filing text; `after` = extra rows printed after a hit
# (tables whose numbers sit on the next row). `kind` sets the year-earlier pairing for tagged values.
LINES = [
    ("advances", "Servicing advances: cash used or released (cash flow statement)", "duration",
     r"(increase|decrease)\)?.{0,25}(servicing|servicer) advances|^(servicing |servicer )?advances,? net|servicer advances receivable", 0),
    ("hedge_cash", "Cash spent or received on hedges (cash flow statement)", "duration",
     r"settlement.{0,60}(derivative|hedg)|(derivative|hedg).{0,40}settle|hedging (gain|loss)", 0),
    ("gse_liquidity", "Cushion over the Fannie Mae / Freddie Mac liquidity requirement", "text",
     r"liquidity requirement|minimum liquidity|^liquidity( \(\d\))?\s*(\||$)|fannie mae (&|and) freddie mac", 2),
    ("dq60", "Delinquency of the servicing book, 60+ days", "text",
     r"60\+|60 days|60 or more days", 0),
    ("debt_equity", "Debt, equity and unsecured notes (maturities in the notes)", "instant",
     r"senior (unsecured )?notes|unsecured (senior )?notes|total (stockholders|shareholders)' equity|total equity", 0),
    ("msr", "Mortgage servicing rights at fair value, and the change", "instant",
     r"(mortgage )?servicing rights?,? at fair value|msrs?,? at fair value|change in fair value of msr", 0),
]

# Standard tags found by the 2026-11-25 survey (`survey`), verified against the Q3-2026 statement rows.
# Only these are read as tagged values; everything else is text only. Re-run `survey` after a
# company changes its tagging; never add a tag that the survey did not find.
EQ = "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"
TAGS = {  # survey 2026-11-25 22:19 ET, period 2026-09-30; advances and the two text lines: no tag at any company
    ("PFSI", "hedge_cash"): ["PaymentsForProceedsFromDerivativeInstrumentInvestingActivities"],
    ("PFSI", "debt_equity"): [EQ, "LongTermDebt"],
    ("RKT", "debt_equity"): [EQ, "UnsecuredDebt", "SecuredDebt"],
    ("RKT", "msr"): ["ServicingAssetAtFairValueAmount"],
    ("UWMC", "debt_equity"): [EQ, "SeniorNotes"],
    ("LDI", "debt_equity"): [EQ, "LongTermDebt"],
    ("LDI", "msr"): ["ServicingAssetAtFairValueAmount"],
    ("ONIT", "debt_equity"): [EQ, "SeniorNotes"],
    ("ONIT", "msr"): ["ServicingAssetAtFairValueAmount"],
    ("RITM", "debt_equity"): [EQ, "UnsecuredDebt", "SecuredDebt", "LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths"],
    ("RITM", "msr"): ["ServicingAssetAtFairValueAmount"],
}
# A tag's meaning is the issuer's: LongTermDebt is total debt at LDI and secured plus unsecured at
# RITM, for example. The reader never computes a ratio across tags or across companies.

# Blocks printed BEFORE a hit: liquidity tables put "Required | Reported" (or "Actual | Required")
# headers in a separate block above the row (Onity, 2026-11-25), and the row is unreadable without it.
BEFORE = {"gse_liquidity": 3}

HEADING = re.compile(r"^(note|NOTE)\s*\d+\b|^\d{1,2}\.\s+[A-Z][A-Za-z ,&’']{3,}$|^(PART|Item|ITEM)\s+[0-9IV]+")


class ReadError(Exception):
    pass


def edgar(*args, timeout=150):
    r = subprocess.run([sys.executable, EDGAR, *args], capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout, r.stderr


# ---------- facts ----------
FACT_RX = re.compile(r"^\s+(\d{4}-\d{2}-\d{2})\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(-?[\d,]+(?:\.\d+)?)"
                     r"\s+start (\d{4}-\d{2}-\d{2}|- \(instant\))\s+filed (\d{4}-\d{2}-\d{2})\s+(\S+)\s*$")


def parse_facts(text):
    """Rows of `edgar_doc.py facts` output. A data-looking line that does not parse is an error."""
    rows = []
    for line in text.splitlines():
        if not line.startswith("  ") or not line.strip():
            continue
        m = FACT_RX.match(line)
        if not m:
            raise ReadError(f"unparseable facts line: {line.strip()[:120]!r}")
        end, fp, fy, form, unit, val, start, filed, accn = m.groups()
        rows.append(dict(end=end, fp=fp, fy=fy, form=form, unit=unit, val=float(val.replace(",", "")),
                         start=None if start.startswith("-") else start, filed=filed, accn=accn))
    return rows


def pick(rows, accn, start, end):
    """One value for (start, end) from the given filing; None if absent; error if the filing disagrees with itself."""
    hit = {r["val"] for r in rows if r["accn"] == accn and r["end"] == end and r["start"] == start and r["unit"] == "USD"}
    if len(hit) > 1:
        raise ReadError(f"filing {accn} carries {len(hit)} different values for {start or 'instant'}..{end}")
    return hit.pop() if hit else None


def periods(kind, period):
    e = dt.date.fromisoformat(period)
    ye = dt.date(e.year - 1, e.month, e.day if not (e.month == 2 and e.day == 29) else 28)
    if kind == "duration":  # year to date, and the same months a year earlier
        return (f"{e.year}-01-01", period), (f"{e.year - 1}-01-01", ye.isoformat())
    return (None, period), (None, f"{e.year - 1}-12-31")  # balance: period end vs last year end


def tagged_value(cik, concept, kind, period, accn):
    rc, out, err = edgar("facts", "--cik", cik, "--concept", concept, "--last", "200")
    if rc != 0:
        raise ReadError(f"facts {concept} failed: {err.strip()[:160]}")
    rows = parse_facts(out)
    cur, pri = periods(kind, period)
    return pick(rows, accn, *cur), pick(rows, accn, *pri), cur, pri


# ---------- filing and text ----------
def find_filing(cik, period):
    """Accession of the 10-Q/10-K whose balance sheet is dated `period` (via the Assets fact)."""
    rc, out, err = edgar("facts", "--cik", cik, "--concept", "Assets", "--last", "40")
    if rc != 0:
        raise ReadError(f"facts Assets failed: {err.strip()[:160]}")
    accns = {r["accn"] for r in parse_facts(out) if r["end"] == period and r["form"] in ("10-Q", "10-K")
             and r["start"] is None}
    if len(accns) != 1:
        raise ReadError(f"{len(accns)} 10-Q/10-K filings with a balance sheet dated {period} (need exactly 1)")
    return accns.pop()


def choose_doc(names):
    """The main report among a filing's documents: an .htm named with an 8-digit date, not an exhibit."""
    main = [n for n in names if n.lower().endswith(".htm") and re.search(r"\d{8}", n)
            and not re.search(r"ex(hibit)?[-_]?\d|ex\d|^a3[12]|-index|^r\d+\.htm", n.lower())]
    if len(main) != 1:
        raise ReadError(f"{len(main)} candidate main documents ({', '.join(main) or 'none'}); need exactly 1")
    return main[0]


def filing_text(cik, accn):
    rc, out, err = edgar("exhibits", "--cik", cik, "--accession", accn)
    if rc != 0:
        raise ReadError(f"exhibits failed: {err.strip()[:160]}")
    names = re.findall(r"^  (\S+)  \(", out, re.M)
    doc = choose_doc(names)
    rc, out, err = edgar("doc", "--cik", cik, "--accession", accn, "--doc", doc, timeout=240)
    if rc != 0 or len(out) < 20000:
        raise ReadError(f"doc {doc} failed or too short ({len(out)} chars): {err.strip()[:160]}")
    return doc, out


def blocks(text):
    """Table rows and paragraphs: the reader prints one cell per line and a blank line between rows."""
    out = []
    for b in re.split(r"\n\s*\n", text):
        b = re.sub(r"\s*\n\s*", " | ", b.strip()).replace("​", "")
        b = re.sub(r"(\|\s*)+", "| ", b).strip(" |")
        if b:
            out.append(b)
    return out


def text_hits(bl, rx, after, limit=4, before=0):
    pat = re.compile(rx, re.I)
    hits, heading = [], ""
    for i, b in enumerate(bl):
        if HEADING.search(b[:80]):
            heading = b[:70]
        if len(b) <= 450 and pat.search(b) and re.search(r"\d", " ".join(bl[i:i + after + 1])):
            hits.append((i, heading, " ⏎ ".join(x[:300] for x in bl[max(0, i - before):i + after + 1])))
            if len(hits) >= limit:
                break
    return hits


def money(v):
    return "not found" if v is None else f"${v / 1e6:,.1f}M"


def read_company(key, name, cik, period):
    accn = find_filing(cik, period)
    doc, text = filing_text(cik, accn)
    bl = blocks(text)
    link = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn.replace('-', '')}/{doc}"
    out = [f"## {key} — {name} (CIK {cik})", "",
           f"Filing {accn} · document [{doc}]({link}) · {len(bl):,} blocks read", ""]
    for lk, label, kind, rx, after in LINES:
        out.append(f"### {label}")
        concepts = TAGS.get((key, lk), [])
        for concept in concepts:
            cur, pri, cp, pp = tagged_value(cik, concept, kind, period, accn)
            out.append(f"- **Tagged** `us-gaap:{concept}` (sign as the issuer tags it): "
                       f"{money(cur)} [{cp[0] or 'at'} {cp[1]}] vs {money(pri)} [{pp[0] or 'at'} {pp[1]}], "
                       f"both from {accn}")
        if not concepts:
            out.append("- **No standard tag** (survey 2026-11-25): text only")
        hits = text_hits(bl, rx, after, before=BEFORE.get(lk, 0))
        if not hits:
            out.append(f"- Text: **not found** in {doc} (this document only; not proof the filing lacks it)")
        for i, head, row in hits:
            out.append(f"- Text, block {i}{' under ' + repr(head) if head else ''}: `{row}`")
        out.append("")
    return out


def cmd_read(period, keys):
    want = [c for c in COMPANIES if not keys or c[0] in keys]
    stamp = subprocess.run(["date", "+%Y-%m-%d %H:%M"], capture_output=True, text=True,
                           env={**os.environ, "TZ": "America/New_York"}).stdout.strip()
    lines = [f"# Servicer filing draft — period ending {period}", "",
             f"**DRAFT, generated {stamp} ET by `tools/filing_reader.py`.** Not a ledger, grade or alarm. "
             "Read the filing before using any figure; a value marked not found is unknown, not zero. "
             "Tagged values are the issuer's XBRL as SEC serves it; text rows are this tool's parse of "
             "DEWEY's document read and can split or merge table cells.", "", f"*{RITHM_REASON}*", ""]
    failed = []
    for key, name, cik in want:
        try:
            lines += read_company(key, name, cik, period)
            print(f"OK    {key}")
        except (ReadError, subprocess.TimeoutExpired) as e:
            failed.append(key)
            lines += [f"## {key} — {name}: **COULD NOT BE READ**: {e}", ""]
            print(f"FAIL  {key}: {e}")
    os.makedirs(OUTDIR, exist_ok=True)
    path = os.path.join(OUTDIR, f"{period}_servicers_DRAFT_{stamp[:10]}_{stamp[11:].replace(':', '')}.md")
    with open(path, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"DRAFT {os.path.relpath(path, DESK)} — {len(want) - len(failed)} of {len(want)} companies read")
    return path, failed


# ---------- survey ----------
CANDIDATES = {
    "advances": ["IncreaseDecreaseInServicingAdvances", "PaymentsForProceedsFromServicingAdvances"],
    "hedge_cash": ["PaymentsForProceedsFromDerivativeInstrumentInvestingActivities",
                   "PaymentsForDerivativeInstrumentInvestingActivities", "ProceedsFromDerivativeInstrumentInvestingActivities",
                   "PaymentsForProceedsFromHedgeInvestingActivities"],
    "debt_equity": ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
                    "UnsecuredDebt", "SeniorNotes"],
    "msr": ["ServicingAssetAtFairValueAmount"],
}


def cmd_survey(period="2026-09-30"):
    print(f"Standard-tag survey, period {period} (gse_liquidity and dq60 have no standard us-gaap tag: text only)")
    for key, name, cik in COMPANIES:
        try:
            accn = find_filing(cik, period)
        except ReadError as e:
            print(f"{key:<5} FILING NOT FOUND: {e}")
            continue
        for lk, cands in CANDIDATES.items():
            found = []
            for c in cands:
                rc, out, err = edgar("facts", "--cik", cik, "--concept", c, "--last", "200")
                if rc == 0 and any(r["accn"] == accn and r["end"] == period for r in parse_facts(out)):
                    found.append(c)
            print(f"{key:<5} {lk:<12} {'TAGGED: ' + ', '.join(found) if found else 'untagged (text only)'}")
    return 0


# ---------- hand-reading check ----------
HAND = [  # (company, line, strings that must all appear in that line's text hits, hand source)
    ("PFSI", "advances", ["( 240,485 )"], "PFSI Q3 10-Q cash flow, nine months −$240.5M (PIPELINE row 'PENNYMAC 10-Q OPENED', 11/25)"),
    ("PFSI", "gse_liquidity", ["793,788", "699,504"], "Fannie/Freddie liquidity $793.8M vs $699.5M required = cushion $94.3M (PIPELINE 11/25)"),
    ("LDI", "dq60", ["2.05", "1.45", "2,371,572"], "LDI Q3 8-K: 60+ DQ 2.0% ($2.37B) vs 1.5% a year earlier (PIPELINE 11/11, a different document)"),
]
HAND_TAGGED = [("PFSI", "hedge_cash", 1349.8, "PFSI Q3 10-Q hedge settlements nine months −$1,349.8M (PIPELINE 11/25); tag is a payment, so positive"),
               ("LDI", "debt_equity", 310.9, "LDI Q3 8-K: equity $310.9M (PIPELINE 11/11, a different document)")]


def cmd_check(period="2026-09-30"):
    bad = 0
    for key in sorted({h[0] for h in HAND} | {h[0] for h in HAND_TAGGED}):
        _, name, cik = next(c for c in COMPANIES if c[0] == key)
        accn = find_filing(cik, period)
        _, text = filing_text(cik, accn)
        bl = blocks(text)
        for co, lk, needs, src in [h for h in HAND if h[0] == key]:
            spec = next(l for l in LINES if l[0] == lk)
            got = " ".join(h[2] for h in text_hits(bl, spec[3], spec[4], before=BEFORE.get(lk, 0)))
            miss = [n for n in needs if n not in got]
            print(f"{'ok  ' if not miss else 'FAIL'} {co} {lk}: {'matches' if not miss else 'missing ' + str(miss)} — {src}")
            bad += bool(miss)
        for co, lk, want, src in [h for h in HAND_TAGGED if h[0] == key]:
            concept = (TAGS.get((co, lk)) or [None])[0]
            cur = tagged_value(cik, concept, next(l for l in LINES if l[0] == lk)[2], period, accn)[0] if concept else None
            ok = cur is not None and abs(cur / 1e6 - want) < 0.1
            print(f"{'ok  ' if ok else 'FAIL'} {co} {lk} tagged: {money(cur)} vs hand {want}M — {src}")
            bad += not ok
    print(f"CHECK {'PASS' if not bad else 'FAIL'}: {bad} mismatch(es)")
    return 1 if bad else 0


# ---------- selftest (no network) ----------
def selftest():
    good = ("  2026-09-30  Q3 2026  10-Q     USD  1,349,779,000  start 2026-01-01  filed 2026-11-03  0001104659-26-121982\n"
            "  2025-09-30  Q3 2026  10-Q     USD  -143,439,000  start 2025-01-01  filed 2026-11-03  0001104659-26-121982\n")
    cases = [
        ("facts line with a missing column", lambda: parse_facts("  2026-09-30  Q3 2026  10-Q  USD  1,000  filed 2026-11-03  X\n")),
        ("facts line with a non-number value", lambda: parse_facts(good.replace("1,349,779,000", "n/a"))),
        ("one filing, two values for one period", lambda: pick(parse_facts(good + good.splitlines()[0].replace("1,349,779,000", "9") + "\n"),
                                                               "0001104659-26-121982", "2026-01-01", "2026-09-30")),
        ("no main document among exhibits", lambda: choose_doc(["pfsi-ex31d1.htm", "R1.htm", "FilingSummary.xml"])),
        ("two candidate main documents", lambda: choose_doc(["abc-20260930.htm", "abc-20260930x10q.htm"])),
    ]
    bad = 0
    for name, fn in cases:
        try:
            fn()
            print(f"  FAIL (accepted): {name}"); bad += 1
        except ReadError as e:
            print(f"  ok  refused: {name} — {e}")
    rows = parse_facts(good)
    checks = [
        ("year-earlier value read from the same filing", pick(rows, "0001104659-26-121982", "2025-01-01", "2025-09-30") == -143439000.0),
        ("absent period is None, shown as 'not found', never zero", pick(rows, "0001104659-26-121982", "2024-01-01", "2024-09-30") is None
         and money(None) == "not found"),
        ("other filing's rows are not used", pick(rows, "0000000000-00-000000", "2026-01-01", "2026-09-30") is None),
        ("main document chosen among exhibits", choose_doc(["nrz-20260930.htm", "ritm-2026930exhibit311.htm", "R2.htm"]) == "nrz-20260930.htm"),
        ("table row joined and found", text_hits(blocks("(Increase) decrease in servicing advances\n\n( 240,485 )\n\n\nX\n\n"), LINES[0][3], 0) == []
         and bool(text_hits(blocks("(Increase) decrease in servicing advances\n( 240,485 )\n\nX"), LINES[0][3], 0))),
        ("text with no match reports nothing, not a figure", text_hits(blocks("Nothing here 123\n\nOther 456"), LINES[1][3], 0) == []),
    ]
    for name, ok in checks:
        print(f"  {'ok ' if ok else 'FAIL'} {name}"); bad += not ok
    print(f"SELFTEST {'PASS' if not bad else 'FAIL'}: {len(cases)} malformed inputs, {len(checks)} behaviour checks, {bad} failure(s)")
    return 1 if bad else 0


def main(argv):
    if argv == ["--selftest"]:
        return selftest()
    if not argv or argv[0] not in ("read", "survey", "check"):
        print(__doc__); return 2
    if argv[0] == "survey":
        return cmd_survey()
    if argv[0] == "check":
        return cmd_check()
    if len(argv) < 3 or argv[1] != "--period" or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", argv[2]):
        print("usage: read --period YYYY-MM-DD [TICKER ...]"); return 2
    keys = argv[3:]
    unknown = [k for k in keys if k not in {c[0] for c in COMPANIES}]
    if unknown:
        print(f"unknown company {unknown}; choose from {[c[0] for c in COMPANIES]}"); return 2
    _, failed = cmd_read(argv[2], keys)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
