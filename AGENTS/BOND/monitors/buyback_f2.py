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
      rc=0 = nothing OWED and no DATA GAP (explicitly NOT "every read is done forever");
      rc=1 = OWED (an in-scope op has published with no VALID ledgered read) and/or a DATA GAP
             (past op with null results · scheduled date absent from the feed · unclassifiable
             in-window op · details rows with no ops row · details/ops totals disagree · window
             expired) -- the two counters are printed SEPARATELY and named in the summary;
      rc=2 = fetch failure, NOT a pass (from the CLI; from boot it is counted as one GAP).
      ⛔ WINDOW EXPIRY ALARM: past WINDOW[1] this tool returns non-zero every boot until the next
      QRA's schedule is parsed in -- a carrier that dates itself is L401's defect one quarter out.
  BLIND READ 2026-09-17 (coldreader, 17 findings): 10 ❌ fixed the same session (window expiry
  alarm · same-date multi-op guard + blocking totals check · OWED/GAP counters split · ledger row
  validity = packet_path present AND resolvable (inbox/ or processed/) AND verdict · normalised
  scope match with null-field ⇒ UNCLASSIFIED (a gap, never "no read owed") · --op refuses to render
  an out-of-scope packet · one-sided selftest assertions tightened · rc=2 reachable from the CLI ·
  enumeration = ops ∪ details dates · null cap guard). ⚠️ RESIDUE declared, not fixed: the
  "newest quartile" cut is 20-50% of DISTINCT maturities under banker's rounding (q=5 ⇒ 1 of 5) --
  the base rate was computed with the same rule, so the 0/52 stands, but the label overstates the
  precision; buybacks_operations has no total-count truncation guard (223 < 500 today); an all-zero
  par published op yields verdict None (counted OWED, packet header reads None); printed "rc=" lines
  are prose, the function returns a COUNT that boot adds to drift.
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
LEDGER_PROCESSED_FALLBACK = ("inbox/", "inbox/processed/")   # RED git-mv's consumed packets

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


def _norm(x):
    if x is None:
        return None
    x = " ".join(str(x).split()).casefold()
    return None if x in ("", "null", "none") else x


def in_scope(op):
    """Return (verdict, reason) with verdict in {True, False, None}; None = UNCLASSIFIED (a null or
    unrecognised field on an in-window op) -- reported as a GAP, never as 'no F2 read owed'."""
    d = op.get("operation_date", "")
    if not (WINDOW[0] <= d <= WINDOW[1]):
        return False, "outside the sb0607 window"
    ot, st, mb = _norm(op.get("operation_type")), _norm(op.get("security_type")), _norm(op.get("maturity_bucket"))
    if ot is None or st is None or mb is None:
        return None, f"UNCLASSIFIED -- null field(s) on an in-window op (type={op.get('operation_type')!r}, sec={op.get('security_type')!r}, bucket={op.get('maturity_bucket')!r}); verify at the primary"
    if ot != "liquidity support":
        return False, f"operation_type {op.get('operation_type')!r} (F2 reads liquidity-support ops only)"
    if st != "nominal coupons":
        return False, f"security_type {op.get('security_type')!r} (F2 reads NOMINAL long-end ops; FT-11 reads nominal benchmarks)"
    if mb not in {b.casefold() for b in IN_SCOPE_BUCKETS}:
        return False, f"bucket {op.get('maturity_bucket')!r} is not a stepped-up sector (sb0607 = 10Y-20Y and 20Y-30Y only)"
    return True, "stepped-up long-end nominal LS op"


def published(rows):
    """Results are PUBLISHED iff any eligible row carries a non-null par_amt_accepted."""
    return any(_dec(r.get("par_amt_accepted")) is not None for r in rows)


def complete(op, rows):
    """A PUBLISHED op is GRADEABLE only when its results are COMPLETE (added 2026-09-24).

    ⛔ Why: published() flips on the FIRST non-null row, and metrics() counts a null row as $0.
    FiscalData publishes security_details BEFORE the ops-row totals (KB-BND-272), so at ~14:15 ET a
    partial publication would be graded as final. An independent read (2026-09-24) built the case:
    today's 35 eligible rows with only two filled and the ops row null read 66.67% ON-THE-RUN, FIRES,
    rc=0 -- a confident verdict on half the data, and the details-vs-ops cross-check was skipped
    precisely because the ops row was null. Every clause below fails CLOSED (no verdict, a GAP).
    """
    nulls = sum(1 for r in rows if _dec(r.get("par_amt_accepted")) is None)
    if nulls:
        return False, f"{nulls} of {len(rows)} eligible rows still null (partial publication)"
    ne = _dec(op.get("nbr_issues_eligible"))
    if ne is None:
        return False, "ops-row nbr_issues_eligible null -- cannot confirm the eligible list is whole"
    if int(ne) != len(rows):
        return False, f"{len(rows)} detail rows vs nbr_issues_eligible {int(ne)} (quartile base incomplete)"
    if _dec(op.get("total_par_amt_accepted")) is None:
        return False, "ops-row total_par_amt_accepted null -- details sum cannot be cross-checked"
    return True, "complete"


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
        verdict = "ON-THE-RUN (F2 FIRES, 🟠 marker -> RED/PROME)" if rs > ON_THE_RUN_CUT else "OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)"
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


def ledger_row_valid(row, repo_root=None):
    """A ledger row discharges the obligation ONLY if it names a verdict AND a packet path that
    resolves -- at the path given, or at the recipient's inbox/processed/ (RED git-mv's consumed
    packets there, so a path recorded at delivery goes dead within minutes). Returns (ok, why)."""
    if not row:
        return False, "no ledger row"
    if not (row.get("verdict") or "").strip():
        return False, "ledger row has no verdict"
    pp = (row.get("packet_path") or "").strip()
    if not pp:
        return False, "ledger row has no packet_path"
    root = repo_root or os.path.normpath(os.path.join(HERE, "..", "..", ".."))
    cands = [pp, pp.replace("/inbox/", "/inbox/processed/", 1)]
    for c in cands:
        if os.path.exists(os.path.join(root, c)):
            return True, c
    return False, f"packet_path does not resolve at {pp} or its inbox/processed/ variant"


def _pct(x):
    return "n/a" if x is None else f"{(x * 100):.2f}%"


# ----------------------------------------------------------------------------- pending
def pending_report(ops, sd, ledger, today, schedule=None, repo_root=None):
    """Pure: returns (lines, n_owed, n_gaps). No I/O beyond os.path.exists on ledger paths.
    `schedule` defaults to the issuer SCHEDULE."""
    schedule = SCHEDULE if schedule is None else schedule
    by = {}
    for r in sd:
        by.setdefault(r["operation_date"], []).append(r)
    ops_by = {}
    for o in ops:
        ops_by.setdefault(o.get("operation_date", ""), []).append(o)
    lines, owed, gaps = [], 0, 0
    if today > WINDOW[1]:
        gaps += 1
        lines.append(f"   ⛔ WINDOW EXPIRED: today {today} > {WINDOW[1]} (sb0607 / August-quarter schedule). This carrier is DATED "
                     f"by its window -- parse the November QRA's tentative buyback schedule into SCHEDULE/WINDOW before trusting "
                     f"any 'nothing owed' line. Non-zero every boot until then.")
    seen = set()
    dates = sorted(d for d in (set(ops_by) | set(by)) if WINDOW[0] <= d <= WINDOW[1])
    for d in dates:
        dops = ops_by.get(d, [])
        rows = by.get(d, [])
        if not dops:
            gaps += 1
            lines.append(f"   🔴 {d}  security_details rows exist ({len(rows)}) but NO operations row -> UNCLASSIFIED (bucket unknown); "
                         f"the ops row may be lagging -- re-fetch; counted as a GAP")
            seen.add(d)
            continue
        if len(dops) > 1:
            gaps += 1
            lines.append(f"   🔴 {d}  {len(dops)} operations share this date and security_details is keyed by date only -> "
                         f"CUSIP sets would MERGE; no verdict computed; grade by hand at the primary (GAP)")
            seen.add(d)
            continue
        op = dops[0]
        ok, why = in_scope(op)
        if ok is None:
            gaps += 1
            lines.append(f"   🔴 {d}  {why} (GAP -- never 'no read owed')")
            seen.add(d)
            continue
        if not ok:
            lines.append(f"   ℹ️  {d}  {op.get('security_type')} / {op.get('maturity_bucket')} / {op.get('operation_type')}"
                         f" -> OUT OF SCOPE, no F2 read owed ({why})")
            continue
        seen.add(d)
        if not published(rows):
            when = f"{op.get('operation_start_time_est')}-{op.get('operation_close_time_est')} ET"
            cap = _dec(op.get("max_par_amt_redeemed"))
            cap_s = f"cap ${cap / Decimal(10**9):.1f}B" if cap is not None else "cap n/a (null in the announcement row)"
            if d < today:
                gaps += 1
                tag = "PAST -- results not yet in security_details (check the primary, KB-BND-272 lag) -- GAP"
            else:
                tag = "TODAY" if d == today else "upcoming"
            lines.append(f"   ⏳ {d}  {op.get('maturity_bucket')}  {cap_s}  ANNOUNCED, results null  [{tag}; op {when}; results ~2:15 PM ET]")
            continue
        cok, cwhy = complete(op, rows)
        if not cok:
            gaps += 1
            lines.append(f"   🔴 {d}  {op.get('maturity_bucket')}  results PARTIAL -> NO VERDICT ({cwhy}); re-run when complete (GAP)")
            continue
        m = metrics(op, rows)
        if m["accepted_ops_row"] is not None and m["accepted_ops_row"] != m["accepted_total_details"]:
            gaps += 1
            lines.append(f"   🔴 {d}  {op.get('maturity_bucket')}  details sum ${m['accepted_total_details']} != ops row ${m['accepted_ops_row']} "
                         f"-> BLOCKED, no verdict (merged/partial rows?); grade by hand at the primary (GAP)")
            continue
        led = ledger.get(d)
        valid, vwhy = ledger_row_valid(led, repo_root)
        if valid:
            lines.append(f"   ✅ {d}  {op.get('maturity_bucket')}  PUBLISHED, read ROUTED -> {led.get('routed_to')} "
                         f"({vwhy}) verdict {led.get('verdict')}; recent {led.get('recent_share_pct')}%")
        else:
            owed += 1
            lines.append(f"   🔴 {d}  {op.get('maturity_bucket')}  PUBLISHED and {vwhy} -> F2 READ OWED TO RED NOW. "
                         f"recent_share {_pct(m['recent_share'])} -> {m['verdict']}.  Run: --op {d}")
    for d, bucket, size in schedule:
        if d in seen or d < WINDOW[0]:
            continue
        if d in ops_by:
            continue        # present in the feed and classified out of scope above (a mis-labelled feed row)
        if d < today:
            gaps += 1
            lines.append(f"   🔴 {d}  {bucket}  on the ISSUER SCHEDULE, PAST, and NOT in the FiscalData feed -> verify at the primary (cancelled? fetch gap?) -- GAP")
        else:
            lines.append(f"   📅 {d}  {bucket}  {size}  SCHEDULED (issuer PDF 9/9); preliminary CUSIP list D-1 11:00 ET, op 1:40-2:00 PM ET")
    return lines, owed, gaps


def _pending(today=None):
    """Returns (count, fetch_failed). count = owed + gaps."""
    today = today or _dt.date.today().isoformat()
    try:
        ops, sd = fetch_live()
    except Exception as e:  # noqa: BLE001
        print(f"   [buyback_f2] FETCH FAILURE: {e} -- NOT a pass (CLI rc=2; boot counts one GAP)")
        return 1, True
    lines, owed, gaps = pending_report(ops, sd, read_ledger(), today)
    print(f"   window {WINDOW[0]} -> {WINDOW[1]} · scope = LS + nominal + {{10Y-20Y, 20Y-30Y}} · ledger {os.path.relpath(LEDGER, os.path.dirname(HERE))}")
    for l in lines:
        print(l)
    if owed or gaps:
        print(f"   [buyback_f2] NOT A PASS -- OWED reads: {owed} (route to RED before closeout) · DATA GAPS: {gaps} (verify at the primary). Count returned = {owed + gaps}.")
    else:
        print("   [buyback_f2] clean -- nothing OWED and no data gap right now (NOT 'all reads done': the next in-scope op re-arms this).")
    return owed + gaps, False


def pending_check(today=None):
    """Called from boot_recompute.py. Prints; returns a COUNT (owed + gaps; a fetch failure = 1) that boot adds to drift."""
    return _pending(today)[0]


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
    # cap=None models an announcement row whose max_par_amt_redeemed is null
    op = {"operation_date": date, "operation_type": optype, "security_type": sectype, "maturity_bucket": bucket,
          "max_par_amt_redeemed": cap, "total_par_amt_offered": offered, "total_par_amt_accepted": "null",
          "operation_start_time_est": "01:40 PM", "operation_close_time_est": "02:00 PM"}
    rr = [dict(operation_date=date, **r) for r in (rows or [])]
    # A synthetic op whose rows are ALL non-null models COMPLETE results, so it carries the ops-row
    # totals the real feed publishes once complete (2026-09-24, with complete()); any null row keeps
    # the ops row null = the partial-publication state, which complete() must refuse.
    if rr and all(_dec(r.get("par_amt_accepted")) is not None for r in rr):
        op["nbr_issues_eligible"] = str(len(rr))
        op["total_par_amt_accepted"] = f"{sum(_dec(r['par_amt_accepted']) for r in rr):.2f}"
    return op, rr


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
    check("9/10 recent_share = 1.79% exactly -> OFF-THE-RUN", round(m["recent_share"] * 100, 2) == Decimal("1.79") and m["verdict"].startswith("OFF"))
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
    lines, owed, gaps = pending_report([ann], rows, {}, "2026-09-24", schedule=SCHEDULE[1:])
    check("announced op TODAY -> pending, not owed, no gap", owed == 0 and gaps == 0 and any("⏳ 2026-09-24" in l for l in lines))
    lines, owed, gaps = pending_report([ann], rows, {}, "2026-09-26", schedule=SCHEDULE[1:])
    check("announced op PAST with null results -> a DATA GAP, not an owed read", owed == 0 and gaps == 1)
    # THE GUARD ITSELF: a published in-scope op with no ledger row is OWED; with a row it is not (OVERLAP).
    pub, prow = _synth("2026-09-24", "20Y to 30Y", rows=[
        {"cusip_nbr": "OLD", "coupon_rate_pct": "1.250", "maturity_date": "2050-05-15", "par_amt_accepted": "3000000000.00", "weighted_avg_accepted_price": "60.0"},
        {"cusip_nbr": "MID", "coupon_rate_pct": "3.000", "maturity_date": "2053-05-15", "par_amt_accepted": "0.00", "weighted_avg_accepted_price": "null"},
        {"cusip_nbr": "NEW1", "coupon_rate_pct": "4.500", "maturity_date": "2055-11-15", "par_amt_accepted": "1000000000.00", "weighted_avg_accepted_price": "99.0"},
        {"cusip_nbr": "NEW2", "coupon_rate_pct": "4.750", "maturity_date": "2056-02-15", "par_amt_accepted": "0.00", "weighted_avg_accepted_price": "null"}])
    lines, owed, gaps = pending_report([pub], prow, {}, "2026-09-25", schedule=SCHEDULE[1:])
    check("published in-scope op, no ledger row -> OWED (gaps 0)", owed == 1 and gaps == 0 and any("🔴 2026-09-24" in l for l in lines))
    import tempfile
    tmp = tempfile.mkdtemp(); os.makedirs(os.path.join(tmp, "AGENTS/RED/inbox/processed")); open(os.path.join(tmp, "AGENTS/RED/inbox/processed/p.md"), "w").write("x")
    lines, owed, gaps = pending_report([pub], prow, {"2026-09-24": {"op_date": "2026-09-24", "routed_to": "RED", "packet_path": "AGENTS/RED/inbox/p.md", "verdict": "OFF", "recent_share_pct": "0.00"}}, "2026-09-25", schedule=SCHEDULE[1:], repo_root=tmp)
    check("published in-scope op WITH a VALID ledger row (path resolves via inbox/processed/) -> routed, not owed (overlap)", owed == 0 and gaps == 0 and any("✅ 2026-09-24" in l for l in lines))
    lines, owed, gaps = pending_report([pub], prow, {"2026-09-24": {"op_date": "2026-09-24"}}, "2026-09-25", schedule=SCHEDULE[1:], repo_root=tmp)
    check("ledger row with ONLY op_date does NOT discharge -> still OWED", owed == 1 and any("no verdict" in l or "no packet_path" in l for l in lines))
    lines, owed, gaps = pending_report([pub], prow, {"2026-09-24": {"op_date": "2026-09-24", "routed_to": "RED", "packet_path": "AGENTS/RED/inbox/missing.md", "verdict": "OFF"}}, "2026-09-25", schedule=SCHEDULE[1:], repo_root=tmp)
    check("ledger row whose packet_path resolves nowhere -> still OWED", owed == 1 and any("does not resolve" in l for l in lines))
    # SAME-DATE MULTI-OP: the real 9/10 op plus a TIPS op on the same date would merge CUSIP sets -> blocked, a GAP, no verdict.
    tips2, _ = _synth("2026-09-10", "10Y to 30Y", sectype="TIPS")
    lines, owed, gaps = pending_report([fx["operation"], tips2], fx["security_details"], {}, "2026-09-11", schedule=[])
    check("two ops on one date -> GAP, no verdict, nothing 'routed' or 'fires'", gaps == 1 and owed == 0 and not any("FIRES" in l or "ROUTED" in l for l in lines))
    # DETAILS/OPS TOTAL MISMATCH -> blocked
    bad = dict(fx["operation"]); bad["total_par_amt_accepted"] = "1.00"
    lines, owed, gaps = pending_report([bad], fx["security_details"], {}, "2026-09-11", schedule=[])
    check("details sum != ops row -> BLOCKED as a GAP, no verdict", gaps == 1 and owed == 0 and any("BLOCKED" in l for l in lines))
    # UNCLASSIFIED (null field) on an in-window op -> GAP, never 'no read owed'
    nul, nrows = _synth("2026-10-20", None)
    lines, owed, gaps = pending_report([nul], nrows, {}, "2026-10-21", schedule=[])
    check("null bucket on an in-window op -> UNCLASSIFIED GAP", gaps == 1 and any("UNCLASSIFIED" in l for l in lines) and not any("no F2 read owed" in l for l in lines))
    ws, wrows = _synth("2026-10-20", " 20y TO 30Y  ")
    check("whitespace/case-variant bucket still classifies IN scope", in_scope(ws)[0] is True)
    # DETAILS WITHOUT AN OPS ROW -> visible as a GAP
    lines, owed, gaps = pending_report([], [dict(operation_date="2026-10-20", cusip_nbr="Z", coupon_rate_pct="4.0", maturity_date="2050-05-15", par_amt_accepted="1000000.00", weighted_avg_accepted_price="99")], {}, "2026-10-21", schedule=[])
    check("security_details rows with no ops row -> GAP (not invisible)", gaps == 1 and any("NO operations row" in l for l in lines))
    # NULL CAP on an announced op does not crash the report
    ann2, arows2 = _synth("2026-09-24", "20Y to 30Y", cap=None, rows=[{"cusip_nbr": "X1", "coupon_rate_pct": "4.000", "maturity_date": "2050-02-15", "par_amt_accepted": "null", "weighted_avg_accepted_price": "null"}])
    lines, owed, gaps = pending_report([ann2], arows2, {}, "2026-09-24", schedule=[])
    check("announced op with null cap -> reported, no crash", any("cap n/a" in l for l in lines))
    # WINDOW EXPIRY: past 11/4 the tool is non-zero even when every scheduled op is routed
    lines, owed, gaps = pending_report([], [], {}, "2026-11-20", schedule=[])
    check("past WINDOW end -> ⛔ WINDOW EXPIRED gap, never rc=0", gaps >= 1 and any("WINDOW EXPIRED" in l for l in lines))
    mm = metrics(pub, prow)
    check("synthetic recent_share = 0.00% exactly (q=4 distinct maturities -> idx 3 -> cut 2056-02-15, whose par is 0)", round(mm["recent_share"] * 100, 2) == Decimal("0.00"))
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
    lines, owed, gaps = pending_report([], [], {}, "2026-09-17", schedule=SCHEDULE[1:])
    check("schedule: 6 future in-scope ops listed 📅", sum(1 for l in lines if "📅" in l) == 6 and owed == 0 and gaps == 0)
    lines, owed, gaps = pending_report([], [], {}, "2026-09-26", schedule=SCHEDULE[1:])
    check("schedule: a PAST scheduled op missing from the feed is a GAP 🔴 (not an owed read)", any("🔴 2026-09-24" in l for l in lines) and owed == 0 and gaps == 1)
    # WHOLE-SCHEDULE case as it stands on 2026-09-17: fixture 9/10 op ledgered, nothing owed, six scheduled.
    lines, owed, gaps = pending_report([fx["operation"]], fx["security_details"], read_ledger(), "2026-09-17")
    check("full schedule on 2026-09-17 with the LIVE ledger: 9/10 routed (path resolves), 0 owed, 0 gaps, 6 scheduled", owed == 0 and gaps == 0 and sum(1 for l in lines if "📅" in l) == 6 and any("✅ 2026-09-10" in l for l in lines))
    lines, owed, gaps = pending_report([fx["operation"]], fx["security_details"], {}, "2026-09-17")
    check("full schedule on 2026-09-17 with an EMPTY ledger: 9/10 is OWED (the L401 state before this tool)", owed == 1 and any("🔴 2026-09-10" in l for l in lines))
    # PARTIAL PUBLICATION (2026-09-24 independent read): must NOT grade.
    check("9/10 fixture is COMPLETE (40 rows == nbr_issues_eligible 40, ops total present)", complete(fx["operation"], fx["security_details"])[0] is True)
    pr = [dict(r) for r in fx["security_details"]]
    for r in pr[2:]:
        r["par_amt_accepted"] = "null"
    check("partial rows (38 of 40 null) -> NOT complete", complete(fx["operation"], pr)[0] is False)
    pop = dict(fx["operation"]); pop["total_par_amt_accepted"] = "null"
    check("ops-row total null -> NOT complete", complete(pop, fx["security_details"])[0] is False)
    check("missing eligible row (39 of 40) -> NOT complete", complete(fx["operation"], fx["security_details"][:-1])[0] is False)
    lines, owed, gaps = pending_report([pop], pr, {}, "2026-09-10", schedule=[])
    check("partial publication in the report -> GAP + NO VERDICT, never owed/graded", gaps == 1 and owed == 0 and any("PARTIAL" in l for l in lines))
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
        print(f"[buyback_f2] {a.op} {op.get('security_type')} / {op.get('maturity_bucket')} / {op.get('operation_type')} -> {'IN SCOPE' if ok else ('UNCLASSIFIED: ' if ok is None else 'OUT OF SCOPE: ') + why}")
        if ok is not True:
            print("   ⛔ no packet rendered -- F2 packets are for in-scope ops only"); return 2
        if len([o for o in ops if o["operation_date"] == a.op]) > 1:
            print("   ⛔ more than one operation on this date; details rows would merge -- grade by hand"); return 2
        if not published(rows):
            print("   results NOT published in security_details -- nothing to grade (do not quote the ops row)"); return 1
        cok, cwhy = complete(op, rows)
        if not cok:
            print(f"   ⛔ results PARTIAL -- {cwhy}. NO packet; re-run when complete."); return 1
        m = metrics(op, rows)
        if m["accepted_ops_row"] is not None and m["accepted_ops_row"] != m["accepted_total_details"]:
            print(f"   ⛔ details sum {m['accepted_total_details']} != ops row {m['accepted_ops_row']} -- no packet"); return 2
        print(render_packet(m))
        return 0
    count, failed = _pending()
    return 2 if failed else (1 if count else 0)


if __name__ == "__main__":
    sys.exit(main())
