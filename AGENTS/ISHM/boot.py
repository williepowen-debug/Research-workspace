#!/usr/bin/env python3
"""
boot.py — ISHM boot instrument. Wall clock + ledger staleness + predictions-due + catalysts-due
+ missed prints + print-ledger hygiene + frozen perimeter + matrix/map + FRED hard data, one verdict.

Built by DAEDALUS 2026-10-23 (ISHM build; pattern = CYPHER boot.py 2026-10-22).
cwd-proof + self-locating: AGENTS/ISHM/boot.py -> parents[2] == repo root. Pure stdlib.

Legs:
  1. ledger staleness — workbook/*.tsv AND TRADE.md (shared script; verdict = rc OR marker).
  2. predictions-due  — workbook/PREDICTIONS.tsv OPEN rows past Resolve_By.
  3. catalysts-due    — docket/CATALYSTS.tsv rows dated TODAY, within WINDOW_DAYS, or past;
     EMPTY-FORWARD if nothing is dated today or later; THIN-FORWARD if the last row is < FORWARD_DAYS out.
  4. missed prints    — every PAST catalyst whose event cell starts with a [SERIES-KEY] must have a
     PRINTS.tsv row for that Series with Release_Date >= the catalyst date (blueprint §7
     scheduled-release freshness check). A catalyst with no key is reported, never silently skipped.
  5. print ledger     — workbook/PRINTS.tsv enums (Series key · Vintage · SA · Basis); a FLASH /
     ADVANCE row whose Successor_Date has passed with no later-vintage row for the same
     Series + Ref_Period is flagged.
  6. perimeter        — PERIMETER.tsv carries the FROZEN banner and EXACTLY the eight ruled tickers.
  7. matrix + map     — workbook/VX.tsv scores 1-5 or UNKNOWN (UNKNOWN = scoring owed, REVIEW);
     Kind MECHANISM/THERMOMETER; composite = MECHANISM rows only. FLOW states valid, every row
     keyed to an existing VX vector.
  8. FRED hard data   — keyless fredgraph.csv per FRED_SERIES. Positive control: >= MIN_OBS
     observations and a newest observation within FRED_STALE_DAYS (0 rows or HTML = the route is
     broken, never "quiet"). FRED's newest observation newer than the ledger's newest Ref_Period for
     that key = a print not yet read (REVIEW).

Combined exit (CHECK_STANDARD §9): 0 quiet · 1 REVIEW · 2 a leg FAILED / cannot certify.
Flags: --offline skips leg 8 and says so (rc 1 — a skipped control is reported, never a pass).
Tests: AGENTS/ISHM/scripts/test_boot.py (throwaway copies; real files md5-checked unchanged).
Drill hooks (never set in a real boot; the header says when they are set):
  ISHM_BOOT_TODAY=YYYY-MM-DD  evaluate date legs as of that day
  ISHM_HOME=<dir>             read the desk's ledgers from a copy of AGENTS/ISHM/
  ISHM_FRED_DIR=<dir>         read <dir>/<FRED_ID>.csv instead of fred.stlouisfed.org
"""

import csv
import os
import re
import subprocess
import sys
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(os.environ.get("ISHM_HOME") or Path(__file__).resolve().parent)
STALENESS = ROOT / "scripts" / "ledger_staleness.py"
PREDICTIONS = HERE / "workbook" / "PREDICTIONS.tsv"
CATALYSTS = HERE / "docket" / "CATALYSTS.tsv"
PRINTS = HERE / "workbook" / "PRINTS.tsv"
PERIMETER = HERE / "PERIMETER.tsv"
VX = HERE / "workbook" / "VX.tsv"
FLOW = HERE / "workbook" / "FLOW.tsv"

WINDOW_DAYS = 2              # same horizon as PROME's summons check
FORWARD_DAYS = 30            # charter § WAKE TRIGGERS: keep the calendar >= 30 days forward
FRED_STALE_DAYS = 120        # monthly series: newest observation older than this = route or series broken
MIN_OBS = 24
TIMEOUT = 25
USER_AGENT = "ISHM-Research williepowen@gmail.com"
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
# ledger key -> FRED id (verified keyless at build 2026-10-23 09:4x ET: newest obs INDPRO/TCU/IPMAN 2026-09-01,
# DGORDER/NEWORDER/ANXAVS/AMTMNO 2026-08-01; the old ISM id NAPM returns an HTML page, not data)
FRED_SERIES = {"IP": "INDPRO", "IP-MFG": "IPMAN", "TCU": "TCU", "DGORDER": "DGORDER",
               "NEWORDER": "NEWORDER", "ANDENO-SHIP": "ANXAVS", "AMTMNO": "AMTMNO"}

PERIMETER_TICKERS = {"CAT", "DE", "HON", "GE", "PH", "MMM", "EMR", "UNP"}   # WQ-506 ④, frozen
SERIES_KEYS = {"ISM-MFG", "ISM-MFG-NO", "ISM-MFG-PROD", "ISM-MFG-INV", "ISM-MFG-PRICES", "SPG-PMI-MFG",
               "EMPIRE", "PHILLY", "RICHMOND", "KCFED", "DALLAS", "IP", "IP-MFG", "TCU", "DGORDER",
               "NEWORDER", "ANDENO-SHIP", "AMTMNO", "CASS-SHIP", "CASS-EXP", "AAR-CARLOADS",
               "AAR-INTERMODAL", "CLASS8-ORDERS", "AIR-CARGO", "EARNINGS", "GDP-EQUIP", "TRADE-COMPUTERS",
               "ATA-TONNAGE", "AMT-USMTO", "AMT-CUTTING", "ACT-TRAILERS", "AAR-BREADTH", "BEIGE-MFG"}
VINTAGE_FIXED = {"FLASH", "ADVANCE", "FIRST-PUBLISHED", "FINAL"}
VINTAGE_PROVISIONAL = {"FLASH", "ADVANCE"}
SA_VALUES = {"SA", "NSA"}
BASES = {"PRIMARY-VERIFIED", "ARTIFACT-VERIFIED", "SECONDARY-SOURCE", "OWNER-ASSERTED", "UNANCHORED"}
VX_KINDS = {"MECHANISM", "THERMOMETER"}
FLOW_STATES = {"CONFIRMED", "NOT-OBSERVED", "MODELED", "UNTESTED"}
KEY_RE = re.compile(r"^\[([A-Z0-9-]+)\]")

_DRILL = os.environ.get("ISHM_BOOT_TODAY")
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
    except ValueError:
        shown = path
    return 2, [f"  🔴 {label}: {shown} MISSING — the register this leg certifies does not "
               f"exist; enforcement is silently absent, do NOT read this as quiet"]


def _load(label, path, skip_comments=True):
    """(rows, None) or (None, (rc, lines)) — one failure shape for every ledger leg."""
    if not path.exists():
        return None, _missing(label, path)
    try:
        return _rows(path, skip_comments), None
    except Exception as e:  # noqa: BLE001
        return None, (2, [f"  🔴 {label}: read error {type(e).__name__}: {e}"])


def _date(raw):
    try:
        return datetime.strptime((raw or "").strip()[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def _period(raw):
    """'2026-09' or '2026-09-01' -> date(2026, 9, 1); weekly '2026-W42' -> None (not FRED-comparable)."""
    s = (raw or "").strip()
    try:
        return datetime.strptime(s[:7], "%Y-%m").date()
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


def _catalysts():
    rows, fail = _load("catalysts", CATALYSTS, skip_comments=False)  # PROME's reader takes line 1 as header
    if fail:
        return None, fail
    if rows and "date" not in rows[0]:
        return None, (2, ["  🔴 catalysts: CATALYSTS.tsv line 1 is not the `date…` header — PROME's summons reader would misparse it"])
    return rows, None


def catalysts_due():
    rows, fail = _catalysts()
    if fail:
        return fail
    horizon = TODAY + timedelta(days=WINDOW_DAYS)
    window, past, unparsed, last = [], [], 0, None
    for r in rows:
        when = _date(r.get("date"))
        if when is None:
            unparsed += 1
            continue
        last = when if last is None or when > last else last
        line = f"{r.get('date')} [{(r.get('priority') or '?').strip()}] {(r.get('event') or '').strip()[:64]}"
        if when < TODAY:
            past.append((when, line))
        elif when <= horizon:
            window.append(f"  ⚠️ {'TODAY' if when == TODAY else f'in {(when - TODAY).days}d'}: {line}")
    out = list(window)
    if past:
        past.sort()
        out.append(f"  ⚠️ {len(past)} past-dated row(s) (oldest {past[0][0]}) — consume, then re-date to the next release or retire: "
                   + " · ".join(l for _, l in past[:3]) + (" …" if len(past) > 3 else ""))
    if last is None or last < TODAY:
        out.append("  ⚠️ EMPTY-FORWARD: no row dated today or later — nothing can summon this desk")
    elif (last - TODAY).days < FORWARD_DAYS:
        out.append(f"  ⚠️ THIN-FORWARD: last row {last} is {(last - TODAY).days}d out (< {FORWARD_DAYS}d) — extend the calendar")
    if unparsed:
        out.append(f"  ⚠️ {unparsed} row(s) with no parseable date — not scanned")
    if out:
        return 1, out + [f"  ({len(rows)} row(s) scanned; window {WINDOW_DAYS}d; forward horizon {FORWARD_DAYS}d)"]
    return 0, [f"  ✓ none due — {len(rows)} row(s), last row {last} ({(last - TODAY).days}d out), none inside {WINDOW_DAYS}d"]


def missed_prints():
    cats, fail = _catalysts()
    if fail:
        return fail
    prints, fail = _load("print ledger", PRINTS)
    if fail:
        return fail
    seen = {}
    for p in prints:
        k, d = (p.get("Series") or "").strip(), _date(p.get("Release_Date"))
        if k and d and (k not in seen or d > seen[k]):
            seen[k] = d
    out, checked, unkeyed = [], 0, 0
    for r in cats:
        when = _date(r.get("date"))
        if when is None or when >= TODAY:
            continue
        m = KEY_RE.match((r.get("event") or "").strip())
        if not m:
            unkeyed += 1
            continue
        checked += 1
        key = m.group(1)
        if key not in SERIES_KEYS:
            out.append(f"  ⚠️ {r.get('date')}: catalyst key [{key}] is not a declared SERIES-KEY — cannot be matched")
        elif key not in seen or seen[key] < when:
            out.append(f"  ⚠️ MISSED PRINT: [{key}] released {when} — no PRINTS.tsv row with Release_Date >= {when}"
                       + (f" (newest on file {seen[key]})" if key in seen else " (none on file)"))
    if unkeyed:
        out.append(f"  ℹ️ {unkeyed} past catalyst(s) carry no [SERIES-KEY] — not print-checkable (fine for non-print rows; say so in notes)")
    tail = f"  ({checked} past keyed catalyst(s) checked against {len(prints)} print row(s))"
    if any(l.startswith("  ⚠️") for l in out):
        return 1, out + [tail]
    return 0, [f"  ✓ every past keyed catalyst has its print on file" if checked else
               "  ✓ 0 past keyed catalysts — nothing to check yet (say so, never imply a check ran)"] + out + [tail]


def print_ledger():
    rows, fail = _load("print ledger", PRINTS)
    if fail:
        return fail
    if not rows:
        return 1, ["  ⚠️ 0 print rows — the desk has read no print (expected only before the first session; PAT-155)"]
    out = []
    later = {}
    for r in rows:
        later.setdefault(((r.get("Series") or "").strip(), (r.get("Ref_Period") or "").strip()), []).append(
            _token(r.get("Vintage")))
    for i, r in enumerate(rows, 1):
        label = f"{(r.get('Series') or '?').strip()} {(r.get('Ref_Period') or '?').strip()}"
        if (r.get("Series") or "").strip() not in SERIES_KEYS:
            out.append(f"  ⚠️ row {i} {label}: Series not a declared SERIES-KEY")
        vint = _token(r.get("Vintage"))
        if vint not in VINTAGE_FIXED and not vint.startswith("REVISED-"):
            out.append(f"  ⚠️ row {i} {label}: Vintage '{(r.get('Vintage') or '').strip()[:20]}' not in the declared enum")
        if _token(r.get("SA")) not in SA_VALUES:
            out.append(f"  ⚠️ row {i} {label}: SA must be SA or NSA")
        if _token(r.get("Basis")) not in BASES:
            out.append(f"  ⚠️ row {i} {label}: Basis '{(r.get('Basis') or '').strip()[:20]}' is not a Class 12 token")
        if _date(r.get("Release_Date")) is None:
            out.append(f"  ⚠️ row {i} {label}: unparsable Release_Date")
        if vint in VINTAGE_PROVISIONAL:
            succ = _date(r.get("Successor_Date"))
            vints = later[((r.get("Series") or "").strip(), (r.get("Ref_Period") or "").strip())]
            superseded = any(v not in VINTAGE_PROVISIONAL for v in vints)
            if succ is None:
                out.append(f"  ⚠️ row {i} {label}: {vint} row with no Successor_Date — the final's date is part of the row")
            elif succ < TODAY and not superseded:
                out.append(f"  ⚠️ SUCCESSOR DUE: {label} {vint} — successor date {succ} passed, no later-vintage row")
    if out:
        return 1, out + [f"  ({len(rows)} print row(s) scanned)"]
    return 0, [f"  ✓ enums valid; no provisional row past its successor date — {len(rows)} row(s)"]


def perimeter():
    if not PERIMETER.exists():
        return _missing("perimeter", PERIMETER)
    text = PERIMETER.read_text(encoding="utf-8")
    rows = _rows(PERIMETER)
    tickers = [(r.get("Ticker") or "").strip().upper() for r in rows]
    out = []
    if not text.startswith("# FROZEN PERIMETER"):
        out.append("  ⚠️ PERIMETER.tsv lost its FROZEN banner on line 1 — the list is only frozen while the banner says so")
    extra, missing = set(tickers) - PERIMETER_TICKERS, PERIMETER_TICKERS - set(tickers)
    if extra:
        out.append(f"  ⚠️ NOT IN THE RULED EIGHT: {', '.join(sorted(extra))} — a ninth name is a Will-gated re-cut, never an edit")
    if missing:
        out.append(f"  ⚠️ RULED NAME MISSING: {', '.join(sorted(missing))}")
    if len(tickers) != len(set(tickers)):
        out.append("  ⚠️ duplicate ticker row(s)")
    if out:
        return 1, out + [f"  ({len(tickers)} row(s) vs the 8 ruled at WQ-506)"]
    return 0, [f"  ✓ FROZEN banner present; exactly the 8 ruled tickers: {' '.join(sorted(tickers))}"]


def matrix_and_flow():
    vx, fail = _load("matrix", VX)
    if fail:
        return fail
    fl, fail = _load("flow", FLOW)
    if fail:
        return fail
    if not vx:
        return 1, ["  ⚠️ 0 matrix rows — no vector can be scored or stacked (PAT-155)"]
    out, ids, unscored, mech = [], set(), [], []
    for r in vx:
        vid = (r.get("ID") or "?").strip()
        ids.add(vid)
        kind, score = _token(r.get("Kind")), _token(r.get("Score"))
        if kind not in VX_KINDS:
            out.append(f"  ⚠️ {vid}: Kind '{(r.get('Kind') or '').strip()[:20]}' is not MECHANISM/THERMOMETER")
        if score == "UNKNOWN":
            unscored.append(vid)
        elif score not in {"1", "2", "3", "4", "5"}:
            out.append(f"  ⚠️ {vid}: Score '{(r.get('Score') or '').strip()[:20]}' is not 1-5 or UNKNOWN")
        elif kind == "MECHANISM":
            mech.append(int(score))
    n_mech = sum(1 for r in vx if _token(r.get("Kind")) == "MECHANISM")
    if unscored:
        consequence = ("the MECHANISM composite remains available; unscored THERMOMETER rows are excluded"
                       if len(mech) == n_mech and n_mech
                       else "the composite cannot be stated until every MECHANISM row is scored")
        out.append(f"  ⚠️ UNSCORED: {len(unscored)} of {len(vx)} vector(s) ({' '.join(unscored)}) — "
                   f"scoring is the desk's judgment and is owed; {consequence}")
    for r in fl:
        fid = (r.get("ID") or "?").strip()
        if _token(r.get("State")) not in FLOW_STATES:
            out.append(f"  ⚠️ {fid}: State '{(r.get('State') or '').strip()[:20]}' is not in the declared FLOW enum")
        if (r.get("Vector") or "").strip() not in ids:
            out.append(f"  ⚠️ {fid}: Vector '{(r.get('Vector') or '').strip()[:20]}' has no VX row — an orphan mechanism")
    comp = (f"Total {sum(mech)}/{5 * n_mech} (raw; report the shared-root-adjusted total beside it)"
            if len(mech) == n_mech and n_mech else "composite UNKNOWN until every MECHANISM row is scored")
    tail = f"  ({len(vx)} vector(s), {n_mech} MECHANISM; {len(fl)} flow row(s); {comp})"
    if out:
        return 1, out + [tail]
    return 0, [f"  ✓ every vector scored and every flow row valid — {comp}", tail]


def _fred(fid):
    """[(date, value-string)] — raises on any failure; the caller turns that into rc 2."""
    d = os.environ.get("ISHM_FRED_DIR")
    if d:
        text = (Path(d) / f"{fid}.csv").read_text(encoding="utf-8")
    else:
        req = urllib.request.Request(FRED_URL.format(fid), headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            text = resp.read().decode("utf-8", "replace")
    lines = text.strip().splitlines()
    if not lines or "<" in lines[0] or "," not in lines[0]:
        raise ValueError("response is not a FRED CSV (HTML or empty)")
    obs = []
    for ln in lines[1:]:
        parts = ln.split(",")
        when = _date(parts[0]) if parts else None
        if when and len(parts) > 1 and parts[1].strip() not in ("", "."):
            obs.append((when, parts[1].strip()))
    return obs


def fred_hard_data():
    if OFFLINE:
        return 1, ["  ⚠️ NOT RUN (--offline): FRED hard-data leg unchecked — a skipped control is not a pass"]
    prints, fail = _load("print ledger", PRINTS)
    if fail:
        return fail
    newest = {}
    for p in prints:
        k, per = (p.get("Series") or "").strip(), _period(p.get("Ref_Period"))
        if k and per and (k not in newest or per > newest[k]):
            newest[k] = per
    out, failed, good = [], [], []
    for key, fid in FRED_SERIES.items():
        try:
            obs = _fred(fid)
        except Exception as e:  # noqa: BLE001
            failed.append(f"  🔴 FRED {fid}: fetch/parse FAILED ({type(e).__name__}: {str(e)[:80]}) — cannot certify; "
                          f"do NOT read as 'no new print'")
            continue
        if len(obs) < MIN_OBS:
            failed.append(f"  🔴 FRED {fid}: {len(obs)} observation(s) (< {MIN_OBS}) — the positive-control population "
                          f"is too small; the route is likely broken")
            continue
        last_d, last_v = obs[-1]
        if (TODAY - last_d).days > FRED_STALE_DAYS:
            failed.append(f"  🔴 FRED {fid}: newest observation {last_d} is {(TODAY - last_d).days}d old — series or route broken")
            continue
        good.append(f"{fid} {last_d:%Y-%m} = {last_v}")
        mine = newest.get(key)
        if mine is None or mine < last_d:
            have = f"ledger newest {mine:%Y-%m}" if mine else "no ledger row yet"
            out.append(f"  ⚠️ NEW PRINT ON FRED: [{key}] {fid} {last_d:%Y-%m} = {last_v} — {have} "
                       f"(read the release, then write the PRINTS row with its vintage; FRED is latest-revised)")
    tail = [f"  (FRED newest: {' · '.join(good)})"] if good else []
    src = f"DRILL DIR {os.environ['ISHM_FRED_DIR']}" if os.environ.get("ISHM_FRED_DIR") else "LIVE fred.stlouisfed.org"
    tail.append(f"  ({len(FRED_SERIES)} series checked; source {src})")
    if failed:
        return 2, failed + out + tail
    if out:
        return 1, out + tail
    return 0, [f"  ✓ ledger current with FRED on all {len(FRED_SERIES)} series"] + tail


def main():
    print("=" * 74)
    print(f"  ⏰ WALL CLOCK: {datetime.now().strftime('%Y-%m-%d %H:%M %A')} — never hand-write a time; copy this line")
    if _DRILL:
        print(f"  🧪 DRILL CLOCK: date legs evaluate as of {TODAY} (ISHM_BOOT_TODAY) — NOT a real boot")
    for v in ("ISHM_HOME", "ISHM_FRED_DIR"):
        if os.environ.get(v):
            print(f"  🧪 DRILL: {v}={os.environ[v]} — NOT a real boot")
    print("  ISHM BOOT — staleness · predictions · catalysts · missed prints · print ledger · perimeter · matrix/map · FRED")
    print("=" * 74)
    rcs = []
    print("\n--- 1. ledger staleness (workbook + TRADE.md) ---")
    if os.environ.get("ISHM_HOME"):
        print("  ⚠️ NOT RUN (drill home): the shared staleness script reads the real desk, not the copy")
        rcs.append(1)
    else:
        sw = run_alert([str(STALENESS), "ISHM", "--quiet"])
        st = run_alert([str(STALENESS), "ISHM", "--trade", "--quiet"])
        if sw == st == 0:
            print("  ✓ quiet (alert-contract: this check prints only when stale or misconfigured)")
        rcs.append(2 if 2 in (sw, st) else (1 if 1 in (sw, st) else 0))
    for title, fn in (("2. predictions-due (OPEN rows past Resolve_By)", predictions_due),
                      ("3. catalysts-due (today · ≤2d · past · forward horizon)", catalysts_due),
                      ("4. missed prints (past keyed catalysts vs PRINTS.tsv)", missed_prints),
                      ("5. print ledger (enums · provisional rows past their successor date)", print_ledger),
                      ("6. frozen perimeter (the eight ruled bellwethers)", perimeter),
                      ("7. convergence matrix + transmission map", matrix_and_flow),
                      ("8. FRED hard data (positive control · new print not yet read)", fred_hard_data)):
        print(f"\n--- {title} ---")
        rc, lines = fn()
        print("\n".join(lines))
        rcs.append(rc)
    print("\n" + "=" * 74)
    if 2 in rcs:
        print("  ISHM boot: a leg FAILED — check manually, do NOT assume quiet.")
        return 2
    if 1 in rcs:
        print("  ISHM boot: REVIEW — work the flagged items before new research.")
        return 1
    print("  ISHM boot: all quiet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
