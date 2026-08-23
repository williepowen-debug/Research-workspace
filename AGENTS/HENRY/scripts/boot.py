#!/usr/bin/env python3
"""
HENRY Boot Kit (v1) — consolidated boot brief.

Read-only by design: it DISPLAYS live state, it does NOT write STATUS.md
(writing the dashboard back is the analyst's job at write-back). NOTE: the old
refresh_status.py was RETIRED 2026-06-15 to archive/retired/ (stale writer —
hardcoded narrative; do not resurrect — see MAINTENANCE.md).

Four components (all from existing materials):
  (a) LIVE TAPE       — fetch.py real-time/last quotes (not a pre-open period=1d bar)
  (b) GAMMA           — gamma_flip.py free-tier SPX dealer-gamma flip / net GEX / walls (14d, fast)
  (c) CREDIT          — credit_monitor.py (HY/CCC/BB + CCC-BB bifurcation)
  (d) PREDICTIONS-DUE — scan workbook/PREDICTIONS.tsv for OPEN/ACTIVE rows due ≤ today
  (e) LEDGER STALENESS— mtime alert on live workbook ledgers
  (f) INBOX TRIAGE    — filenames only; flags date/gate hits. NOT processing.
  (g) STALE CONSUMERS — consumer_check.py off workbook/PUBLISHED.tsv

Usage:
  .venv/bin/python3 AGENTS/HENRY/scripts/boot.py
  .venv/bin/python3 AGENTS/HENRY/scripts/boot.py --quick     # skip credit + gamma (slower external pulls)
  .venv/bin/python3 AGENTS/HENRY/scripts/boot.py --verbose   # full credit_monitor output
  .venv/bin/python3 AGENTS/HENRY/scripts/boot.py --selftest  # assert the due-scan logic fires

Note (per Prome/ORC 6/15): boot.py does NOT prevent spawn-cadence staleness gaps —
no kit runs while HENRY is asleep. Its payoff is (1) a clean live pull that can't be
mislabeled a session-boundary stale snapshot, and (2) the predictions-due scan.
"""

import json
import os
import re
import subprocess
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
HENRY_DIR = SCRIPTS_DIR.parent
WORKSPACE = HENRY_DIR.parent.parent  # Research-workspace/
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"
FETCH_PY = WORKSPACE / "FORGE" / "tools" / "market-data" / "fetch.py"
CREDIT_MONITOR = SCRIPTS_DIR / "credit_monitor.py"
PREDICTIONS_TSV = HENRY_DIR / "workbook" / "PREDICTIONS.tsv"

# Full HENRY tape: index/vol/rates/banks/alts/energy/fx
TICKERS = [
    "^GSPC", "^VIX", "^VIX9D", "^VIX3M", "^VVIX", "^SKEW",
    "^TNX", "TLT", "KRE", "WAL", "APO", "ARES", "BZ=F", "JPY=X",
]
LABEL = {
    "^GSPC": "SPX", "^VIX": "VIX", "^VIX9D": "VIX9D", "^VIX3M": "VIX3M",
    "^VVIX": "VVIX", "^SKEW": "SKEW", "^TNX": "10Y", "TLT": "TLT",
    "KRE": "KRE", "WAL": "WAL", "APO": "APO", "ARES": "ARES",
    "BZ=F": "Brent", "JPY=X": "USD/JPY",
}

# Statuses that mean "still live / resolvable"
OPEN_STATUSES = {"ACTIVE", "OPEN"}


def _py():
    return str(VENV_PYTHON) if VENV_PYTHON.exists() else sys.executable


def run(cmd, timeout=90):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=timeout, cwd=str(WORKSPACE))
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return 1, "", f"TIMEOUT after {timeout}s"
    except Exception as e:  # noqa: BLE001
        return 1, "", str(e)


# ---------------------------------------------------------------- (a) LIVE TAPE
def live_tape():
    print(f"\n{'─'*64}\n  (a) LIVE TAPE   ·   pulled {datetime.now():%Y-%m-%d %H:%M:%S} local")
    print(f"{'─'*64}")
    code, out, err = run([_py(), str(FETCH_PY), "price"] + TICKERS + ["--json"])
    if code != 0:
        print(f"  ⚠️  fetch.py failed: {err[:300]}")
        return
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        print(f"  ⚠️  could not parse fetch.py output:\n{out[:300]}")
        return
    for t in TICKERS:
        info = data.get(t, {})
        if not info or "error" in info:
            print(f"  {LABEL.get(t, t):<8} {'—':>12}   (no quote)")
            continue
        px = info.get("price")
        chg = info.get("change_pct", info.get("changePercent"))
        chg_s = f"{chg:+.2f}%" if isinstance(chg, (int, float)) else ""
        try:
            px_s = f"{float(px):,.2f}"
        except (TypeError, ValueError):
            px_s = str(px)
        print(f"  {LABEL.get(t, t):<8} {px_s:>12}   {chg_s}")
    print("\n  ⚠️  real-time/last quote — stamp THIS timestamp in STATUS, not 'close'.")


# -------------------------------------------------------------------- (b) GAMMA
def gamma(asof=None):
    print(f"\n{'─'*64}\n  (b) GAMMA  ·  SPX dealer-gamma flip (gamma_flip.py, free-tier)\n{'─'*64}")
    try:
        if str(SCRIPTS_DIR) not in sys.path:
            sys.path.insert(0, str(SCRIPTS_DIR))
        from gamma_flip import compute_gamma_flip
        r = compute_gamma_flip(asof=asof, horizon=14)  # boot-fast; flip stable vs 35d (7,521 vs 7,522)
    except Exception as e:  # noqa: BLE001
        print(f"  ⚠️  gamma_flip failed: {str(e)[:200]}")
        return
    if "error" in r:
        print(f"  ⚠️  {r['error']}")
        return
    spot, flip, g0 = r["spot"], r["flip"], r["gex_at_spot"]
    if flip:
        rel = spot - flip
        side = "BELOW → NEG-gamma, dealers AMPLIFY" if rel < 0 else "ABOVE → POS-gamma, dealers dampen"
        print(f"  SPX {spot:,.2f} · flip ~{flip:,.0f} · spot {rel:+,.0f}pts {side}")
    else:
        print(f"  SPX {spot:,.2f} · no flip in ±10% band · regime {r['regime']}")
    pw, cw = r["put_wall"], r["call_wall"]
    pw_note = " (SPX THROUGH it)" if pw and spot < pw else ""
    # SFG sweep 2026-08-17 (DAEDALUS): print the SOURCE token. A silent CBOE->yfinance
    # demotion used to render byte-identical to a healthy read, and yfinance has zeroed
    # openInterest on 97% of the ^SPX chain before (7/23). This value auto-publishes to
    # workbook/PUBLISHED.tsv, which other agents' gates consume.
    src = r.get("source", "?")
    src_flag = "" if src == "cboe" else "  ⚠️ NON-PRIMARY SOURCE"
    print(f"  Net GEX {g0/1e9:+.1f}B/1% · put wall {pw:,.0f}{pw_note} · call wall {cw:,.0f}"
          f"   [{r['horizon']}d, {r['n_contracts']} contracts, src={src}]{src_flag}")
    # ACTION 2: pct-of-healthy floor. MIN_CONTRACTS=400 vs a healthy ~6,000 lets a 90%
    # degraded chain print a confident flip. Warn (never suppress) below 25% of healthy.
    # ⚠️ CALIBRATION CAVEAT, stated rather than hidden: 6,000 is DAEDALUS's figure for a
    # healthy chain and matches the 35d pull (7,438 on 2026-08-23). The 14d pull is
    # naturally thinner (3,795 same day), so ONE constant across both horizons
    # UNDER-warns at 14d. It only ever warns, never suppresses, so the failure is a
    # missed alert, not a blocked read. Re-base per-horizon when there is a base rate.
    HEALTHY_CONTRACTS = 6000
    n = r.get("n_contracts") or 0
    if n < 0.25 * HEALTHY_CONTRACTS:
        print(f"  ⚠️  THIN CHAIN: {n:,} contracts = {n/HEALTHY_CONTRACTS:.0%} of a healthy "
              f"~{HEALTHY_CONTRACTS:,} chain — flip/sign degraded, do NOT publish walls")
    print("  (free-tier: sign+flip robust, $B assumption-dependent · gamma_flip.py --days 35 for the definitive read)")


# ------------------------------------------------------------------- (c) CREDIT
def credit(verbose=False):
    print(f"\n{'─'*64}\n  (c) CREDIT  ·  FRED bifurcation (credit_monitor.py)\n{'─'*64}")
    if not CREDIT_MONITOR.exists():
        print("  ⚠️  credit_monitor.py not found")
        return
    code, out, err = run([_py(), str(CREDIT_MONITOR)])
    # SFG sweep 2026-08-17: `and not out` let a PARTIAL-output failure pass silently on a
    # leg that feeds a kill line. A non-zero exit is a failure whether or not it printed.
    if code != 0:
        print(f"  ⚠️  credit_monitor exit {code}: {err[:300]}")
        if not out:
            return
    if verbose:
        print(out)
    else:
        for line in out.splitlines():
            if any(m in line for m in ("BB", "HY", "CCC", "GAP", "HYG", "flag", "✓",
                                       "\u26a0", "\u26a0\ufe0f", "ERROR", "FLAGS",
                                       "🔴", "🟠", "🟡")):
                print(f"  {line.strip()}")


# ----------------------------------------------------- (d) PREDICTIONS-DUE SCAN
def _parse_deadline(resdate):
    """Return ('rolling'|date|None, raw). For a date range, deadline = end date."""
    low = resdate.lower()
    if "rolling" in low:
        return "rolling", resdate
    isos = re.findall(r"\d{4}-\d{2}-\d{2}", resdate)
    if isos:
        ds = [date.fromisoformat(x) for x in isos]
        return max(ds), resdate  # end of range = the deadline
    return None, resdate  # unparseable (e.g. "Apr 30", "5/28-6/02")


def _classify(rows, today):
    """rows: list of (id, status, resdate). Returns due/upcoming/rolling/unparseable."""
    due, upcoming, rolling, unparseable = [], [], [], []
    horizon = today + timedelta(days=7)
    for pid, status, resdate in rows:
        if status.strip().upper() not in OPEN_STATUSES:
            continue
        dl, raw = _parse_deadline(resdate)
        if dl == "rolling":
            rolling.append((pid, raw))
        elif dl is None:
            unparseable.append((pid, raw))
        elif dl <= today:
            due.append((pid, dl, raw))
        elif dl <= horizon:
            upcoming.append((pid, dl, raw))
    return due, upcoming, rolling, unparseable


def _read_rows():
    if not PREDICTIONS_TSV.exists():
        return None
    rows = []
    lines = PREDICTIONS_TSV.read_text().strip().split("\n")
    for line in lines[1:]:
        c = line.split("\t")
        if len(c) >= 4:
            rows.append((c[0], c[2], c[3]))
    return rows


def predictions_due(today=None):
    today = today or date.today()
    print(f"\n{'─'*64}\n  (d) PREDICTIONS-DUE SCAN  ·  as of {today}\n{'─'*64}")
    rows = _read_rows()
    if rows is None:
        print("  ⚠️  PREDICTIONS.tsv not found")
        return
    due, upcoming, rolling, unparseable = _classify(rows, today)
    if due:
        print("  🔴 DUE — resolve now (OPEN/ACTIVE, deadline ≤ today):")
        for pid, dl, raw in due:
            print(f"     {pid:<8} deadline {dl}  [{raw}]")
    else:
        print("  ✓ none overdue.")
    if upcoming:
        print("  🟠 UPCOMING (≤7d):")
        for pid, dl, raw in upcoming:
            print(f"     {pid:<8} resolves {dl}  ({(dl - today).days}d)  [{raw}]")
    if rolling:
        print("  🟡 ROLLING watch: " + ", ".join(p for p, _ in rolling))
    if unparseable:
        print("  ⚠️  unparseable resolve-date (check manually): "
              + ", ".join(f"{p}[{r}]" for p, r in unparseable))


# ── (e) LEDGER STALENESS ──────────────────────────────────────────────
# Added 2026-07-27 (HENRY, accepting DAEDALUS staleness-sweep #2 finding).
# The gap it caught: boot covered tape/gamma/credit/predictions but had NO
# ledger leg, so FLOW/KB/MARKET_DATA silently drifted 33d+ unnoticed — the
# TRUE SILENT-ROT class. Root CLAUDE.md §Data Hygiene requires a live ledger
# to carry a BOOT-TIME mtime alert (not a closeout ritual), or be FROZEN.
# FROZEN files are skipped here by design — they are declared dead, not rotten.
LEDGERS = [
    "workbook/PREDICTIONS.tsv",
    "workbook/VX.tsv",
    "workbook/KB.tsv",
    "workbook/FLOW.tsv",
    "workbook/MARKET_DATA.tsv",
    "board_log.tsv",
]
STALE_YELLOW, STALE_ORANGE = 14, 30


def ledger_staleness(today=None):
    today = today or date.today()
    print(f"\n{'─'*64}\n  (e) LEDGER STALENESS  ·  mtime vs {today}\n{'─'*64}")
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rows, worst = [], 0
    for rel in LEDGERS:
        p = os.path.join(base, rel)
        if not os.path.exists(p):
            rows.append(("  ⚠️ ", rel, "MISSING", -1))
            continue
        # FROZEN ledgers are declared dead — skip, don't nag.
        try:
            with open(p, encoding="utf-8", errors="replace") as fh:
                if fh.readline().lstrip().startswith("# FROZEN"):
                    rows.append(("  ❄️ ", rel, "FROZEN (not maintained)", -1))
                    continue
        except OSError:
            pass
        age = (today - date.fromtimestamp(os.path.getmtime(p))).days
        worst = max(worst, age)
        flag = "  🔴" if age >= STALE_ORANGE else ("  🟠" if age >= STALE_YELLOW else "  ✓ ")
        rows.append((flag, rel, f"{date.fromtimestamp(os.path.getmtime(p))}", age))
    for flag, rel, stamp, age in rows:
        agestr = "" if age < 0 else f"  ({age}d)"
        print(f"{flag} {rel:<28} {stamp}{agestr}")
    if worst >= STALE_ORANGE:
        print(f"\n  🔴 STALE — a live ledger is {worst}d old. STATUS is canonical; either "
              f"refresh it this session or FROZEN-banner it (root §Data Hygiene).")
    elif worst >= STALE_YELLOW:
        print(f"\n  🟠 drifting — oldest live ledger {worst}d. Refresh at write-back.")
    else:
        print("\n  ✓ all live ledgers fresh (<14d).")
    # Falsification-layer guard (DAEDALUS F2 disposition, 2026-08-06):
    # THESIS_VALIDATION.md is SUPERSEDED — its function lives in STATUS
    # § INVALIDATION TRIAD + PREDICTIONS.tsv. This surface rotted twice
    # (7/11 pilot 4-of-4; 8/3 at 38d) because a second live falsification
    # copy decays on a ~3-week clock. Guard: the banner must stay; if it
    # ever reads live again it needs a maintenance owner, not a restamp.
    tv = os.path.join(base, "workbook/THESIS_VALIDATION.md")
    try:
        with open(tv, encoding="utf-8", errors="replace") as fh:
            head = fh.read(400)
        if "SUPERSEDED" not in head:
            print("  🔴 THESIS_VALIDATION.md has LOST its SUPERSEDED banner — it is "
                  "not a live falsification layer (successors: STATUS §INVALIDATION "
                  "TRIAD + PREDICTIONS.tsv). Restore the banner or re-own maintenance.")
    except OSError:
        pass


# ── (f) INBOX TRIAGE ──────────────────────────────────────────────────
# Added 2026-07-28. The MAIL rule says inbox PROCESSING is a separate task —
# correct, it is expensive (7 packets cost real context). But I read "don't
# process" as "don't look", so a file named
#   2026-07-24_from-LABOR_ahe-composition-eci-7-31-post-fomc-repricing-risk.md
# sat unopened for four days during FOMC week. The filename alone said it was
# time-critical. TRIAGE IS NOT PROCESSING: filenames only, no file contents,
# no context cost. Flag; do not open. Opening remains the analyst's call.
INBOX_WINDOW_DAYS = 14      # a date in a filename this close = flag it
INBOX_STALE_DAYS = 10       # unread this long = flag regardless (rot backstop)
GATE_KEYWORDS = [
    # subject matter I hold gates on
    "gamma", "flip", "gex", "cpi", "ppi", "pce", "fomc", "eci", "nfp",
    "vix", "auction", "credit", "capex", "fcf",
    # PACKET-TYPE markers — time-critical by CLASS, whatever the subject.
    # Added after BOND's 2026-07-28 reply slipped through: its filename
    # ("prereg-challenged-by-my-own-backtest-pre-print") named the EPISTEMICS,
    # not the subject, so no subject keyword could catch it. A correction or a
    # pre-registration is urgent regardless of what it is about.
    "prereg", "retraction", "retracted", "correction", "corrects",
    "supersedes", "urgent",
]
# ⚠️ KNOWN LIMIT: this is a FILENAME heuristic and cannot beat an uninformative
# filename. It depends on senders naming packets by subject or type. Do not
# over-tune the keyword list to chase individual misses — that trades a rule
# for a lookup table. When it misses, the fix is a fleet filename convention.
# M-D inside a filename (7-31, 8-12) — the leading YYYY-MM-DD prefix is
# stripped first so the packet's OWN date is never mistaken for a catalyst.
MD_RE = re.compile(r"(?<![\d])(1[0-2]|[1-9])-(3[01]|[12]\d|[1-9])(?![\d])")


def _live_prediction_ids():
    rows = _read_rows() or []
    return [pid.lower() for pid, status, _ in rows if status.strip().upper() in OPEN_STATUSES]


def triage_names(names, today, live_ids):
    """Pure decision layer — filenames in, (flagged, quiet) out. Testable."""
    flagged, quiet = [], []
    for name in names:
        stem = re.sub(r"^\d{4}-\d{2}-\d{2}[a-z]?_", "", name)  # strip own date
        low = stem.lower()
        reasons = []
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", name)
        age = (today - date(int(m[1]), int(m[2]), int(m[3]))).days if m else None
        for mo, dy in MD_RE.findall(stem):
            try:
                d = date(today.year, int(mo), int(dy))
            except ValueError:
                continue
            delta = (d - today).days
            if 0 <= delta <= INBOX_WINDOW_DAYS:
                reasons.append(f"date-in-window {mo}/{dy} ({delta}d out)")
        for pid in live_ids:
            if pid and pid in low:
                reasons.append(f"live gate {pid.upper()}")
        # ⚠️ TOKEN match, not substring — "mississippi" contains "ppi", and the
        # first cut duly flagged an AEOLUS river-levels packet as a macro-data
        # release. Same failure class as the 174960/7496 substring hit in
        # consumer_check.py: match whole tokens, never fragments.
        toks = set(re.split(r"[^a-z0-9]+", low))
        hits = [k for k in GATE_KEYWORDS if k in toks]
        if hits and not reasons:
            reasons.append(f"gate keyword: {', '.join(hits[:3])}")
        if age is not None and age >= INBOX_STALE_DAYS and not reasons:
            reasons.append(f"unread {age}d")
        (flagged if reasons else quiet).append((name, age, reasons))
    return flagged, quiet


def inbox_triage(today=None, names=None):
    today = today or date.today()
    print(f"\n{'─'*64}\n  (f) INBOX TRIAGE  ·  filenames only — this is NOT processing\n{'─'*64}")
    if names is None:
        inbox = HENRY_DIR / "inbox"
        names = sorted(p.name for p in inbox.glob("*.md")) if inbox.exists() else []
    if not names:
        print("  ✓ inbox clear.")
        return [], []
    flagged, quiet = triage_names(names, today, _live_prediction_ids())
    for name, age, reasons in flagged:
        print(f"  🔴 {name}")
        print(f"       {' · '.join(reasons)}" + (f" · {age}d unread" if age is not None else ""))
    if quiet:
        print(f"  ⚪ no hit ({len(quiet)}): " + ", ".join(
            re.sub(r"^\d{4}-\d{2}-\d{2}[a-z]?_", "", n)[:38] for n, _, _ in quiet))
    print(f"\n  → {len(flagged)} of {len(names)} flagged. Open flagged ONLY; "
          f"the rest wait for a processing spawn.")
    return flagged, quiet


# ── (g) STALE-CONSUMER CHECK ──────────────────────────────────────────
# Added 2026-07-28. Runs consumer_check.py off workbook/PUBLISHED.tsv, which
# gamma_flip.py writes on every run. Answers the question nobody was asking:
# "who is still grading a gate against a number I have already superseded?"
CONSUMER_CHECK = WORKSPACE / "scripts" / "consumer_check.py"  # repo-root scripts/, NOT AGENTS/HENRY/scripts/ — closeout audit R3, fixed 2026-07-31
PUBLISHED_TSV = HENRY_DIR / "workbook" / "PUBLISHED.tsv"


def stale_consumers():
    print(f"\n{'─'*64}\n  (g) STALE-CONSUMER CHECK  ·  who still cites a number I superseded?\n{'─'*64}")
    if not (CONSUMER_CHECK.exists() and PUBLISHED_TSV.exists()):
        print("  ⚠️  consumer_check.py or workbook/PUBLISHED.tsv missing — skipped.")
        return
    code, out, err = run([_py(), str(CONSUMER_CHECK), "--agent", "HENRY",
                          "--from-ledger"], timeout=180)
    if not out:
        print(f"  ⚠️  consumer_check produced no output: {(err or '')[:200]}")
        return
    keep = [l for l in out.split("\n")
            if l.strip() and not l.startswith("=") and "own dir excluded" not in l
            and "CONSUMER CHECK" not in l]
    print("\n".join(keep[:26]) if keep else "  (no output)")


def selftest_triage():
    """REGRESSION: replay the exact 7-packet inbox of 2026-07-28.

    That morning the MAIL rule ("don't process on normal spawns") was read as
    "don't look", and LABOR's packet — with `eci-7-31` in the filename, during
    FOMC week — sat unopened for four days. This asserts the triage would have
    surfaced it, and equally that it stays QUIET on the five that were correctly
    deferrable. A triage that flags everything is the same as no rule at all.
    """
    today = date(2026, 7, 28)
    names = [
        "2026-07-22_from-AEOLUS_c5-mississippi-lowwater.md",
        "2026-07-22_to-HENRY_capex-decel-fcf-inflection.md",
        "2026-07-23_from-PROME_orphan-detector-ADOPTED.md",
        "2026-07-24_from-DEWEY_p2-sterile-capex-crossref.md",
        "2026-07-24_from-DEWEY_p3-china-fisc-comparative.md",
        "2026-07-24_from-LABOR_ahe-composition-eci-7-31-post-fomc-repricing-risk.md",
        "2026-07-27_from-PROME_batch3-dispatch-P2-and-P3.md",
    ]
    flagged, quiet = triage_names(names, today, ["hen-36", "hen-41", "hen-42"])
    fnames = {n for n, _, _ in flagged}
    must_flag = "2026-07-24_from-LABOR_ahe-composition-eci-7-31-post-fomc-repricing-risk.md"
    must_stay_quiet = {
        "2026-07-24_from-DEWEY_p3-china-fisc-comparative.md",
        "2026-07-22_from-AEOLUS_c5-mississippi-lowwater.md",
    }
    ok = must_flag in fnames and not (must_stay_quiet & fnames)
    print(f"  triage selftest: flagged {len(flagged)}/7 → "
          f"{sorted(re.sub(r'^.*?_from-|^.*?_to-', '', n)[:22] for n in fnames)}")
    print("  ✅ PASS — LABOR/eci-7-31 surfaced; deferrable packets stayed quiet."
          if ok else
          f"  ❌ FAIL — LABOR flagged={must_flag in fnames}, "
          f"false positives={sorted(must_stay_quiet & fnames)}")
    return 0 if ok else 1


def selftest():
    """Assert the due-scan fires on a row like HEN-32 (resolve 6/10, ACTIVE)."""
    today = date(2026, 6, 15)
    fake = [
        ("HEN-XX", "ACTIVE", "2026-06-10"),                 # must be DUE
        ("HEN-YY", "ACTIVE", "2026-06-17-to-2026-06-19"),   # upcoming
        ("HEN-ZZ", "ACTIVE", "rolling"),                    # rolling
        ("HEN-DN", "MISS",   "2026-06-10"),                 # closed → ignored
    ]
    due, upcoming, rolling, _ = _classify(fake, today)
    ok = (
        any(p == "HEN-XX" for p, *_ in due)
        and not any(p == "HEN-DN" for p, *_ in due)
        and any(p == "HEN-YY" for p, *_ in upcoming)
        and "HEN-ZZ" in [p for p, _ in rolling]
    )
    print(f"  selftest: due={[p for p,*_ in due]} upcoming={[p for p,*_ in upcoming]} "
          f"rolling={[p for p,_ in rolling]}")
    print("  ✅ PASS — due-scan surfaces an ACTIVE/past-deadline row (and ignores closed)."
          if ok else "  ❌ FAIL")
    return 0 if ok else 1


def main():
    if "--selftest" in sys.argv:
        return selftest() or selftest_triage()
    quick = "--quick" in sys.argv
    verbose = "--verbose" in sys.argv
    t0 = time.time()
    now = datetime.now()
    print(f"\n{'='*64}\n  HENRY BOOT KIT (v1)   ·   {now:%A, %B %d, %Y  %H:%M}\n{'='*64}")
    live_tape()
    if not quick:
        gamma()
        credit(verbose=verbose)
    else:
        print("\n  (b) GAMMA + (c) CREDIT — skipped (--quick)")
    predictions_due()
    ledger_staleness()
    inbox_triage()
    if not quick:
        stale_consumers()
    print(f"\n{'='*64}\n  boot brief done in {time.time()-t0:.1f}s   "
          f"(--verbose full credit · --quick skip gamma+credit · --selftest)\n{'='*64}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
