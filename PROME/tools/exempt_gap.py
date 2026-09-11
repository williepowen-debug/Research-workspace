#!/usr/bin/env python3
"""Receiver-independent check on the §3.5 pull-complete EXEMPT desks (Will: "ok go ahead", 2026-09-11 13:37 ET).

WHY (2026-09-11): CARL is exempt — WALTER writes it no handoffs because CARL's own whole-INDEX
scan IS the pull. On 9/2 CARL installed the v0.2 lane step, read its always-empty lane as
"nothing unconsumed", and stopped logging scan rows on 9/1. For ten days two action-line signals
(one IMMEDIATE) sat unread while every surface either side keeps read clean. Same failure mode
the spec recorded for RED on 8/12 (§3.5.6): the exemption removes the only artifact that would
show the scan was skipped, so a skipped scan and a clean scan are indistinguishable — to the desk.

They are NOT indistinguishable to a third party who reads BOTH the BOARD and the desk's ledger.
This script is that third party. It does not depend on the desk running anything.

What it measures, per exempt desk D (the set is READ from walter_doctor.py's PULL_COMPLETE —
the declared reference — never re-typed here; PROME is excluded because board_scan.py is its own
blocking check):
  * every BOARD signal whose `action:` line (or the legacy `to:` line, pre-v0.12) names D — info-cc lines are not the exemption's risk
  * whether that signal_id appears in ANY of D's BOARD consumption ledgers (live + archived)
  * flags an unlogged action signal once it is >= --min-age-days old (default 2 — a desk that
    booted since dispatch and did not log it is the failure; a signal dispatched an hour ago is not)
  * a desk with NO ledger at all is flagged UNKNOWN — an exemption nobody can test is the
    walter_doctor phrase "cannot be tested at all", and that is a flag, not a pass.

Exit codes: 0 clean · 1 at least one aged unlogged action signal or an untestable desk · 2 execution error.
Advisory in `prome_gate.py boot` (a flag = packet/doorbell the desk; it is that desk's ledger to fill,
never PROME's to grade on its behalf — §3.5.2, a spawned reader cannot integrate).

Usage:
    python3 PROME/tools/exempt_gap.py                   # live repo, today
    python3 PROME/tools/exempt_gap.py --desks CARL,RED  # subset
    python3 PROME/tools/exempt_gap.py --root <dir> --today 2026-09-11   # tests / fixtures
"""
import argparse
import datetime as dt
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from board_scan import parse_front, sig_key, clean  # noqa: E402  (same parser the PROME pull uses)

SIG_ID_RE = re.compile(r"SIG-W-\d{8}-\d{3}")
DOCTOR_REL = "AGENTS/WALTER/tools/walter_doctor.py"
FALLBACK_EXEMPT = {"CARL", "RED", "TERRY"}  # used ONLY if the doctor line cannot be parsed; printed when used
LEDGER_GLOBS = (  # every surface a desk has ever used as a BOARD consumption ledger; FILED handoffs do not count (§5.1)
    "board_log.tsv",
    "board/BOARD_LOG.tsv",
    "archive/board_log*.tsv",
    "board/archive/*.tsv",
)


def repo_root():
    return pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                       capture_output=True, text=True, check=True).stdout.strip())


def exempt_desks(root):
    """Read PULL_COMPLETE from walter_doctor.py. Returns (set, note)."""
    p = root / DOCTOR_REL
    try:
        m = re.search(r"^PULL_COMPLETE\s*=\s*\{([^}]*)\}", p.read_text(encoding="utf-8"), re.M)
        if m:
            names = {x.strip().strip("'\"").upper() for x in m.group(1).split(",") if x.strip()}
            names.discard("PROME")
            return names, f"exempt set read from {DOCTOR_REL}: {', '.join(sorted(names))}"
    except OSError:
        pass
    return set(FALLBACK_EXEMPT), (f"⚠️  {DOCTOR_REL} PULL_COMPLETE not parseable — using the fallback set "
                                  f"{', '.join(sorted(FALLBACK_EXEMPT))}; fix the reference, not this script")


def desk_ledgers(root, desk):
    base = root / "AGENTS" / desk
    out = []
    for g in LEDGER_GLOBS:
        out.extend(sorted(base.glob(g)))
    return out


def logged_ids(ledgers):
    ids = set()
    for p in ledgers:
        try:
            ids |= set(SIG_ID_RE.findall(p.read_text(encoding="utf-8", errors="replace")))
        except OSError:
            continue
    return ids


def load_signals(root):
    """{signal_id: (date, action_upper_list, headline)} for every BOARD/SIG-W-*.md."""
    sigs = {}
    for p in sorted((root / "BOARD").glob("SIG-W-*.md"), key=lambda q: sig_key(q.name)):
        d, n = sig_key(p.name)
        if not d:
            continue
        sid = f"SIG-W-{d}-{n:03d}"
        fm = parse_front(p)
        # `action:` is the v0.12 (2026-07-27) key; 585 April–July files carry the legacy `to:` key with the
        # same meaning (measured 2026-09-11 — TERRY's bare-`id:` finding prompted the census). A key-name
        # census that reads only the new spelling fails OPEN on every legacy row, so both are read.
        acts = [a.upper() for a in (fm.get("action") or fm.get("to") or [])]
        sigs[sid] = (dt.date(int(d[:4]), int(d[4:6]), int(d[6:8])), acts, fm.get("_headline", ""))
    return sigs


def scan(root, today, min_age_days, desks=None):
    """Pure function over the tree. Returns (rows, note) — rows = per-desk dicts."""
    exempt, note = exempt_desks(root)
    if desks:
        exempt = {d.upper() for d in desks}
    sigs = load_signals(root)
    rows = []
    for desk in sorted(exempt):
        ledgers = desk_ledgers(root, desk)
        logged = logged_ids(ledgers)
        addressed = [sid for sid, (d, acts, hl) in sigs.items() if desk in acts]
        unlogged = [sid for sid in addressed if sid not in logged]
        aged = [sid for sid in unlogged if (today - sigs[sid][0]).days >= min_age_days]
        rows.append({
            "desk": desk, "ledgers": ledgers, "logged": len(logged),
            "addressed": len(addressed), "unlogged": unlogged, "aged": aged,
            "detail": [(sid, (today - sigs[sid][0]).days, sigs[sid][2]) for sid in aged],
            "untestable": not ledgers,
        })
    return rows, note


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None, help="repo root (default: git toplevel)")
    ap.add_argument("--today", default=None, help="YYYY-MM-DD (default: today)")
    ap.add_argument("--min-age-days", type=int, default=2)
    ap.add_argument("--desks", default=None, help="comma list; overrides the doctor set")
    args = ap.parse_args(argv)
    root = pathlib.Path(args.root).resolve() if args.root else repo_root()
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    if not (root / "BOARD").is_dir():
        print(f"EXEMPT-GAP ✗ no BOARD dir under {root}", file=sys.stderr)
        return 2
    rows, note = scan(root, today, args.min_age_days, args.desks.split(",") if args.desks else None)
    print(f"EXEMPT-GAP — §3.5 exempt desks vs their own BOARD ledgers · as-of {today} · "
          f"flag = action-line signal unlogged ≥{args.min_age_days}d · {note}")
    flagged = 0
    for r in rows:
        led = ", ".join(str(p.relative_to(root)) for p in r["ledgers"]) or "NONE"
        if r["untestable"]:
            flagged += 1
            print(f"⚠️  {r['desk']}: NO BOARD consumption ledger found ({' | '.join(LEDGER_GLOBS)}) — "
                  f"{r['addressed']} action-line signals address it and none can be tested (UNKNOWN, not PASS)")
            continue
        head = (f"{r['desk']}: ledgers [{led}] · logged {r['logged']} · action-addressed {r['addressed']} · "
                f"unlogged {len(r['unlogged'])} · aged ≥{args.min_age_days}d {len(r['aged'])}")
        if r["aged"]:
            flagged += 1
            print(f"⚠️  {head}")
            for sid, age, hl in r["detail"][-8:]:
                print(f"       {sid}  {age:>3}d  {clean(hl, 90)}")
            if len(r["detail"]) > 8:
                print(f"       … {len(r['detail']) - 8} older (full list: --desks {r['desk']} in a terminal)")
        else:
            print(f"✅ {head}")
    if flagged:
        print(f"\n→ {flagged} desk(s) flagged. Rule: the ledger is the DESK's to fill — packet/doorbell it "
              f"(§3.5.2: a reader who cannot integrate cannot discharge it); a desk with no ledger owes one.")
        return 1
    print("\nEXEMPT-GAP ✓ every exempt desk's action-line signals are logged or younger than the floor")
    return 0


if __name__ == "__main__":
    sys.exit(main())
