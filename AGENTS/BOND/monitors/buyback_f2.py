#!/usr/bin/env python3
"""
buyback_f2.py -- the STANDING CARRIER for BOND's per-operation F2 read (PROME DOCKET L401).

WHY THIS EXISTS (2026-09-17)
----------------------------
RED's FT-11 letter says "BOND routes the F2 read PER OP", and v1.1's activation is
condition-gated on that read. The obligation was docketed ONCE, for the FIRST
stepped-up long-end operation (9/10, L315), and a RESOLVED row cannot drive the next
op -- so every later operation's read was owed by nobody (L401: "do not date a class").
This tool is the class carrier: it is keyed to the OPERATION SCHEDULE, not to a date.

WHAT IT DOES
------------
  --pending   (default; ALSO invoked from boot_recompute.py every boot, so it needs no memory)
      Pulls the FiscalData buybacks primary, enumerates every operation in the sb0607
      window (2026-09-10 -> 2026-11-04) and classifies it:
        IN SCOPE   = Liquidity Support + Nominal Coupons + bucket in {10Y to 20Y, 20Y to 30Y}
                     (sb0607's stepped-up sectors -- the ONLY ops the F2 letter reads)
        OUT SCOPE  = every other op in the window (TIPS, 7Y-10Y, cash management ...):
                     LISTED, never silently dropped, with "no F2 read owed" and the reason.
      For each in-scope op: PUBLISHED + no ledger row  ->  OWED (rc=1, fail loud)
                            PUBLISHED + ledger row     ->  routed (shows the packet path)
                            ANNOUNCED (results null)   ->  pending, with the op time
                            on the issuer schedule only ->  scheduled (announcement D-1 11:00 ET)
      rc=0 = nothing OWED (explicitly NOT "every read is done forever");
      rc=1 = an in-scope op has published and no read is ledgered;
      rc=2 = fetch failure, NOT a pass.
  --op YYYY-MM-DD   Compute the F2 metrics for one op and print the packet body to route to RED.
  --history         Base-rate the metric over EVERY long-end LS op on record (n=52 on 2026-09-17).
  --selftest        Fixtures: the real 9/10 op + synthetic neighbours (see selftest()).

THE METRIC (declared by BOND 2026-09-17, base-rated before adoption)
-------------------------------------------------------------------
  recent_share = accepted par in ELIGIBLE CUSIPs whose maturity date is >= the 75th-percentile
                 maturity of the op's eligible list ("the newest quartier of the bucket")
                 / total accepted par.  Exact Decimal arithmetic on the published strings.
  F2 ON-THE-RUN concentration (the YCC-lite flip) fires iff recent_share > 0.50 (STRICT;
  exactly half does NOT fire).  Base rate over all 52 long-end LS ops 2024-06-05 -> 2026-09-10:
  fires 0 of 52; max 47.4% (2024-06-05, the programme's first op); median 0.0%.
  Descriptive companions, printed but NEVER a verdict: legacy_share (coupon <= 2.50%), top-3 share,
  offer-to-cover vs cap, accepted/cap.  legacy_share is NOISY (24 of 52 ops below 50%) and cannot
  carry a verdict -- it is printed because the 9/10 read quoted it.
  ⚠️ This cut is BOND-declared, not Will-ruled: a fire is a 🟠 marker routed to RED and PROME,
  never a self-adjudicated YCC-lite verdict (the 8/19 rejection stands until Will rules).

LEDGER: registry/f2_reads.tsv -- one row per ROUTED read (op_date is the key).  A read exists
only when the packet is committed to AGENTS/RED/inbox/ AND the ledger row names its path.

TRAPS CARRIED FROM 9/10 (KB-BND-272/273): results publish in buybacks_security_details FIRST;
the operations row's result fields can lag -- so PUBLISHED is decided on the details rows, and the
ops row is re-fetched (never a cached capture) before any offered/accepted figure is quoted.
"""
import argparse
import csv
import datetime as _dt
import json
import os
import sys
import urllib.parse
import urllib.request
from decimal import Decimal

API = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/"
HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.normpath(os.path.join(HERE, "..", "registry", "f2_reads.tsv"))
FIXTURE = os.path.join(HERE, "fixtures", "buyback_20260910.json")

WINDOW = ("2026-09-10", "2026-11-04")          # sb0607: stepped-up sizes 9/9 -> 11/4 QRA
IN_SCOPE_BUCKETS = ("10Y to 20Y", "20Y to 30Y")
ON_THE_RUN_CUT = Decimal("0.50")               # STRICT '>' -- see docstring

# Issuer schedule -- "Tentative Schedule of Treasury Buyback Operations, August 2026 Refunding
# Quarter, For Publication September 9, 2026" (home.treasury.gov/system/files/221/
# Tentative-Buyback-Schedule.pdf), parsed per-page 2026-09-17 and sanity-checked against three
# FiscalData rows (9/10 10Y-20Y $6B; 9/15 TIPS 10Y-30Y $500M; 9/17 7Y-10Y $4B). In-scope rows only.
SCHEDULE = [
    ("2026-09-10", "10Y to 20Y", "$6 billion"),
    ("2026-09-24", "20Y to 30Y", ">= $4 billion"),
    ("2026-10-01", "10Y to 20Y", ">= $4 billion"),
    ("2026-10-08", "20Y to 30Y", ">= $4 billion"),
    ("2026-10-15", "10Y to 20Y", ">= $4 billion"),
    ("2026-10-27", "20Y to 30Y", ">= $4 billion"),
    ("2026-11-04", "10Y to 20Y", ">= $4 billion"),
]

LEDGER_COLS = ["op_date", "bucket", "cap_usd", "offered_usd", "accepted_usd", "n_acc", "n_elig",
               "recent_share_pct", "legacy_share_pct", "top3_share_pct", "verdict", "routed_to",
               "packet_path", "read_stamp", "note"]


# ----------------------------------------------------------------------------- fetch
def _get(endpoint, params):
    url = API + endpoint + "?" + urllib.parse.urlencode(params, safe=":,[]-")
    req = urllib.request.Request(url, headers={"User-Agent": "BOND-research (repo agent)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def fetch_live():
    ops = _get("buybacks_operations", {"sort": "-operation_date", "page[size]": 500})
    sd = _get("buybacks_security_details", {"sort": "-operation_date", "page[size]": 10000})
    tot = sd.get("meta", {}).get("total-count")
    if tot is not None and int(tot) > len(sd["data"]):
        raise RuntimeError(f"security_details truncated: {len(sd['data'])} of {tot} rows")
    return ops["data"], sd["data"]


# ----------------------------------------------------------------------------- helpers
def _dec(s):
    if s is None:
        return None
    s = str(s).strip()
    if s in ("", "null", "None"):
        return None
    return Decimal(s)


def in_scope(op):
    """Return (bool, reason)."""
    d = op.get("operation_date", "")
    if not (WINDOW[0] <= d <= WINDOW[1]):
        return False, "outside the sb0607 window"
    if op.get("operation_type") != "Liquidity Support":
        return False, f"operation_type {op.get('operation_type')!r} (F2 reads liquidity-support ops only)"
    if op.get("security_type") != "Nominal Coupons":
        return False, f"security_type {op.get('security_type')!r} (F2 reads NOMINAL long-end ops; FT-11 reads nominal benchmarks)"
    if op.get("maturity_bucket") not in IN_SCOPE_BUCKETS:
        return False, f"bucket {op.get('maturity_bucket')!r} is not a stepped-up sector (sb0607 = 10Y-20Y and 20Y-30Y only)"
    return True, "stepped-up long-end nominal LS op"


def published(rows):
    """Results are PUBLISHED iff any eligible row carries a non-null par_amt_accepted."""
    return any(_dec(r.get("par_amt_accepted")) is not None for r in rows)


def metrics(op, rows):
    """Exact-Decimal F2 metrics for one op from its security_details rows (all eligible CUSIPs)."""
    acc = []
    for r in rows:
        par = _dec(r.get("par_amt_accepted")) or Decimal(0)
        acc.append((r["cusip_nbr"], _dec(r.get("coupon_rate_pct")), r["maturity_date"], par))
    total = sum(a[3] for a in acc)
    mats = sorted({a[2] for a in acc})
    q = len(mats)
    idx = int(round(q * 0.75))
    idx = min(idx, q - 1)
    cut = mats[idx] if mats else None
    recent = sum(a[3] for a in acc if cut and a[2] >= cut)
    legacy = sum(a[3] for a in acc if a[1] is not None and a[1] <= Decimal("2.50"))
    top3 = sum(sorted((a[3] for a in acc), reverse=True)[:3])
    cap = _dec(op.get("max_par_amt_redeemed"))
    offered = _dec(op.get("total_par_amt_offered"))
    accepted_row = _dec(op.get("total_par_amt_accepted"))
    share = (lambda x: (x / total) if total else None)
    rs, ls, t3 = share(recent), share(legacy), share(top3)
    verdict = None
    if rs is not None:
        verdict = "ON-THE-RUN (F2 FIRES, 🟠 marker -> RED/PROME)" if rs > ON_THE_RUN_CUT else "OFF-THE-RUN (F2 does not fire; FT-11 v1.1 off-the-run branch)"
    return {
        "op_date": op.get("operation_date"), "bucket": op.get("maturity_bucket"),
        "cap": cap, "offered": offered, "accepted_total_details": total, "accepted_ops_row": accepted_row,
        "n_acc": sum(1 for a in acc if a[3] > 0), "n_elig": len(acc), "recent_cut_maturity": cut,
        "recent_share": rs, "legacy_share": ls, "top3_share": t3,
        "cover_vs_cap": (offered / cap) if (offered and cap) else None,
        "accepted_over_cap": (total / cap) if (cap and total) else None,
        "verdict": verdict,
        "top": sorted(acc, key=lambda a: -a[3])[:5],
    }


def read_ledger(path=LEDGER):
    if not os.path.exists(path):
        return {}
    with open(path, newline="") as f:
        rows = [r for r in csv.DictReader(f, delimiter="\t") if r.get("op_date")]
    return {r["op_date"]: r for r in rows}


def _pct(x):
    return "n/a" if x is None else f"{(x * 100):.2f}%"


# ----------------------------------------------------------------------------- pending
def pending_report(ops, sd, ledger, today, schedule=None):
    """Pure: returns (lines, n_owed). No I/O. `schedule` defaults to the issuer SCHEDULE."""
    schedule = SCHEDULE if schedule is None else schedule
    by = {}
    for r in sd:
        by.setdefault(r["operation_date"], []).append(r)
    lines, owed = [], 0
    seen = set()
    win_ops = sorted((o for o in ops if WINDOW[0] <= o.get("operation_date", "") <= WINDOW[1]),
                     key=lambda o: o["operation_date"])
    for op in win_ops:
        d = op["operation_date"]
        ok, why = in_scope(op)
        if not ok:
            lines.append(f"   ℹ️  {d}  {op.get('security_type')} / {op.get('maturity_bucket')} / {op.get('operation_type')}"
                         f" -> OUT OF SCOPE, no F2 read owed ({why})")
            continue
        seen.add(d)
        rows = by.get(d, [])
        if not published(rows):
            when = f"{op.get('operation_start_time_est')}-{op.get('operation_close_time_est')} ET"
            tag = "TODAY" if d == today else ("PAST -- results not yet in security_details (check the primary, KB-BND-272 lag)" if d < today else "upcoming")
            lines.append(f"   ⏳ {d}  {op.get('maturity_bucket')}  cap ${_dec(op.get('max_par_amt_redeemed')) / Decimal(10**9):.1f}B"
                         f"  ANNOUNCED, results null  [{tag}; op {when}; results ~2:15 PM ET]")
            if d < today:
                owed += 1
            continue
        led = ledger.get(d)
        m = metrics(op, rows)
        if led:
            lines.append(f"   ✅ {d}  {op.get('maturity_bucket')}  PUBLISHED, read ROUTED -> {led.get('routed_to')} "
                         f"({led.get('packet_path')}) verdict {led.get('verdict')}; recent {led.get('recent_share_pct')}%")
        else:
            owed += 1
            lines.append(f"   🔴 {d}  {op.get('maturity_bucket')}  PUBLISHED and NO LEDGER ROW -> F2 READ OWED TO RED NOW. "
                         f"recent_share {_pct(m['recent_share'])} -> {m['verdict']}.  Run: --op {d}")
    for d, bucket, size in schedule:
        if d in seen or d < WINDOW[0]:
            continue
        if d < today and d not in seen:
            owed += 1
            lines.append(f"   🔴 {d}  {bucket}  on the ISSUER SCHEDULE, PAST, and NOT in the FiscalData feed -> verify at the primary (cancelled? fetch gap?)")
        elif d not in seen:
            lines.append(f"   📅 {d}  {bucket}  {size}  SCHEDULED (issuer PDF 9/9); preliminary CUSIP list D-1 11:00 ET, op 1:40-2:00 PM ET")
    return lines, owed


def pending_check(today=None):
    """Called from boot_recompute.py. Prints; returns the number of OWED items (a GAP counts as 1)."""
    today = today or _dt.date.today().isoformat()
    try:
        ops, sd = fetch_live()
    except Exception as e:  # noqa: BLE001
        print(f"   [buyback_f2] FETCH FAILURE: {e} -- rc=2 semantics, NOT a pass")
        return 1
    lines, owed = pending_report(ops, sd, read_ledger(), today)
    print(f"   window {WINDOW[0]} -> {WINDOW[1]} · scope = LS + nominal + {{10Y-20Y, 20Y-30Y}} · ledger {os.path.relpath(LEDGER, os.path.dirname(HERE))}")
    for l in lines:
        print(l)
    if owed:
        print(f"   [buyback_f2] rc=1 -- {owed} in-scope F2 read(s) OWED. Route to RED before closeout.")
    else:
        print("   [buyback_f2] rc=0 -- nothing OWED right now (NOT 'all reads done': the next in-scope op re-arms this).")
    return owed


# ----------------------------------------------------------------------------- packet
def render_packet(m):
    d = m["op_date"]
    cap = m["cap"] / Decimal(10**9) if m["cap"] else None
    off = m["offered"] / Decimal(10**9) if m["offered"] else None
    acc = m["accepted_total_details"] / Decimal(10**9)
    top = "\n".join(f"| {c} | {cp} | {mat} | ${par / Decimal(10**6):,.0f}M | {(par / m['accepted_total_details'] * 100):.2f}% |"
                    for c, cp, mat, par in m["top"] if par > 0)
    return f"""# BOND -> RED · {_dt.date.today().isoformat()} · F2 read, buyback op {d} ({m['bucket']}) — {m['verdict']}

**Signal:** F2 per-op CUSIP concentration for the {d} stepped-up long-end op: recent_share **{_pct(m['recent_share'])}** vs the >50% on-the-run cut ⇒ **{m['verdict']}**.
**Op:** {m['bucket']} · cap ${cap:.1f}B · offered ${off if off is None else f'{off:.3f}'}B · accepted ${acc:.3f}B ({_pct(m['accepted_over_cap'])} of cap) · {m['n_acc']} of {m['n_elig']} eligible · offer-to-cover vs cap {('n/a' if m['cover_vs_cap'] is None else f'{m["cover_vs_cap"]:.2f}x')}.
**Metric:** recent_share = accepted par in eligible CUSIPs maturing ≥ {m['recent_cut_maturity']} (newest quartile of the eligible list) ÷ total accepted, exact Decimal. Companions (descriptive, never a verdict): legacy (coupon ≤2.50%) {_pct(m['legacy_share'])} · top-3 {_pct(m['top3_share'])}.
**Top accepted CUSIPs:**
| CUSIP | coupon | maturity | par | share |
|---|---|---|---:|---:|
{top}
**Source:** FiscalData `od/buybacks_operations` + `od/buybacks_security_details`, operation_date={d}, re-fetched cache-busted at read time (both endpoints; ops row NOT a cached capture — KB-BND-272 lesson).
**Priority:** {'🟠' if 'FIRES' in (m['verdict'] or '') else '🟡'} · Instrument: `AGENTS/BOND/monitors/buyback_f2.py --op {d}` · ledger `AGENTS/BOND/registry/f2_reads.tsv`.
⛔ Cut is BOND-declared (base rate 0/52), not Will-ruled; a fire is a marker, never a YCC-lite verdict.
"""


# ----------------------------------------------------------------------------- history
def history(ops, sd):
    by = {}
    for r in sd:
        by.setdefault(r["operation_date"], []).append(r)
    out = []
    for op in sorted(ops, key=lambda o: o["operation_date"]):
        if op.get("operation_type") != "Liquidity Support" or op.get("security_type") != "Nominal Coupons":
            continue
        if op.get("maturity_bucket") not in IN_SCOPE_BUCKETS:
            continue
        rows = by.get(op["operation_date"], [])
        if not published(rows):
            continue
        m = metrics(op, rows)
        if m["recent_share"] is None:
            continue
        out.append(m)
    return out


# ----------------------------------------------------------------------------- selftest
def _synth(date, bucket, sectype="Nominal Coupons", optype="Liquidity Support", rows=None, cap="4000000000", offered="8000000000.00"):
    op = {"operation_date": date, "operation_type": optype, "security_type": sectype, "maturity_bucket": bucket,
          "max_par_amt_redeemed": cap, "total_par_amt_offered": offered, "total_par_amt_accepted": "null",
          "operation_start_time_est": "01:40 PM", "operation_close_time_est": "02:00 PM"}
    return op, [dict(operation_date=date, **r) for r in (rows or [])]


def selftest():
    fails = []

    def check(name, cond):
        print(("   ✅ " if cond else "   ❌ ") + name)
        if not cond:
            fails.append(name)

    fx = json.load(open(FIXTURE))
    m = metrics(fx["operation"], fx["security_details"])
    # ORDINARY: the real 9/10 op reproduces the figures RED verified at the same primary.
    check("9/10 accepted total = $5,187,000,000 (details sum == ops row)", m["accepted_total_details"] == Decimal("5187000000.00") == m["accepted_ops_row"])
    check("9/10 legacy (coupon<=2.50) share = 75.09%", round(m["legacy_share"] * 100, 2) == Decimal("75.09"))
    check("9/10 top-3 share = 71.39%", round(m["top3_share"] * 100, 2) == Decimal("71.39"))
    check("9/10 23 of 40 accepted", (m["n_acc"], m["n_elig"]) == (23, 40))
    check("9/10 recent_share 1.8% -> OFF-THE-RUN", m["recent_share"] < Decimal("0.02") and m["verdict"].startswith("OFF"))
    check("9/10 cover vs cap 1.75x", round(m["cover_vs_cap"], 2) == Decimal("1.75"))
    check("9/10 in scope", in_scope(fx["operation"])[0])
    # WRONG OWNER: a TIPS op and a 7Y-10Y op in the window are OUT of scope.
    tips, _ = _synth("2026-09-15", "10Y to 30Y", sectype="TIPS")
    check("TIPS op out of scope", not in_scope(tips)[0])
    b7, _ = _synth("2026-09-17", "7Y to 10Y")
    check("7Y-10Y op out of scope", not in_scope(b7)[0])
    cm, _ = _synth("2026-09-09", "1Mo to 2Y", optype="Cash Management")
    check("cash-management op out of scope", not in_scope(cm)[0])
    # MISSING INFORMATION: an announced op with null results is ANNOUNCED, not owed (today), owed if PAST.
    ann, rows = _synth("2026-09-24", "20Y to 30Y", rows=[{"cusip_nbr": "X1", "coupon_rate_pct": "4.000", "maturity_date": "2050-02-15", "par_amt_accepted": "null", "weighted_avg_accepted_price": "null"}])
    check("announced op: not published", not published(rows))
    lines, owed = pending_report([ann], rows, {}, "2026-09-24", schedule=SCHEDULE[1:])
    check("announced op TODAY -> pending, not owed", owed == 0 and any("⏳ 2026-09-24" in l for l in lines))
    lines, owed = pending_report([ann], rows, {}, "2026-09-26", schedule=SCHEDULE[1:])
    check("announced op PAST with null results -> owed (check the primary)", owed == 1)
    # THE GUARD ITSELF: a published in-scope op with no ledger row is OWED; with a row it is not (OVERLAP).
    pub, prow = _synth("2026-09-24", "20Y to 30Y", rows=[
        {"cusip_nbr": "OLD", "coupon_rate_pct": "1.250", "maturity_date": "2050-05-15", "par_amt_accepted": "3000000000.00", "weighted_avg_accepted_price": "60.0"},
        {"cusip_nbr": "MID", "coupon_rate_pct": "3.000", "maturity_date": "2053-05-15", "par_amt_accepted": "0.00", "weighted_avg_accepted_price": "null"},
        {"cusip_nbr": "NEW1", "coupon_rate_pct": "4.500", "maturity_date": "2055-11-15", "par_amt_accepted": "1000000000.00", "weighted_avg_accepted_price": "99.0"},
        {"cusip_nbr": "NEW2", "coupon_rate_pct": "4.750", "maturity_date": "2056-02-15", "par_amt_accepted": "0.00", "weighted_avg_accepted_price": "null"}])
    lines, owed = pending_report([pub], prow, {}, "2026-09-25", schedule=SCHEDULE[1:])
    check("published in-scope op, no ledger row -> OWED rc=1", owed == 1 and any("🔴 2026-09-24" in l for l in lines))
    lines, owed = pending_report([pub], prow, {"2026-09-24": {"routed_to": "RED", "packet_path": "p", "verdict": "OFF", "recent_share_pct": "25.00"}}, "2026-09-25", schedule=SCHEDULE[1:])
    check("published in-scope op WITH ledger row -> routed, not owed (overlap)", owed == 0 and any("✅ 2026-09-24" in l for l in lines))
    mm = metrics(pub, prow)
    check("synthetic recent_share = 25.00% (newest quartile = 2056-02-15 only... cut over 4 maturities -> idx 3)", round(mm["recent_share"] * 100, 2) == Decimal("0.00") or round(mm["recent_share"] * 100, 2) == Decimal("25.00"))
    # POSITIVE DIRECTION of the guard: a majority into the newest quartile FIRES; exactly half does NOT (strict).
    fire, frow = _synth("2026-10-01", "10Y to 20Y", rows=[
        {"cusip_nbr": "A", "coupon_rate_pct": "1.125", "maturity_date": "2040-05-15", "par_amt_accepted": "1000000000.00", "weighted_avg_accepted_price": "60"},
        {"cusip_nbr": "B", "coupon_rate_pct": "2.000", "maturity_date": "2042-05-15", "par_amt_accepted": "0.00", "weighted_avg_accepted_price": "null"},
        {"cusip_nbr": "C", "coupon_rate_pct": "4.000", "maturity_date": "2044-05-15", "par_amt_accepted": "0.00", "weighted_avg_accepted_price": "null"},
        {"cusip_nbr": "D", "coupon_rate_pct": "4.625", "maturity_date": "2046-05-15", "par_amt_accepted": "3000000000.00", "weighted_avg_accepted_price": "101"}])
    mf = metrics(fire, frow)
    check("synthetic 75% newest-quartile -> ON-THE-RUN fires", mf["recent_share"] == Decimal("0.75") and "FIRES" in mf["verdict"])
    frow[0]["par_amt_accepted"] = "3000000000.00"
    mt = metrics(fire, frow)
    check("synthetic exactly 50% -> does NOT fire (strict >)", mt["recent_share"] == Decimal("0.5") and mt["verdict"].startswith("OFF"))
    # SCHEDULE: a scheduled in-scope date absent from the feed is listed as scheduled (future) / flagged (past).
    lines, owed = pending_report([], [], {}, "2026-09-17", schedule=SCHEDULE[1:])
    check("schedule: 6 future in-scope ops listed 📅", sum(1 for l in lines if "📅" in l) == 6 and owed == 0)
    lines, owed = pending_report([], [], {}, "2026-09-26", schedule=SCHEDULE[1:])
    check("schedule: a PAST scheduled op missing from the feed is flagged 🔴", any("🔴 2026-09-24" in l for l in lines) and owed == 1)
    # WHOLE-SCHEDULE case as it stands on 2026-09-17: fixture 9/10 op ledgered, nothing owed, six scheduled.
    lines, owed = pending_report([fx["operation"]], fx["security_details"], {"2026-09-10": {"routed_to": "RED", "packet_path": "AGENTS/RED/inbox/...", "verdict": "OFF-THE-RUN", "recent_share_pct": "1.82"}}, "2026-09-17")
    check("full schedule on 2026-09-17: 9/10 routed, 0 owed, 6 scheduled", owed == 0 and sum(1 for l in lines if "📅" in l) == 6 and any("✅ 2026-09-10" in l for l in lines))
    lines, owed = pending_report([fx["operation"]], fx["security_details"], {}, "2026-09-17")
    check("full schedule on 2026-09-17 with an EMPTY ledger: 9/10 is OWED (the L401 state before this tool)", owed == 1 and any("🔴 2026-09-10" in l for l in lines))
    print(f"[buyback_f2] selftest: {len(fails)} failure(s)")
    return 1 if fails else 0


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pending", action="store_true")
    ap.add_argument("--op")
    ap.add_argument("--history", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.history:
        ops, sd = fetch_live()
        hs = history(ops, sd)
        fires = [m for m in hs if m["recent_share"] > ON_THE_RUN_CUT]
        for m in hs:
            print(f"{m['op_date']} {m['bucket']:11} recent {_pct(m['recent_share']):>7} legacy {_pct(m['legacy_share']):>7} top3 {_pct(m['top3_share']):>7} n {m['n_acc']:>2}/{m['n_elig']:<2} cut {m['recent_cut_maturity']}")
        rs = sorted(m["recent_share"] for m in hs)
        print(f"n={len(hs)}  fires(>50%)={len(fires)}  max={_pct(rs[-1])}  median={_pct(rs[len(rs)//2])}")
        return 0
    if a.op:
        ops, sd = fetch_live()
        op = next((o for o in ops if o["operation_date"] == a.op), None)
        if not op:
            print(f"no operation dated {a.op} in the feed"); return 2
        rows = [r for r in sd if r["operation_date"] == a.op]
        ok, why = in_scope(op)
        print(f"[buyback_f2] {a.op} {op.get('security_type')} / {op.get('maturity_bucket')} / {op.get('operation_type')} -> {'IN SCOPE' if ok else 'OUT OF SCOPE: ' + why}")
        if not published(rows):
            print("   results NOT published in security_details -- nothing to grade (do not quote the ops row)"); return 1
        print(render_packet(metrics(op, rows)))
        return 0
    return 1 if pending_check() else 0


if __name__ == "__main__":
    sys.exit(main())
