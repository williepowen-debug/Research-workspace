#!/usr/bin/env python3
"""
TERRY Boot — read-only situational card for trade construction sessions.

Prints: repo state, Terry file health, open setups, and optional market snapshot.
No writes, no trade recommendations, no execution.
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
TERRY_DIR = SCRIPTS_DIR.parent
WORKSPACE = SCRIPTS_DIR.parents[2]

REQUIRED = [
    "CLAUDE.md", "README.md", "STATUS.md", "RISK_RULES.md", "RISK_SCORING.md", "TRADE_CARD_TEMPLATE.md",
    "TRADE_CARD_TEMPLATE_FIRE.md",  # both added 2026-09-01 (DAEDALUS 8/28 sweep item 2): boot step 4 + CONTRACT block name them
    "POSITION_INTAKE.md", "CHART_OPTIONS_WORKFLOW.md", "TRADE_BOOK.md", "SETUPS.tsv", "SIGNALS.tsv", "POSTMORTEMS.md",
    "scripts/boot.py", "scripts/snapshot.py", "scripts/risk_calc.py", "scripts/chain_parse.py",
    "scripts/ledger_sweep.py",
]

# Active rows older than this many days get a re-verify / retire flag at boot (anti-rot).
SIGNAL_STALE_DAYS = 21


def _tsv_rows(path):
    """
    DictReader that starts at the REAL header row, skipping any leading banner lines.

    Why this is not cosmetic: from the moment SIGNALS.tsv gained its two-clock banner
    (2026-07-30), DictReader was keying every row off the BANNER, so `r.get("status")`
    returned None for all 15 rows and the boot card printed "active rows: 0 of 15" with no
    NEXUS regime PIN at all. It looked like a quiet ledger; it was a dead one. A check that
    silently reports NOTHING outlives one that reports something wrong
    (`finding_silent_blank_evades_review`).
    """
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    hdr_i = next((i for i, l in enumerate(lines) if l.count("\t") > 1), 0)
    return list(csv.DictReader(lines[hdr_i:], delimiter="\t"))


def _tsv_shape_errors(path, label):
    """
    Column-count validation that finds the REAL header row.

    A naive `lines[0]` header assumption broke on 2026-07-30 the moment SIGNALS.tsv gained
    its two-clock banner (PAT-044): the banner is one column, so every data row read as
    "malformed" and `boot.py --selftest` had been failing ever since — a guard reporting a
    defect that did not exist, which is how a guard gets ignored. PAPER_BOOK.tsv has the
    same banner shape. Header = first line carrying more than one tab.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    hdr_i = next((i for i, l in enumerate(lines) if l.count("\t") > 1), None)
    if hdr_i is None:
        return [f"{label}: no header row found"]
    cols = len(lines[hdr_i].split("\t"))
    bad = [i + 1 for i, l in enumerate(lines) if i > hdr_i and l.strip() and len(l.split("\t")) != cols]
    return [f"{label} bad column count on lines: {bad[:8]}"] if bad else []


def sh(cmd):
    try:
        return subprocess.check_output(cmd, cwd=WORKSPACE, text=True, stderr=subprocess.STDOUT).strip()
    except subprocess.CalledProcessError as e:
        return f"ERR: {e.output.strip()}"


def file_health():
    rows = []
    for name in REQUIRED:
        p = TERRY_DIR / name
        rows.append((name, p.exists(), p.stat().st_size if p.exists() else 0))
    return rows


def setups():
    p = TERRY_DIR / "SETUPS.tsv"
    if not p.exists():
        return [], ["SETUPS.tsv missing"]
    errors = []
    rows = _tsv_rows(p)
    # SHELVED/DEAD added 2026-07-17: a card killed by its own gate is terminal. Without these,
    # TRY-FIRE-005 kept reporting as an open/actionable row after its DENY shelve (see POSTMORTEMS).
    terminal = {"CLOSED", "EXPIRED", "SUPERSEDED", "CREATED", "N/A", "SHELVED", "DEAD"}
    openish = [r for r in rows if (r.get("status") or "").upper() not in terminal and (r.get("instrument") or "") != "TERRY"]
    errors += _tsv_shape_errors(p, "SETUPS.tsv")
    return openish, errors


def _parse_date(s):
    try:
        y, m, d = (s or "").strip().split("-")
        return date(int(y), int(m), int(d))
    except Exception:
        return None


def signals():
    """Positioning/timing context ledger (WALTER INFO + other routed context). Decay-aware."""
    p = TERRY_DIR / "SIGNALS.tsv"
    if not p.exists():
        return [], ["SIGNALS.tsv missing"]
    errors = []
    rows = _tsv_rows(p)
    errors += _tsv_shape_errors(p, "SIGNALS.tsv")
    # A silent zero is the worst output a surveillance surface has: on 2026-07-30 this
    # printed "active rows: 0 of 15" for a full session and read as a quiet ledger rather
    # than a dead parser. Zero keyed rows against a non-empty file is a DEFECT, said loudly.
    if rows and not any((r.get("status") or "").strip() for r in rows):
        errors.append(
            "SIGNALS.tsv parsed but NO row has a 'status' — parser/header defect, "
            "NOT a quiet ledger. Do not read '0 active' as clean.")
    return rows, errors


def will_drops():
    """Files in Will's reserved drop zone awaiting review (gitignored — invisible to git status)."""
    d = TERRY_DIR / "inbox" / "WILL"
    if not d.exists():
        return []
    skip = {".gitkeep", "README.md"}
    return sorted(p.name for p in d.iterdir() if p.is_file() and p.name not in skip)


def unprocessed_inbox():
    """Unconsumed packets in inbox/ and inbox/<AGENT>/ — everything NOT under a processed/ dir.

    ⚠️ ADDED 2026-07-30 (DAEDALUS audit S3). This boot card read ONLY inbox/WILL/,
    so the general inbox and inbox/WALTER/ were surfaced by NEITHER the script nor
    the BOOT protocol. It cost real work the same day it was found: a WALTER
    IMMEDIATE (first Mediterranean strike of the war) sat unread through a full
    session, and three packets — one of them a supersession that made a card's
    adopted figures stale — were discovered only because PROME mentioned them in
    review. An inbox nothing reads is a delivery failure dressed as a quiet day,
    which is precisely the defect LIQUID was found to have the same morning.
    """
    root = TERRY_DIR / "inbox"
    if not root.exists():
        return []
    skip = {".gitkeep", "README.md"}
    out = []
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.name in skip:
            continue
        rel = p.relative_to(root)
        if "processed" in rel.parts or rel.parts[0] == "WILL":
            continue          # WILL has its own dedicated block below
        out.append(str(rel))
    return out


def inbox_report():
    items = unprocessed_inbox()
    if not items:
        print("\nInbox: ✓ 0 unprocessed (inbox/ + inbox/<AGENT>/, excl. WILL drop zone)")
        return
    print(f"\n🔴 Inbox: {len(items)} UNPROCESSED packet(s) — consume or file to processed/ this session")
    for name in items:
        flag = " ⚠️ IMMEDIATE" if "IMMEDIATE" in name.upper() or name.startswith("WALTER/SIG") else ""
        print(f"  📬 {name}{flag}")
    print("  → a packet nobody reads is a delivery failure, not a quiet day (DAEDALUS S3, 2026-07-30).")


def latest_status_head(lines=18):
    p = TERRY_DIR / "STATUS.md"
    if not p.exists():
        return ["STATUS.md missing"]
    return p.read_text().splitlines()[:lines]


def ledger_sweep_summary():
    """
    Surface card/ledger disagreement AT BOOT, not at closeout.

    Wired in because detection was never the gap — INVOCATION was. On 2026-07-30 the same
    drift class landed 5x in one session with the corrections already written elsewhere;
    a check nobody runs is not a check. Advisory here (never blocks a boot); the blocking
    copy is the closeout step, which exits 1.
    """
    print("\nLedger sweep (card vs ledgers · superseded values):")
    try:
        res = subprocess.run(
            [sys.executable, "AGENTS/TERRY/scripts/ledger_sweep.py"],
            capture_output=True, text=True, timeout=90, cwd=WORKSPACE,
        )
    except Exception as exc:
        print(f"  ⚠ could not run ledger_sweep.py ({exc}) — run it manually before closeout")
        return
    if res.returncode == 0:
        print("  ✓ all surfaces agree, no naked superseded values")
        return
    for line in res.stdout.splitlines():
        s = line.strip()
        if s.startswith("🔴") or s.startswith("STATE ") or s.startswith("SUPERSEDED"):
            print(f"  {s}")
        elif s.startswith("AGENTS/") or s.startswith("->"):
            print(f"      {s}")
    print("  ⚠ FIX BEFORE CLOSEOUT — full detail: python3 AGENTS/TERRY/scripts/ledger_sweep.py")


def run(args):
    print("TERRY boot card")
    print("===============")
    # ⏰ WALL CLOCK FIRST — added 2026-08-04. The PRIMARY fix for the stamp-skew
    # class, and it is prevention, not detection: on 8/4 hand-written prose stamps
    # ran +66 to +69 minutes fast across BOTH TERRY's and BRENT's surfaces, because
    # times were INFERRED rather than read. ledger_sweep check E is only a backstop
    # — it can catch a future stamp only while that time is still in the future, so
    # a stamp written at 11:11 claiming 12:20 is undetectable from 12:20 onward.
    # The cheap, total fix is having the real clock in front of you from the start.
    # Why it matters: RISK_RULES durable finding #6 grades execution against
    # SAME-TIMESTAMP marks, and that rule exists because a 21-minute gap
    # manufactured a fake execution finding. A 69-minute skew is 3x that gap.
    now = datetime.now()
    print(f"\n⏰ WALL CLOCK: {now.strftime('%Y-%m-%d %H:%M:%S %Z').strip()} ({now.strftime('%A')})")
    print("   Never hand-write a time or a weekday — copy them from this line.")

    print("\nRepo:")
    print("  status:", sh(["git", "status", "--branch", "--short"]).replace("\n", " | "))
    print("  ahead/behind:", sh(["git", "rev-list", "--left-right", "--count", "HEAD...origin/master"]))

    print("\nFile health:")
    missing = False
    for name, ok, size in file_health():
        marker = "✓" if ok and size > 0 else "✗"
        if marker == "✗":
            missing = True
        print(f"  {marker} {name:<28} {size:>6} bytes")

    openish, errors = setups()
    print("\nSetups:")
    print(f"  actionable/open rows: {len(openish)}")
    for r in openish[:8]:
        print(f"  - {r.get('setup_id')} {r.get('instrument')} {r.get('structure')} | {r.get('verdict')} | {r.get('status')} | {r.get('notes')}")
    for e in errors:
        print(f"  ⚠ {e}")

    sig_rows, sig_errors = signals()
    today = date.today()
    pins = [r for r in sig_rows if (r.get("status") or "").upper() == "PIN"]
    # Match on SHAPE, not an exact-value set. The 7/30 decay sweep introduced richer statuses
    # ("LIVE-RECONFIRMED", "SHAPE-LIVE / LEVELS-STALE", "LIVE (CLAIM-2 RETRACTED)") and the old
    # exact-match set silently dropped every one of them -- including SIG-W-20260626-026, which
    # STATUS calls "the load-bearing squeeze-risk input". A reader whose vocabulary lags the
    # file it reads fails FALSE-NEGATIVE, and quietly. Same class as the banner defect above.
    def _is_active(r):
        st = (r.get("status") or "").upper()
        return ("LIVE" in st or "DECAYING" in st) and not st.startswith("RETIRED")
    active = [r for r in sig_rows if _is_active(r)]
    unknown = [r for r in sig_rows
               if not _is_active(r)
               and (r.get("status") or "").upper() not in {"RETIRED", "PIN", ""}]
    print("\nSignals (trade-construction context — see SIGNALS.tsv):")
    for r in pins:
        d = _parse_date(r.get("as_of"))
        if not d:
            note = "  ⚠ UNSET — pull from NEXUS"
        elif (today - d).days > SIGNAL_STALE_DAYS:
            note = f"  ⚠ {(today - d).days}d old — refresh from NEXUS"
        else:
            note = ""
        print(f"  ★ PIN {r.get('cluster')} [{r.get('source')}]: {r.get('key_level')}{note}")
    print(f"  active rows: {len(active)} of {len(sig_rows)}")
    for r in active:
        st = (r.get("status") or "").upper()
        d = _parse_date(r.get("as_of"))
        age, flag = "", ""
        if d:
            days = (today - d).days
            age = f"{days}d"
            # 2026-09-01 (DAEDALUS 8/28 wiring-sweep ⑳): the STALE flag gated on an EXACT set
            # {"LIVE","LIVE-WEAK"} / "DECAYING" while _is_active() above was widened 7/30 to a
            # SUBSTRING test -- so a row could be counted active and never earn its retirement
            # warning (live 8/28: 3 of 12 active rows at 65d/36d/39d printed with NO flag, one of
            # them literally labelled LEVELS-STALE). Split-brain fix: same substring test here.
            if "DECAYING" in st and days > SIGNAL_STALE_DAYS:
                flag = "  ⚠ decaying >21d — reconfirm before use"
            elif "LIVE" in st and days > SIGNAL_STALE_DAYS:
                flag = "  ⚠ STALE >21d — re-verify or retire"
        print(f"  - [{r.get('source')}] {r.get('signal_id')} [{st}] {r.get('bears_on')} | {r.get('key_level')} | as_of {r.get('as_of')} ({age}){flag}")
    for r in unknown:
        print(f"  ? [{r.get('source')}] {r.get('signal_id')} [{(r.get('status') or '').upper()}] "
              f"— status not recognised as active/retired; triage it rather than assume quiet")
    for e in sig_errors:
        print(f"  ⚠ {e}")

    inbox_report()

    drops = will_drops()
    print(f"\nWill drop zone (inbox/WILL/): {len(drops)} file(s) awaiting review")
    for name in drops:
        print(f"  📥 {name}")
    if drops:
        print("  → run the day-trading review loop (daytrading/) or position triage on these.")

    print("\nSTATUS head:")
    for line in latest_status_head():
        print("  " + line)

    ledger_sweep_summary()

    print("\nReminder:")
    print("  Terry proposes only. Will approves/rejects. No execution.")
    print("  Use POSITION_INTAKE.md for existing positions and TRADE_CARD_TEMPLATE.md for proposals.")

    if args.snapshot:
        cmd = [sys.executable, str(SCRIPTS_DIR / "snapshot.py"), *args.snapshot]
        if args.benchmark:
            cmd += ["--benchmark", args.benchmark]
        if args.days:
            cmd += ["--days", str(args.days)]
        if args.stress:
            cmd += ["--stress"]
        print("\n--- snapshot ---")
        print(sh(cmd))

    return 1 if missing or errors else 0


def selftest():
    missing = [name for name, ok, size in file_health() if not ok or size <= 0]
    if missing:
        print(f"SELFTEST FAIL missing/empty: {missing}")
        return 1
    _, errors = setups()
    _, sig_errors = signals()
    errors = errors + sig_errors
    if errors:
        print(f"SELFTEST FAIL: {errors}")
        return 1
    print("boot.py SELFTEST: PASS")
    return 0


def main():
    ap = argparse.ArgumentParser(description="TERRY read-only boot card")
    ap.add_argument("--snapshot", nargs="*", help="Optional tickers to pass to snapshot.py, e.g. --snapshot WAL KRE")
    ap.add_argument("--benchmark", help="Benchmark for optional snapshot")
    ap.add_argument("--days", type=int, default=30, help="Lookback days for optional snapshot")
    ap.add_argument("--stress", action="store_true", help="Include stress backdrop in optional snapshot")
    ap.add_argument("--selftest", action="store_true", help="Validate Terry files and SETUPS.tsv")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
