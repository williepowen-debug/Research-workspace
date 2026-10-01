#!/usr/bin/env python3
"""dark_window_check.py — how long has each desk been dark while it holds a live test? (DOCKET L487 half (b))

WHY: PJM's 4th emergency (9/16–9/18) happened inside WATT-11's registered window while WATT had no
session; nothing on any fleet surface carried it, and WATT graded it 8 days late only because a vendor
feed still retained the tape. The WQ-184 driver keys on DATED rows, WQ-206 on aged ACTION lines, WQ-221
on aged waits — an EVENT inside a dark desk's live window falls through all three.

WHAT (descriptive; record runs/2026-10-01_L487_DARK_WINDOW_CHECK.md):
  For every desk holding a LIVE TEST — an open row in a ledger registered in scorecards/LEDGERS.tsv, or a
  PROME/GATES.tsv row whose state starts LIVE and whose owner cell names it — print its DARK RUN: days
  since its last OWN-AUTHORED commit (subject starts with the desk name). Sorted longest first.
  "Open" is scorecard.bucket(status) is None — the scorecard's terminal-token map, imported.
  ⛔ It never chooses an alert level. N is Will's (a WQ row). With --threshold N it flags runs ≥ N.

rc (CHECK_STANDARD §9): 0 measured (no threshold given, or none ≥ N) · 1 ≥1 desk at/over --threshold
                        2 UNKNOWN: registry unreadable, zero ledgers evaluated, or git log failed
USAGE
  python3 AGENTS/DAEDALUS/scripts/dark_window_check.py [--as-of YYYY-MM-DD] [--threshold N]
          [--live DESK,DESK] [--lookback 45]
  python3 AGENTS/DAEDALUS/scripts/dark_window_check.py --selftest
PROVES: the dark-run arithmetic over own-authored commit subjects, and which registered tests were open.
Does NOT prove the desk missed anything (a dark desk may have nothing happen), does NOT see a live
session that has not committed (pass --live from ListAgents), and does NOT see tests held outside the
registry or GATES (KB watch rows, prose windows).
"""
import argparse
import datetime as dt
import os
import re
import subprocess
import sys
import tempfile
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import scorecard  # noqa: E402  — LEDGERS registry reader + terminal-token map (one definition)

ROOT = scorecard.ROOT
GATES = os.path.join(ROOT, "PROME", "GATES.tsv")
MADE_COLS = ("Date_Made", "Made_Date", "made", "registered", "Date")
DESK_RE = re.compile(r"^AGENTS/([A-Z][A-Z0-9]+)/")


def iso(s):
    m = re.search(r"(?<!\d)(\d{4}-\d\d-\d\d)(?!\d)", s or "")
    if not m:
        return None
    try:
        return dt.date.fromisoformat(m.group(1))
    except ValueError:
        return None


GRADED = re.compile(r"(\d{4}-\d\d-\d\d)\s*\(?\s*graded", re.I)


def grade_date(cell):
    """Replay: a cell naming a GRADE date ('2026-09-23 (event) / 2026-09-28 (graded)') resolves on that
    date, never the event date (result-read X4); otherwise the first ISO date."""
    m = GRADED.search(cell or "")
    return dt.date.fromisoformat(m.group(1)) if m else iso(cell)


def open_tests(registry, as_of, live_mode):
    """{desk: [row_id, …]}, cannot[(path, reason)], evaluated_count."""
    tests, cannot, evaluated = {}, [], 0
    reg = scorecard.tsv_rows(registry)
    want = ["path", "status_col", "date_col", "date_source", "outcome_col", "status"]
    if not reg or reg[0][1] != want:
        raise RuntimeError(f"LEDGERS registry header != {want}")
    for ln, f in reg[1:]:
        if len(f) != len(want):
            cannot.append((f[0] if f else f"registry line {ln}", "registry row width"))
            continue
        r = dict(zip(want, f))
        if r["status"] != "LIVE":
            continue
        m = DESK_RE.match(r["path"])
        if not m:
            cannot.append((r["path"], "path is not AGENTS/<DESK>/…"))
            continue
        desk, p = m.group(1), os.path.join(ROOT, r["path"])
        if not os.path.isfile(p):
            cannot.append((r["path"], "file absent"))
            continue
        rows = scorecard.tsv_rows(p)
        if not rows:
            cannot.append((r["path"], "empty"))
            continue
        h = rows[0][1]
        made_col = next((c for c in MADE_COLS if c in h), None)
        if r["status_col"] not in h or made_col is None:
            cannot.append((r["path"], f"header lacks {'status' if r['status_col'] not in h else 'a made-date'} column"))
            continue
        si, mi, oi = h.index(r["status_col"]), h.index(made_col), (h.index(r["outcome_col"]) if r["outcome_col"] in h else None)
        di = h.index(r["date_col"]) if r["date_col"] in h else None
        evaluated += 1
        bad = width = 0
        for rln, row in rows[1:]:
            if len(row) != len(h):
                width += 1                     # counted and printed (B4: never silent)
                continue
            made = iso(row[mi])
            if made is None:
                b0 = scorecard.bucket(row[si])
                if b0 is None or b0 == "UNMAPPED":
                    bad += 1                   # only an OPEN row lost to an unparseable date matters (W1)
                continue
            if made > as_of:
                continue
            b = scorecard.bucket(row[si])
            terminal = b is not None and b != "UNMAPPED"   # an unknown token (e.g. NEEDS_VERIFY) counts OPEN: over-include, never hide
            if live_mode:
                is_open = not terminal
            else:
                rd = grade_date(row[di]) if di is not None else None
                if rd is None and r["date_source"] == "INLINE-FIRST-ISO" and oi is not None:
                    rd = grade_date(row[oi])
                is_open = (not terminal) or (rd is not None and rd > as_of)
            if is_open:
                tests.setdefault(desk, []).append(row[0].strip()[:16])
        if bad:
            cannot.append((r["path"], f"{bad} row(s) with an open OR unmapped status token and no parseable made date — not counted (an unmapped token may be the desk's own terminal word)"))
        if width:
            cannot.append((r["path"], f"{width} row(s) whose field count != header — not read"))
    return tests, cannot, evaluated


def live_gates(path, desks_known):
    """{desk: [gate_id, …]} for GATES rows whose state starts LIVE; owner cell matched by desk-name word."""
    out = {}
    if not os.path.isfile(path):
        return out, [(path, "GATES absent")]
    rows = scorecard.tsv_rows(path)
    if not rows or "owner" not in rows[0][1] or "state" not in rows[0][1]:
        return out, [(path, "GATES header lacks owner/state")]
    h = rows[0][1]
    oi, si = h.index("owner"), h.index("state")
    for _ln, f in rows[1:]:
        if len(f) <= max(oi, si) or not f[si].strip().upper().startswith("LIVE"):
            continue
        for d in desks_known:
            if re.search(r"\b%s\b" % d, f[oi]):
                out.setdefault(d, []).append(f[0].strip())
    return out, []


def own_dates(desk, log_lines):
    """B3, pure: dates of lines `YYYY-MM-DD<TAB>subject` whose subject STARTS with the desk name, optionally
    after one `[tag] ` (`[cleanup] SAM: …`, result-read X7). `DESK-08 …` (a row id) and any subject
    merely naming the desk (`PROME -> WATT`, `WALTER: deliver … WATT`) never count."""
    pat = re.compile(r"^(?:\[[^\]]{1,30}\]\s*)?%s\b(?!-)" % re.escape(desk))
    return sorted({dt.date.fromisoformat(l[:10]) for l in log_lines if len(l) > 11 and pat.match(l[11:])})


def own_commit_dates(desk, since, until):
    """Local (machine = ET) author dates (W7: never UTC) of the desk's own commits."""
    r = subprocess.run(["git", "-C", ROOT, "log", f"--since={since} 00:00", f"--until={until} 23:59:59",
                        "--format=%ad%x09%s", "--date=short-local"], capture_output=True, text=True, timeout=60)
    if r.returncode:
        raise RuntimeError(f"git log failed rc={r.returncode}")
    return own_dates(desk, r.stdout.splitlines())


def assess(as_of, threshold=None, live=(), lookback=45, registry=scorecard.REGISTRY, gates=GATES,
           commit_dates=own_commit_dates, today=None):
    today = today or dt.datetime.now(ZoneInfo("America/New_York")).date()
    live_mode = as_of >= today
    try:
        tests, cannot, evaluated = open_tests(registry, as_of, live_mode)
    except (RuntimeError, OSError) as e:
        return 2, [f"DARK-WINDOW UNKNOWN: {e}"]
    if evaluated == 0:
        return 2, ["DARK-WINDOW UNKNOWN: zero registered ledgers evaluated — an empty population proves nothing"]
    desks_known = sorted(set(tests) | {m.group(1) for m in (DESK_RE.match(f"AGENTS/{d}/") for d in os.listdir(os.path.join(ROOT, "AGENTS"))) if m}) \
        if os.path.isdir(os.path.join(ROOT, "AGENTS")) else sorted(tests)
    gmap, gcannot = live_gates(gates, desks_known) if live_mode else ({}, [])
    cannot += gcannot
    since = as_of - dt.timedelta(days=lookback)
    lines = []
    for d in sorted(set(tests) | set(gmap)):
        if d in live:
            lines.append((-1, d, "LIVE-UNCOMMITTED (session live per caller; not counted as dark)"))
            continue
        try:
            ds = commit_dates(d, since.isoformat(), as_of.isoformat())
        except (RuntimeError, OSError, subprocess.TimeoutExpired) as e:
            return 2, [f"DARK-WINDOW UNKNOWN: {e}"]
        last = ds[-1] if ds else None
        run = (as_of - last).days if last else None
        rows = tests.get(d, [])
        g = gmap.get(d, [])
        txt = (f"{'≥' + str(lookback) if run is None else run:>4}d dark · last own commit {last or 'none in ' + str(lookback) + 'd'} · "
               f"{len(rows)} open row(s)" + (f" ({', '.join(rows[:3])}{' …' if len(rows) > 3 else ''})" if rows else "")
               + (f" · {len(g)} LIVE gate(s) ({', '.join(g[:2])}{' …' if len(g) > 2 else ''})" if g else ""))
        lines.append((lookback + 1 if run is None else run, d, txt))
    lines.sort(key=lambda t: (-t[0], t[1]))
    flagged = [t for t in lines if threshold is not None and t[0] >= threshold]
    mode = "LIVE (open = non-terminal now)" if live_mode else "REPLAY (open = made ≤ as-of and unresolved at as-of; a LOWER BOUND — rows since moved to an unregistered archive are invisible; commits counted through the END of the as-of day)"
    out = [f"DARK-WINDOW as-of {as_of} · mode {mode} · {len(lines)} desk(s) holding a live test · "
           f"{evaluated} ledger(s) evaluated · GATES {'read' if live_mode else 'NOT read in replay (no state history)'} · "
           f"liveness {'from --live: ' + ','.join(live) if live else 'NOT CHECKED (pass --live from ListAgents)'} · "
           + (f"threshold N={threshold}" if threshold is not None else "threshold N NOT SET — Will's to set (WQ row); nothing is flagged")]
    for run, d, txt in lines:
        out.append(f"  {'⏰' if (run, d, txt) in flagged else '·'} {d:9s} {txt}")
    for p, why in cannot:
        out.append(f"  CANNOT-EVALUATE {p}: {why}")
    out.append(f"DARK-WINDOW-RESULT rc={1 if flagged else 0} desks={len(lines)} flagged={len(flagged)} cannot={len(cannot)}")
    return (1 if flagged else 0), out


def selftest():
    fails = total = 0

    def chk(ok, msg):
        nonlocal fails, total
        total += 1
        fails += not ok
        print(f"  {'✓' if ok else '✗'} {msg}")

    def line(out, desk):
        return [l for l in out if re.match(r"\s+[·⏰] %s\s" % desk, l)]

    with tempfile.TemporaryDirectory() as td:
        for d in ("AAA", "BBB", "WAL", "WALTER"):
            os.makedirs(os.path.join(td, "AGENTS", d))
        reg = os.path.join(td, "LEDGERS.tsv")
        la, lb = os.path.join(td, "AGENTS", "AAA", "P.tsv"), os.path.join(td, "AGENTS", "BBB", "P.tsv")
        arch = os.path.join(td, "AGENTS", "BBB", "ARCH.tsv")
        REG = ("# r\npath\tstatus_col\tdate_col\tdate_source\toutcome_col\tstatus\n"
               "AGENTS/AAA/P.tsv\tStatus\tDate_Resolved\tCOLUMN\tOutcome\tLIVE\n"
               "AGENTS/BBB/P.tsv\tStatus\tDate_Resolved\tCOLUMN\tOutcome\tLIVE\n"
               "AGENTS/BBB/ARCH.tsv\tStatus\tDate_Resolved\tCOLUMN\tOutcome\tARCHIVE\n"
               "AGENTS/CCC/P.tsv\tStatus\tDate_Resolved\tCOLUMN\tOutcome\tLIVE\n")
        open(reg, "w").write(REG)
        open(la, "w").write("ID\tDate_Made\tStatus\tDate_Resolved\tOutcome\n"
                            "A-1\t2026-09-01\tOPEN\t\t\nA-2\t2026-09-02\tOPEN\t\t\nA-3\t2026-09-03\tOPEN\t\t\n"
                            "A-4\t2026-09-04\tOPEN\t\t\n"
                            "A-5\t2026-09-05\tMISS\t2026-09-12 (event) / 2026-09-20 (graded)\tx\n"
                            "A-6\tsoon\tOPEN\t\t\nA-7\tsoon\tHIT\t2026-09-01\tx\n"
                            "A-8\t2026-10-05\tOPEN\t\t\nA-9\t2026-09-06\tNEEDS_VERIFY\t\t\n"
                            "A-10\t2026-09-07\tOPEN\n")
        open(lb, "w").write("ID\tDate_Made\tStatus\tDate_Resolved\tOutcome\nB-1\t2026-09-01\tHIT\t2026-09-10\tx\n")
        open(arch, "w").write("ID\tDate_Made\tStatus\tDate_Resolved\tOutcome\nB-9\t2026-09-01\tOPEN\t\t\n")
        gates = os.path.join(td, "GATES.tsv")
        open(gates, "w").write("gate_id\tregistered\towner\tcondition\tconsequence_on_fire\tstate\n"
                               "G-1\t2026-09-01\tBBB/PROME\tc\tc\tLIVE — armed\n"
                               "G-2\t2026-09-01\tAAA\tc\tc\tRESOLVED 9/9\n"
                               "G-3\t2026-09-01\tWALTER\tc\tc\tLIVE\n")
        dates = {"AAA": [dt.date(2026, 9, 10)], "BBB": [dt.date(2026, 9, 28)], "WALTER": [dt.date(2026, 10, 1)]}
        cd = lambda d, s, u: [x for x in dates.get(d, []) if x <= dt.date.fromisoformat(u)]
        old = scorecard.ROOT
        globals()["ROOT"] = td
        scorecard.ROOT = td
        try:
            today = dt.date(2026, 10, 1)
            rc, out = assess(today, registry=reg, gates=gates, commit_dates=cd, today=today)
            txt = "\n".join(out)
            print("    [measure] " + out[-1])
            a = line(out, "AAA")
            chk(rc == 0 and len(a) == 1 and "21d dark" in a[0], "B1+B2: AAA is ONE line, 21d dark since 9/10")
            chk(len(a) == 1 and "5 open row(s)" in a[0],
                "B7+W2: AAA counts exactly 5 open (A-1..4 + NEEDS_VERIFY A-9); MISS A-5, HIT A-7, made-after A-8 excluded")
            chk(not line(out, "WAL") and len(line(out, "WALTER")) == 1, "W6: gate G-3 owned by WALTER never credits WAL (word match)")
            chk("G-2" not in txt and any("1 LIVE gate(s) (G-1)" in l for l in line(out, "BBB")),
                "gate-only BBB in test via LIVE G-1; RESOLVED G-2 absent from output")
            chk("B-9" not in txt, "W6: an ARCHIVE-status registry ledger is never read")
            chk("CANNOT-EVALUATE AGENTS/CCC/P.tsv: file absent" in txt and "1 row(s) with an open OR unmapped status token and no parseable made date" in txt
                and "1 row(s) whose field count != header" in txt,
                "B4+W1+W3: absent ledger, an OPEN unparseable-made row (A-6; terminal A-7 not reported), a short row — all printed")
            desk_lines = [l.split()[1] for l in out if re.match(r"\s+[·⏰] ", l)]
            chk(desk_lines[:1] == ["AAA"], f"W6: sorted longest-dark first (got {desk_lines})")
            chk("threshold N NOT SET" in out[0] and "⏰" not in txt, "B6: no threshold ⇒ rc 0, nothing flagged, N unset said")
            rc2, out2 = assess(today, threshold=21, registry=reg, gates=gates, commit_dates=cd, today=today)
            chk(rc2 == 1 and any("⏰ AAA" in l for l in out2) and not any("⏰ BBB" in l for l in out2),
                "B6+W6: --threshold 21 flags AAA at EXACTLY 21d (≥, boundary), not BBB; rc 1")
            rc3, out3 = assess(today, live=("AAA",), registry=reg, gates=gates, commit_dates=cd, today=today)
            chk(any("LIVE-UNCOMMITTED" in l for l in line(out3, "AAA")) and "NOT CHECKED" not in out3[0] and "NOT CHECKED" in out[0],
                "B5: --live AAA ⇒ LIVE-UNCOMMITTED; header names liveness source, else says NOT CHECKED")
            rc4, out4 = assess(dt.date(2026, 9, 15), registry=reg, gates=gates, commit_dates=cd, today=today)
            chk(any("6 open row(s)" in l for l in line(out4, "AAA")) and "LOWER BOUND" in out4[0],
                "X4 replay 9/15: A-5 open (GRADED 9/20 beats event 9/12) ⇒ 6 open; header says LOWER BOUND")

            def boom(d, s, u):
                raise RuntimeError("git log failed rc=128")
            rc6, out6 = assess(today, registry=reg, gates=gates, commit_dates=boom, today=today)
            chk(rc6 == 2 and "UNKNOWN" in out6[0], "W6: git failure ⇒ rc 2 UNKNOWN, never a clean list")
            open(reg, "w").write("# r\npath\tstatus_col\tdate_col\tdate_source\toutcome_col\tstatus\n"
                                 "AGENTS/CCC/P.tsv\tStatus\tDate_Resolved\tCOLUMN\tOutcome\tLIVE\n")
            rc5, out5 = assess(today, registry=reg, gates=gates, commit_dates=cd, today=today)
            chk(rc5 == 2 and "zero registered ledgers" in out5[0], "B4b: zero ledgers evaluated ⇒ rc 2")
        finally:
            scorecard.ROOT = old
            globals()["ROOT"] = old
    # B3 on the REAL filter (own_dates — the function own_commit_dates calls; result-read X5)
    log = ["2026-09-20\tWATT: x", "2026-09-21\tWATT -> PROME: y", "2026-09-22\t[cleanup] WATT: z",
           "2026-09-23\tPROME -> WATT: no", "2026-09-24\tWALTER: deliver WATT no", "2026-09-25\tWATT-11 row id no",
           "2026-09-26\tsee WATT: no"]
    got = [d.day for d in own_dates("WATT", log)]
    chk(got == [20, 21, 22], f"B3+X7: own = WATT: · WATT -> · [tag] WATT: ; never PROME -> WATT · WALTER · WATT-11 · mid-line (got {got})")
    chk(own_dates("WAL", ["2026-09-20\tWALTER: x"]) == [], "B3: WAL never matches a WALTER subject")
    print("DARK-WINDOW SELFTEST " + (f"✓ {total}/{total}" if not fails else f"✗ {fails}/{total} FAILED"))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--as-of")
    ap.add_argument("--threshold", type=int)
    ap.add_argument("--live", default="")
    ap.add_argument("--lookback", type=int, default=45)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    today = dt.datetime.now(ZoneInfo("America/New_York")).date()
    as_of = dt.date.fromisoformat(a.as_of) if a.as_of else today
    rc, out = assess(as_of, a.threshold, tuple(x for x in a.live.split(",") if x), a.lookback, today=today)
    print("\n".join(out))
    return rc


if __name__ == "__main__":
    sys.exit(main())
