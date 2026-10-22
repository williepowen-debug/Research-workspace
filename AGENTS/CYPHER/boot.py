#!/usr/bin/env python3
"""
boot.py — CYPHER boot instrument. Wall clock + ledger staleness + predictions-due
+ catalysts-due + escalation watch + incident re-checks + CISA KEV + SEC 8-K Item 1.05,
one verdict.

Built by DAEDALUS 2026-10-22 (CYPHER build; pattern = GIBBS boot.py 2026-10-14).
cwd-proof + self-locating: AGENTS/CYPHER/boot.py -> parents[2] == repo root. Pure stdlib.

Legs:
  1. ledger staleness — workbook/*.tsv AND TRADE.md (shared script; verdict = rc OR marker).
  2. predictions-due  — workbook/PREDICTIONS.tsv OPEN rows past Resolve_By.
  3. catalysts-due    — docket/CATALYSTS.tsv rows dated TODAY, within WINDOW_DAYS, or past.
  4. escalation watch — workbook/ESCALATION_WATCH.tsv: state tokens valid (Class 2); every
     non-terminal row re-checked within WATCH_STALE_DAYS.
  5. incidents        — workbook/INCIDENTS.tsv: enums valid; REPORTED / ATTEMPTS-ONLY rows
     re-checked within INCIDENT_RECHECK_DAYS.
  6. CISA KEV         — every KEV:<CVE> key on a live row, checked against the KEV catalog.
     A listing is a FIRED CANDIDATE: the machine flags, the OWNER sets State.
  7. SEC 8-K Item 1.05 — EDGAR full-text search over CONTROL_DAYS; the population is its own
     positive control (0 hits = the query is broken, never "quiet"); filings dated inside
     LOOKBACK_DAYS are listed for the owner to read.

Combined exit (CHECK_STANDARD §9): 0 quiet · 1 REVIEW · 2 a leg FAILED / cannot certify.
Flags: --offline skips legs 6-7 and says so (rc 1 — a skipped control is reported, never a pass).
Drill hooks (never set in a real boot; the header says when they are set):
  CYPHER_BOOT_TODAY=YYYY-MM-DD  evaluate date legs as of that day
  CYPHER_KEV_FILE=<json>        read the KEV catalog from a file instead of cisa.gov
  CYPHER_EDGAR_FILE=<json>      read the EDGAR search response from a file instead of efts.sec.gov
"""

import csv
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STALENESS = ROOT / "scripts" / "ledger_staleness.py"
PREDICTIONS = HERE / "workbook" / "PREDICTIONS.tsv"
CATALYSTS = HERE / "docket" / "CATALYSTS.tsv"
WATCH = HERE / "workbook" / "ESCALATION_WATCH.tsv"
INCIDENTS = HERE / "workbook" / "INCIDENTS.tsv"

WINDOW_DAYS = 2              # same horizon as PROME's summons check
WATCH_STALE_DAYS = 7         # charter § ESCALATION WATCH: every open row re-checked within 7 days
INCIDENT_RECHECK_DAYS = 14
KEV_STALE_DAYS = 10          # KEV normally updates several times a week
LOOKBACK_DAYS = 7
CONTROL_DAYS = 120           # build check: 18 Item 1.05 8-Ks in 2026-07-01..10-22
KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
EDGAR_URL = "https://efts.sec.gov/LATEST/search-index"
USER_AGENT = "CYPHER-Research williepowen@gmail.com"   # SEC requires a contact; fleet form (REGINALD)
TIMEOUT = 25

WATCH_STATES = {"ARMED", "NOT-FIRED", "FIRED", "STOOD-DOWN", "UNOBSERVABLE", "CANNOT-FIRE"}
WATCH_TERMINAL = {"FIRED", "STOOD-DOWN"}            # no re-check clock, no KEV watch
WATCH_NO_CLOCK = WATCH_TERMINAL | {"UNOBSERVABLE", "CANNOT-FIRE"}
CLASSES = {"VULN-WIDESPREAD", "SUPPLY-CHAIN", "RANSOMWARE-EXTORTION", "DATA-THEFT", "OT-PHYSICAL",
           "INFRA-OUTAGE", "CA-TRUST", "STATE-CAMPAIGN", "INFO-INTEGRITY", "UNCLASSIFIED"}
EVENT_STATES = {"CONFIRMED", "ATTEMPTS-ONLY", "DISCLOSED", "REPORTED", "FALSE", "SUPERSEDED"}
EVENT_DEAD = {"FALSE", "SUPERSEDED"}
RECHECK_STATES = {"REPORTED", "ATTEMPTS-ONLY"}
BASES = {"PRIMARY-VERIFIED", "ARTIFACT-VERIFIED", "SECONDARY-SOURCE", "OWNER-ASSERTED", "UNANCHORED"}
CVE_RE = re.compile(r"^CVE-\d{4}-\d{4,}$")

_DRILL = os.environ.get("CYPHER_BOOT_TODAY")
TODAY = date.fromisoformat(_DRILL) if _DRILL else date.today()
OFFLINE = "--offline" in sys.argv[1:]


def run_alert(cmd):
    """Shared ledger_staleness runner (CHECK_STANDARD §8/§9): 0 quiet · 1 REVIEW · 2 failure."""
    try:
        p = subprocess.run([sys.executable, *cmd], cwd=str(ROOT), capture_output=True, text=True)
    except Exception as e:  # noqa: BLE001
        print(f"  boot.py: FAILED to launch {cmd[0]}: {e}", file=sys.stderr)
        return 2
    out, err = (p.stdout or "").strip(), (p.stderr or "").strip()
    if out:
        print(out)
    if err:
        print(err, file=sys.stderr)
    if p.returncode not in (0, 1):
        return 2
    return 1 if (p.returncode == 1 or "⚠️" in out or "🔴" in out) else 0


def _rows(path, skip_comments=True):
    with path.open(encoding="utf-8") as f:
        lines = [ln for ln in f if not (skip_comments and ln.startswith("#"))]
    return list(csv.DictReader(lines, delimiter="\t"))


def _missing(label, path):
    try:
        shown = path.relative_to(HERE)
    except ValueError:          # a drill or a moved file: never let the failure path itself crash
        shown = path
    return 2, [f"  🔴 {label}: {shown} MISSING — the register this leg certifies does not "
               f"exist; enforcement is silently absent, do NOT read this as quiet"]


def _load(label, path):
    """(rows, None) or (None, (rc, lines)) — one failure shape for every ledger leg."""
    if not path.exists():
        return None, _missing(label, path)
    try:
        return _rows(path), None
    except Exception as e:  # noqa: BLE001
        return None, (2, [f"  🔴 {label}: read error {type(e).__name__}: {e}"])


def _date(raw):
    try:
        return datetime.strptime((raw or "").strip()[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def _token(cell):
    return (cell or "").strip().upper().split(" ")[0]


def predictions_due():
    rows, fail = _load("predictions", PREDICTIONS)
    if fail:
        return fail
    due, unparsed, open_n = [], 0, 0
    for r in rows:
        if _token(r.get("Status")) != "OPEN":
            continue
        open_n += 1
        when = _date(r.get("Resolve_By"))
        if when is None:
            unparsed += 1
            continue
        if when <= TODAY:
            due.append(f"  ⚠️ DUE: {(r.get('ID') or '?').strip()} [{r.get('Resolve_By')}] {(r.get('Prediction') or '').strip()[:70]}")
    if unparsed:
        due.append(f"  ⚠️ {unparsed} OPEN row(s) with an unparsable Resolve_By — cannot tell if due; fix the date")
    if due:
        return 1, due + [f"  ({len(rows)} row(s), {open_n} OPEN scanned on Resolve_By)"]
    return 0, [f"  ✓ none due — {len(rows)} row(s), {open_n} OPEN scanned on Resolve_By"]


def catalysts_due():
    if not CATALYSTS.exists():
        return _missing("catalysts", CATALYSTS)
    try:
        rows = _rows(CATALYSTS, skip_comments=False)   # PROME's summons reader takes line 1 as the header
    except Exception as e:  # noqa: BLE001
        return 2, [f"  🔴 catalysts: read error {type(e).__name__}: {e}"]
    if rows and "date" not in rows[0]:
        return 2, ["  🔴 catalysts: CATALYSTS.tsv line 1 is not the `date…` header — PROME's summons reader would misparse it"]
    horizon = TODAY + timedelta(days=WINDOW_DAYS)
    window, past, unparsed, forward = [], [], 0, 0
    for r in rows:
        when = _date(r.get("date"))
        if when is None:
            unparsed += 1
            continue
        if when >= TODAY:
            forward += 1
        line = f"{r.get('date')} [{(r.get('priority') or '?').strip()}] {(r.get('event') or '').strip()[:60]}"
        if when < TODAY:
            past.append((when, line))
        elif when <= horizon:
            window.append(f"  ⚠️ {'TODAY' if when == TODAY else f'in {(when - TODAY).days}d'}: {line}")
    out = list(window)
    if past:
        past.sort()
        out.append(f"  ⚠️ {len(past)} past-dated row(s) (oldest {past[0][0]}) — owner prunes or re-dates: "
                   + " · ".join(l for _, l in past[:3]) + (" …" if len(past) > 3 else ""))
    if forward == 0:
        out.append("  ⚠️ EMPTY-FORWARD: no row dated today or later — nothing can summon this desk")
    if unparsed:
        out.append(f"  ⚠️ {unparsed} row(s) with no parseable date — not scanned")
    if out:
        return 1, out + [f"  ({len(rows)} row(s) scanned; window {WINDOW_DAYS}d)"]
    return 0, [f"  ✓ none due — {len(rows)} row(s) scanned, {forward} forward, none inside {WINDOW_DAYS}d"]


def escalation_watch():
    rows, fail = _load("escalation watch", WATCH)
    if fail:
        return fail
    if not rows:
        return 1, ["  ⚠️ 0 watch rows — nothing is being watched. If a wave is open this is a defect (PAT-155)"]
    out, waves = [], {}
    for r in rows:
        wid, row = (r.get("Wave_ID") or "?").strip(), (r.get("Row") or "?").strip()
        tok = _token(r.get("State"))
        waves.setdefault(wid, {}).setdefault(tok, 0)
        waves[wid][tok] += 1
        if tok not in WATCH_STATES:
            out.append(f"  ⚠️ {wid} row {row}: State '{(r.get('State') or '').strip()[:30]}' is not a Class 2 token — fix it")
            continue
        if tok in WATCH_NO_CLOCK:
            continue
        when = _date(r.get("State_As_Of"))
        if when is None:
            out.append(f"  ⚠️ {wid} row {row}: unparsable State_As_Of — cannot tell when it was last checked")
        elif (TODAY - when).days > WATCH_STALE_DAYS:
            out.append(f"  ⚠️ RE-CHECK DUE: {wid} row {row} ({tok}, as of {when}, {(TODAY - when).days}d) — "
                       f"{(r.get('Sign') or '').strip()[:60]}")
    summary = []
    for wid, counts in waves.items():
        open_ = any(t not in ("STOOD-DOWN",) for t in counts)
        summary.append(f"  {'◉' if open_ else '○'} {wid}: " + " · ".join(f"{t} {n}" for t, n in sorted(counts.items()))
                       + ("" if open_ else " (closed)"))
        if counts.get("FIRED"):
            summary.append(f"  ℹ️ {wid}: {counts['FIRED']} FIRED row(s) — each needs its consequence-owner packet (row Notes)")
    if out:
        return 1, out + summary
    return 0, [f"  ✓ every open row checked within {WATCH_STALE_DAYS}d — {len(rows)} row(s)"] + summary


def incidents():
    rows, fail = _load("incidents", INCIDENTS)
    if fail:
        return fail
    if not rows:
        return 1, ["  ⚠️ 0 incident rows — an empty ledger certifies nothing (PAT-155)"]
    out, stale = [], []
    for r in rows:
        iid = (r.get("ID") or "?").strip()
        for col, allowed in (("Class", CLASSES), ("Event_State", EVENT_STATES), ("Basis", BASES)):
            if _token(r.get(col)) not in allowed:
                out.append(f"  ⚠️ {iid}: {col} '{(r.get(col) or '').strip()[:30]}' is not in the declared enum")
        if _token(r.get("Event_State")) in RECHECK_STATES:
            when = _date(r.get("Last_Checked"))
            if when is None:
                out.append(f"  ⚠️ {iid}: unparsable Last_Checked — cannot tell when it was last checked")
            elif (TODAY - when).days > INCIDENT_RECHECK_DAYS:
                stale.append((when, f"{iid} ({_token(r.get('Event_State'))}, {when})"))
    if stale:
        stale.sort()
        out.append(f"  ⚠️ RE-CHECK DUE: {len(stale)} REPORTED/ATTEMPTS-ONLY row(s) last checked >{INCIDENT_RECHECK_DAYS}d ago: "
                   + " · ".join(s for _, s in stale[:5]) + (" …" if len(stale) > 5 else ""))
    if out:
        return 1, out + [f"  ({len(rows)} incident row(s) scanned)"]
    return 0, [f"  ✓ enums valid; no REPORTED/ATTEMPTS-ONLY row older than {INCIDENT_RECHECK_DAYS}d — {len(rows)} row(s)"]


def _kev_keys():
    """{CVE: [row labels]} from live rows of both ledgers, plus malformed-key lines."""
    keys, bad = {}, []
    for path, idcol, statecol, dead in ((WATCH, "Row", "State", WATCH_TERMINAL),
                                        (INCIDENTS, "ID", "Event_State", EVENT_DEAD)):
        if not path.exists():
            continue
        for r in _rows(path):
            if _token(r.get(statecol)) in dead:
                continue
            label = (f"{(r.get('Wave_ID') or '').strip()} row {(r.get(idcol) or '?').strip()}"
                     if path == WATCH else (r.get(idcol) or "?").strip())
            raw = (r.get("Watch_Keys") or "").strip()
            for part in filter(None, (p.strip() for p in raw.split(";"))):
                if not part.upper().startswith("KEV:"):
                    continue
                for cve in filter(None, (c.strip().upper() for c in part[4:].split(","))):
                    if CVE_RE.match(cve):
                        keys.setdefault(cve, []).append(label)
                    else:
                        bad.append(f"  ⚠️ {label}: malformed KEV key '{cve}' — not checked")
    return keys, bad


def _fetch_json(url, env_var, params=None):
    """(obj, source_label) — raises on any failure; the caller turns that into rc 2."""
    path = os.environ.get(env_var)
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8")), f"DRILL FILE {path}"
    full = url + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(full, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8")), "LIVE " + url


def kev():
    try:
        keys, bad = _kev_keys()
    except Exception as e:  # noqa: BLE001
        return 2, [f"  🔴 KEV: could not read Watch_Keys ({type(e).__name__}: {e}) — cannot certify"]
    if not keys:
        return (1 if bad else 0), bad + ["  ✓ 0 KEV keys on live rows — nothing to check (say so, never imply a check ran)"]
    if OFFLINE:
        return 1, bad + [f"  ⚠️ NOT RUN (--offline): {len(keys)} KEV key(s) unchecked — a skipped control is not a pass"]
    try:
        cat, src = _fetch_json(KEV_URL, "CYPHER_KEV_FILE")
        vulns = cat["vulnerabilities"]
        if not isinstance(vulns, list) or not vulns:
            raise ValueError("catalog has 0 vulnerabilities")
    except Exception as e:  # noqa: BLE001
        return 2, bad + [f"  🔴 KEV: fetch/parse FAILED ({type(e).__name__}: {e}) — cannot certify; "
                         f"do NOT read as 'not listed'. Check {KEV_URL} by hand"]
    listed = {(v.get("cveID") or "").strip().upper(): v for v in vulns}
    out = list(bad)
    for cve, labels in sorted(keys.items()):
        if cve in listed:
            out.append(f"  ⚠️ KEV LISTED: {cve} (dateAdded {listed[cve].get('dateAdded')}) — rows: {', '.join(labels)}. "
                       f"FIRED CANDIDATE: the owner sets State and sends the P1 packet; the machine never writes")
    released = _date(cat.get("dateReleased"))
    if released is None:
        out.append("  ⚠️ KEV catalog dateReleased unparsable — catalog freshness unknown")
    elif (TODAY - released).days > KEV_STALE_DAYS:
        out.append(f"  ⚠️ KEV catalog released {released} ({(TODAY - released).days}d) — the feed itself may be stale")
    tail = f"  ({len(keys)} key(s) vs KEV v{cat.get('catalogVersion')} released {cat.get('dateReleased')}, {len(vulns)} entries; source {src})"
    if out:
        return 1, out + [tail]
    return 0, [f"  ✓ {len(keys)} watched CVE(s) absent from KEV: {', '.join(sorted(keys))}", tail]


def edgar_105():
    if OFFLINE:
        return 1, ["  ⚠️ NOT RUN (--offline): 8-K Item 1.05 sweep unchecked — a skipped control is not a pass"]
    start = TODAY - timedelta(days=CONTROL_DAYS)
    params = {"q": '"Item 1.05"', "forms": "8-K", "dateRange": "custom",
              "startdt": start.isoformat(), "enddt": TODAY.isoformat()}
    try:
        d, src = _fetch_json(EDGAR_URL, "CYPHER_EDGAR_FILE", params)
        total = int(d["hits"]["total"]["value"])
        hits = d["hits"]["hits"]
    except Exception as e:  # noqa: BLE001
        return 2, [f"  🔴 8-K Item 1.05: fetch/parse FAILED ({type(e).__name__}: {e}) — cannot certify; "
                   f"do NOT read as 'no filings'"]
    if total == 0:
        return 2, [f"  🔴 8-K Item 1.05: 0 filings in {CONTROL_DAYS}d — the positive-control population is empty, so the "
                   f"QUERY is likely broken (build check found 18 in 2026-07-01..10-22). Do NOT read as quiet"]
    recent_from = TODAY - timedelta(days=LOOKBACK_DAYS)
    recent, seen = [], set()
    for h in hits:
        s = h.get("_source") or {}
        when = _date(s.get("file_date"))
        name = ((s.get("display_names") or ["?"])[0] or "?")[:70]
        key = (s.get("file_date"), name)
        if when and when >= recent_from and key not in seen:
            seen.add(key)
            recent.append(f"  ⚠️ 8-K Item 1.05 {s.get('file_date')}: {name} — read it: bank, core/digital vendor, or a wave CVE?")
    out = sorted(recent, reverse=True)
    if total > len(hits):
        out.append(f"  ⚠️ {total} filings but only {len(hits)} returned — the recent list may be incomplete")
    tail = f"  ({total} Item 1.05 8-K(s) in {start}..{TODAY}; listing filings since {recent_from}; source {src})"
    if out:
        return 1, out + [tail]
    return 0, [f"  ✓ no Item 1.05 8-K filed since {recent_from}; control population {total} in {CONTROL_DAYS}d", tail]


def main():
    print("=" * 74)
    print(f"  ⏰ WALL CLOCK: {datetime.now().strftime('%Y-%m-%d %H:%M %A')} — never hand-write a time; copy this line")
    if _DRILL:
        print(f"  🧪 DRILL CLOCK: date legs evaluate as of {TODAY} (CYPHER_BOOT_TODAY) — NOT a real boot")
    for v in ("CYPHER_KEV_FILE", "CYPHER_EDGAR_FILE"):
        if os.environ.get(v):
            print(f"  🧪 DRILL FILE: {v}={os.environ[v]} — NOT a real boot")
    print("  CYPHER BOOT — staleness · predictions · catalysts · escalation watch · incidents · KEV · 8-K 1.05")
    print("=" * 74)
    rcs = []
    print("\n--- 1. ledger staleness (workbook + TRADE.md) ---")
    sw = run_alert([str(STALENESS), "CYPHER", "--quiet"])
    st = run_alert([str(STALENESS), "CYPHER", "--trade", "--quiet"])
    if sw == st == 0:
        print("  ✓ quiet (alert-contract: this check prints only when stale or misconfigured)")
    rcs.append(2 if 2 in (sw, st) else (1 if 1 in (sw, st) else 0))
    for title, fn in (("2. predictions-due (OPEN rows past Resolve_By)", predictions_due),
                      ("3. catalysts-due (docket/CATALYSTS.tsv: today · ≤2d · past)", catalysts_due),
                      ("4. escalation watch (Class 2 tokens · 7-day re-check)", escalation_watch),
                      ("5. incidents (enums · 14-day re-check of unconfirmed rows)", incidents),
                      ("6. CISA KEV (watched CVEs on live rows)", kev),
                      ("7. SEC 8-K Item 1.05 (material cyber incidents)", edgar_105)):
        print(f"\n--- {title} ---")
        rc, lines = fn()
        print("\n".join(lines))
        rcs.append(rc)
    print("\n" + "=" * 74)
    if 2 in rcs:
        print("  CYPHER boot: a leg FAILED — check manually, do NOT assume quiet.")
        return 2
    if 1 in rcs:
        print("  CYPHER boot: REVIEW — work the flagged items before new research.")
        return 1
    print("  CYPHER boot: all quiet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
