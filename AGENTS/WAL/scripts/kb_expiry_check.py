#!/usr/bin/env python3
"""WAL KB expiry check — read the Stale_By column that nobody was reading.

Born 2026-08-20 (WAL session #3 core-file sweep). `workbook/KB.tsv` has carried a
`Stale_By` column since it was seeded on 2026-03-25. Every row gets a date at
ingest. NOTHING HAS EVER READ IT. Measured at birth: 64 of 177 rows (36%) were
ACTIVE and past their own declared expiry, some by four months.

That is the `finding_dated_carry_item_has_no_expiry_check` class: a carried
assertion is a string, and reading a file never evaluates it.

This does NOT re-date anything and MUST NOT. An expired row needs a judgment —
re-verify, mark SUPERSEDED, or extend with a reason — and bulk-re-dating would
launder exactly the signal this prints. Advisory, read-only, exit 0 always.

Usage:  python3 scripts/kb_expiry_check.py [--kb PATH] [--quiet] [--top N]
"""
import csv, datetime, argparse, sys, os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", default=os.path.join(os.path.dirname(__file__), "..", "workbook", "KB.tsv"))
    ap.add_argument("--quiet", action="store_true", help="one summary line only (boot mode)")
    ap.add_argument("--top", type=int, default=10, help="how many oldest to name")
    a = ap.parse_args()

    if not os.path.exists(a.kb):
        print(f"kb_expiry_check: no KB at {a.kb} — skipped"); return 0
    rows = [r for r in csv.reader(open(a.kb), delimiter="\t") if r and not r[0].startswith("#")]
    if len(rows) < 2:
        print("kb_expiry_check: KB has no data rows"); return 0
    idx = {k: j for j, k in enumerate(rows[0])}
    for col in ("ID", "Status", "Stale_By", "Entity"):
        if col not in idx:
            print(f"kb_expiry_check: KB is missing the {col!r} column — schema changed, check me"); return 0

    today = datetime.date.today()
    expired, blank, live, bad = [], 0, 0, 0
    for r in rows[1:]:
        if len(r) <= max(idx.values()):        # short row: count, never crash
            bad += 1; continue
        if r[idx["Status"]].strip().upper() != "ACTIVE":
            continue
        sb = r[idx["Stale_By"]].strip()
        if not sb:
            blank += 1; continue
        try:
            d = datetime.date.fromisoformat(sb)
        except ValueError:
            bad += 1; continue
        if d < today:
            expired.append((d, r[idx["ID"]], r[idx["Entity"]]))
        else:
            live += 1
    expired.sort()

    total = len(expired) + blank + live
    if a.quiet:
        if expired:
            oldest = (today - expired[0][0]).days
            print(f"⚠️  KB expiry: {len(expired)}/{total} ACTIVE rows past their own Stale_By "
                  f"(oldest {oldest}d) — re-verify, mark SUPERSEDED, or extend WITH A REASON")
        return 0

    print("KB EXPIRY CHECK — the Stale_By column, actually read")
    print("=" * 66)
    print(f"  ACTIVE rows:            {total}")
    pct = f"   ({len(expired) / total * 100:.0f}%)" if total else ""
    print(f"  past their own expiry:  {len(expired)}{'  ⚠️' if expired else '  ✓'}{pct}")
    print(f"  Stale_By blank:         {blank}   (never given an expiry at all)")
    print(f"  still in date:          {live}")
    if bad:
        print(f"  unparseable/short:      {bad}   ← fail-loud, not silently bucketed")
    if expired:
        print(f"\n  oldest {min(a.top, len(expired))} (date · id · entity):")
        for d, i_, e in expired[: a.top]:
            print(f"    {d}  {(today - d).days:>4}d overdue  {i_:<12} {e}")
        print("\n  ⚠️  Do NOT bulk re-date these. Each needs a judgment — re-verify,")
        print("      mark SUPERSEDED, or extend WITH A REASON. Bulk re-dating destroys")
        print("      the only signal this column carries.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
