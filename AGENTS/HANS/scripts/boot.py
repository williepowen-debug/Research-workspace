#!/usr/bin/env python3
"""
HANS Boot Sequence — European macro monitor & staleness guard

Ported from ZHAO's boot.py shape (2026-08-28), which exists because ZHAO found a
2.5-month drift on 2026-07-04 and built the fix. HANS found a **6.5-month** drift
on 2026-08-28 (BoE Bank Rate carried at 4.50 when it was 3.75) *by hand*, in a
session Will had to spawn. This script is that lesson turned into a mechanism.

DESIGN RULE THIS SCRIPT OBEYS, and it is the whole point:
  ⚠️ IT REPORTS ITS OWN PERIMETER. Section [2] names every load-bearing series
  that CANNOT be auto-pulled from this box. A boot check that silently omits
  the series it can't reach produces a clean board that means nothing —
  the exact defect class logged four times on 2026-08-28.

Sections, most-actionable first:
  [1] LIVE PULL          — auto-pullable series + band check against registry
  [2] NOT AUTO-PULLABLE  — ⚠️ the manual list, WITH its sources. Never omit.
  [3] REGISTRY STATE     — open fires from HANS_T_FIRED_LOG + scannable rows
  [4] KEY-FIGURE AGE     — load-bearing VX rows by days-since-update
  [5] DUE / OVERDUE      — predictions by Resolve_By
  [6] LEDGER STALENESS   — live VX rows only (FROZEN/RETIRED excluded by design)
  [7] KB EXPIRY          — facts past their own Stale_By. This is what Stale_By is FOR.

EXIT CODES (added 2026-08-28 after review: this script previously ALWAYS exited 0
while the charter claimed boot "enforces" expiry. Diagnostic dressed as enforcement.)
  0  CLEAN     — nothing needs attention
  1  ATTENTION — stale live vectors, expired KB facts, or failed pulls. NOT blocking:
                 a boot report should inform a session, not refuse to start one.
  2  BLOCKING  — an INTEGRITY failure, not a freshness one. Currently one condition:
                 a live pull shows a threshold BREACHED with no corresponding OPEN
                 row in the fire ledger, i.e. registry and ledger disagree about
                 reality. That is the state where acting on the board is unsafe.

MUST run with the repo venv (yfinance is not in system python3):
  .venv/bin/python AGENTS/HANS/scripts/boot.py
"""
import sys
from datetime import date, datetime
from pathlib import Path

HANS = Path(__file__).resolve().parent.parent
VX = HANS / "workbook" / "VX.tsv"
PRED = HANS / "workbook" / "PREDICTIONS.tsv"
KB = HANS / "workbook" / "KB.tsv"
THRESH = HANS / "registry" / "THRESHOLDS.tsv"
FIRES = HANS / "registry" / "HANS_T_FIRED_LOG.tsv"

STALE_DAYS = 21      # a live vector older than this is flagged
KEY_STALE_DAYS = 14  # tighter bar for load-bearing rows
DEAD = {"FROZEN", "RETIRED", "UNREACHABLE"}  # deliberately parked — never nag


# ---------------------------------------------------------------- bands
def _ttf(v):
    # ⚠️ L3/L4 CARRIED NO THRESHOLD ID until 2026-08-28 — the two MOST SEVERE tiers
    # were the ones excluded from the integrity check. Caught by test_hans, not by eye.
    if v > 200: return "🔴", "L4 CRISIS >200  [HANS-T-07]"
    if v > 100: return "🔴", "L3 RED >100  [HANS-T-07]"
    if v >= 66: return "🟠", "L2 ORANGE >=66  [HANS-T-07]"
    if v >= 60: return "🟡", "L1 WATCH >=60  [HANS-T-07]"   # id was MISSING: only L2+ reached the integrity check
    return "🟢", "below L1 (<60)"

def _eurusd(v):
    if v < 1.00: return "🔴", "CRISIS <1.00  [HANS-T-11]"     # id was missing on the SEVERE tier too
    if v < 1.05: return "🟠", "WATCH <1.05  [HANS-T-11]"
    return "🟢", "no stress"

def _dxy(v):
    return ("🟡", "dollar-strength zone >105") if v > 105 else ("🟢", "normal")

def _ctx(_v):
    return "⚪", "context only — no HANS band"

LIVE = [
    ("TTF front-month (EUR/MWh)", "TTF=F",     _ttf),
    ("EUR/USD",                   "EURUSD=X",  _eurusd),
    ("DXY",                       "DX-Y.NYB",  _dxy),
    ("GBP/USD",                   "GBPUSD=X",  _ctx),
    ("Henry Hub ($/MMBtu)",       "NG=F",      _ctx),
    ("Euro Stoxx 50",             "^STOXX50E", _ctx),
    ("DAX",                       "^GDAXI",    _ctx),
    ("FTSE 100",                  "^FTSE",     _ctx),
]

# ⚠️ The honest half. Load-bearing and NOT reachable from this box.
# ⚠️ Only what genuinely has NO feed. Bund + EGB spreads MOVED to fetch_eu.py
# on 2026-08-28 — they were never truly unreachable, only absent from yfinance.
MANUAL = [
    ("UK 10Y gilt",         "HANS-T-06",                  "tradingeconomics.com/united-kingdom/government-bond-yield"),
    ("UK 30Y gilt",         "HANS-T-13 (LDI instrument)", "tradingeconomics.com/united-kingdom/30-year-bond-yield"),
    ("ECB deposit rate",    "HANS-T-04",                  "ecb.europa.eu/press/pr  (8 GovC dates/yr)"),
    ("BoE Bank Rate",       "— (was 75bp stale 6.5mo)",   "bankofengland.co.uk  (8 MPC dates/yr)"),
    ("German/EU flash PMI", "HANS-T-01/02/03",            "pmi.spglobal.com  (~22nd-24th monthly)"),
]


def _rows(path):
    if not path.exists(): return [], []
    lines = path.read_text().rstrip("\n").split("\n")
    hdr = lines[0].split("\t")
    return hdr, [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]


def _age(d):
    try: return (date.today() - datetime.strptime(d.strip(), "%Y-%m-%d").date()).days
    except Exception: return None


def main():
    rc = 0            # 0 clean · 1 attention · 2 blocking (see module docstring)
    breached = []     # thresholds the live pull shows breached, for the §3 integrity check
    pull_fails = 0
    print(f"\n{'='*74}\n HANS BOOT — {date.today()}\n{'='*74}")

    # [1] live pull
    print("\n[1] LIVE PULL")
    try:
        import yfinance as yf
    except ImportError:
        print("  🔴 yfinance missing — run with .venv/bin/python")
        yf = None
    if yf:
        for label, sym, band in LIVE:
            try:
                px = yf.Ticker(sym).fast_info.get("lastPrice")
                if px is None: raise ValueError("no lastPrice")
                em, txt = band(float(px))
                print(f"  {em} {label:<28} {float(px):>10,.2f}   {txt}")
                if em in ("🔴", "🟠") and "HANS-T-" in txt:
                    breached.append(txt.split("[")[-1].rstrip("]").strip())
            except Exception as e:
                # a failed pull is REPORTED, never silently skipped
                print(f"  ⚠️  {label:<28} {'PULL FAILED':>10}   {sym}: {str(e)[:38]}")
                pull_fails += 1

    # [2] European primary pull — ECB Data Portal (keyless) + AGSI+
    #     Its structured return feeds BOTH the exit code and the §3 integrity check.
    print("\n[2] EUROPEAN PRIMARY PULL")
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import fetch_eu
        eu = fetch_eu.main()          # returns {observations, failures, breached}
        # ⚠️ CONSUME the return. Before 2026-08-28 this was called for its PRINTING only,
        # so ECB/AGSI failures and breaches never reached the exit code or the integrity
        # check — a run with working Yahoo and dead European primaries exited 0 CLEAN
        # while the screen said PULL FAILED.
        breached.extend(eu.get("breached", []))
        pull_fails += len(eu.get("failures", []))
        for f in eu.get("failures", []):
            print(f"  ⚠️  PRIMARY PULL FAILED: {f}")
    except Exception as e:
        print(f"  ⚠️  fetch_eu failed entirely: {str(e)[:70]} — run it directly to diagnose")
        pull_fails += 1
    print("  ⚠️  PERIMETER: a clean [1]+[2] still does NOT clear the board. Event-driven rows")
    print("     (ECB/BoE decisions, monthly PMI) have no feed by nature — check the calendar:")
    for label, tid, src in MANUAL:
        print(f"  •  {label:<34} {tid:<30} {src}")

    # [3] registry
    print("\n[3] REGISTRY STATE")
    _, fires = _rows(FIRES)
    openf = [f for f in fires if f.get("state", "").strip() == "OPEN"]
    print(f"  {len(openf)} OPEN fire(s) of {len(fires)} logged:")
    for f in openf:
        print(f"    🔥 {f['threshold_id']:<12} {f.get('tier',''):<18} {f.get('fired_date','')}  val {f.get('value_at_fire','')}")
    _, th = _rows(THRESH)
    scan = [t for t in th if "SCANNABLE-DAILY" in t.get("scannable", "")]
    unre = [t for t in th if "UNINSTRUMENTED" in t.get("scannable", "")]
    print(f"  {len(scan)} of {len(th)} rows are daily-scannable · {len(unre)} UNINSTRUMENTED (cannot fire — excluded from any clean-board count)")
    # INTEGRITY CHECK — the only blocking condition. Registry vs ledger disagreement.
    open_ids = {f["threshold_id"] for f in openf}
    breached_u = sorted(set(breached))
    orphan = [t for t in breached_u if t not in open_ids]
    print(f"  integrity perimeter: {len(breached_u)} breach(es) observed this run "
          f"across Yahoo + ECB + AGSI → {breached_u if breached_u else 'none'}")
    if orphan:
        rc = 2
        print(f"  🔴 BLOCKING — live pull shows {orphan} BREACHED with no OPEN fire row.")
        print("     Registry and fire ledger disagree about reality. Log the fire or correct the band")
        print("     BEFORE acting on this board.")

    # [4] key-figure age
    print("\n[4] KEY-FIGURE AGE")
    _, vx = _rows(VX)
    KEY = ["VX-HANS-3.05", "VX-HANS-3.06", "VX-HANS-3.08", "VX-HANS-8.01",
           "VX-HANS-8.07", "VX-HANS-8.06", "VX-HANS-4.01", "VX-HANS-4.02", "VX-HANS-2.01"]
    for k in KEY:
        r = next((x for x in vx if x["Vector_ID"] == k), None)
        if not r: continue
        a = _age(r.get("Last_Updated", ""))
        em = "🔴" if a is None or a > KEY_STALE_DAYS else ("🟡" if a > 7 else "🟢")
        print(f"  {em} {k:<15} {r['Name'][:34]:<34} {str(a)+'d' if a is not None else '?':>5}  = {r.get('Current_Value','')[:16]}")

    # [5] due / overdue
    print("\n[5] PREDICTIONS — DUE / OVERDUE")
    _, pr = _rows(PRED)
    op = [p for p in pr if p.get("Status", "").strip() == "OPEN"]
    if not op: print("  (none open)")
    for p in sorted(op, key=lambda x: x.get("Resolve_By", "")):
        a = _age(p.get("Resolve_By", ""))
        if a is None: em, note = "⚪", "no Resolve_By"
        elif a >= 0:  em, note = "🔴", f"OVERDUE by {a}d — GRADE IT"
        elif a > -14: em, note = "🟠", f"due in {-a}d"
        else:         em, note = "🟢", f"due in {-a}d"
        print(f"  {em} {p['Pred_ID']:<8} {p.get('Resolve_By',''):<12} {note}")

    # [6] ledger staleness — live rows only
    print("\n[6] LEDGER STALENESS (live rows only; FROZEN/RETIRED excluded by design)")
    live = [r for r in vx if r.get("Status", "").strip() not in DEAD]
    # ⚠️ `(_age(...) or 999)` is WRONG here: age 0 is FALSY, so every row refreshed
    # TODAY reported as 999d stale. Caught on this script's first run, 2026-08-28.
    # [[finding_test_the_guard_not_just_the_guarded]] — a guard's own v1 fails first.
    stale = []
    for r in live:
        a = _age(r.get("Last_Updated", ""))
        if a is None or a > STALE_DAYS:
            stale.append((r["Vector_ID"], r["Name"][:38], a))
    print(f"  {len(live)} live / {len(vx)} total vectors ({len(vx)-len(live)} parked)")
    if not stale:
        print(f"  🟢 no live vector older than {STALE_DAYS}d")
    else:
        rc = max(rc, 1)
        print(f"  🔴 {len(stale)} live vector(s) over {STALE_DAYS}d:")
        for vid, nm, a in sorted(stale, key=lambda x: -(x[2] if x[2] is not None else 9999))[:12]:
            print(f"     {vid:<15} {nm:<38} {str(a)+chr(100) if a is not None else 'no date'}")
    # [7] KB expiry — the whole point of the Stale_By field
    print("\n[7] KB EXPIRY (facts past their own Stale_By)")
    _, kb = _rows(KB)
    live_kb = [k for k in kb if k.get("Status", "").strip() not in {"SUPERSEDED", "RETIRED"}]
    expired = []
    for k in live_kb:
        sb = k.get("Stale_By", "").strip()
        if not sb:
            continue
        a = _age(sb)
        if a is not None and a >= 0:
            expired.append((k["ID"], k.get("Group", ""), k["Fact"][:52], a))
    noexp = [k["ID"] for k in live_kb if not k.get("Stale_By", "").strip()]
    print(f"  {len(live_kb)} live fact(s) · {len(live_kb)-len(noexp)} carry an expiry")
    if expired:
        rc = max(rc, 1)
        print(f"  🔴 {len(expired)} EXPIRED — re-verify or supersede:")
        for i, g, f, a in sorted(expired, key=lambda x: -x[3]):
            print(f"     {i:<14} {g:<12} +{a}d  {f}")
    else:
        print("  🟢 no live fact is past its Stale_By")
    # a setup/metadata row with no expiry is expected; only flag if it is NOT the seed row
    real_noexp = [i for i in noexp if not i.endswith("-001")]
    if real_noexp:
        rc = max(rc, 1)
        print(f"  ⚠️  {len(real_noexp)} live fact(s) with NO Stale_By — they can never expire: {', '.join(real_noexp[:6])}")
    elif noexp:
        print(f"  ·  {len(noexp)} seed/metadata row(s) without an expiry — expected, not flagged")
    if pull_fails:
        rc = max(rc, 1)
        print(f"\n  ⚠️  {pull_fails} live pull(s) FAILED — the board is partially blind.")
    verdict = {0: "🟢 CLEAN", 1: "🟡 ATTENTION", 2: "🔴 BLOCKING"}[rc]
    print(f"\n  EXIT {rc} — {verdict}")
    if rc == 1:
        print("  (attention, not blocking: a boot report informs a session, it does not refuse to start one)")
    print()
    return rc


if __name__ == "__main__":
    sys.exit(main())
