#!/usr/bin/env python3
"""ABS-EE office screen: largest lease ending before the loan matures.

Scope: research/2026-10-22_ABS-EE_LEASE_SCREEN_SCOPE.md (Will: build after the
October Trepp print; started on his word 2026-11-05).

PERIMETER: registered CMBS trusts that file Form ABS-EE, roughly 2017+ vintages.
It does NOT see 144A SASB, CRE CLO, pre-2017 conduits or bank balance sheets.
Never call its output "the office market".

Usage (run with .venv/bin/python3 from the repo root):
  absee_office_screen.py fetch  --index FILE [--index FILE] --cache DIR
                                --from 2026-10-10 --to 2026-11-05
  absee_office_screen.py screen --cache DIR --out-prefix PATH

If a tape is flagged as misfiled, pull that trust's prior filing into the same
cache with fetch --only 'NAME$' and an earlier date window, then re-run screen.

fetch reads SEC full-index form.idx files and stores each commercial-mortgage
filing gzipped in the cache, with a manifest. It keeps the downloads outside
the repo. screen writes <prefix>_loans.tsv and <prefix>_summary.json.

Rules that matter:
- Commercial mortgages are identified by the filing header's ABS ASSET CLASS,
  never by trust name.
- Balances are each trust's own note, so pari-passu pieces add up in dollars.
  They are merged for COUNTS only. See piece_groups().
- The maturity tested is the earliest of the anticipated repayment date and the
  contractual or modified maturity. The ARD case is reported separately.
- A blank field stays blank. Nothing is imputed, and every exclusion is counted.
- Two October 2026 filings carried another trust's whole loan tape. A tape that
  fully matches another trust's is replaced by the wrong trust's prior filing.
  See find_duplicate_tapes().
- The headline uses tenant data reviewed within about 15 months. Staler rows are
  counted and disclosed, never tested.
"""
import argparse
import collections
import csv
import datetime as dt
import gzip
import json
import os
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

CMBS_CLASS = "Commercial mortgages"
# Skipping by name only saves bandwidth: auto EX-102 files run to hundreds of MB.
# Anything not skipped here is still classified by its header.
SKIP_NAME = re.compile(
    r"\b(auto|automobile|vehicle|motorcycle|lease|leasing|receivables|equipment|"
    r"carmax|carvana|harley|floorplan|dealer)\b",
    re.I,
)
STALE_REVIEW_DAYS = 456  # ~15 months, scope step 5
THIN_DSCR = 1.25
THIN_OCC = 0.80
MATURITY_YEARS = (2026, 2027, 2028, 2029)
CURRENT_LAG_DAYS = 45
REFI_WINDOW_DAYS = 730  # a lease ending under 2 years after maturity; CREED addition, not in the scope
DEFEASED_CODES = {"F", "IP"}  # full, in part. X = not applicable, N = none.


def parse_date(text):
    """MM-DD-YYYY as filed; None when blank or malformed."""
    if not text:
        return None
    m = re.fullmatch(r"(\d{2})-(\d{2})-(\d{4})", text.strip())
    if not m:
        return None
    try:
        return dt.date(int(m.group(3)), int(m.group(1)), int(m.group(2)))
    except ValueError:
        return None


def parse_num(text):
    if text is None or not str(text).strip():
        return None
    try:
        return float(text)
    except ValueError:
        return None


def header_value(text, label):
    m = re.search(re.escape(label) + r":\s*(.+)", text)
    return m.group(1).strip() if m else None


def extract_ex102(text):
    """Return the EX-102 XML of a full-submission text, or None."""
    for doc in re.finditer(r"<DOCUMENT>(.*?)</DOCUMENT>", text, re.S):
        body = doc.group(1)
        if re.search(r"<TYPE>EX-102", body):
            m = re.search(r"<XML>\s*(.*?)\s*</XML>", body, re.S)
            return m.group(1) if m else None
    return None


def _strip(tag):
    return tag.rsplit("}", 1)[-1]


def parse_assets(xml_text):
    """Yield one dict per asset: flat asset fields plus a 'properties' list."""
    xml_text = re.sub(r"^\s*<\?xml[^>]*\?>", "", xml_text)
    root = ET.fromstring(xml_text)
    for node in root:
        if _strip(node.tag) != "assets":
            continue
        asset = {"properties": []}
        for child in node:
            name = _strip(child.tag)
            if name == "property":
                asset["properties"].append({_strip(c.tag): (c.text or "").strip() for c in child})
            else:
                asset[name] = (child.text or "").strip()
        yield asset


def norm_zip(value):
    digits = re.sub(r"\D", "", value or "")[:5]
    return digits.zfill(5) if digits else ""


def effective_maturity(asset):
    """Earliest of ARD and contractual or post-modification maturity.

    Returns (date, basis) with basis ARD, MOD or CONTRACT.
    A modified maturity replaces the original one. An ARD counts only if it
    falls before that date.
    """
    contract = parse_date(asset.get("maturityDate"))
    modified = parse_date(asset.get("postModificationMaturityDate"))
    ard = parse_date(asset.get("hyperAmortizingDate"))
    legal, basis = (modified, "MOD") if modified else (contract, "CONTRACT")
    if ard and (legal is None or ard < legal):
        return ard, "ARD"
    return legal, basis


def is_delinquent_status(code):
    """Payment status 1, 2, 3 or 5 = 30+ past due or non-performing matured.

    0 current, A/B grace or under 30 days, 4 performing matured balloon.
    """
    return (code or "").strip().upper() in {"1", "2", "3", "5"}


def status_resolved(row):
    """CURRENT, DELINQUENT or UNKNOWN. A blank code is judged on paid-through.

    Some trusts leave the payment status blank on current loans. A blank code
    counts as current only if paid through within CURRENT_LAG_DAYS of period
    end. Otherwise it is UNKNOWN and stays out of the performing book.
    """
    code = (row.get("status") or "").strip().upper()
    if code:
        return "DELINQUENT" if is_delinquent_status(code) else "CURRENT"
    paid, period = row.get("paid_through"), row.get("period_end")
    if paid and period and (period - paid).days <= CURRENT_LAG_DAYS:
        return "CURRENT"
    return "UNKNOWN"


def loan_record(asset, trust, period_end):
    """Flatten one asset to a screen row, or None if it has no live balance."""
    balance = parse_num(asset.get("reportPeriodEndActualBalanceAmount"))
    if not balance or balance <= 0:
        return None
    props = asset.get("properties") or []
    types = [(p.get("propertyTypeCode") or "").upper() for p in props]
    values = [parse_num(p.get("valuationSecuritizationAmount")) or 0.0 for p in props]
    total_value = sum(values)
    office_value = sum(v for v, t in zip(values, types) if t == "OF")
    first = props[0] if props else {}
    maturity, basis = effective_maturity(asset)
    contract = parse_date(asset.get("maturityDate"))

    def pick(field):
        for prop in props:
            if prop.get(field):
                return prop[field]
        return asset.get(field)

    nra = parse_num(first.get("netRentableSquareFeetNumber"))
    tenant_sf = parse_num(first.get("squareFeetLargestTenantNumber"))
    return {
        "trust": trust,
        "asset": asset.get("assetNumber"),
        "name": first.get("propertyName", ""),
        "address": first.get("propertyAddress", ""),
        "city": first.get("propertyCity", ""),
        "state": first.get("propertyState", ""),
        "zip": norm_zip(first.get("propertyZip")),
        "county": first.get("propertyCounty", ""),
        "n_props": len(props),
        "type": first.get("propertyTypeCode", "").upper() if len(props) == 1 else "PORTFOLIO",
        "office_value_share": (office_value / total_value) if total_value else None,
        "all_office": bool(types) and all(t == "OF" for t in types),
        "balance": balance,
        "original": parse_num(asset.get("originalLoanAmount")),
        "structure": asset.get("loanStructureCode", ""),
        "origination": parse_date(asset.get("originationDate")),
        "maturity": maturity,
        "maturity_basis": basis,
        "contract_maturity": contract,
        "status": asset.get("paymentStatusLoanCode", ""),
        "paid_through": parse_date(asset.get("paidThroughDate")),
        "ss_transfer": parse_date(asset.get("mostRecentSpecialServicerTransferDate")),
        "ss_return": parse_date(asset.get("mostRecentMasterServicerReturnDate")),
        "defeased": (first.get("DefeasedStatusCode") or "").upper(),
        "dscr": parse_num(pick("mostRecentDebtServiceCoverageNetCashFlowpercentage")),
        "occupancy": parse_num(pick("mostRecentPhysicalOccupancyPercentage")),
        "tenant": first.get("largestTenant", ""),
        "tenant_sf": tenant_sf,
        "nra": nra,
        "lease_end": parse_date(first.get("leaseExpirationLargestTenantDate")),
        "review": parse_date(first.get("mostRecentAnnualLeaseRolloverReviewDate")),
        "value": parse_num(first.get("valuationSecuritizationAmount")),
        "period_end": period_end,
    }


def in_special_servicing(row):
    """Open transfer: a transfer date with no later return date."""
    transfer, back = row.get("ss_transfer"), row.get("ss_return")
    return bool(transfer) and (back is None or back < transfer)


def is_performing(row):
    return status_resolved(row) == "CURRENT" and not in_special_servicing(row)


def is_defeased(row):
    return row.get("defeased") in DEFEASED_CODES


def tenant_share(row):
    if row.get("tenant_sf") and row.get("nra"):
        return row["tenant_sf"] / row["nra"]
    return None


def _same_size(a, b):
    """True if the two rentable areas agree within 2%, or either is blank."""
    if not a or not b:
        return True
    return abs(a - b) / max(a, b) <= 0.02


def piece_groups(rows):
    """Union rows that are notes on one building.

    Two rows join when they share state, zip, rentable area and maturity, or
    state, zip and origination date with rentable areas within 2%. Separate
    buildings under one origination stay apart, because each has its own tenant
    and its own balance. Balances are summed, never deduplicated: each trust
    reports only the note it holds. Rows with no zip never join.
    """
    parent = list(range(len(rows)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    by_size, by_orig = {}, collections.defaultdict(list)
    for i, row in enumerate(rows):
        if not row.get("zip"):
            continue
        if row.get("nra") and row.get("contract_maturity"):
            key = (row["state"], row["zip"], row["nra"], row["contract_maturity"])
            if key in by_size:
                parent[find(i)] = find(by_size[key])
            else:
                by_size[key] = i
        if row.get("origination"):
            key = (row["state"], row["zip"], row["origination"])
            for j in by_orig[key]:
                if _same_size(row.get("nra"), rows[j].get("nra")):
                    parent[find(i)] = find(j)
            by_orig[key].append(i)
    groups = collections.defaultdict(list)
    for i in range(len(rows)):
        groups[find(i)].append(i)
    return [[rows[i] for i in idx] for idx in groups.values()]


def merge_group(pieces):
    """One record per building. Dollars add; the freshest tenant data speaks.

    Trusts disagree on lease dates for the same loan, so tenant fields come from
    the piece with the latest lease review. Credit status is worst-of: one
    delinquent or specially serviced piece marks the whole loan.
    """
    src = max(
        pieces,
        key=lambda r: (
            r.get("lease_end") is not None,
            r.get("review") or dt.date.min,
            r["balance"],
        ),
    )
    merged = dict(src)
    merged["balance"] = sum(r["balance"] for r in pieces)
    merged["n_pieces"] = len(pieces)
    merged["trusts"] = sorted({r["trust"] for r in pieces})
    merged["lease_disagreed"] = len({r.get("lease_end") for r in pieces}) > 1
    for field in ("dscr", "occupancy"):
        if merged.get(field) is None:
            merged[field] = next((r[field] for r in pieces if r.get(field) is not None), None)
    for rank in ("DELINQUENT", "UNKNOWN"):
        worst = next((r for r in pieces if status_resolved(r) == rank), None)
        if worst:
            merged["status"], merged["paid_through"] = worst.get("status"), worst.get("paid_through")
            break
    serviced = next((r for r in pieces if in_special_servicing(r)), None)
    if serviced:
        merged["ss_transfer"], merged["ss_return"] = serviced["ss_transfer"], serviced.get("ss_return")
    modified = next((r for r in pieces if r.get("maturity_basis") == "MOD"), None)
    if modified:
        merged["maturity"], merged["maturity_basis"] = modified["maturity"], "MOD"
    return merged


def tape_key(row):
    return (row.get("asset"), round(row["balance"], 2), row.get("name"), row.get("maturity"))


def find_duplicate_tapes(rows, threshold=0.95):
    """Return {wrong_trust: right_trust} where one trust carries another's tape.

    Notes on one loan overlap by a handful of rows at most; a filing error
    overlaps fully. Of a matched pair, the wrong trust is the one whose name year
    sits furthest above the latest loan origination in the tape.
    """
    tapes = collections.defaultdict(list)
    for row in rows:
        tapes[row["trust"]].append(row)
    owners = collections.defaultdict(list)
    for trust, items in tapes.items():
        for key in {tape_key(r) for r in items}:
            owners[key].append(trust)
    overlap = collections.Counter()
    for trusts in owners.values():
        for i, a in enumerate(sorted(trusts)):
            for b in sorted(trusts)[i + 1 :]:
                overlap[(a, b)] += 1

    def gap(trust):
        m = re.search(r"\b(20\d{2})-", trust)
        latest = max((r["origination"].year for r in tapes[trust] if r.get("origination")), default=None)
        return (int(m.group(1)) - latest) if m and latest else -99

    out = {}
    for (a, b), count in overlap.items():
        if count >= threshold * max(len(tapes[a]), len(tapes[b])):
            wrong, right = (a, b) if gap(a) > gap(b) else (b, a)
            out[wrong] = right
    return out


def screen_row(row):
    """Classify one single-property office row. Returns the screen flags."""
    lease, maturity, period = row.get("lease_end"), row.get("maturity"), row.get("period_end")
    review = row.get("review")
    share = tenant_share(row)
    return {
        "testable": bool(lease and maturity),
        "before_maturity": bool(lease and maturity and lease < maturity),
        "refi_window": bool(
            lease and maturity and lease >= maturity and (lease - maturity).days <= REFI_WINDOW_DAYS
        ),
        "lease_passed": bool(lease and period and lease <= period),
        "matured": bool(maturity and period and maturity <= period),
        "share": share,
        "fresh": bool(review and period and (period - review).days <= STALE_REVIEW_DAYS),
        "thin_dscr": row.get("dscr") is not None and row["dscr"] < THIN_DSCR,
        "thin_occ": row.get("occupancy") is not None and row["occupancy"] < THIN_OCC,
    }


def bucket_year(maturity):
    if maturity is None:
        return "blank"
    if maturity.year < MATURITY_YEARS[0]:
        return "before 2026"
    if maturity.year > MATURITY_YEARS[-1]:
        return "2030+"
    return str(maturity.year)


def summarize(rows):
    """Headline table over merged, live, undefeased, performing office loans."""
    out = collections.OrderedDict()

    def add(key, row):
        cell = out.setdefault(key, [0, 0.0])
        cell[0] += 1
        cell[1] += row["balance"]

    for row in rows:
        flags = screen_row(row)
        add("book", row)
        if not flags["testable"]:
            add("not testable", row)
            continue
        if flags["matured"]:
            add("already past maturity", row)
            continue
        year = bucket_year(row["maturity"])
        add("forward book", row)
        add(f"forward {year}", row)
        if not flags["fresh"]:
            add("stale tenant data", row)
            add(f"stale {year}", row)
            continue
        add("fresh book", row)
        add(f"fresh {year}", row)
        share = flags["share"]
        thin = flags["thin_dscr"] or flags["thin_occ"]
        if flags["refi_window"]:
            add("window", row)
            add(f"window {year}", row)
            if share is not None and share > 0.30:
                add("window share>30", row)
                add(f"window share>30 {year}", row)
                if thin:
                    add("window share>30 thin", row)
                    add(f"window share>30 thin {year}", row)
        if not flags["before_maturity"]:
            continue
        cuts = ["hit"]
        if share is not None and share > 0.30:
            cuts.append("share>30")
        if share is not None and share > 0.50:
            cuts.append("share>50")
        if thin:
            cuts.append("thin")
        if thin and share is not None and share > 0.30:
            cuts.append("share>30 thin")
        for cut in cuts:
            add(cut, row)
            add(f"{cut} {year}", row)
        if flags["lease_passed"]:
            add("hit lease date already passed", row)
        if row.get("maturity_basis") == "ARD":
            add("hit on ARD basis", row)
    return out


LA_COUNTY_ZIP3 = {str(z) for z in range(900, 919)} | {"935"}
ORANGE_ZIP3 = {"926", "927", "928"}


def metro_slice(rows, include_orange=False):
    """Los Angeles control perimeter: county name, else zip prefix."""
    out = []
    for row in rows:
        county = (row.get("county") or "").upper()
        zip3 = (row.get("zip") or "")[:3]
        hit = "LOS ANGELES" in county or (not county and zip3 in LA_COUNTY_ZIP3)
        if include_orange:
            hit = hit or "ORANGE" in county and row.get("state") == "CA" or (not county and zip3 in ORANGE_ZIP3)
        if hit and row.get("state") == "CA":
            out.append(row)
    return out


def fetch_url(url, ua, head_only_class=None, chunk=1 << 20, timeout=180):
    """Read a filing, stopping early if its header is not the wanted class."""
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        head = resp.read(8192)
        klass = header_value(head.decode("latin1"), "ABS ASSET CLASS")
        if head_only_class and klass != head_only_class:
            return klass, None
        parts = [head]
        while True:
            block = resp.read(chunk)
            if not block:
                break
            parts.append(block)
    return klass, b"".join(parts)


def index_rows(paths, start, end):
    for path in paths:
        with open(path, encoding="latin1") as fh:
            for line in fh:
                if not line.startswith("ABS-EE"):
                    continue
                m = re.match(
                    r"(ABS-EE(?:/A)?)\s+(.+?)\s+(\d+)\s+(\d{4}-\d{2}-\d{2})\s+(edgar/\S+)", line
                )
                if m and start <= m.group(4) <= end:
                    yield m.groups()


def cmd_fetch(args):
    from sec_contact import sec_ua

    ua = sec_ua()
    os.makedirs(args.cache, exist_ok=True)
    manifest = os.path.join(args.cache, "manifest.tsv")
    done = {}
    if os.path.exists(manifest):
        with open(manifest, encoding="utf-8") as fh:
            for rec in csv.DictReader(fh, delimiter="\t"):
                done[rec["path"]] = rec
    rows = {}
    skipped = 0
    for form, name, cik, date, path in index_rows(args.index, args.start, args.end):
        if SKIP_NAME.search(name) or (args.only and not re.search(args.only, name)):
            skipped += 1
            continue
        rows.setdefault(path, (form, name, cik, date))
    print(f"index: {len(rows)} unique filings to classify, {skipped} rows skipped by name")
    fields = ["path", "form", "name", "cik", "date", "class", "bytes", "status"]
    new_file = not os.path.exists(manifest)
    with open(manifest, "a", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        if new_file:
            writer.writeheader()
        for i, (path, (form, name, cik, date)) in enumerate(sorted(rows.items())):
            if path in done:
                continue
            url = "https://www.sec.gov/Archives/" + path
            rec = dict(path=path, form=form, name=name, cik=cik, date=date, bytes=0)
            try:
                klass, data = fetch_url(url, ua, head_only_class=CMBS_CLASS)
                rec["class"] = klass or ""
                rec["status"] = "SKIPPED_CLASS"
                if data:
                    target = os.path.join(args.cache, path.replace("/", "_") + ".gz")
                    with gzip.open(target, "wb") as out:
                        out.write(data)
                    rec["bytes"] = len(data)
                    rec["status"] = "OK"
            except Exception as exc:  # recorded and retried on the next run
                rec["class"] = ""
                rec["status"] = f"ERROR {type(exc).__name__}"
                done_err = rec["status"]
                print(f"  {path}: {done_err}", file=sys.stderr)
            if not rec["status"].startswith("ERROR"):
                writer.writerow(rec)
                fh.flush()
            time.sleep(0.15)
            if i % 50 == 0:
                print(f"  {i}/{len(rows)}", flush=True)
    print("done")


def _tape(text, trust):
    rows = []
    for asset in parse_assets(extract_ex102(text) or ""):
        row = loan_record(asset, trust, parse_date(asset.get("reportingPeriodEndDate")))
        if row:
            rows.append(row)
    return rows


def load_rows(cache):
    """Parse the newest filing per trust, repairing any misfiled tape."""
    with open(os.path.join(cache, "manifest.tsv"), encoding="utf-8") as fh:
        manifest = [r for r in csv.DictReader(fh, delimiter="\t") if r["status"] == "OK"]
    filings = collections.defaultdict(list)
    for rec in manifest:
        with gzip.open(os.path.join(cache, rec["path"].replace("/", "_") + ".gz"), "rb") as fh:
            text = fh.read().decode("latin1")
        trust = header_value(text, "COMPANY CONFORMED NAME") or rec["name"]
        period = header_value(text, "CONFORMED PERIOD OF REPORT") or ""
        filings[trust].append((period, rec["date"], rec["path"], text))
    rows, errors = [], []
    cycle = collections.Counter()
    chosen = {}
    for trust, items in filings.items():
        items.sort(key=lambda f: (f[0], f[1]), reverse=True)
        chosen[trust] = items[0]
        cycle[items[0][0][:6]] += 1
        try:
            if not extract_ex102(items[0][3]):
                errors.append((items[0][2], "no EX-102"))
                continue
            rows.extend(_tape(items[0][3], trust))
        except ET.ParseError as exc:
            errors.append((items[0][2], f"xml {exc}"))
    repairs = []
    for wrong, right in find_duplicate_tapes(rows).items():
        lost = [r for r in rows if r["trust"] == wrong]
        rows = [r for r in rows if r["trust"] != wrong]
        prior = filings[wrong][1] if len(filings[wrong]) > 1 else None
        repaired = _tape(prior[3], wrong) if prior else []
        rows.extend(repaired)
        repairs.append(
            {
                "trust": wrong,
                "tape_actually_from": right,
                "dropped_rows": len(lost),
                "dropped_balance": sum(r["balance"] for r in lost),
                "replacement_period": prior[0] if prior else None,
                "replacement_rows": len(repaired),
                "replacement_balance": sum(r["balance"] for r in repaired),
            }
        )
    return rows, errors, cycle, len(filings), repairs


COLUMNS = (
    "cut trusts n_pieces name address city state zip balance maturity maturity_basis contract_maturity "
    "tenant share lease_end review dscr occupancy status lease_disagreed"
).split()


def write_loans(rows, path):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t")
        writer.writerow(COLUMNS)
        for row in sorted(rows, key=lambda r: -r["balance"]):
            flags = screen_row(row)
            if not ((flags["before_maturity"] or flags["refi_window"]) and flags["fresh"] and not flags["matured"]):
                continue
            cells = []
            for col in COLUMNS:
                value = flags["share"] if col == "share" else row.get(col)
                if col == "cut":
                    value = "LEASE_BEFORE_MATURITY" if flags["before_maturity"] else "ENDS_UNDER_2Y_AFTER"
                if col == "trusts":
                    value = "; ".join(value)
                if col == "share" and value is not None:
                    value = round(value, 3)
                if isinstance(value, float) and col == "balance":
                    value = round(value)
                cells.append("" if value is None else value)
            writer.writerow(cells)


def run_screen(cache):
    rows, errors, cycle, trusts, repairs = load_rows(cache)
    types = collections.Counter()
    type_balance = collections.Counter()
    for row in rows:
        types[row["type"]] += 1
        type_balance[row["type"]] += row["balance"]
    office = [r for r in rows if r["type"] == "OF" and r["n_props"] == 1]
    groups = piece_groups(office)
    loans = [merge_group(g) for g in groups]
    live = [r for r in loans if not is_defeased(r)]
    book = [r for r in live if is_performing(r)]
    states = collections.Counter()
    state_balance = collections.Counter()
    for row in live:
        key = status_resolved(row)
        if key == "CURRENT" and in_special_servicing(row):
            key = "SPECIAL SERVICING, NOT DELINQUENT"
        states[key] += 1
        state_balance[key] += row["balance"]
    unclassified = [
        r for r in rows
        if r["type"] == ""
        and r["name"].strip().lower() not in {"defeased", "na", "n/a", "", "defeasance"}
    ]
    portfolio = [r for r in rows if r["type"] == "PORTFOLIO"]
    control = {}
    for label, orange in (("la_county", False), ("la_plus_orange", True)):
        metro = metro_slice(live, include_orange=orange)
        city = [r for r in metro if (r.get("city") or "").upper() == "LOS ANGELES"]
        other = [r for r in metro if (r.get("city") or "").upper() != "LOS ANGELES"]
        cell = {}
        for name, part in (("all", metro), ("city_of_la", city), ("rest", other)):
            testable = [r for r in part if r.get("lease_end") and r.get("maturity")]
            hits = [r for r in testable if r["lease_end"] < r["maturity"]]
            big = [r for r in hits if (tenant_share(r) or 0) > 0.50]
            bad = [r for r in part if status_resolved(r) == "DELINQUENT"]
            serviced = [r for r in part if in_special_servicing(r)]
            total = sum(r["balance"] for r in part) or 1.0
            cell[name] = {
                "loans": len(part),
                "balance": sum(r["balance"] for r in part),
                "hit_balance": sum(r["balance"] for r in hits),
                "hit_share_of_balance": sum(r["balance"] for r in hits) / total,
                "hit_over_50_balance": sum(r["balance"] for r in big),
                "dq_share": sum(r["balance"] for r in bad) / total,
                "ss_share": sum(r["balance"] for r in serviced) / total,
            }
        control[label] = cell
    summary = {
        "trusts": trusts,
        "cycle": dict(cycle),
        "repairs": repairs,
        "parse_errors": errors,
        "live_rows_all_types": len(rows),
        "live_balance_all_types": sum(r["balance"] for r in rows),
        "by_type": {k: [types[k], type_balance[k]] for k, _ in types.most_common()},
        "single_office_rows": len(office),
        "single_office_balance": sum(r["balance"] for r in office),
        "office_loans_after_merge": len(loans),
        "multi_piece_loans": sum(1 for r in loans if r["n_pieces"] > 1),
        "lease_disagreed_loans": sum(1 for r in loans if r.get("lease_disagreed")),
        "defeased": [sum(1 for r in loans if is_defeased(r)), sum(r["balance"] for r in loans if is_defeased(r))],
        "live_status": {k: [states[k], state_balance[k]] for k in states},
        "unclassified_named_rows": [len(unclassified), sum(r["balance"] for r in unclassified)],
        "portfolio_all_office": [
            sum(1 for r in portfolio if r["all_office"]),
            sum(r["balance"] for r in portfolio if r["all_office"]),
        ],
        "mixed_use": [types["MU"], type_balance["MU"]],
        "screen": dict(summarize(book)),
        "la_control": control,
    }
    return summary, book


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    fetch = sub.add_parser("fetch")
    fetch.add_argument("--index", action="append", required=True)
    fetch.add_argument("--cache", required=True)
    fetch.add_argument("--from", dest="start", required=True)
    fetch.add_argument("--to", dest="end", required=True)
    fetch.add_argument("--only", help="regex on filer name; used to pull one trust's prior filing")
    screen = sub.add_parser("screen")
    screen.add_argument("--cache", required=True)
    screen.add_argument("--out-prefix", required=True)
    args = parser.parse_args()
    if args.cmd == "fetch":
        cmd_fetch(args)
        return 0
    summary, book = run_screen(args.cache)
    with open(args.out_prefix + "_summary.json", "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1, default=str)
    write_loans(book, args.out_prefix + "_loans.tsv")
    print(json.dumps(summary, indent=1, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
