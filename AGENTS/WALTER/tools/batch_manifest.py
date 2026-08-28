#!/usr/bin/env python3
"""WALTER batch manifest — declare the INPUT count before processing, reconcile before closeout.

WHY THIS EXISTS (2026-07-31, and it is the only failure class WALTER's telemetry is
structurally blind to):

    Will sent a 7-image batch. WALTER processed six. The missed one was the
    IRGC tanker claim — the highest-consequence item in the drop, touching a
    registered gate and FALCON's flip-ups. It sat ~2h and surfaced ONLY because
    Will happened to ask for a sweep.

    `board_reconcile` OK. `log_reconcile` OK. `delivery_claim_vs_git` OK. All 24
    doctor checks green. Every one of them measures what was DISPATCHED, where it
    LANDED, and whether it COMMITTED. An input that arrives and quietly never
    becomes anything is invisible to all of them.

The asymmetry that justifies the build: an over-declared item costs one line of
"NO-ACTION"; an un-dispositioned input is invisible indefinitely and is found by luck.

⚠️ THE RESIDUAL, STATED PLAINLY BECAUSE IT IS NOT CLOSED:
    This catches items dropped WITHIN a declared batch. It CANNOT catch a batch that
    was never declared — the same "keyed on the thing you might forget" shape recorded
    in [[finding_test_the_guard_not_just_the_guarded]]. There is no honest mechanical
    fix from inside WALTER: nothing in the repo observes Will's chat. The mitigation is
    that `--open` is one command and the doctor nags while a batch is OPEN.
    DO NOT let a green manifest be read as "no inputs were dropped."

Usage:
  batch_manifest.py --open N --source "Will-Telegram 7-image batch 8/3 ~14:00Z"
  batch_manifest.py --item BM-20260803-01 3 DISPATCH SIG-W-20260803-005
  batch_manifest.py --item BM-20260803-01 4 KILL "kill_log: vintage 2025"
  batch_manifest.py --status
  batch_manifest.py --close BM-20260803-01      # refuses on any gap
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
WALTER = REPO / "AGENTS" / "WALTER"
LEDGER = Path(os.environ.get("WALTER_BATCH_LEDGER", WALTER / "registry" / "BATCH_MANIFEST.tsv"))

COLS = ["batch_id", "opened_utc", "source", "declared", "dispositioned", "state", "items", "notes"]
DISPOSITIONS = {"DISPATCH", "KILL", "NOTE", "FOLD", "DUP", "NO-ACTION"}


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _read() -> list[dict]:
    if not LEDGER.exists():
        return []
    rows = []
    for i, line in enumerate(LEDGER.read_text(encoding="utf-8").splitlines()):
        if not line.strip() or line.startswith("#"):
            continue
        f = line.split("\t")
        if i == 0 and f[0] == "batch_id":
            continue
        if len(f) != len(COLS):
            sys.exit(f"REFUSING TO RUN: {LEDGER.name} line {i+1} has {len(f)} fields, expected "
                     f"{len(COLS)}. Fix the row by hand — a manifest that cannot be parsed "
                     f"cannot prove anything, and guessing at the split would be worse.")
        rows.append(dict(zip(COLS, f)))
    return rows


def _write(rows: list[dict]) -> None:
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    out = ["\t".join(COLS)]
    out += ["\t".join(r[c] for c in COLS) for r in rows]
    LEDGER.write_text("\n".join(out) + "\n", encoding="utf-8")


def _items(r: dict) -> dict[int, str]:
    """items cell: '1=DISPATCH:SIG-...;3=KILL:reason' -> {1: 'DISPATCH:SIG-...'}"""
    d = {}
    for part in r["items"].split(";"):
        part = part.strip()
        if not part or "=" not in part:
            continue
        n, v = part.split("=", 1)
        try:
            d[int(n)] = v
        except ValueError:
            continue
    return d


def _max_suffix_today(rows: list[dict], today: str) -> tuple[int, int]:
    """Highest NN already used for today, from BOTH sources.

    Returns (ledger_max, file_max). Either may be 0 if that source has none.

    ⚠️ WHY THIS IS max() OVER TWO SOURCES AND NOT A ROW COUNT (2026-08-28):
    the allocator used to be `sum(1 for r in rows if ...) + 1`, which has TWO
    independent failure modes and hit both on the same day:
      (a) COUNT != MAX. Any gap in the ledger re-issues a used id.
      (b) THE LEDGER IS NOT THE ONLY RECORD. A batch staged as a per-batch
          manifest FILE (which is what a session does under a concurrent-writer
          hold, when the shared ledger must not be written) is INVISIBLE to a
          ledger-only scan.
    Live collision: 2026-08-28. BM-20260828-02/03/04 were declared and fully
    dispositioned as manifest FILES under a walter-0828 writer hold and never
    got ledger rows; the ledger held only -01, so `--open` re-issued the LIVE id
    BM-20260828-02 for a new 10-image batch. Caught before the first --item
    write, so the morning manifest was not overwritten -- but only by luck of
    the operator checking. [[finding_record_of_an_action_is_not_the_action]]
    """
    def suffix(bid: str) -> int:
        try:
            return int(bid.rsplit("-", 1)[1])
        except (IndexError, ValueError):
            return 0

    ledger_max = max((suffix(r["batch_id"]) for r in rows
                      if r["batch_id"].startswith(f"BM-{today}")), default=0)
    file_max = max((suffix(f.name.replace("-manifest.tsv", ""))
                    for f in LEDGER.parent.glob(f"BM-{today}-*-manifest.tsv")), default=0)
    return ledger_max, file_max


def cmd_open(args) -> int:
    rows = _read()
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    ledger_max, file_max = _max_suffix_today(rows, today)
    n = max(ledger_max, file_max) + 1
    bid = f"BM-{today}-{n:02d}"

    # Belt-and-braces: never hand back an id either source already knows.
    # A guard's own v1 is the thing most likely to be wrong
    # [[finding_test_the_guard_not_just_the_guarded]], so this asserts the
    # OUTCOME rather than trusting the arithmetic above.
    taken = {r["batch_id"] for r in rows} | {
        f.name.replace("-manifest.tsv", "")
        for f in LEDGER.parent.glob("BM-*-manifest.tsv")}
    if bid in taken:
        print(f"\u2717 REFUSING TO OPEN {bid} — id already in use "
              f"(ledger_max={ledger_max}, manifest_file_max={file_max}). "
              f"Reconcile the ledger against registry/BM-*-manifest.tsv before opening.")
        return 1
    if file_max > ledger_max:
        print(f"\u26a0 NOTE: {file_max - ledger_max} batch(es) today exist as manifest FILES "
              f"with no ledger row (file_max={file_max} > ledger_max={ledger_max}). "
              f"Id allocated safely above both; backfill those ledger rows when convenient.")
    rows.append({"batch_id": bid, "opened_utc": _now(), "source": args.source,
                 "declared": str(args.open), "dispositioned": "0", "state": "OPEN",
                 "items": "", "notes": args.notes or ""})
    _write(rows)
    print(f"OPENED {bid} — {args.open} item(s) declared")
    print(f"  source: {args.source}")
    print(f"  record each item as you disposition it:")
    print(f"    batch_manifest.py --item {bid} <n> <{'|'.join(sorted(DISPOSITIONS))}> <ref>")
    print(f"  then: batch_manifest.py --close {bid}")
    return 0


def cmd_item(args) -> int:
    bid, num, disp, ref = args.item[0], args.item[1], args.item[2].upper(), " ".join(args.item[3:])
    if disp not in DISPOSITIONS:
        sys.exit(f"unknown disposition {disp!r} — one of {sorted(DISPOSITIONS)}")
    try:
        num_i = int(num)
    except ValueError:
        sys.exit(f"item number must be an integer, got {num!r}")
    rows = _read()
    for r in rows:
        if r["batch_id"] != bid:
            continue
        if r["state"] == "CLOSED":
            sys.exit(f"{bid} is CLOSED — reopen deliberately rather than appending silently")
        items = _items(r)
        declared = int(r["declared"])
        if num_i < 1 or num_i > declared:
            sys.exit(f"item {num_i} is outside the declared range 1..{declared} for {bid}. "
                     f"If the batch was bigger than declared, that is itself the finding — "
                     f"re-open a corrected manifest rather than widening this one silently.")
        if num_i in items:
            print(f"⚠️  item {num_i} already dispositioned as {items[num_i]} — OVERWRITING with {disp}:{ref}")
        items[num_i] = f"{disp}:{ref}" if ref else disp
        r["items"] = ";".join(f"{k}={v}" for k, v in sorted(items.items()))
        r["dispositioned"] = str(len(items))
        _write(rows)
        missing = [i for i in range(1, declared + 1) if i not in items]
        print(f"{bid}: item {num_i} = {disp} ({len(items)}/{declared})")
        if missing:
            print(f"  still un-dispositioned: {missing}")
        else:
            print(f"  ✓ all {declared} accounted for — run --close {bid}")
        return 0
    sys.exit(f"no such batch {bid!r} — run --status")


def cmd_close(args) -> int:
    rows = _read()
    for r in rows:
        if r["batch_id"] != args.close:
            continue
        declared, items = int(r["declared"]), _items(r)
        missing = [i for i in range(1, declared + 1) if i not in items]
        if missing:
            print(f"✗ REFUSING TO CLOSE {r['batch_id']} — {len(missing)} of {declared} "
                  f"un-dispositioned: {missing}")
            print(f"  source: {r['source']}")
            print(f"  Every item needs a disposition, INCLUDING 'nothing to do' — that is what")
            print(f"  NO-ACTION is for. An item silently absent is the exact failure this exists")
            print(f"  to catch (the 7/31 7-image batch: 6 processed, 1 invisible for ~2h).")
            return 1
        r["state"], r["notes"] = "CLOSED", (r["notes"] + f" closed {_now()}").strip()
        _write(rows)
        print(f"✓ CLOSED {r['batch_id']} — {declared}/{declared} dispositioned")
        return 0
    sys.exit(f"no such batch {args.close!r}")


def cmd_status(_) -> int:
    rows = _read()
    if not rows:
        print("no batches recorded")
        print("⚠️  This is NOT evidence that no batch arrived — see the module docstring: "
              "an UNDECLARED batch is invisible to this tool by construction.")
        return 0
    open_rows = [r for r in rows if r["state"] == "OPEN"]
    for r in rows[-10:]:
        declared, items = int(r["declared"]), _items(r)
        missing = [i for i in range(1, declared + 1) if i not in items]
        flag = "✓" if r["state"] == "CLOSED" else ("✗" if missing else "○")
        print(f"{flag} {r['batch_id']}  {r['state']:6}  {len(items)}/{declared}  {r['source'][:60]}")
        if missing:
            print(f"    un-dispositioned: {missing}")
    if open_rows:
        print(f"\n{len(open_rows)} batch(es) OPEN — reconcile before closeout.")
        return 1
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--open", type=int, metavar="N", help="declare a batch of N items")
    g.add_argument("--item", nargs="+", metavar="ARG", help="BATCH_ID N DISPOSITION [ref...]")
    g.add_argument("--close", metavar="BATCH_ID")
    g.add_argument("--status", action="store_true")
    ap.add_argument("--source", default="", help="what the batch was (required with --open)")
    ap.add_argument("--notes", default="")
    args = ap.parse_args()
    if args.open is not None:
        if not args.source:
            sys.exit("--open requires --source (what arrived, and when) — an unlabelled "
                     "manifest row is unauditable a day later")
        if args.open < 1:
            sys.exit("--open N must be >= 1")
        return cmd_open(args)
    if args.item:
        if len(args.item) < 3:
            sys.exit("--item needs at least BATCH_ID N DISPOSITION")
        return cmd_item(args)
    if args.close:
        return cmd_close(args)
    return cmd_status(args)


if __name__ == "__main__":
    sys.exit(main())
