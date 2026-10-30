#!/usr/bin/env python3
"""
WAL Boot Kit — v0.1 (built 2026-10-28; Will in session: "yes build the boot script").
Charter boot step 5 in one command: the live price against the owner-held EV and REGINALD's
exit level, plus every carrier this desk waits on — SEC filings (periodic report, 8-K,
Form 144, 13D/G, Form 4 transaction codes), the FFIEC Call Report filer list, FINRA short
interest.

Usage (repo root):
  .venv/bin/python3 AGENTS/WAL/scripts/boot.py
  ... --since YYYY-MM-DD   # filing window start (default: the STATUS.md "Last Updated" date)
  ... --offline            # skip every network source (each is reported UNCHECKED)

Exit code: 0 = every source read, nothing new · 1 = ATTENTION (a carrier moved or a desk
figure needs a refresh) · 2 = nothing needs attention but at least one source was UNCHECKED.
⚠️ A source that could not be read is never reported as quiet: UNCHECKED is not clean
(`finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction`).

Read-only: writes nothing, never prints credential material. Reference values are read from
their owners at run time — EV from THESIS.md, the exit level from REGINALD's THRESHOLDS.tsv,
the last MI3 quarter from MI3_SERIES.tsv, the last logged short-interest settlement from
KB.tsv — never hardcoded here (`finding_a_frozen_denominator_fails_toward_all_clear_invisibly`).
"""

import argparse
import base64
import csv
import io
import json
import re
import subprocess
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from pathlib import Path

WAL_DIR = Path(__file__).resolve().parent.parent          # AGENTS/WAL
REPO_ROOT = WAL_DIR.parent.parent
FETCH = REPO_ROOT / "FORGE" / "tools" / "market-data" / "fetch.py"
ENV_FILE = REPO_ROOT / "FORGE" / "tools" / "market-data" / ".env"
THRESHOLDS = REPO_ROOT / "AGENTS" / "REGINALD" / "registry" / "THRESHOLDS.tsv"
EXIT_LOG = REPO_ROOT / "AGENTS" / "REGINALD" / "registry" / "REG_T02_EXIT_LOG.tsv"

CIK = "0001212545"                 # Western Alliance Bancorporation
RSSD = 3138146                     # Western Alliance Bank (Call Report filer)
SEC_UA = "WAL-Research williepowen@gmail.com"   # SEC requires a contact; fleet form (REGINALD/CYPHER)
FFIEC_URL = "https://ffieccdr.azure-api.us/public/"
FINRA_URL = "https://api.finra.org/data/group/otcMarket/name/consolidatedShortInterest"
BIG_MOVE = 3.0                     # charter step 5: "WAL can move 3-5% in a session"
JWT_WARN_DAYS = 14                 # same horizon env_doctor warns at

# 8-K items that bear directly on the bear legs (impairment, restatement, officer change).
HOT_8K_ITEMS = {"2.06": "material impairment", "4.02": "non-reliance / restatement",
                "5.02": "officer or director change (V4)"}
ROUTINE_FORM4 = {"A", "D", "F", "M", "G", "J", "I", "C", "W"}   # grants, settlements, withholding, gifts


class Report:
    """Collects ATTENTION and UNCHECKED items so the footer and exit code cannot disagree."""

    def __init__(self):
        self.attention, self.unchecked = [], []

    def attend(self, msg):
        self.attention.append(msg)
        print(f"  🟠 ATTENTION: {msg}")

    def miss(self, msg):
        self.unchecked.append(msg)
        print(f"  ⚠️  UNCHECKED: {msg}")

    def rc(self):
        return 1 if self.attention else (2 if self.unchecked else 0)


def section(title):
    print(f"\n── {title} " + "─" * max(0, 66 - len(title)))


# ---------------------------------------------------------------- owner-file readers (pure)

def status_last_updated(text):
    m = re.search(r"Last Updated:\s*(\d{4}-\d{2}-\d{2})", text)
    return datetime.strptime(m[1], "%Y-%m-%d").date() if m else None


def thesis_ev(text):
    """EV from the THESIS.md header — the owner surface (CLAUDE.md: THESIS owns version/EV/PT)."""
    head = "\n".join(text.splitlines()[:6])
    m = re.search(r"EV \$(\d+(?:\.\d+)?)", head)
    return float(m[1]) if m else None


def exit_level(thresholds_text):
    """REG-T-02's exit level from REGINALD's registry row ('WAL >= 81.90 on 3 consecutive ...')."""
    for line in thresholds_text.splitlines():
        if line.startswith("REG-T-02\t"):
            m = re.search(r">=\s*(\d+(?:\.\d+)?)", line.split("\t")[-1])
            return float(m[1]) if m else None
    return None


def exit_log_last(text):
    """Last data row of REGINALD's exit log: (date, close, run, state). Pointer only — REGINALD grades."""
    rows = [l.split("\t") for l in text.splitlines() if re.match(r"\d{4}-\d{2}-\d{2}\t", l)]
    if not rows:
        return None
    r = rows[-1]
    return r[0], r[1], r[3], r[4]


def mi3_last_quarter(text):
    rows = [l for l in text.splitlines() if l and not l.startswith("#")]
    dates = [l.split("\t")[0] for l in rows[1:] if re.match(r"\d{4}-\d{2}-\d{2}", l)]
    return datetime.strptime(max(dates), "%Y-%m-%d").date() if dates else None


def kb_latest_finra_settlement(kb_text):
    """Newest 'FINRA settlement YYYY-MM-DD' among ACTIVE KB rows (the last logged reading)."""
    lines = [l for l in kb_text.splitlines() if l and not l.startswith("#")]
    best = None
    for r in csv.DictReader(lines, delimiter="\t"):
        if r.get("Status") != "ACTIVE":
            continue
        m = re.search(r"FINRA settlement (\d{4}-\d{2}-\d{2})", r.get("Fact") or "")
        if m:
            d = datetime.strptime(m[1], "%Y-%m-%d").date()
            best = d if best is None or d > best else best
    return best


# ---------------------------------------------------------------- calendar helpers (pure)

def latest_quarter_end(today):
    """Most recent calendar quarter end strictly before `today`."""
    for back in range(0, 5):
        y, q = today.year, (today.month - 1) // 3 - back
        while q < 0:
            q, y = q + 4, y - 1
        m = 3 * q + 3
        end = date(y, m, 31 if m in (3, 12) else 30)
        if end < today:
            return end
    raise ValueError(today)


def periodic_report(qend):
    """(form, statutory due date) for a large accelerated filer: 10-Q +40 days, 10-K +60 days."""
    return ("10-K", qend + timedelta(days=60)) if qend.month == 12 else ("10-Q", qend + timedelta(days=40))


def call_report_due(qend):
    return qend + timedelta(days=30)


def jwt_expiry(token):
    """Expiry date from a JWT's own `exp` claim; None when the token is not a decodable JWT."""
    try:
        payload = token.split(".")[1]
        claims = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)))
        return datetime.fromtimestamp(int(claims["exp"])).date()
    except (IndexError, ValueError, KeyError, TypeError):
        return None


def fmt(d):
    return f"{d.strftime('%a')} {d.isoformat()}"


# ---------------------------------------------------------------- filing classification (pure)

def form4_codes(xml_text):
    """(non-derivative codes, derivative codes) from a Form 4 ownership XML."""
    root = ET.fromstring(xml_text)
    nd = [t.findtext("transactionCoding/transactionCode") for t in root.iter("nonDerivativeTransaction")]
    dv = [t.findtext("transactionCoding/transactionCode") for t in root.iter("derivativeTransaction")]
    return [c for c in nd if c], [c for c in dv if c]


def classify(form, items):
    """('carrier'|'attention'|'insider'|'info', label) for one issuer filing."""
    if form in ("10-Q", "10-K", "10-Q/A", "10-K/A"):
        return "carrier", "periodic report — run the frozen 10-Q frame verbatim"
    if form in ("8-K", "8-K/A"):
        hot = [f"{i} {HOT_8K_ITEMS[i]}" for i in items if i in HOT_8K_ITEMS]
        return "attention", "8-K items " + (", ".join(items) or "none listed") + (f" — 🔴 {'; '.join(hot)}" if hot else "")
    if form == "144":
        return "attention", "Form 144 planned sale (V4 discriminator)"
    if "13D" in form or "13G" in form:
        return "attention", "beneficial-ownership filing"
    if form in ("4", "4/A"):
        return "insider", "Form 4"
    return "info", form


# ---------------------------------------------------------------- network sources

def http(url, headers=None, data=None, timeout=20):
    req = urllib.request.Request(url, data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def run_fetch(tickers, today):
    """FORGE fetch.py price --json, with the served vintage checked (OZK boot.py §8 contract)."""
    try:
        out = subprocess.run([sys.executable, str(FETCH), "price", *tickers, "--json"],
                             capture_output=True, text=True, timeout=45)
    except (subprocess.TimeoutExpired, OSError) as e:
        return None, f"fetch.py did not run ({type(e).__name__})"
    if out.returncode != 0 or not out.stdout.strip():
        return None, f"fetch.py rc={out.returncode}: {(out.stderr or '').strip()[:200]}"
    try:
        return json.loads(out.stdout), None
    except json.JSONDecodeError:
        return None, "fetch.py stdout was not JSON"


def last_weekday(d):
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d


def price_section(rep, today, args):
    section("PRICE  (FORGE fetch.py; EV from THESIS.md; exit level from REGINALD THRESHOLDS.tsv)")
    ev = thesis_ev((WAL_DIR / "THESIS.md").read_text(encoding="utf-8"))
    lvl = exit_level(THRESHOLDS.read_text(encoding="utf-8")) if THRESHOLDS.exists() else None
    if args.offline:
        rep.miss("price (offline)")
    else:
        data, err = run_fetch(["WAL", "KRE"], today)
        wal = (data or {}).get("WAL") or {}
        if err or not wal.get("price"):
            rep.miss(f"price — {err or 'WAL missing from payload'}")
        else:
            p, chg, asof = wal["price"], wal.get("change_pct"), wal.get("asof")
            live = asof == last_weekday(today).isoformat()
            tag = f"[{asof}{'' if live else ' — NOT the latest session: stale or holiday'}]"
            print(f"  WAL ${p:.2f} ({'chg n/a' if chg is None else f'{chg:+.2f}%'}) {tag}")
            kre = data.get("KRE") or {}
            if kre.get("price"):
                kc = kre.get("change_pct")
                print(f"  KRE ${kre['price']:.2f} ({'chg n/a' if kc is None else f'{kc:+.2f}%'})")
            if ev:
                print(f"  SPOT vs EV ${ev:.2f}: {(p - ev) / ev * 100:+.2f}% (delta/EV)")
            else:
                rep.miss("EV not found in the THESIS.md header")
            if lvl:
                print(f"  Buffer to exit level ${lvl:.2f}: {(lvl - p) / p * 100:+.2f}% (delta/spot)")
            if chg is not None and abs(chg) >= BIG_MOVE:
                rep.attend(f"WAL moved {chg:+.2f}% (≥{BIG_MOVE:.0f}%) — check news/filings before citing")
            if not live:
                rep.miss(f"price vintage {asof} is not the latest session; re-pull before citing")
    if EXIT_LOG.exists():
        last = exit_log_last(EXIT_LOG.read_text(encoding="utf-8"))
        if last:
            print(f"  REGINALD exit log last row {last[0]} (close {last[1]}): run {last[2]} of 3, {last[3]} — REGINALD grades")
    st = status_last_updated((WAL_DIR / "STATUS.md").read_text(encoding="utf-8"))
    if st and st < today:
        print(f"  STATUS.md price tokens date from {st}: re-sync the header price AND the buffer line at closeout")


def filings_section(rep, today, since, args):
    qend = latest_quarter_end(today)
    form, due = periodic_report(qend)
    section(f"SEC FILINGS  (CIK {CIK}; window from {since}; {form} for {qend} due {fmt(due)})")
    if args.offline:
        rep.miss("SEC EDGAR (offline)")
        return
    try:
        sub = json.loads(http(f"https://data.sec.gov/submissions/CIK{CIK}.json", {"User-Agent": SEC_UA}))
    except Exception as e:
        rep.miss(f"SEC submissions JSON ({type(e).__name__})")
        return
    r = sub["filings"]["recent"]
    rows = [{k: r[k][i] for k in ("form", "filingDate", "reportDate", "accessionNumber", "items", "primaryDocument")}
            for i in range(len(r["form"]))]
    periodic = [x for x in rows if x["form"] in (form, form + "/A") and x["reportDate"] == qend.isoformat()]
    if periodic:
        x = periodic[-1]
        rep.attend(f"{form} for {qend} FILED {x['filingDate']} ({x['accessionNumber']}) — run the frozen frame, then the re-score rule")
    else:
        late = " — PAST the statutory date: look for an NT filing" if today > due else ""
        print(f"  {form} for {qend}: NOT FILED (statutory {fmt(due)}, {(due - today).days}d){late}")
        if late:
            rep.attend(f"{form} for {qend} not filed after its statutory date")
    new = [x for x in rows if x["filingDate"] >= since.isoformat()]
    if not new:
        print(f"  No issuer filings since {since}.")
    form4_fetches = 0
    for x in sorted(new, key=lambda x: x["filingDate"]):
        kind, label = classify(x["form"], [i for i in (x["items"] or "").split(",") if i])
        line = f"{x['filingDate']} {x['form']} {x['accessionNumber']}"
        if kind == "carrier":
            if x not in periodic:                      # the current-quarter report is announced above
                rep.attend(f"{line} (period {x['reportDate']}) — {label}")
            continue
        if kind == "attention":
            rep.attend(f"{line} — {label}")
        elif kind == "insider":
            if form4_fetches >= 40:
                rep.miss(f"{line} — Form 4 codes not read (fetch cap 40)")
                continue
            doc = x["primaryDocument"].split("/")[-1]
            url = f"https://www.sec.gov/Archives/edgar/data/{int(CIK)}/{x['accessionNumber'].replace('-', '')}/{doc}"
            try:
                time.sleep(0.15)                       # SEC fair access: stay well under 10 req/s
                form4_fetches += 1
                nd, dv = form4_codes(http(url, {"User-Agent": SEC_UA}).decode("utf-8", "replace"))
            except Exception as e:
                rep.miss(f"{line} — Form 4 XML not read ({type(e).__name__})")
                continue
            odd = sorted({c for c in nd if c not in ROUTINE_FORM4})
            if odd:
                rep.attend(f"{line} — Form 4 non-derivative code(s) {','.join(odd)} (P = open-market buy, S = sale: V4)")
            else:
                print(f"  {line} — routine codes {','.join(sorted(set(nd + dv))) or 'none'}")
        else:
            print(f"  {line} — {label} (info)")


def ffiec_section(rep, today, args):
    qend = latest_quarter_end(today)
    due = call_report_due(qend)
    section(f"FFIEC CALL REPORT  (RSSD {RSSD}; {qend} due {fmt(due)})")
    mi3 = mi3_last_quarter((WAL_DIR / "workbook" / "MI3_SERIES.tsv").read_text(encoding="utf-8"))
    print(f"  MI3_SERIES.tsv last quarter: {mi3}")
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if line.strip() and not line.lstrip().startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    user, token = env.get("FFIEC_CDR_USERNAME"), env.get("FFIEC_CDR_TOKEN")
    if not user or not token:
        rep.miss("FFIEC credentials absent on this box (PROME/MACHINE_LOCAL.md)")
        return
    exp = jwt_expiry(token)
    if exp is None:
        print("  JWT expiry: not decodable")
    elif exp <= today:
        rep.attend(f"FFIEC JWT EXPIRED {exp} — renewal is Will's (WILL_QUEUE row 31)")
        return
    else:
        left = (exp - today).days
        print(f"  JWT expires {fmt(exp)} ({left}d)")
        if left <= JWT_WARN_DAYS and mi3 is not None and mi3 < qend:
            rep.attend(f"FFIEC JWT expires in {left}d while the {qend} pull is still owed — pull before {exp} or renew (WILL_QUEUE row 31)")
    if args.offline:
        rep.miss("FFIEC filer list (offline)")
        return
    headers = {"UserID": user, "Authentication": "Bearer " + token, "Content-Type": "application/json",
               "dataSeries": "Call", "reportingPeriodEndDate": qend.strftime("%m/%d/%Y"),
               "lastUpdateDateTime": (qend + timedelta(days=1)).strftime("%m/%d/%Y")}
    # Same transport as scripts/ffiec_wal_retrieve_20261014.py: headers go to curl on stdin, never argv.
    config = "\n".join('header = "%s"' % (k + ": " + v).replace("\\", "\\\\").replace('"', '\\"')
                       for k, v in headers.items())
    try:
        res = subprocess.run(["curl", "-sS", "--max-time", "40", "--config", "-", "--write-out", "\n%{http_code}",
                              FFIEC_URL + "RetrieveFilersSinceDate"], input=config, text=True,
                             capture_output=True, timeout=60)
        body, code = res.stdout.rsplit("\n", 1)
        filers = json.loads(body) if code == "200" else None
    except Exception as e:
        rep.miss(f"FFIEC filer list ({type(e).__name__})")
        return
    if not isinstance(filers, list):
        rep.miss(f"FFIEC filer list HTTP {code}")
        return
    filed = RSSD in filers or str(RSSD) in map(str, filers)
    if filed and (mi3 is None or mi3 < qend):
        rep.attend(f"Call Report for {qend} FILED — pull it (ffiec_wal_retrieve_20261014.py, new dated sources folder) and append the MI3_SERIES row")
    elif filed:
        print(f"  Call Report for {qend} filed; MI3_SERIES already carries it.")
    else:
        note = " — past the due date; public posting can lag a few days" if today > due else ""
        print(f"  Call Report for {qend}: NOT FILED yet ({len(filers)} banks filed so far){note}")


def tracker_last(text, metric):
    """Newest Date for `metric` in workbook/MARKET_TRACKER.tsv (long format), else None."""
    ds = [l.split("\t")[0] for l in text.splitlines()
          if not l.startswith("#") and l.count("\t") >= 2 and l.split("\t")[1] == metric]
    return date.fromisoformat(max(ds)) if ds else None


def finra_section(rep, today, args):
    section("FINRA SHORT INTEREST + MARKET TRACKER  (last logged = workbook/MARKET_TRACKER.tsv)")
    tracker = (WAL_DIR / "workbook" / "MARKET_TRACKER.tsv").read_text(encoding="utf-8")
    kb_last = tracker_last(tracker, "short_interest_shares")
    snap = tracker_last(tracker, "close_WAL")
    print(f"  Tracker last FINRA settlement: {kb_last} · last price snapshot: {snap}")
    if snap is None or (today - snap).days > 10:
        rep.attend(f"market tracker snapshot is {'missing' if snap is None else f'{(today - snap).days}d old'} — run scripts/market_tracker.py --write")
    if args.offline:
        rep.miss("FINRA (offline)")
        return
    q = {"limit": 50, "compareFilters": [{"fieldName": "symbolCode", "fieldValue": "WAL", "compareType": "EQUAL"}],
         "dateRangeFilters": [{"fieldName": "settlementDate", "startDate": (today - timedelta(days=75)).isoformat(),
                               "endDate": today.isoformat()}]}
    try:
        rows = json.loads(http(FINRA_URL, {"Content-Type": "application/json", "Accept": "application/json"},
                               json.dumps(q).encode()))
    except Exception as e:
        rep.miss(f"FINRA ({type(e).__name__})")
        return
    if not rows:
        rep.miss("FINRA returned no WAL rows for the last 75 days")
        return
    last = max(rows, key=lambda r: r["settlementDate"])
    pct = last.get("changePercent")
    print(f"  FINRA latest settlement {last['settlementDate']}: {last['currentShortPositionQuantity']:,} shares "
          f"({'chg n/a' if pct is None else f'{pct:+.2f}%'}), days-to-cover {last.get('daysToCoverQuantity')}")
    if kb_last is None or last["settlementDate"] > kb_last.isoformat():
        rep.attend(f"FINRA settlement {last['settlementDate']} is newer than the tracker's — run scripts/market_tracker.py --write")


def main():
    ap = argparse.ArgumentParser(description="WAL boot kit — price and carriers in one command (read-only).")
    ap.add_argument("--since", help="filing window start YYYY-MM-DD (default: STATUS.md Last Updated date)")
    ap.add_argument("--offline", action="store_true", help="skip network sources (reported UNCHECKED)")
    args = ap.parse_args()
    today = date.today()
    since = (datetime.strptime(args.since, "%Y-%m-%d").date() if args.since
             else status_last_updated((WAL_DIR / "STATUS.md").read_text(encoding="utf-8")) or today - timedelta(days=7))
    print(f"WAL BOOT KIT v0.1 — {datetime.now().strftime('%a %Y-%m-%d %H:%M')} (local clock)")
    rep = Report()
    price_section(rep, today, args)
    filings_section(rep, today, since, args)
    ffiec_section(rep, today, args)
    finra_section(rep, today, args)
    section("SUMMARY")
    for m in rep.attention:
        print(f"  🟠 {m}")
    for m in rep.unchecked:
        print(f"  ⚠️  UNCHECKED — {m}")
    if not rep.attention and not rep.unchecked:
        print("  Nothing new across price, filings, Call Report and short interest.")
    print(f"  rc={rep.rc()} (0 quiet · 1 attention · 2 unchecked). Scope: these four sources only — "
          "not news, courts, peers or the inbox (boot steps 4c, 6, 7, 7b).")
    return rep.rc()


if __name__ == "__main__":
    sys.exit(main())
