#!/usr/bin/env python3
"""
OTTO — one-shot backfill of `collection_period` onto workbook/PANEL_10D.tsv.

WHY
  WQ-107 (Will-ruled 2026-09-01, PROME packet 2026-09-01): CARL cannot register OTTO's
  CARL-V2 downgrade-leg table (SIG-W-20260828-004) at the ≤2026-09-10 V2 grade sitting
  until the DISCLOSED collection period is on every panel row. Until 2026-09-02 the
  collection month was inferred as filing_month − 1; that inference produced 8
  collisions and 9 gaps at Exeter's double-filed Dec-2025 / Mar-2026, and a leg table
  registered on an inferred month is exactly the seasonality-mislabel class the panel's
  26-of-26 spec exists to kill.

CONTRACT (same fail-loud rules as panel_10d.py)
  - The period is read from the SERVICER REPORT ITSELF, at `source_url`, keyed on the
    ROW LABEL — never on a tag number (CARL 2026-09-01 §3: tag numbering is unstable
    across shelves and across months on the same deal).
  - NEVER inferred from filing_date / distribution date. A row whose period cannot be
    read is written EMPTY with the reason named in `parse_misses`. An empty cell means
    "not read", never "same month as the filing minus one".
  - POSITIVE CONTROL: the frozen control exhibit must yield its known period before any
    write. Control failure = no write at all.
  - Atomic write via a tmp file; the ledger is never left half-written.
  - Rows already carrying a collection_period are left alone unless --force.

Usage:
  .venv/bin/python3 AGENTS/OTTO/scripts/backfill_collection_period.py --dry-run
  .venv/bin/python3 AGENTS/OTTO/scripts/backfill_collection_period.py
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from panel_10d import (COLUMNS, LEGACY_COLUMNS_14, LEDGER, CONTROL,
                       fetch, flatten, collection_period)

# Frozen control: the same archived exhibit panel_10d.py pins its parser control to.
# Its disclosed period is a property of that fixed document, so this tests the READER
# and never the world.
CONTROL_PERIOD = "2026-05-01/2026-05-31"


def read_ledger():
    rows, legacy = [], 0
    with LEDGER.open() as fh:
        lines = [ln.rstrip("\n") for ln in fh if ln.strip()]
    hdr = lines[0].split("\t")
    body = lines[1:] if hdr[0] == "run_ts" else lines
    for ln in body:
        parts = ln.split("\t")
        if len(parts) == len(LEGACY_COLUMNS_14):
            rec = dict(zip(LEGACY_COLUMNS_14, parts)); rec["collection_period"] = ""
            legacy += 1
        elif len(parts) == len(COLUMNS):
            rec = dict(zip(COLUMNS, parts))
        else:
            raise SystemExit(f"RAGGED ROW ({len(parts)} fields) — refusing to write: {ln[:80]}")
        rows.append(rec)
    return rows, legacy


def main():
    dry = "--dry-run" in sys.argv
    force = "--force" in sys.argv

    print(f"\n{'='*100}\n  OTTO — collection_period backfill on {LEDGER.name}\n{'='*100}")

    print("  POSITIVE CONTROL — frozen exhibit "
          f"({CONTROL['deal']}, {CONTROL['label']}) must read {CONTROL_PERIOD}: ", end="", flush=True)
    got, miss = collection_period(flatten(fetch(CONTROL["url"])))
    if got != CONTROL_PERIOD:
        print(f"**FAIL** (got {got!r}, miss={miss!r}) → nothing written")
        return 1
    print("PASS ✓")

    rows, legacy = read_ledger()
    print(f"  {len(rows)} row(s) read ({legacy} in the legacy 14-col shape).\n")

    # One fetch per DISTINCT source_url — the same exhibit is never pulled twice.
    todo = sorted({r["source_url"] for r in rows
                   if r["source_url"] and (force or not r["collection_period"])})
    print(f"  {len(todo)} distinct exhibit(s) to read.\n")

    cache, failed = {}, []
    for i, url in enumerate(todo, 1):
        try:
            cp, miss = collection_period(flatten(fetch(url)))
        except Exception as e:
            cp, miss = None, f"collection_period-fetch-{type(e).__name__}"
        cache[url] = (cp, miss)
        if cp is None:
            failed.append((url, miss))
        print(f"  [{i:3d}/{len(todo)}] {cp or 'MISS: ' + str(miss)}   {url.rsplit('/',1)[-1]}")

    filled = blank = 0
    for r in rows:
        if r["collection_period"] and not force:
            continue
        cp, miss = cache.get(r["source_url"], (None, "collection_period-no-source_url"))
        if cp:
            r["collection_period"] = cp
            filled += 1
            # a previously-recorded miss for THIS field is now resolved
            r["parse_misses"] = ";".join(
                m for m in r["parse_misses"].split(";")
                if m and not m.startswith("collection_period"))
        else:
            blank += 1
            existing = [m for m in r["parse_misses"].split(";") if m]
            if miss not in existing:
                existing.append(miss)
            r["parse_misses"] = ";".join(existing)

    # ── Off-cadence audit: what the OLD inference would have got wrong ────────
    infer_bad = collisions = 0
    by_deal = {}
    for r in rows:
        if not r["collection_period"]:
            continue
        fy, fm = int(r["filing_date"][:4]), int(r["filing_date"][5:7])
        im = (fy, fm - 1) if fm > 1 else (fy - 1, 12)          # the retired inference
        actual = (int(r["collection_period"][:4]), int(r["collection_period"][5:7]))
        if im != actual:
            infer_bad += 1
        by_deal.setdefault(r["deal"], []).append(actual)
    for deal, months in by_deal.items():
        collisions += len(months) - len(set(months))

    print(f"\n  filled {filled} · left blank {blank} · "
          f"rows where filing_month−1 ≠ disclosed month: {infer_bad} · "
          f"same-deal duplicate collection months: {collisions}")
    if failed:
        print(f"  ⚠ {len(failed)} exhibit(s) unreadable — left EMPTY, reason in parse_misses:")
        for u, m in failed:
            print(f"      {m}  {u}")

    if dry:
        print("\n  [--dry-run] nothing written\n")
        return 0

    tmp = LEDGER.with_suffix(".tsv.tmp")
    with tmp.open("w") as fh:
        fh.write("\t".join(COLUMNS) + "\n")
        for r in rows:
            fh.write("\t".join(r.get(c, "") for c in COLUMNS) + "\n")
    os.replace(tmp, LEDGER)
    print(f"\n  {LEDGER.name}: {len(rows)} row(s) written, {len(COLUMNS)} columns.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
