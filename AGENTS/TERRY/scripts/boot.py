#!/usr/bin/env python3
"""
TERRY Boot — read-only situational card for trade construction sessions.

Prints: repo state, Terry file health, open setups, and optional market snapshot.
No writes, no trade recommendations, no execution.
"""

from __future__ import annotations

import argparse
import re as _re
import csv
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
TERRY_DIR = SCRIPTS_DIR.parent
REPO_ROOT = TERRY_DIR.parent.parent          # AGENTS/TERRY -> AGENTS -> repo root
WORKSPACE = SCRIPTS_DIR.parents[2]

REQUIRED = [
    "CLAUDE.md", "README.md", "STATUS.md", "RISK_RULES.md", "RISK_SCORING.md", "TRADE_CARD_TEMPLATE.md",
    "TRADE_CARD_TEMPLATE_FIRE.md",  # both added 2026-09-01 (DAEDALUS 8/28 sweep item 2): boot step 4 + CONTRACT block name them
    "POSITION_INTAKE.md", "CHART_OPTIONS_WORKFLOW.md", "TRADE_BOOK.md", "SETUPS.tsv", "SIGNALS.tsv", "POSTMORTEMS.md",
    "scripts/boot.py", "scripts/snapshot.py", "scripts/risk_calc.py", "scripts/chain_parse.py",
    "scripts/ledger_sweep.py",
]

# Active rows older than this many days get a re-verify / retire flag at boot (anti-rot).
SIGNAL_STALE_DAYS = 21   # fallback ONLY — the tightest bar, used when a row declares no decay class

# SIGNALS.tsv line 3 declares its own bars: "Decay bars: short=21d med=45d durable=90d,
# measured against as_of (NOT date_recv)". Until 2026-09-03 boot.py ignored that column and
# applied 21d to EVERY row, so a `durable` row at 22d printed "⚠ STALE >21d" against a bar of
# 90. Measured on the live ledger the day of the fix: 5 rows flagged, only ONE (23d vs a short
# bar of 21) was actually over — a 4-in-5 false-positive rate on a line whose only job is to be
# believed. ⚠️ That is how an advisory dies: the desk's own ledger_sweep notes record the same
# lesson ("a false positive here buys alert fatigue"). Fallback is the TIGHTEST bar, so a row
# with a missing or unknown decay class still warns rather than going quiet.
# `none` (added 2026-09-11, DEWEY packet 2026-09-10) is a DECLARED absence of a clock, for a
# row whose claim is a METHOD rule — one about what data is REACHABLE, not about the tape.
# No tape can age it. DEW-MECH-SELL claim (1) sat on a 45d bar and minted a false STALE flag
# that cost a PROME routing hop, a TERRY sweep and a DEWEY boot slot to conclude that a rule
# about what is purchasable had not changed in 52 days. That is a ROW-SHAPE defect, not a
# sweep defect. ⛔ THIS IS NOT A WIDENED GUARD: the guard flags rows whose EVIDENCE has aged,
# and a method rule has no evidence that ages. It is opt-in per row, it must be written
# deliberately, and it is the ONLY exempt value — anything unrecognised still falls back to
# the TIGHTEST bar below, so a typo fails LOUD rather than silently buying an exemption.
SIGNAL_DECAY_BARS = {"short": 21, "med": 45, "durable": 90, "none": None}

# Status markers that mean "deliberately not active — a human triaged this and closed it."
# Matched as SUBSTRINGS so a row may carry its ruling inline ("RETIRED (terminal, Will-ruled
# 2026-08-18)") without falling out of the vocabulary. Anything NOT matching still prints "?".
_TERMINAL_STATUS_MARKERS = ("RETIRED", "RETRACTED", "HISTORICAL-PRECEDENT", "LAPSED", "CLOSED")


def _signal_bar(row):
    """Decay bar in days, or None for an explicit `decay=none` METHOD row.

    Unknown/missing -> the TIGHTEST bar (never silence). Only the literal string
    `none` earns the no-clock exemption; `nonsense` does not.
    """
    raw = (row.get("decay") or "").strip().lower()
    if raw in SIGNAL_DECAY_BARS:
        return SIGNAL_DECAY_BARS[raw]
    return SIGNAL_STALE_DAYS


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


def _is_terminal_status(status: str | None, terminal: set[str]) -> bool:
    """True if a SETUPS.tsv status claims a terminal state.

    Exact whole-string match FIRST (preserves every pre-2026-09-03 catch, incl. "N/A"),
    then the LEADING token. Leading only, never a scan of the whole cell: a status that
    discusses another card ("005 is DEAD-terminal per its own rule") must not donate that
    card's state here — the same cross-card leakage ledger_sweep.py records for its own
    vocabulary.
    """
    raw = (status or "").upper().strip()
    if raw in terminal:
        return True
    stripped = re.sub(r"^[^A-Z0-9]+", "", raw)   # drop leading emoji/markdown: "🔴 DEAD — ..."
    head = re.split(r"[\s/]+", stripped, maxsplit=1)[0] if stripped else ""
    return head.strip("-\u2014,.:;()*_") in terminal


def setups():
    p = TERRY_DIR / "SETUPS.tsv"
    if not p.exists():
        return [], ["SETUPS.tsv missing"]
    errors = []
    rows = _tsv_rows(p)
    # SHELVED/DEAD added 2026-07-17: a card killed by its own gate is terminal. Without these,
    # TRY-FIRE-005 kept reporting as an open/actionable row after its DENY shelve (see POSTMORTEMS).
    #
    # 🔴 FIXED 2026-09-03 (Will-approved) — THAT 7/17 FIX NEVER WORKED, AND NOTHING SAID SO FOR 48 DAYS.
    # The test was `status.upper() not in terminal`, an EXACT WHOLE-STRING match, so it only ever
    # fired on a status that was *nothing but* the bare word. Real rows are written
    # "DEAD / TERMINAL / ARCHIVED — $0 at risk" and "CLOSED — REALIZED -$111.60", which match
    # nothing. ★ TRY-FIRE-005 — the exact row SHELVED/DEAD were added FOR — kept reporting as
    # actionable the entire time. Measured on the live ledger the day of the fix: boot printed
    # "actionable/open rows: 20" when only 8 rows were genuinely open.
    # ⚠️ The failure direction is what made it invisible: over-reporting open work makes the desk
    #    look BUSY, never broken, so nobody reads the number as a defect.
    # ⇒ Now ALSO matched on the LEADING state token. Strictly ADDITIVE — the exact-string test is
    #   kept first, so this can only ever catch MORE, never fewer (that also preserves "N/A",
    #   whose leading token is "N").
    # ⛔ RETIRED and LAPSED added; DORMANT, NO-BUILD and "NO AT THIS PRICE" DELIBERATELY NOT.
    #   A false TERMINAL here HIDES A LIVE CARD from the boot card, which is the dangerous
    #   direction — worse than showing a dead one. Those three are revivable by construction
    #   (TRY-FIRE-002 is DORMANT with a dated re-examination), so they stay visible on purpose.
    terminal = {"CLOSED", "EXPIRED", "SUPERSEDED", "CREATED", "N/A", "SHELVED", "DEAD",
                "RETIRED", "LAPSED"}
    openish = [r for r in rows
               if not _is_terminal_status(r.get("status"), terminal)
               and (r.get("instrument") or "") != "TERRY"]
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

    # 2026-09-11: the companion test below was an EXACT-set membership check
    # ({"RETIRED","PIN",""}) sitting directly beneath an _is_active() that had already been
    # widened to SUBSTRING on 7/30 for exactly this reason -- a split brain, half-fixed.
    # Consequence: any row whose status someone described BETTER than the vocabulary
    # ("RETIRED (terminal, Will-ruled ...)", "RETRACTED", "HISTORICAL-PRECEDENT") fell
    # through to the "? status not recognised" line and nagged FOREVER. That is the
    # alert-fatigue death this file's own comments keep warning about, and it is the
    # memory-index class `finding_status_token_membership_test_desupervises_improved_rows`:
    # a guard scoped by TOKEN drops the rows someone labelled more precisely.
    # ⛔ NOT a widened guard: an unrecognised status STILL prints "?". Only these explicit
    # TERMINAL markers are quiet, and each one means "a human already triaged this row".
    def _is_deliberately_quiet(r):
        st = (r.get("status") or "").upper().strip()
        if st == "" or st == "PIN":
            return True
        return any(m in st for m in _TERMINAL_STATUS_MARKERS)
    active = [r for r in sig_rows if _is_active(r)]
    unknown = [r for r in sig_rows
               if not _is_active(r) and not _is_deliberately_quiet(r)]
    print("\nSignals (trade-construction context — see SIGNALS.tsv):")
    for r in pins:
        d = _parse_date(r.get("as_of"))
        if not d:
            note = "  ⚠ UNSET — pull from NEXUS"
        elif (today - d).days > _signal_bar(r):
            note = f"  ⚠ {(today - d).days}d old vs its {r.get('decay') or 'short'} bar ({_signal_bar(r)}d) — refresh from NEXUS"
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
            bar = _signal_bar(r)
            if bar is None:
                # Declared METHOD row: no clock, by declaration. Printed, never silent —
                # an exemption nobody can see is indistinguishable from a guard that broke.
                flag = "  · decay=none (METHOD) — no clock by declaration; re-verify only if its PREMISE changes"
            elif "DECAYING" in st and days > bar:
                flag = f"  ⚠ decaying {days}d > its {r.get('decay') or 'short'} bar ({bar}d) — reconfirm before use"
            elif "LIVE" in st and days > bar:
                flag = f"  ⚠ STALE {days}d > its {r.get('decay') or 'short'} bar ({bar}d) — re-verify or retire"
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

    # ---- BOARD consumption (§3.5 exempt-desk warrant) --------------------
    board_unlogged = []
    try:
        board_unlogged, _addr, _logd = board_gap(REPO_ROOT / "BOARD", TERRY_DIR, date.today())
        print("\nBOARD (WALTER) — §3.5 EXEMPT desk, this step IS the pull record:")
        print(f"  action-line signals addressed to TERRY: {_addr} · logged in board_log.tsv: {_logd}")
        if board_unlogged:
            print(f"  \U0001F534 {len(board_unlogged)} UNLOGGED action-line signal(s) \u2265{BOARD_MIN_AGE_DAYS}d old:")
            for sid, d in board_unlogged[:12]:
                print(f"     {sid}  [{d}]  {(date.today() - d).days}d")
            if len(board_unlogged) > 12:
                print(f"     … +{len(board_unlogged) - 12} more")
            print("  \u2192 log EACH in board_log.tsv (acted/noted/superseded/info-only). "
                  "\u26d4 Do NOT log a row you have not read — a false consumption record is worse than a gap.")
        else:
            print("  \u2713 every action-line signal is logged, or younger than the floor")
    except Exception as e:                      # a broken BOARD must not break the boot card
        print(f"\nBOARD (WALTER): \u26a0 step could not run ({e}) — treat as UNKNOWN, not PASS")

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

    return 1 if missing or errors or board_unlogged else 0


_TERMINAL_CASES: list[tuple[str, bool]] = [
    # ★ PERMANENT REGRESSIONS — the verbatim live strings the pre-2026-09-03 exact-match
    #   filter reported as OPEN for 48 days. Case 1 is TRY-FIRE-005, the row the 7/17 fix
    #   was written for and never caught.
    ("DEAD / TERMINAL / ARCHIVED \u2014 $0 at risk, never entered", True),
    ("CLOSED \u2014 REALIZED -$111.60 / -38.8%", True),
    ("RETIRED (terminal, Will-ruled 2026-08-18) \u2014 never armed", True),
    ("DEAD (terminal) 2026-08-13 \u2014 arm expired unfired", True),
    ("LAPSED", True),
    ("N/A", True),                       # exact-match preservation: leading token is "N"
    ("\U0001f534 DEAD \u2014 terminal", True),   # emoji/markdown prefix
    # ⛔ MUST STAY OPEN. A false terminal HIDES a live card from the boot card, which is the
    #    dangerous direction; these four pin that.
    ("FIRED/ACTIVE", False),
    ("FIRED / LIVE - filled 9/2 @ $2.20 x1 in ROBINHOOD", False),
    ("STAGED - Will APPROVED (decision) WQ-168 12:45 ET", False),
    ("CONDITIONAL / DECISION-READY / $0 new risk", False),
    # ⛔ DELIBERATELY NOT TERMINAL \u2014 revivable by construction, kept visible on purpose.
    ("HELD DORMANT \u2014 adjudicated, owner reassigned", False),
    ("NO-BUILD / LIQUIDITY GATE FAILED / $0 at risk", False),
    ("NO AT THIS PRICE / SCOPE-DELIVERED \u2014 unarmed", False),
    # substring guard: a terminal word must be the whole leading TOKEN, never a prefix
    ("DEADLINE 9/30 for the exit", False),
    ("", False),
]


_BAR_CASES: list[tuple[str, "int | None"]] = [
    ("short", 21), ("med", 45), ("durable", 90),
    ("DURABLE", 90),          # case-insensitive
    (" med ", 45),            # whitespace
    ("", 21), ("bogus", 21),  # unknown/missing -> TIGHTEST bar, never silence
    ("none", None), ("NONE", None), (" none ", None),   # declared METHOD row: no clock
    ("nonsense", 21),         # ⚠ near-miss must NOT inherit the exemption
]


def _selftest_bars() -> list[str]:
    bad = []
    for decay, want in _BAR_CASES:
        got = _signal_bar({"decay": decay})
        if got != want:
            bad.append(f"_signal_bar(decay={decay!r}) = {got}, want {want}")
    # the live regression: a durable PIN at 22d must NOT flag; a short row at 23d must.
    if 22 > _signal_bar({"decay": "durable"}):
        bad.append("durable row at 22d would flag — the 4-of-5 false-positive bug is back")
    if 23 <= _signal_bar({"decay": "short"}):
        bad.append("short row at 23d would NOT flag — real staleness missed")
    # 2026-09-11: a `none` row must never flag at ANY age, and the exemption must not leak
    # to a near-miss spelling. Writing `none` into the column WITHOUT this code change was
    # the trap: the old fallback mapped it to 21d, so the "fix" would have made the false
    # STALE flag FIRE SOONER while reading as if it had been solved.
    if _signal_bar({"decay": "none"}) is not None:
        bad.append("decay=none no longer exempt — false STALE flags on METHOD rows are back")
    if _signal_bar({"decay": "nonsense"}) != 21:
        bad.append("a near-miss decay value inherited the none-exemption — fail-loud default broken")
    return bad


# ---------------------------------------------------------------------------
# BOARD consumption step (added 2026-09-11, PROME packet 4b35fa523 / commit of the
# §3.5 exempt-desk finding). TERRY is a §3.5 EXEMPT desk — spec v0.21, 2026-08-26,
# exempt BY FALSIFIER: WALTER writes this desk no handoffs and no delivery rows, so
# nothing PUSHES a BOARD signal here. The exemption's whole warrant is that TERRY
# PULLS at its own cadence. ⛔ Until today nothing recorded the pull: board_log.tsv
# held 3 inbox rows and ZERO SIG-W ids, and this file had no BOARD step at all.
#
# ★ THE MEASURED COST OF THAT GAP, found while back-filling: of the 20 action-line
# signals since 8/11, the 15 dated 8/22 or EARLIER all arrived in inbox/WALTER/
# processed/ — and ALL FIVE dated 8/28 or LATER reached this desk by no route at
# all. The boundary is the 8/26 exemption date, with ZERO exceptions. The exemption
# did not degrade delivery gradually; it stopped it on its effective date.
#
# ⚠️ ACTED-AND-UNLOGGED IS THE FAILURE SHAPE THIS CANNOT SEE FROM OUTSIDE: a signal
# consumed on a card and one never read are identical to a third party until a row
# exists. This step makes the pull auditable from INSIDE. Logic copied from
# PROME/tools/exempt_gap.py (the reference), deliberately NOT imported — this desk's
# boot must not break when another desk refactors its tools.
SIG_ID_RE = _re.compile(r"SIG-W-\d{8}-\d{3}")
BOARD_MIN_AGE_DAYS = 2   # a signal filed today is not yet a drain failure
BOARD_LEDGER_GLOBS = ("board_log.tsv", "archive/board_log*.tsv")


def _board_action_ids(board_dir, desk="TERRY"):
    """{signal_id: date} for every BOARD signal whose `action:` line names the desk.

    info-cc lines are NOT the exemption's risk and are deliberately excluded — the
    same scoping the reference uses.
    """
    out = {}
    if not board_dir.is_dir():
        return out
    for f in sorted(board_dir.glob("SIG-W-*.md")):
        try:
            head = f.read_text(encoding="utf-8", errors="replace")[:1200]
        except OSError:
            continue
        m = _re.search(r"^action:\s*\[(.*?)\]", head, _re.M | _re.S)
        if not m:
            continue
        names = {x.strip().strip("'\"").upper() for x in m.group(1).split(",") if x.strip()}
        if desk.upper() not in names:
            continue
        # ⚠️ THE BOARD CARRIES TWO FRONT-MATTER CONVENTIONS. Measured 2026-09-11 over
        # 939 files: 835 use `signal_id:` and 104 (11%) use bare `id:`. The v1 of this
        # parser matched only `signal_id:` and SILENTLY DROPPED all 104 — it did not
        # error, they simply never appeared in the addressed set, so an unlogged one
        # could never be flagged. ⛔ FAIL-OPEN, the worst direction for a guard whose
        # whole job is to notice absence. Caught only because the addressed count came
        # back 19 against PROME's 20 and the difference was chased instead of shrugged
        # off (the one that differed: SIG-W-20260820-003, `id:`-form).
        # `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`
        sid = _re.search(r"^(?:signal_id|id):\s*(SIG-W-\d{8}-\d{3})", head, _re.M)
        if not sid:                       # last resort: the filename itself
            sid = _re.search(r"(SIG-W-\d{8}-\d{3})", f.name)
        d = _re.search(r"^date:\s*(\d{4})-(\d{2})-(\d{2})", head, _re.M)
        if sid and d:
            out[sid.group(1)] = date(int(d.group(1)), int(d.group(2)), int(d.group(3)))
    return out


def _board_logged_ids(terry_dir):
    ids = set()
    for g in BOARD_LEDGER_GLOBS:
        for f in sorted(terry_dir.glob(g)):
            try:
                ids |= set(SIG_ID_RE.findall(f.read_text(encoding="utf-8", errors="replace")))
            except OSError:
                continue
    return ids


def board_gap(board_dir, terry_dir, today):
    """(unlogged_aged, addressed_total, logged_total) — the ID-diff, as a pure function."""
    addressed = _board_action_ids(board_dir)
    logged = _board_logged_ids(terry_dir)
    aged = sorted((sid, d) for sid, d in addressed.items()
                  if sid not in logged and (today - d).days >= BOARD_MIN_AGE_DAYS)
    return aged, len(addressed), len(logged)


_QUIET_CASES: list[tuple[str, bool]] = [
    ("RETIRED", True), ("PIN", True), ("", True),
    ("RETIRED (terminal, Will-ruled 2026-08-18) — never armed", True),  # the described-better case
    ("RETRACTED (terminal — never cite)", True),                        # DEW-MECH-SELL-C2
    ("HISTORICAL-PRECEDENT (closed episode — no further bar)", True),   # DEW-MECH-SELL-C3
    ("LAPSED", True), ("CLOSED + evaluated", True),
    ("SUPERSEDED", False),        # ⚠ genuinely untriaged -> must still print "?"
    ("WAITING ON BOND", False),
    ("nonsense", False),
]


_BOARD_FM_CASES = [
    # (front-matter text, expect_found) — BOTH id conventions must parse, and a
    # signal that does NOT name TERRY on the action line must NOT be picked up.
    ("---\nsignal_id: SIG-W-20260819-015\ndate: 2026-08-19\naction: [TERRY, BOND]\ninfo: [RED]\n", True),
    ("---\nid: SIG-W-20260820-003\ndate: 2026-08-20\naction: [BOND, TERRY]\ninfo: [HENRY]\n", True),   # the 9/11 regression
    ("---\nsignal_id: SIG-W-20260911-004\ndate: 2026-09-11\naction: []\ninfo: [HAWK, NEXUS]\n", False),
    ("---\nid: SIG-W-20260901-009\ndate: 2026-09-01\naction: [BROCK]\ninfo: [TERRY]\n", False),        # info-cc is NOT action
    # ⚠️ THE CASE ABOVE DOES NOT ACTUALLY FALSIFY an action|info regex: `re.search`
    # returns the EARLIEST match and `action:` precedes `info:`, so a broken pattern
    # still reads the action line and still gets the right answer. Verified by
    # injection 2026-09-11 — widening the regex to `(?:action|info):` left the suite
    # PASSING. The case below has NO action line at all, so only a pattern that
    # wrongly accepts `info:` can find TERRY in it. THAT is the falsifying fixture.
    # `[[finding_test_the_guard_not_just_the_guarded]]`
    ("---\nsignal_id: SIG-W-20260902-001\ndate: 2026-09-02\ninfo: [TERRY, RED]\n", False),
]


def _selftest_board() -> list[str]:
    """The BOARD step must see BOTH front-matter conventions and must not treat an
    info-cc as an action line. v1 matched only `signal_id:` and silently dropped 104
    of 939 live files — a guard blind to 11% of its input, failing OPEN."""
    import tempfile as _tf
    bad = []
    with _tf.TemporaryDirectory() as td:
        bd = Path(td) / "BOARD"; bd.mkdir()
        want = set()
        for i, (fm, expect) in enumerate(_BOARD_FM_CASES):
            m = _re.search(r"SIG-W-\d{8}-\d{3}", fm)
            (bd / f"{m.group(0)}-case{i}.md").write_text(fm, encoding="utf-8")
            if expect:
                want.add(m.group(0))
        got = set(_board_action_ids(bd).keys())
        if got != want:
            bad.append(f"_board_action_ids: got {sorted(got)}, want {sorted(want)}")
        # the ID-diff itself: an addressed-but-unlogged signal must surface
        td2 = Path(td) / "desk"; td2.mkdir()
        (td2 / "board_log.tsv").write_text("ts\tsignal_id\tdisposition\n"
                                           "x\tSIG-W-20260819-015\tacted\n", encoding="utf-8")
        aged, addressed, logged = board_gap(bd, td2, date(2026, 9, 11))
        ids = [a for a, _ in aged]
        if "SIG-W-20260820-003" not in ids:
            bad.append("board_gap missed an addressed-but-unlogged `id:`-form signal")
        if "SIG-W-20260819-015" in ids:
            bad.append("board_gap flagged a signal that IS logged")
        if addressed != 2:
            bad.append(f"board_gap addressed={addressed}, want 2")
    return bad


def _selftest_quiet() -> list[str]:
    """The quiet-status vocabulary must cover described-better rows WITHOUT swallowing
    a status nobody has triaged. Both directions are failures."""
    bad = []
    # rebuild the closure-local predicate against the module-level marker set
    def quiet(st):
        u = (st or "").upper().strip()
        if u == "" or u == "PIN":
            return True
        return any(m in u for m in _TERMINAL_STATUS_MARKERS)
    for st, want in _QUIET_CASES:
        if quiet(st) != want:
            bad.append(f"_is_deliberately_quiet({st!r}) = {not want}, want {want}")
    return bad


def _selftest_terminal() -> list[str]:
    terminal = {"CLOSED", "EXPIRED", "SUPERSEDED", "CREATED", "N/A", "SHELVED", "DEAD",
                "RETIRED", "LAPSED"}
    bad = []
    for text, want in _TERMINAL_CASES:
        got = _is_terminal_status(text, terminal)
        if got != want:
            bad.append(f"_is_terminal_status({text!r}) = {got}, want {want}")
    return bad


def selftest():
    missing = [name for name, ok, size in file_health() if not ok or size <= 0]
    if missing:
        print(f"SELFTEST FAIL missing/empty: {missing}")
        return 1
    _, errors = setups()
    _, sig_errors = signals()
    errors = errors + sig_errors + _selftest_terminal() + _selftest_bars() + _selftest_quiet() + _selftest_board()
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
