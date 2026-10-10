#!/usr/bin/env python3
"""
REGINALD 8-K Filing Monitor
Checks each thesis bank's material-event filings at the regulator the bank ACTUALLY files with:
SEC EDGAR for holding companies, FDIC FLNG for Bank OZK (cert 110, files with the FDIC since 2017).

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/8k_monitor.py
  .venv/bin/python3 AGENTS/REGINALD/scripts/8k_monitor.py --days 30
  .venv/bin/python3 AGENTS/REGINALD/scripts/8k_monitor.py --selftest   # fixtures, no network

Per-name state (only CLEAR and FOUND are reads; everything else is NO VERDICT):
  CLEAR        route reached, response valid, issuer identity matched, route live, nothing in window
  FOUND        filing(s) in window — item numbers parsed, or marked UNPARSED (severity unknown)
  FAILED       request failed after retries
  PARSE        response unusable: not the expected schema, or the identity does not match the bank
  STALE-ROUTE  valid response, but the issuer's newest filing at this route is older than
               ROUTE_LIVE_DAYS (or there is none) — the bank may not file here; nothing certified
  UNCOVERED    a PRIORITY bank with no route configured

Exit: 0 = every covered name read and nothing needs review · 1 = filing(s) need review
      (a 🔴/🟠 item or an UNPARSED filing) · 2 = INCOMPLETE — at least one name has NO VERDICT.
      An rc 2 run never prints an all-clear.

Repair 2026-10-09 (Will's bounded pass): OZK was queried at the SEC (CIK 1569650), where it has
filed nothing since 2017 — its "No 8-K" line was clean by construction. VLY was keyed to CIK
74260, which is OLD REPUBLIC INTERNATIONAL. FLG, AMTB, CFG and CUBI were not covered at all.
"""

import importlib.util
import json
import re
import sys
import time
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
OZK_FLNG = REPO / "AGENTS" / "OZK" / "scripts" / "flng_watch.py"   # the OZK desk's FDIC route, reused

# Will 2026-10-09 earnings-read priority banks. A name here with no TARGETS route = UNCOVERED.
PRIORITY = ("CFG", "CUBI", "EGBN", "FLG", "OZK", "AMTB", "WAL")

# CIKs verified against SEC company_tickers.json 2026-10-09. `match` must appear in the feed's
# <conformed-name>, so a wrong CIK reads as PARSE, never as a quiet bank.
TARGETS = {
    "CFG":  {"route": "sec", "cik": "759944",  "match": "CITIZENS FINANCIAL"},
    "CUBI": {"route": "sec", "cik": "1488813", "match": "CUSTOMERS BANCORP"},
    "EGBN": {"route": "sec", "cik": "1050441", "match": "EAGLE BANCORP"},
    "FLG":  {"route": "sec", "cik": "910073",  "match": "FLAGSTAR"},
    "OZK":  {"route": "fdic", "cert": 110,     "match": "Bank OZK"},
    "AMTB": {"route": "sec", "cik": "1734342", "match": "AMERANT"},
    "WAL":  {"route": "sec", "cik": "1212545", "match": "WESTERN ALLIANCE"},
    "ZION": {"route": "sec", "cik": "109380",  "match": "ZIONS"},
    "VLY":  {"route": "sec", "cik": "714310",  "match": "VALLEY NATIONAL"},
}

# Every listed bank files an earnings 8-K each quarter; no filing at a route for this long means
# the route is wrong or dead, not that the bank is quiet.
ROUTE_LIVE_DAYS = 120

ITEM_FLAGS = {
    "1.01": ("🔴", "Entry into Material Agreement"),
    "1.02": ("🔴", "Termination of Material Agreement"),
    "1.03": ("🟠", "Bankruptcy/Receivership"),
    "2.01": ("🟠", "Completion of Acquisition/Disposition"),
    "2.02": ("🔴", "Results of Operations (EARNINGS)"),
    "2.03": ("🟠", "Creation of Direct Financial Obligation"),
    "2.04": ("🔴", "Triggering Events / Default"),
    "2.05": ("🔴", "Costs of Exit/Restructuring"),
    "2.06": ("🔴", "Material Impairments"),
    "3.01": ("🟠", "Delisting/Transfer"),
    "3.03": ("🟠", "Material Modification of Rights"),
    "4.01": ("🟠", "Changes in Auditor"),
    "4.02": ("🔴", "Non-Reliance on Financial Statements"),
    "5.01": ("🟠", "Changes in Control"),
    "5.02": ("🔴", "Departure/Appointment of Officers"),
    "5.03": ("🟠", "Amendments to Articles/Bylaws"),
    "5.07": ("⚪", "Shareholder Vote"),
    "7.01": ("⚪", "Regulation FD Disclosure"),
    "8.01": ("⚪", "Other Events"),
    "9.01": ("⚪", "Financial Statements/Exhibits"),
}

SEC_HEADERS = {"User-Agent": "REGINALD-Research williepowen@gmail.com"}
NO_VERDICT = ("FAILED", "PARSE", "STALE-ROUTE", "UNCOVERED")


def fetch(url, headers, attempts=3, timeout=25):
    """Return (body, error). A failure is returned, never swallowed into 'no filings'."""
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=headers)
            return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace"), None
        except Exception as e:  # noqa: BLE001 — returned to the caller as FAILED
            last = e
            if i < attempts - 1:
                time.sleep(1.5 * (i + 1))
    return None, f"{type(last).__name__}: {last}"


def items_from_text(text):
    out = []
    for m in re.findall(r"(\d\.\d\d)", text or ""):
        if m not in out:
            out.append(m)
    return out


def grade_sec(text, info, days, today):
    """Pure verdict on an EDGAR atom feed -> (state, filings, message). No network."""
    if text is None:
        return "FAILED", [], "request failed"
    if "<feed" not in text or "<company-info>" not in text:
        return "PARSE", [], "response is not an EDGAR company atom feed"
    name_m = re.search(r"<conformed-name>([^<]+)</conformed-name>", text)
    name = name_m.group(1).strip() if name_m else ""
    if info["match"].upper() not in name.upper():
        return "PARSE", [], f"identity mismatch: CIK {info['cik']} is '{name or '?'}', expected '{info['match']}'"
    filings = []
    for entry in re.findall(r"<entry>(.*?)</entry>", text, re.DOTALL):
        d = re.search(r"<filing-date>([^<]+)</filing-date>", entry)
        if not d:
            return "PARSE", [], "an entry has no <filing-date>"
        href = re.search(r"<filing-href>([^<]+)</filing-href>", entry)
        form = re.search(r"<filing-type>([^<]+)</filing-type>", entry)
        desc = re.search(r"<items-desc>([^<]+)</items-desc>", entry)
        filings.append({"date": d.group(1), "form": form.group(1) if form else "8-K",
                        "href": href.group(1) if href else "",
                        "items": items_from_text(desc.group(1)) if desc else []})
    if not filings:
        return "STALE-ROUTE", [], f"'{name}' has NO 8-K at this route"
    newest = max(f["date"] for f in filings)
    if newest < (today - timedelta(days=ROUTE_LIVE_DAYS)).isoformat():
        return "STALE-ROUTE", [], f"newest 8-K at this route is {newest} (>{ROUTE_LIVE_DAYS}d) — wrong or dead route"
    cutoff = (today - timedelta(days=days)).isoformat()
    window = [f for f in filings if f["date"] >= cutoff]
    if not window:
        return "CLEAR", [], f"'{name}': no 8-K since {cutoff} (newest {newest}; route live)"
    return "FOUND", window, f"'{name}': {len(window)} 8-K(s) since {cutoff}"


def load_flng():
    spec = importlib.util.spec_from_file_location("ozk_flng_watch", OZK_FLNG)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def grade_fdic(rows, flng, days, today):
    """Pure verdict on an FDIC FLNG response, validated by the OZK desk's own evaluate()."""
    rc, msg, _ = flng.evaluate(rows, flng.BASELINE_ID)
    if rc == 2:
        return "PARSE", [], f"OZK desk validator: {msg}"
    dated = [(str(r.get("sysAddRecDttm") or "")[:10], r) for r in rows]
    if any(not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) for d, _ in dated):
        return "PARSE", [], "a filing row has no usable sysAddRecDttm date"
    newest = max(d for d, _ in dated)
    if newest < (today - timedelta(days=ROUTE_LIVE_DAYS)).isoformat():
        return "STALE-ROUTE", [], f"newest FDIC filing is {newest} (>{ROUTE_LIVE_DAYS}d)"
    cutoff = (today - timedelta(days=days)).isoformat()
    window = []
    for d, r in sorted(dated, key=lambda x: x[0]):
        if d >= cutoff:
            names = [a.get("instFlngAtchOrglNme", "?") for a in (r.get("instFlngAtchList") or [])]
            window.append({"date": d, "form": f"FLNG {r['instFlngId']}", "href": "",
                           "items": items_from_text(" ".join(names)), "attachments": names})
    if not window:
        return "CLEAR", [], f"FDIC FLNG cert 110: {len(rows)} filings, none since {cutoff} (newest {newest}). Filings only — FLNG does NOT carry OZK press releases"
    return "FOUND", window, f"FDIC FLNG cert 110: {len(window)} filing(s) since {cutoff}"


def summarize(results, priority=PRIORITY):
    """results: {ticker: (state, filings, msg)} -> (rc, lines). Pure."""
    lines = []
    for t in priority:
        if t not in results:
            results[t] = ("UNCOVERED", [], "no route configured for a priority bank")
    no_verdict = [t for t, (s, _, _) in results.items() if s in NO_VERDICT]
    review = []
    for t, (s, filings, _) in results.items():
        if s != "FOUND":
            continue
        for f in filings:
            sev = [ITEM_FLAGS.get(i, ("⚪", ""))[0] for i in f["items"]]
            if not f["items"] or "🔴" in sev or "🟠" in sev:
                review.append(t)
                break
    if no_verdict:
        lines.append(f"  ⚠️  INCOMPLETE — NO VERDICT for {len(no_verdict)} name(s): "
                     + ", ".join(f"{t} [{results[t][0]}]" for t in no_verdict)
                     + ". This run certifies nothing about them.")
    if review:
        lines.append(f"  🔴 REVIEW — filing(s) with a 🔴/🟠 item or UNPARSED items: {', '.join(sorted(set(review)))}")
    read = [t for t, (s, _, _) in results.items() if s in ("CLEAR", "FOUND")]
    if no_verdict:
        lines.append(f"  (read cleanly: {', '.join(read) if read else 'NONE'})")
        return 2, lines
    if review:
        return 1, lines
    lines.append(f"  ✅ All {len(results)} names read at their filing route; nothing needing review ({', '.join(read)}).")
    return 0, lines


def selftest():
    today = date(2026, 10, 9)

    def feed(name, dates, items="items 8.01 and 9.01"):
        e = "".join(f"<entry><filing-date>{d}</filing-date><filing-type>8-K</filing-type>"
                    f"<items-desc>{items}</items-desc></entry>" for d in dates)
        return f"<feed><company-info><conformed-name>{name}</conformed-name></company-info>{e}</feed>"

    wal = TARGETS["WAL"]
    vly = TARGETS["VLY"]

    class F:  # stand-in for the OZK desk module: same evaluate() contract
        BASELINE_ID = 11981
        @staticmethod
        def evaluate(rows, since):
            if not isinstance(rows, list) or len(rows) < 3:
                return 2, "UNKNOWN: incomplete", []
            return 0, "QUIET", []

    fd = [{"instFlngId": i, "sysAddRecDttm": "2026-08-05T10:00:00", "instFlngAtchList": []} for i in range(3)]
    cases = [
        ("sec: valid, route live, nothing in window -> CLEAR", grade_sec(feed("WESTERN ALLIANCE BANCORPORATION", ["2026-07-30"]), wal, 7, today)[0], "CLEAR"),
        ("sec: request failed -> FAILED", grade_sec(None, wal, 7, today)[0], "FAILED"),
        ("sec: HTML error page -> PARSE", grade_sec("<html>Too Many Requests</html>", wal, 7, today)[0], "PARSE"),
        ("sec: wrong company at CIK (old VLY key = Old Republic) -> PARSE", grade_sec(feed("OLD REPUBLIC INTERNATIONAL CORP", ["2026-07-23"]), vly, 7, today)[0], "PARSE"),
        ("sec: valid feed, zero 8-Ks -> STALE-ROUTE", grade_sec(feed("WESTERN ALLIANCE BANCORPORATION", []), wal, 7, today)[0], "STALE-ROUTE"),
        ("sec: newest 8-K 2017 (OZK-at-SEC shape) -> STALE-ROUTE", grade_sec(feed("WESTERN ALLIANCE BANCORPORATION", ["2017-06-01"]), wal, 7, today)[0], "STALE-ROUTE"),
        ("sec: 8-K in window -> FOUND", grade_sec(feed("WESTERN ALLIANCE BANCORPORATION", ["2026-10-08"]), wal, 7, today)[0], "FOUND"),
        ("fdic: validator rejects -> PARSE", grade_fdic([], F, 7, today)[0], "PARSE"),
        ("fdic: valid, nothing in window -> CLEAR", grade_fdic(fd, F, 7, today)[0], "CLEAR"),
        ("fdic: undated row -> PARSE", grade_fdic(fd + [{"instFlngId": 9}], F, 7, today)[0], "PARSE"),
    ]
    clear = ("CLEAR", [], "")
    found_unparsed = ("FOUND", [{"date": "2026-10-08", "form": "8-K", "href": "", "items": []}], "")
    found_quiet = ("FOUND", [{"date": "2026-10-08", "form": "8-K", "href": "", "items": ["8.01"]}], "")
    rc_cases = [
        ("summary: all CLEAR -> rc 0 with all-clear", summarize({t: clear for t in PRIORITY}), 0, True),
        ("summary: one FAILED -> rc 2, no all-clear", summarize({**{t: clear for t in PRIORITY}, "CFG": ("FAILED", [], "")}), 2, False),
        ("summary: priority bank missing -> UNCOVERED rc 2, no all-clear", summarize({t: clear for t in PRIORITY if t != "AMTB"}), 2, False),
        ("summary: STALE-ROUTE -> rc 2, no all-clear", summarize({**{t: clear for t in PRIORITY}, "OZK": ("STALE-ROUTE", [], "")}), 2, False),
        ("summary: FOUND with UNPARSED items -> rc 1, no all-clear", summarize({**{t: clear for t in PRIORITY}, "WAL": found_unparsed}), 1, False),
        ("summary: FOUND 8.01 only -> rc 0", summarize({**{t: clear for t in PRIORITY}, "WAL": found_quiet}), 0, True),
    ]
    fails = 0
    for name, got, want in cases:
        ok = got == want
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {got:<11} (want {want})  {name}")
    for name, (rc, lines), want_rc, want_clear in rc_cases:
        has_clear = any("✅" in ln for ln in lines)
        ok = rc == want_rc and has_clear == want_clear
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  rc {rc} all-clear={has_clear}  (want rc {want_rc}, {want_clear})  {name}")
    n = len(cases) + len(rc_cases)
    print(f"8K-MONITOR SELFTEST {'PASS' if not fails else 'FAIL'}: {n - fails}/{n}")
    return 1 if fails else 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    days = 7
    if "--days" in sys.argv:
        days = int(sys.argv[sys.argv.index("--days") + 1])
    today = datetime.now().date()

    print(f"\n{'='*70}")
    print(f"  REGINALD 8-K Monitor — {datetime.now():%Y-%m-%d %H:%M} (last {days} days)")
    print(f"{'='*70}")

    results = {}
    flng = None
    for ticker, info in TARGETS.items():
        if info["route"] == "sec":
            url = (f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={info['cik']}"
                   f"&type=8-K&dateb=&owner=exclude&count=20&output=atom")
            text, err = fetch(url, SEC_HEADERS)
            state, filings, msg = grade_sec(text, info, days, today)
            if err:
                msg = f"{msg}: {err}"
            route = f"SEC CIK {info['cik']}"
            time.sleep(0.15)
        else:
            route = f"FDIC FLNG cert {info['cert']} (OZK desk flng_watch)"
            try:
                flng = flng or load_flng()
                body, err = fetch(flng.API, {"User-Agent": flng.UA})
                if body is None:
                    state, filings, msg = "FAILED", [], f"request failed: {err}"
                else:
                    try:
                        rows = json.loads(body)
                    except ValueError:
                        rows = None
                    state, filings, msg = grade_fdic(rows, flng, days, today)
            except Exception as e:  # noqa: BLE001 — the reused route itself is unavailable
                state, filings, msg = "FAILED", [], f"OZK desk route unavailable ({type(e).__name__}: {e})"
        results[ticker] = (state, filings, msg)
        icon = {"CLEAR": "✅", "FOUND": "📄"}.get(state, "⚠️ ")
        print(f"\n  {ticker} — {route}")
        print(f"  {icon} {state}: {msg}")
        for f in filings:
            if f["items"]:
                flags = [ITEM_FLAGS.get(i, ("⚪", f"Item {i}")) for i in f["items"]]
                print(f"     {f['date']}  {f['form']}  " + " · ".join(f"{fl[0]} {i} {fl[1]}" for i, fl in zip(f["items"], flags)))
            else:
                print(f"     {f['date']}  {f['form']}  ⚠️ items UNPARSED — severity unknown, read it")
            for a in f.get("attachments", []):
                print(f"         {a}")

    rc, lines = summarize(results)
    print()
    for ln in lines:
        print(ln)
    print()
    return rc


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # a crash must not exit 0 or collide with rc 1 REVIEW
        print(f"8K-MONITOR 2 INCOMPLETE: internal error ({type(e).__name__}: {e}) — no verdict")
        sys.exit(2)
