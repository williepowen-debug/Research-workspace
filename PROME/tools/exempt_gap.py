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
the declared reference; the FALLBACK set below is used, loudly, only when that line cannot be
parsed or is empty; PROME is excluded because board_scan.py is its own blocking check):
  * every BOARD signal whose `action:` line (or the legacy `to:` line, pre-v0.12) names D — info-cc lines are not the exemption's risk
  * whether that signal_id IS a whole CELL (bare, or id+filename-slug as RED writes it) in ANY of D's BOARD
    consumption ledgers (live + archived) — a cell that continues with prose is a mention, not a row
  * flags an unlogged action signal once it is >= --min-age-days old (default 2 — a desk that
    booted since dispatch and did not log it is the failure; a signal dispatched an hour ago is not)
  * a desk with NO ledger at all is flagged UNKNOWN — an exemption nobody can test is the
    walter_doctor phrase "cannot be tested at all", and that is a flag, not a pass.

FAIL-CLOSED RULES (cold read 2026-09-11, 8 ❌ fixed in one pass): a signal file this scan cannot read
(malformed filename date, any non-conforming name under BOARD/ other than INDEX.md, no frontmatter, no routing
key on a post-v0.12 file, I/O error) is SKIPPED, COUNTED and NAMED —
never silently dropped and never allowed to abort the other files; a duplicate signal_id MERGES its
owners and is named; an empty exempt set or an unreadable ledger is an instrument failure, not a pass.

Exit codes: 0 clean · 1 a desk owes rows (aged unlogged action signal, or no ledger) ·
2 instrument problem (skipped files · duplicate ids · empty exempt set · unreadable ledger · crash) —
prome_gate treats both 1 and 2 as flags, but the receipt says which.
Advisory in `prome_gate.py boot` (a flag = packet/doorbell the desk; it is that desk's ledger to fill,
never PROME's to grade on its behalf — §3.5.2, a spawned reader cannot integrate).

Usage:
    python3 PROME/tools/exempt_gap.py                   # live repo, today
    python3 PROME/tools/exempt_gap.py --desks CARL,RED  # subset (full flag list printed)
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

# a ledger CELL that IS an id: the bare id, or the id followed only by its filename slug (RED's ledgers write
# `SIG-W-20260813-002-price-source-null-bars` in the id column — measured 9/11, 8 real dispositions). A cell that
# continues with whitespace or prose ("SIG-W-… superseded, ignoring") is a mention, not a row.
SIG_ID_CELL = re.compile(r"^(SIG-W-\d{8}-\d{3})(?:-[A-Za-z0-9._-]*)?$")
V012_DATE = dt.date(2026, 7, 27)                     # BOARD_CONSUMPTION_SPEC v0.12: `action:` becomes the routing key
NON_SIGNAL_FILES = {"INDEX.md"}                      # the only non-signal .md that belongs under BOARD/
DOCTOR_REL = "AGENTS/WALTER/tools/walter_doctor.py"
FALLBACK_EXEMPT = {"CARL", "RED", "TERRY"}  # used ONLY if the doctor line is unparseable/empty; printed when used
LEDGER_GLOBS = (  # every surface a desk has ever used as a BOARD consumption ledger; FILED handoffs do not count (§5.1)
    "board_log.tsv",
    "board/BOARD_LOG.tsv",
    "archive/board_log*.tsv",
    "board/archive/*.tsv",
)
OWNER_TOKEN = re.compile(r"^[A-Z][A-Z0-9_-]{1,}$")


def owners(value):
    """Normalize a routing-line value to a list of upper-case desk names.

    Live BOARD forms (measured 2026-09-11): `[A, B]` (parse_front returns a list) · bare `A` · `A (ACTION — free
    text, commas included)` — the last two arrive as ONE STRING, and iterating a string yields letters
    (the 15:0x defect TERRY caught before it shipped a miss). Text after the first "(" is annotation, never a
    name; names are exact tokens, so TERRYX never matches TERRY.
    """
    if not value:
        return []
    items = value if isinstance(value, list) else [value]
    out = []
    for item in items:
        head = re.split(r"[(—–]", str(item), 1)[0]          # drop "(annotation…" and dash-led notes
        for tok in re.split(r"[,\s;/]+", head):
            tok = tok.strip().strip("'\"[]").upper()
            if tok and OWNER_TOKEN.match(tok):
                out.append(tok)
    return out


def repo_root():
    return pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                       capture_output=True, text=True, check=True).stdout.strip())


def exempt_desks(root):
    """Read PULL_COMPLETE from walter_doctor.py. Returns (set, note, ok) — ok=False means the fallback was used."""
    p = root / DOCTOR_REL
    try:
        m = re.search(r"^PULL_COMPLETE\s*=\s*\{([^}]*)\}", p.read_text(encoding="utf-8"), re.M)
        if m:
            names = {x.strip().strip("'\"").upper() for x in m.group(1).split(",") if x.strip()}
            names.discard("PROME")
            if names:
                return names, f"exempt set read from {DOCTOR_REL}: {', '.join(sorted(names))}", True
    except OSError:
        pass
    return set(FALLBACK_EXEMPT), (f"⛔ {DOCTOR_REL} PULL_COMPLETE unparseable or empty — FALLBACK set "
                                  f"{', '.join(sorted(FALLBACK_EXEMPT))} used; fix the reference, not this script"), False


def desk_ledgers(root, desk):
    base = root / "AGENTS" / desk
    out = []
    for g in LEDGER_GLOBS:
        out.extend(sorted(base.glob(g)))
    return out


def id_column(lines):
    """Index of the signal-id column from a header row (`signal_id` / `Signal_ID`, any case) in the first 5 lines;
    None when no header names one — then every cell is read (legacy ledgers), which is the weaker rule."""
    for line in lines[:5]:
        cells = [c.strip().lower() for c in line.split("\t")]
        if "signal_id" in cells:
            return cells.index("signal_id")
    return None


def logged_ids(ledgers):
    """Ids logged as a ROW in any ledger — read from the signal_id COLUMN when the header names one (third cold
    read 9/11: a column-agnostic match let a filename reference in an artifact column clear another signal's
    obligation). Returns (ids, errors) — an unreadable ledger is an error, not zero."""
    ids, errors = set(), []
    for p in ledgers:
        try:
            lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
            col = id_column(lines)
            for line in lines:
                cells = line.split("\t")
                targets = [cells[col]] if col is not None and col < len(cells) else (cells if col is None else [])
                for cell in targets:
                    m = SIG_ID_CELL.match(cell.strip())
                    if m:
                        ids.add(m.group(1))
        except Exception as e:  # directory, permissions, decode — an instrument failure, never "nothing logged"
            errors.append(f"{p}: {type(e).__name__}: {e}")
    return ids, errors


def load_signals(root):
    """Returns (sigs, skipped, dupes).

    sigs = {signal_id: (date, owner_list, headline)} for every readable BOARD/SIG-W-*.md.
    skipped = [(filename, reason)] — files the scan could NOT read; counted and named, never dropped.
    dupes = [signal_id] — ids present in more than one file; owners MERGED (never overwritten) and named.
    """
    sigs, skipped, dupes, unrouted_legacy = {}, [], [], 0
    files = [p for p in (root / "BOARD").glob("*.md") if p.name not in NON_SIGNAL_FILES]
    for p in sorted(files, key=lambda q: sig_key(q.name)):
        try:
            d, n = sig_key(p.name)
            if not d:                                     # lower-case, short date, stray file — named, never dropped
                raise ValueError("filename does not match SIG-W-YYYYMMDD-NNN")
            sid = f"SIG-W-{d}-{n:03d}"
            date = dt.date(int(d[:4]), int(d[4:6]), int(d[6:8]))
            fm = parse_front(p)
            if "_headline" not in fm:                     # parse_front returns {} on I/O error or no --- block
                raise ValueError("no frontmatter block or file unreadable")
            if "action" not in fm and "to" not in fm:     # NO routing key at all (an empty `action: []` is routed to nobody)
                if date >= V012_DATE:
                    raise ValueError("no `action:`/`to:` routing key on a post-v0.12 signal")
                unrouted_legacy += 1                      # the 34 early-April files: counted, reported, not a flag
            acts = owners(fm.get("action")) or owners(fm.get("to"))
            if sid in sigs:
                dupes.append(sid)
                prev = sigs[sid]
                sigs[sid] = (prev[0], sorted(set(prev[1]) | set(acts)), prev[2])
            else:
                sigs[sid] = (date, acts, fm.get("_headline", ""))
        except Exception as e:
            skipped.append((p.name, f"{type(e).__name__}: {e}"))
    return sigs, skipped, dupes, unrouted_legacy


def scan(root, today, min_age_days, desks=None):
    """Pure function over the tree. Returns (rows, note, instrument) — rows = per-desk dicts;
    instrument = {"skipped": [...], "dupes": [...], "exempt_ok": bool, "ledger_errors": [...]}."""
    exempt, note, ok = exempt_desks(root)
    if desks:
        exempt = {d.upper() for d in desks}
        note = f"desk set OVERRIDDEN by --desks: {', '.join(sorted(exempt))} (doctor set not used)"
        ok = True
    sigs, skipped, dupes, unrouted_legacy = load_signals(root)
    rows, ledger_errors = [], []
    for desk in sorted(exempt):
        ledgers = desk_ledgers(root, desk)
        logged, errs = logged_ids(ledgers)
        ledger_errors += errs
        addressed = [sid for sid, (d, acts, hl) in sigs.items() if desk in acts]
        unlogged = [sid for sid in addressed if sid not in logged]
        aged = [sid for sid in unlogged if (today - sigs[sid][0]).days >= min_age_days]
        rows.append({
            "desk": desk, "ledgers": ledgers, "logged": len(logged),
            "addressed": len(addressed), "unlogged": unlogged, "aged": aged,
            "fresh": len(unlogged) - len(aged),
            "detail": [(sid, (today - sigs[sid][0]).days, sigs[sid][2]) for sid in aged],
            "untestable": not ledgers,
        })
    return rows, note, {"skipped": skipped, "dupes": dupes, "exempt_ok": ok, "ledger_errors": ledger_errors,
                        "unrouted_legacy": unrouted_legacy}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None, help="repo root (default: git toplevel)")
    ap.add_argument("--today", default=None, help="YYYY-MM-DD (default: today)")
    ap.add_argument("--min-age-days", type=int, default=2)
    ap.add_argument("--desks", default=None, help="comma list; overrides the doctor set; prints the FULL flag list")
    args = ap.parse_args(argv)
    try:
        root = pathlib.Path(args.root).resolve() if args.root else repo_root()
        today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
        if args.min_age_days < 0:
            raise ValueError("--min-age-days must be >= 0")
        if not (root / "BOARD").is_dir():
            print(f"EXEMPT-GAP ✗ no BOARD dir under {root}", file=sys.stderr)
            return 2
        rows, note, inst = scan(root, today, args.min_age_days, args.desks.split(",") if args.desks else None)
    except Exception as e:
        print(f"EXEMPT-GAP ✗ rc 2 — {type(e).__name__}: {e}", file=sys.stderr)
        return 2
    print(f"EXEMPT-GAP — §3.5 exempt desks vs their own BOARD ledgers · as-of {today} · "
          f"flag = action-line signal unlogged ≥{args.min_age_days}d · {note}")
    desk_flags = 0
    for r in rows:
        led = ", ".join(str(p.relative_to(root)) for p in r["ledgers"]) or "NONE"
        if r["untestable"]:
            desk_flags += 1
            print(f"⚠️  {r['desk']}: NO BOARD consumption ledger found ({' | '.join(LEDGER_GLOBS)}) — "
                  f"{r['addressed']} action-line signals address it and none can be tested (UNKNOWN, not PASS)")
            continue
        head = (f"{r['desk']}: ledgers [{led}] · logged {r['logged']} · action-addressed {r['addressed']} · "
                f"unlogged {len(r['unlogged'])} (fresh <{args.min_age_days}d: {r['fresh']}) · "
                f"aged ≥{args.min_age_days}d {len(r['aged'])}")
        if r["aged"]:
            desk_flags += 1
            print(f"⚠️  {head}")
            shown = r["detail"] if args.desks else r["detail"][-8:]
            for sid, age, hl in shown:
                print(f"       {sid}  {age:>3}d  {clean(hl, 90)}")
            if len(r["detail"]) > len(shown):
                print(f"       … {len(r['detail']) - len(shown)} older — full list: --desks {r['desk']}")
        else:
            print(f"✅ {head}")
    # instrument problems — printed by name, never a bare count
    inst_flags = 0
    for name, why in inst["skipped"]:
        inst_flags += 1
        print(f"⛔ SKIPPED {name} — {why}")
    for sid in inst["dupes"]:
        inst_flags += 1
        print(f"⛔ DUPLICATE signal_id {sid} in more than one file — owners merged; the BOARD needs one file per id")
    for err in inst["ledger_errors"]:
        inst_flags += 1
        print(f"⛔ LEDGER UNREADABLE {err}")
    if not inst["exempt_ok"]:
        inst_flags += 1
    if inst["unrouted_legacy"]:
        print(f"ℹ️  {inst['unrouted_legacy']} pre-v0.12 signal file(s) carry no routing key at all — counted, not a flag")
    if not rows:
        print("⛔ no exempt desk scanned — an empty set is an instrument failure, not a clean pass")
        return 2
    if inst_flags:
        print(f"\n⛔ {inst_flags} instrument problem(s) above — this scan's ✅ lines are SCOPED to the files it could "
              f"read, not clean; fix the named files/reference first.")
    if desk_flags:
        print(f"\n→ {desk_flags} desk(s) flagged. Rule: the ledger is the DESK's to fill — packet/doorbell it "
              f"(§3.5.2: a reader who cannot integrate cannot discharge it); a desk with no ledger owes one.")
    if inst_flags:
        return 2
    if desk_flags:
        return 1
    print("\nEXEMPT-GAP ✓ every exempt desk's action-line signals are logged or younger than the floor")
    return 0


if __name__ == "__main__":
    sys.exit(main())
