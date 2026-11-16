#!/usr/bin/env python3
"""
tape_scan.py — WATT boot leg: scan the PJM-RTO 5-minute LMP tape from the
STATUS tape cutoff to the latest published print, and pre-grade every run the
existing P1 letter defines.

Built 2026-11-16 by WATT (PROME assignment on Will's word 13:45 ET; idea of
2026-10-29; lesson L-59). Acceptance conditions, written before the build:
proposals/2026-11-16_TAPE_SCAN_ACCEPTANCE.md (A1-A10).

WHY: power_watch.py reads only the current EPT day. On 2026-10-29 it printed
quiet while the tape held the 10/27 18:50-19:00 RED-letter fire, because WATT
was not running 10/24-10/28. A quiet boot was a claim about its own day only.

WHAT IT DOES (and does not):
  - Cutoff: exactly one STATUS.md line
      **Tape cutoff (machine-read):** YYYY-MM-DDTHH:MM EPT
    = the last 5-min PJM-RTO interval this desk has read, either feed.
    Missing / duplicated / unparseable / future => NO API call, rc 2.
    Never falls back to scanning one day.
  - Scan start = cutoff minus 60 minutes, so a run already under way at the
    cutoff is measured from inside the window.
  - Call 1: rt_unverified_fivemin_lmps (fresh, ~15-day retention, L-44).
    Call 2 (only if call 1 left material holes): rt_fivemin_hrl_lmps
    (verified, retained at least 49 days, lags 1-4 days, KB-194).
    At most 2 DM2 calls; power_watch spends 2; a boot stays <= 4 of 6/min.
  - Price limb: 2+ consecutive 5-min prints >= LMP_RED (imported from
    power_watch.py, never retyped). Demand limb: EIA-930 hour demand / peak of
    the 24 hours before it, rounded to 1 dp, met at >= 97.0 (power_watch's
    method), reported under both hour-stamp conventions (10/29 grade practice).
  - Posting limb and EEA2-alone: NOT READ (the board shows current postings
    only). Any found run is REVIEW; the desk grades it by the letter.
  - Changes no threshold, gate letter, score or prediction. Writes nothing.

Exit: 0 = whole span read, no run · 1 = REVIEW (a price-limb run, or a
$1,000 print whose neighbour interval is missing or is the latest print) ·
2 = UNKNOWN (cutoff unreadable, API refused / rate-limited / truncated, or a
span neither call covered). rc 2 output still prints any run it found.

Usage:
  live:   .venv/bin/python3 AGENTS/WATT/tape_scan.py
  replay: .venv/bin/python3 AGENTS/WATT/tape_scan.py --cutoff 2026-10-24T00:00 \
            --now 2026-10-28T23:59 --replay-unverified F.json \
            [--replay-verified F.json] [--replay-demand F.json]
"""

import argparse
import json
import math
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
# Levels and endpoints come from the existing instrument (acceptance A3).
from power_watch import LMP_ORANGE, LMP_RED, PJM_DM2_BASE, PJM_RTO_PNODE_ID  # noqa: E402

EPT = ZoneInfo("America/New_York")
UTC = timezone.utc
STEP = timedelta(minutes=5)
LOOKBACK = timedelta(minutes=60)
TAIL_LIMIT = timedelta(minutes=60)
FUTURE_TOLERANCE = timedelta(minutes=10)
DEMAND_MET_PCT = 97.0          # P1 letter demand limb (THESIS.md; STATUS EXIT P1)
ROW_COUNT = 50000              # one call; >> 15 days x 288 rows
UNVERIFIED = "rt_unverified_fivemin_lmps"
VERIFIED = "rt_fivemin_hrl_lmps"
STATUS_PATH = HERE / "STATUS.md"
CUTOFF_LINE = re.compile(r"^\*\*Tape cutoff \(machine-read\):\*\*[ \t]*(.*)$", re.M)


class CutoffError(Exception):
    pass


def floor5(dt):
    return dt - timedelta(minutes=dt.minute % 5, seconds=dt.second,
                          microseconds=dt.microsecond)


def ept(dt):
    return dt.astimezone(EPT).strftime("%Y-%m-%d %H:%M")


def read_cutoff(text, now_utc):
    """Return (cutoff_utc, raw) from exactly one machine-read STATUS line."""
    hits = CUTOFF_LINE.findall(text)
    if len(hits) != 1:
        raise CutoffError(f"found {len(hits)} '**Tape cutoff (machine-read):**' lines "
                          f"in STATUS.md; exactly 1 required")
    raw = hits[0].strip()
    m = re.match(r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}) EPT\b", raw)
    if not m:
        raise CutoffError(f"cannot parse cutoff '{raw}'; required form "
                          f"YYYY-MM-DDTHH:MM EPT")
    try:
        naive = datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M")
    except ValueError as e:
        raise CutoffError(f"cannot parse cutoff '{raw}': {e}") from e
    cut = naive.replace(tzinfo=EPT).astimezone(UTC)
    if cut > now_utc + FUTURE_TOLERANCE:
        raise CutoffError(f"cutoff {m.group(1)} EPT is in the future (now {ept(now_utc)} EPT)")
    return cut, m.group(1)


def parse_payload(payload):
    """DM2 payload -> {utc_stamp: price}. Raises on missing items or truncation.
    UTC is derived from EPT; in the fall-back hour duplicates get fold 0 then 1
    in input-sorted order (stated limit: prices may swap between the two hours)."""
    if not isinstance(payload, dict) or payload.get("items") is None:
        raise ValueError("payload has no 'items' list")
    items = payload["items"]
    total = payload.get("totalRows")
    if isinstance(total, int) and total > len(items):
        raise ValueError(f"silent truncation: {len(items)} rows returned of totalRows {total}")
    seen = {}
    out = {}
    for r in sorted(items, key=lambda r: r["datetime_beginning_ept"]):
        naive = datetime.strptime(r["datetime_beginning_ept"][:16], "%Y-%m-%dT%H:%M")
        k = seen.get(naive, 0)
        seen[naive] = k + 1
        out[naive.replace(tzinfo=EPT, fold=min(k, 1)).astimezone(UTC)] = float(r["total_lmp_rt"])
    return out


def dm2_live_fetcher(key):
    def fetch_fn(feed, start_utc, end_utc):
        f = lambda d: (f"{d.astimezone(EPT).month}/{d.astimezone(EPT).day}/"  # noqa: E731
                       f"{d.astimezone(EPT).year} {d.astimezone(EPT):%H:%M}")
        qs = urllib.parse.urlencode({
            "rowCount": ROW_COUNT, "startRow": 1,
            "datetime_beginning_ept": f"{f(start_utc)}to{f(end_utc)}",
            "pnode_id": PJM_RTO_PNODE_ID,
            "fields": "datetime_beginning_ept,total_lmp_rt",
        })
        req = urllib.request.Request(f"{PJM_DM2_BASE}/{feed}?{qs}",
                                     headers={"Ocp-Apim-Subscription-Key": key})
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    return fetch_fn


def demand_live(hours):
    import fetch  # loaded by power_watch already; FORGE shared client
    rows = fetch.eia_pjm_demand(hours=hours)
    if not rows or "error" in rows[0]:
        raise ValueError(f"EIA-930 fetch failed: {rows[0].get('error') if rows else 'no rows'}")
    return rows


def demand_map(rows):
    out = {}
    for r in rows:
        stamp = r.get("date") or r.get("period")
        if stamp and r.get("value") not in (None, ""):
            out[datetime.strptime(stamp[:13], "%Y-%m-%dT%H").replace(tzinfo=UTC)] = float(r["value"])
    return out


def demand_pct(dmap, hour):
    """power_watch method: hour / max(24 hours before it), rounded to 1 dp."""
    if hour not in dmap:
        return None
    window = [dmap[hour - timedelta(hours=i)] for i in range(1, 25)
              if hour - timedelta(hours=i) in dmap]
    if len(window) < 20 or not max(window):
        return None
    return round(dmap[hour] / max(window) * 100.0, 1)


def missing_groups(tape, start, end):
    """Consecutive missing 5-min stamps in [start, end] as lists of stamps."""
    groups, cur, t = [], [], start
    while t <= end:
        if t in tape:
            if cur:
                groups.append(cur)
                cur = []
        else:
            cur.append(t)
        t += STEP
    if cur:
        groups.append(cur)
    return groups


def material(groups, tape):
    """A hole is material if it could hold a run (2+ stamps) or touches a $1,000 print."""
    out = []
    for g in groups:
        nbrs = (g[0] - STEP, g[-1] + STEP)
        if len(g) >= 2 or any(tape.get(n, 0) >= LMP_RED for n in nbrs):
            out.append(g)
    return out


def find_runs(tape):
    """Maximal sequences of consecutive stamps with price >= LMP_RED."""
    runs, cur = [], []
    for t in sorted(tape):
        if tape[t] >= LMP_RED and (not cur or t - cur[-1] == STEP):
            cur.append(t)
        else:
            if cur:
                runs.append(cur)
            cur = [t] if tape[t] >= LMP_RED else []
    if cur:
        runs.append(cur)
    return runs


def scan(cutoff_utc, now_utc, fetch_fn, demand_fn):
    """Core scan. Returns (rc, lines)."""
    L = []
    start = floor5(cutoff_utc - LOOKBACK)
    end_req = now_utc
    L.append(f"  cutoff {ept(cutoff_utc)} EPT; scan start {ept(start)} EPT "
             f"(60-min lookback); requested to {ept(end_req)} EPT")
    tape, src, unknown, failures = {}, {}, [], []

    # --- call 1: unverified feed ---
    try:
        rows = parse_payload(fetch_fn(UNVERIFIED, start, end_req))
        tape.update(rows)
        src.update({t: "unverified" for t in rows})
        L.append(f"  call 1 {UNVERIFIED}: {len(rows)} rows")
    except Exception as e:  # noqa: BLE001 — every failure is UNKNOWN, never clean
        failures.append(f"call 1 {UNVERIFIED}: {e}")
        L.append(f"  call 1 {UNVERIFIED}: FAILED ({e}). Span {ept(start)} to "
                 f"{ept(end_req)} EPT is UNKNOWN. No second call (same key and limit).")
        return 2, L + verdict(2, [], [], failures,
                              [(start, end_req)])

    latest = max(tape) if tape else None
    holes = material(missing_groups(tape, start, latest), tape) if latest else []
    # --- call 2: verified feed, only for material holes ---
    if holes:
        a, b = holes[0][0], holes[-1][-1]
        try:
            vrows = parse_payload(fetch_fn(VERIFIED, a, b))
            filled = 0
            for t, v in vrows.items():
                if t not in tape and a <= t <= b:
                    tape[t] = v
                    src[t] = "verified"
                    filled += 1
            L.append(f"  call 2 {VERIFIED} for {ept(a)} to {ept(b)} EPT: "
                     f"{len(vrows)} rows, {filled} missing stamps filled")
        except Exception as e:  # noqa: BLE001
            failures.append(f"call 2 {VERIFIED}: {e}")
            L.append(f"  call 2 {VERIFIED}: FAILED ({e}); holes stay UNKNOWN")
        latest = max(tape)
    else:
        L.append("  call 2: not needed (no material hole in call 1)")

    groups = missing_groups(tape, start, latest) if latest else []
    for g in material(groups, tape):
        unknown.append((g[0], g[-1] + STEP))
    if latest is None:
        unknown.append((start, end_req))
    elif now_utc - latest > TAIL_LIMIT:
        unknown.append((latest + STEP, now_utc))
    singles_missing = sum(1 for g in groups if len(g) == 1) - sum(
        1 for g in material(groups, tape) if len(g) == 1)
    n_exp = int((latest - start) / STEP) + 1 if latest else 0
    L.append(f"  covered {ept(min(tape)) if tape else '-'} to {ept(latest) if latest else '-'} EPT: "
             f"{len(tape)} of {n_exp} 5-min stamps; {singles_missing} isolated missing "
             f"stamp(s) that cannot complete a run (counted, not escalated)")

    # --- per EPT day ---
    by_day = {}
    for t in sorted(tape):
        by_day.setdefault(t.astimezone(EPT).date(), []).append(t)
    L.append(f"  per EPT day (n · max · prints >= ${LMP_ORANGE:,.0f} · >= ${LMP_RED:,.0f}):")
    for d, ts in by_day.items():
        top = max(ts, key=lambda t: tape[t])
        L.append(f"    {d}  n={len(ts):>3}  max ${tape[top]:>9,.2f} @{top.astimezone(EPT):%H:%M}  "
                 f"{sum(tape[t] >= LMP_ORANGE for t in ts):>3}  {sum(tape[t] >= LMP_RED for t in ts):>3}")

    # --- runs and singles ---
    first = min(tape) if tape else None
    runs, review_singles, transients = [], [], []
    for r in find_runs(tape):
        flags = []
        if r[0] < cutoff_utc <= r[-1] + STEP:
            flags.append("STRADDLES THE CUTOFF (began before it; partly seen last session)")
        if r[0] == first:
            flags.append("BEGAN AT OR BEFORE SCAN START (true start not measured)")
        if r[-1] == latest:
            flags.append("RUNNING AT LATEST PRINT")
        if (r[0] - STEP not in tape and r[0] != first) or \
           (r[-1] + STEP not in tape and r[-1] != latest):
            flags.append("NEIGHBOUR INTERVAL MISSING: true length UNKNOWN")
        if len(r) >= 2:
            runs.append((r, flags))
        elif flags:
            review_singles.append((r, flags))
        else:
            transients.append(r)

    dmap, dfail = None, None
    if runs or review_singles:
        earliest = min(x[0][0] for x in runs + review_singles)
        hours = min(5000, math.ceil((now_utc - earliest) / timedelta(hours=1)) + 34)
        try:
            dmap = demand_map(demand_fn(hours))
        except Exception as e:  # noqa: BLE001
            dfail = str(e)

    def demand_line(r):
        if dmap is None:
            return f"demand limb UNKNOWN (EIA-930: {dfail})", "UNKNOWN"
        hb = sorted({t.replace(minute=0) for t in r})
        conv = {}
        parts = []
        for name, hrs in (("hour-beginning", hb), ("hour-ending", [h + timedelta(hours=1) for h in hb])):
            pcts = [(h, demand_pct(dmap, h)) for h in hrs]
            met = any(p is not None and p >= DEMAND_MET_PCT for _, p in pcts)
            unk = any(p is None for _, p in pcts)
            conv[name] = "MET" if met else ("UNKNOWN" if unk else "NOT-MET")
            parts.append(f"{name} " + ", ".join(
                f"{h:%m-%dT%H}Z {'n/a' if p is None else f'{p:.1f}%'}" for h, p in pcts)
                + f" => {conv[name]}")
        vals = set(conv.values())
        state = ("MET-BOTH" if vals == {"MET"} else "SPLIT" if "MET" in vals
                 else "UNKNOWN" if "UNKNOWN" in vals else "NOT-MET")
        return "demand limb (>= 97.0% of prior-24h peak): " + "; ".join(parts), state

    L.append(f"  price-limb runs (>= ${LMP_RED:,.0f} for 2+ consecutive 5-min prints): {len(runs)}")
    for r, flags in runs:
        dl, state = demand_line(r)
        prices = " / ".join(f"${tape[t]:,.2f}" for t in r[:6]) + (" ..." if len(r) > 6 else "")
        feeds = "/".join(sorted({src[t] for t in r}))
        L.append(f"    RUN {ept(r[0])} to {r[-1].astimezone(EPT):%H:%M} EPT, {len(r)} prints "
                 f"({feeds}): {prices}; max ${max(tape[t] for t in r):,.2f}")
        for f_ in flags:
            L.append(f"      {f_}")
        L.append(f"      {dl}")
        L.append("      posting limb and EEA2: NOT READ by this scan; check posting ids issued in the window")
        pre = {"MET-BOTH": "PRICE + DEMAND LIMBS MET: FIRED-ON-LETTER pre-grade; desk confirms on the verified feed",
               "SPLIT": "SPLIT: demand limb met under one hour convention only; desk grades",
               }.get(state, f"PRICE LIMB ONLY (demand {state}): letter NOT established by the scan; desk checks postings")
        L.append(f"      pre-grade: {pre}")
    for r, flags in review_singles:
        L.append(f"    SINGLE ${tape[r[0]]:,.2f} @{ept(r[0])} EPT ({src[r[0]]}): {'; '.join(flags)}; REVIEW")
    if transients:
        L.append("  single prints >= $1,000 (price alone = logged transient, not a band): " + ", ".join(
            f"{ept(r[0])} ${tape[r[0]]:,.2f}" for r in transients))

    rc = 2 if (unknown or failures) else (1 if (runs or review_singles) else 0)
    return rc, L + verdict(rc, runs, review_singles, failures, unknown)


def verdict(rc, runs, review_singles, failures, unknown):
    L = []
    for a, b in unknown:
        L.append(f"  UNKNOWN span {ept(a)} to {ept(b)} EPT: not read on either feed; P1 there is UNKNOWN, not quiet")
    found = len(runs) + len(review_singles)
    if rc == 2:
        L.append(f"  TAPE SCAN: UNKNOWN ({len(unknown)} span(s), {len(failures)} failure(s))"
                 + (f"; ALSO REVIEW: {found} run(s)/edge print(s) found in the read part" if found else ""))
    elif rc == 1:
        L.append(f"  TAPE SCAN: REVIEW — {len(runs)} price-limb run(s), {len(review_singles)} edge print(s); desk grades by the P1 letter")
    else:
        L.append("  TAPE SCAN: 0 price-limb runs in the whole span on the feeds read. This says nothing "
                 "about postings or EEA declarations (not read).")
    return L


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--status", default=str(STATUS_PATH))
    ap.add_argument("--cutoff", help="replay: YYYY-MM-DDTHH:MM EPT (bypasses STATUS)")
    ap.add_argument("--now", help="replay: YYYY-MM-DDTHH:MM EPT")
    ap.add_argument("--replay-unverified")
    ap.add_argument("--replay-verified")
    ap.add_argument("--replay-demand")
    ap.add_argument("--retention-days", type=float, default=15.0,
                    help="replay: emulate the unverified feed's retention")
    a = ap.parse_args(argv)

    print("=" * 72)
    print("  WATT TAPE SCAN — PJM-RTO 5-min LMP since the STATUS tape cutoff")
    print("=" * 72)
    now = (datetime.strptime(a.now, "%Y-%m-%dT%H:%M").replace(tzinfo=EPT).astimezone(UTC)
           if a.now else datetime.now(UTC))
    try:
        if a.cutoff:
            cut, raw = read_cutoff(f"**Tape cutoff (machine-read):** {a.cutoff} EPT", now)
        else:
            cut, raw = read_cutoff(Path(a.status).read_text(encoding="utf-8"), now)
    except (CutoffError, OSError) as e:
        print(f"  CUTOFF UNREADABLE: {e}.\n  No API call made. P1 since the last session is "
              f"UNKNOWN; read the tape by hand from the STATUS prose cutoff (L-59).")
        print("  TAPE SCAN: UNKNOWN (cutoff unreadable)")
        return 2

    if a.replay_unverified:
        fetch_fn, demand_fn = replay_fetchers(a, now)
        print("  MODE: REPLAY from saved payloads (not a live read)")
    else:
        key = os.environ.get("PJM_API_KEY", "")
        if not key:
            print("  PJM_API_KEY absent on this box. No call made. P1 since the cutoff is UNKNOWN.")
            print("  TAPE SCAN: UNKNOWN (no key)")
            return 2
        fetch_fn, demand_fn = dm2_live_fetcher(key), demand_live
    rc, lines = scan(cut, now, fetch_fn, demand_fn)
    print("\n".join(lines))
    return rc


def replay_fetchers(a, now):
    """Serve saved DM2 payloads as the API would: only rows inside the requested
    window, and (unverified) only rows inside the emulated retention."""
    def load(p):
        return json.load(open(p, encoding="utf-8"))
    unv = load(a.replay_unverified)
    ver = load(a.replay_verified) if a.replay_verified else None
    dem = load(a.replay_demand) if a.replay_demand else None
    keep_from = now - timedelta(days=a.retention_days)

    def fetch_fn(feed, s, e):
        src = unv if feed == UNVERIFIED else ver
        if src is None:
            raise ValueError(f"no replay payload for {feed}")
        rows = parse_payload({"items": src["items"]})
        items = [{"datetime_beginning_ept": t.astimezone(EPT).strftime("%Y-%m-%dT%H:%M:00"),
                  "total_lmp_rt": v} for t, v in rows.items()
                 if s <= t <= e and t <= now and (feed != UNVERIFIED or t >= keep_from)]
        return {"items": items, "totalRows": len(items)}

    def demand_fn(hours):
        if dem is None:
            raise ValueError("no replay demand file")
        # serve only hours that existed at the replayed 'now'
        cap = now.strftime("%Y-%m-%dT%H")
        return [r for r in dem if (r.get("date") or r.get("period") or "")[:13] <= cap]
    return fetch_fn, demand_fn


if __name__ == "__main__":
    sys.exit(main())
